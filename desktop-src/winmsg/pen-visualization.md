---
description: The following constants are used by applications or UI frameworks to identify how UI feedback is processed when one of the listed pen gestures is detected.
ms.assetid: 434DC272-DC1C-4091-BB38-DDCB1A635D8D
title: Pen Visualization (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Pen Visualization

The following constants are used by applications or UI frameworks to identify how UI feedback is processed when one of the listed pen gestures is detected.

These constants are used with the **SPI\_GETPENVISUALIZATION** and **SPI\_SETPENVISUALIZATION** parameters and the [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) function.

<dl> <dt>

<span id="PENVISUALIZATION_OFF"></span><span id="penvisualization_off"></span>**PENVISUALIZATION\_OFF**
</dt> <dd> <dl> <dt>

0x0000
</dt> <dt>



Specifies that UI feedback for all pen gestures is off.


</dt> </dl> </dd> <dt>

<span id="PENVISUALIZATION_ON"></span><span id="penvisualization_on"></span>**PENVISUALIZATION\_ON**
</dt> <dd> <dl> <dt>

0x0023
</dt> <dt>



Specifies that UI feedback for all pen gestures is on.


</dt> </dl> </dd> <dt>

<span id="PENVISUALIZATION_TAP"></span><span id="penvisualization_tap"></span>**PENVISUALIZATION\_TAP**
</dt> <dd> <dl> <dt>

0x0001
</dt> <dt>



Specifies UI feedback for a pen tap.


</dt> </dl> </dd> <dt>

<span id="PENVISUALIZATION_DOUBLETAP"></span><span id="penvisualization_doubletap"></span>**PENVISUALIZATION\_DOUBLETAP**
</dt> <dd> <dl> <dt>

0x0002
</dt> <dt>



Specifies UI feedback for a pen double tap.


</dt> </dl> </dd> <dt>

<span id="PENVISUALIZATION_CURSOR"></span><span id="penvisualization_cursor"></span>**PENVISUALIZATION\_CURSOR**
</dt> <dd> <dl> <dt>

0x0020
</dt> <dt>



Specifies UI feedback for the pen cursor.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[Configuration Constants](configuration-constants.md)
</dt> <dt>

[**Contact Visualization**](contact-visualization.md)
</dt> <dt>

[**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa)
</dt> <dt>

[Input Feedback Configuration](/previous-versions/windows/desktop/input_feedback/input-feedback-configuration-portal)
</dt> </dl>

 

