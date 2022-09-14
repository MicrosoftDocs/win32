---
title: CounterItem.ScaleFactor property
description: Retrieves or sets the scale factor used to graph the counter value.
ms.assetid: 8589c0e6-b1c1-4d85-a21e-3e76afee67b1
keywords:
- ScaleFactor property SysMon
- ScaleFactor property SysMon , CounterItem class
- CounterItem class SysMon , ScaleFactor property
topic_type:
- apiref
api_name:
- CounterItem.ScaleFactor
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CounterItem.ScaleFactor property

Retrieves or sets the scale factor used to graph the counter value.

This property is read/write.

## Syntax


```VB
Property ScaleFactor As Long
```



## Property value

Scale factor used in displaying the graphed counter values. Valid values range from -9 to 9 (the values correspond to 0.000000001 - 100000000.0).

**Prior to Windows Vista:** Valid values range from -7 to 7 (the values correspond to 0.0000001 - 1000000.0).

## Remarks

Only set this property if you want to change the counter's default scale factor (each counter defines its own scale factor). The value of this property is set to Integer.MaxValue if the counter is using its default scale factor to graph the values.

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

[**SystemMonitor.ScaleToFit**](systemmonitor-scaletofit.md)
</dt> </dl>

 

 





