# JUL – SINTECE Integration Control Document v3.0

---

<div style="text-align: center;">

![Abu Dhabi Ports Logo](./images/Maqta-logo.png)

# **JUL – SINTECE**
# **Integration Control Document**

</div>

---

<div style="page-break-after: always;"></div>

## Version Control

| Ver | Date | Name | Role | Summary of Changes |
|-----|------|------|------|-------------------|
| 1.0 | 12-Nov-2025 | Linoy Pappachan Malakkaran | Senior Integration Specialist | Initial Draft - Created ICD with technical specifications for JUL-SINTECE integration. Defined API specifications, data models, integration workflows, security requirements, and testing procedures. |
| 2.0 | 13-Nov-2025 | Linoy Pappachan Malakkaran | Senior Integration Specialist | New:<br/>1. Amendment APIs<br/>2. Cancellation APIs<br/>3. Approval workflow specifications<br/>4. Status management with canAmend/canCancel flags<br/>5. Validation framework<br/>6. Enhanced error handling |
| 3.0 | 14-Nov-2025 | Linoy Pappachan Malakkaran | Senior Integration Specialist | New:<br/>1. Keycloak SSO authentication<br/>2. NIF Validation API<br/>3. Invoice Download API<br/>4. CTN Status Retrieval API<br/>5. Consolidated CNCA certificate submission API<br/>6. Updated table formats |

## Version Reviewers / Approvers

| Name | Role | Signoff | Comments |
|------|------|---------|----------|
| TBD | Digital Systems & Solutions Development and Governance Team Leader | | |
| TBD | Digital Systems & Solutions Development and Governance Team Leader | | |

---

<div style="page-break-after: always;"></div>

## Table of Contents

| Section | Title | Page |
|---------|-------|------|
| **1** | **Introduction** | 5 |
| 1.1 | Purpose | 5 |
| 1.2 | Objective | 5 |
| 1.3 | Scope | 5 |
| 1.4 | Overview | 6 |
| 1.5 | Document Structure | 6 |
| 1.6 | Process Flow | 6 |
| 1.7 | Definition of Terms, Acronyms and Abbreviations | 7 |
| 1.8 | Intended Audience | 7 |
| **2** | **Interface Technical Specifications** | 8 |
| **3** | **Functional Requirements** | 9 |
| **4** | **Non-Functional Requirements** | 10 |
| 4.1 | Security | 10 |
| 4.2 | Reliability | 10 |
| 4.3 | Volumetric | 11 |
| **5** | **Master Data APIs** | 12 |
| 5.1 | Cargo Types API | 12 |
| 5.2 | Incoterms API | 14 |
| 5.3 | Countries API | 16 |
| 5.4 | Carriers API | 18 |
| 5.5 | Currencies API | 20 |
| 5.6 | Banks API | 22 |
| 5.7 | Units API | 24 |
| 5.8 | Container Types API | 26 |
| 5.9 | Transport Types API | 28 |
| 5.10 | Locations/Ports API | 30 |
| 5.11 | Goods Classifications API | 32 |
| 5.12 | IMO Codes API | 34 |
| 5.13 | Vessels API | 36 |
| 5.14 | CTN Cities API | 38 |
| 5.15 | CTN Ports API | 40 |
| **6** | **Certificate Management APIs** | 42 |
| 6.1 | CTN Attachments API | 42 |
| 6.2 | CTN Creation API (Certificate Submission) | 44 |
| 6.3 | Request Visa API (Certificate Issuance Submission) | 46 |
| 6.4 | NIF Validation API | 48 |
| 6.5 | Invoice Download API | 50 |
| **7** | **File Management APIs** | 52 |
| 7.1 | File Upload API | 52 |
| **8** | **CTN Related Entity APIs** | 54 |
| 8.1 | Consignees API | 54 |
| 8.2 | Attachment Names API | 56 |
| 8.3 | CTN Tracking API | 58 |
| **9** | **Enhanced API Capabilities** | 60 |
| 9.1 | Amendment APIs | 60 |
| 9.2 | Cancellation APIs | 62 |
| 9.3 | Approval Workflow APIs | 64 |
| 9.4 | Status Polling APIs | 66 |
| **10** | **Validation Framework** | 68 |
| 10.1 | Field-Level Validation Rules | 68 |
| 10.2 | Business Validation Rules | 70 |
| 10.3 | Authentication and Authorization | 72 |
| **11** | **Response Codes & Error Handling** | 74 |
| **12** | **Interface End Points** | 76 |
| **13** | **Appendix – Enclosures** | 78 |

---

<div style="page-break-after: always;"></div>

## 1. Introduction

### 1.1 Purpose

This document defines the integration specifications between JUL (Abu Dhabi Ports) and SINTECE (ARCCLA) systems. Through this integration, JUL will enable CNCA certificate issuance processes including submission, amendment, cancellation, and approval workflows for cargo shipments to Angola.

### 1.2 Objective

Abu Dhabi Ports provides the structure of the APIs to be developed by ARCCLA and ARCCLA will build the services in the same way and provide APIs to Abu Dhabi Ports (JUL System).

### 1.3 Scope

The scope of this document is to establish an integration channel between JUL and SINTECE, specifying the functional and non-functional requirements, services list, services signature, transport protocol and exchanged messages for the integration between JUL and SINTECE.

### 1.4 Overview

CNCA (Certificado Nacional de Carga de Angola) is a mandatory cargo tracking document required for all shipments destined to Angola. JUL system manages certificate requests from shippers/freight forwarders, while SINTECE (ARCCLA's system) processes and approves these certificates. This integration establishes a real-time communication channel for:

- Certificate submission and issuance
- Amendment requests for submitted certificates
- Cancellation requests
- Status tracking and updates
- Master data synchronization
- Document attachment management

### 1.5 Document Structure

This ICD document contains services specifications that serve JUL integration with SINTECE system.

### 1.6 Process Flow

#### Integration Process Flow

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│                 │         │                  │         │                 │
│   JUL System    │◄───────►│  Integration     │◄───────►│  SINTECE        │
│  (Abu Dhabi     │         │  Layer (SOA)     │         │  (ARCCLA)       │
│   Ports)        │         │                  │         │                 │
└─────────────────┘         └──────────────────┘         └─────────────────┘
       │                                                          │
       │                                                          │
       │  1. Submit Certificate Request                          │
       │─────────────────────────────────────────────────────────►│
       │                                                          │
       │  2. Validate & Process                                  │
       │                                                          │
       │  3. Return Certificate Number & Status                  │
       │◄─────────────────────────────────────────────────────────│
       │                                                          │
       │  4. Poll Status Updates                                 │
       │─────────────────────────────────────────────────────────►│
       │                                                          │
       │  5. Receive Status Updates                              │
       │◄─────────────────────────────────────────────────────────│
       │                                                          │
```

### 1.7 Definition of Terms, Acronyms and Abbreviations

| Term | Definition |
|------|------------|
| JUL | Abu Dhabi Ports system for CNCA certificate management |
| SINTECE | ARCCLA's system for certificate processing and approval |
| ARCCLA | Angolan regulatory agency responsible for cargo certification |
| CNCA | Certificado Nacional de Carga de Angola - required certificate for Angola cargo |
| CTN | Certificate/Cargo Tracking Note - internal certificate reference |
| BL | Bill of Lading - shipping document required for certificates |
| DUP | Declaration of Unique Property - unique customs identifier |
| ICD | Integration Control Document |
| SOA | Service Oriented Architecture |
| REST | Representational State Transfer |
| JSON | JavaScript Object Notation |
| SSO | Single Sign-On |
| NIF | Número de Identificação Fiscal (Angola Tax ID) |

### 1.8 Intended Audience

| S. No | Group | Definition |
|-------|-------|------------|
| 1 | Abu Dhabi Ports | JUL System Development and Integration Team |
| 2 | SOA | Service Oriented Architecture (Middleware) |
| 3 | ARCCLA | SINTECE System Development Team |
| 4 | QA Engineers | Testing and validation teams |
| 5 | Business Analysts | Requirements validation and business process owners |

---

<div style="page-break-after: always;"></div>

## 2. Interface Technical Specifications

| S. No | Service Name | Provider | Consumer | Mode of Integration | Description |
|-------|-------------|----------|----------|-------------------|-------------|
| 1. | Cargo Types API | ARCCLA | JUL | REST API | JUL will fetch available cargo types from SINTECE |
| 2. | Incoterms API | ARCCLA | JUL | REST API | JUL will fetch Incoterms master data from SINTECE |
| 3. | Countries API | ARCCLA | JUL | REST API | JUL will fetch country codes from SINTECE |
| 4. | Carriers API | ARCCLA | JUL | REST API | JUL will fetch carrier information from SINTECE |
| 5. | Currencies API | ARCCLA | JUL | REST API | JUL will fetch currency codes from SINTECE |
| 6. | Banks API | ARCCLA | JUL | REST API | JUL will fetch bank information from SINTECE |
| 7. | Units API | ARCCLA | JUL | REST API | JUL will fetch unit of measurement data from SINTECE |
| 8. | Container Types API | ARCCLA | JUL | REST API | JUL will fetch container type codes from SINTECE |
| 9. | Transport Types API | ARCCLA | JUL | REST API | JUL will fetch transport mode information from SINTECE |
| 10. | Locations/Ports API | ARCCLA | JUL | REST API | JUL will fetch port and location master data from SINTECE |
| 11. | Goods Classifications API | ARCCLA | JUL | REST API | JUL will fetch HS code and goods classification data from SINTECE |
| 12. | IMO Codes API | ARCCLA | JUL | REST API | JUL will fetch IMO dangerous goods codes from SINTECE |
| 13. | Vessels API | ARCCLA | JUL | REST API | JUL will fetch vessel master data from SINTECE |
| 14. | CTN Cities API | ARCCLA | JUL | REST API | JUL will fetch city information from SINTECE |
| 15. | CTN Ports API | ARCCLA | JUL | REST API | JUL will fetch CTN-specific port data from SINTECE |
| 16. | CTN Attachments API | ARCCLA | JUL | REST API | JUL will fetch required document attachment types from SINTECE |
| 17. | CTN Creation API | ARCCLA | JUL | REST API | JUL will submit certificate requests to SINTECE |
| 18. | Request Visa API | ARCCLA | JUL | REST API | JUL will submit complete certificate issuance requests to SINTECE |
| 19. | NIF Validation API | ARCCLA | JUL | REST API | JUL will validate Angola Tax IDs (NIF) with SINTECE |
| 20. | Invoice Download API | ARCCLA | JUL | REST API | JUL will fetch invoice documents from SINTECE |
| 21. | File Upload API | JUL | ARCCLA | REST API | ARCCLA will upload attachments to JUL |
| 22. | Consignees API | ARCCLA | JUL | REST API | JUL will fetch consignee information from SINTECE |
| 23. | Attachment Names API | ARCCLA | JUL | REST API | JUL will fetch attachment naming conventions from SINTECE |
| 24. | CTN Tracking API | ARCCLA | JUL | REST API | JUL will retrieve certificate status from SINTECE |
| 25. | Amendment Request API | ARCCLA | JUL | REST API | JUL will submit certificate amendment requests to SINTECE |
| 26. | Cancellation Request API | ARCCLA | JUL | REST API | JUL will submit certificate cancellation requests to SINTECE |
| 27. | Approval Workflow API | ARCCLA | JUL | REST API | JUL will retrieve approval workflow status from SINTECE |
| 28. | Status Polling API | ARCCLA | JUL | REST API | JUL will poll for certificate status updates from SINTECE |

---

<div style="page-break-after: always;"></div>

## 3. Functional Requirements

JUL will publish certificate requests to SINTECE in real-time. Certificate data will be published in real-time and in case of any updated/deleted data it will be re-pushed to SINTECE.

- **Certificate Submission**: JUL will send CNCA certificate requests to SINTECE for validation and issuance. Certificates can be submitted in draft mode for validation or final submission mode for issuance.

- **Master Data Synchronization**: JUL will fetch master data (cargo types, countries, ports, vessels, etc.) from SINTECE through dedicated APIs. This data will be cached locally and refreshed periodically.

- **Amendment Processing**: After certificate submission, users can request amendments if the certificate status allows (canAmend flag = true). Amendments require ARCCLA approval.

- **Cancellation Processing**: Users can request certificate cancellations if the status allows (canCancel flag = true). Cancellations require ARCCLA approval.

- **Status Tracking**: JUL will poll SINTECE for certificate status updates. Status changes will be reflected in real-time in the JUL system.

- **Approval Workflows**: ARCCLA will review and approve/reject certificate requests, amendments, and cancellations through SINTECE. JUL will reflect approval statuses.

- **Document Management**: Required documents (BL, Invoice, Packing List, etc.) will be uploaded to JUL and referenced in certificate submissions to SINTECE.

- **NIF Validation**: Angola Tax Registration Numbers (NIF) will be validated through SINTECE before certificate submission.

- **Invoice Management**: Approved certificates generate invoices in SINTECE. JUL can download these invoices for payment processing.

---

<div style="page-break-after: always;"></div>

## 4. Non-Functional Requirements

### 4.1 Security

**Authentication**

Connectivity between JUL and SINTECE will be through secure HTTPS with Keycloak SSO authentication. Authentication will be done using OAuth 2.0 / OpenID Connect with JWT tokens.

**Key Security Requirements:**
- All API endpoints must use HTTPS (TLS 1.2 or higher)
- JWT tokens must be validated on every request
- Token expiration: 30 minutes (configurable)
- Refresh token support required
- API rate limiting: 100 requests per minute per client
- IP whitelisting for production environments

**Authorization**

Role-based access control (RBAC) will be implemented:
- **Shipper**: Can submit, amend, cancel certificates
- **Freight Forwarder**: Can submit, amend, cancel certificates on behalf of shippers
- **ARCCLA Officer**: Can approve/reject requests
- **System Administrator**: Full access to all operations

### 4.2 Reliability

**High Availability**

Each entity has high availability for the production environment at all levels:
- Minimum 99.9% uptime SLA
- Load balancing across multiple application servers
- Database replication with failover support
- Automated health checks every 60 seconds

**Disaster Recovery**

DR failover on any of the two sides will be done manually. In case of source failure, the DR switchover is seamless on the target side. But when the target fails, the source needs to point to the new target.

- Recovery Time Objective (RTO): 4 hours
- Recovery Point Objective (RPO): 1 hour
- Automated backup every 6 hours
- Regular DR drills quarterly

**Error Handling**

- Retry logic for transient failures (3 attempts with exponential backoff)
- Circuit breaker pattern for downstream service failures
- Comprehensive error logging and monitoring
- Alerting for critical failures

### 4.3 Volumetric

Average response time expectations:

| Operation Type | Expected Response Time | Maximum Response Time |
|---------------|----------------------|---------------------|
| Master Data API | 200ms | 500ms |
| Certificate Submission | 2 seconds | 5 seconds |
| File Upload | 5 seconds | 15 seconds |
| Status Polling | 100ms | 300ms |
| NIF Validation | 1 second | 3 seconds |

**Volume Expectations:**

- **Certificate Submissions**: 500 per day (peak: 100 per hour)
- **Status Polling**: 10,000 requests per day
- **Master Data Sync**: Once per day (scheduled)
- **File Uploads**: 1,500 per day (average 2-3 files per certificate)
- **Concurrent Users**: 50
- **Peak Concurrent Users**: 100

**Data Retention:**

- Active certificates: Online storage for 2 years
- Historical certificates: Archive storage for 7 years
- Audit logs: 5 years
- Application logs: 90 days

---

<div style="page-break-after: always;"></div>

## 5. Master Data APIs

### 5.1 Cargo Types API

#### 5.1.1 Overview

This method allows JUL to retrieve the list of available cargo types from SINTECE. Cargo types are used during certificate submission to classify the type of goods being shipped.

| Operation Name | GetCargoTypes |
|---------------|---------------|
| Request URL | Will be provided by ARCCLA |
| Data Provider | ARCCLA |
| Consumer | JUL |
| Business Purpose | JUL to fetch cargo type master data from SINTECE |
| Pattern | Synchronous |
| Method | GET |
| Endpoint | /api/v1/master-data/cargo-types |

#### 5.1.2 Request and Response Elements

**Request Elements**

| S. No | Attributes | Data Type - Length | Condition (Mandatory/ Optional) | Lookup id | Format/Derivation logic for fields | Data Example |
|-------|-----------|-------------------|--------------------------------|-----------|----------------------------------|--------------|
| 1. | page | Number - 10 | O | | Page number for pagination. Default: 1 | 1 |
| 2. | pageSize | Number - 10 | O | | Number of records per page. Default: 100, Max: 500 | 100 |
| 3. | searchTerm | String - 100 | O | | Filter results by name or code | "Container" |
| 4. | active | Boolean | O | | Filter by active status. Default: true | true |

**Response Elements**

| S. No | Attributes | Data Type - Length | Condition (Mandatory/ Optional) | Format/Derivation logic for fields | Data Example |
|-------|-----------|-------------------|---------------------------------|----------------------------------|--------------|
| 1. | success | Boolean | M | Indicates if the request was successful | true |
| 2. | message | String - 500 | O | Response message | "Cargo types retrieved successfully" |
| 3. | statusCode | Number - 3 | M | HTTP status code | 200 |
| 4. | timestamp | DateTime | M | Response timestamp in ISO 8601 format | "2025-11-14T10:30:00Z" |
| 5. | data | Object | M | Container for response data | {...} |

**CargoTypes Array (within data object)**

| S. No | Attributes | Data Type - Length | Condition (Mandatory/ Optional) | Format/Derivation logic for fields | Data Example |
|-------|-----------|-------------------|---------------------------------|----------------------------------|--------------|
| 6. | id | Number - 20 | M | Unique identifier for cargo type | 1 |
| 7. | code | String - 20 | M | Cargo type code | "CONT_GENERAL" |
| 8. | nameEn | String - 200 | M | Cargo type name in English | "General Containerized Cargo" |
| 9. | nameFr | String - 200 | O | Cargo type name in French | "Marchandises Générales Conteneurisées" |
| 10. | description | String - 500 | O | Detailed description | "Standard containerized goods" |
| 11. | isActive | Boolean | M | Indicates if cargo type is active | true |
| 12. | requiresIMO | Boolean | M | Indicates if IMO classification is required | false |
| 13. | createdAt | DateTime | M | Creation timestamp | "2025-01-01T00:00:00Z" |
| 14. | updatedAt | DateTime | M | Last update timestamp | "2025-11-14T10:00:00Z" |

**Pagination Object (within data)**

| S. No | Attributes | Data Type - Length | Condition (Mandatory/ Optional) | Format/Derivation logic for fields | Data Example |
|-------|-----------|-------------------|---------------------------------|----------------------------------|--------------|
| 15. | currentPage | Number - 10 | M | Current page number | 1 |
| 16. | pageSize | Number - 10 | M | Records per page | 100 |
| 17. | totalRecords | Number - 10 | M | Total number of records | 25 |
| 18. | totalPages | Number - 10 | M | Total number of pages | 1 |

#### 5.1.3 Schema Definition

```json
{
  "success": true,
  "message": "Cargo types retrieved successfully",
  "statusCode": 200,
  "timestamp": "2025-11-14T10:30:00Z",
  "data": {
    "cargoTypes": [
      {
        "id": 1,
        "code": "CONT_GENERAL",
        "nameEn": "General Containerized Cargo",
        "nameFr": "Marchandises Générales Conteneurisées",
        "description": "Standard containerized goods",
        "isActive": true,
        "requiresIMO": false,
        "createdAt": "2025-01-01T00:00:00Z",
        "updatedAt": "2025-11-14T10:00:00Z"
      }
    ],
    "pagination": {
      "currentPage": 1,
      "pageSize": 100,
      "totalRecords": 25,
      "totalPages": 1
    }
  }
}
```

#### 5.1.4 Request and Response Samples

**Request Sample (GET)**

```
GET /api/v1/master-data/cargo-types?page=1&pageSize=100&active=true
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

**Response Sample (Success - 200)**

```json
{
  "success": true,
  "message": "Cargo types retrieved successfully",
  "statusCode": 200,
  "timestamp": "2025-11-14T10:30:00Z",
  "data": {
    "cargoTypes": [
      {
        "id": 1,
        "code": "CONT_GENERAL",
        "nameEn": "General Containerized Cargo",
        "nameFr": "Marchandises Générales Conteneurisées",
        "description": "Standard containerized goods",
        "isActive": true,
        "requiresIMO": false,
        "createdAt": "2025-01-01T00:00:00Z",
        "updatedAt": "2025-11-14T10:00:00Z"
      },
      {
        "id": 2,
        "code": "BULK_DRY",
        "nameEn": "Dry Bulk Cargo",
        "nameFr": "Vrac Sec",
        "description": "Dry bulk commodities",
        "isActive": true,
        "requiresIMO": false,
        "createdAt": "2025-01-01T00:00:00Z",
        "updatedAt": "2025-11-14T10:00:00Z"
      }
    ],
    "pagination": {
      "currentPage": 1,
      "pageSize": 100,
      "totalRecords": 2,
      "totalPages": 1
    }
  }
}
```

**Response Sample (Error - 401)**

```json
{
  "success": false,
  "message": "Unauthorized access. Invalid or expired token.",
  "statusCode": 401,
  "timestamp": "2025-11-14T10:30:00Z",
  "errors": [
    {
      "code": "AUTH_ERROR",
      "message": "JWT token validation failed"
    }
  ]
}
```

---

<div style="page-break-after: always;"></div>

## 6. Certificate Management APIs

### 6.1 CTN Creation API (Certificate Submission)

#### 6.1.1 Overview

This method allows JUL to submit a CNCA certificate request to SINTECE. The certificate can be submitted in draft mode for validation or final submission mode for processing.

| Operation Name | SubmitCertificate |
|---------------|------------------|
| Request URL | Will be provided by ARCCLA |
| Data Provider | JUL |
| Consumer | ARCCLA |
| Business Purpose | JUL to submit certificate requests to SINTECE |
| Pattern | Synchronous |
| Method | POST |
| Endpoint | /api/v1/certificates/submit |

#### 6.1.2 Request and Response Elements

**Request Elements**

| S. No | Attributes | Data Type - Length | Condition (Mandatory/ Optional) | Lookup id | Format/Derivation logic for fields | Data Example |
|-------|-----------|-------------------|---------------------------------|-----------|----------------------------------|--------------|
| **General Information** |
| 1. | isDraft | Boolean | M | | Indicates if submission is draft. true=Draft validation only, false=Final submission | false |
| 2. | referenceNumber | String - 50 | O | | Client's internal reference number | "REF-2025-001" |
| **Shipper Information** |
| 3. | shipperName | String - 200 | M | | Full legal name of shipper | "ABC Trading Company Ltd" |
| 4. | shipperAddress | String - 500 | M | | Complete shipper address | "123 Trade Street, Dubai, UAE" |
| 5. | shipperCountryCode | String - 3 | M | | ISO 3166-1 alpha-3 country code | "ARE" |
| 6. | shipperPhone | String - 20 | M | | Contact phone number with country code | "+971501234567" |
| 7. | shipperEmail | String - 100 | M | | Valid email address | "contact@abctrading.com" |
| 8. | shipperTaxId | String - 50 | O | | Tax registration number | "123456789" |
| **Consignee Information** |
| 9. | consigneeId | Number - 20 | M | | Consignee ID from SINTECE | 12345 |
| 10. | consigneeName | String - 200 | M | | Full legal name of consignee | "XYZ Import Ltd" |
| 11. | consigneeAddress | String - 500 | M | | Complete consignee address in Angola | "456 Luanda Avenue, Luanda, Angola" |
| 12. | consigneeNIF | String - 20 | M | | Angola Tax ID (validated via NIF API) | "5000123456" |
| 13. | consigneePhone | String - 20 | M | | Contact phone number | "+244912345678" |
| 14. | consigneeEmail | String - 100 | M | | Valid email address | "import@xyzcompany.ao" |
| **Transport Information** |
| 15. | transportMode | String - 20 | M | | MARITIME, AIR, ROAD, RAIL | "MARITIME" |
| 16. | carrierCode | String - 20 | M | | Carrier code from SINTECE | "MAERSK" |
| 17. | vesselName | String - 200 | M (if Maritime) | | Name of vessel | "MSC MEDITERRANEAN" |
| 18. | voyageNumber | String - 50 | M (if Maritime) | | Voyage/flight number | "VOY-2025-123" |
| 19. | portOfLoadingCode | String - 10 | M | | UN/LOCODE of loading port | "AEJEA" |
| 20. | portOfDischargeCode | String - 10 | M | | UN/LOCODE of discharge port in Angola | "AOLAD" |
| 21. | estimatedDepartureDate | Date | M | | ISO 8601 date format | "2025-12-01" |
| 22. | estimatedArrivalDate | Date | M | | ISO 8601 date format | "2025-12-15" |
| **Cargo Information** |
| 23. | billOfLadingNumber | String - 50 | M | | BL/AWB number | "MAEU123456789" |
| 24. | cargoTypeCode | String - 20 | M | | Code from Cargo Types API | "CONT_GENERAL" |
| 25. | totalGrossWeight | Number - 15,3 | M | | Total weight in kg | 25000.500 |
| 26. | totalVolume | Number - 15,3 | M | | Total volume in m³ | 60.000 |
| 27. | numberOfPackages | Number - 10 | M | | Total number of packages | 500 |
| 28. | packageType | String - 50 | M | | Type of packaging | "Cartons" |
| **Container Information** |
| 29. | containers | Array | M (if containerized) | | Array of container objects | [...] |
| 30. | containers[].number | String - 20 | M | | Container number (ISO 6346) | "MAEU1234567" |
| 31. | containers[].typeCode | String - 10 | M | | Container type code | "20GP" |
| 32. | containers[].sealNumber | String - 50 | M | | Container seal number | "SEAL123456" |
| 33. | containers[].grossWeight | Number - 15,3 | M | | Weight in kg | 20000.000 |
| **Commercial Information** |
| 34. | invoiceNumber | String - 50 | M | | Commercial invoice number | "INV-2025-001" |
| 35. | invoiceDate | Date | M | | ISO 8601 date format | "2025-11-10" |
| 36. | invoiceAmount | Number - 15,2 | M | | Total invoice amount | 50000.00 |
| 37. | invoiceCurrency | String - 3 | M | | ISO 4217 currency code | "USD" |
| 38. | incotermCode | String - 3 | M | | Incoterms 2020 code | "CIF" |
| 39. | incotermLocation | String - 100 | M | | Incoterms location | "Luanda Port" |
| **Goods Details** |
| 40. | goods | Array | M | | Array of goods line items | [...] |
| 41. | goods[].lineNumber | Number - 5 | M | | Sequential line number | 1 |
| 42. | goods[].hsCode | String - 10 | M | | HS Code (6-8 digits) | "8703.2319" |
| 43. | goods[].description | String - 1000 | M | | Detailed goods description | "Motor vehicles, spark-ignition engine" |
| 44. | goods[].quantity | Number - 15,3 | M | | Quantity | 10.000 |
| 45. | goods[].unitCode | String - 10 | M | | Unit of measurement code | "NMB" |
| 46. | goods[].grossWeight | Number - 15,3 | M | | Weight in kg | 15000.000 |
| 47. | goods[].volume | Number - 15,3 | O | | Volume in m³ | 30.000 |
| 48. | goods[].unitPrice | Number - 15,2 | M | | Price per unit | 5000.00 |
| 49. | goods[].totalValue | Number - 15,2 | M | | Line total value | 50000.00 |
| 50. | goods[].originCountryCode | String - 3 | M | | ISO 3166-1 alpha-3 code | "JPN" |
| 51. | goods[].isDangerous | Boolean | M | | Indicates if goods are dangerous | false |
| 52. | goods[].imoClass | String - 10 | O (M if isDangerous) | | IMO class code | "3" |
| 53. | goods[].unNumber | String - 10 | O (M if isDangerous) | | UN Number | "UN1203" |
| **Attachments** |
| 54. | attachments | Array | M | | Array of document references | [...] |
| 55. | attachments[].documentType | String - 50 | M | | Type from Attachment Names API | "COMMERCIAL_INVOICE" |
| 56. | attachments[].fileId | String - 100 | M | | File ID from File Upload API | "file_abc123xyz" |
| 57. | attachments[].fileName | String - 255 | M | | Original filename | "invoice_INV-2025-001.pdf" |
| 58. | attachments[].fileSize | Number - 10 | M | | File size in bytes | 524288 |

**Response Elements**

| S. No | Attributes | Data Type - Length | Condition (Mandatory/ Optional) | Format/Derivation logic for fields | Data Example |
|-------|-----------|-------------------|---------------------------------|----------------------------------|--------------|
| 1. | success | Boolean | M | Indicates if the request was successful | true |
| 2. | message | String - 500 | M | Response message | "Certificate submitted successfully" |
| 3. | statusCode | Number - 3 | M | HTTP status code | 200 |
| 4. | timestamp | DateTime | M | Response timestamp in ISO 8601 format | "2025-11-14T10:30:00Z" |
| 5. | data | Object | M | Container for response data | {...} |

**Certificate Data Object**

| S. No | Attributes | Data Type - Length | Condition (Mandatory/ Optional) | Format/Derivation logic for fields | Data Example |
|-------|-----------|-------------------|---------------------------------|----------------------------------|--------------|
| 6. | certificateNumber | String - 50 | M | Unique CNCA certificate number | "CNCA-2025-000123" |
| 7. | referenceNumber | String - 50 | O | Client reference from request | "REF-2025-001" |
| 8. | status | String - 50 | M | Current certificate status | "SUBMITTED" |
| 9. | statusDescription | String - 200 | M | Status description | "Certificate has been submitted for review" |
| 10. | canAmend | Boolean | M | Indicates if amendment is allowed | false |
| 11. | canCancel | Boolean | M | Indicates if cancellation is allowed | true |
| 12. | submittedAt | DateTime | M | Submission timestamp | "2025-11-14T10:30:00Z" |
| 13. | estimatedApprovalDate | Date | O | Expected approval date | "2025-11-16" |
| 14. | invoiceNumber | String - 50 | O | SINTECE invoice number (if generated) | "INV-SINTECE-2025-456" |
| 15. | invoiceAmount | Number - 15,2 | O | Invoice amount in USD | 250.00 |
| 16. | warnings | Array | O | Array of warning messages | [...] |
| 17. | warnings[].code | String - 50 | O | Warning code | "WARN_IMO_CHECK" |
| 18. | warnings[].message | String - 500 | O | Warning description | "Please verify IMO classification for HS Code 8703.2319" |

#### 6.1.3 Schema Definition

See appendix for complete JSON schema.

#### 6.1.4 Request and Response Samples

**Request Sample (POST)**

```json
{
  "isDraft": false,
  "referenceNumber": "REF-2025-001",
  "shipperName": "ABC Trading Company Ltd",
  "shipperAddress": "123 Trade Street, Dubai, UAE",
  "shipperCountryCode": "ARE",
  "shipperPhone": "+971501234567",
  "shipperEmail": "contact@abctrading.com",
  "consigneeId": 12345,
  "consigneeName": "XYZ Import Ltd",
  "consigneeAddress": "456 Luanda Avenue, Luanda, Angola",
  "consigneeNIF": "5000123456",
  "consigneePhone": "+244912345678",
  "consigneeEmail": "import@xyzcompany.ao",
  "transportMode": "MARITIME",
  "carrierCode": "MAERSK",
  "vesselName": "MSC MEDITERRANEAN",
  "voyageNumber": "VOY-2025-123",
  "portOfLoadingCode": "AEJEA",
  "portOfDischargeCode": "AOLAD",
  "estimatedDepartureDate": "2025-12-01",
  "estimatedArrivalDate": "2025-12-15",
  "billOfLadingNumber": "MAEU123456789",
  "cargoTypeCode": "CONT_GENERAL",
  "totalGrossWeight": 25000.500,
  "totalVolume": 60.000,
  "numberOfPackages": 500,
  "packageType": "Cartons",
  "containers": [
    {
      "number": "MAEU1234567",
      "typeCode": "20GP",
      "sealNumber": "SEAL123456",
      "grossWeight": 20000.000
    }
  ],
  "invoiceNumber": "INV-2025-001",
  "invoiceDate": "2025-11-10",
  "invoiceAmount": 50000.00,
  "invoiceCurrency": "USD",
  "incotermCode": "CIF",
  "incotermLocation": "Luanda Port",
  "goods": [
    {
      "lineNumber": 1,
      "hsCode": "8703.2319",
      "description": "Motor vehicles with spark-ignition internal combustion piston engine",
      "quantity": 10.000,
      "unitCode": "NMB",
      "grossWeight": 15000.000,
      "volume": 30.000,
      "unitPrice": 5000.00,
      "totalValue": 50000.00,
      "originCountryCode": "JPN",
      "isDangerous": false
    }
  ],
  "attachments": [
    {
      "documentType": "COMMERCIAL_INVOICE",
      "fileId": "file_abc123xyz",
      "fileName": "invoice_INV-2025-001.pdf",
      "fileSize": 524288
    },
    {
      "documentType": "BILL_OF_LADING",
      "fileId": "file_def456uvw",
      "fileName": "bl_MAEU123456789.pdf",
      "fileSize": 312576
    }
  ]
}
```

**Response Sample (Success - 200)**

```json
{
  "success": true,
  "message": "Certificate submitted successfully",
  "statusCode": 200,
  "timestamp": "2025-11-14T10:30:00Z",
  "data": {
    "certificateNumber": "CNCA-2025-000123",
    "referenceNumber": "REF-2025-001",
    "status": "SUBMITTED",
    "statusDescription": "Certificate has been submitted for review",
    "canAmend": false,
    "canCancel": true,
    "submittedAt": "2025-11-14T10:30:00Z",
    "estimatedApprovalDate": "2025-11-16",
    "invoiceNumber": "INV-SINTECE-2025-456",
    "invoiceAmount": 250.00,
    "warnings": []
  }
}
```

**Response Sample (Validation Error - 400)**

```json
{
  "success": false,
  "message": "Validation failed",
  "statusCode": 400,
  "timestamp": "2025-11-14T10:30:00Z",
  "errors": [
    {
      "field": "consigneeNIF",
      "code": "INVALID_NIF",
      "message": "NIF validation failed. Please verify the Angola Tax ID."
    },
    {
      "field": "goods[0].hsCode",
      "code": "INVALID_HS_CODE",
      "message": "HS Code 8703.2319 is not valid. Please use 8 digits."
    }
  ]
}
```

---

<div style="page-break-after: always;"></div>

## 10. Validation Framework

### 10.1 Field-Level Validation Rules

All API requests must comply with the following validation rules:

#### General Field Validations

| Field Type | Validation Rule | Error Code | Error Message |
|------------|----------------|------------|---------------|
| String (Required) | Not null, not empty, no whitespace only | FIELD_REQUIRED | "{fieldName} is required and cannot be empty" |
| String (Length) | Length must be within min-max range | FIELD_LENGTH_INVALID | "{fieldName} must be between {min} and {max} characters" |
| Number (Required) | Not null, must be numeric | FIELD_REQUIRED | "{fieldName} is required and must be a valid number" |
| Number (Range) | Value must be within min-max range | VALUE_OUT_OF_RANGE | "{fieldName} must be between {min} and {max}" |
| Date | Valid ISO 8601 format (YYYY-MM-DD) | INVALID_DATE_FORMAT | "{fieldName} must be in format YYYY-MM-DD" |
| DateTime | Valid ISO 8601 format with timezone | INVALID_DATETIME_FORMAT | "{fieldName} must be in ISO 8601 format" |
| Email | Valid email format (RFC 5322) | INVALID_EMAIL | "{fieldName} must be a valid email address" |
| Phone | Valid international format with country code | INVALID_PHONE | "{fieldName} must be a valid phone number with country code" |
| Boolean | Must be true or false | INVALID_BOOLEAN | "{fieldName} must be either true or false" |

#### Business-Specific Validations

| Field | Validation Rule | Error Code | Error Message |
|-------|----------------|------------|---------------|
| consigneeNIF | Must pass NIF Validation API | INVALID_NIF | "NIF validation failed. Please verify the Angola Tax ID." |
| hsCode | Must be 6, 8, or 10 digits, exist in Goods Classification API | INVALID_HS_CODE | "HS Code {value} is invalid or not found" |
| portOfLoadingCode | Must exist in Locations/Ports API | INVALID_PORT_CODE | "Port of Loading code {value} is invalid" |
| portOfDischargeCode | Must exist in CTN Ports API, must be in Angola | INVALID_DISCHARGE_PORT | "Port of Discharge must be a valid Angola port" |
| carrierCode | Must exist in Carriers API | INVALID_CARRIER | "Carrier code {value} is invalid or not active" |
| cargoTypeCode | Must exist in Cargo Types API | INVALID_CARGO_TYPE | "Cargo type code {value} is invalid" |
| incotermCode | Must exist in Incoterms API | INVALID_INCOTERM | "Incoterm code {value} is invalid" |
| transportMode | Must be: MARITIME, AIR, ROAD, or RAIL | INVALID_TRANSPORT_MODE | "Transport mode must be MARITIME, AIR, ROAD, or RAIL" |
| containers[].number | Must match ISO 6346 format (4 letters + 7 digits) | INVALID_CONTAINER_NUMBER | "Container number {value} does not match ISO 6346 format" |
| estimatedArrivalDate | Must be after estimatedDepartureDate | INVALID_DATE_RANGE | "Estimated arrival date must be after departure date" |
| invoiceAmount | Must equal sum of goods[].totalValue | AMOUNT_MISMATCH | "Invoice amount must equal the sum of all goods line items" |
| totalGrossWeight | Must equal sum of goods[].grossWeight | WEIGHT_MISMATCH | "Total gross weight must equal the sum of all goods weights" |

### 10.2 Business Validation Rules

#### Certificate Submission Validations

1. **Consignee NIF Validation**
   - NIF must be validated through NIF Validation API before certificate submission
   - NIF must be active and registered in Angola

2. **Port Validation**
   - Port of Loading can be any valid international port
   - Port of Discharge must be a valid port in Angola (country code = AGO)

3. **Date Validations**
   - Invoice Date must not be in the future
   - Estimated Departure Date must be >= current date
   - Estimated Arrival Date must be > Estimated Departure Date
   - Estimated Arrival Date should not exceed 60 days from Estimated Departure Date

4. **Container Validations** (if containerized cargo)
   - Total number of containers must match the sum of declared containers
   - Sum of container gross weights must equal totalGrossWeight
   - Container type codes must be valid from Container Types API

5. **Goods Line Items Validations**
   - At least one goods line item is required
   - Line numbers must be sequential starting from 1
   - HS Code must be valid for the origin country
   - If isDangerous = true, imoClass and unNumber are mandatory
   - Unit codes must be valid from Units API
   - Sum of goods[].totalValue must equal invoiceAmount
   - Sum of goods[].grossWeight must equal totalGrossWeight

6. **Attachment Validations**
   - Minimum required documents: COMMERCIAL_INVOICE, BILL_OF_LADING, PACKING_LIST
   - All fileIds must be valid (previously uploaded via File Upload API)
   - File sizes must not exceed 10MB per file
   - Total attachments size must not exceed 50MB
   - Accepted formats: PDF, JPG, JPEG, PNG

7. **Amendment Validations**
   - Certificate must have canAmend = true
   - Amendment reason must be provided and not empty
   - Only specific fields can be amended based on current status

8. **Cancellation Validations**
   - Certificate must have canCancel = true
   - Cancellation reason must be provided and not empty
   - Once cancelled, certificate cannot be reinstated

### 10.3 Authentication and Authorization

#### 10.3.1 SSO Solution - Keycloak

Abu Dhabi Ports uses Keycloak as the Single Sign-On (SSO) solution for authentication and authorization across all integrated systems including JUL-SINTECE integration.

**Keycloak Configuration:**

| Configuration | Value |
|---------------|-------|
| Keycloak Server URL | https://sso.adports.ae (Production)<br/>https://sso-uat.adports.ae (UAT) |
| Realm | ADP-External-Services |
| Client ID | jul-sintece-integration |
| Client Authentication | Client ID and Secret |
| Token Type | JWT (JSON Web Tokens) |
| Token Signing Algorithm | RS256 |
| Access Token Lifespan | 30 minutes |
| Refresh Token Lifespan | 8 hours |
| SSL Required | All requests |

#### 10.3.2 Supported Authentication Protocols

1. **OAuth 2.0 Client Credentials Flow** (Recommended for system-to-system)
2. **OpenID Connect (OIDC)**
3. **SAML 2.0** (If required)

#### 10.3.3 JWT Token Management

**Token Request Example:**

```http
POST https://sso.adports.ae/auth/realms/ADP-External-Services/protocol/openid-connect/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id=jul-sintece-integration
&client_secret={client_secret}
&scope=openid profile email
```

**Token Response Example:**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 1800,
  "refresh_expires_in": 28800,
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "not-before-policy": 0,
  "session_state": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "scope": "openid profile email"
}
```

**Using the Access Token:**

```http
GET https://api.sintece.ao/api/v1/master-data/cargo-types
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json
```

**JWT Token Structure:**

```json
{
  "header": {
    "alg": "RS256",
    "typ": "JWT",
    "kid": "key-id-123"
  },
  "payload": {
    "exp": 1700000000,
    "iat": 1699998200,
    "jti": "unique-token-id",
    "iss": "https://sso.adports.ae/auth/realms/ADP-External-Services",
    "aud": "jul-sintece-integration",
    "sub": "service-account-jul-sintece",
    "typ": "Bearer",
    "azp": "jul-sintece-integration",
    "acr": "1",
    "realm_access": {
      "roles": [
        "certificate_submit",
        "certificate_amend",
        "certificate_cancel",
        "master_data_read"
      ]
    },
    "resource_access": {
      "jul-sintece-integration": {
        "roles": [
          "api_access"
        ]
      }
    },
    "scope": "openid profile email",
    "clientId": "jul-sintece-integration",
    "clientHost": "10.0.0.1",
    "preferred_username": "service-account-jul-sintece"
  }
}
```

#### 10.3.4 Role-Based Access Control (RBAC)

| Role | Permissions | Description |
|------|------------|-------------|
| certificate_submit | POST /api/v1/certificates/submit | Can submit new certificates |
| certificate_amend | POST /api/v1/certificates/amend | Can submit amendment requests |
| certificate_cancel | POST /api/v1/certificates/cancel | Can submit cancellation requests |
| certificate_read | GET /api/v1/certificates/* | Can retrieve certificate information |
| master_data_read | GET /api/v1/master-data/* | Can fetch master data |
| file_upload | POST /api/v1/files/upload | Can upload attachments |
| invoice_download | GET /api/v1/invoices/* | Can download invoices |
| admin | ALL | Full system access |

#### 10.3.5 Integration Requirements

**For ARCCLA/SINTECE Team:**

1. Register a new client in Keycloak with client ID: `sintece-jul-integration`
2. Configure client authentication method: Client ID and Secret
3. Request client credentials from Abu Dhabi Ports Keycloak administrators
4. Implement OAuth 2.0 Client Credentials flow in SINTECE APIs
5. Validate JWT tokens on every incoming API request
6. Verify token signature using Keycloak public keys
7. Check token expiration and required roles/scopes
8. Implement token refresh logic for long-running processes

**Security Best Practices:**

1. **Never** log or expose client secrets in application logs
2. Store client secrets securely (environment variables, secret management systems)
3. Implement token caching to avoid unnecessary token requests
4. Use HTTPS/TLS 1.2+ for all API communications
5. Implement rate limiting on authentication endpoints
6. Monitor and alert on authentication failures
7. Rotate client secrets periodically (every 90 days recommended)
8. Implement IP whitelisting for production environments

---

<div style="page-break-after: always;"></div>

## 11. Response Codes & Error Handling

The response message will be different based on the submitted request. In case of a valid request, a success response will be sent back synchronously. In case of an invalid request, an error response will be returned with appropriate error codes and messages.

### Standard HTTP Response Codes

| HTTP Response Code | Description | When Used |
|-------------------|-------------|-----------|
| 200 OK | Success | Request processed successfully |
| 201 Created | Resource Created | New certificate/resource created successfully |
| 400 Bad Request | Client Error | Invalid request data, validation failures |
| 401 Unauthorized | Authentication Error | Invalid or expired token, missing credentials |
| 403 Forbidden | Authorization Error | Valid token but insufficient permissions |
| 404 Not Found | Resource Not Found | Requested resource does not exist |
| 409 Conflict | Conflict Error | Resource already exists or state conflict |
| 422 Unprocessable Entity | Business Logic Error | Valid request but business rules violated |
| 429 Too Many Requests | Rate Limit Exceeded | Client exceeded API rate limits |
| 500 Internal Server Error | Server Error | Unexpected server-side error |
| 502 Bad Gateway | Gateway Error | Upstream service unavailable |
| 503 Service Unavailable | Service Unavailable | Temporary service outage, maintenance |
| 504 Gateway Timeout | Gateway Timeout | Upstream service timeout |

### Application Error Codes

| Error Code | HTTP Status | Description | Example Message |
|-----------|------------|-------------|----------------|
| FIELD_REQUIRED | 400 | Required field is missing | "shipperName is required and cannot be empty" |
| FIELD_LENGTH_INVALID | 400 | Field length validation failed | "consigneeName must be between 1 and 200 characters" |
| INVALID_FORMAT | 400 | Field format is invalid | "shipperEmail must be a valid email address" |
| INVALID_DATE_FORMAT | 400 | Date format is invalid | "estimatedDepartureDate must be in format YYYY-MM-DD" |
| VALUE_OUT_OF_RANGE | 400 | Numeric value out of range | "invoiceAmount must be greater than 0" |
| INVALID_NIF | 400 | NIF validation failed | "NIF validation failed. Please verify the Angola Tax ID." |
| INVALID_HS_CODE | 400 | HS Code validation failed | "HS Code 8703.2319 is invalid or not found" |
| INVALID_PORT_CODE | 400 | Port code validation failed | "Port code AEXXX is invalid or not found" |
| INVALID_CARRIER | 400 | Carrier validation failed | "Carrier code XXX is invalid or not active" |
| AMOUNT_MISMATCH | 400 | Amount calculation error | "Invoice amount must equal the sum of all goods line items" |
| WEIGHT_MISMATCH | 400 | Weight calculation error | "Total gross weight must equal the sum of all goods weights" |
| INVALID_DATE_RANGE | 400 | Date range validation failed | "Estimated arrival date must be after departure date" |
| DUPLICATE_CERTIFICATE | 409 | Certificate already exists | "A certificate with BL number MAEU123456789 already exists" |
| CERTIFICATE_NOT_FOUND | 404 | Certificate not found | "Certificate number CNCA-2025-000123 not found" |
| AMENDMENT_NOT_ALLOWED | 422 | Amendment not permitted | "Certificate cannot be amended in current status" |
| CANCELLATION_NOT_ALLOWED | 422 | Cancellation not permitted | "Certificate cannot be cancelled in current status" |
| AUTH_ERROR | 401 | Authentication failed | "JWT token validation failed" |
| AUTH_EXPIRED | 401 | Token expired | "Access token has expired. Please refresh your token." |
| INSUFFICIENT_PERMISSIONS | 403 | Insufficient permissions | "User does not have permission to perform this action" |
| RATE_LIMIT_EXCEEDED | 429 | Rate limit exceeded | "Rate limit exceeded. Maximum 100 requests per minute allowed." |
| FILE_TOO_LARGE | 400 | File size exceeded | "File size exceeds maximum allowed size of 10MB" |
| INVALID_FILE_TYPE | 400 | Invalid file type | "File type .exe is not allowed. Accepted: PDF, JPG, PNG" |
| FILE_NOT_FOUND | 404 | File not found | "File with ID file_abc123 not found" |
| INTERNAL_ERROR | 500 | Server internal error | "An unexpected error occurred. Please contact support." |
| SERVICE_UNAVAILABLE | 503 | Service unavailable | "Service temporarily unavailable. Please try again later." |
| GATEWAY_TIMEOUT | 504 | Gateway timeout | "Request timeout. Please try again." |

### Error Response Format

**Standard Error Response Structure:**

```json
{
  "success": false,
  "message": "Validation failed",
  "statusCode": 400,
  "timestamp": "2025-11-14T10:30:00Z",
  "errors": [
    {
      "field": "consigneeNIF",
      "code": "INVALID_NIF",
      "message": "NIF validation failed. Please verify the Angola Tax ID.",
      "details": {
        "nif": "5000123456",
        "validationEndpoint": "/api/v1/nif/validate"
      }
    },
    {
      "field": "goods[0].hsCode",
      "code": "INVALID_HS_CODE",
      "message": "HS Code 87032319 must be 6, 8, or 10 digits",
      "details": {
        "provided": "87032319",
        "expected": "8 or 10 digits"
      }
    }
  ],
  "requestId": "req_abc123xyz",
  "documentation": "https://docs.adports.ae/jul-sintece/errors"
}
```

### Retry Logic and Error Handling Recommendations

**For Transient Errors (500, 502, 503, 504):**

1. Implement exponential backoff retry strategy
2. Maximum 3 retry attempts
3. Initial delay: 1 second
4. Backoff multiplier: 2x (1s, 2s, 4s)
5. Add jitter to prevent thundering herd

**For Client Errors (400, 401, 403, 404, 409, 422):**

1. Do NOT retry automatically
2. Log error details for debugging
3. Display user-friendly error messages
4. Provide guidance for resolution

**For Rate Limit Errors (429):**

1. Respect Retry-After header if provided
2. Implement client-side rate limiting
3. Use exponential backoff with maximum wait time

**Example Retry Implementation (Pseudocode):**

```python
max_retries = 3
retry_delay = 1  # seconds

for attempt in range(max_retries):
    try:
        response = call_api()
        if response.status_code == 200:
            return response
        elif response.status_code in [500, 502, 503, 504]:
            if attempt < max_retries - 1:
                sleep(retry_delay * (2 ** attempt))
                continue
        else:
            # Client error - do not retry
            handle_error(response)
            break
    except ConnectionError:
        if attempt < max_retries - 1:
            sleep(retry_delay * (2 ** attempt))
            continue
```

---

<div style="page-break-after: always;"></div>

## 12. Interface End Points

All API endpoints will be provided by ARCCLA upon environment setup.

### Base URLs

| Environment | Base URL | Description |
|------------|----------|-------------|
| Development | https://api-dev.sintece.ao | Development environment for initial integration testing |
| UAT (Testing) | https://api-uat.sintece.ao | User Acceptance Testing environment |
| Production | https://api.sintece.ao | Production environment |

### Authentication Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /auth/token | POST | Obtain JWT access token using client credentials |
| /auth/refresh | POST | Refresh expired access token using refresh token |
| /auth/revoke | POST | Revoke access token (logout) |

### Master Data Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/v1/master-data/cargo-types | GET | Retrieve cargo types |
| /api/v1/master-data/incoterms | GET | Retrieve Incoterms |
| /api/v1/master-data/countries | GET | Retrieve countries |
| /api/v1/master-data/carriers | GET | Retrieve carriers |
| /api/v1/master-data/currencies | GET | Retrieve currencies |
| /api/v1/master-data/banks | GET | Retrieve banks |
| /api/v1/master-data/units | GET | Retrieve units of measurement |
| /api/v1/master-data/container-types | GET | Retrieve container types |
| /api/v1/master-data/transport-types | GET | Retrieve transport types |
| /api/v1/master-data/locations | GET | Retrieve locations/ports |
| /api/v1/master-data/goods-classifications | GET | Retrieve HS codes |
| /api/v1/master-data/imo-codes | GET | Retrieve IMO dangerous goods codes |
| /api/v1/master-data/vessels | GET | Retrieve vessels |
| /api/v1/master-data/ctn-cities | GET | Retrieve CTN cities |
| /api/v1/master-data/ctn-ports | GET | Retrieve CTN ports |

### Certificate Management Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/v1/certificates/submit | POST | Submit new certificate request |
| /api/v1/certificates/amend | POST | Submit amendment request |
| /api/v1/certificates/cancel | POST | Submit cancellation request |
| /api/v1/certificates/{certificateNumber} | GET | Retrieve certificate details |
| /api/v1/certificates/{certificateNumber}/status | GET | Retrieve certificate status |
| /api/v1/certificates/track | GET | Track certificate by BL or reference number |

### Document Management Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/v1/files/upload | POST | Upload document attachments |
| /api/v1/files/{fileId} | GET | Download file by ID |
| /api/v1/attachments/types | GET | Retrieve attachment types |
| /api/v1/attachments/names | GET | Retrieve attachment naming conventions |

### Validation Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/v1/nif/validate | POST | Validate Angola Tax ID (NIF) |
| /api/v1/certificates/validate | POST | Validate certificate data (draft mode) |

### Invoice Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/v1/invoices/{invoiceNumber}/download | GET | Download invoice PDF |
| /api/v1/invoices/{invoiceNumber}/status | GET | Check invoice payment status |

### Consignee Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /api/v1/consignees | GET | Retrieve consignee list |
| /api/v1/consignees/{consigneeId} | GET | Retrieve consignee details |
| /api/v1/consignees/search | GET | Search consignees by NIF or name |

### Health & Monitoring Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /health | GET | API health check |
| /api/v1/status | GET | Service status and version |
| /api/v1/ping | GET | Connectivity test |

### Rate Limits

| Endpoint Category | Rate Limit | Time Window |
|------------------|------------|-------------|
| Authentication | 10 requests | Per minute |
| Master Data | 100 requests | Per minute |
| Certificate Submit | 50 requests | Per minute |
| Certificate Query | 200 requests | Per minute |
| File Upload | 20 requests | Per minute |
| All Other Endpoints | 100 requests | Per minute |

---

<div style="page-break-after: always;"></div>

## 13. Appendix – Enclosures

### Enclosure 1: Complete API Request/Response Samples

Detailed JSON samples for all API endpoints are provided in separate files:

1. `master_data_api_samples.json` - Complete samples for all master data APIs
2. `certificate_submission_samples.json` - Certificate submission request/response samples
3. `amendment_samples.json` - Amendment request samples
4. `cancellation_samples.json` - Cancellation request samples
5. `error_response_samples.json` - Error response examples

### Enclosure 2: JSON Schema Definitions

Complete JSON schema definitions for request and response validation:

1. `certificate_submission_schema.json` - Certificate submission schema
2. `amendment_request_schema.json` - Amendment request schema
3. `cancellation_request_schema.json` - Cancellation request schema
4. `error_response_schema.json` - Standard error response schema

### Enclosure 3: Postman Collection

A comprehensive Postman collection for testing all API endpoints:

`JUL_SINTECE_Integration_Postman_Collection.json`

This collection includes:
- Pre-configured authentication
- All API endpoints with sample requests
- Test scripts for response validation
- Environment variables for DEV, UAT, and PROD

### Enclosure 4: Integration Checklist

**Pre-Integration Requirements:**

- [ ] Keycloak client credentials obtained
- [ ] Network connectivity established between JUL and SINTECE
- [ ] IP whitelisting completed
- [ ] SSL certificates installed
- [ ] Firewall rules configured
- [ ] Test environment access granted

**Development Phase:**

- [ ] Master data APIs integrated
- [ ] Certificate submission API integrated
- [ ] File upload API integrated
- [ ] NIF validation API integrated
- [ ] Amendment workflow implemented
- [ ] Cancellation workflow implemented
- [ ] Error handling implemented
- [ ] Logging and monitoring configured

**Testing Phase:**

- [ ] Unit tests completed
- [ ] Integration tests completed
- [ ] End-to-end testing completed
- [ ] Performance testing completed
- [ ] Security testing completed
- [ ] User acceptance testing completed

**Production Readiness:**

- [ ] Production credentials configured
- [ ] Production endpoints updated
- [ ] Monitoring and alerting configured
- [ ] Runbook prepared
- [ ] Support escalation process defined
- [ ] Go-live approval obtained

### Enclosure 5: Contact Information

**Abu Dhabi Ports - JUL System**

| Role | Name | Email | Phone |
|------|------|-------|-------|
| Integration Lead | TBD | integration@adports.ae | +971-x-xxx-xxxx |
| Technical Support | Support Team | support@adports.ae | +971-x-xxx-xxxx |
| Project Manager | TBD | pm@adports.ae | +971-x-xxx-xxxx |

**ARCCLA - SINTECE System**

| Role | Name | Email | Phone |
|------|------|-------|-------|
| Integration Lead | TBD | integration@arccla.ao | +244-xxx-xxx-xxx |
| Technical Support | Support Team | support@arccla.ao | +244-xxx-xxx-xxx |
| Project Manager | TBD | pm@arccla.ao | +244-xxx-xxx-xxx |

### Enclosure 6: Change Log Template

All changes to this document must be logged using the following template:

| Version | Date | Author | Section | Change Description | Impact |
|---------|------|--------|---------|-------------------|---------|
| X.X | YYYY-MM-DD | Name | Section # | Description | High/Med/Low |

### Enclosure 7: Glossary of Terms

| Term | Definition |
|------|------------|
| API | Application Programming Interface |
| BL | Bill of Lading |
| CNCA | Certificado Nacional de Carga de Angola |
| CTN | Cargo Tracking Note |
| DUP | Declaration of Unique Property |
| HS Code | Harmonized System Code |
| IMO | International Maritime Organization |
| Incoterms | International Commercial Terms |
| JWT | JSON Web Token |
| NIF | Número de Identificação Fiscal (Angola Tax ID) |
| OAuth | Open Authorization |
| OIDC | OpenID Connect |
| REST | Representational State Transfer |
| RBAC | Role-Based Access Control |
| SOA | Service Oriented Architecture |
| SSO | Single Sign-On |
| TLS | Transport Layer Security |
| UN/LOCODE | United Nations Code for Trade and Transport Locations |

---

**End of Document**

---

**Document Control Information**

| Field | Value |
|-------|-------|
| Document Title | JUL-SINTECE Integration Control Document |
| Document ID | ICD-JUL-SINTECE-002 |
| Version | 3.0 |
| Date | November 14, 2025 |
| Status | Draft for Review |
| Classification | Internal Use |
| Owner | Abu Dhabi Ports Integration Team |
| Review Cycle | Quarterly |
| Next Review Date | February 14, 2026 |

**Abu Dhabi Ports Contact Information**

Abu Dhabi, UAE
P.O. BOX 54477
Tel: +971 2 508 5555
Email: info@adports.ae
Website: www.adports.ae

---
