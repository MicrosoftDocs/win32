---
title: Stream Buffer Format
description: Stream Buffer Format
ms.assetid: 4b24c12e-b43f-492e-a000-af4f59d5e16f
keywords:
- Musical Instrument Digital Interface (MIDI),stream buffers
- MIDI (Musical Instrument Digital Interface),stream buffers
- stream buffers,format
- MIDIHDR structure
- MIDIEVENT structure
ms.topic: article
ms.date: 05/31/2018
---

# Stream Buffer Format

The **lpData** member of the [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure points to a stream buffer, and the **dwBufferLength** member specifies the actual size of this buffer. The **dwBytesRecorded** member of **MIDIHDR** specifies the number of bytes in the buffer that are actually used by the MIDI events; this value must be less than or equal to the value specified by **dwBufferLength**.

Each of the MIDI events in the stream buffer is specified by a [**MIDIEVENT**](/windows/win32/api/mmeapi/ns-mmeapi-midievent) structure, which contains the time for the event, a stream identifier, an event code, and, when appropriate, parameters for the event. Each of these **MIDIEVENT** structures must begin on a doubleword boundary. If necessary, pad bytes must be added to the end of the structure to ensure that the next one starts on a doubleword boundary.

 

 