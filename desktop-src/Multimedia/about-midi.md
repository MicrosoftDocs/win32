---
title: About MIDI
description: About MIDI
ms.assetid: 32030c98-e513-4ee3-bbd0-ba41fceadd57
keywords:
- Windows multimedia,Musical Instrument Digital Interface (MIDI)
- multimedia,Musical Instrument Digital Interface (MIDI)
- multimedia audio,Musical Instrument Digital Interface (MIDI)
- audio,Musical Instrument Digital Interface (MIDI)
- Musical Instrument Digital Interface (MIDI),about
- MIDI (Musical Instrument Digital Interface),about
- Musical Instrument Digital Interface (MIDI),Media Control Interface (MCI)
- MIDI (Musical Instrument Digital Interface),Media Control Interface (MCI)
- Musical Instrument Digital Interface (MIDI),stream buffers
- MIDI (Musical Instrument Digital Interface),stream buffers
- Musical Instrument Digital Interface (MIDI),MIDI services
- MIDI (Musical Instrument Digital Interface),MIDI services
- Media Control Interface (MCI),Musical Instrument Digital Interface (MIDI)
- MCI (Media Control Interface),Musical Instrument Digital Interface (MIDI)
- stream buffers,about
- MIDI services,about
ms.topic: article
ms.date: 05/31/2018
---

# About MIDI

The Microsoft Win32 application programming interface (API) provides the following methods for applications to work with MIDI data:

-   The Media Control Interface (MCI). Although the simplest way to play a MIDI file is to use the MCIWnd window class, you can also use MCI commands to create a customized interface to a MIDI device. For more information about the MCIWnd window class, see [MCIWnd Window Class](mciwnd-window-class.md). For more information about MCI, see [MCI](mci.md), or [Media Control Interface (MCI)](media-control-interface--mci.md).
-   [Stream Buffers](stream-buffers.md). This format allows an application to manipulate buffers of time-stamped MIDI data for playback. Stream buffers are useful to applications that require more precise control over output than MCI offers.
-   [MIDI Services](midi-services.md). Applications that need the most precise control of MIDI data typically use these low-level services.

The following topics discuss each of these methods and provides an overview of the MIDI Mapper.

-   [The MIDI Mapper](the-midi-mapper.md)
-   [Media Control Interface (MCI)](media-control-interface--mci.md)
-   [Stream Buffers](stream-buffers.md)
-   [MIDI Services](midi-services.md)
-   [Playing MIDI Files](playing-midi-files.md)
-   [Recording MIDI Audio](recording-midi-audio.md)
-   [Processing MIDI Data from Two MIDI Sources](processing-midi-data-from-two-midi-sources.md)
-   [Creating MIDI Files](creating-midi-files.md)

 

 




