---
Description: The IX509EndorsementKey interface exposes the following methods.
ms.assetid: 536E5DE6-FF14-45C8-9227-68AF673E5FDC
title: IX509EndorsementKey Methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IX509EndorsementKey Methods

The [**IX509EndorsementKey**](/windows/win32/Certenroll/nn-certenroll-ix509endorsementkey?branch=master) interface exposes the following methods.

## In this section



| Topic                                                                                        | Description                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddCertificate method**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-addcertificate?branch=master)<br/>               | Add an endorsement key certificate to the key storage provider (KSP) that supports endorsement keys.<br/>                                                                                                                                                                                     |
| [**Close method**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-close?branch=master)<br/>                                 | Closes the endorsement key. You can only call the [**Close**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-close?branch=master) method after the [**Open**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-open?branch=master) method has been successfully called.<br/>                                                                                              |
| [**ExportPublicKey method**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-exportpublickey?branch=master)<br/>             | Exports the endorsement public key.<br/>                                                                                                                                                                                                                                                      |
| [**GetCertificateByIndex method**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-getcertificatebyindex?branch=master)<br/> | Gets the endorsement certificate associated with the endorsement key from the key storage provider for the specified index.<br/>                                                                                                                                                              |
| [**GetCertificateCount method**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-getcertificatecount?branch=master)<br/>     | Gets the count of the endorsement certificates in the key storage provider.<br/>                                                                                                                                                                                                              |
| [**Open method**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-open?branch=master)<br/>                                   | Opens the endorsement key. The endorsement key must be open before you can retrieve an information from the endorsement key, add or remove certificates, or export the endorsement key.<br/>                                                                                                  |
| [**RemoveCertificate method**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-removecertificate?branch=master)<br/>         | Removes an endorsement certificate related to the endorsement key from the key storage provider. You can only call the [**RemoveCertificate**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-removecertificate?branch=master) method after the [**Open**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-open?branch=master) method has been successfully called.<br/> |



 

 

 




