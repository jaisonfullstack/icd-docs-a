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
| **Document ID** | ICD-JUL-SINTECE-002 |
| **Version** | 3.0 |
| **Organization** | Abu Dhabi Ports |
| **Date** | November 14, 2025 |
| **Status** | Draft for Review |
| **Classification** | Internal Use |
| **Prepared By** | Abu Dhabi Ports Integration Team |
| **Scope** | CNCA Certificate Issuance Process Integration with Amendment and Cancellation Workflows |

---

## 📝 Version History

| **Version** | **Date** | **Author** | **Description of Changes** |
|-------------|----------|------------|----------------------------|
| 1.0 | 2025-11-12 | Linoy Pappachan Malakkaran | Initial ICD creation with technical specifications for JUL-SINTECE integration. Defined API specifications, data models, integration workflows, security requirements, and testing procedures. |
| 2.0 | 2025-11-13 | Linoy Pappachan Malakkaran | Added amendment and cancellation APIs, approval workflows, status management with canAmend/canCancel flags, validation framework, and error handling. Added process flow improvements and implementation recommendations. |
| 3.0 | 2025-11-14 | Linoy Pappachan Malakkaran | Removed flow diagrams, webhook references, payment processing references. Added Keycloak SSO authentication, NIF validation API, invoice download API, status retrieval API, and consolidated CNCA certificate submission API. Updated table format to 6 columns. |

---

<div style="page-break-before: always;"></div>

## 📑 Table of Contents

<div class="toc-container">

<table>
<tbody>
<tr class="toc-section"><td>1</td><td><a href="#1-introduction">Introduction</a> 📖</td><td>5</td></tr>
<tr class="toc-subsection"><td>1.1</td><td><a href="#11-purpose">Purpose</a></td><td>5</td></tr>
<tr class="toc-subsection"><td>1.2</td><td><a href="#12-scope">Scope</a></td><td>5</td></tr>
<tr class="toc-subsection"><td>1.3</td><td><a href="#13-audience">Audience</a></td><td>6</td></tr>
<tr class="toc-subsection"><td>1.4</td><td><a href="#14-definitions">Definitions</a></td><td>6</td></tr>

<tr class="toc-section"><td>2</td><td><a href="#2-system-overview-">System Overview</a> 🏗️</td><td>7</td></tr>
<tr class="toc-subsection"><td>2.1</td><td><a href="#21-system-architecture">System Architecture</a></td><td>7</td></tr>
<tr class="toc-subsection"><td>2.2</td><td><a href="#22-integration-pattern">Integration Pattern</a></td><td>8</td></tr>
<tr class="toc-subsection"><td>2.3</td><td><a href="#23-system-actors">System Actors</a></td><td>9</td></tr>
<tr class="toc-subsection"><td>2.4</td><td><a href="#24-amendment-and-cancellation-capabilities">Amendment and Cancellation Capabilities</a></td><td>10</td></tr>

<tr class="toc-section"><td>3</td><td><a href="#3-process-flows-">Process Flows</a> 🔄</td><td>11</td></tr>
<tr class="toc-subsection"><td>3.1</td><td><a href="#31-as-is-process-analysis">As-Is Process Analysis</a></td><td>11</td></tr>
<tr class="toc-subsection"><td>3.2</td><td><a href="#32-to-be-process">To-Be Process</a></td><td>13</td></tr>
<tr class="toc-subsubsection"><td>3.2.1</td><td><a href="#321-section-by-section-certificate-submission-workflow">Section-by-Section Certificate Submission Workflow</a></td><td>13</td></tr>

<tr class="toc-subsection"><td>3.3</td><td><a href="#33-system-integration-architecture">System Integration Architecture</a></td><td>16</td></tr>
<tr class="toc-subsection"><td>3.4</td><td><a href="#34-amendment-workflow-process">Amendment Workflow Process</a></td><td>17</td></tr>
<tr class="toc-subsection"><td>3.5</td><td><a href="#35-cancellation-workflow-process">Cancellation Workflow Process</a></td><td>18</td></tr>
<tr class="toc-subsection"><td>3.6</td><td><a href="#36-arccla-approval-workflows">ARCCLA Approval Workflows</a></td><td>19</td></tr>

<tr class="toc-section"><td>4</td><td><a href="#4-data-models-">Data Models</a> 📊</td><td>20</td></tr>
<tr class="toc-subsection"><td>4.1</td><td><a href="#41-core-ctn-entity-structure">Core CTN Entity Structure</a></td><td>20</td></tr>
<tr class="toc-subsection"><td>4.2</td><td><a href="#42-amendment-entity-structure">Amendment Entity Structure</a></td><td>22</td></tr>
<tr class="toc-subsection"><td>4.3</td><td><a href="#43-cancellation-entity-structure">Cancellation Entity Structure</a></td><td>23</td></tr>
<tr class="toc-subsection"><td>4.4</td><td><a href="#44-status-management">Status Management</a></td><td>24</td></tr>

<tr class="toc-section"><td>5</td><td><a href="#5-core-api-specifications-">Core API Specifications</a> 🔗</td><td>25</td></tr>
<tr class="toc-subsection"><td>5.1</td><td><strong><a href="#51-master-data-apis">Master Data APIs</a></strong></td><td>25</td></tr>
<tr class="toc-subsubsection"><td>5.1.1</td><td><a href="#511-cargo-types-api">Cargo Types API</a></td><td>25</td></tr>
<tr class="toc-subsubsection"><td>5.1.2</td><td><a href="#512-incoterms-api">Incoterms API</a></td><td>27</td></tr>
<tr class="toc-subsubsection"><td>5.1.3</td><td><a href="#513-countries-api">Countries API</a></td><td>29</td></tr>
<tr class="toc-subsubsection"><td>5.1.4</td><td><a href="#514-carriers-api">Carriers API</a></td><td>31</td></tr>
<tr class="toc-subsubsection"><td>5.1.5</td><td><a href="#515-currencies-api">Currencies API</a></td><td>33</td></tr>
<tr class="toc-subsubsection"><td>5.1.6</td><td><a href="#516-banks-api">Banks API</a></td><td>35</td></tr>
<tr class="toc-subsubsection"><td>5.1.7</td><td><a href="#517-units-api">Units API</a></td><td>37</td></tr>
<tr class="toc-subsubsection"><td>5.1.8</td><td><a href="#518-container-types-api">Container Types API</a></td><td>39</td></tr>
<tr class="toc-subsubsection"><td>5.1.9</td><td><a href="#519-transport-types-api">Transport Types API</a></td><td>41</td></tr>
<tr class="toc-subsubsection"><td>5.1.10</td><td><a href="#5110-locationsports-api">Locations/Ports API</a></td><td>43</td></tr>
<tr class="toc-subsubsection"><td>5.1.11</td><td><a href="#5111-goods-classifications-api">Goods Classifications API</a></td><td>45</td></tr>
<tr class="toc-subsubsection"><td>5.1.12</td><td><a href="#5112-imo-codes-api">IMO Codes API</a></td><td>47</td></tr>
<tr class="toc-subsubsection"><td>5.1.13</td><td><a href="#5113-vessels-api">Vessels API</a></td><td>49</td></tr>
<tr class="toc-subsubsection"><td>5.1.14</td><td><a href="#5114-ctn-cities-api">CTN Cities API</a></td><td>51</td></tr>
<tr class="toc-subsubsection"><td>5.1.15</td><td><a href="#5115-ctn-ports-api">CTN Ports API</a></td><td>53</td></tr>
<tr class="toc-subsection"><td>5.2</td><td><strong><a href="#52-certificate-management-apis">Certificate Management APIs</a></strong></td><td>55</td></tr>
<tr class="toc-subsubsection"><td>5.2.1</td><td><a href="#521-ctn-list-api">CTN List API</a></td><td>55</td></tr>
<tr class="toc-subsubsection"><td>5.2.2</td><td><a href="#522-ctn-details-api">CTN Details API</a></td><td>57</td></tr>
<tr class="toc-subsubsection"><td>5.2.3</td><td><a href="#523-ctn-attachments-api">CTN Attachments API</a></td><td>59</td></tr>
<tr class="toc-subsubsection"><td>5.2.4</td><td><a href="#524-freight-payment-types-api">Freight Payment Types API</a></td><td>61</td></tr>
<tr class="toc-subsubsection"><td>5.2.5</td><td><a href="#525-ctn-creation-api-certificate-submission">CTN Creation API (Certificate Submission)</a></td><td>63</td></tr>
<tr class="toc-subsubsection"><td>5.2.6</td><td><a href="#526-nif-validation-api-angola-tax-registration-number">NIF Validation API (Angola Tax Registration Number)</a></td><td>67</td></tr>
<tr class="toc-subsubsection"><td>5.2.7</td><td><a href="#527-invoice-download-api">Invoice Download API</a></td><td>69</td></tr>
<tr class="toc-subsection"><td>5.3</td><td><strong><a href="#53-ctn-related-entity-apis">CTN Related Entity APIs</a></strong></td><td>79</td></tr>
<tr class="toc-subsubsection"><td>5.3.1</td><td><a href="#531-consignees-api">Consignees API</a></td><td>79</td></tr>
<tr class="toc-subsubsection"><td>5.3.2</td><td><a href="#532-attachment-names-api">Attachment Names API</a></td><td>81</td></tr>
<tr class="toc-subsubsection"><td>5.3.3</td><td><a href="#533-ctn-tracking-api">CTN Tracking API</a></td><td>83</td></tr>

<tr class="toc-section"><td>6</td><td><a href="#6-enhanced-api-capabilities-">Enhanced API Capabilities</a> ⚡</td><td>85</td></tr>
<tr class="toc-subsection"><td>6.1</td><td><a href="#61-amendment-apis">Amendment APIs</a></td><td>85</td></tr>
<tr class="toc-subsection"><td>6.2</td><td><a href="#62-cancellation-apis">Cancellation APIs</a></td><td>87</td></tr>
<tr class="toc-subsection"><td>6.3</td><td><a href="#63-approval-workflow-apis">Approval Workflow APIs</a></td><td>89</td></tr>
<tr class="toc-subsection"><td>6.4</td><td><a href="#64-status-polling-apis">Status Polling APIs</a></td><td>91</td></tr>

<tr class="toc-section"><td>7</td><td><a href="#7-api-implementation-summary-">API Implementation Summary</a> 📊</td><td>93</td></tr>
<tr class="toc-subsection"><td>7.1</td><td><a href="#71-complete-cnca-certificate-api-coverage">Complete CNCA Certificate API Coverage</a></td><td>93</td></tr>
<tr class="toc-subsection"><td>7.2</td><td><a href="#72-implementation-readiness">Implementation Readiness</a></td><td>95</td></tr>

<tr class="toc-section"><td>8</td><td><a href="#8-validation-framework-">Validation Framework</a> ✅</td><td>97</td></tr>
<tr class="toc-subsection"><td>8.1</td><td><a href="#81-field-level-validation-rules">Field-Level Validation Rules</a></td><td>97</td></tr>
<tr class="toc-subsection"><td>8.2</td><td><a href="#82-business-validation-rules">Business Validation Rules</a></td><td>99</td></tr>
<tr class="toc-subsection"><td>8.3</td><td><a href="#83-authentication-and-authorization">Authentication and Authorization</a></td><td>101</td></tr>
<tr class="toc-subsubsection"><td>8.3.1</td><td><a href="#831-sso-solution---keycloak">SSO Solution - Keycloak</a></td><td>101</td></tr>
<tr class="toc-subsubsection"><td>8.3.2</td><td><a href="#832-supported-authentication-protocols">Supported Authentication Protocols</a></td><td>102</td></tr>
<tr class="toc-subsubsection"><td>8.3.3</td><td><a href="#833-client-integration-capabilities">Client Integration Capabilities</a></td><td>103</td></tr>
<tr class="toc-subsubsection"><td>8.3.4</td><td><a href="#834-jwt-token-management">JWT Token Management</a></td><td>104</td></tr>
<tr class="toc-subsubsection"><td>8.3.5</td><td><a href="#835-integration-requirements">Integration Requirements</a></td><td>106</td></tr>
</tbody>
</table>

</div>

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
- Certificate download and status tracking
- Real-time status tracking and notifications

**SINTECE System (ARCCLA)**
- Backend certificate processing and approval system
- ARCCLA broker review workflow
- Amendment/cancellation approval processes
- Certificate issuance and status management
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
1. **Initial CTN Creation**: JUL creates basic CTN record with core information via POST /api/ctns
2. **Section-wise Data Addition**: JUL adds detailed information in separate steps (internal to JUL system):
   - **Addresses**: Shipper, consignee, forwarder, notify party details
   - **Goods**: Cargo descriptions, classifications, weights, values
   - **Containers**: Container types, numbers, seals
   - **Tracking**: Transport routes, vessels, ports, schedules
   - **Attachments**: Supporting documents
3. **Certificate Validation**: SINTECE validates complete certificate data with business rules
4. **Visa Request Submission**: JUL submits for approval via POST /api/ctns/actions/requestvisa/{id}
5. **ARCCLA Review**: ARCCLA broker reviews and approves/rejects certificate
6. **Certificate Issuance**: Certificate issued with amendment/cancellation capabilities
7. **Status Updates**: Status communicated via API polling and notifications

---

*Amendment Flow:*
1. JUL validates amendment eligibility using canAmend status flag
2. JUL submits amendment request via POST /api/CTNs/{id}/amendments with change tracking
3. SINTECE validates amendment request and notifies ARCCLA broker
4. ARCCLA broker reviews amendment in SINTECE with impact analysis
5. SINTECE sends amendment approval/rejection to JUL via notifications
6. If approved, SINTECE updates certificate and certificate status
7. JUL updates certificate status and notifies stakeholders

*Cancellation Flow:*
1. JUL validates cancellation eligibility using canCancel status flag
2. JUL submits cancellation request via POST /api/CTNs/{id}/cancellations with reason documentation
3. SINTECE validates cancellation request and calculates financial impact
4. ARCCLA broker reviews cancellation in SINTECE with impact analysis
5. SINTECE sends cancellation approval/rejection to JUL via notifications
6. If approved, SINTECE processes cancellation and updates certificate status

### 2.3 System Actors

The following actors interact with the integrated system:

| **Actor** | **Role** | **System Access** |
|-----------|----------|-------------------|
| **Trader (Importer/Exporter)** | Business entity shipping goods to/from Angola | JUL System (Web Portal) |
| **Customs Broker / Freight Forwarder** | Licensed agent representing trader with amendment/cancellation capabilities | JUL System (Web Portal with Amendment/Cancellation Features) |
| **ARCCLA Broker** | Government official authorized to approve certificates, amendments, and cancellations | SINTECE System (Internal Portal with Amendment/Cancellation Workflows) |

**Enhanced User Interaction Flow:**

*Standard Certificate Flow:*
1. **Trader** logs into enhanced JUL → Creates certificate request → Uploads documents → Nominates broker
2. **Customs Broker** logs into enhanced JUL → Accepts nomination → Completes application with real-time validation → Submits to SINTECE
3. **ARCCLA Broker** logs into enhanced SINTECE → Reviews request with decision support tools → Approves/Rejects → Generates certificate (if approved)
4. **Trader** and **Customs Broker** receive certificate in JUL → Download and use for customs clearance

*Amendment Flow:*
1. **Customs Broker** checks amendment eligibility in JUL → Creates amendment request → Documents changes
2. **ARCCLA Broker** receives amendment notification in SINTECE → Reviews changes with impact analysis → Approves/Rejects
3. **Customs Broker** receives amendment decision in JUL → Updates stakeholders
4. **Trader** receives updated certificate with amendment history in JUL

*Cancellation Flow:*
1. **Customs Broker** checks cancellation eligibility in JUL → Creates cancellation request → Documents reasons
2. **ARCCLA Broker** receives cancellation notification in SINTECE → Reviews with impact analysis → Approves/Rejects
3. **Customs Broker** receives cancellation decision in JUL → Updates stakeholders
4. **Trader** receives cancellation confirmation

### 2.4 Amendment and Cancellation Capabilities

**Amendment Management:**
- Real-time eligibility validation based on certificate status
- Change tracking with before/after value comparison
- Impact analysis for proposed amendments
- Role-based approval workflow
- Complete audit trail with history

**Cancellation Management:**
- Real-time eligibility validation with financial impact assessment
- Reason code documentation
- Role-based approval workflow with escalation
- Complete audit trail

**Enhanced Status Management:**
- Dynamic eligibility flags (canAmend, canCancel) based on real-time business rules
- Enhanced status workflow supporting amendment/cancellation states
- Real-time status tracking and notifications
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

The JUL-SINTECE integration introduces a fully digital workflow with section-by-section certificate submission capabilities to improve data accuracy and user experience.

#### 3.2.1 Section-by-Section Certificate Submission Workflow

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                        CNCA CERTIFICATE SUBMISSION WORKFLOW                         │
└─────────────────────────────────────────────────────────────────────────────────────┘

   JUL System                          SINTECE System                     ARCCLA System
        │                                    │                                   │
        │ 1. POST /api/ctns                 │                                   │
        │ ─────────────────────────────────► │ Create Basic CTN Record          │
        │                                    │ Status: Draft                    │
        │ ◄───────────── CTN ID: 503808     │                                   │
        │                                    │                                   │
        │ 2. POST /api/ctnAddresses          │                                   │
        │ ─────────────────────────────────► │ Add Shipper/Consignee           │
        │                                    │ Add Forwarder/Notify Party       │
        │ ◄───────────── Address IDs         │                                   │
        │                                    │                                   │
        │ 3. POST /api/ctnGoods              │                                   │
        │ ─────────────────────────────────► │ Add Cargo Details               │
        │                                    │ Classifications & Values          │
        │ ◄───────────── Goods ID            │                                   │
        │                                    │                                   │
        │ 4. POST /api/ctnContainers         │                                   │
        │ ─────────────────────────────────► │ Add Container Information        │
        │                                    │ Container Numbers & Seals        │
        │ ◄───────────── Container ID        │                                   │
        │                                    │                                   │
        │ 5. POST /api/ctnTracking           │                                   │
        │ ─────────────────────────────────► │ Add Transport Routes            │
        │                                    │ Vessel & Port Information        │
        │ ◄───────────── Tracking ID         │                                   │
        │                                    │                                   │
        │ 6. POST /api/fileupload            │                                   │
        │ ─────────────────────────────────► │ Upload Documents                │
        │ ◄───────────── File GUID           │                                   │
        │                                    │                                   │
        │ 7. POST /api/ctnAttachments        │                                   │
        │ ─────────────────────────────────► │ Link Documents to CTN           │
        │ ◄───────────── Attachment ID       │                                   │
        │                                    │                                   │
        │ 8. POST /api/ctns/actions/         │                                   │
        │    requestvisa/503808              │                                   │
        │ ─────────────────────────────────► │ Validate Complete Data          │
        │                                    │ Submit for Approval              │
        │                                    │ Status: Pending Review           │
        │                                    │ ─────────────────────────────► │ │
        │                                    │                               │ │
        │                                    │ ◄───────────────────────────── │ │
        │ ◄───────────── Visa Response       │ Review & Decision               │
        │                                    │ Status: Approved/Rejected       │
        │                                    │                                   │
        
┌─────────────────────────────────────────────────────────────────────────────────────┐
│ SECTION-BY-SECTION BENEFITS:                                                        │
│ ✓ Improved User Experience - Step-by-step data entry                               │
│ ✓ Enhanced Data Quality - Focused validation per section                           │
│ ✓ Progress Tracking - Users can save and resume                                    │
│ ✓ Flexible Workflow - Optional sections based on cargo type                        │
│ ✓ Error Isolation - Issues contained to specific sections                          │
│ ✓ API Efficiency - Smaller, targeted API calls                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```



> **✅ Core Certificate Process Improvements:**
> 1. **Digital Initiation**: Traders initiate requests directly through JUL system with section-by-section data entry
> 2. **Progressive Document Building**: Step-by-step completion of certificate sections for improved data quality
> 3. **Automated Validation**: Real-time validation of submitted data at each section
> 4. **Streamlined Approval**: ARCCLA brokers receive complete, validated requests for review
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

### 3.3 System Integration Architecture

The integration establishes comprehensive touchpoints between JUL and SINTECE systems with a modern API-driven architecture and centralized authentication.

**System Integration Overview:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    SYSTEM INTEGRATION ARCHITECTURE               │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────────┐         ┌──────────────────────┐
│   JUL SYSTEM         │         │  KEYCLOAK SSO        │
│   (Owner: ADP)       │◄────────┤  (Owner: ADP)        │
│                      │  Auth   │                      │
│  • Certificate UI    │         │  • Authentication    │
│  • Document Mgmt     │         │  • Authorization     │
│  • Status Tracking   │         │  • JWT Token Mgmt    │
│  • User Portal       │         │  • Role Management   │
└──────────┬───────────┘         └──────────────────────┘
           │                              ▲
           │ REST APIs                    │ Auth
           │ (HTTPS/TLS)                  │
           ▼                              │
┌──────────────────────┐         ┌──────────────────────┐
│  INTEGRATION LAYER   │         │  SINTECE SYSTEM      │
│  (Owner: Shared)     │◄────────┤  (Owner: ARCCLA)     │
│                      │  Auth   │                      │
│  • API Gateway       │         │  • Certificate       │
│  • Data Transform    │         │    Processing        │
│  • Validation        │         │  • Approval Workflow │
│  • Error Handling    │         │  • Master Data Mgmt  │
└──────────────────────┘         │  • Status Management │
                                 └──────────────────────┘

KEY INTEGRATION POINTS:
─────────────────────────────────────────────────────────
• Authentication: Keycloak SSO with JWT tokens
• Master Data Sync: Real-time via REST APIs
• Certificate Submission: Section-by-section APIs
• Status Updates: Polling-based status retrieval
• Document Exchange: Secure file transfer APIs
```

**Component Ownership Table:**

| Component | Owner | Responsibilities |
|-----------|-------|------------------|
| **JUL System** | Abu Dhabi Ports (ADP) | User interface, certificate request initiation, document upload, status display, user notifications, certificate download |
| **Keycloak SSO** | Abu Dhabi Ports (ADP) | User authentication, authorization, JWT token issuance and validation, session management, role-based access control |
| **Integration Layer** | Shared (ADP + ARCCLA) | API gateway, request/response transformation, data validation, error handling, logging and monitoring |
| **SINTECE System** | ARCCLA (Angola) | Certificate processing, approval workflows, master data management, certificate issuance, status management |

**Integration Flow Description:**
1. User authenticates via Keycloak SSO (OpenID Connect/OAuth2)
2. JUL obtains JWT access token for API authorization
3. JUL sends certificate data to SINTECE via REST APIs
4. Integration layer validates and transforms requests
5. SINTECE processes certificate and updates status
6. JUL polls SINTECE for status updates
7. Certificate issued and available for download

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
- Document management and storage
- Audit logging and compliance reporting

### 3.4 Amendment Workflow Process

The amendment workflow provides controlled modification capabilities for issued certificates with comprehensive ARCCLA approval processes.

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

**Cancellation Request Initiation:**
1. **Eligibility Check**: System validates certificate status and cancellation permissions
2. **Impact Assessment**: System calculates impact and eligibility
3. **Request Creation**: Customs broker provides cancellation reason and additional details
4. **Submission**: Cancellation request is submitted to ARCCLA for review

**ARCCLA Review and Processing:**
1. **Notification**: ARCCLA broker receives cancellation request notification
2. **Review**: Validation of cancellation reason and business justification
3. **Analysis**: Review of cancellation impact and timing
4. **Decision**: Approval or rejection of cancellation request
5. **Processing**: For approved cancellations, certificate is cancelled

**Cancellation Eligibility Rules:**
- Certificate status allows cancellation (not yet issued or used for customs clearance)
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
    "MultiLingualDescription": {
      "Id": 2183,
      "Translations": [
        {
          "Id": 2187,
          "LanguageISO": "en",
          "MultiLingualTextId": 2183,
          "Text": "CONTAINER"
        },
        {
          "Id": 2188,
          "LanguageISO": "fr",
          "MultiLingualTextId": 2183,
          "Text": "CONTENEUR"
        },
        {
          "Id": 2304,
          "LanguageISO": "pt",
          "MultiLingualTextId": 2183,
          "Text": "Contentor"
        }
      ]
    },
    "Code": "CONTAINER",
    "CargoType_Desc": "CONTAINER",
    "CreatedOn": null,
    "CreatedById": null,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "MultiLingualDescription": {
      "Id": 2184,
      "Translations": [
        {
          "Id": 2189,
          "LanguageISO": "en",
          "Text": "BULK"
        },
        {
          "Id": 2190,
          "LanguageISO": "fr",
          "Text": "VRAC"
        },
        {
          "Id": 2309,
          "LanguageISO": "pt",
          "Text": "Sacrias ou carga fracionada"
        }
      ]
    },
    "Code": "BULK",
    "CargoType_Desc": "BULK",
    "CreatedOn": null,
    "CreatedById": null,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
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

**Sample JSON Request:**
```json
GET /api/Incoterms?$sort=IncotermCode&IncotermCode=&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 6,
    "IncotermCode": "CFR",
    "MultiLingualDescription": {
      "Id": 2211,
      "Translations": [
        {
          "Id": 2238,
          "LanguageISO": "en",
          "MultiLingualTextId": 2211,
          "Text": "Cost and Freight"
        }
      ],
      "DescriptiveFields": "Cost and Freight"
    },
    "Active": true,
    "CreatedOn": null,
    "ModifiedOn": "2023-01-11T16:51:28.8309058",
    "ModifiedById": 1,
    "ModifiedByLogin": "TCNT"
  },
  {
    "Id": 2,
    "IncotermCode": "CIF",
    "MultiLingualDescription": {
      "Id": 2207,
      "Translations": [
        {
          "Id": 2234,
          "LanguageISO": "en",
          "Text": "Cost, Insurance, Freight"
        }
      ],
      "DescriptiveFields": "Cost, Insurance, Freight"
    },
    "Active": true,
    "CreatedOn": null,
    "ModifiedOn": null,
    "ModifiedById": null
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

**Business Purpose:** Manages shipping carrier information essential for maritime transport documentation and tracking. Critical for bill of lading validation, carrier liability determination, vessel scheduling coordination, and ensuring proper documentation of transportation responsibility throughout the supply chain.

**Endpoint:** `GET /api/Carriers`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Name |
| 2 | Name | String - 200 | O | Filter by carrier name | A.C. ORSSLEFF'S |
| 3 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **CARRIER_UI_001**: Name filter optional, 1-200 characters
- **CARRIER_UI_002**: Display carrier name with city/country for clarity
- **CARRIER_UI_003**: Auto-complete dropdown with carrier search

**Business Validation Rules:**
- **CARRIER_BV_001**: Only active carriers allowed for new shipments
- **CARRIER_BV_002**: Carrier must be authorized for the route
- **CARRIER_BV_003**: Carrier contact information required for tracking

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique carrier identifier | 789 |
| 2 | Name | String - 200 | M | Carrier company name | A.C. ORSSLEFF'S EFTF A/S |
| 3 | LicenseNumber | String - 50 | O | Carrier license number | LICENSE123 |
| 4 | Address | String - 500 | O | Carrier address | Kongevejen 40 |
| 5 | City | String - 100 | O | Carrier city | 2840 Holte |
| 6 | CountryId | Integer | O | Country identifier | 56 |
| 7 | Email | String - 200 | O | Contact email | chartering@acoe.dk |
| 8 | Telephone | String - 50 | O | Contact telephone | +45 45 46 00 66 |
| 9 | TrackingURL | String - 500 | O | Tracking website URL | https://track.carrier.com |

**Error Codes:**
- **CARRIER_E001**: "Invalid parameters" (HTTP 400)
- **CARRIER_E002**: "No data found" (HTTP 404)
- **CARRIER_E003**: "Access denied" (HTTP 403)

**Sample JSON Request:**
```json
GET /api/Carriers?$sort=Name&Name=&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1343,
    "LicenseNumber": null,
    "Address": "Care of ZEABORN Ship Management GmbH & Cie KG , Ludwig-Erhard-Strasse 22, 20459 Hamburg, Germany",
    "City": "Hamburg",
    "CountryId": 54,
    "Email": null,
    "Name": "\"E.R. BRISTOL\" Schiffsbeteiligungsgesellschaft",
    "Telephone": null,
    "TrackingURL": null,
    "CreatedOn": "2020-07-17T08:57:52.973",
    "CreatedById": 1,
    "ModifiedOn": "2020-07-17T08:57:52.973",
    "ModifiedById": 1
  },
  {
    "Id": 789,
    "LicenseNumber": null,
    "Address": "Kongevejen 40",
    "City": "2840 Holte",
    "CountryId": 56,
    "Email": "chartering@acoe.dk",
    "Name": "A.C. ORSSLEFF'S EFTF A/S",
    "Telephone": "+45 45 46 00 66",
    "TrackingURL": "",
    "CreatedOn": "2008-05-13T08:36:14",
    "CreatedById": 1,
    "ModifiedOn": "2018-08-29T09:24:35.927",
    "ModifiedById": 1
  }
]
```

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

**Sample JSON Request:**
```json
GET /api/Currencies?$sort=Code&Code=USD&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "Code": "EUR",
    "MarkedForUpdate": false,
    "Countries": [],
    "Exchange_rates": [],
    "CreatedOn": null,
    "CreatedById": null,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "Code": "USD",
    "MarkedForUpdate": false,
    "Countries": [],
    "Exchange_rates": [],
    "CreatedOn": null,
    "CreatedById": null,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.1.6 Banks API

**Business Purpose:** Manages banking institution data for payment processing and invoice generation in CNCA certificate transactions. Essential for financial settlements, payment validations, and generating proper invoicing documentation with correct banking details.

**Endpoint:** `GET /api/Banks`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Name |
| 2 | Name | String - 200 | O | Filter by bank name | Standard Bank |
| 3 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **BANK_UI_001**: Bank name filter optional, 1-200 characters
- **BANK_UI_002**: Display active banks only in dropdown selection
- **BANK_UI_003**: Validate bank selection for payment processing

**Business Validation Rules:**
- **BANK_BV_001**: Only active banks allowed for new payments
- **BANK_BV_002**: Bank must support international transfers for foreign traders
- **BANK_BV_003**: Bank details required for invoice generation

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique bank identifier | 15 |
| 2 | Name | String - 200 | M | Bank institution name | Standard Bank Angola |
| 3 | Code | String - 20 | O | Bank code | SBA |
| 4 | SwiftCode | String - 11 | O | International SWIFT code | SBICAOLU |
| 5 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **BANK_E001**: "Invalid parameters" (HTTP 400)
- **BANK_E002**: "No data found" (HTTP 404)
- **BANK_E003**: "Access denied" (HTTP 403)

**Sample JSON Request:**
```json
GET /api/Banks?$sort=Name&Name=&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "Name": "Banco Angolano de Investimentos",
    "Code": "BAI",
    "Address": "Rua Major Kanhangulo, nº 34",
    "City": "Luanda",
    "CountryID": 10,
    "Country": {
      "Id": 10,
      "Country_Code": "AO",
      "Country_Name": "Angola",
      "ExportingCountry": true,
      "ImportingCountry": true
    },
    "Website": "http://www.bancobai.ao",
    "Telephone": "222 693 800 / 222 693 899",
    "NIFNumber": null,
    "CreatedOn": null,
    "ModifiedOn": "2023-01-24T11:54:44.7181885",
    "ModifiedById": 1,
    "ModifiedByLogin": "TCNT"
  },
  {
    "Id": 2,
    "Name": "Banco Angolano de Negocios e Comercio, S.A.",
    "Code": "BANC",
    "Address": "Travessa da Sorte, nº 12. Maianga",
    "City": "Luanda",
    "CountryID": 10,
    "Country": {
      "Id": 10,
      "Country_Code": "AO",
      "Country_Name": "Angola",
      "ExportingCountry": true,
      "ImportingCountry": true
    },
    "Website": null,
    "Telephone": null,
    "NIFNumber": null,
    "CreatedOn": null,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```
- **BANK_E002**: "Bank not authorized for transactions" (HTTP 422)
- **BANK_E003**: "Inactive bank selected" (HTTP 422)

#### 5.1.7 Units API

**Business Purpose:** Manages measurement unit definitions essential for accurate quantity and weight calculations in cargo documentation. Critical for ensuring consistent unit conversions, compliance with international standards, and accurate cost calculations based on cargo measurements.

**Endpoint:** `GET /api/Units`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Unit_Desc |
| 2 | Unit_Desc | String - 50 | O | Filter by unit description | KG |
| 3 | UnitType | String - 20 | O | Filter by unit category | Weight |
| 4 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **UNIT_UI_001**: Unit description required, 1-50 characters
- **UNIT_UI_002**: Unit type selection from predefined categories
- **UNIT_UI_003**: Display with conversion factors for clarity

**Business Validation Rules:**
- **UNIT_BV_001**: Unit must be internationally recognized standard
- **UNIT_BV_002**: Conversion factors must be mathematically accurate
- **UNIT_BV_003**: Weight units required for cargo calculations

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique unit identifier | 1 |
| 2 | Unit_Desc | String - 50 | M | Unit description | Kilogram |
| 3 | UnitSymbol | String - 10 | M | Standard unit symbol | KG |
| 4 | UnitType | String - 20 | M | Unit category | Weight |
| 5 | ConversionFactor | Decimal | O | Conversion to base unit | 1.000 |
| 6 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **UNIT_E001**: "Invalid unit parameters" (HTTP 400)
- **UNIT_E002**: "Unit not found" (HTTP 404)
- **UNIT_E003**: "Unit conversion error" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/Units?$sort=Unit_Desc&UnitType=Weight&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "Unit_Desc": "Kilogram",
    "UnitSymbol": "KG",
    "UnitType": "Weight",
    "ConversionFactor": 1.000,
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "Unit_Desc": "Ton",
    "UnitSymbol": "TON",
    "UnitType": "Weight",
    "ConversionFactor": 1000.000,
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.1.8 Container Types API

**Business Purpose:** Manages container type classifications essential for proper container booking, handling procedures, and shipping cost calculations. Critical for determining container capacity, weight limits, handling requirements, and ensuring accurate freight calculations based on container specifications.

**Endpoint:** `GET /api/ContainerTypes`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Container_Type |
| 2 | Container_Type | String - 50 | O | Filter by container type | 20GP |
| 3 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **CONTAINER_UI_001**: Container type filter optional, 1-50 characters
- **CONTAINER_UI_002**: Display container type with dimensions for clarity
- **CONTAINER_UI_003**: Group standard vs special container types

**Business Validation Rules:**
- **CONTAINER_BV_001**: Container type must match cargo requirements
- **CONTAINER_BV_002**: Dangerous goods require specialized containers
- **CONTAINER_BV_003**: Weight limits vary by container type

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique container type identifier | 1 |
| 2 | Container_Type | String - 50 | M | Container type code | 20GP |
| 3 | Description | String - 200 | M | Container description | 20-foot General Purpose |
| 4 | Length | Decimal | O | Container length in feet | 20.00 |
| 5 | Width | Decimal | O | Container width in feet | 8.00 |
| 6 | Height | Decimal | O | Container height in feet | 8.50 |
| 7 | MaxWeight | Decimal | O | Maximum weight capacity in tons | 28.20 |
| 8 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **CONTAINER_E001**: "Invalid parameters" (HTTP 400)
- **CONTAINER_E002**: "Container type not found" (HTTP 404)
- **CONTAINER_E003**: "Container type not applicable for cargo" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/ContainerTypes?$sort=Container_Type&Container_Type=20GP&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "Container_Type": "20GP",
    "Description": "20-foot General Purpose",
    "Length": 20.00,
    "Width": 8.00,
    "Height": 8.50,
    "MaxWeight": 28.20,
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "Container_Type": "40GP",
    "Description": "40-foot General Purpose",
    "Length": 40.00,
    "Width": 8.00,
    "Height": 8.50,
    "MaxWeight": 30.48,
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.1.9 Transport Types API

**Business Purpose:** Manages transportation mode classifications essential for logistics planning, route optimization, and freight calculations. Critical for determining shipping costs, transit times, regulatory requirements, and ensuring proper transport documentation based on cargo and route characteristics.

**Endpoint:** `GET /api/TransportTypes`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Type_Name |
| 2 | Type_Name | String - 50 | O | Filter by transport type | Sea |
| 3 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **TRANSPORT_UI_001**: Transport type filter optional, 1-50 characters
- **TRANSPORT_UI_002**: Display with appropriate transport icons
- **TRANSPORT_UI_003**: Group by transport mode for clarity

**Business Validation Rules:**
- **TRANSPORT_BV_001**: Transport type must match cargo requirements
- **TRANSPORT_BV_002**: Dangerous goods require specific transport modes
- **TRANSPORT_BV_003**: Some goods restricted for certain transport types

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique transport type identifier | 1 |
| 2 | Type_Name | String - 50 | M | Transport type name | Sea |
| 3 | Description | String - 200 | O | Transport type description | Maritime sea transport |
| 4 | Code | String - 10 | O | Transport type code | SEA |
| 5 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **TRANSPORT_E001**: "Invalid parameters" (HTTP 400)
- **TRANSPORT_E002**: "Transport type not found" (HTTP 404)
- **TRANSPORT_E003**: "Transport type not applicable for cargo" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/TransportTypes?$sort=Type_Name&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "Type_Name": "Air",
    "Description": "Air cargo transport",
    "Code": "AIR",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "Type_Name": "Sea",
    "Description": "Maritime sea transport",
    "Code": "SEA",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.1.10 Locations/Ports API

**Business Purpose:** Manages geographical location and port information essential for origin/destination tracking, routing decisions, and customs compliance. Critical for calculating shipping routes, determining applicable regulations, port charges, and ensuring accurate geographic references in certificates and shipping documents.

**Endpoint:** `GET /api/Locations`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | PortName |
| 2 | CountryId | Integer | M | Country identifier filter | 4 |
| 3 | PortName | String - 200 | O | Filter by port name | Dubai |
| 4 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **LOCATION_UI_001**: Country ID required for location filtering
- **LOCATION_UI_002**: Port name search minimum 2 characters
- **LOCATION_UI_003**: Display with country name for clarity

**Business Validation Rules:**
- **LOCATION_BV_001**: Location must be active port for shipping
- **LOCATION_BV_002**: Port must support container operations
- **LOCATION_BV_003**: Location must have valid customs facilities

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique location identifier | 1 |
| 2 | PortName | String - 200 | M | Port/location name | Port of Dubai |
| 3 | PortCode | String - 10 | O | Standard port code | DXB |
| 4 | CountryId | Integer | M | Associated country | 4 |
| 5 | CountryName | String - 100 | O | Country name | United Arab Emirates |
| 6 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **LOCATION_E001**: "Invalid country ID" (HTTP 400)
- **LOCATION_E002**: "Port not found" (HTTP 404)
- **LOCATION_E003**: "Port not operational for cargo" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/Locations?$sort=PortName&CountryId=4&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "PortName": "Port of Dubai",
    "PortCode": "DXB",
    "CountryId": 4,
    "CountryName": "United Arab Emirates",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "PortName": "Abu Dhabi Port",
    "PortCode": "AUH",
    "CountryId": 4,
    "CountryName": "United Arab Emirates", 
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.1.11 Goods Classifications API

**Business Purpose:** Manages standardized goods classification codes essential for customs clearance, duty calculations, and regulatory compliance. Critical for determining applicable tariffs, import restrictions, statistical reporting, and ensuring proper cargo categorization according to international trade standards.

**Endpoint:** `GET /api/GoodsClassifications`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Goods_Classification_Desc |
| 2 | Goods_Classification_Desc | String - 200 | O | Filter by classification | Electronics |
| 3 | ClassificationCode | String - 20 | O | Filter by classification code | HS8517 |
| 4 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **GOODS_UI_001**: Classification filter minimum 3 characters
- **GOODS_UI_002**: Display with HS code for clarity
- **GOODS_UI_003**: Group by classification category

**Business Validation Rules:**
- **GOODS_BV_001**: Classification must be valid HS code
- **GOODS_BV_002**: Some goods require special permits
- **GOODS_BV_003**: Prohibited goods cannot be classified

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique classification identifier | 1 |
| 2 | Goods_Classification_Desc | String - 200 | M | Classification description | Electronic equipment |
| 3 | ClassificationCode | String - 20 | M | HS classification code | HS8517 |
| 4 | Category | String - 100 | O | Classification category | Electronics |
| 5 | DutyRate | Decimal | O | Applicable duty rate percentage | 5.00 |
| 6 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **GOODS_E001**: "Invalid classification parameters" (HTTP 400)
- **GOODS_E002**: "Classification not found" (HTTP 404)
- **GOODS_E003**: "Classification not applicable" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/GoodsClassifications?$sort=Goods_Classification_Desc&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "Goods_Classification_Desc": "Electronic equipment",
    "ClassificationCode": "HS8517",
    "Category": "Electronics",
    "DutyRate": 5.00,
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "Goods_Classification_Desc": "Textile products",
    "ClassificationCode": "HS6203",
    "Category": "Textiles",
    "DutyRate": 12.00,
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.1.12 IMO Codes API

**Business Purpose:** Manages International Maritime Organization dangerous goods classification codes essential for hazardous cargo handling, safety compliance, and regulatory adherence. Critical for determining special handling requirements, storage restrictions, transport documentation, and ensuring maritime safety standards compliance.

**Endpoint:** `GET /api/IMOs`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | IMO_Desc |
| 2 | IMO_Desc | String - 200 | O | Filter by IMO description | Flammable Liquids |
| 3 | IMOClass | String - 10 | O | Filter by IMO class | 3 |
| 4 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **IMO_UI_001**: IMO description filter minimum 3 characters
- **IMO_UI_002**: Display with hazard class for safety
- **IMO_UI_003**: Highlight dangerous goods with warning indicators

**Business Validation Rules:**
- **IMO_BV_001**: IMO class must be valid IMDG code
- **IMO_BV_002**: Dangerous goods require special documentation
- **IMO_BV_003**: Some IMO classes prohibited for certain routes

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique IMO identifier | 1 |
| 2 | IMO_Desc | String - 200 | M | IMO description | Flammable Liquids |
| 3 | IMOClass | String - 10 | M | IMDG hazard class | 3 |
| 4 | UNNumber | String - 10 | O | UN identification number | UN1203 |
| 5 | PackingGroup | String - 5 | O | Packing group classification | II |
| 6 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **IMO_E001**: "Invalid IMO parameters" (HTTP 400)
- **IMO_E002**: "IMO code not found" (HTTP 404)
- **IMO_E003**: "Dangerous goods not permitted" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/IMOs?$sort=IMO_Desc&IMOClass=3&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "IMO_Desc": "Flammable Liquids",
    "IMOClass": "3",
    "UNNumber": "UN1203",
    "PackingGroup": "II",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "IMO_Desc": "Corrosive Substances",
    "IMOClass": "8",
    "UNNumber": "UN1760",
    "PackingGroup": "II",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.1.13 Vessels API

**Business Purpose:** Manages vessel information essential for maritime transport operations, vessel tracking, and shipping documentation. Critical for identifying vessels in certificates, tracking cargo movements, ensuring vessel compliance, and providing accurate shipping details for customs and logistics operations.

**Endpoint:** `GET /api/Vessels`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Name |
| 2 | Name | String - 256 | O | Filter by vessel name | CPO HAMBURG |
| 3 | Code | String - 20 | O | Filter by vessel code | 229638000 |
| 4 | active | Integer | O | Active status filter | 1 |

**UI Validation Rules:**
- **VESSEL_UI_001**: Vessel name filter minimum 3 characters
- **VESSEL_UI_002**: Display with IMO number for identification
- **VESSEL_UI_003**: Show flag state for vessel information

**Business Validation Rules:**
- **VESSEL_BV_001**: Vessel must have valid IMO number
- **VESSEL_BV_002**: Vessel must be registered and active
- **VESSEL_BV_003**: Vessel must be suitable for cargo type

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique vessel identifier | 5132 |
| 2 | Name | String - 256 | M | Vessel name | CPO HAMBURG1234 |
| 3 | Code | String - 20 | M | Vessel identification code | 229638000 |
| 4 | IDNumber | String - 20 | M | IMO number | 9450375 |
| 5 | FlagId | Integer | O | Flag state identifier | 148 |
| 6 | Flag | String - 100 | O | Flag state name | Germany |
| 7 | Active | Boolean | M | Active status | true |

**Error Codes:**
- **VESSEL_E001**: "Invalid vessel parameters" (HTTP 400)
- **VESSEL_E002**: "Vessel not found" (HTTP 404)
- **VESSEL_E003**: "Vessel not available for route" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/Vessels?$sort=Name&Name=CPO&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 5132,
    "Name": "CPO HAMBURG1234",
    "Code": "229638000",
    "IDNumber": "9450375",
    "FlagId": 148,
    "Flag": "Germany",
    "Active": true,
    "CreatedOn": null,
    "CreatedById": null,
    "CreatedByLogin": null,
    "ModifiedOn": "2023-01-25T13:18:15.1194343",
    "ModifiedById": 13275,
    "ModifiedByLogin": "TESTEXCONSUL"
  },
  {
    "Id": 5163,
    "Name": "NILEDUTCH LION",
    "Code": "636013690",
    "IDNumber": "9337456",
    "FlagId": 128,
    "Flag": "Liberia",
    "Active": true,
    "CreatedOn": null,
    "CreatedById": null,
    "CreatedByLogin": null,
    "ModifiedOn": null,
    "ModifiedById": null,
    "ModifiedByLogin": null
  }
]
```

#### 5.1.14 CTN Cities API

**Business Purpose:** Manages city information essential for origin and destination tracking in certificate processing. Critical for accurate geographical references, determining applicable regulations, calculating logistics routes, and ensuring precise location data for customs compliance and certificate validation.

**Endpoint:** `GET /api/CTNCities`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Name |
| 2 | CountryId | Integer | M | Country identifier filter | 10 |
| 3 | Name | String - 200 | O | Filter by city name | Luanda |
| 4 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **CITY_UI_001**: Country ID required for city filtering
- **CITY_UI_002**: City name search minimum 2 characters
- **CITY_UI_003**: Display with country name for clarity

**Business Validation Rules:**
- **CITY_BV_001**: City must exist within selected country
- **CITY_BV_002**: City must be active for trade operations
- **CITY_BV_003**: City must support logistics operations

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique city identifier | 262 |
| 2 | Name | String - 200 | M | City name | Benguela |
| 3 | CountryId | Integer | M | Associated country identifier | 10 |
| 4 | Country | String - 100 | O | Country name | Angola |
| 5 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **CITY_E001**: "Invalid country ID" (HTTP 400)
- **CITY_E002**: "City not found" (HTTP 404)
- **CITY_E003**: "City not operational for trade" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/CTNCities?$sort=Name&CountryId=10&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 262,
    "Active": true,
    "CountryId": 10,
    "Name": "Benguela",
    "Country": "Angola",
    "CreatedOn": null,
    "CreatedById": null,
    "CreatedByLogin": null,
    "ModifiedOn": null,
    "ModifiedById": null,
    "ModifiedByLogin": null
  },
  {
    "Id": 277,
    "Active": true,
    "CountryId": 10,
    "Name": "Caála",
    "Country": "Angola",
    "CreatedOn": null,
    "CreatedById": null,
    "CreatedByLogin": null,
    "ModifiedOn": null,
    "ModifiedById": null,
    "ModifiedByLogin": null
  },
  {
    "Id": 255,
    "Active": true,
    "CountryId": 10,
    "Name": "Cabinda",
    "Country": "Angola",
    "CreatedOn": null,
    "CreatedById": null,
    "CreatedByLogin": null,
    "ModifiedOn": null,
    "ModifiedById": null,
    "ModifiedByLogin": null
  }
]
```

#### 5.1.15 CTN Ports API

**Business Purpose:** Manages Angolan port information essential for CTN certificate processing and customs clearance. Critical for determining applicable port authorities, customs offices, handling procedures, and ensuring accurate port references in certificates and logistics documentation.

**Endpoint:** `GET /api/CTNPorts`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | Name |
| 2 | Name | String - 100 | O | Filter by port name | Luanda |
| 3 | PortCode | String - 10 | O | Filter by port code | LAD |
| 4 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **CTNPORT_UI_001**: Port name search minimum 2 characters
- **CTNPORT_UI_002**: Display with customs office information
- **CTNPORT_UI_003**: Show operational status clearly

**Business Validation Rules:**
- **CTNPORT_BV_001**: Port must be operational for CTN processing
- **CTNPORT_BV_002**: Customs office must be active
- **CTNPORT_BV_003**: Port must support container operations

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique port identifier | 1 |
| 2 | Name | String - 100 | M | Port name | Port of Luanda |
| 3 | PortCode | String - 10 | M | Standard port code | LAD |
| 4 | CustomsOffice | String - 100 | O | Associated customs office | Alfândega de Luanda |
| 5 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **CTNPORT_E001**: "Invalid port parameters" (HTTP 400)
- **CTNPORT_E002**: "Port not found" (HTTP 404)
- **CTNPORT_E003**: "Port not operational" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/CTNPorts?$sort=Name&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "Name": "Port of Luanda",
    "PortCode": "LAD",
    "CustomsOffice": "Alfândega de Luanda",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "Name": "Port of Lobito",
    "PortCode": "LBT",
    "CustomsOffice": "Alfândega de Lobito",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

### 5.2 Certificate Management APIs

Certificate management APIs handle the core CTN certificate lifecycle operations, enabling the creation, retrieval, and management of CNCA certificates throughout their entire lifecycle from draft to completion.

**Note:** APIs marked as "Internal to JUL" are handled within the JUL system and do not require SINTECE implementation.

#### 5.2.1 CTN List API (Internal to JUL)

**Note:** This API is internal to the JUL system and does not require implementation by SINTECE.

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

**Sample JSON Request:**
```json
GET /api/ctns?$expand=CargoType,Status,Visum_Agent,CreatedBy,Consignee&$sort=-ModifiedOn&$top=10
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 503808,
    "CTN_Reference_Number": "170543",
    "StatusId": 2,
    "Groupage": false,
    "ParentCTNId": null,
    "CargoTypeId": 1,
    "ETD": "2025-11-12T00:00:00",
    "ETA": "2025-12-09T00:00:00",
    "BL_number": "vc568009iujh",
    "IncotermId": 2,
    "OriginCountryId": 10,
    "FinalDestinationCountryId": 4,
    "FreightPaymentTypeId": 1,
    "Total_number_containers": 1,
    "Total_number_vehicles": 0,
    "Total_Ocean_Freight": 22.0,
    "Total_Value_Of_Goods": 33.0,
    "Total_Charges": 0.0,
    "General_Total": 22.0,
    "View_CurrencyId": 1,
    "Exchange_Rate": 1.0,
    "UniqueTradeNumber": "56789098765",
    "DCNumber": "7777777",
    "DateRequestVisa": "2025-11-12T19:41:07.533",
    "IsExport": true,
    "IsImport": false,
    "CargoType": {
      "Id": 1,
      "CargoType_Desc": "CONTAINER",
      "Code": "CONTAINER"
    },
    "Status": {
      "Id": 2,
      "Status_Desc": "Submitted",
      "Code": "SUBMITTED"
    },
    "OriginCountry": {
      "Id": 10,
      "Country_Name": "Angola",
      "Country_Code": "AO"
    },
    "FinalDestinationCountry": {
      "Id": 4,
      "Country_Name": "Afghanistan",
      "Country_Code": "AF"
    },
    "CreatedOn": "2025-11-12T18:49:30.8817831+01:00",
    "ModifiedOn": "2025-11-12T19:41:07.533",
    "CreatedById": 1
  }
]
```

#### 5.2.2 CTN Details API (Internal to JUL)

**Note:** This API is internal to the JUL system and does not require implementation by SINTECE.

**Business Purpose:** Retrieves comprehensive CTN certificate details including all related entities and status information essential for certificate management and processing. Critical for viewing complete CTN records, managing certificate lifecycle, tracking status changes, and providing detailed information for customs clearance and logistics coordination.

**Endpoint:** `GET /api/ctns/{id}`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | id | Integer | M | CTN unique identifier from URL path | 503808 |
| 2 | $expand | String - 500 | O | OData expand for related entities | CargoType,ParentCTN,Status,Incoterm |

**UI Validation Rules:**
- **CTNDET_UI_001**: CTN ID must be valid integer for lookup
- **CTNDET_UI_002**: Display expanded entities in structured format
- **CTNDET_UI_003**: Show status progression and timeline

**Business Validation Rules:**
- **CTNDET_BV_001**: CTN must exist and be accessible to user
- **CTNDET_BV_002**: User must have read permission for CTN
- **CTNDET_BV_003**: Related entities must be properly expanded

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique CTN identifier | 503808 |
| 2 | CTN_Reference_Number | String - 50 | M | System generated CTN reference | 170543 |
| 3 | BL_number | String - 50 | M | Bill of lading number | vc568009iujh |
| 4 | UniqueTradeNumber | String - 50 | M | Unique trade number | 56789098765 |
| 5 | VoyageNo | String - 50 | O | Voyage number | VOY123 |
| 6 | StatusId | Integer | M | Current status identifier | 2 |
| 7 | Total_number_containers | Integer | M | Total number of containers | 1 |
| 8 | Total_Value_Of_Goods | Decimal | M | Total value of goods | 33.0 |
| 9 | CTNCost | Decimal | O | Certificate cost | 0.0 |
| 10 | ETD | DateTime | M | Estimated time of departure | 2025-11-12T00:00:00 |
| 11 | ETA | DateTime | M | Estimated time of arrival | 2025-12-09T00:00:00 |

**Error Codes:**
- **CTNDET_E001**: "CTN not found" (HTTP 404)
- **CTNDET_E002**: "Access denied to CTN" (HTTP 403)
- **CTNDET_E003**: "Invalid expand parameters" (HTTP 400)

**Sample JSON Request:**
```json
GET /api/ctns/503808?$expand=CargoType,ParentCTN,Status,Incoterm,Carrier,OriginCountry,Origin_City,FinalDestinationCountry,FreightPaymentType,View_Currency,Visum_Agent,RefusedBy,RejectedBy,Bank,Consignee&$top=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
{
  "CTN_Addresses": [],
  "CTN_Containers": [],
  "CTN_Goods": [],
  "CTN_RORO": [],
  "CTN_Tracking": [],
  "Id": 503808,
  "CTN_Reference_Number": "170543",
  "StatusId": 2,
  "Groupage": false,
  "ParentCTNId": null,
  "CargoTypeId": 1,
  "ETD": "2025-11-12T00:00:00",
  "ETA": "2025-12-09T00:00:00",
  "BL_number": "vc568009iujh",
  "IncotermId": 2,
  "OriginCountryId": 10,
  "FinalDestinationCountryId": 4,
  "FreightPaymentTypeId": 1,
  "Total_number_containers": 1,
  "Total_number_vehicles": 0,
  "Total_Ocean_Freight": 22.0,
  "Total_Value_Of_Goods": 33.0,
  "Total_Charges": 0.0,
  "General_Total": 22.0,
  "View_CurrencyId": 1,
  "Exchange_Rate": 1.0,
  "UniqueTradeNumber": "56789098765",
  "CTNCost": 0.0,
  "CommissionCNC": 0.00,
  "Status": {
    "Id": 2,
    "MultiLingualDescription": {
      "Id": 2195,
      "Translations": [
        {
          "Id": 2211,
          "LanguageISO": "en",
          "MultiLingualTextId": 2195,
          "Text": "Request Visa"
        }
      ]
    },
    "Code": "RequestVisa"
  },
  "Origin_City": {
    "Id": 262,
    "Active": true,
    "CountryId": 10,
    "Name": "Benguela"
  },
  "RefusedBy": {
    "Id": 13267,
    "Official_Name": "CNC LUANDA EXPORT SUBAGENT",
    "Email": "helpdesk@tcnt.eu",
    "Address": "LUANDA",
    "Active": true
  },
  "CreatedOn": "2025-11-12T18:58:11.807",
  "CreatedById": 13267,
  "ModifiedOn": "2025-11-12T19:32:43.48",
  "ModifiedById": 13267
}
```

#### 5.2.3 CTN Attachments API

**Business Purpose:** Manages CTN certificate attachments and supporting documents essential for compliance verification and audit trails. Critical for storing required documentation, enabling file downloads, maintaining document integrity, and ensuring complete certificate packages for customs and regulatory review.

**Endpoint:** `GET /api/ctnAttachments`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 300 | O | OData expand parameter | CreatedBy,attachment,attachmentName |
| 2 | ctn | Integer | M | CTN identifier | 503808 |
| 3 | ctnid | Integer | M | CTN identifier (alternative) | 503808 |

**UI Validation Rules:**
- **CTNATT_UI_001**: CTN ID required for attachment lookup
- **CTNATT_UI_002**: Display file types with appropriate icons
- **CTNATT_UI_003**: Show file size and upload date for management

**Business Validation Rules:**
- **CTNATT_BV_001**: CTN must exist and be accessible
- **CTNATT_BV_002**: File size must not exceed system limits
- **CTNATT_BV_003**: File types must be approved formats

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Attachment record ID | 12345 |
| 2 | CTNId | Integer | M | Related CTN ID | 503808 |
| 3 | FileName | String - 255 | M | Original file name | bill_of_lading.pdf |
| 4 | FileSize | Integer | M | File size in bytes | 2048576 |
| 5 | AttachmentTypeId | Integer | M | Type of attachment | 1 |
| 6 | AttachmentTypeName | String - 100 | O | Attachment type description | Bill of Lading |
| 7 | UploadDate | DateTime | M | File upload timestamp | 2023-12-15T10:30:00Z |
| 8 | CreatedById | Integer | M | User who uploaded file | 13345 |

**Error Codes:**
- **CTNATT_E001**: "Invalid CTN ID" (HTTP 400)
- **CTNATT_E002**: "No attachments found" (HTTP 404)
- **CTNATT_E003**: "File access denied" (HTTP 403)

**Sample JSON Request:**
```json
GET /api/ctnAttachments?$expand=CreatedBy,attachment,attachmentName&ctnid=503808
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 12345,
    "CTNId": 503808,
    "FileName": "bill_of_lading.pdf",
    "FileSize": 2048576,
    "AttachmentTypeId": 1,
    "AttachmentTypeName": "Bill of Lading",
    "UploadDate": "2023-12-15T10:30:00Z",
    "CreatedById": 13345,
    "CreatedBy": {
      "Id": 13345,
      "UserName": "CNCEXPORTER",
      "Email": "exporter@company.com"
    }
  }
]
```

#### 5.2.4 CTN Creation API (Certificate Submission)

**Note:** This unified API consolidates what was previously multiple separate operations (creation, addresses, goods, containers, tracking, attachments) into one comprehensive submission. JUL will handle all data processing internally and save as draft, eliminating the need for multiple API calls from SINTECE.

**Business Purpose:** Creates new CTN certificate records with complete information for CNCA certificate applications in a single comprehensive request. This unified API combines what was previously multiple separate operations (creation, addresses, goods, containers, tracking, attachments) into one streamlined submission. Critical for submitting complete certificate requests, establishing certificate records with all required data, validating comprehensive submission data, and enabling the certificate approval workflow efficiently.

**Endpoint:** `POST /api/ctns`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| **Core CTN Information** |
| 1 | Id | Integer | O | CTN identifier (null for new) | null |
| 2 | CTN_Reference_Number | String - 50 | O | System generated reference | "" |
| 3 | StatusId | Integer | M | Status identifier (1=Created) | 1 |
| 4 | Groupage | Boolean | O | Groupage indicator | false |
| 5 | ParentCTNId | Integer | O | Parent CTN identifier | null |
| 6 | CargoTypeId | Integer | M | Cargo type identifier | 1 |
| 7 | ETD | DateTime | O | Estimated time departure | null |
| 8 | ETA | DateTime | O | Estimated time arrival | null |
| 9 | BL_number | String - 50 | M | Bill of lading number | vc568009iujh |
| 10 | IncotermId | Integer | M | Incoterm identifier | 2 |
| 11 | OriginCountryId | Integer | M | Origin country identifier | 10 |
| 12 | FinalDestinationCountryId | Integer | M | Destination country identifier | 4 |
| 13 | FreightPaymentTypeId | Integer | M | Freight payment type identifier | 1 |
| 14 | Total_number_containers | Integer | O | Total containers count | 0 |
| 15 | Total_number_vehicles | Integer | O | Total vehicles count | 0 |
| 16 | Total_Ocean_Freight | Decimal | O | Total ocean freight value | 0 |
| 17 | Total_Value_Of_Goods | Decimal | O | Total goods value | 0 |
| 18 | Total_Charges | Decimal | O | Total charges amount | 0 |
| 19 | General_Total | Decimal | O | General total amount | 0 |
| 20 | View_CurrencyId | Integer | M | Currency identifier | 1 |
| 21 | Exchange_Rate | Decimal | O | Exchange rate | 1 |
| 22 | Visum_Location | String - 100 | O | Visa location | null |
| 23 | Visum_Reference_number | String - 50 | O | Visa reference number | null |
| 24 | Visum_Cost | Decimal | O | Visa cost | 1 |
| 25 | Visum_Date | DateTime | O | Visa date | null |
| 26 | Visum_AgentId | Integer | O | Visa agent identifier | null |
| 27 | Invoicer_to_agent | String - 100 | O | Invoicing agent | null |
| 28 | VoyageNo | String - 50 | O | Voyage number | null |
| 29 | RegularisationCTN | Boolean | O | Regularisation flag | false |
| 30 | IsExport | Boolean | M | Export indicator | true |
| 31 | IsImport | Boolean | O | Import indicator | false |
| 32 | Origin_CityId | Integer | M | Origin city identifier | 262 |
| 33 | Final_Destination_CityId | Integer | O | Final destination city | null |
| 34 | CarrierId | Integer | M | Carrier identifier | 789 |
| 35 | UniqueTradeNumber | String - 50 | M | Unique trade number | 56789098765 |
| 36 | Commission | Decimal | O | Commission amount | 0 |
| 37 | CommissionCNC | Decimal | O | CNC commission | 0 |
| 38 | CTNExchangeRate | Decimal | O | CTN exchange rate | null |
| 39 | MarkedForUpdate | Boolean | O | Update marker | false |
| 40 | ReceivedByGumar | Boolean | O | Gumar receipt flag | false |
| 41 | ErrorSendToGumar | Boolean | O | Gumar error flag | false |
| 42 | BankId | Integer | O | Bank identifier | 2 |
| 43 | ConsigneeId | Integer | M | Consignee identifier | 43214 |
| 44 | ReExport | Boolean | O | Re-export indicator | false |
| 45 | DCNumber | String - 50 | O | Document control number | 7777777 |
| 46 | CreatedOn | DateTime | O | Creation timestamp | 2025-11-12T18:49:30.88Z |
| 47 | CreatedById | Integer | O | Creator identifier | 1 |
| **Address Information** |
| 48 | CTN_Addresses | Array | O | Array of address objects for shipper, consignee, forwarder, notify party | [...] |
| 48.1 | - Id | Integer | O | Address identifier (null for new) | null |
| 48.2 | - QryAddressTypeId | Integer | M | Address type (1=Shipper, 2=Consignee, 3=Forwarder, 4=Notify) | 2 |
| 48.3 | - Name | String - 200 | M | Company/Person name | M.A.C.S AS.TEC.N. E IND |
| 48.4 | - Address | String - 500 | M | Physical address | maculusso rua comandate |
| 48.5 | - City | String - 100 | M | City name | kwenhan |
| 48.6 | - CountryId | Integer | M | Country identifier | 10 |
| 48.7 | - Email | String - 100 | O | Email address | contact@company.com |
| 48.8 | - Telephone | String - 50 | M | Phone number | 923798669 |
| 48.9 | - NIFNumber | String - 50 | M | Tax identification number | 0000000458608 |
| **Goods Information** |
| 49 | CTN_Goods | Array | O | Array of goods/cargo objects | [...] |
| 49.1 | - Id | Integer | O | Goods identifier (null for new) | null |
| 49.2 | - GoodsClassificationId | Integer | M | Goods classification identifier | 16882 |
| 49.3 | - IMOId | Integer | M | IMO hazardous code identifier | 2 |
| 49.4 | - CargoTypeId | Integer | M | Cargo type identifier | 1 |
| 49.5 | - DescriptionGoods | String - 500 | M | Goods description | test |
| 49.6 | - GrossWeightKG | Decimal | M | Gross weight in kg | 10.0 |
| 49.7 | - VolumeCBM | Decimal | M | Volume in cubic meters | 11.0 |
| 49.8 | - OceanFreight | Decimal | M | Ocean freight cost | 22.0 |
| 49.9 | - ValueOfGoods | Decimal | M | Value of goods | 33.0 |
| 49.10 | - NumberOfPackages | Integer | M | Number of packages | 3 |
| **Container Information** |
| 50 | CTN_Containers | Array | O | Array of container objects | [...] |
| 50.1 | - Id | Integer | O | Container identifier (null for new) | null |
| 50.2 | - ContainerTypeId | Integer | M | Container type identifier | 31 |
| 50.3 | - Number_of_Containers | Integer | M | Number of containers | 1 |
| 50.4 | - ContainerNumbers | String - 100 | M | Container number(s) | MSCU1234567 |
| 50.5 | - SealNumbers | String - 100 | M | Seal number(s) | 23234 |
| 50.6 | - Groupage | Boolean | O | Groupage indicator | false |
| 50.7 | - IsEmpty | Boolean | O | Empty container indicator | false |
| 50.8 | - OwnedByShipper | Boolean | O | Shipper owned indicator | false |
| **Transport/Tracking Information** |
| 51 | CTN_Tracking | Array | O | Array of transport route objects | [...] |
| 51.1 | - Id | Integer | O | Tracking identifier | null |
| 51.2 | - SourceCountryId | Integer | M | Source country identifier | 10 |
| 51.3 | - SourcePortId | Integer | M | Source port identifier | 80 |
| 51.4 | - ETD | DateTime | M | Estimated time departure | 2025-11-12T00:00:00.000Z |
| 51.5 | - TransportTypeId | Integer | M | Transport type identifier | 1 |
| 51.6 | - VoyageNumber | String - 50 | M | Voyage number | 546894 |
| 51.7 | - CarrierId | Integer | M | Carrier identifier | 789 |
| 51.8 | - VesselId | Integer | M | Vessel identifier | 5163 |
| 51.9 | - DestinationCountryId | Integer | M | Destination country identifier | 4 |
| 51.10 | - DestinationPortId | Integer | M | Destination port identifier | 35 |
| 51.11 | - ETA | DateTime | M | Estimated time arrival | 2025-12-09T00:00:00.000Z |
| 51.12 | - Sequence | Integer | M | Sequence number | 1 |
| **RORO Information** |
| 52 | CTN_RORO | Array | O | Array of RORO cargo objects (for roll-on/roll-off cargo) | [...] |
| **Attachment Information** |
| 53 | CTN_Attachments | Array | O | Array of document attachment objects | [...] |
| 53.1 | - Id | Integer | O | Attachment identifier (null for new) | null |
| 53.2 | - AttachmentGuid | String - 50 | M | File upload GUID from fileupload API | 0da7461c-2155-4d20-a695-6b7463367327 |
| 53.3 | - NameId | Integer | M | Attachment name type identifier | 4 |

**UI Validation Rules:**
- **CTNCRE_UI_001**: All mandatory fields must be completed for core CTN information
- **CTNCRE_UI_002**: BL number must be unique and valid format
- **CTNCRE_UI_003**: Trade number must follow required pattern
- **CTNCRE_UI_004**: At least one address must be provided (typically consignee)
- **CTNCRE_UI_005**: All address fields must be complete when address is provided
- **CTNCRE_UI_006**: At least one goods entry must be provided for the shipment
- **CTNCRE_UI_007**: Container information must match declared container count
- **CTNCRE_UI_008**: Transport route must have valid origin and destination
- **CTNCRE_UI_009**: Attachment GUIDs must be valid from fileupload API

**Business Validation Rules:**
- **CTNCRE_BV_001**: BL number must not exist in system
- **CTNCRE_BV_002**: All referenced entities (countries, ports, carriers, etc.) must be valid and active
- **CTNCRE_BV_003**: User must have permission to create CTNs
- **CTNCRE_BV_004**: NIFNumber validation must pass for Angola addresses
- **CTNCRE_BV_005**: Total values must match sum of individual goods values
- **CTNCRE_BV_006**: Container count must match actual container entries
- **CTNCRE_BV_007**: Transport sequence must be logical (ETD before ETA)
- **CTNCRE_BV_008**: Required attachments must be present based on trade type

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | New CTN identifier | 503808 |
| 2 | CTN_Reference_Number | String - 50 | M | System generated reference | AO-CNT-503808-2025 |
| 3 | StatusId | Integer | M | Initial status (1=Draft) | 1 |
| 4 | BL_number | String - 50 | M | Confirmed BL number | vc568009iujh |
| 5 | UniqueTradeNumber | String - 50 | M | Confirmed trade number | 56789098765 |
| 6 | CreatedOn | DateTime | M | Creation timestamp | 2025-11-14T10:30:00Z |
| 7 | CreatedById | Integer | M | Creator user identifier | 1 |
| 8 | AddressesCreated | Integer | M | Number of addresses created | 2 |
| 9 | GoodsCreated | Integer | M | Number of goods entries created | 1 |
| 10 | ContainersCreated | Integer | M | Number of container entries created | 1 |
| 11 | TrackingCreated | Integer | M | Number of tracking entries created | 1 |
| 12 | AttachmentsCreated | Integer | M | Number of attachments created | 2 |

**Error Codes:**
- **CTNCRE_E001**: "BL number already exists" (HTTP 409)
- **CTNCRE_E002**: "Invalid reference data" (HTTP 400)
- **CTNCRE_E003**: "Insufficient permissions" (HTTP 403)
- **CTNCRE_E004**: "Invalid address information" (HTTP 422)
- **CTNCRE_E005**: "Invalid goods information" (HTTP 422)
- **CTNCRE_E006**: "Invalid container information" (HTTP 422)
- **CTNCRE_E007**: "Invalid tracking information" (HTTP 422)
- **CTNCRE_E008**: "Invalid attachment information" (HTTP 422)
- **CTNCRE_E009**: "NIF validation failed" (HTTP 422)

**Sample JSON Request:**
```json
POST /api/ctns
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

{
  "Id": null,
  "CTN_Reference_Number": "",
  "StatusId": 1,
  "Groupage": false,
  "ParentCTNId": null,
  "CargoTypeId": 1,
  "ETD": null,
  "ETA": null,
  "BL_number": "vc568009iujh",
  "IncotermId": 2,
  "OriginCountryId": 10,
  "FinalDestinationCountryId": 4,
  "FreightPaymentTypeId": 1,
  "Total_number_containers": 1,
  "Total_number_vehicles": 0,
  "Total_Ocean_Freight": 22.0,
  "Total_Value_Of_Goods": 33.0,
  "Total_Charges": 55.0,
  "General_Total": 55.0,
  "View_CurrencyId": 1,
  "Exchange_Rate": 1,
  "Visum_Location": null,
  "Visum_Reference_number": null,
  "Visum_Cost": 1,
  "Visum_Date": null,
  "Visum_AgentId": null,
  "Invoicer_to_agent": null,
  "VoyageNo": "546894",
  "RegularisationCTN": false,
  "IsExport": true,
  "IsImport": false,
  "Origin_CityId": 262,
  "Final_Destination_CityId": null,
  "CarrierId": 789,
  "UniqueTradeNumber": "56789098765",
  "Commission": 0,
  "CommissionCNC": 0,
  "CTNExchangeRate": null,
  "MarkedForUpdate": false,
  "ReceivedByGumar": false,
  "ErrorSendToGumar": false,
  "BankId": 2,
  "ConsigneeId": 43214,
  "ReExport": false,
  "DCNumber": "7777777",
  "CreatedOn": "2025-11-14T10:30:00Z",
  "CreatedById": 1,
  "CTN_Addresses": [
    {
      "Id": null,
      "QryAddressTypeId": 1,
      "Name": "EXPORTER COMPANY LTD",
      "Address": "123 Export Street",
      "City": "Export City", 
      "CountryId": 10,
      "Email": "exporter@company.com",
      "Telephone": "244123456789",
      "NIFNumber": "1234567890"
    },
    {
      "Id": null,
      "QryAddressTypeId": 2,
      "Name": "M.A.C.S AS.TEC.N. E IND",
      "Address": "maculusso rua comandate",
      "City": "kwenhan",
      "CountryId": 4,
      "Email": "contact@company.com",
      "Telephone": "923798669",
      "NIFNumber": "0000000458608"
    }
  ],
  "CTN_Goods": [
    {
      "Id": null,
      "GoodsClassificationId": 16882,
      "IMOId": 2,
      "CargoTypeId": 1,
      "DescriptionGoods": "Electronic Components and Parts",
      "GrossWeightKG": 1000.0,
      "VolumeCBM": 11.0,
      "OceanFreight": 22.0,
      "ValueOfGoods": 33.0,
      "NumberOfPackages": 3
    }
  ],
  "CTN_Containers": [
    {
      "Id": null,
      "ContainerTypeId": 31,
      "Number_of_Containers": 1,
      "ContainerNumbers": "MSCU1234567",
      "SealNumbers": "23234",
      "Groupage": false,
      "IsEmpty": false,
      "OwnedByShipper": false
    }
  ],
  "CTN_Tracking": [
    {
      "Id": null,
      "SourceCountryId": 10,
      "SourcePortId": 80,
      "ETD": "2025-11-15T00:00:00.000Z",
      "TransportTypeId": 1,
      "VoyageNumber": "546894",
      "CarrierId": 789,
      "VesselId": 5163,
      "DestinationCountryId": 4,
      "DestinationPortId": 35,
      "ETA": "2025-12-09T00:00:00.000Z",
      "Sequence": 1
    }
  ],
  "CTN_RORO": [],
  "CTN_Attachments": [
    {
      "Id": null,
      "AttachmentGuid": "0da7461c-2155-4d20-a695-6b7463367327",
      "NameId": 4
    },
    {
      "Id": null,
      "AttachmentGuid": "1eb8572d-3266-5e31-b7a6-7c8574468438",
      "NameId": 1
    }
  ]
}
```

**Sample JSON Response:**
```json
{
  "Id": 503808,
  "CTN_Reference_Number": "AO-CNT-503808-2025",
  "StatusId": 1,
  "BL_number": "vc568009iujh",
  "UniqueTradeNumber": "56789098765",
  "CreatedOn": "2025-11-14T10:30:00Z",
  "CreatedById": 1,
  "AddressesCreated": 2,
  "GoodsCreated": 1,
  "ContainersCreated": 1,
  "TrackingCreated": 1,
  "AttachmentsCreated": 2,
  "Message": "CTN certificate created successfully with all associated data"
}
```

#### 5.2.5 Request Visa API (Certificate Issuance Submission)

**Business Purpose:** Submits completed CTN certificates for approval and visa issuance essential for finalizing the certificate approval process. Critical for triggering certificate review, validating completeness requirements, initiating approval workflow, and moving certificates from draft to approval status.

**Endpoint:** `POST /api/ctns/actions/requestvisa/{id}`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | id | Integer | M | CTN identifier from URL path | 503808 |
| 2 | Content-Length | Integer | M | Request body length (0 for this action) | 0 |

**Pre-submission Validation Requirements:**
- **Shipper Address**: Complete shipper address information required
- **Forwarder Address**: Complete forwarder address information required  
- **Attachments**: At least 1 attachment must be uploaded
- **CTN Data**: All mandatory CTN fields must be completed

**UI Validation Rules:**
- **REQVISA_UI_001**: CTN must be in "Edited" status to request visa
- **REQVISA_UI_002**: Display validation errors clearly to user
- **REQVISA_UI_003**: Confirm all requirements before submission

**Business Validation Rules:**
- **REQVISA_BV_001**: CTN must have complete address information
- **REQVISA_BV_002**: Required attachments must be uploaded
- **REQVISA_BV_003**: CTN must pass all business validations

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | rowsAffected | Integer | M | Number of affected records | -1 |
| 2 | error | String - 1000 | O | Validation error messages | "" |
| 3 | newCtnId | Integer | M | CTN identifier (0 for existing) | 0 |

**Error Codes:**
- **REQVISA_E001**: "Missing or incomplete Shipper Address" (HTTP 400)
- **REQVISA_E002**: "Missing or incomplete Forwarder Address" (HTTP 400)
- **REQVISA_E003**: "At least 1 attachment must be uploaded" (HTTP 400)
- **REQVISA_E004**: "CTN not found or not accessible" (HTTP 404)

**Sample JSON Request:**
```json
POST /api/ctns/actions/requestvisa/503808
Content-Length: 0
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
{
  "rowsAffected": -1,
  "error": "",
  "newCtnId": 0
}
```

#### 5.2.5.1 Document Upload API for Request Visa

**Business Purpose:** Enables SINTECE to upload documents specifically for the Request Visa process, providing document management capabilities separate from the general file upload API. Critical for visa application documentation, compliance verification, and regulatory submission requirements.

**Endpoint:** `POST /api/ctns/{ctnId}/documents/upload`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | ctnId | Integer | M | CTN identifier from URL path | 503808 |
| 2 | file | Binary | M | Document file (multipart/form-data) | [binary file data] |
| 3 | documentType | String - 50 | M | Type of document being uploaded | BILL_OF_LADING |
| 4 | documentName | String - 256 | M | Document name/title | Bill of Lading Original |
| 5 | description | String - 500 | O | Document description | Original shipping document for visa application |
| 6 | isRequired | Boolean | M | Whether document is mandatory | true |

**UI Validation Rules:**
- **DOCUP_UI_001**: File size must not exceed 25MB for visa documents
- **DOCUP_UI_002**: Document type must be from approved list
- **DOCUP_UI_003**: Document name required, max 256 characters
- **DOCUP_UI_004**: File types allowed: PDF, JPG, PNG, DOC, DOCX, XLS, XLSX

**Business Validation Rules:**
- **DOCUP_BV_001**: CTN must exist and be accessible
- **DOCUP_BV_002**: Document type must be valid for visa application
- **DOCUP_BV_003**: User must have permission to upload documents
- **DOCUP_BV_004**: Duplicate documents should be detected

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | documentId | String (UUID) | M | Unique document identifier | f47ac10b-58cc-4372-a567-0e02b2c3d479 |
| 2 | documentName | String - 256 | M | Uploaded document name | Bill of Lading Original |
| 3 | fileName | String - 256 | M | Original file name | BOL_ABC123.pdf |
| 4 | fileSize | Integer | M | File size in bytes | 1048576 |
| 5 | mimeType | String - 100 | M | File MIME type | application/pdf |
| 6 | downloadUrl | String - 500 | M | URL to download document | /api/ctns/503808/documents/f47ac10b-58cc-4372-a567-0e02b2c3d479/download |
| 7 | uploadDate | DateTime | M | Upload timestamp | 2025-11-14T15:30:00Z |
| 8 | documentType | String - 50 | M | Document type | BILL_OF_LADING |
| 9 | status | String - 20 | M | Document status | UPLOADED |
| 10 | ctnId | Integer | M | Associated CTN ID | 503808 |

**Error Codes:**
- **DOCUP_E001**: "CTN not found" (HTTP 404)
- **DOCUP_E002**: "Invalid document type" (HTTP 400)
- **DOCUP_E003**: "File size exceeds limit" (HTTP 413)
- **DOCUP_E004**: "Invalid file type" (HTTP 415)
- **DOCUP_E005**: "Document upload failed" (HTTP 500)

**Sample Multipart Request:**
```
POST /api/ctns/503808/documents/upload
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="BOL_ABC123.pdf"
Content-Type: application/pdf

[Binary PDF file content]
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="documentType"

BILL_OF_LADING
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="documentName"

Bill of Lading Original
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="description"

Original shipping document for visa application
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="isRequired"

true
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

**Sample JSON Response:**
```json
{
  "documentId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "documentName": "Bill of Lading Original",
  "fileName": "BOL_ABC123.pdf",
  "fileSize": 1048576,
  "mimeType": "application/pdf",
  "downloadUrl": "/api/ctns/503808/documents/f47ac10b-58cc-4372-a567-0e02b2c3d479/download",
  "uploadDate": "2025-11-14T15:30:00Z",
  "documentType": "BILL_OF_LADING",
  "status": "UPLOADED",
  "ctnId": 503808
}
```

#### 5.2.5.2 Document Delete API for Request Visa

**Business Purpose:** Allows SINTECE to delete uploaded documents from CTN certificates before visa submission. Critical for document management, correcting upload mistakes, replacing outdated documents, and maintaining clean documentation sets.

**Endpoint:** `DELETE /api/ctns/{ctnId}/documents/{documentId}`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | ctnId | Integer | M | CTN identifier from URL path | 503808 |
| 2 | documentId | String (UUID) | M | Document identifier from URL path | f47ac10b-58cc-4372-a567-0e02b2c3d479 |
| 3 | reason | String - 200 | O | Deletion reason (in request body) | Incorrect document uploaded |

**UI Validation Rules:**
- **DOCDEL_UI_001**: Confirm deletion with user before proceeding
- **DOCDEL_UI_002**: Display document details before deletion
- **DOCDEL_UI_003**: Reason for deletion optional but recommended

**Business Validation Rules:**
- **DOCDEL_BV_001**: CTN must exist and be accessible
- **DOCDEL_BV_002**: Document must exist and belong to CTN
- **DOCDEL_BV_003**: User must have permission to delete documents
- **DOCDEL_BV_004**: Cannot delete documents after visa submission
- **DOCDEL_BV_005**: Cannot delete required documents unless replacing

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | success | Boolean | M | Deletion success indicator | true |
| 2 | documentId | String (UUID) | M | Deleted document identifier | f47ac10b-58cc-4372-a567-0e02b2c3d479 |
| 3 | documentName | String - 256 | M | Name of deleted document | Bill of Lading Original |
| 4 | deletedAt | DateTime | M | Deletion timestamp | 2025-11-14T16:45:00Z |
| 5 | deletedBy | Integer | M | User who deleted document | 13345 |
| 6 | message | String - 200 | M | Confirmation message | Document successfully deleted |

**Error Codes:**
- **DOCDEL_E001**: "CTN not found" (HTTP 404)
- **DOCDEL_E002**: "Document not found" (HTTP 404)
- **DOCDEL_E003**: "Cannot delete after visa submission" (HTTP 409)
- **DOCDEL_E004**: "Cannot delete required document" (HTTP 409)
- **DOCDEL_E005**: "Insufficient permissions" (HTTP 403)

**Sample JSON Request:**
```json
DELETE /api/ctns/503808/documents/f47ac10b-58cc-4372-a567-0e02b2c3d479
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

{
  "reason": "Incorrect document uploaded, need to replace with updated version"
}
```

**Sample JSON Response:**
```json
{
  "success": true,
  "documentId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "documentName": "Bill of Lading Original",
  "deletedAt": "2025-11-14T16:45:00Z",
  "deletedBy": 13345,
  "message": "Document successfully deleted"
}
```

#### 5.2.6 NIF Validation API (Angola Tax Registration Number)

**Business Purpose:** Validates NIF (Número de Identificação Fiscal) - Angola Tax Registration Number for importers, exporters, and consignees. Critical for ensuring tax compliance, preventing fraud, validating business entities, and meeting ARCCLA regulatory requirements for CNCA certificate processing.

**Endpoint:** `POST /api/validation/nif`

**Request Elements:**

| S. No | Attributes | Data Type - Length | Condition (M/O) | Format/Derivation logic for fields | Data Example |
|-------|------------|-------------------|-----------------|-----------------------------------|--------------|
| 1 | nifNumber | String - 14 | M | Angola Tax Registration Number (9-14 digits) | 5000000000 |
| 2 | entityName | String - 200 | O | Name of entity for cross-validation | ABC Trading Company |
| 3 | entityType | String - 20 | O | Type of entity (IMPORTER, EXPORTER, CONSIGNEE) | IMPORTER |
| 4 | validationType | String - 20 | O | Validation type (STANDARD, ENHANCED) | STANDARD |

**UI Validation Rules:**
- **NIF_UI_001**: NIF number mandatory, 9-14 alphanumeric characters
- **NIF_UI_002**: Entity name optional, max 200 characters
- **NIF_UI_003**: Entity type from predefined list only
- **NIF_UI_004**: Remove leading/trailing spaces from NIF

**Business Validation Rules:**
- **NIF_BV_001**: NIF must follow Angola tax authority format
- **NIF_BV_002**: NIF must be active and valid in ARCCLA system
- **NIF_BV_003**: Entity name must match registered name if provided
- **NIF_BV_004**: Suspended or blacklisted NIFs cannot be used
- **NIF_BV_005**: NIF entity type must match certificate type (import/export)

**Response Elements:**

| S. No | Attributes | Data Type - Length | Condition (M/O) | Format/Derivation logic for fields | Data Example |
|-------|------------|-------------------|-----------------|-----------------------------------|--------------|
| 1 | validationStatus | String - 20 | M | Validation result (VALID, INVALID, SUSPENDED) | VALID |
| 2 | nifNumber | String - 14 | M | Validated NIF number | 5000000000 |
| 3 | registeredName | String - 200 | O | Official registered name from tax authority | ABC Trading Company Lda |
| 4 | entityStatus | String - 20 | O | Entity status (ACTIVE, INACTIVE, SUSPENDED) | ACTIVE |
| 5 | registrationDate | Date | O | NIF registration date | 2020-05-15 |
| 6 | validationCode | String - 10 | M | Validation result code | NIF_VALID |
| 7 | validationMessage | String - 500 | M | Detailed validation message | NIF is valid and active |
| 8 | errorDetails | Array | O | Array of validation errors if any | [] |

**Error Codes:**
- **NIF_E001**: "Invalid NIF format" (HTTP 400)
- **NIF_E002**: "NIF not found in ARCCLA system" (HTTP 404)
- **NIF_E003**: "NIF suspended or blacklisted" (HTTP 403)
- **NIF_E004**: "Entity name mismatch" (HTTP 400)
- **NIF_E005**: "NIF validation service unavailable" (HTTP 503)
- **NIF_E006**: "Invalid entity type for certificate" (HTTP 400)

**Sample JSON Request:**
```json
POST /api/validation/nif
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

{
  "nifNumber": "5000000000",
  "entityName": "ABC Trading Company",
  "entityType": "IMPORTER",
  "validationType": "STANDARD"
}
```

**Sample JSON Response (Success):**
```json
{
  "validationStatus": "VALID",
  "nifNumber": "5000000000",
  "registeredName": "ABC Trading Company Lda",
  "entityStatus": "ACTIVE",
  "registrationDate": "2020-05-15",
  "validationCode": "NIF_VALID",
  "validationMessage": "NIF is valid and active in ARCCLA system",
  "errorDetails": []
}
```

**Sample JSON Response (Error):**
```json
{
  "validationStatus": "INVALID",
  "nifNumber": "5000000000",
  "registeredName": null,
  "entityStatus": null,
  "registrationDate": null,
  "validationCode": "NIF_NOT_FOUND",
  "validationMessage": "NIF not found in ARCCLA tax registration system",
  "errorDetails": [
    {
      "field": "nifNumber",
      "code": "NIF_E002",
      "message": "The provided NIF does not exist in the Angola tax authority database"
    }
  ]
}
```

**Integration Notes:**
- NIF validation should be performed before CTN certificate creation
- Cached validation results valid for 24 hours
- Real-time validation with ARCCLA tax authority system
- Supports bulk NIF validation (future enhancement)

#### 5.2.7 Invoice Download API

**Important Note on Invoice Applicability:**
> **CRITICAL:** Invoices are ONLY applicable for IMPORT profiles. Export profiles do NOT require invoice generation or download functionality. The invoice download API should only be called for import certificate types.

**Business Purpose:** Enables download of CNCA certificate invoices after certificate completion for import profiles only. Critical for financial record-keeping, customs documentation, and audit trail maintenance. **Not applicable for export certificates.**

**Endpoint:** `GET /api/invoices/{invoiceId}/download`

**Request Elements:**

| S. No | Attributes | Data Type - Length | Condition (M/O) | Format/Derivation logic for fields | Data Example |
|-------|------------|-------------------|-----------------|-----------------------------------|--------------|
| 1 | invoiceId | String - 50 | M | Unique invoice identifier from certificate | INV-2024-001234 |
| 2 | format | String - 10 | O | Invoice format (PDF, XML) - default PDF | PDF |
| 3 | certificateType | String - 20 | O | Certificate type for validation (IMPORT/EXPORT) | IMPORT |

**Path Parameters:**
- `invoiceId`: Unique invoice identifier (mandatory)

**Query Parameters:**
- `format`: Desired file format (optional, defaults to PDF)

**UI Validation Rules:**
- **INV_UI_001**: Invoice ID mandatory, alphanumeric with hyphens
- **INV_UI_002**: Format must be PDF or XML only
- **INV_UI_003**: Download only available for import profiles
- **INV_UI_004**: Display warning for export certificate requests

**Business Validation Rules:**
- **INV_BV_001**: Invoice must exist and be associated with authenticated user
- **INV_BV_002**: Certificate must be in "Approved" or "Issued" status
- **INV_BV_003**: User must have permission to access invoice
- **INV_BV_004**: Invoice download only allowed for IMPORT certificates
- **INV_BV_005**: Export certificates should not generate or download invoices

**Response Elements:**

| S. No | Attributes | Data Type - Length | Condition (M/O) | Format/Derivation logic for fields | Data Example |
|-------|------------|-------------------|-----------------|-----------------------------------|--------------|
| 1 | fileName | String - 100 | M | Generated file name | invoice_INV-2024-001234.pdf |
| 2 | fileSize | Number | M | File size in bytes | 245678 |
| 3 | contentType | String - 50 | M | MIME type of file | application/pdf |
| 4 | downloadUrl | String - 500 | O | Direct download URL (if applicable) | https://jul.adports.ae/downloads/... |
| 5 | invoiceData | Binary | M | Invoice file binary content (Base64 encoded) | [binary data] |
| 6 | generatedDate | Date | M | Invoice generation timestamp | 2025-11-14T10:30:00Z |

**Error Codes:**
- **INV_E001**: "Invoice not found" (HTTP 404)
- **INV_E002**: "Certificate not completed" (HTTP 400)
- **INV_E003**: "Access denied" (HTTP 403)
- **INV_E004**: "Invalid invoice format requested" (HTTP 400)
- **INV_E005**: "Export certificates do not support invoices" (HTTP 400)
- **INV_E006**: "Invoice generation in progress" (HTTP 202)

**Sample API Request:**
```http
GET /api/invoices/INV-2024-001234/download?format=PDF
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
{
  "fileName": "invoice_INV-2024-001234.pdf",
  "fileSize": 245678,
  "contentType": "application/pdf",
  "downloadUrl": "https://jul.adports.ae/api/files/download/abc123xyz",
  "generatedDate": "2025-11-14T10:30:00Z",
  "invoiceData": "JVBERi0xLjQKJeLjz9MKMSAwIG9iago8PC9UeXBlL0NhdGFsb2cvUGFnZXMgMiAwIFI+..."
}
```

**Invoice Applicability Rules:**

| Certificate Type | Invoice Required | Invoice Download Available | Notes |
|-----------------|------------------|---------------------------|-------|
| **IMPORT** | ✅ Yes | ✅ Yes | Invoice generated after approval |
| **EXPORT** | ❌ No | ❌ No | Export certificates do not require invoices |

**Important Implementation Notes:**
1. **Pre-Download Validation:** Always validate certificate type before allowing invoice download
2. **UI Display:** Do not show invoice download button/option for export certificates
3. **Error Handling:** Return specific error (INV_E005) when export certificate attempts invoice download
4. **Business Logic:** Invoice generation workflow should only trigger for import certificates
5. **Audit Trail:** Log all invoice download attempts with certificate type information

**Integration Workflow:**
1. Certificate approved by ARCCLA
2. For IMPORT certificates: Invoice generated automatically
3. Certificate becomes available for download
4. User downloads invoice via API or UI
5. For EXPORT certificates: Skip invoice generation entirely

---

### 5.3 CTN Related Entity APIs

CTN Related Entity APIs manage the specific entities and components that are directly associated with CTN certificate processing, including consignee information, attachment management, and tracking data.

#### 5.3.1 Consignees API

**Business Purpose:** Manages consignee information essential for CTN certificate processing and customs compliance. Critical for identifying cargo recipients, validating company details, ensuring proper documentation, and enabling accurate certificate issuance with verified consignee data.

**Endpoint:** `GET /api/Consignees`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | NIFNumber |
| 2 | NIFNumber | String - 50 | O | Filter by NIF number | 123456789 |
| 3 | CompanyName | String - 200 | O | Filter by company name | ACME |
| 4 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **CONSIGNEE_UI_001**: NIF number format validation (9-14 digits)
- **CONSIGNEE_UI_002**: Company name minimum 3 characters
- **CONSIGNEE_UI_003**: Display with address for identification

**Business Validation Rules:**
- **CONSIGNEE_BV_001**: NIF number must be unique and valid
- **CONSIGNEE_BV_002**: Company must be registered and active
- **CONSIGNEE_BV_003**: Consignee must have valid import license

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique consignee identifier | 1 |
| 2 | NIFNumber | String - 50 | M | Tax identification number | 123456789 |
| 3 | CompanyName | String - 200 | M | Company/consignee name | ACME Import Company |
| 4 | ContactEmail | String - 100 | O | Contact email address | contact@acme.ao |
| 5 | Address | String - 500 | O | Company address | Rua da Independencia 123 |
| 6 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **CONSIGNEE_E001**: "Invalid NIF number format" (HTTP 400)
- **CONSIGNEE_E002**: "Consignee not found" (HTTP 404)
- **CONSIGNEE_E003**: "Consignee not authorized for import" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/Consignees?$sort=NIFNumber&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "NIFNumber": "123456789",
    "CompanyName": "ACME Import Company",
    "ContactEmail": "contact@acme.ao",
    "Address": "Rua da Independencia 123, Luanda",
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.3.2 Attachment Names API

**Business Purpose:** Manages standardized attachment type classifications essential for CTN document management and compliance verification. Critical for organizing certificate documents, ensuring complete documentation, and maintaining audit trails for regulatory compliance.

**Endpoint:** `GET /api/AttachmentNames`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $sort | String - 100 | O | OData sort parameter | AttachmentName_Desc |
| 2 | AttachmentName_Desc | String - 200 | O | Filter by attachment name | Bill of Lading |
| 3 | DocumentType | String - 50 | O | Filter by document type | Shipping |
| 4 | active | Boolean | O | Filter active records only | 1 |

**UI Validation Rules:**
- **ATTACHMENT_UI_001**: Attachment name filter minimum 3 characters
- **ATTACHMENT_UI_002**: Group by document type for organization
- **ATTACHMENT_UI_003**: Display with required/optional indicator

**Business Validation Rules:**
- **ATTACHMENT_BV_001**: Some attachment types are mandatory
- **ATTACHMENT_BV_002**: File format restrictions apply by type
- **ATTACHMENT_BV_003**: Attachment size limits vary by type

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | Id | Integer | M | Unique attachment type identifier | 1 |
| 2 | AttachmentName_Desc | String - 200 | M | Attachment type description | Bill of Lading |
| 3 | DocumentType | String - 50 | O | Document category | Shipping |
| 4 | IsRequired | Boolean | O | Mandatory attachment indicator | true |
| 5 | MaxFileSizeMB | Integer | O | Maximum file size in MB | 10 |
| 6 | Active | Boolean | M | Active status indicator | true |

**Error Codes:**
- **ATTACHMENT_E001**: "Invalid attachment parameters" (HTTP 400)
- **ATTACHMENT_E002**: "Attachment type not found" (HTTP 404)
- **ATTACHMENT_E003**: "File exceeds size limit" (HTTP 413)

**Sample JSON Request:**
```json
GET /api/AttachmentNames?$sort=AttachmentName_Desc&active=1
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 1,
    "AttachmentName_Desc": "Bill of Lading",
    "DocumentType": "Shipping",
    "IsRequired": true,
    "MaxFileSizeMB": 10,
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  },
  {
    "Id": 2,
    "AttachmentName_Desc": "Commercial Invoice",
    "DocumentType": "Financial",
    "IsRequired": true,
    "MaxFileSizeMB": 5,
    "Active": true,
    "CreatedOn": "2023-01-15T10:30:00Z",
    "CreatedById": 1,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

#### 5.3.3 CTN Tracking API

**Business Purpose:** Manages CTN shipment tracking information essential for logistics monitoring and cargo visibility. Critical for providing real-time shipment status, managing transport schedules, and enabling proactive logistics coordination throughout the shipping lifecycle.

**Endpoint:** `GET /api/ctnTracking`

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | $expand | String - 500 | O | OData expand parameter | CTN,DestinationPort,SourcePort,TransportType |
| 2 | ctn | Integer | M | CTN identifier | 503808 |
| 3 | ctnid | Integer | M | CTN identifier (alternative) | 503808 |

**UI Validation Rules:**
- **TRACKING_UI_001**: CTN ID required for tracking lookup
- **TRACKING_UI_002**: Display tracking timeline visualization
- **TRACKING_UI_003**: Show estimated vs actual times with status

**Business Validation Rules:**
- **TRACKING_BV_001**: CTN must exist and be active
- **TRACKING_BV_002**: Tracking dates must be logical sequence
- **TRACKING_BV_003**: Vessel and voyage information must be consistent

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
| 8 | ATD | DateTime | O | Actual time of departure | 2023-12-15T11:15:00Z |
| 9 | ATA | DateTime | O | Actual time of arrival | 2023-12-20T14:45:00Z |
| 10 | VesselId | Integer | O | Vessel identifier | 5163 |
| 11 | VoyageNumber | String - 50 | O | Voyage number | 546894 |

**Error Codes:**
- **TRACKING_E001**: "Invalid CTN ID" (HTTP 400)
- **TRACKING_E002**: "Tracking information not found" (HTTP 404)
- **TRACKING_E003**: "Tracking data inconsistent" (HTTP 422)

**Sample JSON Request:**
```json
GET /api/ctnTracking?$expand=CTN,DestinationPort,SourcePort,TransportType&ctnid=503808
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
[
  {
    "Id": 71898,
    "CTNId": 503808,
    "SourcePortId": 80,
    "DestinationPortId": 35,
    "TransportTypeId": 1,
    "ETD": "2025-11-12T00:00:00.000Z",
    "ETA": "2025-12-09T00:00:00.000Z",
    "ATD": null,
    "ATA": null,
    "VesselId": 5163,
    "VoyageNumber": "546894",
    "CreatedOn": "2025-11-12T18:49:00Z",
    "CreatedById": 13345,
    "ModifiedOn": null,
    "ModifiedById": null
  }
]
```

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

**Business Validation Rules:**
- **CONTAINER_BV_001**: Container number must follow ISO 6346 standard
- **CONTAINER_BV_002**: Container type must be valid and active
- **CONTAINER_BV_003**: Seal numbers must be unique per container

**Error Codes:**
- **CONTAINER_E001**: "Invalid container number pattern" (HTTP 400)
- **CONTAINER_E002**: "Container already exists" (HTTP 409)
- **CONTAINER_E003**: "Invalid container type" (HTTP 422)

**Sample JSON Request (GET):**
```json
GET /api/ctnContainers?$expand=ContainerType&ctn=503808&ctnid=503808
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response (GET):**
```json
[]
```

**Sample JSON Request (POST):**
```json
POST /api/ctnContainers
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

{
  "Id": null,
  "CTNId": 503808,
  "ContainerTypeId": 31,
  "Number_of_Containers": 1,
  "ContainerNumbers": "MSCU1234567",
  "SealNumbers": "23234",
  "Groupage": false,
  "ContainerType": null,
  "CTN": null,
  "IsEmpty": false,
  "OwnedByShipper": false
}
```

**Sample JSON Response (POST Success):**
```json
{
  "Id": 510046,
  "CTNId": 503808,
  "ContainerTypeId": 31,
  "Number_of_Containers": 1,
  "ContainerNumbers": "MSCU1234567", 
  "SealNumbers": "23234",
  "Groupage": false,
  "ContainerType": null,
  "CTN": null,
  "IsEmpty": false,
  "OwnedByShipper": false
}
```

**Sample JSON Response (GET /new Template):**
```json
{
  "Id": null,
  "CTNId": null,
  "ContainerTypeId": null,
  "Number_of_Containers": 1,
  "ContainerNumbers": null,
  "SealNumbers": null,
  "Groupage": false,
  "ContainerType": null,
  "CTN": null,
  "IsEmpty": false,
  "OwnedByShipper": false
}
```

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

**UI Validation Rules:**
- **FILEUP_UI_001**: File size must not exceed 10MB
- **FILEUP_UI_002**: Only approved file types allowed (PDF, JPG, PNG, DOC, DOCX)
- **FILEUP_UI_003**: File name must not contain special characters

**Business Validation Rules:**
- **FILEUP_BV_001**: File must not be corrupted or malicious
- **FILEUP_BV_002**: Duplicate files should be detected and warned
- **FILEUP_BV_003**: User must have permission to upload files

**Error Codes:**
- **FILEUP_E001**: "File size exceeds maximum limit" (HTTP 413)
- **FILEUP_E002**: "File type not supported" (HTTP 415)
- **FILEUP_E003**: "File upload failed" (HTTP 500)

**Sample Multipart Request:**
```
POST /api/fileupload
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="Bill_of_Lading.pdf"
Content-Type: application/pdf

[Binary PDF file content]
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="fileName"

Bill_of_Lading.pdf
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="description"

Original shipping document for CTN certificate
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

**Sample JSON Response:**
```json
{
  "fileId": "0da7461c-2155-4d20-a695-6b7463367327",
  "fileName": "Bill_of_Lading.pdf",
  "fileSize": 245760,
  "mimeType": "application/pdf",
  "uploadDate": "2023-11-12T14:30:00Z"
}
```

**GET /api/fileupload/{fileId} - Download File**

**Request Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | fileId | String (UUID) | M | File identifier from URL path | 0da7461c-2155-4d20-a695-6b7463367327 |

**Sample Download Request:**
```
GET /api/fileupload/0da7461c-2155-4d20-a695-6b7463367327
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Response Elements:**

| S. No | Attributes | Data Type-Length | Condition | Format/Derivation Logic | Data Example |
|-------|------------|------------------|-----------|------------------------|--------------|
| 1 | contentStream | Base64 Binary | M | Base64 encoded file content | JVBERi0xLjQKJeLjz9MK... |
| 2 | fileName | String - 256 | M | Original file name | Bill_of_Lading.pdf |
| 3 | mimeType | String - 100 | M | File MIME type | application/pdf |
| 4 | fileSize | Integer | M | File size in bytes | 245760 |

**Sample Download Response:**
```json
{
  "contentStream": "JVBERi0xLjQKJeLjz9MKNSAwIG9iago8PC9MZW5ndGggNzggL0ZpbHRlciAvRmxhdGVEZWNvZGU+PnN0cmVhbQ==",
  "fileName": "Bill_of_Lading.pdf",
  "mimeType": "application/pdf",
  "fileSize": 245760
}
```

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

## 6. Enhanced API Capabilities ⚡

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

#### 6.4.2 Status Retrieval API (Polling-Based Status Updates)

**Business Purpose:** Enables JUL system to retrieve current status of CNCA certificates by polling SINTECE system. Replaces webhook-based notifications with pull-based status updates, providing reliable status synchronization, eliminating callback URL management, and supporting firewall-friendly integration patterns.

**Endpoint:** `GET /api/ctns/{ctnId}/status`

**Request Elements:**

| S. No | Attributes | Data Type - Length | Condition (M/O) | Format/Derivation logic for fields | Data Example |
|-------|------------|-------------------|-----------------|-----------------------------------|--------------|
| 1 | ctnId | Integer | M | CTN certificate identifier (path parameter) | 503808 |
| 2 | includeHistory | Boolean | O | Include status change history (query param) | false |
| 3 | includeDetails | Boolean | O | Include detailed status information (query param) | true |

**Path Parameters:**
- `ctnId`: CTN certificate identifier (mandatory)

**Query Parameters:**
- `includeHistory`: Set to true to get full status change history
- `includeDetails`: Set to true to get detailed status information

**UI Validation Rules:**
- **STATUS_UI_001**: CTN ID mandatory, positive integer
- **STATUS_UI_002**: Boolean parameters only accept true/false
- **STATUS_UI_003**: Display loading state during status retrieval

**Business Validation Rules:**
- **STATUS_BV_001**: CTN must exist in system
- **STATUS_BV_002**: User must have permission to view CTN status
- **STATUS_BV_003**: Status must be current (not stale data)

**Response Elements:**

| S. No | Attributes | Data Type - Length | Condition (M/O) | Format/Derivation logic for fields | Data Example |
|-------|------------|-------------------|-----------------|-----------------------------------|--------------|
| 1 | ctnId | Integer | M | CTN certificate identifier | 503808 |
| 2 | ctnReferenceNumber | String - 50 | M | System generated CTN reference | 170543 |
| 3 | currentStatus | String - 50 | M | Current certificate status | Approved |
| 4 | statusId | Integer | M | Status identifier | 3 |
| 5 | statusUpdatedAt | DateTime | M | Last status update timestamp | 2025-11-14T10:30:00Z |
| 6 | statusUpdatedBy | String - 100 | O | User who updated status | ARCCLA_Broker_123 |
| 7 | canAmend | Boolean | M | Amendment eligibility flag | true |
| 8 | canCancel | Boolean | M | Cancellation eligibility flag | false |
| 9 | statusMessage | String - 500 | O | Status description or notes | Certificate approved by ARCCLA |
| 10 | nextAction | String - 200 | O | Recommended next action | Process payment and download certificate |
| 11 | statusHistory | Array | O | Status change history (if requested) | [...] |

**Status History Element (when includeHistory=true):**

| S. No | Attributes | Data Type - Length | Condition (M/O) | Format/Derivation logic for fields | Data Example |
|-------|------------|-------------------|-----------------|-----------------------------------|--------------|
| 1 | statusId | Integer | M | Status identifier | 2 |
| 2 | statusName | String - 50 | M | Status name | Submitted |
| 3 | changedAt | DateTime | M | Status change timestamp | 2025-11-13T14:20:00Z |
| 4 | changedBy | String - 100 | O | User who changed status | Customs_Broker_456 |
| 5 | remarks | String - 500 | O | Status change remarks | Submitted for ARCCLA review |

**Error Codes:**
- **STATUS_E001**: "CTN not found" (HTTP 404)
- **STATUS_E002**: "Access denied" (HTTP 403)
- **STATUS_E003**: "Invalid CTN ID format" (HTTP 400)
- **STATUS_E004**: "Status service temporarily unavailable" (HTTP 503)

**Sample API Request:**
```http
GET /api/ctns/503808/status?includeHistory=true&includeDetails=true
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Sample JSON Response:**
```json
{
  "ctnId": 503808,
  "ctnReferenceNumber": "170543",
  "currentStatus": "Approved",
  "statusId": 3,
  "statusUpdatedAt": "2025-11-14T10:30:00Z",
  "statusUpdatedBy": "ARCCLA_Broker_123",
  "canAmend": true,
  "canCancel": false,
  "statusMessage": "Certificate approved by ARCCLA. Ready for payment processing.",
  "nextAction": "Process payment and download certificate",
  "statusHistory": [
    {
      "statusId": 1,
      "statusName": "Created",
      "changedAt": "2025-11-12T18:49:30Z",
      "changedBy": "Customs_Broker_456",
      "remarks": "Initial CTN creation"
    },
    {
      "statusId": 2,
      "statusName": "Submitted",
      "changedAt": "2025-11-13T14:20:00Z",
      "changedBy": "Customs_Broker_456",
      "remarks": "Submitted for ARCCLA review"
    },
    {
      "statusId": 3,
      "statusName": "Approved",
      "changedAt": "2025-11-14T10:30:00Z",
      "changedBy": "ARCCLA_Broker_123",
      "remarks": "Certificate approved by ARCCLA"
    }
  ]
}
```

**Polling Strategy Recommendations:**

| Certificate Status | Recommended Polling Interval | Notes |
|-------------------|------------------------------|-------|
| **Created** | No polling needed | Local status |
| **Submitted** | Every 5 minutes | Active review period |
| **UnderReview** | Every 10 minutes | ARCCLA processing |
| **PendingInfo** | Every 30 minutes | Waiting for trader response |
| **Approved** | Every 2 minutes | Payment processing |
| **Issued** | No polling needed | Final status |
| **Cancelled** | No polling needed | Final status |

**Implementation Guidelines:**
1. **Efficient Polling:** Use appropriate intervals based on certificate status
2. **Rate Limiting:** Respect API rate limits (max 120 requests/minute per user)
3. **Caching:** Cache status responses for 30 seconds to reduce API calls
4. **Error Handling:** Implement exponential backoff for failed polling attempts
5. **User Experience:** Show real-time updates in UI based on polling results
6. **Background Jobs:** Use scheduled jobs for polling instead of continuous loops
7. **Notification:** Trigger user notifications when status changes detected

**Advantages Over Webhooks:**
- ✅ No callback URL configuration required
- ✅ Firewall-friendly (outbound requests only)
- ✅ Better control over update frequency
- ✅ Simpler security model (no webhook signature validation)
- ✅ Easier error handling and retry logic
- ✅ No missed notifications due to network issues

---

<div style="page-break-before: always;"></div>

## 7. API Implementation Summary 📊

### 6.1 Complete CNCA Certificate API Coverage

The JUL-SINTECE Integration Control Document provides comprehensive API documentation covering the complete CNCA certificate lifecycle with section-by-section submission capabilities.

**📈 API Coverage Statistics:**
- **Total APIs Documented**: 31 comprehensive APIs
- **Master Data APIs**: 15 essential reference data endpoints
- **Certificate Management APIs**: 11 core certificate workflow endpoints
- **CTN Related Entity APIs**: 5 supporting data endpoints
- **JSON Coverage**: 100% of APIs include production-ready request/response samples

**🔧 Section-by-Section Certificate Submission APIs:**

| API Category | Endpoint | Purpose | Production Data |
|--------------|----------|---------|-----------------|
| **Core Creation** | POST /api/ctns | Create initial CTN record | ✅ CTN 503808 |
| **Address Management** | POST /api/ctnAddresses | Add shipper/consignee/forwarder details | ✅ Live addresses |
| **Cargo Details** | POST /api/ctnGoods | Add goods classifications and values | ✅ Cargo data |
| **Container Info** | POST /api/ctnContainers | Add container types and numbers | ✅ Container specs |
| **Transport Routes** | POST /api/ctnTracking | Add vessel and port information | ✅ Route data |
| **Document Attachment** | POST /api/ctnAttachments | Link supporting documents | ✅ File links |
| **Final Submission** | POST /api/ctns/actions/requestvisa/{id} | Submit for approval | ✅ Visa requests |

**🎯 Key Integration Benefits:**

1. **Progressive Data Entry**: Section-by-section approach improves user experience and data quality
2. **Comprehensive Validation**: Field-level and business rule validation at each step
3. **Production Ready**: All APIs tested with real SINTECE system data
4. **Complete Workflow**: From initial creation to final certificate approval
5. **Error Handling**: Detailed error codes and validation messages
6. **Audit Trail**: Complete tracking of certificate submission process

**🔄 Workflow Completeness:**
- ✅ **Initial Creation**: Basic CTN record with core information
- ✅ **Data Enhancement**: Section-wise addition of detailed information
- ✅ **Document Management**: File upload and attachment linking
- ✅ **Validation & Submission**: Complete data validation before approval request
- ✅ **Status Tracking**: Real-time status monitoring throughout process
- ✅ **Amendment Support**: Post-issuance certificate modification capabilities
- ✅ **Cancellation Support**: Certificate cancellation workflow

### 6.2 Implementation Readiness

**🚀 Development Team Benefits:**
- Complete API specifications with production JSON samples
- Comprehensive error code documentation
- Business rule validation requirements
- Real system response examples for testing
- Step-by-step integration guidance

**⚡ Business Process Coverage:**
- End-to-end CNCA certificate lifecycle
- Section-by-section submission for improved UX
- Complete supporting document management
- Automated validation and approval workflows
- Real-time status tracking and notifications

---

<div style="page-break-before: always;"></div>

## 8. Validation Framework ✅

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

### 8.3 Authentication and Authorization

The JUL-SINTECE integration uses Keycloak as the primary Single Sign-On (SSO) solution for centralized authentication and authorization management. Keycloak provides enterprise-grade identity and access management capabilities, ensuring secure and seamless authentication across both JUL and SINTECE systems.

#### 8.3.1 SSO Solution - Keycloak

**Overview:**
The JUL-SINTECE integration uses Keycloak as the primary Single Sign-On (SSO) solution for centralized authentication and authorization management. Keycloak provides enterprise-grade identity and access management capabilities, ensuring secure and seamless authentication across both JUL and SINTECE systems.

**Key Features:**
- Centralized user authentication and session management
- Single Sign-On (SSO) across multiple applications
- Token-based authentication with JWT
- Role-based access control (RBAC)
- Multi-factor authentication (MFA) support
- User federation and identity brokering

#### 8.3.2 Supported Authentication Protocols

The client authentication system has the capability to integrate with Keycloak using the following protocols:

| Protocol | Description | Use Case |
|----------|-------------|----------|
| **OpenID Connect** | Authentication layer built on OAuth 2.0 | Recommended for user authentication and SSO |
| **OAuth 2.0** | Authorization framework for delegated access | API authorization and service-to-service communication |
| **SAML 2.0** | XML-based authentication protocol | Enterprise SSO integration (if required) |

**Primary Protocol:** OpenID Connect (OIDC) is the recommended protocol for JUL-SINTECE integration.

#### 8.3.3 Client Integration Capabilities

**Current System Capabilities:**
- JWT token support and validation
- Token-based authentication flow
- Support for Bearer token authentication
- Client credentials flow for service-to-service communication
- Authorization code flow for user authentication

**Integration Approach:**
1. **Client Registration:** Register JUL application in Keycloak realm
2. **Client Credentials:** Obtain client ID and client secret
3. **Token Endpoint:** Configure token endpoint for authentication
4. **User Info Endpoint:** Configure user information retrieval
5. **Logout Endpoint:** Implement proper logout and session management

#### 8.3.4 JWT Token Management

**Token Format and Structure:**
The system uses JSON Web Tokens (JWT) for secure authentication. All API requests must include a valid JWT token in the Authorization header.

**Token Request:**
```http
POST /auth/realms/{realm}/protocol/openid-connect/token
Content-Type: application/x-www-form-urlencoded

grant_type=password&
client_id=jul-client&
client_secret={client_secret}&
username={username}&
password={password}
```

**Token Response:**
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 3600,
  "refresh_expires_in": 1800,
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "not-before-policy": 0,
  "session_state": "d2d2b3b4-4f5e-4f3e-9c1a-5f6e7d8e9f0a",
  "scope": "profile email"
}
```

**Token Usage in API Requests:**
All API requests must include the access token in the Authorization header:
```http
GET /api/ctns
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Token Validation:**
- Tokens are validated on every API request
- Signature verification using public key from Keycloak
- Expiration time validation
- Issuer and audience claims validation
- Required scopes/roles validation

**Token Refresh:**
When the access token expires, use the refresh token to obtain a new access token:
```http
POST /auth/realms/{realm}/protocol/openid-connect/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token&
client_id=jul-client&
client_secret={client_secret}&
refresh_token={refresh_token}
```

**Token Lifecycle:**
- **Access Token Lifetime:** 60 minutes (configurable)
- **Refresh Token Lifetime:** 30 minutes (configurable)
- **Session Timeout:** Configurable per realm
- **Token Revocation:** Supported via logout endpoint

#### 8.3.5 Integration Requirements

**Technical Requirements:**
1. **Keycloak Server:** Version 21.0 or higher
2. **TLS/SSL:** All communication must use HTTPS
3. **Network Access:** JUL system must have network access to Keycloak server
4. **Client Configuration:** Proper client registration in Keycloak
5. **Role Mapping:** Define and map user roles for authorization

**Security Requirements:**
- Secure storage of client credentials
- Token encryption in transit
- Token validation on every API call
- Proper error handling for authentication failures
- Session timeout and automatic logout

**Implementation Checklist:**
- [ ] Register JUL application as Keycloak client
- [ ] Configure redirect URIs and valid origins
- [ ] Set up user roles and permissions
- [ ] Implement token acquisition flow
- [ ] Implement token refresh mechanism
- [ ] Add authorization header to all API calls
- [ ] Implement proper logout functionality
- [ ] Test token expiration and refresh
- [ ] Implement error handling for auth failures
- [ ] Document authentication flows for developers

---

*End of Interface Control Document*

**Document Status:** DRAFT v3.0  
**Last Updated:** November 14, 2025  
**Next Review:** December 14, 2025

---