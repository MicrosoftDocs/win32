---
title: Numbers (Windows Multimedia)
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
ms.topic: article
ms.date: 05/31/2018
---

# Numbers (Windows Multimedia)

The number controls allow the user to enter numerical data associated with a line. The numerical data is expressed as signed integers, unsigned integers, or integer decibel values. These controls use the [**MIXERCONTROLDETAILS\_SIGNED**](/previous-versions//dd757297(v=vs.85)) and [**MIXERCONTROLDETAILS\_UNSIGNED**](/previous-versions//dd757298(v=vs.85)) structures to retrieve and set control properties. The following table describes the types of number controls.



| Control  | Description                                                                                                                         |
|----------|-------------------------------------------------------------------------------------------------------------------------------------|
| Signed   | Allows integer values entered in the range of – 231 through (231 –1).                                                               |
| Unsigned | Allows integer values entered in the range of 0 through (232 –1).                                                                   |
| Decibel  | Allows integer decibel values to be entered, in tenths of decibels. The range of values for this control is –32,768 through 32,767. |
| Percent  | Allows values to be entered as percentages.                                                                                         |



 

 

 
