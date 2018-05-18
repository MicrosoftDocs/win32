---
Description: 'The IX509EndorsementKey interface exposes the following methods.'
ms.assetid: '536E5DE6-FF14-45C8-9227-68AF673E5FDC'
title: IX509EndorsementKey Methods
---

# IX509EndorsementKey Methods

The [**IX509EndorsementKey**](ix509endorsementkey.md) interface exposes the following methods.

## In this section



| Topic                                                                                        | Description                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddCertificate method**](ix509endorsementkey-addcertificate.md)<br/>               | Add an endorsement key certificate to the key storage provider (KSP) that supports endorsement keys.<br/>                                                                                                                                                                                     |
| [**Close method**](ix509endorsementkey-close.md)<br/>                                 | Closes the endorsement key. You can only call the [**Close**](ix509endorsementkey-close.md) method after the [**Open**](ix509endorsementkey-open.md) method has been successfully called.<br/>                                                                                              |
| [**ExportPublicKey method**](ix509endorsementkey-exportpublickey.md)<br/>             | Exports the endorsement public key.<br/>                                                                                                                                                                                                                                                      |
| [**GetCertificateByIndex method**](ix509endorsementkey-getcertificatebyindex.md)<br/> | Gets the endorsement certificate associated with the endorsement key from the key storage provider for the specified index.<br/>                                                                                                                                                              |
| [**GetCertificateCount method**](ix509endorsementkey-getcertificatecount.md)<br/>     | Gets the count of the endorsement certificates in the key storage provider.<br/>                                                                                                                                                                                                              |
| [**Open method**](ix509endorsementkey-open.md)<br/>                                   | Opens the endorsement key. The endorsement key must be open before you can retrieve an information from the endorsement key, add or remove certificates, or export the endorsement key.<br/>                                                                                                  |
| [**RemoveCertificate method**](ix509endorsementkey-removecertificate.md)<br/>         | Removes an endorsement certificate related to the endorsement key from the key storage provider. You can only call the [**RemoveCertificate**](ix509endorsementkey-removecertificate.md) method after the [**Open**](ix509endorsementkey-open.md) method has been successfully called.<br/> |



 

 

 




