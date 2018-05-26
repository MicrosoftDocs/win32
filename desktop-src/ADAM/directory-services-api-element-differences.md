---
title: Directory Services API Element Differences
description: When using Directory Services API elements to program for AD LDS, there are several important differences from programming for Active Directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b6f0f402-e1fe-4b78-a453-bf9380420ff6
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- Directory Services API Element Differences ADAM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Directory Services API Element Differences

When using Directory Services API elements to program for AD LDS, there are several important differences from programming for Active Directory.

The following table lists the differences in the Directory Services programming elements when used with AD LDS.



| Programming element                                            | Difference                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DsBindWithSpnEx**](https://msdn.microsoft.com/library/ms675963)                      | Added the **NTDSAPI\_BIND\_FORCE\_KERBEROS** flag.                                                                                                                                                                                                                                                                              |
| [**DsBindByInstance**](dsbindbyinstance.md)                   | New function.                                                                                                                                                                                                                                                                                                                   |
| **ADAM\_SCP\_SITE\_NAME\_STRING**                              | String constant used by AD LDS for constructing keyword values for SCP publication for a site name, for example: "site:Default-First-Site-Name".                                                                                                                                                                                |
| **ADAM\_SCP\_PARTITION\_STRING**                               | String constant used by AD LDS for constructing keyword values for SCP publication for a partition distinguished name, for example: "partition:O=FABRIKAM,L=WA,C=US".                                                                                                                                                           |
| **ADAM\_SCP\_INSTANCE\_NAME\_STRING**                          | String constant used by AD LDS for constructing keyword values for SCP publication for an instance name, for example: "instance:someinstance".                                                                                                                                                                                  |
| **ADAM\_SCP\_FSMO\_STRING**                                    | String constant used by AD LDS for constructing keyword values for SCP publication for an FSMO name prefix, for example: "fsmo:naming".                                                                                                                                                                                         |
| **ADAM\_SCP\_FSMO\_NAMING\_STRING**                            | String constant used by AD LDS for constructing keyword values for SCP publication for an FSMO name suffix, for example: "fsmo:naming".                                                                                                                                                                                         |
| **ADAM\_SCP\_FSMO\_SCHEMA\_STRING**                            | String constant used by AD LDS for constructing keyword values for SCP publication for an FSMO name suffix, for example: "fsmo:schema".                                                                                                                                                                                         |
| **ADAM\_REPL\_AUTHENTICATION\_MODE\_NEGOTIATE\_PASS\_THROUGH** | Negotiate with pass-through authentication. All instances must run using service accounts with the same name and password. Used with the [**ms-DS-Repl-Authentication-Mode**](https://msdn.microsoft.com/library/ms677477) attribute of the configuration partition for an AD LDS instance.<br/>                               |
| **ADAM\_REPL\_AUTHENTICATION\_MODE\_NEGOTIATE**                | Negotiate authentication. If Kerberos is available, it will be used. Otherwise, authentication will fall back to NTLM unless machine policy forbids this.Used with the [**ms-DS-Repl-Authentication-Mode**](https://msdn.microsoft.com/library/ms677477) attribute of the configuration partition for an AD LDS instance.<br/> |
| **ADAM\_REPL\_AUTHENTICATION\_MODE\_MUTUAL\_AUTH\_REQUIRED**   | AD LDS will require Kerberos mutual authentication.Used with the [**ms-DS-Repl-Authentication-Mode**](https://msdn.microsoft.com/library/ms677477) attribute of the configuration partition for an AD LDS instance.<br/>                                                                                                       |
| **NTDSDSA\_OPT\_DISABLE\_SPN\_REGISTRATION**                   | New value for **nTDSDSA** objects.                                                                                                                                                                                                                                                                                              |



 

AD LDS does not support the [**userAccountControl**](https://msdn.microsoft.com/library/ms680832) attribute. Instead, AD LDS uses several individual attributes to hold the information that is contained in the flags of the **userAccountControl** attribute. The following table lists the **userAccountControl** flags and their corresponding AD LDS attributes. Any **userAccountControl** flags that are not listed below are not supported by AD LDS.

| AD LDS attribute                                                                                | userAccountControl flag (defined in iads.h)                                | Hexadecimal value |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|-------------------|
| [**ms-DS-UserAccountAutoLocked**](https://msdn.microsoft.com/library/ms678641)                       | [**ADS\_UF\_LOCKOUT**](https://msdn.microsoft.com/library/aa772300)                            | 0x00000010        |
| [**msDS-UserAccountDisabled**](https://msdn.microsoft.com/library/ms677836)                             | [**ADS\_UF\_ACCOUNTDISABLE**](https://msdn.microsoft.com/library/aa772300)                     | 0x00000002        |
| [**msDS-UserDontExpirePassword**](https://msdn.microsoft.com/library/ms677837)                       | [**ADS\_UF\_DONT\_EXPIRE\_PASSWD**](https://msdn.microsoft.com/library/aa772300)               | 0x00010000        |
| [**ms-DS-UserEncryptedTextPasswordAllowed**](https://msdn.microsoft.com/library/ms678642) | [**ADS\_UF\_ENCRYPTED\_TEXT\_PASSWORD\_ALLOWED**](https://msdn.microsoft.com/library/aa772300) | 0x00000080        |
| [**msDS-UserPasswordExpired**](https://msdn.microsoft.com/library/ms677838)                             | [**ADS\_UF\_PASSWORD\_EXPIRED**](https://msdn.microsoft.com/library/aa772300)                  | 0x00800000        |
| [**ms-DS-UserPasswordNotRequired**](https://msdn.microsoft.com/library/ms678643)                   | [**ADS\_UF\_PASSWD\_NOTREQD**](https://msdn.microsoft.com/library/aa772300)                    | 0x00000020        |



 

 

 





