---
title: Authoring Guidelines for MIDI Files
description: Authoring Guidelines for MIDI Files
ms.assetid: 57e3d260-d275-4b0c-9db0-d036dd12fdb8
keywords:
- Musical Instrument Digital Interface (MIDI),file authoring guidelines
- MIDI (Musical Instrument Digital Interface),file authoring guidelines
- creating MIDI files,file authoring guidelines
- standard MIDI patch assignments
- standard MIDI key assignments
- Musical Instrument Digital Interface (MIDI),standard patch assignments
- MIDI (Musical Instrument Digital Interface),standard patch assignments
- Musical Instrument Digital Interface (MIDI),standard key assignments
- MIDI (Musical Instrument Digital Interface),standard key assignments
- creating MIDI files,standard patch assignments
- creating MIDI files,standard key assignments
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Guidelines for MIDI Files

Follow these guidelines to author device-independent MIDI files for Windows:

-   Use the [Standard MIDI Patch Assignments](standard-midi-patch-assignments.md) and [Standard MIDI Key Assignments](standard-midi-key-assignments.md).
-   Always send a program-change message to a channel to select a patch before sending other messages to that channel. For the two percussion channels (10 and 16), select program number 0.
-   Always follow a MIDI program-change message with a MIDI main-volume controller message (controller number 7) to set the relative volume of the patch.
-   Use a value of 80 (0x50) for the main-volume controller for normal listening levels. For quieter or louder levels, you can use lower or higher values.
-   Use only the following MIDI messages: note-on with velocity, note-off, program change, pitch bend, main volume (controller 7), and damper pedal (controller 64). Internal synthesizers are required to respond to these messages and most MIDI musical instruments respond to them as well.

 

 




