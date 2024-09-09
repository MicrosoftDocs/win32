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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sliders (Windows Multimedia)

\[The feature associated with this page, [Audio Mixers](/windows/win32/multimedia/audio-mixers), is a legacy feature. It has been superseded by [Volume Controls](/windows/win32/coreaudio/volume-controls). **Volume Controls** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Volume Controls** instead of **Audio Mixers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The slider controls are typically horizontal controls that can be adjusted to the left or right. These controls use the [**MIXERCONTROLDETAILS\_SIGNED**](/previous-versions//dd757297(v=vs.85)) structure to retrieve and set control properties. The following table describes the types of sliders.



| Control    | Description                                                                                                               |
|------------|---------------------------------------------------------------------------------------------------------------------------|
| Slider     | Has a range of –32,768 through 32,767. The mixer driver defines the limits of this control.                               |
| Pan        | Has a range of –32,768 through 32,767. The mixer driver defines the limits of this control, with 0 as the midrange value. |
| QSound Pan | Provides expanded sound control through QSound. This control has a range of –15 through 15.                               |



 

 

 
