---
Description: Lists the interfaces provided by CryptoAPI.
ms.assetid: f94f0264-78b8-4a28-9d3a-dda55db29897
title: Cryptography Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**ICertAdmin**](/windows/win32/Certadm/nn-certadm-icertadmin?branch=master)                                         | Used by administration programs to manage requests, certificates, and revocations.                                                                                                                                                              |
| [**ICertAdmin2**](/windows/win32/Certadm/nn-certadm-icertadmin2?branch=master)                                       | Used by administration programs to manage requests, certificates, and revocations. Supersedes [**ICertAdmin**](/windows/win32/Certadm/nn-certadm-icertadmin?branch=master).                                                                                                                 |
| [**ICertConfig**](/windows/win32/Certcli/nn-certcli-icertconfig?branch=master)                                       | Used by clients to get information about the available servers.                                                                                                                                                                                 |
| [**ICertConfig2**](/windows/win32/Certcli/nn-certcli-icertconfig2?branch=master)                                     | Used by clients to get information about the available servers. Supersedes [**ICertConfig**](/windows/win32/Certcli/nn-certcli-icertconfig?branch=master).                                                                                                                                  |
| [**ICertGetConfig**](/windows/win32/Certcli/nn-certcli-icertgetconfig?branch=master)                                 | Provides functionality for retrieving the public configuration data (specified during client setup) for a [*Certificate Services*](security.c_gly#-security-certificate-services-gly) server.                |
| [**ICertRequest**](/windows/win32/Certcli/nn-certcli-icertrequest?branch=master)                                     | Used to send a request to the server and get the results of the request.                                                                                                                                                                        |
| [**ICertRequest2**](/windows/win32/Certcli/nn-certcli-icertrequest2?branch=master)                                   | Used to send a request to the server and get the results of the request. Supersedes [**ICertRequest**](/windows/win32/Certcli/nn-certcli-icertrequest?branch=master).                                                                                                                       |
| [**ICertServerExit**](/windows/win32/Certif/nn-certif-icertserverexit?branch=master)                               | Used by [exit modules](exit-modules.md) to get certificate and request properties.                                                                                                                                                             |
| [**ICertServerPolicy**](/windows/win32/Certif/nn-certif-icertserverpolicy?branch=master)                           | Used by the [policy module](policy-modules.md) to get and set certificate and request properties.                                                                                                                                              |
| [**ICertView**](/windows/win32/Certview/nn-certview-icertview?branch=master)                                           | Used by clients for [viewing the Certificate Services database](viewing-the-certificate-services-database.md).                                                                                                                                 |
| [**ICertView2**](/windows/win32/Certview/nn-certview-icertview2?branch=master)                                         | Used by clients for viewing the Certificate Services database. Supersedes [**ICertView**](/windows/win32/Certview/nn-certview-icertview?branch=master).                                                                                                                                       |
| [**IEnumCERTVIEWATTRIBUTE**](/windows/win32/Certview/nn-certview-ienumcertviewattribute?branch=master)                 | Used by clients to access the certificate attributes for a row in the Certificate Services view.                                                                                                                                                |
| [**IEnumCERTVIEWCOLUMN**](/windows/win32/Certview/nn-certview-ienumcertviewcolumn?branch=master)                       | Used by clients to access the data columns of a row in the Certificate Services view.                                                                                                                                                           |
| [**IEnumCERTVIEWEXTENSION**](/windows/win32/Certview/nn-certview-ienumcertviewextension?branch=master)                 | Used by clients to access the certificate extension data for a row in the Certificate Services view.                                                                                                                                            |
| [**IEnumCERTVIEWROW**](/windows/win32/Certview/nn-certview-ienumcertviewrow?branch=master)                             | Used by clients to enumerate the rows of the Certificate Services view.                                                                                                                                                                         |
| [**IOCSPAdmin**](/windows/win32/certadm/nn-certadm-iocspadmin?branch=master)                                         | Used by administration programs to configure Online Certificate Status Protocol (OCSP) responder servers.                                                                                                                                       |
| [**IOCSPCAConfiguration**](/windows/win32/Certadm/nn-certadm-iocspcaconfiguration?branch=master)                     | Provides functionality to configure an OCSP responder service to handle status requests for a specific [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA).<br/> |
| [**IOCSPCAConfigurationCollection**](/windows/win32/Certadm/nn-certadm-iocspcaconfigurationcollection?branch=master) | Provides functionality to manage the CA configurations for which an OCSP responder service can handle requests.                                                                                                                                 |
| [**IOCSPProperty**](/windows/win32/Certadm/nn-certadm-iocspproperty?branch=master)                                   | Provides functionality to configure an OCSP responder server attribute.                                                                                                                                                                         |
| [**IOCSPPropertyCollection**](/windows/win32/Certadm/nn-certadm-iocsppropertycollection?branch=master)               | Used by administration programs to manage OCSP responder server attributes.                                                                                                                                                                     |



 

## Server Engine Import Interfaces

The following reference topics describe the interfaces that are imported by the server engine.



| Interface                                      | Description                                                                                                                            |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertExit**](/windows/win32/Certexit/nn-certexit-icertexit?branch=master)                 | Exported by exit modules. Used by the server engine to deliver finished certificates and revocation information.                       |
| [**ICertExit2**](/windows/win32/Certexit/nn-certexit-icertexit2?branch=master)               | Adds the [**GetManageModule**](/windows/win32/Certexit/nf-certexit-icertexit2-getmanagemodule?branch=master) method to [**ICertExit**](/windows/win32/Certexit/nn-certexit-icertexit?branch=master).                               |
| [**ICertManageModule**](/windows/win32/Certmod/nn-certmod-icertmanagemodule?branch=master) | Exported by policy or exit modules. Used to display module information or to display a user interface for configuration of the module. |
| [**ICertPolicy**](/windows/win32/Certpol/nn-certpol-icertpolicy?branch=master)             | Exported by the policy module. Used by the server engine to check requests and get properties for certificates.                        |
| [**ICertPolicy2**](/windows/win32/Certpol/nn-certpol-icertpolicy2?branch=master)           | Adds the [**GetManageModule**](/windows/win32/Certpol/nf-certpol-icertpolicy2-getmanagemodule?branch=master) method to [**ICertPolicy**](/windows/win32/Certpol/nn-certpol-icertpolicy?branch=master).                         |



 

## Encoding Interfaces

The following reference topics describe the interfaces that can be exported by [extension handlers](writing-custom-extension-handlers.md) and are imported by the policy module.



| Interface                                                | Description                                                                                                                                                                                                                                   |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertEncodeAltName**](/windows/win32/Certenc/nn-certenc-icertencodealtname?branch=master)         | Used by the [policy module](policy-modules.md) to handle alternate name extensions.                                                                                                                                                          |
| [**ICertEncodeBitString**](/windows/win32/Certenc/nn-certenc-icertencodebitstring?branch=master)     | Used by the policy module to handle bit strings used in certificate extensions.                                                                                                                                                               |
| [**ICertEncodeCRLDistInfo**](/windows/win32/Certenc/nn-certenc-icertencodecrldistinfo?branch=master) | Used by the policy module to handle [*certificate revocation list*](security.c_gly#-security-certificate-revocation-list-gly) (CRL) distribution information arrays used in certificate extensions. |
| [**ICertEncodeDateArray**](/windows/win32/Certenc/nn-certenc-icertencodedatearray?branch=master)     | Used by the policy module to handle **Date** arrays used in certificate extensions.                                                                                                                                                           |
| [**ICertEncodeLongArray**](/windows/win32/Certenc/nn-certenc-icertencodelongarray?branch=master)     | Used by the policy module to handle **Long** arrays used in certificate extensions.                                                                                                                                                           |
| [**ICertEncodeStringArray**](/windows/win32/Certenc/nn-certenc-icertencodestringarray?branch=master) | Used by the policy module to handle **STRING** arrays used in certificate extensions.                                                                                                                                                         |



 

## Certificate Enrollment Interfaces

This section describes the objects, methods and properties of the Certificate Enrollment Control and the object, methods, and properties available in Smart Card Enrollment Control. These include the following interfaces.



| Interface                                                                                  | Description                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICEnroll**](/windows/win32/Xenroll/nn-xenroll-icenroll?branch=master)                                                               | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**ICEnroll2**](/windows/win32/Xenroll/nn-xenroll-icenroll2?branch=master)                                                             | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**ICEnroll3**](/windows/win32/Xenroll/nn-xenroll-icenroll3?branch=master)                                                             | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**ICertificateEnrollmentPolicyServerSetup**](/windows/win32/Casetup/nn-casetup-icertificateenrollmentpolicyserversetup?branch=master) | Represents the Certificate Enrollment Policy (CEP) Web Service within Active Directory Certificate Services (ADCS). The service enables users and computers to obtain certificate enrollment policy information. |
| [**ICertificateEnrollmentServerSetup**](/windows/win32/Casetup/nn-casetup-icertificateenrollmentserversetup?branch=master)             | Represents the Certificate Enrollment Web Service (CES) within ADCS. The service enables users and computers to enroll for and renew certificates.                                                               |
| [**ICEnroll4**](/windows/win32/Xenroll/nn-xenroll-icenroll4?branch=master)                                                             | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**IEnroll**](/windows/win32/Xenroll/nn-xenroll-ienroll?branch=master)                                                                 | One of several interfaces that represent the Certificate Enrollment Control. The interface is primarily of interest if you are not using Automation.                                                             |
| [**IEnroll2**](/windows/win32/Xenroll/nn-xenroll-ienroll2?branch=master)                                                               | One of several interfaces that represent the Certificate Enrollment Control. The interface is primarily of interest if you are not using Automation.                                                             |
| [**IEnroll4**](/windows/win32/Xenroll/nn-xenroll-ienroll4?branch=master)                                                               | One of several interfaces that represent the Certificate Enrollment Control. The interface is primarily of interest if you are not using Automation.                                                             |
| [**ISCrdEnr**](iscrdenr.md)                                                               | Represents the smart card enrollment control. It is primarily of interest if you are not using Automation.                                                                                                       |



 

## CAPICOM Interoperability Interfaces

The following reference topics describe the interfaces that allow derivations of CryptoAPI to work together with CAPICOM 2.0.



| Interface                              | Description                                                                                                                                                                              |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertContext**](icertcontext.md)   | Provides access to the context of a CAPICOM X.509v3 [**Certificate**](certificate.md) object. This context allows the CAPICOM certificate to be used in other derivations of CryptoAPI. |
| [**ICertStore**](icertstore.md)       | Provides access to the context of a CAPICOM [**Store**](store.md) object. This context allows the CAPICOM certificate store to be used in other derivations of CryptoAPI.               |
| [**IChainContext**](ichaincontext.md) | Provides access to the context of a CAPICOM [**Chain**](chain.md) object. This context allows the CAPICOM certificate trust chain to be used in other derivations of CryptoAPI.         |



 

 

 




