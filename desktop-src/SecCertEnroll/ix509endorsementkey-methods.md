---
description: The IX509EndorsementKey interface exposes the following methods.
ms.assetid: 536E5DE6-FF14-45C8-9227-68AF673E5FDC
title: IX509EndorsementKey Methods
ms.topic: reference
ms.date: 05/31/2018
---

# IX509EndorsementKey Methods

The [**IX509EndorsementKey**](/windows/desktop/api/Certenroll/nn-certenroll-ix509endorsementkey) interface exposes the following methods.

## In this section



| Topic                                                                                        | Description                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddCertificate method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-addcertificate)<br/>               | Add an endorsement key certificate to the key storage provider (KSP) that supports endorsement keys.<br/>                                                                                                                                                                                     |
| [**Close method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-close)<br/>                                 | Closes the endorsement key. You can only call the [**Close**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-close) method after the [**Open**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-open) method has been successfully called.<br/>                                                                                              |
| [**ExportPublicKey method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-exportpublickey)<br/>             | Exports the endorsement public key.<br/>                                                                                                                                                                                                                                                      |
| [**GetCertificateByIndex method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-getcertificatebyindex)<br/> | Gets the endorsement certificate associated with the endorsement key from the key storage provider for the specified index.<br/>                                                                                                                                                              |
| [**GetCertificateCount method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-getcertificatecount)<br/>     | Gets the count of the endorsement certificates in the key storage provider.<br/>                                                                                                                                                                                                              |
| [**Open method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-open)<br/>                                   | Opens the endorsement key. The endorsement key must be open before you can retrieve an information from the endorsement key, add or remove certificates, or export the endorsement key.<br/>                                                                                                  |
| [**RemoveCertificate method**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-removecertificate)<br/>         | Removes an endorsement certificate related to the endorsement key from the key storage provider. You can only call the [**RemoveCertificate**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-removecertificate) method after the [**Open**](/windows/desktop/api/Certenroll/nf-certenroll-ix509endorsementkey-open) method has been successfully called.<br/> |



 

 

 




