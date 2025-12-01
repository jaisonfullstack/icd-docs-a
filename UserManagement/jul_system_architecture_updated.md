# JUL Single Window - System Architecture & Diagrams
## Focus: User Management & Company Registration

## 1. High-Level System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         JUL SINGLE WINDOW SYSTEM                             │
│                        (LPCO Angola - Port Community)                        │
│                   Focus: User Management & Company Registration              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                           EXTERNAL USERS & PORTALS                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │  Public Portal   │  │ Company Portal   │  │  Admin Portals   │          │
│  │ (Registration)   │  │  (User Mgmt)     │  │  (Management)    │          │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘          │
│           │                     │                      │                    │
│           └─────────────────────┴──────────────────────┘                    │
│                                  │                                          │
└──────────────────────────────────┼──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ANGULAR FRONTEND LAYER                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    AUTHENTICATION FLOW                              │    │
│  │  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐           │    │
│  │  │  LDAP Auth   │   │   SSO Auth   │   │ Standalone   │           │    │
│  │  │  (External)  │   │  (External)  │   │   Security   │           │    │
│  │  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘           │    │
│  │         │                  │                  │                    │    │
│  │         └──────────────────┴──────────────────┘                    │    │
│  │                            │                                       │    │
│  │                            ▼                                       │    │
│  │                   ┌─────────────────┐                             │    │
│  │                   │  KEYCLOAK IDP   │                             │    │
│  │                   │  (Auth Server)  │                             │    │
│  │                   └────────┬────────┘                             │    │
│  │                            │                                       │    │
│  │                   ┌────────▼────────┐                             │    │
│  │                   │  Access Token   │                             │    │
│  │                   │   + JWT Claims  │                             │    │
│  │                   └────────┬────────┘                             │    │
│  └─────────────────────────────┼──────────────────────────────────────┘    │
│                                │                                           │
│                                ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────┐      │
│  │                      API GATEWAY                                 │      │
│  │  ┌────────────────────────────────────────────────────────┐     │      │
│  │  │  Adapter Library (Token Validation & Enrichment)       │     │      │
│  │  │  • Validate JWT Token                                  │     │      │
│  │  │  • Get User/Groups from Keycloak                       │     │      │
│  │  │  • Fetch Roles & Permissions (with Cache)              │     │      │
│  │  │  • Create Internal JWT (include permissions)           │     │      │
│  │  │  • Log user session                                    │     │      │
│  │  └────────────────────────────────────────────────────────┘     │      │
│  │                                                                  │      │
│  │  ┌────────────────────────────────────────────────────────┐     │      │
│  │  │  Authorization Layer                                   │     │      │
│  │  │  • Check access endpoint                               │     │      │
│  │  │  • Config backlist                                     │     │      │
│  │  │  • ACL validation                                      │     │      │
│  │  └────────────────────────────────────────────────────────┘     │      │
│  └──────────────────────────────┬───────────────────────────────────┘      │
└─────────────────────────────────┼──────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      BACKEND MICROSERVICES (.NET)                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │   Company Mgmt   │  │   User Mgmt      │  │  Dashboard Svc   │          │
│  │   Microservice   │  │   Microservice   │  │   (Analytics)    │          │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘          │
│           │                     │                      │                    │
│           └─────────────────────┴──────────────────────┘                    │
│                                 │                                           │
│                   ┌─────────────┴─────────────┐                             │
│                   │    RabbitMQ Message Bus   │                             │
│                   └─────────────┬─────────────┘                             │
└─────────────────────────────────┼──────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATA LAYER                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────┐      │
│  │              PostgreSQL Database (Multi-tenant)                  │      │
│  │  ┌────────────────────┐  ┌────────────────────┐                 │      │
│  │  │  companies table   │  │   users table      │                 │      │
│  │  │  ───────────────   │  │   ────────────     │                 │      │
│  │  │  • company_id (PK) │  │   • user_id (PK)   │                 │      │
│  │  │  • keycloak_group  │  │   • company_id     │                 │      │
│  │  │  • company_name    │  │   • email          │                 │      │
│  │  │  • company_type    │  │   • keycloak_uuid  │                 │      │
│  │  │  • license_number  │  │   • status         │                 │      │
│  │  │  • tax_id          │  │   • created_at     │                 │      │
│  │  │  • approval_status │  │   • department_id  │                 │      │
│  │  │  • created_by      │  │                    │                 │      │
│  │  │  • approved_by     │  │                    │                 │      │
│  │  └────────────────────┘  └────────────────────┘                 │      │
│  │                                                                  │      │
│  │  ┌────────────────────┐  ┌────────────────────┐                 │      │
│  │  │  departments table │  │  company_docs      │                 │      │
│  │  │  (subgroups)       │  │  table             │                 │      │
│  │  └────────────────────┘  └────────────────────┘                 │      │
│  └──────────────────────────────────────────────────────────────────┘      │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────┐      │
│  │                     Keycloak Database                             │      │
│  │  • Users, Groups, Roles, Permissions                             │      │
│  │  • Group Attributes (mapped to company_id)                       │      │
│  │  • Session Management                                            │      │
│  └──────────────────────────────────────────────────────────────────┘      │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────┐      │
│  │                     Redis Cache                                   │      │
│  │  • Roles & Permissions Cache                                     │      │
│  │  • User Session Cache                                            │      │
│  │  • ACL Cache                                                     │      │
│  └──────────────────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Company Registration & User Onboarding Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMPANY REGISTRATION WORKFLOW                             │
└─────────────────────────────────────────────────────────────────────────────┘

PHASE 1: PUBLIC PORTAL - COMPANY REGISTRATION
══════════════════════════════════════════════

    ┌─────────────────┐
    │  New Company    │
    │  (Unregistered) │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  Public Portal - Registration Form  │
    │  ─────────────────────────────────  │
    │  STEP 1: Company Information        │
    │  • Company Name                     │
    │  • Company Type (dropdown)          │
    │    - Trader                         │
    │    - Customs Broker                 │
    │    - Freight Forwarder              │
    │  • Trade License Number             │
    │  • Tax ID (NIF)                     │
    │  • Business Address                 │
    │  • Contact Email & Phone            │
    │  • Supporting Documents Upload      │
    │    - Trade License (PDF)            │
    │    - Tax Certificate                │
    │    - Business Registration          │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  STEP 2: Primary User Registration  │
    │  ─────────────────────────────────  │
    │  • First Name, Last Name            │
    │  • Email (username)                 │
    │  • Phone Number                     │
    │  • Job Title                        │
    │  • Password                         │
    │  • Confirm Password                 │
    │  • Authorized Representative? (Y/N) │
    │  • ID Document Upload               │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  STEP 3: Secondary Users (Optional) │
    │  ─────────────────────────────────  │
    │  Add up to 5 secondary users        │
    │  • Name, Email, Phone, Job Title    │
    │  • Intended Role (Manager/User)     │
    │  (They will receive invite email)   │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  STEP 4: Review & Submit            │
    │  ─────────────────────────────────  │
    │  • Review all information           │
    │  • Accept Terms & Conditions        │
    │  • Submit Application               │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  BACKEND: Process Registration      │
    │  ─────────────────────────────────  │
    │  1. Create company in PostgreSQL    │
    │     • status = 'pending_approval'   │
    │     • approval_status = 'submitted' │
    │  2. Store uploaded documents        │
    │  3. Create Keycloak user (disabled) │
    │  4. Send notification to ARCCLA     │
    │  5. Send confirmation email         │
    │     to primary user                 │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  Registration Submitted             │
    │  ─────────────────────────────────  │
    │  Status: Pending ARCCLA Approval    │
    │  Reference Number: REG-2024-00123   │
    │  Notification sent to:              │
    │  - Primary User Email               │
    │  - ARCCLA Admin Dashboard           │
    └─────────────────────────────────────┘


PHASE 2: ARCCLA ADMIN - APPROVAL WORKFLOW
══════════════════════════════════════════

    ┌─────────────────────────────────────┐
    │  ARCCLA Admin Portal                │
    │  (Angola Government Authority)      │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  View Pending Company Registrations │
    │  ─────────────────────────────────  │
    │  List of all pending companies      │
    │  • REG-2024-00123 - Maersk Angola   │
    │  • REG-2024-00124 - XYZ Brokers     │
    │  • REG-2024-00125 - ABC Logistics   │
    │  ─────────────────────────────────  │
    │  [View Details] for each company    │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  Company Details Review Screen      │
    │  ─────────────────────────────────  │
    │  COMPANY INFO:                      │
    │  • Company Name: Maersk Angola      │
    │  • Type: Trading Company            │
    │  • License: TR-2024-001             │
    │  • Tax ID: 5401234567               │
    │  • Documents: [View PDFs]           │
    │                                     │
    │  PRIMARY USER:                      │
    │  • Carlos Ferreira                  │
    │  • carlos@maersk.com                │
    │  • Job: Import Operations Manager   │
    │                                     │
    │  SECONDARY USERS (2):               │
    │  • Maria Costa - Coordinator        │
    │  • João Silva - Clerk               │
    │                                     │
    │  VALIDATION CHECKS:                 │
    │  ✓ Trade License Valid              │
    │  ✓ Tax ID Verified                  │
    │  ✓ Documents Complete               │
    └────────┬────────────────────────────┘
             │
             ▼
        ┌────┴────┐
        │ APPROVE │ REJECT
        │    ?    │
        └────┬────┘
             │
        ┌────┴─────┐
        │          │
        ▼          ▼
    APPROVE     REJECT
        │          │
        │          └──────────────────────┐
        │                                 │
        ▼                                 ▼
┌───────────────────────┐      ┌──────────────────────┐
│ APPROVE WORKFLOW      │      │ REJECT WORKFLOW      │
│ ────────────────      │      │ ───────────────      │
│ 1. Update company:    │      │ 1. Update company:   │
│    • status='active'  │      │    • status='reject' │
│    • approved_by      │      │    • rejection_reason│
│    • approved_at      │      │    • rejected_by     │
│                       │      │    • rejected_at     │
│ 2. Create Keycloak:   │      │                      │
│    • Create Group     │      │ 2. Send rejection    │
│      org-maersk-angola│      │    email to primary  │
│    • Set attributes   │      │    user with reason  │
│      - company_id     │      │                      │
│      - company_type   │      │ 3. Disable Keycloak  │
│    • Create subdepts  │      │    user (if created) │
│                       │      │                      │
│ 3. Enable primary user│      └──────────────────────┘
│    in Keycloak        │
│    • Enable account   │
│    • Add to group     │
│    • Assign default   │
│      role.trader-mgr  │
│                       │
│ 4. Send invite emails │
│    to secondary users │
│    with setup link    │
│                       │
│ 5. Send welcome email │
│    to primary user    │
│    with login details │
└───────────────────────┘


PHASE 3: COMPANY ADMIN - USER MANAGEMENT
═════════════════════════════════════════

    ┌─────────────────────────────────────┐
    │  Primary User (Company Admin)       │
    │  carlos@maersk.com                  │
    │  role.trader-manager                │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  Company Portal - User Management   │
    │  ─────────────────────────────────  │
    │  MY COMPANY USERS:                  │
    │  ┌───────────────────────────────┐  │
    │  │ Carlos Ferreira (Admin)       │  │
    │  │ • role.trader-manager         │  │
    │  │ • Status: Active              │  │
    │  │ [View] [Edit] [Deactivate]    │  │
    │  └───────────────────────────────┘  │
    │                                     │
    │  ┌───────────────────────────────┐  │
    │  │ Maria Costa                   │  │
    │  │ • Status: Invite Pending      │  │
    │  │ [Resend Invite] [Cancel]      │  │
    │  └───────────────────────────────┘  │
    │                                     │
    │  [+ Add New User]                   │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  Add New User Form                  │
    │  ─────────────────────────────────  │
    │  • Email                            │
    │  • First Name, Last Name            │
    │  • Phone Number                     │
    │  • Job Title                        │
    │  • Assign Role (dropdown):          │
    │    - role.trader-manager            │
    │    - role.trader-user               │
    │  • Department (dropdown):           │
    │    - Import Operations              │
    │    - Export Operations              │
    │  • Authorized Representative? (Y/N) │
    │                                     │
    │  [Send Invitation]                  │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  BACKEND: User Creation             │
    │  ─────────────────────────────────  │
    │  1. Create user in PostgreSQL       │
    │     • company_id (from admin)       │
    │     • status = 'invite_sent'        │
    │                                     │
    │  2. Create Keycloak user            │
    │     • Set temporary password        │
    │     • Add to company group          │
    │     • Add to department subgroup    │
    │     • Assign selected role          │
    │     • Enabled = false (until setup) │
    │                                     │
    │  3. Send invitation email           │
    │     • Setup link with token         │
    │     • Expires in 7 days             │
    └────────┬────────────────────────────┘
             │
             ▼
    ┌─────────────────────────────────────┐
    │  New User - Account Setup           │
    │  ─────────────────────────────────  │
    │  maria@maersk.com clicks link       │
    │                                     │
    │  1. Verify invitation token         │
    │  2. Set permanent password          │
    │  3. Complete profile                │
    │  4. Accept terms                    │
    │  5. Enable Keycloak account         │
    │  6. Update status = 'active'        │
    │  7. Send welcome email              │
    └─────────────────────────────────────┘


PHASE 4: USER MANAGEMENT OPERATIONS
════════════════════════════════════

    ┌─────────────────────────────────────┐
    │  Company Admin Operations           │
    │  ─────────────────────────────────  │
    │                                     │
    │  ACTIVATE USER:                     │
    │  • Enable disabled user account     │
    │  • Update status in PostgreSQL      │
    │  • Enable in Keycloak               │
    │  • Send activation email            │
    │                                     │
    │  DEACTIVATE USER:                   │
    │  • Disable user account             │
    │  • Update status in PostgreSQL      │
    │  • Disable in Keycloak              │
    │  • Revoke active sessions           │
    │  • Send notification email          │
    │                                     │
    │  EDIT USER:                         │
    │  • Update user details              │
    │  • Change department                │
    │  • Update job title                 │
    │  • Modify contact info              │
    │                                     │
    │  ASSIGN ROLES:                      │
    │  • Change user role                 │
    │  • Update in Keycloak               │
    │  • Invalidate permission cache      │
    │  • User gets new permissions        │
    │    on next login                    │
    │                                     │
    │  VIEW USER ACTIVITY:                │
    │  • Last login time                  │
    │  • Login history                    │
    │  • Activity logs                    │
    └─────────────────────────────────────┘
```

---

## 3. Admin Portal Structure & Permissions

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        THREE ADMIN PORTALS                                   │
└─────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════════════════╗
║  ADMIN 1: SUPER ADMIN (System Administrator)                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Role: role.super-admin                                                    ║
║  Scope: ENTIRE REALM (lpco-angola-system)                                  ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────┐    ║
║  │  RESPONSIBILITIES:                                                │    ║
║  │  ════════════════                                                 │    ║
║  │  1. KEYCLOAK CONFIGURATION                                        │    ║
║  │     • Create & manage Realm Roles                                 │    ║
║  │       - permission.view, .create, .edit, etc.                     │    ║
║  │     • Create & manage Client Roles                                │    ║
║  │       - user-management.*, dashboard.*, etc.                      │    ║
║  │     • Create Composite Roles                                      │    ║
║  │       - role.trader-manager                                       │    ║
║  │       - role.customs-broker-manager                               │    ║
║  │       - role.freight-forwarder-manager                            │    ║
║  │     • Configure Client Scopes                                     │    ║
║  │     • Configure Authentication Flows                              │    ║
║  │                                                                    │    ║
║  │  2. GROUP TEMPLATES & STRUCTURE                                   │    ║
║  │     • Define group hierarchy templates                            │    ║
║  │     • Set default group attributes schema                         │    ║
║  │     • Create department templates                                 │    ║
║  │                                                                    │    ║
║  │  3. SYSTEM CONFIGURATION                                          │    ║
║  │     • Configure ACL rules                                         │    ║
║  │     • Manage API Gateway settings                                 │    ║
║  │     • Configure adapter libraries                                 │    ║
║  │     • Set up authentication methods                               │    ║
║  │       - LDAP configuration                                        │    ║
║  │       - SSO integration                                           │    ║
║  │                                                                    │    ║
║  │  4. MONITORING & AUDIT                                            │    ║
║  │     • View all system logs                                        │    ║
║  │     • Monitor user sessions                                       │    ║
║  │     • Security audit reports                                      │    ║
║  │     • Performance monitoring                                      │    ║
║  └──────────────────────────────────────────────────────────────────┘    ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────┐    ║
║  │  MENU STRUCTURE:                                                  │    ║
║  │  ══════════════                                                   │    ║
║  │  📁 Roles & Permissions                                           │    ║
║  │     • Realm Roles Management                                      │    ║
║  │     • Client Roles Management                                     │    ║
║  │     • Composite Roles Builder                                     │    ║
║  │     • Permission Matrix View                                      │    ║
║  │                                                                    │    ║
║  │  📁 Groups & Organizations                                        │    ║
║  │     • Group Templates                                             │    ║
║  │     • Department Templates                                        │    ║
║  │     • Attribute Schemas                                           │    ║
║  │                                                                    │    ║
║  │  📁 System Configuration                                          │    ║
║  │     • Authentication Settings                                     │    ║
║  │     • API Gateway Config                                          │    ║
║  │     • ACL Rules Manager                                           │    ║
║  │     • Adapter Library Settings                                    │    ║
║  │                                                                    │    ║
║  │  📁 Monitoring & Reports                                          │    ║
║  │     • System Logs                                                 │    ║
║  │     • User Activity                                               │    ║
║  │     • Security Audit                                              │    ║
║  │     • Performance Metrics                                         │    ║
║  └──────────────────────────────────────────────────────────────────┘    ║
╚═══════════════════════════════════════════════════════════════════════════╝


╔═══════════════════════════════════════════════════════════════════════════╗
║  ADMIN 2: ARCCLA ADMIN (Angola Government Authority)                      ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Role: role.arccla-admin                                                   ║
║  Scope: ALL COMPANIES (Government Oversight)                               ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────┐    ║
║  │  RESPONSIBILITIES:                                                │    ║
║  │  ════════════════                                                 │    ║
║  │  1. COMPANY APPROVALS                                             │    ║
║  │     • Review company registrations                                │    ║
║  │     • Verify trade licenses                                       │    ║
║  │     • Validate tax documents                                      │    ║
║  │     • Approve/Reject companies                                    │    ║
║  │     • Suspend/Revoke company licenses                             │    ║
║  │                                                                    │    ║
║  │  2. USER AUTHORIZATION APPROVAL                                   │    ║
║  │     • Review "Authorized Representative" requests                 │    ║
║  │     • Approve signing authority                                   │    ║
║  │     • Manage authorized user list                                 │    ║
║  │                                                                    │    ║
║  │  3. COMPANY OVERSIGHT                                             │    ║
║  │     • View all company profiles                                   │    ║
║  │     • Monitor company users                                       │    ║
║  │     • View company activity logs                                  │    ║
║  │                                                                    │    ║
║  │  4. COMPLIANCE & CONTROL                                          │    ║
║  │     • Monitor company activities                                  │    ║
║  │     • Generate compliance reports                                 │    ║
║  │     • Manage blacklist/whitelist                                  │    ║
║  │     • Enforce regulatory policies                                 │    ║
║  └──────────────────────────────────────────────────────────────────┘    ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────┐    ║
║  │  MENU STRUCTURE:                                                  │    ║
║  │  ══════════════                                                   │    ║
║  │  📁 Company Management                                            │    ║
║  │     • Pending Registrations                                       │    ║
║  │     • Approved Companies                                          │    ║
║  │     • Rejected Companies                                          │    ║
║  │     • Suspended Companies                                         │    ║
║  │     • Company Details & Documents                                 │    ║
║  │                                                                    │    ║
║  │  📁 User Authorization                                            │    ║
║  │     • Pending Authorization Requests                              │    ║
║  │     • Approved Representatives                                    │    ║
║  │     • Authorization History                                       │    ║
║  │                                                                    │    ║
║  │  📁 Reports & Analytics                                           │    ║
║  │     • Company Statistics                                          │    ║
║  │     • User Statistics                                             │    ║
║  │     • Compliance Reports                                          │    ║
║  │     • Activity Reports                                            │    ║
║  │                                                                    │    ║
║  │  📁 Compliance & Control                                          │    ║
║  │     • Blacklist Management                                        │    ║
║  │     • Whitelist Management                                        │    ║
║  │     • Policy Enforcement                                          │    ║
║  │     • Audit Logs                                                  │    ║
║  └──────────────────────────────────────────────────────────────────┘    ║
╚═══════════════════════════════════════════════════════════════════════════╝


╔═══════════════════════════════════════════════════════════════════════════╗
║  ADMIN 3: COMPANY ADMIN (Company User Manager)                            ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  Role: role.trader-manager / role.customs-broker-manager /                 ║
║        role.freight-forwarder-manager                                      ║
║  Scope: OWN COMPANY ONLY                                                   ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────┐    ║
║  │  RESPONSIBILITIES:                                                │    ║
║  │  ════════════════                                                 │    ║
║  │  1. USER MANAGEMENT (Company Users Only)                          │    ║
║  │     • Add new users to company                                    │    ║
║  │     • Edit user details                                           │    ║
║  │     • Assign roles to users                                       │    ║
║  │       - Can only assign roles within their company type           │    ║
║  │       - e.g., trader-manager can assign:                          │    ║
║  │         * role.trader-manager                                     │    ║
║  │         * role.trader-user                                        │    ║
║  │     • Activate/Deactivate users                                   │    ║
║  │     • Resend invitation emails                                    │    ║
║  │     • View user activity logs                                     │    ║
║  │                                                                    │    ║
║  │  2. DEPARTMENT MANAGEMENT                                         │    ║
║  │     • Create departments (subgroups)                              │    ║
║  │     • Assign users to departments                                 │    ║
║  │     • Manage department structure                                 │    ║
║  │                                                                    │    ║
║  │  3. COMPANY PROFILE                                               │    ║
║  │     • Update company information                                  │    ║
║  │     • Manage company documents                                    │    ║
║  │     • View company statistics                                     │    ║
║  └──────────────────────────────────────────────────────────────────┘    ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────┐    ║
║  │  MENU STRUCTURE:                                                  │    ║
║  │  ══════════════                                                   │    ║
║  │  📁 User Management                                               │    ║
║  │     • All Company Users                                           │    ║
║  │     • Add New User                                                │    ║
║  │     • Pending Invitations                                         │    ║
║  │     • Active Users                                                │    ║
║  │     • Inactive Users                                              │    ║
║  │     • User Activity Logs                                          │    ║
║  │                                                                    │    ║
║  │  📁 Department Management                                         │    ║
║  │     • All Departments                                             │    ║
║  │     • Create Department                                           │    ║
║  │     • Assign Users to Departments                                 │    ║
║  │                                                                    │    ║
║  │  📁 Company Dashboard                                             │    ║
║  │     • Company Statistics                                          │    ║
║  │     • User Activity Summary                                       │    ║
║  │     • Recent Notifications                                        │    ║
║  │                                                                    │    ║
║  │  📁 Company Profile                                               │    ║
║  │     • Company Information                                         │    ║
║  │     • Update Company Details                                      │    ║
║  │     • Manage Documents                                            │    ║
║  │     • Contact Information                                         │    ║
║  └──────────────────────────────────────────────────────────────────┘    ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## 4. Keycloak & PostgreSQL Integration

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            KEYCLOAK & POSTGRESQL INTEGRATION ARCHITECTURE                    │
└─────────────────────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════════════════╗
║                          DATA SYNCHRONIZATION                              ║
╚═══════════════════════════════════════════════════════════════════════════╝

┌────────────────────────────┐          ┌────────────────────────────┐
│   KEYCLOAK DATABASE        │          │   POSTGRESQL DATABASE      │
│   (Authentication & IAM)   │          │   (Business Data)          │
└─────────────┬──────────────┘          └──────────────┬─────────────┘
              │                                        │
              │                                        │
              ▼                                        ▼
┌──────────────────────────────────────────────────────────────────────┐
│                       MAPPING RELATIONSHIP                            │
│                                                                       │
│  KEYCLOAK                           POSTGRESQL                        │
│  ═════════                          ══════════                        │
│                                                                       │
│  Users Table:                       users table:                      │
│  • id (UUID)          ─────────────▶• keycloak_uuid                  │
│  • username (email)   ─────────────▶• email                          │
│  • firstName          ─────────────▶• first_name                     │
│  • lastName           ─────────────▶• last_name                      │
│  • enabled            ─────────────▶• status (active/inactive)       │
│  • attributes         ─────────────▶• user_attributes (JSONB)        │
│    - phone                             - phone                        │
│    - job_title                         - job_title                    │
│    - authorized_to_sign                - authorized_to_sign           │
│                                                                       │
│  Groups Table:                      companies table:                  │
│  • id (UUID)          ─────────────▶• keycloak_group_id              │
│  • name               ─────────────▶• company_id (slug)              │
│    (org-maersk-angola)                 (maersk-angola)                │
│  • attributes:        ─────────────▶• company_name                   │
│    - org_name                          (Maersk Angola Lda)            │
│    - org_type         ─────────────▶• company_type                   │
│    - company_type                      (trading-company)              │
│    - license_number   ─────────────▶• license_number                 │
│    - tax_id           ─────────────▶• tax_id                         │
│                                     • approval_status                 │
│                                     • created_at                      │
│                                     • approved_at                     │
│                                                                       │
│  User-Group Membership:             user-company relationship:        │
│  • user_id            ─────────────▶• user_id (FK)                   │
│  • group_id           ─────────────▶• company_id (FK)                │
│                                                                       │
│  Roles (via composite):             Stored in Keycloak only           │
│  • realm roles                      (cached in Redis)                 │
│  • client roles                                                       │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘


╔═══════════════════════════════════════════════════════════════════════════╗
║                     COMPANY CREATION WORKFLOW                              ║
╚═══════════════════════════════════════════════════════════════════════════╝

WHEN ARCCLA APPROVES A COMPANY:

STEP 1: PostgreSQL Database Update
───────────────────────────────────
UPDATE companies 
SET 
  approval_status = 'approved',
  status = 'active',
  approved_by = 'arccla-admin-uuid',
  approved_at = NOW()
WHERE company_id = 'maersk-angola';


STEP 2: Keycloak Group Creation via Admin API
──────────────────────────────────────────────
POST /auth/admin/realms/lpco-angola-system/groups
{
  "name": "org-maersk-angola",
  "attributes": {
    "org_id": ["maersk-angola"],
    "org_type": ["trader"],
    "org_name": ["Maersk Angola Lda"],
    "company_type": ["trading-company"],
    "license_number": ["TR-2024-001"],
    "tax_id": ["5401234567"],
    "status": ["active"],
    "registration_date": ["2024-01-15"],
    "contact_email": ["info@maersk.ao"],
    "contact_phone": ["+244 222 123 456"],
    "address": ["Luanda, Angola"]
  }
}

Response: { "id": "group-uuid-12345" }


STEP 3: Update PostgreSQL with Keycloak Group ID
─────────────────────────────────────────────────
UPDATE companies 
SET keycloak_group_id = 'group-uuid-12345'
WHERE company_id = 'maersk-angola';


STEP 4: Create Subgroups (Departments)
───────────────────────────────────────
POST /auth/admin/realms/lpco-angola-system/groups/{group-uuid-12345}/children
{
  "name": "dept-import-operations",
  "attributes": {
    "dept_id": ["maersk-import"],
    "dept_name": ["Import Operations"],
    "dept_code": ["IMP"]
  }
}

POST /auth/admin/realms/lpco-angola-system/groups/{group-uuid-12345}/children
{
  "name": "dept-export-operations",
  "attributes": {
    "dept_id": ["maersk-export"],
    "dept_name": ["Export Operations"],
    "dept_code": ["EXP"]
  }
}


STEP 5: Enable Primary User & Add to Group
───────────────────────────────────────────
// Enable user
PUT /auth/admin/realms/lpco-angola-system/users/{user-uuid}/
{
  "enabled": true
}

// Add user to company group
PUT /auth/admin/realms/lpco-angola-system/users/{user-uuid}/groups/{group-uuid-12345}

// Assign role
POST /auth/admin/realms/lpco-angola-system/users/{user-uuid}/role-mappings/realm
[
  {
    "id": "role-trader-manager-uuid",
    "name": "role.trader-manager"
  }
]


STEP 6: Update PostgreSQL User Record
──────────────────────────────────────
UPDATE users 
SET 
  status = 'active',
  company_id = (SELECT id FROM companies WHERE company_id = 'maersk-angola'),
  activated_at = NOW()
WHERE keycloak_uuid = 'user-uuid';


╔═══════════════════════════════════════════════════════════════════════════╗
║                     USER CREATION WORKFLOW (by Company Admin)             ║
╚═══════════════════════════════════════════════════════════════════════════╝

WHEN COMPANY ADMIN ADDS A NEW USER:

STEP 1: Create in PostgreSQL First
───────────────────────────────────
INSERT INTO users (
  company_id,
  email,
  first_name,
  last_name,
  phone,
  job_title,
  status,
  created_by,
  created_at
) VALUES (
  (SELECT id FROM companies WHERE company_id = 'maersk-angola'),
  'maria@maersk.com',
  'Maria',
  'Costa',
  '+244 222 123 002',
  'Import Coordinator',
  'invite_sent',
  'carlos-uuid',
  NOW()
)
RETURNING id, company_id;


STEP 2: Create Keycloak User
─────────────────────────────
POST /auth/admin/realms/lpco-angola-system/users
{
  "username": "maria@maersk.com",
  "email": "maria@maersk.com",
  "firstName": "Maria",
  "lastName": "Costa",
  "enabled": false,  // Will be enabled after setup
  "emailVerified": false,
  "attributes": {
    "phone": ["+244 222 123 002"],
    "job_title": ["Import Coordinator"],
    "company_id": ["maersk-angola"],
    "authorized_to_sign": ["false"],
    "created_by": ["carlos@maersk.com"]
  },
  "credentials": [{
    "type": "password",
    "value": "temporary-password-12345",
    "temporary": true
  }]
}

Response: { "id": "new-user-uuid-67890" }


STEP 3: Update PostgreSQL with Keycloak UUID
─────────────────────────────────────────────
UPDATE users 
SET keycloak_uuid = 'new-user-uuid-67890'
WHERE email = 'maria@maersk.com';


STEP 4: Add User to Company Group
──────────────────────────────────
PUT /auth/admin/realms/lpco-angola-system/users/new-user-uuid-67890/groups/group-uuid-12345


STEP 5: Assign Role
───────────────────
POST /auth/admin/realms/lpco-angola-system/users/new-user-uuid-67890/role-mappings/realm
[
  {
    "id": "role-trader-user-uuid",
    "name": "role.trader-user"
  }
]


STEP 6: Send Invitation Email
──────────────────────────────
// Generate invitation token
token = generate_invitation_token(user_id, expires_in_days=7)

// Send email with setup link
send_email({
  to: "maria@maersk.com",
  subject: "Welcome to JUL Single Window",
  body: `
    Hello Maria,
    
    You have been invited to join Maersk Angola on JUL Single Window.
    
    Please click the link below to complete your account setup:
    https://jul.angola.gov.ao/setup?token=${token}
    
    This link will expire in 7 days.
  `
})
```