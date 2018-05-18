---
title: The IADs and IDirectoryObject Interfaces
description: ADSI clients manage and manipulate directory service objects by using one of two COM interfaces IADs or IDirectoryObject.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'f9c486b0-3dfb-4abf-afbf-08749e04315f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["IADs ADSI ,about", "IDirectoryObject ADSI , about", "ADSI ADSI ,using,IADs and IDirectoryObject interfaces"]
---

# The IADs and IDirectoryObject Interfaces

ADSI clients manage and manipulate directory service objects by using one of two COM interfaces: [**IADs**](iads.md) or [**IDirectoryObject**](idirectoryobject.md). **IADs** is an [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface intended for use by late-bound clients such as those written in Microsoft Visual Basic, Java, and various scripting languages. **IDirectoryObject** is a vtable interface that provides direct access to objects by early bound clients such as those written in C and C++.

Each ADSI object must implement both [**IADs**](iads.md) and [**IDirectoryObject**](idirectoryobject.md). ADSI clients written in languages such as C or C++, which are able to directly access vtables, can use either interface, but not both in the same application. ADSI clients written in Visual Basic or Java are limited to using **IADs**.

The [**IADs**](iads.md) interface enables late-bound clients to take advantage of the inherent housekeeping features of the ADSI object model. Among these features is the property cache, which enables clients to read and write properties without going over the wire for each call. In addition, client applications gain the use of powerful UI and ActiveX control libraries and a simpler style of programming. In return, late-bound clients must use the **VARIANT** data type, which precludes using the richer native data types provided by ADSI.

The [**IDirectoryObject**](idirectoryobject.md) interface enables early bound clients to take full advantage of native directory-service data types at the cost of foregoing a slight performance advantage from using the property cache. In return, the **IDirectoryObject** interface provides direct, on-the-wire access to object properties through a single request, rather than through individual **get** and **put** calls.

 

 




