---
title: SystemMonitor.Appearance property
description: Retrieves or sets the control's appearance to include or omit three-dimensional display effects.
ms.assetid: cbc1f17f-991a-4b35-9c64-7750a17b42c8
keywords:
- Appearance property SysMon
- Appearance property SysMon , SystemMonitor class
- SystemMonitor class SysMon , Appearance property
topic_type:
- apiref
api_name:
- SystemMonitor.Appearance
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.Appearance property

Retrieves or sets the control's appearance to include or omit three-dimensional display effects.

This property is read-only.

## Syntax


```VB
Property Appearance As Long
```



## Property value

Appearance value that determines if the control is painted with three-dimensional effects.

You can set this property to one of the following values.



| Value                                                                        | Meaning                                                                                  |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Paints the control without visual effects.<br/>                                    |
| <dl> <dt>1</dt> </dl> | Paints the control with three-dimensional effects. This is the default value.<br/> |



 

## Exceptions



| Exception type               | Condition                                    |
|------------------------------|----------------------------------------------|
| **System.ArgumentException** | The specified appearance value is not valid. |



 

## Remarks

This is an ambient property. The value of this property is determined by the container. Setting the value of this property could affect the illusion of the control and container being a single application.

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

 

 





