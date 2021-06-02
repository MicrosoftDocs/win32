---
title: Sliders (Windows Multimedia)
description: Sliders
ms.assetid: cfd82672-5b22-4b59-82b5-15ca68a451fc
keywords:
- audio mixers,controls
- audio mixers,sliders
- mixers,controls
- mixers,sliders
- slider controls
- MIXERCONTROLDETAILS_SIGNED structure
- pan control
- QSound pan control
ms.topic: article
ms.date: 05/31/2018
---

# Sliders (Windows Multimedia)

The slider controls are typically horizontal controls that can be adjusted to the left or right. These controls use the [**MIXERCONTROLDETAILS\_SIGNED**](/previous-versions//dd757297(v=vs.85)) structure to retrieve and set control properties. The following table describes the types of sliders.



| Control    | Description                                                                                                               |
|------------|---------------------------------------------------------------------------------------------------------------------------|
| Slider     | Has a range of –32,768 through 32,767. The mixer driver defines the limits of this control.                               |
| Pan        | Has a range of –32,768 through 32,767. The mixer driver defines the limits of this control, with 0 as the midrange value. |
| QSound Pan | Provides expanded sound control through QSound. This control has a range of –15 through 15.                               |



 

 

 
