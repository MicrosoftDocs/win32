---
title: ResourceLocator.ClearOptions method (WSManDisp.h)
description: Removes any options from the ResourceLocator object.
ms.assetid: 1b4d7f15-c56f-4b0d-9614-8376012abca7
ms.tgt_platform: multiple
keywords:
- ClearOptions method Windows Remote Management
- ClearOptions method Windows Remote Management , ResourceLocator object
- ResourceLocator object Windows Remote Management , ClearOptions method
topic_type:
- apiref
api_name:
- ResourceLocator.ClearOptions
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ResourceLocator.ClearOptions method

Removes any [*options*](windows-remote-management-glossary.md) from the [**ResourceLocator**](resourcelocator.md) object. You can provide a [**ResourceLocator**](resourcelocator.md) object instead of specifying a resource URI in [**Session**](session.md) object operations such as [**Session.Get**](session-get.md), [**Session.Put**](session-put.md), or [**Session.Enumerate**](session-enumerate.md).

## Syntax


```VB
ResourceLocator.ClearOptions()
```



## Parameters

This method has no parameters.

## Remarks

**IWSManResourceLocator::ClearOptions** is the corresponding C++ method.

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

 

 





