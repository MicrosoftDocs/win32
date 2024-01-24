---
description: The following constants are used by applications or UI frameworks to identify how UI feedback is processed when an input contact is detected.
ms.assetid: 6FE8444C-A575-4E89-86D1-1873206688F5
title: Contact Visualization (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Contact Visualization

The following constants are used by applications or UI frameworks to identify how UI feedback is processed when an input contact is detected.

These constants are used with the **SPI\_GETCONTACTVISUALIZATION** and **SPI\_SETCONTACTVISUALIZATION** parameters and the [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) function.

<dl> <dt>

<span id="CONTACTVISUALIZATION_OFF"></span><span id="contactvisualization_off"></span>**CONTACTVISUALIZATION\_OFF**
</dt> <dd> <dl> <dt>

0x0000
</dt> <dt>



Specifies UI feedback for all contacts is off.


</dt> </dl> </dd> <dt>

<span id="CONTACTVISUALIZATION_ON"></span><span id="contactvisualization_on"></span>**CONTACTVISUALIZATION\_ON**
</dt> <dd> <dl> <dt>

0x0001
</dt> <dt>



Specifies UI feedback for all contacts is on.


</dt> </dl> </dd> <dt>

<span id="CONTACTVISUALIZATION_PRESENTATIONMODE"></span><span id="contactvisualization_presentationmode"></span>**CONTACTVISUALIZATION\_PRESENTATIONMODE**
</dt> <dd> <dl> <dt>

0x0002
</dt> <dt>



Specifies UI feedback for all contacts is on with presentation mode visuals.


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

[**Gesture Visualization**](gesture-visualization.md)
</dt> <dt>

[**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa)
</dt> <dt>

[Input Feedback Configuration](/previous-versions/windows/desktop/input_feedback/input-feedback-configuration-portal)
</dt> </dl>

 

