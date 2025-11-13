# JUL-SINTECE Integration Control Document

<style>
@media print {
  .page-break { page-break-before: always; }
  .no-print { display: none; }
}

.highlight-box {
  background-color: #f8f9fa;
  padding: 15px;
  border-left: 4px solid #007bff;
  margin: 10px 0;
  border-radius: 5px;
}

.success-box {
  background-color: #d4edda;
  padding: 15px;
  border-left: 4px solid #28a745;
  margin: 10px 0;
  border-radius: 5px;
}

.warning-box {
  background-color: #fff3cd;
  padding: 15px;
  border-left: 4px solid #ffc107;
  margin: 10px 0;
  border-radius: 5px;
}

.info-box {
  background-color: #d1ecf1;
  padding: 15px;
  border-left: 4px solid #17a2b8;
  margin: 10px 0;
  border-radius: 5px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 15px 0;
}

table th, table td {
  border: 1px solid #dee2e6;
  padding: 8px;
  text-align: left;
}

table th {
  background-color: #f8f9fa;
  font-weight: bold;
}

code {
  background-color: #f8f9fa;
  padding: 2px 4px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
}

pre {
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 5px;
  overflow-x: auto;
  border-left: 4px solid #007bff;
}

/* Process Flow Image Styling */
.process-flow-container {
  text-align: center;
  margin: 20px 0;
  page-break-inside: avoid;
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  border: 2px solid #dee2e6;
}

.process-flow-container img {
  width: 100%;
  max-width: 100%;
  height: auto;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.process-flow-container p {
  font-style: italic;
  margin-top: 15px;
  color: #666;
  font-weight: 500;
  font-size: 14px;
}
</style>

<div style="text-align: center; padding: 20px 0;">
<img src="./images/JUL-logo.png" alt="JUL Logo" style="height: 60px; margin: 0 15px;" />
<img src="./images/Maqta-logo.png" alt="Abu Dhabi Ports Logo" style="height: 60px; margin: 0 15px;" />
</div>

<div style="text-align: center; border: 2px solid #2E5BBA; padding: 20px; margin: 20px 0; background-color: #f8f9fa;">

## CNCA Certificate Issuance Process
### Amendment and Cancellation Capabilities

**Version 2.0**  
**Abu Dhabi Ports**  
**November 13, 2025**

</div>

---

<div style="page-break-before: always;"></div>

## 📋 Document Control

| **Field** | **Value** |
|-----------|-----------|
| **Document Title** | JUL-SINTECE Integration Control Document |
| **Project Name** | JUL System Integration with SINTECE - CNCA Certificate Process |
| **Document ID** | ICD-JUL-SINTECE-002 |
| **Version** | 2.0 |
| **Organization** | Abu Dhabi Ports |
| **Date** | November 13, 2025 |
| **Status** | Draft for Review |
| **Classification** | Internal Use |
| **Author** | Abu Dhabi Ports Integration Team |
| **Scope** | CNCA Certificate Issuance Process Integration with Amendment and Cancellation Workflows |

---

## 📝 Version History

| **Version** | **Date** | **Author** | **Description of Changes** |
|-------------|----------|------------|----------------------------|
| 1.0 | 2025-11-12 | Abu Dhabi Ports | Initial ICD creation with technical specifications for JUL-SINTECE integration. Defined API specifications, data models, integration workflows, security requirements, and testing procedures. |
| 2.0 | 2025-11-13 | Abu Dhabi Ports | Added amendment and cancellation APIs, approval workflows, status management with canAmend/canCancel flags, validation framework, and error handling. Added process flow improvements and implementation recommendations. |

---

<div style="page-break-before: always;"></div>

## 📑 Table of Contents

**1. [Introduction](#1-introduction)** 📖
- 1.1 Purpose
- 1.2 Scope  
- 1.3 Audience
- 1.4 Definitions

**2. [System Overview](#2-system-overview)** 🏗️
- 2.1 System Architecture
- 2.2 Integration Pattern
- 2.3 System Actors
- 2.4 Amendment and Cancellation Capabilities

**3. [Process Flows](#3-process-flows)** 🔄
- 3.1 As-Is Process Analysis
  - 3.1.1 Current State Process Flow Diagram
- 3.2 To-Be Process
  - 3.2.1 Future State Process Flow Diagram
- 3.3 Integration Touchpoints
  - 3.3.1 API Integration Architecture Diagram
- 3.4 Amendment Workflow Process
  - 3.4.1 Amendment Workflow Diagram
- 3.5 Cancellation Workflow Process
  - 3.5.1 Cancellation Workflow Diagram
- 3.6 ARCCLA Approval Workflows

**4. [Data Models](#4-data-models)** 📊
- 4.1 Core CTN Entity Structure
- 4.2 Amendment Entity Structure
- 4.3 Cancellation Entity Structure
- 4.4 Status Management

**5. [Core API Specifications](#5-core-api-specifications)** 🔗
- 5.1 Master Data APIs
  - 5.1.1 Cargo Types API
  - 5.1.2 Incoterms API
  - 5.1.3 Countries API
  - 5.1.4 Carriers API
  - 5.1.5 Currencies API
- 5.2 Certificate Management APIs
  - 5.2.1 CTN List API
  - 5.2.2 CTN Details API
  - 5.2.3 CTN Creation API
  - 5.2.4 Additional Master Data APIs
- 5.3 CTN Related Entity APIs
  - 5.3.1 CTN Tracking API
  - 5.3.2 CTN Attachments API
  - 5.3.3 CTN Goods API
  - 5.3.4 CTN Containers API
  - 5.3.5 CTN Addresses API
  - 5.3.6 CTN Charges API
  - 5.3.7 User Communication API
- 5.4 File Management APIs
  - 5.4.1 File Upload API

**6. [API Capabilities](#6-api-capabilities)** ⚡
- 6.1 Amendment APIs
  - 6.1.1 Amendment Request Creation API
  - 6.1.2 Amendment Status Tracking API
  - 6.1.3 Amendment List API
  - 6.1.4 Amendment Details API
- 6.2 Cancellation APIs
  - 6.2.1 Cancellation Request Creation API
  - 6.2.2 Cancellation Status Tracking API
  - 6.2.3 Cancellation List API
  - 6.2.4 Cancellation Details API
- 6.3 Approval Workflow APIs
  - 6.3.1 ARCCLA Broker Review API
  - 6.3.2 Approval Decision API
  - 6.3.3 Workflow Status API
- 6.4 Status Polling APIs
  - 6.4.1 Certificate Status API
  - 6.4.2 Eligibility Check API
  - 6.4.3 Notification API

**7. [Validation Framework](#7-validation-framework)** ✅
- 7.1 Field-Level Validation Rules
- 7.2 Business Logic Validation
- 7.3 Error Handling Standards

---

<div style="page-break-before: always;"></div>

## 1. Introduction

### 1.1 Purpose

This Interface Control Document (ICD) defines the technical specifications and interface requirements for integrating the JUL system (Abu Dhabi Ports) with the SINTECE system (ARCCLA) for CNCA certificate issuance.

**Key Features:**
- Certificate submission and approval workflow
- Amendment and cancellation requests
- Master data synchronization
- Status tracking and notifications

### 1.2 Scope

**In Scope:**
- Certificate request lifecycle (creation to issuance)
- Amendment and cancellation workflows
- API specifications and data models
- Authentication and authorization
- Validation and error handling

**Out of Scope:**
- Internal SINTECE business logic
- Payment gateway implementation
- Mobile application development
- Legacy system migration

### 1.3 Audience

- **Developers**: API implementation and integration
- **Architects**: System design and technical decisions  
- **QA Engineers**: Testing and validation
- **Business Analysts**: Requirements validation
- **Project Managers**: Implementation tracking

### 1.4 Key Terms

| **Term** | **Definition** |
|----------|----------------|
| **ARCCLA** | Angolan regulatory agency responsible for cargo certification |
| **BL** | Bill of Lading - shipping document required for certificates |
| **CNCA** | Certificado Nacional de Carga de Angola - required certificate for Angola cargo |
| **CTN** | Certificate/Cargo Tracking Note - internal certificate reference |
| **DUP** | Declaration of Unique Property - unique customs identifier |
| **JUL** | Abu Dhabi Ports system for CNCA certificate management |
| **SINTECE** | ARCCLA system for certificate processing and approval |
| **Amendment** | Request to modify submitted certificate data |
| **Cancellation** | Request to cancel submitted certificate |
| **canAmend/canCancel** | System flags indicating eligibility for amendment/cancellation |

---

<div style="page-break-before: always;"></div>

## 2. System Overview 🏗️

### 2.1 System Architecture

**JUL System (Abu Dhabi Ports)**
- Trader portal for CNCA certificate management
- User interface for request creation and document upload  
- Amendment/cancellation request capabilities
- Payment processing and certificate download
- Real-time status tracking and notifications

**SINTECE System (ARCCLA)**
- Backend certificate processing and approval system
- ARCCLA broker review workflow
- Amendment/cancellation approval processes
- Invoice generation and certificate issuance
- Master data management and reporting

**Integration Layer**
- RESTful APIs with JSON data format
- JWT authentication and secure communication
- Real-time API calls and status notifications
- Error handling and audit logging

### 2.2 Integration Pattern

**Communication:**
- RESTful APIs with standard HTTP methods (GET, POST, PUT, DELETE)
- JSON data format with schema validation
- HTTPS/TLS encryption and JWT authentication
- OData query support for filtering and pagination

**Data Flow:**
1. JUL validates certificate data and submits request
2. SINTECE processes with business rules validation  
3. ARCCLA broker reviews and approves/rejects
4. SINTECE generates invoice and processes payment
5. Certificate issued with amendment/cancellation capabilities
6. Status updates communicated via API polling

---

*Amendment Flow:*
1. JUL validates amendment eligibility using canAmend status flag
2. JUL submits amendment request via POST /api/CTNs/{id}/amendments with change tracking
3. SINTECE validates amendment request and notifies ARCCLA broker
4. ARCCLA broker reviews amendment in SINTECE with impact analysis
5. SINTECE sends amendment approval/rejection to JUL via notifications
6. If approved, SINTECE updates certificate and generates amendment invoice if applicable
7. JUL processes any additional payments and updates certificate status

*Cancellation Flow:*
1. JUL validates cancellation eligibility using canCancel status flag
2. JUL submits cancellation request via POST /api/CTNs/{id}/cancellations with reason documentation
3. SINTECE validates cancellation request and calculates financial impact
4. ARCCLA broker reviews cancellation in SINTECE with impact analysis
5. SINTECE sends cancellation approval/rejection to JUL via notifications
6. If approved, SINTECE processes cancellation including any refunds and updates certificate status

### 2.3 System Actors

The following actors interact with the integrated system:

| **Actor** | **Role** | **Responsibilities** | **System Access** |
|-----------|----------|------------------------------|-------------------|
| **Trader (Importer/Exporter)** | Business entity shipping goods to/from Angola | • Initiates CNCA certificate requests<br>• Uploads required documents (BL, DUP)<br>• Nominates customs broker<br>• Reviews and approves certificate details<br>• Makes payment for certificate issuance<br>• Downloads issued certificates<br>• Views amendment/cancellation history and status | JUL System (Web Portal) |
| **Customs Broker / Freight Forwarder** | Licensed agent representing trader with amendment/cancellation capabilities | • Accepts nomination from trader<br>• Completes certificate application<br>• Submits request for approval<br>• Creates amendment requests with change tracking<br>• Creates cancellation requests with reason documentation<br>• Tracks amendment/cancellation status<br>• Receives and forwards certificates to trader<br>• Handles communication with authorities | JUL System (Web Portal with Amendment/Cancellation Features) |
| **ARCCLA Broker** | Government official authorized to approve certificates, amendments, and cancellations | • Reviews submitted certificate requests<br>• Validates data accuracy and completeness<br>• Approves or rejects requests with detailed reasoning<br>• Reviews and approves/rejects amendment requests<br>• Reviews and approves/rejects cancellation requests<br>• Performs impact analysis for amendments/cancellations<br>• Provides rejection reasons/comments<br>• Issues official CNCA certificates<br>• Monitors compliance | SINTECE System (Internal Portal with Amendment/Cancellation Workflows) |
| **System Administrator** | Technical staff managing system operations | • User management and access control with role-based permissions<br>• System configuration including amendment/cancellation workflows<br>• Monitoring and troubleshooting<br>• Data backup and recovery including amendment/cancellation audit trails<br>• Performance optimization | JUL & SINTECE Systems (Admin Interface) |
| **Payment Processor** | Financial institution/payment gateway with enhanced capabilities | • Processes payment transactions including amendment fees<br>• Provides payment confirmations<br>• **Enhanced:** Handles refunds for approved cancellations<br>• **Enhanced:** Manages amendment fee processing<br>• Supports multiple currencies and payment methods | Payment Gateway System (Enhanced Integration) |
| **Compliance Officer** | Regulatory oversight with enhanced monitoring capabilities | • **Enhanced:** Monitors amendment/cancellation patterns for compliance<br>• **Enhanced:** Reviews audit trails for regulatory compliance<br>• **Enhanced:** Generates compliance reports including amendment/cancellation metrics<br>• Ensures adherence to ARCCLA regulations | SINTECE System (Enhanced Compliance Dashboard) |

**Enhanced User Interaction Flow:**

*Standard Certificate Flow:*
1. **Trader** logs into enhanced JUL → Creates certificate request → Uploads documents → Nominates broker
2. **Customs Broker** logs into enhanced JUL → Accepts nomination → Completes application with real-time validation → Submits to SINTECE
3. **ARCCLA Broker** logs into enhanced SINTECE → Reviews request with decision support tools → Approves/Rejects → Generates invoice (if approved)
4. **Customs Broker** receives notification in JUL → Reviews invoice → Processes payment
5. **ARCCLA Broker** receives payment confirmation → Issues certificate with amendment/cancellation capabilities
6. **Trader** and **Customs Broker** receive certificate in JUL → Download and use for customs clearance

*Amendment Flow:*
1. **Customs Broker** checks amendment eligibility in JUL → Creates amendment request → Documents changes
2. **ARCCLA Broker** receives amendment notification in SINTECE → Reviews changes with impact analysis → Approves/Rejects
3. **Customs Broker** receives amendment decision in JUL → Processes any additional payments → Updates stakeholders
4. **Trader** receives updated certificate with amendment history in JUL

*Cancellation Flow:*
1. **Customs Broker** checks cancellation eligibility in JUL → Creates cancellation request → Documents reasons
2. **ARCCLA Broker** receives cancellation notification in SINTECE → Reviews with financial impact analysis → Approves/Rejects
3. **Customs Broker** receives cancellation decision in JUL → Processes any refunds → Updates stakeholders
4. **Trader** receives cancellation confirmation and any applicable refunds

### 2.4 Amendment and Cancellation Capabilities

**Amendment Management:**
- Real-time eligibility validation based on certificate status
- Change tracking with before/after value comparison
- Impact analysis for proposed amendments
- Role-based approval workflow
- Amendment fee calculation and payment processing
- Complete audit trail with history

**Cancellation Management:**
- Real-time eligibility validation with financial impact assessment
- Reason code documentation
- Automated refund calculation based on cancellation timing
- Role-based approval workflow with escalation
- Integration with payment systems for refund processing
- Complete audit trail with financial reconciliation

**Enhanced Status Management:**
- Dynamic eligibility flags (canAmend, canCancel) based on real-time business rules
- Enhanced status workflow supporting amendment/cancellation states
- Real-time status updates with webhook notifications
- Comprehensive status history with audit trail
- Status-based UI enhancements for improved user experience

**Advanced Validation Framework:**
- Multi-level validation (field-level, business rule, cross-system)
- Real-time validation with immediate feedback
- Configurable validation rules with role-based exceptions
- Comprehensive error messaging with corrective action guidance
- Integration testing validation for amendment/cancellation workflows

---

<div style="page-break-before: always;"></div>

## 3. Process Flows 🔄

### 3.1 As-Is Process Analysis

The current SINTECE workflow consists of 15 distinct steps (LC-AR-CNCA-01 through LC-AR-CNCA-15) that involve multiple manual handoffs between traders, customs brokers, and ARCCLA staff. 

#### 3.1.1 Current State Process Flow Diagram

<div class="process-flow-container">
<img src="./images/svg/Traditional SINTECE Workflow.svg" alt="Traditional SINTECE Workflow" />
<p>Figure 3.1: Traditional SINTECE Workflow Process</p>
</div>

> **🚨 Process Inefficiencies:**
> - Multiple email-based communications causing delays
> - Manual document handling and verification processes
> - Limited real-time visibility for stakeholders
> - Duplicate data entry requirements across systems
> - No automated amendment or cancellation capabilities

> **⚠️ Key Bottlenecks:**
> - ARCCLA broker manual review and approval steps
> - Payment processing and reconciliation delays  
> - Physical document submission requirements
> - Manual invoice generation and distribution

### 3.2 To-Be Process

The JUL-SINTECE integration introduces a fully digital workflow with improvements over the current process.

#### 3.2.1 Future State Process Flow Diagram

<div class="process-flow-container">
<img src="./images/svg/EnhancedFutureStateCoreCertificateWorkflow.svg" alt="Enhanced Future State Core Certificate Workflow" />
<p>Figure 3.2: Enhanced Future State Core Certificate Workflow</p>
</div>

> **✅ Core Certificate Process Improvements:**
> 1. **Digital Initiation**: Traders initiate requests directly through JUL system
> 2. **Document Upload**: Electronic submission of BL and DUP documents
> 3. **Automated Validation**: Real-time validation of submitted data
> 4. **Streamlined Approval**: ARCCLA brokers receive structured requests for review
> 5. **Integrated Payment**: Seamless payment processing with automatic reconciliation
> 6. **Digital Certificate Issuance**: Electronic certificate generation and delivery

> **🚀 Enhanced Capabilities Integration:**
> - Real-time amendment requests with ARCCLA approval workflow
> - Cancellation management with refund processing capabilities
> - Status polling with eligibility flags for allowed operations
> - Comprehensive audit trail and notifications system

**Benefits of Enhanced Process:**
- Fully digital workflow with no physical documents
- Real-time status visibility for all parties
- Integrated amendment and cancellation capabilities
- Automated payment processing
- Single data entry point
- Complete audit trail

### 3.3 Integration Touchpoints

The integration establishes comprehensive touchpoints between JUL and SINTECE systems with a modern API-driven architecture.

#### 3.3.1 API Integration Architecture Diagram

<div class="process-flow-container">
<img src="./images/svg/Integration API Flow Diagram.svg" alt="Integration API Flow Diagram" />
<p>Figure 3.3: Integration API Flow Architecture</p>
</div>

**Data Synchronization Points:**
- Master data synchronization (countries, ports, cargo types)
- User account and role management coordination
- Certificate status and lifecycle management
- Amendment and cancellation request handling

**API Integration Points:**
- Authentication and authorization endpoints
- Certificate submission and retrieval APIs  
- Amendment request creation and approval APIs
- Cancellation request creation and approval APIs
- Status monitoring and notification APIs

**Business Process Touchpoints:**
- ARCCLA broker approval workflows
- Payment processing and invoice generation
- Document management and storage
- Audit logging and compliance reporting

### 3.4 Amendment Workflow Process

The amendment workflow provides controlled modification capabilities for issued certificates with comprehensive ARCCLA approval processes.

#### 3.4.1 Enhanced Amendment Workflow Diagram

<div class="process-flow-container">
<img src="./images/svg/Enhanced Amendment Workflow.svg" alt="Enhanced Amendment Workflow" />
<p>Figure 3.4: Enhanced Amendment Workflow Process</p>
</div>

**Amendment Request Initiation:**
1. **Eligibility Check**: System validates certificate status and amendment permissions
2. **Request Creation**: Customs broker selects fields to amend and provides change reasons
3. **Validation**: System performs business rule validation on proposed changes
4. **Submission**: Amendment request is submitted to ARCCLA for review

**ARCCLA Review and Approval:**
1. **Notification**: ARCCLA broker receives amendment request notification
2. **Impact Analysis**: Review of proposed changes and potential impacts
3. **Decision**: Approval or rejection with detailed reasoning
4. **Processing**: For approved amendments, certificate is updated and new invoice generated

**Amendment Eligibility Rules:**
- Certificate status must be "Submitted", "Approved", or "Issued"
- No pending amendments or cancellations exist
- Certificate not yet used for customs clearance
- Amendment requested within allowed timeframe (typically 24 hours after issuance)
- User has appropriate amendment permissions

### 3.5 Cancellation Workflow Process

The cancellation workflow provides controlled termination of certificate requests with comprehensive financial impact management and refund processing.

#### 3.5.1 Enhanced Cancellation Workflow Diagram

<div class="process-flow-container">
<img src="./images/svg/Enhanced Cancellation Workflow.svg" alt="Enhanced Cancellation Workflow" />
<p>Figure 3.5: Enhanced Cancellation Workflow Process</p>
</div>

**Cancellation Request Initiation:**
1. **Eligibility Check**: System validates certificate status and cancellation permissions
2. **Impact Assessment**: System calculates financial impact and refund eligibility
3. **Request Creation**: Customs broker provides cancellation reason and additional details
4. **Submission**: Cancellation request is submitted to ARCCLA for review

**ARCCLA Review and Processing:**
1. **Notification**: ARCCLA broker receives cancellation request notification
2. **Review**: Validation of cancellation reason and business justification
3. **Financial Analysis**: Calculation of appropriate refund amount based on timing and status
4. **Decision**: Approval or rejection of cancellation request
5. **Processing**: For approved cancellations, certificate is cancelled and refund initiated

**Cancellation Eligibility Rules:**
- Certificate status allows cancellation (not yet issued or used for customs clearance)
- Payment status allows refund processing
- Cancellation requested within allowed timeframe
- No active amendments in progress
- Valid business reason for cancellation provided

### 3.6 ARCCLA Approval Workflows

The ARCCLA approval workflows are enhanced to support the new amendment and cancellation capabilities:

**Enhanced Review Dashboard:**
- Unified queue for certificate submissions, amendments, and cancellations
- Priority-based processing with configurable business rules
- Rich context information for informed decision making
- Integrated communication tools for broker-to-broker coordination

**Approval Decision Framework:**
- Structured decision criteria for different request types
- Automated recommendations based on historical patterns
- Escalation procedures for complex or high-value requests
- Audit trail capture for all approval decisions

**Workflow Automation:**
- Automatic assignment of requests to available brokers
- SLA monitoring with escalation triggers
- Batch processing capabilities for high-volume periods
- Integration with existing SINTECE approval processes

**Enhanced Notification System:**
- Real-time notifications to all stakeholders
- Email and system notifications with rich content
- Webhook support for external system integration
- Configurable notification preferences by user role

---

<div style="page-break-before: always;"></div>

## 4. Data Models 📊

### 4.1 Core CTN Entity Structure

The Certificate Tracking Note (CTN) entity serves as the foundation for all certificate operations. The enhanced data model includes additional fields to support amendment and cancellation workflows:

```json
{
  "id": "string (UUID)",
  "certificateNumber": "string (auto-generated)",
  "requestDate": "datetime (ISO 8601)",
  "submissionDate": "datetime (ISO 8601)",
  "status": "string (enum)",
  "canAmend": "boolean",
  "canCancel": "boolean",
  "lastAmendmentDate": "datetime (ISO 8601, nullable)",
  "lastCancellationAttempt": "datetime (ISO 8601, nullable)",
  "isAmended": "boolean (default: false)",
  "isCancelled": "boolean (default: false)",
  "originalCertificateId": "string (UUID, nullable)",
  "trader": {
    "traderId": "string (UUID)",
    "traderName": "string (required, max 200)",
    "traderEmail": "string (required, valid email)",
    "traderPhone": "string (required)",
    "traderAddress": {
      "street": "string (required, max 200)",
      "city": "string (required, max 100)",
      "country": "string (required, ISO country code)",
      "postalCode": "string (optional, max 20)"
    }
  },
  "customsBroker": {
    "brokerId": "string (UUID)",
    "brokerName": "string (required, max 200)",
    "brokerEmail": "string (required, valid email)",
    "brokerLicenseNumber": "string (required, max 50)",
    "brokerCompany": "string (required, max 200)",
    "isNominated": "boolean (default: false)",
    "nominationDate": "datetime (ISO 8601, nullable)"
  },
  "shipment": {
    "billOfLadingNumber": "string (required, max 50)",
    "dupNumber": "string (required, max 50)",
    "vesselName": "string (required, max 200)",
    "voyageNumber": "string (required, max 50)",
    "portOfLoading": "string (required, port code)",
    "portOfDischarge": "string (required, port code)",
    "estimatedTimeOfArrival": "datetime (ISO 8601)",
    "actualTimeOfArrival": "datetime (ISO 8601, nullable)"
  },
  "goods": [
    {
      "itemNumber": "integer (sequence)",
      "description": "string (required, max 500)",
      "hsCode": "string (required, HS code format)",
      "quantity": "number (required, positive)",
      "unit": "string (required, standard units)",
      "weight": "number (required, positive, kg)",
      "volume": "number (optional, positive, m³)",
      "value": "number (required, positive, USD)",
      "origin": "string (required, ISO country code)",
      "manufacturer": "string (optional, max 200)"
    }
  ],
  "containers": [
    {
      "containerNumber": "string (required, max 20)",
      "containerType": "string (required, ISO container type)",
      "sealNumbers": ["string (max 50)"],
      "tareWeight": "number (required, positive, kg)",
      "grossWeight": "number (required, positive, kg)",
      "cargoWeight": "number (required, positive, kg)"
    }
  ],
  "payment": {
    "invoiceNumber": "string (auto-generated)",
    "amount": "number (required, positive, USD)",
    "currency": "string (required, ISO currency code)",
    "paymentStatus": "string (enum)",
    "paymentDate": "datetime (ISO 8601, nullable)",
    "paymentMethod": "string (enum)",
    "refundAmount": "number (optional, positive, USD)",
    "refundStatus": "string (enum, nullable)",
    "refundDate": "datetime (ISO 8601, nullable)"
  },
  "audit": {
    "createdBy": "string (UUID)",
    "createdDate": "datetime (ISO 8601)",
    "lastModifiedBy": "string (UUID)",
    "lastModifiedDate": "datetime (ISO 8601)",
    "version": "integer (auto-increment)"
  }
}
```

**Key Enhancements:**
- Added `canAmend` and `canCancel` eligibility flags
- Enhanced payment model with refund capabilities
- Added amendment and cancellation tracking fields
- Comprehensive audit trail with versioning

### 4.2 Amendment Entity Structure

The amendment entity captures all modification requests with complete change tracking:

```json
{
  "amendmentId": "string (UUID)",
  "originalCertificateId": "string (UUID, foreign key)",
  "amendmentNumber": "string (auto-generated, sequential)",
  "requestDate": "datetime (ISO 8601)",
  "submittedBy": "string (UUID, foreign key)",
  "submittedByRole": "string (enum: CustomsBroker, Trader)",
  "status": "string (enum: Pending, UnderReview, Approved, Rejected, Cancelled)",
  "requestReason": "string (required, max 500)",
  "businessJustification": "string (optional, max 1000)",
  "requestedChanges": [
    {
      "fieldPath": "string (required, JSON path notation)",
      "fieldName": "string (required, human-readable)",
      "oldValue": "any (original value)",
      "newValue": "any (proposed new value)",
      "changeReason": "string (required, max 200)",
      "validationStatus": "string (enum: Valid, Invalid, Warning)"
    }
  ],
  "arcclaReview": {
    "assignedTo": "string (UUID, nullable)",
    "assignedDate": "datetime (ISO 8601, nullable)",
    "reviewStarted": "datetime (ISO 8601, nullable)",
    "reviewCompleted": "datetime (ISO 8601, nullable)",
    "decision": "string (enum: Approved, Rejected, nullable)",
    "decisionReason": "string (optional, max 1000)",
    "reviewComments": "string (optional, max 2000)",
    "impactAssessment": {
      "riskLevel": "string (enum: Low, Medium, High)",
      "affectedSystems": ["string"],
      "complianceImpact": "string (optional, max 500)",
      "financialImpact": "number (optional, USD)"
    }
  },
  "fees": {
    "amendmentFee": "number (required, positive, USD)",
    "currency": "string (required, ISO currency code)",
    "calculationMethod": "string (required)",
    "invoiceNumber": "string (auto-generated, nullable)",
    "paymentStatus": "string (enum)",
    "paymentDate": "datetime (ISO 8601, nullable)"
  },
  "processing": {
    "applicationStarted": "datetime (ISO 8601, nullable)",
    "applicationCompleted": "datetime (ISO 8601, nullable)",
    "certificateUpdated": "datetime (ISO 8601, nullable)",
    "notificationsSent": "datetime (ISO 8601, nullable)",
    "processingErrors": [
      {
        "errorCode": "string",
        "errorMessage": "string",
        "errorDate": "datetime (ISO 8601)"
      }
    ]
  },
  "audit": {
    "createdBy": "string (UUID)",
    "createdDate": "datetime (ISO 8601)",
    "lastModifiedBy": "string (UUID)",
    "lastModifiedDate": "datetime (ISO 8601)",
    "workflowHistory": [
      {
        "action": "string",
        "performedBy": "string (UUID)",
        "performedDate": "datetime (ISO 8601)",
        "comments": "string (optional)",
        "systemGenerated": "boolean"
      }
    ]
  }
}
```

### 4.3 Cancellation Entity Structure

The cancellation entity manages certificate termination requests with comprehensive financial tracking:

```json
{
  "cancellationId": "string (UUID)",
  "originalCertificateId": "string (UUID, foreign key)",
  "cancellationNumber": "string (auto-generated, sequential)",
  "requestDate": "datetime (ISO 8601)",
  "submittedBy": "string (UUID, foreign key)",
  "submittedByRole": "string (enum: CustomsBroker, Trader)",
  "status": "string (enum: Pending, UnderReview, Approved, Rejected, Cancelled)",
  "cancellationReason": {
    "reasonCode": "string (enum: required)",
    "reasonDescription": "string (required, max 500)",
    "additionalDetails": "string (optional, max 1000)",
    "urgencyLevel": "string (enum: Normal, High, Critical)"
  },
  "financialImpact": {
    "originalAmount": "number (required, USD)",
    "refundEligibility": "boolean",
    "refundAmount": "number (optional, USD)",
    "cancellationFee": "number (optional, USD)",
    "netRefund": "number (optional, USD)",
    "refundCalculationMethod": "string (required)",
    "refundJustification": "string (optional, max 500)"
  },
  "arcclaReview": {
    "assignedTo": "string (UUID, nullable)",
    "assignedDate": "datetime (ISO 8601, nullable)",
    "reviewStarted": "datetime (ISO 8601, nullable)",
    "reviewCompleted": "datetime (ISO 8601, nullable)",
    "decision": "string (enum: Approved, Rejected, nullable)",
    "decisionReason": "string (optional, max 1000)",
    "reviewComments": "string (optional, max 2000)",
    "riskAssessment": {
      "fraudRisk": "string (enum: Low, Medium, High)",
      "complianceRisk": "string (enum: Low, Medium, High)",
      "operationalRisk": "string (enum: Low, Medium, High)",
      "overallRisk": "string (enum: Low, Medium, High)"
    }
  },
  "refundProcessing": {
    "refundInitiated": "datetime (ISO 8601, nullable)",
    "refundCompleted": "datetime (ISO 8601, nullable)",
    "refundMethod": "string (enum: nullable)",
    "refundReference": "string (nullable)",
    "refundStatus": "string (enum: nullable)",
    "processingErrors": [
      {
        "errorCode": "string",
        "errorMessage": "string",
        "errorDate": "datetime (ISO 8601)"
      }
    ]
  },
  "audit": {
    "createdBy": "string (UUID)",
    "createdDate": "datetime (ISO 8601)",
    "lastModifiedBy": "string (UUID)",
    "lastModifiedDate": "datetime (ISO 8601)",
    "workflowHistory": [
      {
        "action": "string",
        "performedBy": "string (UUID)",
        "performedDate": "datetime (ISO 8601)",
        "comments": "string (optional)",
        "systemGenerated": "boolean"
      }
    ]
  }
}
```

### 4.4 Enhanced Status Management

The enhanced status management system provides comprehensive lifecycle tracking with dynamic eligibility determination:

**Certificate Status Enumeration:**
```json
{
  "certificateStatuses": [
    "Draft",
    "Submitted", 
    "UnderReview",
    "RequiresAmendment",
    "Approved",
    "PaymentPending",
    "PaymentReceived",
    "Issued",
    "Active",
    "Amended",
    "Cancelled",
    "Expired",
    "Rejected"
  ]
}
```

**Amendment Status Enumeration:**
```json
{
  "amendmentStatuses": [
    "Pending",
    "UnderReview", 
    "RequiresInformation",
    "Approved",
    "Rejected",
    "PaymentPending",
    "PaymentReceived",
    "Processing",
    "Completed",
    "Cancelled",
    "Expired"
  ]
}
```

**Cancellation Status Enumeration:**
```json
{
  "cancellationStatuses": [
    "Pending",
    "UnderReview",
    "RequiresInformation", 
    "Approved",
    "Rejected",
    "RefundPending",
    "RefundProcessing",
    "RefundCompleted",
    "Completed",
    "Cancelled"
  ]
}
```

**Eligibility Rules Matrix:**
The system dynamically calculates eligibility flags based on the following business rules:

**Amendment Eligibility (`canAmend`):**
- Certificate status is in: ["Submitted", "Approved", "Issued", "Active"]
- No pending amendments exist for the certificate
- No pending cancellations exist for the certificate
- Certificate was issued within the allowed amendment timeframe (configurable)
- User has appropriate permissions (CustomsBroker or authorized Trader)
- Certificate has not been used for customs clearance

**Cancellation Eligibility (`canCancel`):**
- Certificate status is in: ["Submitted", "Approved", "PaymentPending", "PaymentReceived", "Issued"]
- No pending amendments exist for the certificate
- No pending cancellations exist for the certificate
- Certificate was submitted within the allowed cancellation timeframe (configurable)
- User has appropriate permissions (CustomsBroker or authorized Trader)
- Certificate has not been used for customs clearance

**Dynamic Status Calculation:**
The system recalculates eligibility flags whenever:
- Certificate status changes
- Amendment or cancellation requests are submitted
- Time-based rules expire
- User permissions are modified
- Business rules are updated by administrators

---

<div style="page-break-before: always;"></div>

## 5. Core API Specifications 🔗

### 5.1 Master Data APIs

Master data APIs provide essential reference data required for certificate creation, validation, and business operations.

#### 5.1.1 Cargo Types API

**Business Purpose:** Manages cargo classification data essential for determining certificate fees, validation rules, and compliance requirements. Critical for proper cargo categorization in international shipping, affecting customs documentation, handling procedures, insurance requirements, and regulatory compliance.

**Endpoint:** `GET /api/CargoTypes`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | CargoType_Desc |
| 2 | CargoType_Desc | String - 200 | O | Filter by cargo type description | CONTAINER |
| 3 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **CARGO_UI_001**: CargoType_Desc filter optional, 1-200 characters
- **CARGO_UI_002**: Sort parameter from predefined fields only
- **CARGO_UI_003**: Max 100 records per page

**Business Validation Rules:**
- **CARGO_BV_001**: Only active cargo types can be used for new CTN creation
- **CARGO_BV_002**: Container cargo requires container details
- **CARGO_BV_003**: Dangerous goods cargo requires special documentation

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique cargo type identifier | 1 |
| 2 | CargoType_Code | String - 10 | M | Cargo type code | CONT |
| 3 | CargoType_Desc | String - 200 | M | Cargo type description | CONTAINER |
| 4 | Active | Boolean | M | Active status indicator | true |
| 5 | CreatedOn | DateTime | O | Record creation timestamp | 2023-01-15T10:30:00Z |

**Error Codes:**
- **CARGO_E001**: "Invalid parameters" (HTTP 400)
- **CARGO_E002**: "No data found" (HTTP 404)
- **CARGO_E003**: "Access denied" (HTTP 403)

**Sample JSON Request:**
```json
GET /api/CargoTypes?$sort=CargoType_Desc&CargoType_Desc=&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "CargoType_Code": "CONT",
    "CargoType_Desc": "CONTAINER",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "CargoType_Code": "BULK",
    "CargoType_Desc": "BULK CARGO",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.1.2 Incoterms API

**Business Purpose:** Provides International Commercial Terms (Incoterms) data crucial for determining responsibility boundaries, costs, and risks between buyers and sellers in international trade transactions. Affects shipping responsibilities, insurance requirements, customs clearance obligations, and liability allocation throughout the shipping process.

**Endpoint:** `GET /api/Incoterms`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | IncotermCode |
| 2 | IncotermCode | String - 10 | O | Filter by Incoterm code | CIF |
| 3 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **INCO_UI_001**: IncotermCode filter optional, exactly 3 uppercase letters
- **INCO_UI_002**: Display code and description together
- **INCO_UI_003**: Default to "Active Only" for new certificates

**Business Validation Rules:**
- **INCO_BV_001**: CIF/CIP terms require insurance documentation
- **INCO_BV_002**: Some Incoterms not applicable for certain cargo types
- **INCO_BV_003**: Incoterm selection affects customs valuation

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique Incoterm identifier | 2 |
| 2 | IncotermCode | String - 10 | M | Incoterm code | CIF |
| 3 | IncotermDesc | String - 200 | M | Incoterm description | Cost, Insurance and Freight |
| 4 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **INCO_E001**: "Invalid format" (HTTP 400)
- **INCO_E002**: "Not applicable for cargo type" (HTTP 422)
- **INCO_E003**: "Inactive Incoterm" (HTTP 422)

**Sample JSON Response:**
```json
[
  {
    "Id": 2,
    "IncotermCode": "CIF",
    "IncotermDesc": "Cost, Insurance and Freight",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1
  }
]
```

#### 5.1.3 Countries API

**Business Purpose:** Essential for international trade compliance, determining applicable regulations, duties, restrictions, and routing requirements for cargo shipments. Critical for sanctions screening, trade agreement benefits, customs procedures, and ensuring compliance with import/export regulations between trading nations.

**Endpoint:** `GET /api/Countries`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Country_Name |
| 2 | Country_Name | String - 100 | O | Filter by country name | Angola |
| 3 | ExportingCountry | Boolean | O | Filter exporting countries | true |
| 4 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **COUNTRY_UI_001**: Country name filter optional, 1-100 characters
- **COUNTRY_UI_002**: Auto-complete dropdown with country name and code
- **COUNTRY_UI_003**: Visual indicator for sanctioned/restricted countries

**Business Validation Rules:**
- **COUNTRY_BV_001**: Angola must be origin or destination for CNCA certificates
- **COUNTRY_BV_002**: Sanctioned countries require special authorization
- **COUNTRY_BV_003**: Country code must match ISO 3166-1 standard

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique country identifier | 10 |
| 2 | Country_Name | String - 100 | M | Country name | Angola |
| 3 | Country_Code | String - 3 | M | ISO country code | AO |
| 4 | ExportingCountry | Boolean | M | Exporting country flag | true |
| 5 | ImportingCountry | Boolean | M | Importing country flag | false |

**Error Codes:**
- **COUNTRY_E001**: "Invalid format" (HTTP 400)
- **COUNTRY_E002**: "Not approved for trade" (HTTP 422)
- **COUNTRY_E003**: "Sanctioned country" (HTTP 403)

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Country_Name |
| 2 | Country_Name | String - 100 | O | Filter by country name | Angola |
| 3 | ExportingCountry | Boolean | O | Filter exporting countries | true |
| 4 | active | Boolean | O | Filter active records only | 1 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique country identifier | 10 |
| 2 | Country_Name | String - 100 | M | Country name | Angola |
| 3 | Country_Code | String - 3 | M | ISO country code | AO |
| 4 | ExportingCountry | Boolean | M | Exporting country flag | true |
| 5 | ImportingCountry | Boolean | M | Importing country flag | false |

#### 5.1.4 Carriers API

**Endpoint:** `GET /api/Carriers`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Name |
| 2 | Name | String - 200 | O | Filter by carrier name | A.C. ORSSLEFF'S |
| 3 | active | Boolean | O | Filter active records only | 1 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique carrier identifier | 789 |
| 2 | Name | String - 200 | M | Carrier company name | A.C. ORSSLEFF'S EFTF A/S |
| 3 | Code | String - 20 | O | Carrier code | ORSSLEFF |
| 4 | Active | Boolean | M | Active status indicator | true |

#### 5.1.5 Currencies API

**Endpoint:** `GET /api/Currencies`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Code |
| 2 | Code | String - 3 | O | Filter by currency code | USD |
| 3 | active | Boolean | O | Filter active records only | 1 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique currency identifier | 2 |
| 2 | Code | String - 3 | M | ISO currency code | USD |
| 3 | Name | String - 100 | O | Currency name | US Dollar |
| 4 | Symbol | String - 5 | O | Currency symbol | $ |

### 5.2 Certificate Management APIs

Certificate management APIs handle the core CTN certificate lifecycle operations, enabling the creation, retrieval, and management of CNCA certificates throughout their entire lifecycle from draft to completion.

#### 5.2.1 CTN List API

**Business Purpose:** Provides comprehensive listing and filtering capabilities for CTN certificates. Essential for dashboard displays, search functionality, status tracking, and bulk operations. Supports real-time monitoring of certificate processing status and enables efficient certificate portfolio management for traders and customs brokers.

**Endpoint:** `GET /api/ctns`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 500 | O | OData expand for related entities | CargoType,Status,Visum_Agent,CreatedBy,Consignee |
| 2 | $sort | String - 100 | O | OData sort parameter | -ModifiedOn |
| 3 | $top | Integer | O | Number of records to return | 10 |
| 4 | $filter | String - 1000 | O | OData filter expression | Status eq 'Active' |

**UI Validation Rules:**
- **CTN_UI_001**: $top parameter max 100 records per request
- **CTN_UI_002**: $expand parameter validate against allowed entity names
- **CTN_UI_003**: $filter parameter OData syntax validation

**Business Validation Rules:**
- **CTN_BV_001**: User can only view certificates belonging to their organization
- **CTN_BV_002**: Sensitive data requires role-based access
- **CTN_BV_003**: Date range filters max 2 years for performance

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique CTN identifier | 503808 |
| 2 | CTN_Reference_Number | String - 50 | M | System generated CTN reference | AO-CNT-503808-2023 |
| 3 | BL_number | String - 50 | M | Bill of lading number | vc568009iujh |
| 4 | UniqueTradeNumber | String - 50 | M | Unique trade number (DUP) | 56789098765 |
| 5 | DCNumber | String - 50 | O | Declaration certificate number | 7777777 |
| 6 | StatusId | Integer | M | Certificate status identifier | 1 |
| 7 | CargoTypeId | Integer | M | Cargo type identifier | 1 |
| 8 | Total_Value_Of_Goods | Decimal | M | Total value of goods in USD | 15000.00 |
| 9 | CreatedOn | DateTime | M | Record creation timestamp | 2025-11-12T18:49:30.88Z |
| 10 | ModifiedOn | DateTime | O | Record modification timestamp | 2025-11-12T19:15:45.23Z |

**Error Codes:**
- **CTN_E001**: "Invalid parameters" (HTTP 400)
- **CTN_E002**: "Access denied" (HTTP 403)
- **CTN_E003**: "No data found" (HTTP 404)

**Sample JSON Response:**
```json
[
  {
    "Id": 503808,
    "CTN_Reference_Number": "AO-CNT-503808-2023",
    "StatusId": 1,
    "BL_number": "vc568009iujh",
    "UniqueTradeNumber": "56789098765",
    "DCNumber": "7777777",
    "CargoTypeId": 1,
    "ETD": "2023-12-15T10:00:00Z",
    "ETA": "2023-12-20T15:30:00Z",
    "Total_Value_Of_Goods": 15000.00,
    "View_CurrencyId": 2,
    "IsExport": true,
    "IsImport": false,
    "CreatedOn": "2025-11-12T18:49:30.8817831Z",
    "CreatedById": 1,
    "ModifiedOn": "2025-11-12T19:15:45.2345678Z",
    "ModifiedById": 1,
    "Status": {
      "Id": 1,
      "Status_Desc": "Draft",
      "Active": true
    },
    "CargoType": {
      "Id": 1,
      "CargoType_Code": "CONT",
      "CargoType_Desc": "CONTAINER"
    }
  }
]
```

#### 5.2.2 CTN Details API

**Endpoint:** `GET /api/ctns/{id}`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | id | Integer | M | CTN unique identifier from URL path | 503808 |
| 2 | $expand | String - 500 | O | OData expand for related entities | CargoType,ParentCTN,Status,Incoterm |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique CTN identifier | 503808 |
| 2 | CTN_Reference_Number | String - 50 | M | System generated CTN reference | AO-CNT-503808-2023 |
| 3 | BL_number | String - 50 | M | Bill of lading number | vc568009iujh |
| 4 | UniqueTradeNumber | String - 50 | M | Unique trade number | 56789098765 |
| 5 | VoyageNo | String - 50 | O | Voyage number | VOY123 |
| 6 | VesselName | String - 200 | O | Vessel name | MSC MEDITERRANEAN |
| 7 | Total_number_containers | Integer | M | Total number of containers | 2 |
| 8 | Total_Value_Of_Goods | Decimal | M | Total value of goods | 15000.00 |
| 9 | CTNCost | Decimal | O | Certificate cost | 150.00 |

#### 5.2.3 CTN Creation API

**Endpoint:** `POST /api/ctns`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | BL_number | String - 50 | M | Bill of lading number | vc568009iujh |
| 2 | UniqueTradeNumber | String - 50 | M | Unique trade number | 56789098765 |
| 3 | CargoTypeId | Integer | M | Cargo type identifier | 1 |
| 4 | IncotermId | Integer | M | Incoterm identifier | 2 |
| 5 | OriginCountryId | Integer | M | Origin country identifier | 10 |
| 6 | FinalDestinationCountryId | Integer | M | Destination country identifier | 85 |
| 7 | Total_Value_Of_Goods | Decimal | M | Total value of goods | 15000.00 |
| 8 | View_CurrencyId | Integer | M | Currency identifier | 2 |
| 9 | IsExport | Boolean | M | Export flag | true |
| 10 | ConsigneeId | Integer | O | Consignee identifier | 12345 |

**Sample JSON Request:**
```json
{
  "BL_number": "vc568009iujh",
  "UniqueTradeNumber": "56789098765", 
  "CargoTypeId": 1,
  "IncotermId": 2,
  "OriginCountryId": 10,
  "FinalDestinationCountryId": 85,
  "Total_Value_Of_Goods": 15000.00,
  "View_CurrencyId": 2,
  "IsExport": true,
  "IsImport": false,
  "ETD": "2023-12-15T10:00:00Z",
  "ETA": "2023-12-20T15:30:00Z",
  "VoyageNo": "VOY123",
  "VesselName": "MSC MEDITERRANEAN",
  "ConsigneeId": 12345
}
```

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Generated CTN unique identifier | 503809 |
| 2 | CTN_Reference_Number | String - 50 | M | Auto-generated CTN reference | AO-CNT-503809-2023 |
| 3 | StatusId | Integer | M | Initial status (typically 1 for Draft) | 1 |
| 4 | CreatedOn | DateTime | M | Record creation timestamp | 2025-11-13T10:30:00Z |
| 5 | CreatedById | Integer | M | User who created the record | 13345 |

#### 5.2.4 Additional Master Data APIs

**CTN Cities API**

**Endpoint:** `GET /api/CTNCities`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Name |
| 2 | CountryId | Integer | M | Country identifier filter | 10 |
| 3 | Name | String - 100 | O | City name filter | Luanda |
| 4 | active | Boolean | O | Filter active records only | 1 |

**Freight Payment Types API**

**Endpoint:** `GET /api/FreightPaymentTypes`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | FreightPaymentType_Desc |
| 2 | FreightPaymentType_Desc | String - 200 | O | Filter by payment type | Prepaid |
| 3 | active | Boolean | O | Filter active records only | 1 |

**Banks API**

**Endpoint:** `GET /api/Banks`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Name |
| 2 | Name | String - 200 | O | Filter by bank name | Banco Nacional |
| 3 | active | Boolean | O | Filter active records only | 1 |

**Consignees API**

**Endpoint:** `GET /api/Consignees`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | NIFNumber |
| 2 | NIFNumber | String - 50 | O | Filter by NIF number | 123456789 |
| 3 | active | Boolean | O | Filter active records only | 1 |

**Transport Types API**

**Endpoint:** `GET /api/TransportTypes`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 100 | O | OData expand parameter | description |
| 2 | $sort | String - 100 | O | OData sort parameter | Description |
| 3 | Description | String - 200 | O | Filter by description | Sea |
| 4 | active | Boolean | O | Filter active records only | 1 |

**Locations/Ports API**

**Endpoint:** `GET /api/Locations`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | PortName |
| 2 | CountryId | Integer | M | Country identifier filter | 4 |
| 3 | PortName | String - 200 | O | Filter by port name | Dubai |
| 4 | active | Boolean | O | Filter active records only | 1 |

**Goods Classifications API**

**Endpoint:** `GET /api/GoodsClassifications`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Goods_Classification_Desc |
| 2 | Goods_Classification_Desc | String - 200 | O | Filter by classification | Electronics |
| 3 | active | Boolean | O | Filter active records only | 1 |

**IMO Codes API**

**Endpoint:** `GET /api/IMOs`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | IMO_Desc |
| 2 | IMO_Desc | String - 200 | O | Filter by IMO description | Flammable Liquids |
| 3 | active | Boolean | O | Filter active records only | 1 |

**Container Types API**

**Endpoint:** `GET /api/ContainerTypes`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Container_Type |
| 2 | Container_Type | String - 50 | O | Filter by container type | 20GP |
| 3 | active | Boolean | O | Filter active records only | 1 |

**Attachment Names API**

**Endpoint:** `GET /api/AttachmentNames`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | AttachmentName_Desc |
| 2 | AttachmentName_Desc | String - 200 | O | Filter by attachment name | Bill of Lading |
| 3 | active | Boolean | O | Filter active records only | 1 |

### 5.3 CTN Related Entity APIs

#### 5.3.1 CTN Tracking API

**Endpoint:** `GET /api/ctnTracking`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 500 | O | OData expand parameter | CTN,DestinationPort,SourcePort,TransportType |
| 2 | ctn | Integer | M | CTN identifier | 503808 |
| 3 | ctnid | Integer | M | CTN identifier (duplicate) | 503808 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Tracking record ID | 71898 |
| 2 | CTNId | Integer | M | Related CTN ID | 503808 |
| 3 | SourcePortId | Integer | O | Source port identifier | 150 |
| 4 | DestinationPortId | Integer | O | Destination port identifier | 275 |
| 5 | TransportTypeId | Integer | M | Transport type identifier | 1 |
| 6 | ETD | DateTime | O | Estimated time of departure | 2023-12-15T10:00:00Z |
| 7 | ETA | DateTime | O | Estimated time of arrival | 2023-12-20T15:30:00Z |
| 8 | VesselName | String - 200 | O | Vessel name | MSC MEDITERRANEAN |
| 9 | VoyageNumber | String - 50 | O | Voyage number | VOY123456 |

#### 5.3.2 CTN Attachments API

**Endpoint:** `GET /api/ctnAttachments`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 300 | O | OData expand parameter | CreatedBy,attachment,attachmentName |
| 2 | ctn | Integer | M | CTN identifier | 503808 |
| 3 | ctnid | Integer | M | CTN identifier (duplicate) | 503808 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Attachment record ID | 320988 |
| 2 | CTNId | Integer | M | Related CTN ID | 503808 |
| 3 | AttachmentNameId | Integer | M | Attachment type ID | 1 |
| 4 | AttachmentId | String (UUID) | M | File attachment ID | 0da7461c-2155-4d20-a695-6b7463367327 |
| 5 | FileName | String - 256 | M | Original file name | Bill_of_Lading.pdf |
| 6 | FileSize | Integer | M | File size in bytes | 245760 |
| 7 | MimeType | String - 100 | M | File MIME type | application/pdf |
| 8 | CreatedOn | DateTime | M | Upload timestamp | 2023-11-12T14:30:00Z |

**POST /api/ctnAttachments - Create Attachment**

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | CTNId | Integer | M | Related CTN identifier | 503808 |
| 2 | AttachmentNameId | Integer | M | Attachment type identifier | 1 |
| 3 | AttachmentId | String (UUID) | M | File upload identifier | 0da7461c-2155-4d20-a695-6b7463367327 |
| 4 | Description | String - 500 | O | Attachment description | Original Bill of Lading |

#### 5.3.3 CTN Goods API

**Endpoint:** `GET /api/ctnGoods`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 300 | O | OData expand parameter | goodsclassification,cargotype,imo |
| 2 | $sort | String - 100 | O | OData sort parameter | gumarref |
| 3 | $with | String - 500 | O | OData aggregate functions | sum(grossweightkg),sum(volumecbm) |
| 4 | ctn | Integer | M | CTN identifier | 503808 |
| 5 | ctnid | Integer | M | CTN identifier (duplicate) | 503808 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Goods record ID | 989192 |
| 2 | CTNId | Integer | M | Related CTN ID | 503808 |
| 3 | Description | String - 500 | M | Goods description | Electronic Components |
| 4 | HSCode | String - 20 | M | Harmonized system code | 854390 |
| 5 | GrossWeightKG | Decimal | M | Gross weight in kilograms | 1500.50 |
| 6 | VolumeCBM | Decimal | O | Volume in cubic meters | 12.5 |
| 7 | ValueOfGoods | Decimal | M | Goods value | 15000.00 |
| 8 | NumberOfPackages | Integer | M | Number of packages | 50 |
| 9 | PackagingType | String - 50 | M | Type of packaging | Cartons |
| 10 | CountryOfOrigin | String - 50 | M | Country of origin | China |

**POST /api/ctnGoods - Create Goods Record**

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | CTNId | Integer | M | Related CTN identifier | 503808 |
| 2 | Description | String - 500 | M | Goods description | Electronic Components |
| 3 | HSCode | String - 20 | M | Harmonized system code | 854390 |
| 4 | GrossWeightKG | Decimal | M | Gross weight in kg | 1500.50 |
| 5 | VolumeCBM | Decimal | O | Volume in cubic meters | 12.5 |
| 6 | ValueOfGoods | Decimal | M | Goods value in USD | 15000.00 |
| 7 | NumberOfPackages | Integer | M | Number of packages | 50 |
| 8 | PackagingType | String - 50 | M | Packaging type | Cartons |
| 9 | CountryOfOriginId | Integer | M | Country of origin ID | 45 |
| 10 | GoodsClassificationId | Integer | O | Goods classification ID | 12 |

#### 5.3.4 CTN Containers API

**Endpoint:** `GET /api/ctnContainers`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 200 | O | OData expand parameter | ContainerType |
| 2 | ctn | Integer | M | CTN identifier | 503808 |
| 3 | ctnid | Integer | M | CTN identifier (duplicate) | 503808 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Container record ID | 510046 |
| 2 | CTNId | Integer | M | Related CTN ID | 503808 |
| 3 | ContainerNumber | String - 20 | M | Container number | MSCU1234567 |
| 4 | ContainerTypeId | Integer | M | Container type ID | 1 |
| 5 | SealNumbers | String - 200 | O | Container seal numbers | SEAL123,SEAL456 |
| 6 | TareWeightKG | Decimal | M | Tare weight in kg | 2300.00 |
| 7 | GrossWeightKG | Decimal | M | Gross weight in kg | 18500.00 |
| 8 | NetWeightKG | Decimal | M | Net weight in kg | 16200.00 |

**POST /api/ctnContainers - Create Container Record**

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | CTNId | Integer | M | Related CTN identifier | 503808 |
| 2 | ContainerNumber | String - 20 | M | Container number | MSCU1234567 |
| 3 | ContainerTypeId | Integer | M | Container type identifier | 1 |
| 4 | SealNumbers | String - 200 | O | Container seal numbers | SEAL123,SEAL456 |
| 5 | TareWeightKG | Decimal | M | Tare weight in kg | 2300.00 |
| 6 | GrossWeightKG | Decimal | M | Gross weight in kg | 18500.00 |

**GET /api/ctnContainers/new - Container Template**

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Template ID (null for new) | null |
| 2 | CTNId | Integer | O | CTN ID (to be set) | null |
| 3 | ContainerNumber | String - 20 | O | Empty container number | "" |
| 4 | ContainerTypeId | Integer | O | Default container type | 1 |
| 5 | TareWeightKG | Decimal | O | Default tare weight | 2300.00 |

#### 5.3.5 CTN Addresses API

**Endpoint:** `GET /api/ctnAddresses`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 200 | O | OData expand parameter | QryAddressType,Country1 |
| 2 | ctn | Integer | M | CTN identifier | 503808 |
| 3 | ctnid | Integer | M | CTN identifier (duplicate) | 503808 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Address record ID | 426334 |
| 2 | CTNId | Integer | M | Related CTN ID | 503808 |
| 3 | AddressTypeId | Integer | M | Address type ID | 1 |
| 4 | CompanyName | String - 200 | M | Company name | ABC Trading LLC |
| 5 | ContactPerson | String - 100 | O | Contact person name | John Smith |
| 6 | Address1 | String - 200 | M | Address line 1 | 123 Business Street |
| 7 | Address2 | String - 200 | O | Address line 2 | Suite 456 |
| 8 | City | String - 100 | M | City | Dubai |
| 9 | CountryId | Integer | M | Country identifier | 4 |
| 10 | PostalCode | String - 20 | O | Postal/ZIP code | 12345 |
| 11 | Phone | String - 50 | O | Phone number | +971-4-1234567 |
| 12 | Email | String - 200 | O | Email address | contact@abc-trading.com |

#### 5.3.6 CTN Charges API

**Endpoint:** `GET /api/ctnCharges`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 200 | O | OData expand parameter | Charge,ctn.view_currency |
| 2 | ctn | Integer | M | CTN identifier | 503808 |
| 3 | ctnid | Integer | M | CTN identifier (duplicate) | 503808 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Charge record ID | 12345 |
| 2 | CTNId | Integer | M | Related CTN ID | 503808 |
| 3 | ChargeId | Integer | M | Charge type ID | 1 |
| 4 | Amount | Decimal | M | Charge amount | 150.00 |
| 5 | CurrencyId | Integer | M | Currency identifier | 2 |
| 6 | Description | String - 200 | O | Charge description | Certificate Processing Fee |
| 7 | IsSystem | Boolean | M | System-generated charge flag | true |

#### 5.3.7 User Communication API

**Endpoint:** `GET /api/userCommunication`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 100 | O | OData expand parameter | modifiedby |
| 2 | $sort | String - 100 | O | OData sort parameter | -modifiedon |
| 3 | ctn | Integer | M | CTN identifier | 503808 |
| 4 | ctnid | Integer | M | CTN identifier (duplicate) | 503808 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Communication record ID | 98765 |
| 2 | CTNId | Integer | M | Related CTN ID | 503808 |
| 3 | Subject | String - 200 | M | Communication subject | Document Review Required |
| 4 | Message | String - 2000 | M | Communication message | Please review attached documents |
| 5 | CreatedOn | DateTime | M | Creation timestamp | 2023-11-12T16:45:00Z |
| 6 | CreatedById | Integer | M | User who created the message | 13345 |
| 7 | IsInternal | Boolean | M | Internal communication flag | false |

**POST /api/userCommunication - Create Communication**

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | CTNId | Integer | M | Related CTN identifier | 503808 |
| 2 | Subject | String - 200 | M | Communication subject | Document Review Required |
| 3 | Message | String - 2000 | M | Communication message | Please review attached documents |
| 4 | IsInternal | Boolean | M | Internal communication flag | false |
| 5 | RecipientIds | Array | O | Array of recipient user IDs | [13345, 13346] |

### 5.4 File Management APIs

#### 5.4.1 File Upload API

**Endpoint:** `POST /api/fileupload`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | file | Binary | M | File upload (multipart/form-data) | [binary file data] |
| 2 | fileName | String - 256 | M | Original file name | Bill_of_Lading.pdf |
| 3 | description | String - 500 | O | File description | Original shipping document |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | fileId | String (UUID) | M | Unique file identifier | 0da7461c-2155-4d20-a695-6b7463367327 |
| 2 | fileName | String - 256 | M | Uploaded file name | Bill_of_Lading.pdf |
| 3 | fileSize | Integer | M | File size in bytes | 245760 |
| 4 | mimeType | String - 100 | M | File MIME type | application/pdf |
| 5 | uploadDate | DateTime | M | Upload timestamp | 2023-11-12T14:30:00Z |

**GET /api/fileupload/{fileId} - Download File**

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | fileId | String (UUID) | M | File identifier from URL path | 0da7461c-2155-4d20-a695-6b7463367327 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | contentStream | Base64 Binary | M | Base64 encoded file content | JVBERi0xLjQKJeLjz9MK... |
| 2 | fileName | String - 256 | M | Original file name | Bill_of_Lading.pdf |
| 3 | mimeType | String - 100 | M | File MIME type | application/pdf |
| 4 | fileSize | Integer | M | File size in bytes | 245760 |

### 5.6 Specialized CTN APIs

#### 5.6.1 Parent CTN Relationships API

**Endpoint:** `GET /api/Ctns/GetAllowedParentCtns`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | ctnId | Integer | M | Current CTN identifier | 503808 |
| 2 | $sort | String - 100 | O | OData sort parameter | BL_number |
| 3 | BL_number | String - 50 | O | Filter by Bill of Lading number | MSC123456 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Parent CTN ID | 503800 |
| 2 | CTN_Reference_Number | String - 50 | M | Parent CTN reference | AO-CNT-503800-2023 |
| 3 | BL_number | String - 50 | M | Parent Bill of Lading | MSC123456 |
| 4 | StatusId | Integer | M | Parent CTN status | 2 |
| 5 | CanBeParent | Boolean | M | Eligibility as parent | true |

#### 5.6.2 CTN Export API

**Endpoint:** `GET /api/ctns/export`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 500 | O | OData expand parameter | CargoType,Status,Visum_Agent |
| 2 | $export_format | String - 10 | M | Export format | csv |
| 3 | $sort | String - 100 | O | OData sort parameter | -ModifiedOn |
| 4 | $top | Integer | O | Number of records | 10 |
| 5 | $filter | String - 1000 | O | OData filter expression | StatusId eq 2 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Content | Text/CSV | M | CSV formatted CTN data | "Id","CTN_Reference_Number"... |
| 2 | ContentType | String - 50 | M | Response content type | text/csv |
| 3 | FileName | String - 100 | M | Suggested file name | CTN_Export_20231112.csv |

---

<div style="page-break-before: always;"></div>

## 6. API Capabilities ⚡

### 6.1 Amendment APIs

Amendment APIs provide controlled modification capabilities for existing certificates with ARCCLA approval workflow.

#### 6.1.1 Amendment Request Creation API

**Endpoint:** `POST /api/CTNs/{id}/amendments`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | id | Integer | M | CTN identifier from URL path | 503808 |
| 2 | requestReason | String - 500 | M | Reason for amendment request | Incorrect vessel name provided |
| 3 | businessJustification | String - 1000 | O | Detailed business justification | Customer informed of vessel change after booking |
| 4 | requestedChanges | Array | M | Array of field changes requested | [field change objects] |
| 5 | urgencyLevel | String - 20 | O | Urgency level (Normal, High, Critical) | Normal |

**Requested Changes Array Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | fieldPath | String - 100 | M | JSON path to field being changed | VesselName |
| 2 | fieldName | String - 100 | M | Human-readable field name | Vessel Name |
| 3 | oldValue | String - 500 | M | Current field value | MSC MEDITERRANEAN |
| 4 | newValue | String - 500 | M | Proposed new field value | MAERSK ESSEX |
| 5 | changeReason | String - 200 | M | Specific reason for this field change | Vessel change notification from carrier |

**Sample JSON Request:**
```json
{
  "requestReason": "Incorrect vessel name provided",
  "businessJustification": "Customer informed of vessel change after booking confirmation",
  "urgencyLevel": "Normal",
  "requestedChanges": [
    {
      "fieldPath": "VesselName",
      "fieldName": "Vessel Name",
      "oldValue": "MSC MEDITERRANEAN",
      "newValue": "MAERSK ESSEX",
      "changeReason": "Vessel change notification from carrier"
    },
    {
      "fieldPath": "ETA",
      "fieldName": "Estimated Time of Arrival",
      "oldValue": "2023-12-20T15:30:00Z",
      "newValue": "2023-12-22T10:00:00Z",
      "changeReason": "Updated ETA due to vessel change"
    }
  ]
}
```

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | amendmentId | String (UUID) | M | Unique amendment identifier | a1b2c3d4-e5f6-7890-abcd-1234567890ef |
| 2 | amendmentNumber | String - 50 | M | Sequential amendment number | AMD-503808-001 |
| 3 | status | String - 20 | M | Amendment status | Pending |
| 4 | requestDate | DateTime | M | Amendment request timestamp | 2025-11-13T10:45:00Z |
| 5 | estimatedFee | Decimal | O | Estimated amendment fee | 25.00 |

**Sample JSON Response:**
```json
{
  "amendmentId": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
  "amendmentNumber": "AMD-503808-001",
  "originalCertificateId": "503808",
  "status": "Pending",
  "requestDate": "2025-11-13T10:45:00Z",
  "estimatedFee": 25.00,
  "currency": "USD",
  "submittedBy": 13345,
  "submittedByRole": "CustomsBroker"
}
```

#### 6.1.2 Amendment Status API

**Endpoint:** `GET /api/amendments/{amendmentId}/status`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | amendmentId | String (UUID) | M | Amendment identifier from URL path | a1b2c3d4-e5f6-7890-abcd-1234567890ef |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | amendmentId | String (UUID) | M | Amendment identifier | a1b2c3d4-e5f6-7890-abcd-1234567890ef |
| 2 | amendmentNumber | String - 50 | M | Amendment number | AMD-503808-001 |
| 3 | status | String - 20 | M | Current amendment status | UnderReview |
| 4 | assignedTo | String - 100 | O | ARCCLA broker assigned | John.Smith@arccla.ao |
| 5 | lastUpdated | DateTime | M | Last status update timestamp | 2025-11-13T14:30:00Z |
| 6 | statusHistory | Array | O | Amendment status history | [status history objects] |

#### 6.1.3 Amendment Approval API

**Endpoint:** `PUT /api/amendments/{amendmentId}/approve`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | amendmentId | String (UUID) | M | Amendment identifier from URL path | a1b2c3d4-e5f6-7890-abcd-1234567890ef |
| 2 | decision | String - 20 | M | Approval decision (Approved/Rejected) | Approved |
| 3 | decisionReason | String - 1000 | O | Reason for approval decision | Valid vessel change confirmed |
| 4 | reviewComments | String - 2000 | O | Additional reviewer comments | Amendment approved without issues |
| 5 | amendmentFee | Decimal | O | Final amendment fee | 25.00 |

### 6.2 Cancellation APIs

Cancellation APIs provide controlled termination of certificate requests with financial impact handling.

#### 6.2.1 Cancellation Request Creation API

**Endpoint:** `POST /api/CTNs/{id}/cancellations`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | id | Integer | M | CTN identifier from URL path | 503808 |
| 2 | reasonCode | String - 20 | M | Standardized cancellation reason code | SHIPMENT_CANCELLED |
| 3 | reasonDescription | String - 500 | M | Detailed cancellation reason | Shipment cancelled by customer |
| 4 | additionalDetails | String - 1000 | O | Additional cancellation details | Customer business closure |
| 5 | urgencyLevel | String - 20 | O | Cancellation urgency (Normal, High, Critical) | High |

**Sample JSON Request:**
```json
{
  "reasonCode": "SHIPMENT_CANCELLED",
  "reasonDescription": "Shipment cancelled by customer due to business closure",
  "additionalDetails": "Customer has permanently ceased operations and requires immediate cancellation",
  "urgencyLevel": "High"
}
```

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | cancellationId | String (UUID) | M | Unique cancellation identifier | x1y2z3a4-b5c6-7890-defg-9876543210ab |
| 2 | cancellationNumber | String - 50 | M | Sequential cancellation number | CAN-503808-001 |
| 3 | status | String - 20 | M | Cancellation status | Pending |
| 4 | requestDate | DateTime | M | Cancellation request timestamp | 2025-11-13T11:30:00Z |
| 5 | estimatedRefund | Decimal | O | Estimated refund amount | 125.00 |

**Sample JSON Response:**
```json
{
  "cancellationId": "x1y2z3a4-b5c6-7890-defg-9876543210ab",
  "cancellationNumber": "CAN-503808-001",
  "originalCertificateId": "503808",
  "status": "Pending",
  "requestDate": "2025-11-13T11:30:00Z",
  "estimatedRefund": 125.00,
  "refundCurrency": "USD",
  "submittedBy": 13345,
  "submittedByRole": "CustomsBroker"
}
```

#### 6.2.2 Cancellation Status API

**Endpoint:** `GET /api/cancellations/{cancellationId}/status`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | cancellationId | String (UUID) | M | Cancellation identifier from URL path | x1y2z3a4-b5c6-7890-defg-9876543210ab |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | cancellationId | String (UUID) | M | Cancellation identifier | x1y2z3a4-b5c6-7890-defg-9876543210ab |
| 2 | cancellationNumber | String - 50 | M | Cancellation number | CAN-503808-001 |
| 3 | status | String - 20 | M | Current cancellation status | UnderReview |
| 4 | assignedTo | String - 100 | O | ARCCLA broker assigned | Maria.Santos@arccla.ao |
| 5 | refundStatus | String - 20 | O | Refund processing status | Pending |
| 6 | lastUpdated | DateTime | M | Last status update timestamp | 2025-11-13T15:45:00Z |

### 6.3 Approval Workflow APIs

Approval workflow APIs enable ARCCLA brokers to review and process amendment/cancellation requests.

#### 6.3.1 Pending Requests API

**Endpoint:** `GET /api/approvals/pending`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | requestType | String - 20 | O | Filter by request type (amendments/cancellations) | amendments |
| 2 | priority | String - 20 | O | Filter by priority level | High |
| 3 | assignedTo | String - 100 | O | Filter by assigned broker | current_user |
| 4 | $top | Integer | O | Number of records to return | 20 |
| 5 | $skip | Integer | O | Number of records to skip | 0 |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | requestId | String (UUID) | M | Amendment/Cancellation identifier | a1b2c3d4-e5f6-7890-abcd-1234567890ef |
| 2 | requestType | String - 20 | M | Type of request (Amendment/Cancellation) | Amendment |
| 3 | requestNumber | String - 50 | M | Request number | AMD-503808-001 |
| 4 | certificateId | String - 50 | M | Related certificate ID | 503808 |
| 5 | submittedDate | DateTime | M | Request submission date | 2025-11-13T10:45:00Z |
| 6 | priority | String - 20 | M | Request priority | Normal |
| 7 | submittedBy | String - 100 | M | User who submitted request | CustomsBroker123 |

### 6.4 Status Polling APIs

Status polling APIs provide real-time status updates with eligibility flags for allowed operations.

#### 6.4.1 Enhanced Certificate Status API

**Endpoint:** `GET /api/CTNs/{id}/enhanced-status`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | id | Integer | M | CTN identifier from URL path | 503808 |
| 2 | includeHistory | Boolean | O | Include status change history | true |
| 3 | includeFlags | Boolean | O | Include eligibility flags | true |

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | certificateId | Integer | M | Certificate identifier | 503808 |
| 2 | currentStatus | String - 20 | M | Current certificate status | Approved |
| 3 | statusId | Integer | M | Status identifier | 3 |
| 4 | canAmend | Boolean | M | Amendment eligibility flag | true |
| 5 | canCancel | Boolean | M | Cancellation eligibility flag | true |
| 6 | lastAmendmentDate | DateTime | O | Date of last amendment | 2025-11-10T14:20:00Z |
| 7 | pendingAmendments | Integer | M | Number of pending amendments | 0 |
| 8 | pendingCancellations | Integer | M | Number of pending cancellations | 0 |
| 9 | eligibilityReasons | Object | O | Detailed eligibility explanations | {...} |

**Sample JSON Response:**
```json
{
  "certificateId": 503808,
  "currentStatus": "Approved",
  "statusId": 3,
  "canAmend": true,
  "canCancel": true,
  "lastStatusUpdate": "2025-11-13T09:30:00Z",
  "lastAmendmentDate": null,
  "pendingAmendments": 0,
  "pendingCancellations": 0,
  "eligibilityReasons": {
    "amendmentEligibility": "Certificate is in approved status and within amendment timeframe",
    "cancellationEligibility": "Certificate not yet issued, cancellation allowed with full refund"
  },
  "businessRules": {
    "amendmentTimeLimit": "24 hours after approval",
    "cancellationTimeLimit": "48 hours after approval",
    "maxAmendmentsAllowed": 3
  }
}
```

#### 6.4.2 Webhook Notifications API

**Endpoint:** `POST /api/webhooks/register`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | callbackUrl | String - 500 | M | URL to receive webhook notifications | https://jul.adports.ae/api/webhooks |
| 2 | events | Array | M | Array of events to subscribe to | ["status_changed", "amendment_approved"] |
| 3 | certificateIds | Array | O | Specific certificates to monitor | [503808, 503809] |
| 4 | authToken | String - 100 | O | Authentication token for webhook | webhook_token_123 |

**Webhook Payload Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | eventType | String - 50 | M | Type of event that occurred | status_changed |
| 2 | certificateId | Integer | M | Certificate that triggered event | 503808 |
| 3 | timestamp | DateTime | M | Event occurrence timestamp | 2025-11-13T16:30:00Z |
| 4 | oldStatus | String - 20 | O | Previous status (for status changes) | Submitted |
| 5 | newStatus | String - 20 | O | New status (for status changes) | Approved |
| 6 | data | Object | O | Additional event-specific data | {...} |

**Sample Webhook Payload:**
```json
{
  "eventType": "status_changed",
  "certificateId": 503808,
  "timestamp": "2025-11-13T16:30:00Z",
  "oldStatus": "Submitted",
  "newStatus": "Approved",
  "data": {
    "approvedBy": "arccla_broker_456",
    "approvalComments": "All documentation verified and approved",
    "invoiceNumber": "INV-503808-2025",
    "paymentDueDate": "2025-11-20T23:59:59Z"
  }
}
```

---

<div style="page-break-before: always;"></div>

## 7. Validation Framework ✅

### 7.1 Field-Level Validation Rules

**Text Field Validations:**
- **TXT_001**: Required fields cannot be null or empty
- **TXT_002**: Text fields must not exceed maximum length
- **TXT_003**: Special characters properly escaped for security

**Numeric Field Validations:**
- **NUM_001**: Numeric fields must contain valid numbers
- **NUM_002**: Currency amounts non-negative with max 2 decimal places
- **NUM_003**: Integer IDs must be positive

**Date/Time Validations:**
- **DT_001**: All dates in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ)
- **DT_002**: ETD must be before or equal to ETA
- **DT_003**: Creation dates cannot be in future

### 7.2 Business Logic Validation

**Trade Compliance:**
- **TC_001**: Angola must be origin or destination for CNCA certificates
- **TC_002**: Sanctioned countries require special compliance screening
- **TC_003**: High-value shipments (>$50,000) require enhanced documentation

**Financial Validations:**
- **FIN_001**: Invoice value must match bill of lading value (±5% tolerance)
- **FIN_002**: Currency conversion rates current (within 24 hours)
- **FIN_003**: Payment terms consistent with Incoterms selected

**Workflow State Validations:**
- **ST_001**: Only valid status transitions allowed per business rules
- **ST_002**: Required actions completed before status advancement
- **ST_003**: Role-based permissions validated for status changes

### 7.3 Error Handling Standards

**Error Response Structure:**
```json
{
  "error": {
    "code": "CTN_V001",
    "message": "Bill of Lading number must be unique",
    "severity": "ERROR",
    "field": "BL_number",
    "timestamp": "2025-11-13T16:45:00Z"
  }
}
```

**Performance Standards:**
- **PERF_001**: Field validations complete within 100ms
- **PERF_002**: Business validations complete within 500ms
- **PERF_003**: External validations complete within 2 seconds

---

*End of Interface Control Document*

**Document Status:** DRAFT v1.0  
**Last Updated:** November 13, 2025  
**Next Review:** December 13, 2025

---