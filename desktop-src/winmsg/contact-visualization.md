---
Description: The following constants are used by applications or UI frameworks to identify how UI feedback is processed when an input contact is detected.
ms.assetid: 6FE8444C-A575-4E89-86D1-1873206688F5
title: Contact Visualization
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Contact Visualization

The following constants are used by applications or UI frameworks to identify how UI feedback is processed when an input contact is detected.

These constants are used with the **SPI\_GETCONTACTVISUALIZATION** and **SPI\_SETCONTACTVISUALIZATION** parameters and the [**SystemParametersInfo**](systemparametersinfo.md) function.

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



|                                     |                                                                                      |
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

[**SystemParametersInfo**](systemparametersinfo.md)
</dt> <dt>

[Input Feedback Configuration](https://msdn.microsoft.com/library/windows/desktop/hh707352)
</dt> </dl>

 

 




