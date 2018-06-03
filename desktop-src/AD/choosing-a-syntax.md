---
title: Choosing a Syntax
description: This topic contains a list of recommended syntaxes to use when defining a new attribute.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ed8a4164-5c82-43c2-8efb-a735c963a884
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Active Directory, syntaxes, defined
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Choosing a Syntax

There are 23 syntaxes defined in Active Directory Domain Services. This topic contains a list of recommended syntaxes to use when defining a new attribute.For more information, see [Syntaxes for Attributes in Active Directory Domain Services](syntaxes-for-attributes-in-active-directory-domain-services.md).

The following table provides a list of recommendations.



| Data to store in attribute      | Syntax to use                                                      | Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Binary data                     | [**String(Octet)**](https://msdn.microsoft.com/library/ms684451)                       | Use to store binary data. This is an array of bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Binary data with a DN reference | [**Object(DN-Binary)**](https://msdn.microsoft.com/library/ms684429)               | Contains a binary value and a distinguished name (DN). The Active Directory server keeps the DN up-to-date.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Boolean                         | [**Boolean**](https://msdn.microsoft.com/library/ms684420)                                  | Use for boolean values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DN Reference                    | [**Object(DS-DN)**](https://msdn.microsoft.com/library/ms684431)                       | Use to store distinguished names that you want kept up-to-date by the Active Directory server. When an attribute of DN syntax is created with a valid DN, the server treats the attribute as a reference to the object represented by the DN that was set. If the referenced object is renamed or moved, the server ensures that the attribute reflects the change. If the attribute is reset with a new DN, the attribute is reference to the object represented by the new DN.                                |
| Integer                         | [**Integer**](https://msdn.microsoft.com/library/ms684425)                                  | Use for integers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Large Integer (64-bit values)   | [**LargeInteger**](https://msdn.microsoft.com/library/ms684427)                        | Use for 64-bit values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Linked DN                       | [**Object(DS-DN)**](https://msdn.microsoft.com/library/ms684431)                       | This string syntax can be used for linked DNs. Back links must be of syntax DN. Forward links can be of syntax DN as well as [**Object(DN-String)**](https://msdn.microsoft.com/library/ms684430), [**Object(DN-Binary)**](https://msdn.microsoft.com/library/ms684429), [**Object(Access-Point)**](https://msdn.microsoft.com/library/ms684428), or [**Object(OR-Name)**](https://msdn.microsoft.com/library/ms684432). Linked attributes must have a **linkID** defined. See the description of **linkID** in [**Attribute-Schema**](https://msdn.microsoft.com/library/ms680969) properties. |
| Security Descriptor             | [**String(NT-Sec-Desc)**](https://msdn.microsoft.com/library/ms684438)           | Octet string containing a security descriptor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Security Identifier (SID)       | [**String(Sid)**](https://msdn.microsoft.com/library/ms684453)                           | Octet string containing a security identifier (SID). Use this syntax to store SID values only.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| String                          | [**String(Unicode)**](https://msdn.microsoft.com/library/ms684455)                   | Use for most string attributes. It supports the Unicode character set. When the Active Directory server performs comparisons against attributes of this syntax (such as evaluating a query), it performs case-insensitive comparisons. Use the other string syntaxes ([**String(IA5)**](https://msdn.microsoft.com/library/ms684437), [**String(Numeric)**](https://msdn.microsoft.com/library/ms684439), and so on) to store strings that should contain only the specific character sets supported by the syntax.<br/>                          |
| String data with a DN reference | [**Object(DN-String)**](https://msdn.microsoft.com/library/ms684430)               | String containing a string value and a distinguished name (DN). The Active Directory server keeps the DN up-to-date.                                                                                                                                                                                                                                                                                                                                                                                            |
| Time                            | [**String(Generalized-Time)**](https://msdn.microsoft.com/library/ms684436) | Use the [**String(Generalized-Time)**](https://msdn.microsoft.com/library/ms684436) syntax to store time values rather than the [**String(UTC-Time)**](https://msdn.microsoft.com/library/ms684456) syntax because **String(Generalized-Time)** uses four characters for the year and **String(UTC-Time)** uses only two.                                                                                                                                                                                                                 |



 

 

 





