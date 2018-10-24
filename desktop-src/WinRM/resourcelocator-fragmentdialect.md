---
title: ResourceLocator.FragmentDialect property
description: Gets or sets the language dialect for a resource fragment dialect when ResourceLocator is used in Session object operations such as Session.Get, Session.Put, or Session.Enumerate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 60b08084-f4b9-4049-b0cd-a7420fcffd7c
ms.tgt_platform: multiple
keywords:
- FragmentDialect property Windows Remote Management
- FragmentDialect property Windows Remote Management , ResourceLocator object
- ResourceLocator object Windows Remote Management , FragmentDialect property
topic_type:
- apiref
api_name:
- ResourceLocator.FragmentDialect
api_location:
- WSMAuto.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ResourceLocator.FragmentDialect property

Gets or sets the language dialect for a [*resource*](windows-remote-management-glossary.md) [*fragment*](windows-remote-management-glossary.md) *dialect* when [**ResourceLocator**](resourcelocator.md) is used in [**Session**](session.md) object operations such as [**Session.Get**](session-get.md), [**Session.Put**](session-put.md), or [**Session.Enumerate**](session-enumerate.md). A fragment represents one property or part of a resource. You can provide a [**ResourceLocator**](resourcelocator.md) object instead of specifying a resource URI in [**Session**](session.md) object operations. The dialect indicates what XML language describes the fragment to the service that implements the [WS-Management Protocol](ws-management-protocol.md) and receives the request.

This property is read/write.

## Syntax


```VB
ResourceLocator.FragmentDialect As string
```



## Property value

An XML string that identifies the language used in the [**FragmentPath**](resourcelocator-fragmentpath.md) property. The dialect string defaults to the XPath 1.0 specification. For more information, see [http://www.w3.org/TR/xpath](http://go.microsoft.com/fwlink/p/?linkid=84163).

## Remarks

[**IWSManResourceLocator::FragmentDialect**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanresourcelocator-get_fragmentdialect) is the corresponding C++ property.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**ResourceLocator**](resourcelocator.md)
</dt> </dl>

 

 





