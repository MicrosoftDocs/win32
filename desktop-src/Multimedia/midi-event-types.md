---
title: MIDI Event Types
description: MIDI Event Types
ms.assetid: 0b0984b7-3087-461e-90f2-a899dc1a88c6
keywords:
- Musical Instrument Digital Interface (MIDI),event types
- MIDI (Musical Instrument Digital Interface),event types
- MIDIEVENT structure
- stream buffers,MIDI event types
- MIDI event types
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MIDI Event Types

The **dwEvent** member of the [**MIDIEVENT**](https://msdn.microsoft.com/en-us/library/Dd798448(v=VS.85).aspx) structure describes the MIDI event that is to take place. Short events fit entirely into this member. Long events require one or more doubleword values in addition to the **dwEvent** member to store the event descriptions.

The high byte of the **dwEvent** member contains information about whether the event is long or short and about whether a callback is generated along with the event. In addition, this byte is used to describe the event type. The remaining 24 bits of the **dwEvent** member are used either to contain the event parameters (for short messages) or to contain the length of the event parameters (for long messages). To extract information from the **dwEvent** member, use the [**MEVT\_EVENTTYPE**](https://msdn.microsoft.com/en-us/library/Dd798442(v=VS.85).aspx) and [**MEVT\_EVENTPARM**](https://msdn.microsoft.com/en-us/library/Dd798441(v=VS.85).aspx) macros.

For a description of the predefined event types, see the reference material for the **MIDIEVENT** structure.

 

 




