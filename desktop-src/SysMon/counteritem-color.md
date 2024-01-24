---
title: CounterItem.Color property
description: Retrieves or sets the color used to graph the counter value.
ms.assetid: 73630efc-3128-4db5-b64c-ebb2f5e7611a
keywords:
- Color property SysMon
- Color property SysMon , CounterItem class
- CounterItem class SysMon , Color property
topic_type:
- apiref
api_name:
- CounterItem.Color
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CounterItem.Color property

Retrieves or sets the color used to graph the counter value.

This property is read/write.

## Syntax


```VB
Property Color As stdole.OLE_COLOR
```



## Property value

Color used to graph the counter value.

## Remarks

If you do not specify the color to use, SYSMON selects colors for the first sixteen counters. If you specify more than sixteen counters, SYSMON will reuse the same colors from the first sixteen counters. To help distinguish the counters from one another, SYSMON changes the [**line style**](counteritem-linestyle.md) used for each multiple of sixteen counters up to the first 80 counters. For example, the first sixteen counters use a solid line style, the next sixteen use a dash line style, and so on. SYSMON then sets the [**line width**](counteritem-width.md) to 2 for counters 81 - 96 and to 3 for counters 96 - 112. If the collection contains more than 112 counters, the counters will contain duplicate color, line style, and width values.

**Prior to Windows Vista:** If you do not specify the color to use, SYSMON selects colors for the first sixteen counters. If you specify more than sixteen counters, SYSMON will reuse the same colors from the first sixteen counters. To help distinguish the counters from one another, SYSMON increases the [**line width**](counteritem-width.md) of the first three counters that receive the same color assignment. If more than three counters use the same color, SYSMON randomly chooses the line width to use for the counter.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**CounterItem**](counteritem.md)
</dt> </dl>

 

 





