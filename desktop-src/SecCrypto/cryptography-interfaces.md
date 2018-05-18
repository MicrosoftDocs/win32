---
Description: 'Lists the interfaces provided by CryptoAPI.'
ms.assetid: 'f94f0264-78b8-4a28-9d3a-dda55db29897'
title: Cryptography Interfaces
---

# Cryptography Interfaces

Cryptography interfaces are categorized according to usage as follows:

-   [Server Engine Export Interfaces](#server-engine-export-interfaces)
-   [Server Engine Import Interfaces](#server-engine-import-interfaces)
-   [Encoding Interfaces](#encoding-interfaces)
-   [Certificate Enrollment Interfaces](#certificate-enrollment-interfaces)
-   [CAPICOM Interoperability Interfaces](#capicom-interoperability-interfaces)

## Server Engine Export Interfaces

The following reference topic describe the interfaces that are exported by the server engine and are called by external objects.



| Interface                                                                | Description                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertAdmin**](icertadmin.md)                                         | Used by administration programs to manage requests, certificates, and revocations.                                                                                                                                                              |
| [**ICertAdmin2**](icertadmin2.md)                                       | Used by administration programs to manage requests, certificates, and revocations. Supersedes [**ICertAdmin**](icertadmin.md).                                                                                                                 |
| [**ICertConfig**](icertconfig.md)                                       | Used by clients to get information about the available servers.                                                                                                                                                                                 |
| [**ICertConfig2**](icertconfig2.md)                                     | Used by clients to get information about the available servers. Supersedes [**ICertConfig**](icertconfig.md).                                                                                                                                  |
| [**ICertGetConfig**](icertgetconfig.md)                                 | Provides functionality for retrieving the public configuration data (specified during client setup) for a [*Certificate Services*](security.c_gly#-security-certificate-services-gly) server.                |
| [**ICertRequest**](icertrequest.md)                                     | Used to send a request to the server and get the results of the request.                                                                                                                                                                        |
| [**ICertRequest2**](icertrequest2.md)                                   | Used to send a request to the server and get the results of the request. Supersedes [**ICertRequest**](icertrequest.md).                                                                                                                       |
| [**ICertServerExit**](icertserverexit.md)                               | Used by [exit modules](exit-modules.md) to get certificate and request properties.                                                                                                                                                             |
| [**ICertServerPolicy**](icertserverpolicy.md)                           | Used by the [policy module](policy-modules.md) to get and set certificate and request properties.                                                                                                                                              |
| [**ICertView**](icertview.md)                                           | Used by clients for [viewing the Certificate Services database](viewing-the-certificate-services-database.md).                                                                                                                                 |
| [**ICertView2**](icertview2.md)                                         | Used by clients for viewing the Certificate Services database. Supersedes [**ICertView**](icertview.md).                                                                                                                                       |
| [**IEnumCERTVIEWATTRIBUTE**](ienumcertviewattribute.md)                 | Used by clients to access the certificate attributes for a row in the Certificate Services view.                                                                                                                                                |
| [**IEnumCERTVIEWCOLUMN**](ienumcertviewcolumn.md)                       | Used by clients to access the data columns of a row in the Certificate Services view.                                                                                                                                                           |
| [**IEnumCERTVIEWEXTENSION**](ienumcertviewextension.md)                 | Used by clients to access the certificate extension data for a row in the Certificate Services view.                                                                                                                                            |
| [**IEnumCERTVIEWROW**](ienumcertviewrow.md)                             | Used by clients to enumerate the rows of the Certificate Services view.                                                                                                                                                                         |
| [**IOCSPAdmin**](iocspadmin.md)                                         | Used by administration programs to configure Online Certificate Status Protocol (OCSP) responder servers.                                                                                                                                       |
| [**IOCSPCAConfiguration**](iocspcaconfiguration.md)                     | Provides functionality to configure an OCSP responder service to handle status requests for a specific [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA).<br/> |
| [**IOCSPCAConfigurationCollection**](iocspcaconfigurationcollection.md) | Provides functionality to manage the CA configurations for which an OCSP responder service can handle requests.                                                                                                                                 |
| [**IOCSPProperty**](iocspproperty.md)                                   | Provides functionality to configure an OCSP responder server attribute.                                                                                                                                                                         |
| [**IOCSPPropertyCollection**](iocsppropertycollection.md)               | Used by administration programs to manage OCSP responder server attributes.                                                                                                                                                                     |



 

## Server Engine Import Interfaces

The following reference topics describe the interfaces that are imported by the server engine.



| Interface                                      | Description                                                                                                                            |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertExit**](icertexit.md)                 | Exported by exit modules. Used by the server engine to deliver finished certificates and revocation information.                       |
| [**ICertExit2**](icertexit2.md)               | Adds the [**GetManageModule**](icertexit2-getmanagemodule.md) method to [**ICertExit**](icertexit.md).                               |
| [**ICertManageModule**](icertmanagemodule.md) | Exported by policy or exit modules. Used to display module information or to display a user interface for configuration of the module. |
| [**ICertPolicy**](icertpolicy.md)             | Exported by the policy module. Used by the server engine to check requests and get properties for certificates.                        |
| [**ICertPolicy2**](icertpolicy2.md)           | Adds the [**GetManageModule**](icertpolicy2-getmanagemodule.md) method to [**ICertPolicy**](icertpolicy.md).                         |



 

## Encoding Interfaces

The following reference topics describe the interfaces that can be exported by [extension handlers](writing-custom-extension-handlers.md) and are imported by the policy module.



| Interface                                                | Description                                                                                                                                                                                                                                   |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertEncodeAltName**](icertencodealtname.md)         | Used by the [policy module](policy-modules.md) to handle alternate name extensions.                                                                                                                                                          |
| [**ICertEncodeBitString**](icertencodebitstring.md)     | Used by the policy module to handle bit strings used in certificate extensions.                                                                                                                                                               |
| [**ICertEncodeCRLDistInfo**](icertencodecrldistinfo.md) | Used by the policy module to handle [*certificate revocation list*](security.c_gly#-security-certificate-revocation-list-gly) (CRL) distribution information arrays used in certificate extensions. |
| [**ICertEncodeDateArray**](icertencodedatearray.md)     | Used by the policy module to handle **Date** arrays used in certificate extensions.                                                                                                                                                           |
| [**ICertEncodeLongArray**](icertencodelongarray.md)     | Used by the policy module to handle **Long** arrays used in certificate extensions.                                                                                                                                                           |
| [**ICertEncodeStringArray**](icertencodestringarray.md) | Used by the policy module to handle **STRING** arrays used in certificate extensions.                                                                                                                                                         |



 

## Certificate Enrollment Interfaces

This section describes the objects, methods and properties of the Certificate Enrollment Control and the object, methods, and properties available in Smart Card Enrollment Control. These include the following interfaces.



| Interface                                                                                  | Description                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICEnroll**](icenroll.md)                                                               | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**ICEnroll2**](icenroll2.md)                                                             | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**ICEnroll3**](icenroll3.md)                                                             | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**ICertificateEnrollmentPolicyServerSetup**](icertificateenrollmentpolicyserversetup.md) | Represents the Certificate Enrollment Policy (CEP) Web Service within Active Directory Certificate Services (ADCS). The service enables users and computers to obtain certificate enrollment policy information. |
| [**ICertificateEnrollmentServerSetup**](icertificateenrollmentserversetup.md)             | Represents the Certificate Enrollment Web Service (CES) within ADCS. The service enables users and computers to enroll for and renew certificates.                                                               |
| [**ICEnroll4**](icenroll4.md)                                                             | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**IEnroll**](ienroll.md)                                                                 | One of several interfaces that represent the Certificate Enrollment Control. The interface is primarily of interest if you are not using Automation.                                                             |
| [**IEnroll2**](ienroll2.md)                                                               | One of several interfaces that represent the Certificate Enrollment Control. The interface is primarily of interest if you are not using Automation.                                                             |
| [**IEnroll4**](ienroll4.md)                                                               | One of several interfaces that represent the Certificate Enrollment Control. The interface is primarily of interest if you are not using Automation.                                                             |
| [**ISCrdEnr**](iscrdenr.md)                                                               | Represents the smart card enrollment control. It is primarily of interest if you are not using Automation.                                                                                                       |



 

## CAPICOM Interoperability Interfaces

The following reference topics describe the interfaces that allow derivations of CryptoAPI to work together with CAPICOM 2.0.



| Interface                              | Description                                                                                                                                                                              |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertContext**](icertcontext.md)   | Provides access to the context of a CAPICOM X.509v3 [**Certificate**](certificate.md) object. This context allows the CAPICOM certificate to be used in other derivations of CryptoAPI. |
| [**ICertStore**](icertstore.md)       | Provides access to the context of a CAPICOM [**Store**](store.md) object. This context allows the CAPICOM certificate store to be used in other derivations of CryptoAPI.               |
| [**IChainContext**](ichaincontext.md) | Provides access to the context of a CAPICOM [**Chain**](chain.md) object. This context allows the CAPICOM certificate trust chain to be used in other derivations of CryptoAPI.         |



 

 

 




