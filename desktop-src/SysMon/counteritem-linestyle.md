---
title: CounterItem.LineStyle property
description: Retrieves or sets the line style used to graph the counter value.
ms.assetid: 5801f0f8-37e5-4b15-a13f-24c71fea550d
keywords:
- LineStyle property SysMon
- LineStyle property SysMon , CounterItem class
- CounterItem class SysMon , LineStyle property
topic_type:
- apiref
api_name:
- CounterItem.LineStyle
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CounterItem.LineStyle property

Retrieves or sets the line style used to graph the counter value.

This property is read/write.

## Syntax


```VB
Property LineStyle As Long
```



## Property value

The line style used to graph the counter value. The values correspond to system constants shown in the following table.



| Value                                                                                                                                                                                                                                                                                                                                                                               | Meaning                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span id="System.Drawing.Drawing2D.DashStyle.Solid"></span><span id="system.drawing.drawing2d.dashstyle.solid"></span><span id="SYSTEM.DRAWING.DRAWING2D.DASHSTYLE.SOLID"></span><dl> <dt>**System.Drawing.Drawing2D.DashStyle.Solid**</dt> <dt>0</dt> </dl>                     | Solid line. This is the default value.<br/>                |
| <span id="System.Drawing.Drawing2D.DashStyle.Dash"></span><span id="system.drawing.drawing2d.dashstyle.dash"></span><span id="SYSTEM.DRAWING.DRAWING2D.DASHSTYLE.DASH"></span><dl> <dt>**System.Drawing.Drawing2D.DashStyle.Dash**</dt> <dt>1</dt> </dl>                         | Dotted line with long segments and narrow spaces.<br/>     |
| <span id="System.Drawing.Drawing2D.DashStyle.Dot"></span><span id="system.drawing.drawing2d.dashstyle.dot"></span><span id="SYSTEM.DRAWING.DRAWING2D.DASHSTYLE.DOT"></span><dl> <dt>**System.Drawing.Drawing2D.DashStyle.Dot**</dt> <dt>2</dt> </dl>                             | Dotted line with uniform segments and spaces.<br/>         |
| <span id="System.Drawing.Drawing2D.DashStyle.DashDot"></span><span id="system.drawing.drawing2d.dashstyle.dashdot"></span><span id="SYSTEM.DRAWING.DRAWING2D.DASHSTYLE.DASHDOT"></span><dl> <dt>**System.Drawing.Drawing2D.DashStyle.DashDot**</dt> <dt>3</dt> </dl>             | Dotted line with alternating short and long segments.<br/> |
| <span id="System.Drawing.Drawing2D.DashStyle.DashDotDot"></span><span id="system.drawing.drawing2d.dashstyle.dashdotdot"></span><span id="SYSTEM.DRAWING.DRAWING2D.DASHSTYLE.DASHDOTDOT"></span><dl> <dt>**System.Drawing.Drawing2D.DashStyle.DashDotDot**</dt> <dt>4</dt> </dl> | Dotted line with alternating dashes and double dots.<br/>  |



 

## Exceptions



| Exception type               | Condition                              |
|------------------------------|----------------------------------------|
| **System.ArgumentException** | The specified line style is not valid. |



 

## Remarks

To specify a value other than DashStyle.Solid, [**CounterItem.Width**](counteritem-width.md) must be set to 1. If the width is greater than 1, SYSMON ignores the specified line style and uses DashStyle.Solid.

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

 

 





