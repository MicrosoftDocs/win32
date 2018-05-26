---
title: ADSI Properties and Attributes
description: Attributes are sometimes referred to as properties. This can cause confusion. This documentation uses the following definitions for properties and attributes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8e391d36-5a8d-4960-805a-0caf281cab80
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- ADSI properties and attributes ADSI
- ADSI ADSI , using, accessing and manipulating data, properties and attributes
- properties ADSI
- attributes ADSI
- properties ADSI , defined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADSI Properties and Attributes

Attributes are sometimes referred to as properties. This can cause confusion. This documentation uses the following definitions for properties and attributes.

Properties are named values associated with a programming object. For example, the [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master) interface exposes properties such as [**Class**](iads-property-methods.md) and **Name**.

Attributes are the data associated with objects in a directory service. For example, a user object will have an attribute called **cn** which contains a string that is the common or relative distinguished name of the object. Attributes are accessible through ADSI interface methods such as [**IADs.Get**](/windows/win32/Iads/nf-iads-iads-get?branch=master) and [**IADs.Put**](/windows/win32/Iads/nf-iads-iads-put?branch=master).

For more information about ADSI properties and attributes, see:

-   [The ADSI Attribute Cache](the-adsi-attribute-cache.md)
-   [Single vs. Multiple Value Attributes](single-vs--multiple-value-attributes.md)
-   [Active Directory Operational Attributes](active-directory-operational-attributes.md)

 

 




