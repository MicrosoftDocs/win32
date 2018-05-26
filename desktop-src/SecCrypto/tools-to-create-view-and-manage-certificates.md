---
Description: CryptoAPI Tools are tools to perform common certificate management tasks.
ms.assetid: 29146de8-adae-444b-bc75-fa43a19ab8f9
title: Tools to Create, View, and Manage Certificates
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Tools to Create, View, and Manage Certificates

CryptoAPI Tools are tools to perform common certificate management tasks.



| Tool                                | Remarks                                                                                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MakeCert](makecert.md)<br/> | Creates a test [*X.509*](security.x_gly#-security-x-509-gly) certificate.<br/>                                                                                |
| [Cert2SPC](cert2spc.md)<br/> | Creates a test [*Software Publisher Certificate*](security.s_gly#-security-software-publisher-certificate-gly) (SPC).<br/>           |
| [CertMgr](certmgr.md)<br/>   | Manages certificates, CTLs, and [*certificate revocation lists*](security.c_gly#-security-certificate-revocation-list-gly) (CRLs).<br/> |



 

All user input to these tools is case insensitive. Separate options now exist for the [*key pair*](security.k_gly#-security-key-pair-gly) name and the [*private key*](security.p_gly#-security-private-key-gly) file.

## Additional Tools

Certutil.exe is a command-line tool that is installed as part of Certificate Services. You can use Certutil.exe to dump and display [*certification authority*](security.c_gly#-security-certification-authority-gly) (CA) configuration information, configure Certificate Services, back up and restore CA components, and verify [*certificates*](security.c_gly#-security-certificate-gly), [*key pairs*](security.k_gly#-security-key-pair-gly), and certificate chains. For more information about Certutil, see the [Certutil](http://go.microsoft.com/fwlink/p/?linkid=120697) topic on Microsoft TechNet.

 

 




