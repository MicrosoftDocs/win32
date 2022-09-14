---
title: Counters.Item property
description: Retrieves the specified CounterItem instance from the collection.
ms.assetid: bf503371-c8bd-4e0d-ab8d-58de3f8fac5f
keywords:
- Item property SysMon
- Item property SysMon , Counters class
- Counters class SysMon , Item property
topic_type:
- apiref
api_name:
- Counters.Item
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Counters.Item property

Retrieves the specified [**CounterItem**](counteritem.md) instance from the collection.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal index As Object _
) As CounterItem
```



## Property value

[**CounterItem**](counteritem.md) instance that corresponds to the specified index value.

## Exceptions



| Exception type                                  | Condition                         |
|-------------------------------------------------|-----------------------------------|
| **System.Runtime.InteropServices.COMException** | The specified index is not valid. |



 

## Remarks

This is the default property of the [**Counters**](counters.md) object.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**CounterItem**](counteritem.md)
</dt> <dt>

[**Counters**](counters.md)
</dt> </dl>

 

 





