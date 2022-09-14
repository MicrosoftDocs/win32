---
title: Mapping Active Directory Syntax to ADSI Syntax
description: The following table maps the Active Directory syntaxes to their corresponding ADSI syntaxes.
ms.assetid: ffb40eff-e137-4d6a-81e7-24d2cbbdbfbf
ms.tgt_platform: multiple
keywords:
- attributes ADSI ,mapping Active Directory syntax to ADSI syntax
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Active Directory Syntax to ADSI Syntax

The following table maps the Active Directory syntaxes to their corresponding ADSI syntaxes.



| Attribute syntax ID | Active Directory syntax type             | Equivalent ADSI syntax type                                         |
|---------------------|------------------------------------------|---------------------------------------------------------------------|
| 2.5.5.1<br/>  | DN String<br/>                     | DN String<br/>                                                |
| 2.5.5.2<br/>  | Object ID<br/>                     | CaseIgnore String<br/>                                        |
| 2.5.5.3<br/>  | Case Sensitive String<br/>         | CaseExact String<br/>                                         |
| 2.5.5.4<br/>  | Case Ignored String<br/>           | CaseIgnore String<br/>                                        |
| 2.5.5.5<br/>  | Print Case String<br/>             | Printable String<br/>                                         |
| 2.5.5.6<br/>  | Numeric String<br/>                | Numeric String<br/>                                           |
| 2.5.5.7<br/>  | **OR** Name DNWithOctetString<br/> | Not Supported<br/>                                            |
| 2.5.5.8<br/>  | Boolean<br/>                       | Boolean<br/>                                                  |
| 2.5.5.9<br/>  | Integer<br/>                       | Integer<br/>                                                  |
| 2.5.5.10<br/> | Octet String<br/>                  | Octet String<br/>                                             |
| 2.5.5.11<br/> | Time<br/>                          | UTC Time<br/>                                                 |
| 2.5.5.12<br/> | Unicode<br/>                       | Case Ignore String<br/>                                       |
| 2.5.5.13<br/> | Address<br/>                       | Not Supported<br/>                                            |
| 2.5.5.14<br/> | Distname-Address<br/>              |                                                                     |
| 2.5.5.15<br/> | NT Security Descriptor<br/>        | [**IADsSecurityDescriptor**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)<br/> |
| 2.5.5.16<br/> | Large Integer<br/>                 | [**IADsLargeInteger**](/windows/desktop/api/Iads/nn-iads-iadslargeinteger)<br/>             |
| 2.5.5.17<br/> | SID<br/>                           | Octet String<br/>                                             |



 

 

 





