---
title: ResourceLocator.MustUnderstandOptions property (WSManDisp.h)
description: Gets or sets the MustUnderstandOptions value for the ResourceLocator object.
ms.assetid: d366696c-9128-4cbd-98d0-6c2d16c75d59
ms.tgt_platform: multiple
keywords:
- MustUnderstandOptions property Windows Remote Management
- MustUnderstandOptions property Windows Remote Management , ResourceLocator object
- ResourceLocator object Windows Remote Management , MustUnderstandOptions property
topic_type:
- apiref
api_name:
- ResourceLocator.MustUnderstandOptions
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ResourceLocator.MustUnderstandOptions property

Gets or sets the **MustUnderstandOptions** value for the [**ResourceLocator**](resourcelocator.md) object. You can provide a [**ResourceLocator**](resourcelocator.md) object instead of specifying a resource URI in [**Session**](session.md) object operations such as [**Session.Get**](session-get.md), [**Session.Put**](session-put.md), or [**Session.Enumerate**](session-enumerate.md).

This property is read/write.

## Syntax


```VB
ResourceLocator.MustUnderstandOptions As boolean
```



## Property value

Indicates, when **True**, that the service which implements the [WS-Management Protocol](ws-management-protocol.md) must return an error if it is not capable of processing the option.

## Remarks

**IWSManResourceLocator::MustUnderstandOptions** is the corresponding C++ property.

## Requirements



| Requirement | Value |
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

 

 





