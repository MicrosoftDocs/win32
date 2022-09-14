---
title: Choosing an Interface for Binding
description: When a directory object is bound to, the caller specifies the type of ADSI interface desired.
ms.assetid: 3c86e136-6d82-4baf-9c76-27dac8ad68ac
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,using,choosing an interface for binding
ms.topic: article
ms.date: 05/31/2018
---

# Choosing an Interface for Binding

When a directory object is bound to, the caller specifies the type of ADSI interface desired. All ADSI directory objects support the [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface. An ADSI object can also support other interfaces. The actual interfaces supported by the object depends on the class of object. For example, a user object supports the [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser) interface, but will not support the [**IADsComputer**](/windows/desktop/api/Iads/nn-iads-iadscomputer) interface.

Automation clients should use the **IADs\*** interfaces because these interfaces are dual-interfaces that provide a greater level of abstraction and provide data using the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) data type.

In addition to the **IADs\*** interfaces, C/C++ clients can use the [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) and [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) interfaces. These interfaces are not dual-interfaces and do not support automation. These interfaces do provide greater control over exactly which attributes to retrieve and allow access to the raw data stored in a property. For example, when the [**IADs::Get**](/windows/desktop/api/Iads/nf-iads-iads-get) method is used to retrieve the **ntSecurityDescriptor** attribute for an object, the **IADs::Get** method provides an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface pointer that supports the [**IADsSecurityDescriptor**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor) interface. The **IADsSecurityDescriptor** interface is provided by ADSI to represent a security descriptor. In comparison, when the [**IDirectoryObject::GetObjectAttributes**](/windows/desktop/api/Iads/nf-iads-idirectoryobject-getobjectattributes) method is used to retrieve the **ntSecurityDescriptor** attribute, **IDirectoryObject::GetObjectAttributes** provides an array of bytes that can be cast to a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure. The Win32 security APIs can be used with this data to manipulate the security descriptor.

 

 