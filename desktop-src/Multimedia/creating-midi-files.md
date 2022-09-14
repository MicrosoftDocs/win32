---
title: Creating MIDI Files
description: Creating MIDI Files
ms.assetid: 2fca3b41-14f9-4eaf-9fdb-8f952c834302
keywords:
- Windows multimedia,creating MIDI files
- multimedia,creating MIDI files
- multimedia audio,creating MIDI files
- audio,creating MIDI files
- Musical Instrument Digital Interface (MIDI),creating files
- MIDI (Musical Instrument Digital Interface),creating files
- creating MIDI files,about
- MIDI Manufacturers Association (MMA)
- MMA (MIDI Manufacturers Association)
- MIDI Detailed specification
- Standard MIDI Files specification
- General MIDI (GM) specification
- GM (General MIDI) specification
ms.topic: article
ms.date: 05/31/2018
---

# Creating MIDI Files

The Musical Instrument Digital Interface (MIDI) specifications are published by and are copyrighted material of the MIDI Manufacturers Association (MMA). The following list describes the specifications which are of the greatest general interest:

## MIDI Detailed Specification

The MIDI Detailed Specification explains the MIDI hardware and software protocols. This is useful to those developing multimedia applications which implement MIDI support by using MIDI functions to record, edit, and/or play MIDI data.

## Standard MIDI Files 1.0

The Standard MIDI Files specification defines a way to interchange time-stamped MIDI data between different applications on the same or different hardware platforms. This is useful to developers writing applications that read and parse disk files containing MIDI data and/or write MIDI data files to disk.

## General MIDI System - Level 1

The General MIDI (GM) specification defines a minimum MIDI configuration of a "General MIDI System". This system consists of a specific class of MIDI playback devices and is of interest to multimedia developers who author MIDI files. Most PC sound cards and MIDI synthesizers manufactured today are compatible with the GM specification. MIDI files which are authored to the GM specification should generally sound as they were intended to sound, no matter which GM-compatible device they are played on.

To enable MIDI files to be a viable format for representing music in multimedia computing, Windows follows the General MIDI System Level 1 specification. The following topics provide additional MIDI authoring guidelines:

-   [Authoring Guidelines for MIDI Files](authoring-guidelines-for-midi-files.md)
-   [Standard MIDI Patch Assignments](standard-midi-patch-assignments.md)
-   [Standard MIDI Key Assignments](standard-midi-key-assignments.md)

 

 




