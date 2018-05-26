---
title: ADSI Element Differences
description: When using ADSI programming elements to develop applications for AD LDS, some differences apply.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 18190f88-92d2-4832-85f3-50bba8cc86c1
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- ADSI Element Differences ADAM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADSI Element Differences

When using ADSI programming elements to develop applications for AD LDS, some differences apply.

The following table lists the differences in the ADSI programming elements when used with AD LDS. For more information about the programming element, click the element name.



| Programming element                                                                                                                           | Difference                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ADS\_OPTION\_ENUM**](https://msdn.microsoft.com/library/aa772273) enumeration                                                                                     | Two values, [**ADS\_OPTION\_PASSWORD\_PORTNUMBER**](https://msdn.microsoft.com/library/aa772273) and **ADS\_OPTION\_PASSWORD\_METHOD**, added to facilitate setting passwords.                                                                                             |
| [**ADS\_PASSWORD\_ENCODING\_ENUM**](https://msdn.microsoft.com/library/aa772274) enumeration                                                              | Enumeration added to facilitate setting passwords.                                                                                                                                                                                                  |
| [**ADsGetObject**](https://msdn.microsoft.com/library/aa772184) and [**ADsOpenObject**](https://msdn.microsoft.com/library/aa772238) functions                                                   | Path parameter includes a port number to specify an AD LDS instance. For more information, see [LDAP ADsPath](https://msdn.microsoft.com/library/aa746384).                                                                                                                   |
| [**IADsOpenDSObject::OpenDSObject**](https://msdn.microsoft.com/library/aa706065) method                                                               | Path parameter includes a port number to specify an AD LDS instance. For more information, see [LDAP ADsPath](https://msdn.microsoft.com/library/aa746384).                                                                                                                   |
| [**IADsUser::ChangePassword**](https://msdn.microsoft.com/library/aa746341) and [**IADsUser::SetPassword**](https://msdn.microsoft.com/library/aa746344) methods               | Before using these methods, call the [**IADsObjectOptions::SetOption**](https://msdn.microsoft.com/library/aa706061) method to set port number ([**ADS\_OPTION\_PASSWORD\_PORTNUMBER**](https://msdn.microsoft.com/library/aa772273)) and method (**ADS\_OPTION\_PASSWORD\_METHOD**). |
| [**IADsAccessControlEntry::get\_Trustee**](https://msdn.microsoft.com/library/aa705952) and **IADsAccessControlEntry::put\_Trustee** methods | AD LDS security principal names use a string security identifier (SID) rather than a friendly name.                                                                                                                                                 |
| Miscellaneous                                                                                                                                 | The WinNT, NDS, and NWCOMPAT providers do not apply for AD LDS.                                                                                                                                                                                     |



 

 

 




