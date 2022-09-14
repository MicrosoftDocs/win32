---
description: Lists the interfaces provided by CryptoAPI.
ms.assetid: f94f0264-78b8-4a28-9d3a-dda55db29897
title: Cryptography Interfaces
ms.topic: article
ms.date: 05/31/2018
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
| [**ICertAdmin**](/windows/desktop/api/Certadm/nn-certadm-icertadmin)                                         | Used by administration programs to manage requests, certificates, and revocations.                                                                                                                                                              |
| [**ICertAdmin2**](/windows/desktop/api/Certadm/nn-certadm-icertadmin2)                                       | Used by administration programs to manage requests, certificates, and revocations. Supersedes [**ICertAdmin**](/windows/desktop/api/Certadm/nn-certadm-icertadmin).                                                                                                                 |
| [**ICertConfig**](/windows/desktop/api/Certcli/nn-certcli-icertconfig)                                       | Used by clients to get information about the available servers.                                                                                                                                                                                 |
| [**ICertConfig2**](/windows/desktop/api/Certcli/nn-certcli-icertconfig2)                                     | Used by clients to get information about the available servers. Supersedes [**ICertConfig**](/windows/desktop/api/Certcli/nn-certcli-icertconfig).                                                                                                                                  |
| [**ICertGetConfig**](/windows/desktop/api/Certcli/nn-certcli-icertgetconfig)                                 | Provides functionality for retrieving the public configuration data (specified during client setup) for a [*Certificate Services*](../secgloss/c-gly.md) server.                |
| [**ICertRequest**](/windows/desktop/api/Certcli/nn-certcli-icertrequest)                                     | Used to send a request to the server and get the results of the request.                                                                                                                                                                        |
| [**ICertRequest2**](/windows/desktop/api/Certcli/nn-certcli-icertrequest2)                                   | Used to send a request to the server and get the results of the request. Supersedes [**ICertRequest**](/windows/desktop/api/Certcli/nn-certcli-icertrequest).                                                                                                                       |
| [**ICertServerExit**](/windows/desktop/api/Certif/nn-certif-icertserverexit)                               | Used by [exit modules](exit-modules.md) to get certificate and request properties.                                                                                                                                                             |
| [**ICertServerPolicy**](/windows/desktop/api/Certif/nn-certif-icertserverpolicy)                           | Used by the [policy module](policy-modules.md) to get and set certificate and request properties.                                                                                                                                              |
| [**ICertView**](/windows/desktop/api/Certview/nn-certview-icertview)                                           | Used by clients for [viewing the Certificate Services database](viewing-the-certificate-services-database.md).                                                                                                                                 |
| [**ICertView2**](/windows/desktop/api/Certview/nn-certview-icertview2)                                         | Used by clients for viewing the Certificate Services database. Supersedes [**ICertView**](/windows/desktop/api/Certview/nn-certview-icertview).                                                                                                                                       |
| [**IEnumCERTVIEWATTRIBUTE**](/windows/desktop/api/Certview/nn-certview-ienumcertviewattribute)                 | Used by clients to access the certificate attributes for a row in the Certificate Services view.                                                                                                                                                |
| [**IEnumCERTVIEWCOLUMN**](/windows/desktop/api/Certview/nn-certview-ienumcertviewcolumn)                       | Used by clients to access the data columns of a row in the Certificate Services view.                                                                                                                                                           |
| [**IEnumCERTVIEWEXTENSION**](/windows/desktop/api/Certview/nn-certview-ienumcertviewextension)                 | Used by clients to access the certificate extension data for a row in the Certificate Services view.                                                                                                                                            |
| [**IEnumCERTVIEWROW**](/windows/desktop/api/Certview/nn-certview-ienumcertviewrow)                             | Used by clients to enumerate the rows of the Certificate Services view.                                                                                                                                                                         |
| [**IOCSPAdmin**](/windows/desktop/api/certadm/nn-certadm-iocspadmin)                                         | Used by administration programs to configure Online Certificate Status Protocol (OCSP) responder servers.                                                                                                                                       |
| [**IOCSPCAConfiguration**](/windows/desktop/api/Certadm/nn-certadm-iocspcaconfiguration)                     | Provides functionality to configure an OCSP responder service to handle status requests for a specific [*certification authority*](../secgloss/c-gly.md) (CA).<br/> |
| [**IOCSPCAConfigurationCollection**](/windows/desktop/api/Certadm/nn-certadm-iocspcaconfigurationcollection) | Provides functionality to manage the CA configurations for which an OCSP responder service can handle requests.                                                                                                                                 |
| [**IOCSPProperty**](/windows/desktop/api/Certadm/nn-certadm-iocspproperty)                                   | Provides functionality to configure an OCSP responder server attribute.                                                                                                                                                                         |
| [**IOCSPPropertyCollection**](/windows/desktop/api/Certadm/nn-certadm-iocsppropertycollection)               | Used by administration programs to manage OCSP responder server attributes.                                                                                                                                                                     |



 

## Server Engine Import Interfaces

The following reference topics describe the interfaces that are imported by the server engine.



| Interface                                      | Description                                                                                                                            |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertExit**](/windows/desktop/api/Certexit/nn-certexit-icertexit)                 | Exported by exit modules. Used by the server engine to deliver finished certificates and revocation information.                       |
| [**ICertExit2**](/windows/desktop/api/Certexit/nn-certexit-icertexit2)               | Adds the [**GetManageModule**](/windows/desktop/api/Certexit/nf-certexit-icertexit2-getmanagemodule) method to [**ICertExit**](/windows/desktop/api/Certexit/nn-certexit-icertexit).                               |
| [**ICertManageModule**](/windows/desktop/api/Certmod/nn-certmod-icertmanagemodule) | Exported by policy or exit modules. Used to display module information or to display a user interface for configuration of the module. |
| [**ICertPolicy**](/windows/desktop/api/Certpol/nn-certpol-icertpolicy)             | Exported by the policy module. Used by the server engine to check requests and get properties for certificates.                        |
| [**ICertPolicy2**](/windows/desktop/api/Certpol/nn-certpol-icertpolicy2)           | Adds the [**GetManageModule**](/windows/desktop/api/Certpol/nf-certpol-icertpolicy2-getmanagemodule) method to [**ICertPolicy**](/windows/desktop/api/Certpol/nn-certpol-icertpolicy).                         |



 

## Encoding Interfaces

The following reference topics describe the interfaces that can be exported by [extension handlers](writing-custom-extension-handlers.md) and are imported by the policy module.



| Interface                                                | Description                                                                                                                                                                                                                                   |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertEncodeAltName**](/windows/desktop/api/Certenc/nn-certenc-icertencodealtname)         | Used by the [policy module](policy-modules.md) to handle alternate name extensions.                                                                                                                                                          |
| [**ICertEncodeBitString**](/windows/desktop/api/Certenc/nn-certenc-icertencodebitstring)     | Used by the policy module to handle bit strings used in certificate extensions.                                                                                                                                                               |
| [**ICertEncodeCRLDistInfo**](/windows/desktop/api/Certenc/nn-certenc-icertencodecrldistinfo) | Used by the policy module to handle [*certificate revocation list*](../secgloss/c-gly.md) (CRL) distribution information arrays used in certificate extensions. |
| [**ICertEncodeDateArray**](/windows/desktop/api/Certenc/nn-certenc-icertencodedatearray)     | Used by the policy module to handle **Date** arrays used in certificate extensions.                                                                                                                                                           |
| [**ICertEncodeLongArray**](/windows/desktop/api/Certenc/nn-certenc-icertencodelongarray)     | Used by the policy module to handle **Long** arrays used in certificate extensions.                                                                                                                                                           |
| [**ICertEncodeStringArray**](/windows/desktop/api/Certenc/nn-certenc-icertencodestringarray) | Used by the policy module to handle **STRING** arrays used in certificate extensions.                                                                                                                                                         |



 

## Certificate Enrollment Interfaces

This section describes the objects, methods and properties of the Certificate Enrollment Control and the object, methods, and properties available in Smart Card Enrollment Control. These include the following interfaces.



| Interface                                                                                  | Description                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICEnroll**](/windows/desktop/api/Xenroll/nn-xenroll-icenroll)                                                               | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**ICEnroll2**](/windows/desktop/api/Xenroll/nn-xenroll-icenroll2)                                                             | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**ICEnroll3**](/windows/desktop/api/Xenroll/nn-xenroll-icenroll3)                                                             | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**ICertificateEnrollmentPolicyServerSetup**](/windows/desktop/api/Casetup/nn-casetup-icertificateenrollmentpolicyserversetup) | Represents the Certificate Enrollment Policy (CEP) Web Service within Active Directory Certificate Services (ADCS). The service enables users and computers to obtain certificate enrollment policy information. |
| [**ICertificateEnrollmentServerSetup**](/windows/desktop/api/Casetup/nn-casetup-icertificateenrollmentserversetup)             | Represents the Certificate Enrollment Web Service (CES) within ADCS. The service enables users and computers to enroll for and renew certificates.                                                               |
| [**ICEnroll4**](/windows/desktop/api/Xenroll/nn-xenroll-icenroll4)                                                             | One of several interfaces that represent the Certificate Enrollment Control. It is primarily of interest if you are not using Automation.                                                                        |
| [**IEnroll**](/windows/desktop/api/Xenroll/nn-xenroll-ienroll)                                                                 | One of several interfaces that represent the Certificate Enrollment Control. The interface is primarily of interest if you are not using Automation.                                                             |
| [**IEnroll2**](/windows/desktop/api/Xenroll/nn-xenroll-ienroll2)                                                               | One of several interfaces that represent the Certificate Enrollment Control. The interface is primarily of interest if you are not using Automation.                                                             |
| [**IEnroll4**](/windows/desktop/api/Xenroll/nn-xenroll-ienroll4)                                                               | One of several interfaces that represent the Certificate Enrollment Control. The interface is primarily of interest if you are not using Automation.                                                             |
| [**ISCrdEnr**](iscrdenr.md)                                                               | Represents the smart card enrollment control. It is primarily of interest if you are not using Automation.                                                                                                       |



 

## CAPICOM Interoperability Interfaces

The following reference topics describe the interfaces that allow derivations of CryptoAPI to work together with CAPICOM 2.0.



| Interface                              | Description                                                                                                                                                                              |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertContext**](icertcontext.md)   | Provides access to the context of a CAPICOM X.509v3 [**Certificate**](certificate.md) object. This context allows the CAPICOM certificate to be used in other derivations of CryptoAPI. |
| [**ICertStore**](icertstore.md)       | Provides access to the context of a CAPICOM [**Store**](store.md) object. This context allows the CAPICOM certificate store to be used in other derivations of CryptoAPI.               |
| [**IChainContext**](ichaincontext.md) | Provides access to the context of a CAPICOM [**Chain**](chain.md) object. This context allows the CAPICOM certificate trust chain to be used in other derivations of CryptoAPI.         |



 

 

 
