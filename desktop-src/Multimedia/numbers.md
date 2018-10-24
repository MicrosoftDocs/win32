---
title: Numbers
description: Numbers
ms.assetid: d416c4c2-a3e1-45a2-9ae1-82050a5e471b
keywords:
- audio mixers,controls
- audio mixers,numbers
- mixers,controls
- mixers,numbers
- number controls
- MIXERCONTROLDETAILS_SIGNED structure
- MIXERCONTROLDETAILS_UNSIGNED structure
- decibel control
- percent control
- signed control
- unsigned control
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Numbers

The number controls allow the user to enter numerical data associated with a line. The numerical data is expressed as signed integers, unsigned integers, or integer decibel values. These controls use the [**MIXERCONTROLDETAILS\_SIGNED**](https://msdn.microsoft.com/en-us/library/Dd757297(v=VS.85).aspx) and [**MIXERCONTROLDETAILS\_UNSIGNED**](https://msdn.microsoft.com/en-us/library/Dd757298(v=VS.85).aspx) structures to retrieve and set control properties. The following table describes the types of number controls.



| Control  | Description                                                                                                                         |
|----------|-------------------------------------------------------------------------------------------------------------------------------------|
| Signed   | Allows integer values entered in the range of – 231 through (231 –1).                                                               |
| Unsigned | Allows integer values entered in the range of 0 through (232 –1).                                                                   |
| Decibel  | Allows integer decibel values to be entered, in tenths of decibels. The range of values for this control is –32,768 through 32,767. |
| Percent  | Allows values to be entered as percentages.                                                                                         |



 

 

 




