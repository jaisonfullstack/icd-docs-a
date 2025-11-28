# JUL-SINTECE Integration API Endpoints Summary

This document provides a comprehensive list of all API endpoints identified in the JUL-SINTECE Integration Control Document for CNCA certificate processing.

## API Endpoints Summary Table

| S. No | Service Name | Provider | Consumer | Mode of Integration | Description |
|-------|--------------|----------|----------|-------------------|-------------|
| 1 | Get Cargo Types | SINTECE | JUL | REST | Retrieve cargo type classifications for certificate creation |
| 2 | Get Incoterms | SINTECE | JUL | REST | Get International Commercial Terms for trade documentation |
| 3 | Get Countries | SINTECE | JUL | REST | Retrieve country information for origin/destination selection |
| 4 | Get Carriers | SINTECE | JUL | REST | Get shipping carrier information for transport documentation |
| 5 | Get Currencies | SINTECE | JUL | REST | Retrieve currency codes for financial calculations |
| 6 | Get Banks | SINTECE | JUL | REST | Get banking institution data for payment processing |
| 7 | Get Units | SINTECE | JUL | REST | Retrieve measurement units for cargo quantity calculations |
| 8 | Get Container Types | SINTECE | JUL | REST | Get container type classifications for shipping |
| 9 | Get Transport Types | SINTECE | JUL | REST | Retrieve transportation mode classifications |
| 10 | Get Locations/Ports | SINTECE | JUL | REST | Get geographical location and port information |
| 11 | Get Goods Classifications | SINTECE | JUL | REST | Retrieve standardized goods classification codes (HS codes) |
| 12 | Get IMO Codes | SINTECE | JUL | REST | Get International Maritime Organization dangerous goods codes |
| 13 | Get Vessels | SINTECE | JUL | REST | Retrieve vessel information for maritime transport |
| 14 | Get CTN Cities | SINTECE | JUL | REST | Get city information for origin and destination tracking |
| 15 | Get CTN Ports | SINTECE | JUL | REST | Get Angolan port information for CTN certificate processing |
| 16 | Get CTN Certificates | SINTECE | JUL | REST | Retrieve CTN certificate records with comprehensive data |
| 17 | Get CTN Attachments | SINTECE | JUL | REST | Retrieve document attachments for CTN certificates |
| 18 | Create CTN Certificate | JUL | SINTECE | REST | Submit complete CTN certificate data in unified request |
| 19 | Request Certificate Visa | JUL | SINTECE | REST | Submit CTN certificate for approval and visa issuance |
| 20 | Upload Documents | JUL | SINTECE | REST | Upload supporting documents for certificate processing |
| 21 | Delete Documents | JUL | SINTECE | REST | Remove uploaded documents from certificate |
| 22 | Validate NIF Number | JUL | SINTECE | REST | Validate Angola Tax Registration Numbers for compliance |
| 23 | Download Invoice | SINTECE | JUL | REST | Download CNCA certificate invoices (Import certificates only) |
| 24 | Get Certificate Status | SINTECE | JUL | REST | Retrieve current certificate status with eligibility flags |
| 25 | Get Consignees | SINTECE | JUL | REST | Retrieve consignee information for certificate processing |
| 26 | Get Attachment Types | SINTECE | JUL | REST | Get standardized attachment type classifications |
| 27 | Get CTN Tracking | SINTECE | JUL | REST | Retrieve shipment tracking information for certificates |
| 28 | Upload Files | JUL | SINTECE | REST | General file upload for document management |
| 29 | Download Files | SINTECE | JUL | REST | Download uploaded files using file identifier |
| 30 | Get Enhanced Certificate Status | SINTECE | JUL | REST | Get comprehensive certificate status with operation eligibility |
| 31 | Get Parent CTN Relationships | SINTECE | JUL | REST | Retrieve allowed parent CTN relationships for groupage |
| 32 | Export CTN Data | SINTECE | JUL | REST | Export CTN certificate data in various formats (CSV, Excel) |

## API Categories

### 1. Master Data APIs (15 endpoints)
These APIs provide essential reference data required for certificate creation and validation:

- **Cargo Types API** - `GET /api/CargoTypes`
- **Incoterms API** - `GET /api/Incoterms`
- **Countries API** - `GET /api/Countries`
- **Carriers API** - `GET /api/Carriers`
- **Currencies API** - `GET /api/Currencies`
- **Banks API** - `GET /api/Banks`
- **Units API** - `GET /api/Units`
- **Container Types API** - `GET /api/ContainerTypes`
- **Transport Types API** - `GET /api/TransportTypes`
- **Locations/Ports API** - `GET /api/Locations`
- **Goods Classifications API** - `GET /api/GoodsClassifications`
- **IMO Codes API** - `GET /api/IMOs`
- **Vessels API** - `GET /api/Vessels`
- **CTN Cities API** - `GET /api/CTNCities`
- **CTN Ports API** - `GET /api/CTNPorts`

### 2. Certificate Management APIs (11 endpoints)
Core APIs for CTN certificate lifecycle management:

- **Get CTN Certificates** - `GET /api/ctns`
- **Get CTN Attachments** - `GET /api/ctnAttachments`
- **Create CTN Certificate** - `POST /api/ctns`
- **Request Certificate Visa** - `POST /api/ctns/actions/requestvisa/{id}`
- **Upload Documents** - `POST /api/ctns/{ctnId}/documents/upload`
- **Delete Documents** - `DELETE /api/ctns/{ctnId}/documents/{documentId}`
- **Validate NIF** - `POST /api/validation/nif`
- **Download Invoice** - `GET /api/invoices/{invoiceId}/download`
- **Get Certificate Status** - `GET /api/ctns/{ctnId}/status`
- **Enhanced Status** - `GET /api/CTNs/{id}/enhanced-status`
- **Export CTN Data** - `GET /api/ctns/export`

### 3. CTN Related Entity APIs (5 endpoints)
Supporting APIs for CTN-related data management:

- **Consignees API** - `GET /api/Consignees`
- **Attachment Types API** - `GET /api/AttachmentNames`
- **CTN Tracking API** - `GET /api/ctnTracking`
- **Parent CTN API** - `GET /api/Ctns/GetAllowedParentCtns`
- **File Management** - `POST/GET /api/fileupload`

### 4. Authentication API (Keycloak SSO)
Authentication and authorization management:

- **Token Endpoint** - `POST /auth/realms/{realm}/protocol/openid-connect/token`
- **User Info Endpoint** - `GET /auth/realms/{realm}/protocol/openid-connect/userinfo`
- **Logout Endpoint** - `POST /auth/realms/{realm}/protocol/openid-connect/logout`

## Integration Workflow Summary

### Primary Certificate Creation Workflow
1. **Authentication** - Obtain JWT token via Keycloak SSO
2. **Master Data Retrieval** - Get reference data (countries, ports, carriers, etc.)
3. **Certificate Creation** - Submit comprehensive CTN data via unified API
4. **Document Upload** - Attach supporting documents
5. **Visa Request** - Submit for ARCCLA approval
6. **Status Monitoring** - Poll for status updates
7. **Invoice Download** - Download invoice (Import certificates only)

## Technical Implementation Notes

### Authentication Requirements
- All APIs require valid JWT token in Authorization header
- Token format: `Bearer {access_token}`
- Token lifetime: 60 minutes with refresh capability
- Keycloak SSO integration required

### Data Format Standards
- Request/Response: JSON format
- Dates: ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ)
- File uploads: Multipart/form-data
- Character encoding: UTF-8

### Error Handling
- Standard HTTP status codes (200, 400, 401, 403, 404, 422, 500, 503)
- Structured error responses with error codes and messages
- Field-level validation error details
- Business rule violation explanations

### Performance Standards
- Master data API response time: < 2 seconds
- Certificate operations: < 5 seconds
- File uploads: < 30 seconds (10MB max)
- Status polling: Optimized intervals based on certificate status

## Business Process Coverage

This API specification covers the complete CNCA certificate lifecycle:

✅ **Certificate Creation** - Complete section-by-section submission
✅ **Document Management** - Upload, delete, and retrieve documents
✅ **Approval Workflow** - ARCCLA review and approval process
✅ **Status Tracking** - Real-time certificate status monitoring
✅ **Financial Management** - Invoice generation and download (Import only)
✅ **Compliance Validation** - NIF validation and business rule checks
✅ **Audit Trail** - Complete tracking of all certificate operations

## Integration Benefits

1. **Comprehensive Coverage** - 32 APIs cover core CNCA certificate process
2. **Production Ready** - Real system data examples and testing
3. **Unified Approach** - Single API for complete certificate submission
4. **Enhanced UX** - Section-by-section data entry support
5. **Business Compliance** - Built-in validation and compliance checks
6. **Operational Efficiency** - Streamlined workflows and automation
7. **Audit & Compliance** - Complete audit trail and regulatory compliance
8. **Error Resilience** - Comprehensive error handling and validation

---

**Document Information:**
- **Source:** JUL_SINTECE_Integration_Control_Document.md
- **Version:** 3.0
- **Generated:** November 28, 2025
- **Total APIs Documented:** 32 comprehensive endpoints
- **Integration Status:** Production Ready