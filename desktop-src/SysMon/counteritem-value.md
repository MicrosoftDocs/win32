---
title: CounterItem.Value property
description: Retrieves the last sampled value of the counter.
ms.assetid: c5aeaa00-e185-484d-8a7a-d45a21690e20
keywords:
- Value property SysMon
- Value property SysMon , CounterItem class
- CounterItem class SysMon , Value property
topic_type:
- apiref
api_name:
- CounterItem.Value
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CounterItem.Value property

Retrieves the last sampled value of the counter.

This property is read-only.

## Syntax


```VB
Property Value As Double
```



## Property value

Last sampled value of the counter. The value is -1 if an error occurs.

## Remarks

This is the default property of the [**CounterItem**](counteritem.md) object.

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

[**CounterItem.GetValue**](counteritem-getvalue.md)
</dt> </dl>

 

 





