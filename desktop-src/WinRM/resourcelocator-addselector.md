---
title: ResourceLocator.AddSelector method (WSManDisp.h)
description: Adds a selector to the ResourceLocator object. The selector specifies a particular instance of a resource.
ms.assetid: 4b513d39-a377-487f-a03b-f3c5ab0f0b5a
ms.tgt_platform: multiple
keywords:
- AddSelector method Windows Remote Management
- AddSelector method Windows Remote Management , ResourceLocator object
- ResourceLocator object Windows Remote Management , AddSelector method
topic_type:
- apiref
api_name:
- ResourceLocator.AddSelector
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ResourceLocator.AddSelector method

Adds a [*selector*](windows-remote-management-glossary.md) to the [**ResourceLocator**](resourcelocator.md) object. The selector specifies a particular instance of a *resource*. You can provide a [**ResourceLocator**](resourcelocator.md) object instead of specifying a resource URI in [**Session**](session.md) object operations such as [**Session.Get**](session-get.md), [**Session.Put**](session-put.md), or [**Session.Enumerate**](session-enumerate.md).

## Syntax


```VB
ResourceLocator.AddSelector( _
  ByVal resourceSelName, _
  ByVal selValue _
)
```



## Parameters

<dl> <dt>

*resourceSelName* \[in\]
</dt> <dd>

The selector name. For example, when requesting WMI data, this parameter is the key property for a WMI class.

</dd> <dt>

*selValue* \[in\]
</dt> <dd>

The selector value. For example, for WMI data, this parameter contains a value for a key property that identifies a specific instance.

</dd> </dl>

## Remarks

**IWSManResourceLocator::AddSelector** is the corresponding C++ method.

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

 

 





