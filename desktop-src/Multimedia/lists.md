---
title: Lists
description: Lists
ms.assetid: 89fb4457-307a-4693-94d4-57f57c422d1e
keywords:
- audio mixers,controls
- audio mixers,lists
- mixers,controls
- mixers,lists
- list controls
- MIXERCONTROLDETAILS_BOOLEAN structure
- MIXERCONTROLDETAILS_LISTTEXT structure
- single-select control
- multiple-select control
- mixer control
- multiplexer (MUX)
- MUX (multiplexer)
ms.topic: article
ms.date: 05/31/2018
---

# Lists

The list controls provide single-select or multiple-select states for complex audio lines. These controls use the [**MIXERCONTROLDETAILS\_BOOLEAN**](/previous-versions//dd757295(v=vs.85)) structure to retrieve and set control properties. The [**MIXERCONTROLDETAILS\_LISTTEXT**](/previous-versions//dd757296(v=vs.85)) structure is also used to retrieve all text descriptions of a multiple-item control. The following table describes the types of list controls.



| Control           | Description                                                                                                                                                                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single-select     | Restricts the control selection to one item at a time. Unlike the multiplexer control, this control can be used to control more than audio source lines. For example, you could use this control to select a low-pass filter from a list of filters supported by a mixer device. |
| Multiplexer (MUX) | Restricts the line selection to one source line at a time.                                                                                                                                                                                                                       |
| Multiple-select   | Allows the user to select multiple items from a list simultaneously. Unlike the mixer control, the multiple-select control can be used to control more than audio source lines.                                                                                                  |
| Mixer             | Allows the user to select source lines from a list simultaneously.                                                                                                                                                                                                               |



 

 

 