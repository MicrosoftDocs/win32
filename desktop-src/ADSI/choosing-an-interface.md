---
title: Choosing an Interface for Binding
description: When a directory object is bound to, the caller specifies the type of ADSI interface desired.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '3c86e136-6d82-4baf-9c76-27dac8ad68ac'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["ADSI ADSI ,using,choosing an interface for binding"]
---

# Choosing an Interface for Binding

When a directory object is bound to, the caller specifies the type of ADSI interface desired. All ADSI directory objects support the [**IADs**](iads.md) interface. An ADSI object can also support other interfaces. The actual interfaces supported by the object depends on the class of object. For example, a user object supports the [**IADsUser**](iadsuser.md) interface, but will not support the [**IADsComputer**](iadscomputer.md) interface.

Automation clients should use the **IADs\*** interfaces because these interfaces are dual-interfaces that provide a greater level of abstraction and provide data using the [**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118) data type.

In addition to the **IADs\*** interfaces, C/C++ clients can use the [**IDirectoryObject**](idirectoryobject.md) and [**IDirectorySearch**](idirectorysearch.md) interfaces. These interfaces are not dual-interfaces and do not support automation. These interfaces do provide greater control over exactly which attributes to retrieve and allow access to the raw data stored in a property. For example, when the [**IADs::Get**](iads-get.md) method is used to retrieve the **ntSecurityDescriptor** attribute for an object, the **IADs::Get** method provides an [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface pointer that supports the [**IADsSecurityDescriptor**](iadssecuritydescriptor.md) interface. The **IADsSecurityDescriptor** interface is provided by ADSI to represent a security descriptor. In comparison, when the [**IDirectoryObject::GetObjectAttributes**](idirectoryobject-getobjectattributes.md) method is used to retrieve the **ntSecurityDescriptor** attribute, **IDirectoryObject::GetObjectAttributes** provides an array of bytes that can be cast to a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) structure. The Win32 security APIs can be used with this data to manipulate the security descriptor.

 

 




