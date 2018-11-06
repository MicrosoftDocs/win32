---
title: The Volume Scalar
description: The Volume Scalar
ms.assetid: a9fe2c35-9109-4697-9ffa-a31debbe72c8
keywords:
- Musical Instrument Digital Interface (MIDI),volume scalar
- MIDI (Musical Instrument Digital Interface),volume scalar
- MIDI Mapper,volume scalar
- volume scalar
- MIDI Mapper,adjusting output levels
- adjusting output levels
ms.topic: article
ms.date: 05/31/2018
---

# The Volume Scalar

The purpose of the volume scalar is to allow adjustments between the relative output levels of different patches on a synthesizer. For example, if the bass patch on a synthesizer is too loud compared with its piano patch, you can change the setup map to scale the bass volume down or the piano volume up.

The volume scalar specifies a percentage value for changing all MIDI main-volume controller messages that follow an associated program-change message. For example, if the volume scalar value is 50%, the MIDI Mapper modifies MIDI main-volume controller messages as shown in the following illustration.

![midi mapper image](images/mmap-a04.gif)

 

 




