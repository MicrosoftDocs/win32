---
title: The IADs and IDirectoryObject Interfaces
description: ADSI clients manage and manipulate directory service objects by using one of two COM interfaces IADs or IDirectoryObject.
ms.assetid: f9c486b0-3dfb-4abf-afbf-08749e04315f
ms.tgt_platform: multiple
keywords:
- IADs ADSI ,about
- IDirectoryObject ADSI , about
- ADSI ADSI ,using,IADs and IDirectoryObject interfaces
ms.topic: article
ms.date: 05/31/2018
---

# The IADs and IDirectoryObject Interfaces

ADSI clients manage and manipulate directory service objects by using one of two COM interfaces: [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) or [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject). **IADs** is an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface intended for use by late-bound clients such as those written in Microsoft Visual Basic, Java, and various scripting languages. **IDirectoryObject** is a vtable interface that provides direct access to objects by early bound clients such as those written in C and C++.

Each ADSI object must implement both [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) and [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject). ADSI clients written in languages such as C or C++, which are able to directly access vtables, can use either interface, but not both in the same application. ADSI clients written in Visual Basic or Java are limited to using **IADs**.

The [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface enables late-bound clients to take advantage of the inherent housekeeping features of the ADSI object model. Among these features is the property cache, which enables clients to read and write properties without going over the wire for each call. In addition, client applications gain the use of powerful UI and ActiveX control libraries and a simpler style of programming. In return, late-bound clients must use the **VARIANT** data type, which precludes using the richer native data types provided by ADSI.

The [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) interface enables early bound clients to take full advantage of native directory-service data types at the cost of foregoing a slight performance advantage from using the property cache. In return, the **IDirectoryObject** interface provides direct, on-the-wire access to object properties through a single request, rather than through individual **get** and **put** calls.

 

 