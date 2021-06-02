---
description: The following constants are used by applications or UI frameworks to identify how UI feedback is processed when one of the listed gestures is detected.
ms.assetid: 76D3DFF4-7BB2-49A9-8251-0B5D9376B649
title: Gesture Visualization (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Gesture Visualization

The following constants are used by applications or UI frameworks to identify how UI feedback is processed when one of the listed gestures is detected.

These constants are used with the **SPI\_GETGESTUREVISUALIZATION** and **SPI\_SETGESTUREVISUALIZATION** parameters and the [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) function.

**Note**  

For retrieving or setting pen visualization info, we recommend that you use the **SPI\_GETPENVISUALIZATION** and **SPI\_SETPENVISUALIZATION** parameters and the constants listed in [**Pen Visualization**](pen-visualization.md).

<dl> <dt>

<span id="GESTUREVISUALIZATION_OFF"></span><span id="gesturevisualization_off"></span>**GESTUREVISUALIZATION\_OFF**
</dt> <dd> <dl> <dt>

0x0000
</dt> <dt>



Specifies that UI feedback for all gestures is off.


</dt> </dl> </dd> <dt>

<span id="GESTUREVISUALIZATION_ON"></span><span id="gesturevisualization_on"></span>**GESTUREVISUALIZATION\_ON**
</dt> <dd> <dl> <dt>

0x001F
</dt> <dt>



Specifies that UI feedback for all gestures is on.


</dt> </dl> </dd> <dt>

<span id="GESTUREVISUALIZATION_TAP"></span><span id="gesturevisualization_tap"></span>**GESTUREVISUALIZATION\_TAP**
</dt> <dd> <dl> <dt>

0x0001
</dt> <dt>



Specifies UI feedback for a tap.


</dt> </dl> </dd> <dt>

<span id="GESTUREVISUALIZATION_DOUBLETAP"></span><span id="gesturevisualization_doubletap"></span>**GESTUREVISUALIZATION\_DOUBLETAP**
</dt> <dd> <dl> <dt>

0x0002
</dt> <dt>



Specifies UI feedback for a double tap.


</dt> </dl> </dd> <dt>

<span id="GESTUREVISUALIZATION_PRESSANDTAP"></span><span id="gesturevisualization_pressandtap"></span>**GESTUREVISUALIZATION\_PRESSANDTAP**
</dt> <dd> <dl> <dt>

0x0004
</dt> <dt>



Specifies UI feedback for a press and tap.


</dt> </dl> </dd> <dt>

<span id="GESTUREVISUALIZATION_PRESSANDHOLD"></span><span id="gesturevisualization_pressandhold"></span>**GESTUREVISUALIZATION\_PRESSANDHOLD**
</dt> <dd> <dl> <dt>

0x0008
</dt> <dt>



Specifies UI feedback for a press and hold.


</dt> </dl> </dd> <dt>

<span id="GESTUREVISUALIZATION_RIGHTTAP"></span><span id="gesturevisualization_righttap"></span>**GESTUREVISUALIZATION\_RIGHTTAP**
</dt> <dd> <dl> <dt>

0x0010
</dt> <dt>



Specifies UI feedback for a right tap.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                 |
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

 

