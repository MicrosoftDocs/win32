---
title: Counters.Remove method
description: Removes a CounterItem instance from the collection.
ms.assetid: 88e5907a-8c8f-4a24-9c5d-0c592f61dac0
keywords:
- Remove method SysMon
- Remove method SysMon , Counters class
- Counters class SysMon , Remove method
topic_type:
- apiref
api_name:
- Counters.Remove
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Counters.Remove method

Removes a [**CounterItem**](counteritem.md) instance from the collection.

## Syntax


```VB
Counters.Remove( _
  ByVal index As Object _
)
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

Index of the [**CounterItem**](counteritem.md) object to remove from the collection. The index is one-based.

</dd> </dl>

## Return value

This method does not return a value.

## Exceptions



| Exception type                                  | Condition                                                      |
|-------------------------------------------------|----------------------------------------------------------------|
| **System.Runtime.InteropServices.COMException** | The specified index is not valid. The Err.Number value is ???. |



 

## Remarks

To remove all counters from the collection, you can call [**SystemMonitor.Reset**](systemmonitor-reset.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**Counters**](counters.md)
</dt> <dt>

[**SystemMonitor.Reset**](systemmonitor-reset.md)
</dt> </dl>

 

 





