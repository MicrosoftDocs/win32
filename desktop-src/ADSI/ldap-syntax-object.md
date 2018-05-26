---
title: LDAP Syntax Object
description: The LDAP provider uses the following mapping between the LDAP syntax and ADSI syntax.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a82cf8ab-9591-4489-87a6-ccfab0e01d61
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,service providers,mapping syntax to LDAP syntax
- mapping ADSI syntax to LDAP syntax ADSI
- syntax and mapping from ADSI to LDAP ADSI
- LDAP service provider ADSI ,mapping ADSI syntax to LDAP syntax
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP Syntax Object

The LDAP provider uses the following mapping between the LDAP syntax and ADSI syntax.



| LDAP Syntax   | ADSI Syntax (Automation)            |
|---------------|-------------------------------------|
| ADsPath       | VT\_BSTR                            |
| Boolean       | VT\_BOOL                            |
| Counter       | VT\_I4                              |
| EmailAddress  | VT\_BSTR                            |
| FaxNumber     | VT\_BSTR                            |
| Integer       | VT\_I4                              |
| Interval      | VT\_I4                              |
| List          | VT\_VARIANT (VT\_BSTR \| VT\_ARRAY) |
| NetAddress    | VT\_BSTR                            |
| OctetString   | VT\_VARIANT                         |
| Path          | VT\_BSTR                            |
| PhoneNumber   | VT\_BSTR                            |
| PostalAddress | VT\_BSTR                            |
| SmallInterval | VT\_I4                              |
| String        | VT\_BSTR                            |
| Time          | VT\_DATE                            |



 

 

 




