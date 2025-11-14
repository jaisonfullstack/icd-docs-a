# JUL-SINTECE Integration Control Document

<style>
@media print {
  .page-break { page-break-before: always; }
  .no-print { display: none; }
}

.highlight-box {
  background-color: #f8f9fa;
  border-left: 4px solid #007bff;
  padding: 15px;
  margin: 15px 0;
  border-radius: 5px;
}

.success-box {
  background-color: #d4edda;
  border-left: 4px solid #28a745;
  padding: 15px;
  margin: 15px 0;
  border-radius: 5px;
}

.warning-box {
  background-color: #fff3cd;
  border-left: 4px solid #ffc107;
  padding: 15px;
  margin: 15px 0;
  border-radius: 5px;
}

.info-box {
  background-color: #d1ecf1;
  border-left: 4px solid #17a2b8;
  padding: 15px;
  margin: 15px 0;
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
</style>

<div style="text-align: center; padding: 20px 0;">
<img src="./images/JUL-logo.png" alt="JUL Logo" style="height: 60px; margin: 0 15px;" />
<img src="./images/Maqta-logo.png" alt="Abu Dhabi Ports Logo" style="height: 60px; margin: 0 15px;" />
</div>

<div style="text-align: center; border: 2px solid #2E5BBA; padding: 20px; margin: 20px 0; background-color: #f8f9fa;">

## CNCA Certificate Integration
### Streamlined API Specification

**Version 3.0**  
**Abu Dhabi Ports**  
**November 14, 2025**

</div>

---

<div style="page-break-before: always;"></div>

## 📋 Document Control

| **Field** | **Value** |
|-----------|-----------|
| **Document Title** | JUL-SINTECE Integration Control Document |
| **Author** | Linoy Pappachan Malakkaran |
| **Project Name** | JUL System Integration with SINTECE - CNCA Certificate Process |
| **Document ID** | ICD-JUL-SINTECE-003 |
| **Version** | 3.0 |
| **Organization** | Abu Dhabi Ports |
| **Date** | November 14, 2025 |
| **Status** | Draft for Review |
| **Classification** | Internal Use |
| **Prepared By** | Abu Dhabi Ports Integration Team |
| **Scope** | Streamlined CNCA Certificate Integration with Consolidated APIs |

---

## 📝 Version History

| **Version** | **Date** | **Author** | **Description of Changes** |
|-------------|----------|------------|----------------------------|
| 1.0 | 2025-11-12 | Linoy Pappachan Malakkaran | Initial ICD creation with technical specifications for JUL-SINTECE integration. |
| 2.0 | 2025-11-13 | Linoy Pappachan Malakkaran | Added amendment and cancellation APIs, approval workflows, status management. |
| 3.0 | 2025-11-14 | Linoy Pappachan Malakkaran | Streamlined document: Removed OData references, consolidated APIs, added Keycloak SSO, removed flow diagrams, added NIF validation and invoice download APIs. Focused on essential integration specifications only. |

---

<div style="page-break-before: always;"></div>

## 📑 Table of Contents

<div class="toc-container">

<table>
<tbody>
<tr class="toc-section"><td>1</td><td><a href="#1-introduction">Introduction</a> 📖</td><td>5</td></tr>
<tr class="toc-subsection"><td>1.1</td><td><a href="#11-purpose">Purpose</a></td><td>5</td></tr>
<tr class="toc-subsection"><td>1.2</td><td><a href="#12-scope">Scope</a></td><td>5</td></tr>
<tr class="toc-subsection"><td>1.3</td><td><a href="#13-key-terms">Key Terms</a></td><td>5</td></tr>

<tr class="toc-section"><td>2</td><td><a href="#2-system-overview-">System Overview</a> 🏗️</td><td>6</td></tr>
<tr class="toc-subsection"><td>2.1</td><td><a href="#21-system-architecture">System Architecture</a></td><td>6</td></tr>
<tr class="toc-subsection"><td>2.2</td><td><a href="#22-integration-pattern">Integration Pattern</a></td><td>7</td></tr>
<tr class="toc-subsection"><td>2.3</td><td><a href="#23-authentication-sso">Authentication & SSO</a></td><td>7</td></tr>

<tr class="toc-section"><td>3</td><td><a href="#3-system-integration-diagram-">System Integration Diagram</a> 🔗</td><td>8</td></tr>

<tr class="toc-section"><td>4</td><td><a href="#4-api-specifications-">API Specifications</a> 📊</td><td>9</td></tr>
<tr class="toc-subsection"><td>4.1</td><td><a href="#41-master-data-apis">Master Data APIs</a></td><td>9</td></tr>
<tr class="toc-subsection"><td>4.2</td><td><a href="#42-cnca-certificate-submission-api">CNCA Certificate Submission API</a></td><td>15</td></tr>
<tr class="toc-subsection"><td>4.3</td><td><a href="#43-certificate-management-apis">Certificate Management APIs</a></td><td>18</td></tr>
<tr class="toc-subsection"><td>4.4</td><td><a href="#44-amendment-cancellation-apis">Amendment & Cancellation APIs</a></td><td>22</td></tr>
<tr class="toc-subsection"><td>4.5</td><td><a href="#45-validation-apis">Validation APIs</a></td><td>25</td></tr>
<tr class="toc-subsection"><td>4.6</td><td><a href="#46-invoice-download-api">Invoice Download API</a></td><td>27</td></tr>

<tr class="toc-section"><td>5</td><td><a href="#5-data-models-">Data Models</a> 📋</td><td>28</td></tr>
<tr class="toc-subsection"><td>5.1</td><td><a href="#51-certificate-data-structure">Certificate Data Structure</a></td><td>28</td></tr>
<tr class="toc-subsection"><td>5.2</td><td><a href="#52-status-management">Status Management</a></td><td>30</td></tr>

<tr class="toc-section"><td>6</td><td><a href="#6-validation-framework-">Validation Framework</a> ✅</td><td>31</td></tr>
<tr class="toc-subsection"><td>6.1</td><td><a href="#61-business-validation-rules">Business Validation Rules</a></td><td>31</td></tr>
<tr class="toc-subsection"><td>6.2</td><td><a href="#62-error-handling">Error Handling</a></td><td>32</td></tr>
</tbody>
</table>

</div>

---

<div style="page-break-before: always;"></div>

## 1. Introduction

### 1.1 Purpose

This Integration Control Document (ICD) defines the API specifications for integrating the JUL system (Abu Dhabi Ports) with the SINTECE system (ARCCLA) for CNCA certificate processing.

**Key Features:**
- Consolidated CNCA certificate submission API
- Keycloak SSO authentication integration
- Amendment and cancellation capabilities
- NIF validation and invoice download APIs

### 1.2 Scope

**In Scope:**
- Complete CNCA certificate submission workflow
- Master data synchronization APIs
- Amendment and cancellation APIs
- Authentication via Keycloak SSO
- Business validation including NIF validation
- Invoice download for import profiles

**Out of Scope:**
- Internal SINTECE business logic
- Keycloak configuration details
- Mobile application development

### 1.3 Key Terms

| **Term** | **Definition** |
|----------|----------------|
| **ARCCLA** | Angolan regulatory agency responsible for cargo certification |
| **CNCA** | Certificado Nacional de Carga de Angola - required certificate for Angola cargo |
| **CTN** | Certificate/Cargo Tracking Note - internal certificate reference |
| **JUL** | Abu Dhabi Ports system for CNCA certificate management |
| **SINTECE** | ARCCLA system for certificate processing and approval |
| **NIF** | Angola Tax Registration Number requiring business validation |
| **Keycloak** | Identity and access management solution providing SSO capabilities |

---

<div style="page-break-before: always;"></div>

## 2. System Overview 🏗️

### 2.1 System Architecture

**JUL System (Abu Dhabi Ports)**
- Web portal for CNCA certificate management
- Document upload and submission capabilities
- Amendment and cancellation request management
- Certificate download and status tracking

**SINTECE System (ARCCLA)**
- Backend certificate processing system
- ARCCLA broker review and approval workflow
- Invoice generation for import profiles
- Certificate issuance and status management

### 2.2 Integration Pattern

**Communication:**
- RESTful APIs with standard HTTP methods (GET, POST, PUT, DELETE)
- JSON data format with schema validation
- HTTPS/TLS encryption and Keycloak SSO authentication
- Query parameters for filtering and pagination

**Data Flow:**
1. **Complete CTN Submission**: JUL submits complete CNCA certificate data via POST /api/cncaCertificate
2. **Certificate Validation**: SINTECE validates complete certificate data with business rules
3. **ARCCLA Review**: ARCCLA broker reviews and approves/rejects certificate
4. **Invoice Generation**: SINTECE generates invoice for import profiles only
5. **Certificate Issuance**: Certificate issued with amendment/cancellation capabilities
6. **Status Updates**: Status communicated via API polling

### 2.3 Authentication & SSO

**Keycloak Integration:**
- Keycloak serves as the centralized SSO solution
- Client systems can integrate using supported protocols:
  - OpenID Connect (OIDC)
  - OAuth2
  - SAML (if required)
- JWT token-based authentication for API calls
- Role-based access control for different user types

**Authentication Flow:**
1. Client authenticates with Keycloak using preferred protocol
2. Keycloak issues JWT token upon successful authentication
3. JWT token included in API request headers (Authorization: Bearer {token})
4. SINTECE validates JWT token for each API call
5. Token refresh handled according to Keycloak token lifecycle policies

---

<div style="page-break-before: always;"></div>

## 3. System Integration Diagram 🔗

The following diagram illustrates the system component ownership and integration points:

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           CNCA CERTIFICATE INTEGRATION ARCHITECTURE                 │
└─────────────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────┐              ┌──────────────────────┐              ┌──────────────────────┐
    │                      │              │                      │              │                      │
    │    JUL SYSTEM        │              │     KEYCLOAK SSO     │              │   SINTECE SYSTEM     │
    │   (Abu Dhabi Ports)  │              │   (Abu Dhabi Ports)  │              │      (ARCCLA)        │
    │                      │              │                      │              │                      │
    ├──────────────────────┤              ├──────────────────────┤              ├──────────────────────┤
    │                      │              │                      │              │                      │
    │ • Web Portal         │◄─────────────┤ • User Authentication│──────────────┤ • Certificate        │
    │ • Document Upload    │              │ • JWT Token          │              │   Processing         │
    │ • Certificate Mgmt   │              │   Generation         │              │ • ARCCLA Broker      │
    │ • Status Tracking    │              │ • Role Management    │              │   Review             │
    │ • Amendment Requests │              │ • Protocol Support:  │              │ • Invoice Generation │
    │ • Cancellation Mgmt  │              │   - OpenID Connect   │              │   (Import Only)      │
    │                      │              │   - OAuth2           │              │ • Certificate        │
    │                      │              │   - SAML             │              │   Issuance           │
    │                      │              │                      │              │ • Status Management  │
    └──────────────────────┘              └──────────────────────┘              └──────────────────────┘
              │                                       │                                       │
              │                                       │                                       │
              │ HTTPS/TLS + JWT Token                 │ SSO Integration                      │
              │ RESTful API Calls                     │ (OpenID/OAuth2)                     │
              │                                       │                                       │
              └───────────────────────────────────────┼───────────────────────────────────────┘
                                                      │
                          ┌───────────────────────────┴───────────────────────────┐
                          │                                                       │
                          ▼                                                       ▼
              ┌──────────────────────┐                               ┌──────────────────────┐
              │                      │                               │                      │
              │   API INTEGRATION    │                               │   BUSINESS FLOWS     │
              │                      │                               │                      │
              ├──────────────────────┤                               ├──────────────────────┤
              │                      │                               │                      │
              │ • Master Data Sync   │                               │ 1. Certificate       │
              │ • Certificate        │                               │    Submission        │
              │   Submission         │                               │ 2. ARCCLA Review     │
              │ • Status Polling     │                               │ 3. Invoice Generation│
              │ • Amendment APIs     │                               │    (Import Only)     │
              │ • Cancellation APIs  │                               │ 4. Certificate       │
              │ • Invoice Download   │                               │    Issuance          │
              │ • NIF Validation     │                               │ 5. Amendment Process │
              │                      │                               │ 6. Cancellation     │
              │                      │                               │    Process           │
              └──────────────────────┘                               └──────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│ COMPONENT OWNERSHIP:                                                                 │
│ • JUL System: Abu Dhabi Ports                                                       │
│ • Keycloak SSO: Abu Dhabi Ports                                                     │  
│ • SINTECE System: ARCCLA                                                            │
│ • Integration APIs: Defined jointly, implemented by respective owners               │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

**Key Integration Points:**

1. **Authentication**: Keycloak SSO manages user authentication for both systems
2. **Certificate Submission**: Complete CNCA certificate data submitted via single API
3. **Status Synchronization**: JUL polls SINTECE for status updates
4. **Invoice Management**: Invoice download for import profiles only
5. **Amendment/Cancellation**: Bilateral API communication for request processing

---

<div style="page-break-before: always;"></div>

## 4. API Specifications 📊

### 4.1 Master Data APIs

Essential master data synchronization APIs for CNCA certificate processing.

#### 4.1.1 Countries API

**Endpoint:** `GET /api/countries`

**Purpose:** Retrieve list of countries for address and cargo origin/destination.

**Request:**
| **Method** | **Endpoint** | **Headers** |
|------------|--------------|-------------|
| GET | `/api/countries` | `Authorization: Bearer {jwt_token}`<br>`Content-Type: application/json` |

**Request Parameters:**
| **Parameter** | **Type** | **Required** | **Description** |
|---------------|----------|--------------|------------------|
| None | - | - | No parameters required |

**Response:**
| **Field** | **Type** | **Description** |
|-----------|----------|------------------|
| success | boolean | Operation success status |
| data | array | List of country objects |
| data[].id | integer | Country unique identifier |
| data[].name | string | Country full name |
| data[].code | string | ISO 2-letter country code |
| data[].iso3 | string | ISO 3-letter country code |

**Response Sample:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Angola",
      "code": "AO",
      "iso3": "AGO"
    },
    {
      "id": 2,
      "name": "United Arab Emirates",
      "code": "AE", 
      "iso3": "ARE"
    }
  ]
}
```

#### 4.1.2 Ports API

**Endpoint:** `GET /api/ports`

**Purpose:** Retrieve list of ports for loading/discharge locations.

**Request:**
| **Method** | **Endpoint** | **Headers** |
|------------|--------------|-------------|
| GET | `/api/ports` | `Authorization: Bearer {jwt_token}`<br>`Content-Type: application/json` |

**Request Parameters:**
| **Parameter** | **Type** | **Required** | **Description** |
|---------------|----------|--------------|------------------|
| countryCode | string | No | Filter ports by ISO country code |

**Response:**
| **Field** | **Type** | **Description** |
|-----------|----------|------------------|
| success | boolean | Operation success status |
| data | array | List of port objects |
| data[].id | integer | Port unique identifier |
| data[].name | string | Port full name |
| data[].code | string | UN/LOCODE port code |
| data[].country | string | Country full name |
| data[].countryCode | string | ISO country code |

**Response Sample:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Khalifa Port",
      "code": "AEKIP",
      "country": "United Arab Emirates",
      "countryCode": "AE"
    }
  ]
}
```

#### 4.1.3 Cargo Types API

**Endpoint:** `GET /api/cargoTypes`

**Purpose:** Retrieve list of cargo types for certificate classification.

**Request:**
| **Method** | **Endpoint** | **Headers** |
|------------|--------------|-------------|
| GET | `/api/cargoTypes` | `Authorization: Bearer {jwt_token}`<br>`Content-Type: application/json` |

**Request Parameters:**
| **Parameter** | **Type** | **Required** | **Description** |
|---------------|----------|--------------|------------------|
| None | - | - | No parameters required |

**Response:**
| **Field** | **Type** | **Description** |
|-----------|----------|------------------|
| success | boolean | Operation success status |
| data | array | List of cargo type objects |
| data[].id | integer | Cargo type unique identifier |
| data[].name | string | Cargo type description |
| data[].code | string | Cargo type code |

**Response Sample:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Dry Cargo",
      "code": "DRY"
    },
    {
      "id": 2,
      "name": "Liquid Bulk",
      "code": "LIQ"
    }
  ]
}
```

#### 4.1.4 Currencies API

**Endpoint:** `GET /api/currencies`

**Purpose:** Retrieve list of currencies for cargo value declaration.

**Request Sample:**
```http
GET /api/currencies
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

**Response Sample:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "US Dollar",
      "code": "USD",
      "symbol": "$"
    },
    {
      "id": 2,
      "name": "Euro",
      "code": "EUR",
      "symbol": "€"
    }
  ]
}
```

#### 4.1.5 Container Types API

**Endpoint:** `GET /api/containerTypes`

**Purpose:** Retrieve list of container types for containerized cargo.

**Request Sample:**
```http
GET /api/containerTypes
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

**Response Sample:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "20' Dry Van",
      "code": "20DV",
      "size": "20",
      "type": "Dry Van"
    },
    {
      "id": 2,
      "name": "40' High Cube",
      "code": "40HC",
      "size": "40",
      "type": "High Cube"
    }
  ]
}
```

### 4.2 CNCA Certificate Submission API

**Consolidated API for complete CNCA certificate submission.**

#### 4.2.1 Submit Complete CNCA Certificate

**Endpoint:** `POST /api/cncaCertificate`

**Purpose:** Submit complete CNCA certificate data in a single API call, replacing the previous multi-step approach.

**Request:**
| **Method** | **Endpoint** | **Headers** |
|------------|--------------|-------------|
| POST | `/api/cncaCertificate` | `Authorization: Bearer {jwt_token}`<br>`Content-Type: application/json` |

**Request Body Schema:**
| **Field** | **Type** | **Required** | **Description** |
|-----------|----------|--------------|------------------|
| certificateType | string | Yes | "Import" or "Export" |
| shipper | object | Yes | Shipper company details |
| shipper.name | string | Yes | Company name |
| shipper.nif | string | Yes | Angola Tax Registration Number |
| consignee | object | Yes | Consignee company details |
| goods | array | Yes | List of cargo items |
| containers | array | No | Container details (if containerized) |
| transport | object | Yes | Vessel and port information |
| billOfLading | object | Yes | Bill of lading details |
| attachments | array | Yes | Required documents |

**Request Sample:**
```http
POST /api/cncaCertificate
Authorization: Bearer {jwt_token}
Content-Type: application/json

{
  "certificateType": "Import",
  "shipper": {
    "name": "Global Trading Co",
    "address": "123 Business Street",
    "city": "Dubai",
    "country": "AE",
    "nif": "123456789",
    "contact": {
      "phone": "+971-4-1234567",
      "email": "contact@globaltrading.com"
    }
  },
  "consignee": {
    "name": "Angola Importers Ltd",
    "address": "456 Commercial Ave",
    "city": "Luanda",
    "country": "AO",
    "nif": "987654321",
    "contact": {
      "phone": "+244-222-123456",
      "email": "orders@angolaimporters.ao"
    }
  },
  "notifyParty": {
    "name": "Freight Solutions",
    "address": "789 Logistics Blvd",
    "city": "Abu Dhabi",
    "country": "AE",
    "contact": {
      "phone": "+971-2-7654321",
      "email": "notify@freightsolutions.ae"
    }
  },
  "goods": [
    {
      "description": "Steel Pipes",
      "hsCode": "730431",
      "quantity": 1000,
      "unit": "PCS",
      "weight": 25000.50,
      "weightUnit": "KG",
      "value": 50000.00,
      "currency": "USD",
      "packageType": "Bundles",
      "packageCount": 100
    }
  ],
  "containers": [
    {
      "number": "TCLU1234567",
      "type": "40HC",
      "sealNumber": "SEAL123456",
      "weight": 25000.50,
      "weightUnit": "KG"
    }
  ],
  "transport": {
    "vessel": {
      "name": "MV Global Trader",
      "imoNumber": "9876543",
      "flag": "UAE",
      "callSign": "A6ABC"
    },
    "voyage": "GT2024-001",
    "portOfLoading": {
      "name": "Khalifa Port",
      "code": "AEKIP",
      "country": "AE"
    },
    "portOfDischarge": {
      "name": "Port of Luanda",
      "code": "AOLAD",
      "country": "AO"
    },
    "etd": "2025-01-15T10:00:00Z",
    "eta": "2025-01-25T14:30:00Z"
  },
  "billOfLading": {
    "number": "MSKU7749670",
    "date": "2025-01-14T08:00:00Z",
    "type": "Master"
  },
  "attachments": [
    {
      "name": "Bill of Lading",
      "type": "PDF",
      "base64Data": "JVBERi0xLjQK....",
      "required": true
    },
    {
      "name": "Commercial Invoice",
      "type": "PDF",
      "base64Data": "JVBERi0xLjQK....",
      "required": true
    }
  ]
}
```

**Response:**
| **Field** | **Type** | **Description** |
|-----------|----------|------------------|
| success | boolean | Operation success status |
| data | object | Certificate submission details |
| data.certificateId | string | Unique certificate identifier |
| data.status | string | Current certificate status |
| data.submissionDate | datetime | Submission timestamp |
| data.referenceNumber | string | JUL system reference |
| data.canAmend | boolean | Amendment eligibility flag |
| data.canCancel | boolean | Cancellation eligibility flag |
| message | string | Success confirmation message |

**Response Sample:**
```json
{
  "success": true,
  "data": {
    "certificateId": "CTN-2025-001234",
    "status": "Submitted",
    "submissionDate": "2025-01-14T09:15:30Z",
    "referenceNumber": "JUL-CTN-20250114-001234",
    "canAmend": true,
    "canCancel": true,
    "estimatedProcessingTime": "3-5 business days"
  },
  "message": "CNCA certificate submitted successfully for ARCCLA review"
}
```

### 4.3 Certificate Management APIs

#### 4.3.1 Get Certificate List

**Endpoint:** `GET /api/certificates`

**Purpose:** Retrieve list of certificates with filtering and pagination.

**Request:**
| **Method** | **Endpoint** | **Headers** |
|------------|--------------|-------------|
| GET | `/api/certificates` | `Authorization: Bearer {jwt_token}`<br>`Content-Type: application/json` |

**Query Parameters:**
| **Parameter** | **Type** | **Required** | **Description** |
|---------------|----------|--------------|------------------|
| status | string | No | Filter by certificate status |
| limit | integer | No | Number of records to return (default: 20) |
| offset | integer | No | Number of records to skip (default: 0) |

**Response:**
| **Field** | **Type** | **Description** |
|-----------|----------|------------------|
| success | boolean | Operation success status |
| data.certificates | array | List of certificate objects |
| data.pagination | object | Pagination information |
| data.pagination.total | integer | Total number of certificates |
| data.pagination.hasMore | boolean | More records available flag |

**Response Sample:**
```json
{
  "success": true,
  "data": {
    "certificates": [
      {
        "id": "CTN-2025-001234",
        "status": "Submitted",
        "submissionDate": "2025-01-14T09:15:30Z",
        "shipper": "Global Trading Co",
        "consignee": "Angola Importers Ltd",
        "canAmend": true,
        "canCancel": true
      }
    ],
    "pagination": {
      "total": 25,
      "limit": 10,
      "offset": 0,
      "hasMore": true
    }
  }
}
```

#### 4.3.2 Get Certificate Details

**Endpoint:** `GET /api/certificates/{id}`

**Purpose:** Retrieve detailed information for a specific certificate.

**Request Sample:**
```http
GET /api/certificates/CTN-2025-001234
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

**Response Sample:**
```json
{
  "success": true,
  "data": {
    "id": "CTN-2025-001234",
    "status": "Approved",
    "certificateType": "Import",
    "submissionDate": "2025-01-14T09:15:30Z",
    "approvalDate": "2025-01-16T14:20:15Z",
    "shipper": {
      "name": "Global Trading Co",
      "nif": "123456789"
    },
    "consignee": {
      "name": "Angola Importers Ltd",
      "nif": "987654321"
    },
    "goods": [
      {
        "description": "Steel Pipes",
        "value": 50000.00,
        "currency": "USD"
      }
    ],
    "canAmend": false,
    "canCancel": true,
    "invoiceGenerated": true
  }
}
```

#### 4.3.3 Get Certificate Status

**Endpoint:** `GET /api/certificates/{id}/status`

**Purpose:** Get current status and available actions for a certificate.

**Request Sample:**
```http
GET /api/certificates/CTN-2025-001234/status
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

**Response Sample:**
```json
{
  "success": true,
  "data": {
    "id": "CTN-2025-001234",
    "status": "Approved",
    "statusDate": "2025-01-16T14:20:15Z",
    "canAmend": false,
    "canCancel": true,
    "availableActions": ["Cancel"],
    "statusHistory": [
      {
        "status": "Submitted",
        "date": "2025-01-14T09:15:30Z",
        "user": "user@globaltrading.com"
      },
      {
        "status": "Under Review",
        "date": "2025-01-15T10:00:00Z",
        "user": "broker@arccla.ao"
      },
      {
        "status": "Approved",
        "date": "2025-01-16T14:20:15Z",
        "user": "broker@arccla.ao"
      }
    ]
  }
}
```

### 4.4 Amendment & Cancellation APIs

#### 4.4.1 Submit Amendment Request

**Endpoint:** `POST /api/certificates/{id}/amendments`

**Purpose:** Submit amendment request for approved certificate.

**Request:**
| **Method** | **Endpoint** | **Headers** |
|------------|--------------|-------------|
| POST | `/api/certificates/{id}/amendments` | `Authorization: Bearer {jwt_token}`<br>`Content-Type: application/json` |

**Path Parameters:**
| **Parameter** | **Type** | **Required** | **Description** |
|---------------|----------|--------------|------------------|
| id | string | Yes | Certificate ID to amend |

**Request Body:**
| **Field** | **Type** | **Required** | **Description** |
|-----------|----------|--------------|------------------|
| reason | string | Yes | Amendment reason |
| changes | array | Yes | List of field changes |
| changes[].field | string | Yes | Field path to change |
| changes[].oldValue | string | Yes | Current field value |
| changes[].newValue | string | Yes | New field value |
| attachments | array | No | Supporting documents |

**Request Sample:**
```http
POST /api/certificates/CTN-2025-001234/amendments
Authorization: Bearer {jwt_token}
Content-Type: application/json

{
  "reason": "Correct shipper address",
  "changes": [
    {
      "field": "shipper.address",
      "oldValue": "123 Business Street",
      "newValue": "123 Commerce Street",
      "justification": "Address correction as per updated company records"
    }
  ],
  "attachments": [
    {
      "name": "Updated Company Registration",
      "type": "PDF",
      "base64Data": "JVBERi0xLjQK...."
    }
  ]
}
```

**Response Sample:**
```json
{
  "success": true,
  "data": {
    "amendmentId": "AMD-2025-000123",
    "certificateId": "CTN-2025-001234",
    "status": "Pending Review",
    "submissionDate": "2025-01-17T11:30:00Z",
    "estimatedProcessingTime": "2-3 business days"
  },
  "message": "Amendment request submitted for ARCCLA review"
}
```

#### 4.4.2 Submit Cancellation Request

**Endpoint:** `POST /api/certificates/{id}/cancellations`

**Purpose:** Submit cancellation request for certificate.

**Request:**
| **Method** | **Endpoint** | **Headers** |
|------------|--------------|-------------|
| POST | `/api/certificates/{id}/cancellations` | `Authorization: Bearer {jwt_token}`<br>`Content-Type: application/json` |

**Path Parameters:**
| **Parameter** | **Type** | **Required** | **Description** |
|---------------|----------|--------------|------------------|
| id | string | Yes | Certificate ID to cancel |

**Request Body:**
| **Field** | **Type** | **Required** | **Description** |
|-----------|----------|--------------|------------------|
| reason | string | Yes | Cancellation reason |
| reasonCode | string | Yes | Standardized reason code |
| justification | string | Yes | Detailed explanation |
| refundRequested | boolean | No | Request refund flag |

**Request Sample:**
```http
POST /api/certificates/CTN-2025-001234/cancellations
Authorization: Bearer {jwt_token}
Content-Type: application/json

{
  "reason": "Shipment cancelled by customer",
  "reasonCode": "SHIPMENT_CANCELLED",
  "justification": "Customer decided not to proceed with the shipment due to market conditions",
  "refundRequested": true
}
```

**Response Sample:**
```json
{
  "success": true,
  "data": {
    "cancellationId": "CAN-2025-000456",
    "certificateId": "CTN-2025-001234",
    "status": "Pending Review",
    "submissionDate": "2025-01-17T15:45:00Z",
    "refundEligible": true,
    "estimatedRefundAmount": 250.00,
    "estimatedProcessingTime": "3-5 business days"
  },
  "message": "Cancellation request submitted for ARCCLA review"
}
```

### 4.5 Validation APIs

#### 4.5.1 NIF Validation API

**Endpoint:** `POST /api/validate/nif`

**Purpose:** Validate Angola Tax Registration Number (NIF) for business entities.

**Request:**
| **Method** | **Endpoint** | **Headers** |
|------------|--------------|-------------|
| POST | `/api/validate/nif` | `Authorization: Bearer {jwt_token}`<br>`Content-Type: application/json` |

**Request Body:**
| **Field** | **Type** | **Required** | **Description** |
|-----------|----------|--------------|------------------|
| nif | string | Yes | Angola Tax Registration Number |
| entityName | string | Yes | Company/entity name |
| entityType | string | Yes | "Company", "Individual", etc. |

**Request Sample:**
```json
{
  "nif": "123456789",
  "entityName": "Angola Importers Ltd",
  "entityType": "Company"
}
```

**Response:**
| **Field** | **Type** | **Description** |
|-----------|----------|------------------|
| success | boolean | Validation success status |
| data.nif | string | Validated NIF number |
| data.isValid | boolean | NIF validity status |
| data.entityName | string | Registered entity name |
| data.registrationStatus | string | Current registration status |
| data.validatedAt | datetime | Validation timestamp |

**Response Sample:**
```json
{
  "success": true,
  "data": {
    "nif": "123456789",
    "isValid": true,
    "entityName": "Angola Importers Ltd",
    "entityType": "Company",
    "registrationStatus": "Active",
    "registrationDate": "2020-03-15",
    "validatedAt": "2025-01-14T09:15:30Z"
  }
}
```

**Error Response Sample:**
```json
{
  "success": false,
  "error": {
    "code": "INVALID_NIF",
    "message": "NIF number is not valid or not found in Angola tax registry",
    "details": {
      "nif": "123456789",
      "reason": "Entity not found in registry"
    }
  }
}
```

### 4.6 Invoice Download API

**Endpoint:** `GET /api/certificates/{id}/invoice/download`

**Purpose:** Download invoice for approved import certificates. **Note: Invoices are only applicable for import profiles, not export profiles.**

**Request:**
| **Method** | **Endpoint** | **Headers** |
|------------|--------------|-------------|
| GET | `/api/certificates/{id}/invoice/download` | `Authorization: Bearer {jwt_token}`<br>`Accept: application/pdf` |

**Path Parameters:**
| **Parameter** | **Type** | **Required** | **Description** |
|---------------|----------|--------------|------------------|
| id | string | Yes | Certificate ID (CTN number) |

**Response (Success):**
| **Header** | **Value** | **Description** |
|------------|-----------|------------------|
| Content-Type | application/pdf | PDF file format |
| Content-Disposition | attachment; filename="Invoice-{CTN}.pdf" | Download filename |
| Content-Length | {file_size} | File size in bytes |

**Request Sample:**
```http
GET /api/certificates/CTN-2025-001234/invoice/download
Authorization: Bearer {jwt_token}
Accept: application/pdf
```

**Response Sample:**
```
HTTP/1.1 200 OK
Content-Type: application/pdf
Content-Disposition: attachment; filename="Invoice-CTN-2025-001234.pdf"
Content-Length: 145678

%PDF-1.4
1 0 obj
...
```

**Error Response (Export Profile):**
```json
{
  "success": false,
  "error": {
    "code": "INVOICE_NOT_APPLICABLE",
    "message": "Invoices are not applicable for export profile certificates",
    "details": {
      "certificateId": "CTN-2025-001234",
      "certificateType": "Export"
    }
  }
}
```

---

<div style="page-break-before: always;"></div>

## 5. Data Models 📋

### 5.1 Certificate Data Structure

**Complete certificate data model for the consolidated submission API.**

```json
{
  "CNCACertificate": {
    "certificateId": "string",
    "certificateType": "Import|Export",
    "status": "string",
    "shipper": {
      "name": "string",
      "address": "string",
      "city": "string", 
      "country": "string",
      "nif": "string",
      "contact": {
        "phone": "string",
        "email": "string"
      }
    },
    "consignee": {
      "name": "string",
      "address": "string",
      "city": "string",
      "country": "string", 
      "nif": "string",
      "contact": {
        "phone": "string",
        "email": "string"
      }
    },
    "notifyParty": {
      "name": "string",
      "address": "string",
      "city": "string",
      "country": "string",
      "contact": {
        "phone": "string",
        "email": "string"
      }
    },
    "goods": [
      {
        "description": "string",
        "hsCode": "string",
        "quantity": "number",
        "unit": "string",
        "weight": "number",
        "weightUnit": "string",
        "value": "number",
        "currency": "string",
        "packageType": "string",
        "packageCount": "number"
      }
    ],
    "containers": [
      {
        "number": "string",
        "type": "string",
        "sealNumber": "string",
        "weight": "number",
        "weightUnit": "string"
      }
    ],
    "transport": {
      "vessel": {
        "name": "string",
        "imoNumber": "string",
        "flag": "string",
        "callSign": "string"
      },
      "voyage": "string",
      "portOfLoading": {
        "name": "string",
        "code": "string",
        "country": "string"
      },
      "portOfDischarge": {
        "name": "string",
        "code": "string", 
        "country": "string"
      },
      "etd": "datetime",
      "eta": "datetime"
    },
    "billOfLading": {
      "number": "string",
      "date": "datetime",
      "type": "string"
    },
    "attachments": [
      {
        "name": "string",
        "type": "string",
        "base64Data": "string",
        "required": "boolean"
      }
    ]
  }
}
```

### 5.2 Status Management

**Certificate status workflow and eligibility flags.**

| **Status** | **Description** | **canAmend** | **canCancel** | **invoiceApplicable** |
|------------|-----------------|--------------|---------------|-----------------------|
| Submitted | Initial submission | true | true | false |
| Under Review | ARCCLA broker reviewing | false | true | false |
| Approved | Approved by ARCCLA | false | true | true (Import only) |
| Issued | Certificate issued | false | true | true (Import only) |
| Amended | Successfully amended | false | true | true (Import only) |
| Cancelled | Successfully cancelled | false | false | false |
| Rejected | Rejected by ARCCLA | false | false | false |

**Status Transition Rules:**
- Submitted → Under Review → Approved → Issued
- Any status (except Cancelled/Rejected) → Cancelled (with approval)
- Issued → Amended (with approval)

---

<div style="page-break-before: always;"></div>

## 6. Validation Framework ✅

### 6.1 Business Validation Rules

**Core validation rules applied during certificate submission:**

1. **NIF Validation**: All Angola entities must have valid NIF numbers
2. **Required Fields**: All mandatory fields must be provided
3. **Data Format**: Proper data types and formats required
4. **Business Logic**: Cargo value, weight, and quantity must be consistent
5. **Document Requirements**: Required attachments must be provided

**Field-Level Validations:**

| **Field** | **Validation Rule** | **Error Code** |
|-----------|---------------------|----------------|
| shipper.nif | Must be valid Angola NIF if country = AO | INVALID_SHIPPER_NIF |
| consignee.nif | Must be valid Angola NIF if country = AO | INVALID_CONSIGNEE_NIF |
| goods.hsCode | Must be valid 6-digit HS code | INVALID_HS_CODE |
| goods.value | Must be positive number > 0 | INVALID_CARGO_VALUE |
| billOfLading.number | Must be unique and valid format | DUPLICATE_BL_NUMBER |

### 6.2 Error Handling

**Standard error response format:**

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "details": {
      "field": "specific_field_name",
      "value": "invalid_value",
      "reason": "detailed_reason"
    }
  },
  "validationErrors": [
    {
      "field": "shipper.nif",
      "code": "INVALID_NIF",
      "message": "NIF number is not valid"
    }
  ]
}
```

**Common Error Codes:**

| **Error Code** | **Description** | **HTTP Status** |
|----------------|-----------------|-----------------|
| INVALID_NIF | NIF validation failed | 400 |
| MISSING_REQUIRED_FIELD | Required field not provided | 400 |
| INVALID_DATA_FORMAT | Data format incorrect | 400 |
| DUPLICATE_BL_NUMBER | Bill of Lading number already exists | 409 |
| UNAUTHORIZED | Invalid or expired token | 401 |
| CERTIFICATE_NOT_FOUND | Certificate ID not found | 404 |

---

**Author:** Linoy Pappachan Malakkaran  
**Organization:** Abu Dhabi Ports  
**Version:** 3.0  
**Date:** November 14, 2025