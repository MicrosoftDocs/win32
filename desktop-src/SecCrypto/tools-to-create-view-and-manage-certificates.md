---
Description: CryptoAPI Tools are tools to perform common certificate management tasks.
ms.assetid: 29146de8-adae-444b-bc75-fa43a19ab8f9
title: Tools to Create, View, and Manage Certificates
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Tools to Create, View, and Manage Certificates

CryptoAPI Tools are tools to perform common certificate management tasks.



| Tool                                | Remarks                                                                                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MakeCert](makecert.md)<br/> | Creates a test [*X.509*](https://msdn.microsoft.com/28dba6ef-939f-4789-9789-ee6e0fef0177) certificate.<br/>                                                                                |
| [Cert2SPC](cert2spc.md)<br/> | Creates a test [*Software Publisher Certificate*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) (SPC).<br/>           |
| [CertMgr](certmgr.md)<br/>   | Manages certificates, CTLs, and [*certificate revocation lists*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CRLs).<br/> |



 

All user input to these tools is case insensitive. Separate options now exist for the [*key pair*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33) name and the [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) file.

## Additional Tools

Certutil.exe is a command-line tool that is installed as part of Certificate Services. You can use Certutil.exe to dump and display [*certification authority*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CA) configuration information, configure Certificate Services, back up and restore CA components, and verify [*certificates*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb), [*key pairs*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33), and certificate chains. For more information about Certutil, see the [Certutil](http://go.microsoft.com/fwlink/p/?linkid=120697) topic on Microsoft TechNet.

 

 




