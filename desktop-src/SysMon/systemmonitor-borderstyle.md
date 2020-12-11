---
title: SystemMonitor.BorderStyle property
description: Retrieves or sets the border style of the control.
ms.assetid: 9151a3f6-71fb-43ea-b7f6-cc35048145cb
keywords:
- BorderStyle property SysMon
- BorderStyle property SysMon , SystemMonitor class
- SystemMonitor class SysMon , BorderStyle property
topic_type:
- apiref
api_name:
- SystemMonitor.BorderStyle
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.BorderStyle property

Retrieves or sets the border style of the control.

This property is read-only.

## Syntax


```VB
Property BorderStyle As Long
```



## Property value

Border style of the control.

You can set this property to one of the following values.



| Value                                                                                                                                                                                                                                                                                                                                                                                                   | Meaning                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <span id="System.Windows.Forms.FormBorderStyle.VbBSNone"></span><span id="system.windows.forms.formborderstyle.vbbsnone"></span><span id="SYSTEM.WINDOWS.FORMS.FORMBORDERSTYLE.VBBSNONE"></span><dl> <dt>**System.Windows.Forms.FormBorderStyle.VbBSNone**</dt> <dt>0</dt> </dl>                     | No border. This is the default value.<br/> |
| <span id="System.Windows.Forms.FormBorderStyle.VbFixedSingle"></span><span id="system.windows.forms.formborderstyle.vbfixedsingle"></span><span id="SYSTEM.WINDOWS.FORMS.FORMBORDERSTYLE.VBFIXEDSINGLE"></span><dl> <dt>**System.Windows.Forms.FormBorderStyle.VbFixedSingle**</dt> <dt>1</dt> </dl> | Fixed, single border.<br/>                 |



 

## Exceptions



| Exception type               | Condition                                |
|------------------------------|------------------------------------------|
| **System.ArgumentException** | The specified border style is not valid. |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> </dl>

 

 





