---
title: MIDI Reference
description: MIDI Reference
ms.assetid: 6229a4a7-be42-4e2a-af9d-695c4759a4ef
keywords:
- Windows multimedia,Musical Instrument Digital Interface (MIDI)
- multimedia,Musical Instrument Digital Interface (MIDI)
- multimedia audio,Musical Instrument Digital Interface (MIDI)
- audio,Musical Instrument Digital Interface (MIDI)
- Windows multimedia,MIDI reference
- multimedia,MIDI reference
- multimedia audio,MIDI reference
- audio,MIDI reference
- Musical Instrument Digital Interface (MIDI),reference
- MIDI (Musical Instrument Digital Interface),reference
- reference for MIDI,about
- MIDI reference,about
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MIDI Reference

This section describes the functions, macros, messages, and structures associated with the Musical Instrument Digital Interface (MIDI). These elements are grouped as follows.

## Allocating and Managing Buffers

-   [**MIDIHDR**](https://msdn.microsoft.com/en-us/library/Dd798449(v=VS.85).aspx)
-   [**midiInAddBuffer**](https://msdn.microsoft.com/en-us/library/Dd798450(v=VS.85).aspx)
-   [**midiInPrepareHeader**](https://msdn.microsoft.com/en-us/library/Dd798459(v=VS.85).aspx)
-   [**midiInUnprepareHeader**](https://msdn.microsoft.com/en-us/library/Dd798464(v=VS.85).aspx)
-   [**midiOutPrepareHeader**](https://msdn.microsoft.com/en-us/library/Dd798477(v=VS.85).aspx)
-   [**midiOutUnprepareHeader**](https://msdn.microsoft.com/en-us/library/Dd798482(v=VS.85).aspx)

## Callback Functions

-   [**MidiInProc**](https://msdn.microsoft.com/en-us/library/Dd798460(v=VS.85).aspx)
-   [**MidiOutProc**](https://msdn.microsoft.com/en-us/library/Dd798478(v=VS.85).aspx)

## Device Capabilities

-   [**MIDIINCAPS**](https://msdn.microsoft.com/en-us/library/Dd798451(v=VS.85).aspx)
-   [**midiInGetDevCaps**](https://msdn.microsoft.com/en-us/library/Dd798453(v=VS.85).aspx)
-   [**midiInGetID**](https://msdn.microsoft.com/en-us/library/Dd798455(v=VS.85).aspx)
-   [**midiInGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd798456(v=VS.85).aspx)
-   [**MIDIOUTCAPS**](https://msdn.microsoft.com/en-us/library/Dd798467(v=VS.85).aspx)
-   [**midiOutGetDevCaps**](https://msdn.microsoft.com/en-us/library/Dd798469(v=VS.85).aspx)
-   [**midiOutGetID**](https://msdn.microsoft.com/en-us/library/Dd798471(v=VS.85).aspx)
-   [**midiOutGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd798472(v=VS.85).aspx)
-   [**MIDISTRMBUFFVER**](https://msdn.microsoft.com/en-us/library/Dd798493(v=VS.85).aspx)

## Error Processing

-   [**midiInGetErrorText**](https://msdn.microsoft.com/en-us/library/Dd798454(v=VS.85).aspx)
-   [**midiOutGetErrorText**](https://msdn.microsoft.com/en-us/library/Dd798470(v=VS.85).aspx)
-   [**MIM\_ERROR**](mim-error.md)
-   [**MIM\_LONGERROR**](mim-longerror.md)
-   [**MM\_MIM\_ERROR**](mm-mim-error.md)
-   [**MM\_MIM\_LONGERROR**](mm-mim-longerror.md)

## Managing MIDI Streams

-   [**midiStreamClose**](https://msdn.microsoft.com/en-us/library/Dd798485(v=VS.85).aspx)
-   [**midiStreamOpen**](https://msdn.microsoft.com/en-us/library/Dd798486(v=VS.85).aspx)
-   [**midiStreamOut**](https://msdn.microsoft.com/en-us/library/Dd798487(v=VS.85).aspx)
-   [**midiStreamPause**](https://msdn.microsoft.com/en-us/library/Dd798488(v=VS.85).aspx)
-   [**midiStreamPosition**](https://msdn.microsoft.com/en-us/library/Dd798489(v=VS.85).aspx)
-   [**midiStreamProperty**](https://msdn.microsoft.com/en-us/library/Dd798490(v=VS.85).aspx)
-   [**midiStreamRestart**](https://msdn.microsoft.com/en-us/library/Dd798491(v=VS.85).aspx)
-   [**midiStreamStop**](https://msdn.microsoft.com/en-us/library/Dd798492(v=VS.85).aspx)

## Opening and Closing Devices

-   [**midiInClose**](https://msdn.microsoft.com/en-us/library/Dd798452(v=VS.85).aspx)
-   [**midiInOpen**](https://msdn.microsoft.com/en-us/library/Dd798458(v=VS.85).aspx)
-   [**midiOutClose**](https://msdn.microsoft.com/en-us/library/Dd798468(v=VS.85).aspx)
-   [**midiOutOpen**](https://msdn.microsoft.com/en-us/library/Dd798476(v=VS.85).aspx)
-   [**MIM\_CLOSE**](mim-close.md)
-   [**MIM\_OPEN**](mim-open.md)
-   [**MM\_MIM\_CLOSE**](mm-mim-close.md)
-   [**MM\_MIM\_OPEN**](mm-mim-open.md)
-   [**MM\_MOM\_CLOSE**](mm-mom-close.md)
-   [**MM\_MOM\_OPEN**](mm-mom-open.md)
-   [**MOM\_CLOSE**](mom-close.md)
-   [**MOM\_OPEN**](mom-open.md)

## Output Devices

-   [KEYARRAY](keyarray.md)
-   [**midiOutCacheDrumPatches**](https://msdn.microsoft.com/en-us/library/Dd798465(v=VS.85).aspx)
-   [**midiOutCachePatches**](https://msdn.microsoft.com/en-us/library/Dd798466(v=VS.85).aspx)
-   [**midiOutGetVolume**](https://msdn.microsoft.com/en-us/library/Dd798473(v=VS.85).aspx)
-   [**midiOutSetVolume**](https://msdn.microsoft.com/en-us/library/Dd798480(v=VS.85).aspx)
-   [PATCHARRAY](patcharray.md)

## Playing a Message or Messages

-   [**MEVT\_EVENTPARM**](https://msdn.microsoft.com/en-us/library/Dd798441(v=VS.85).aspx)
-   [**MEVT\_EVENTTYPE**](https://msdn.microsoft.com/en-us/library/Dd798442(v=VS.85).aspx)
-   [**MIDIEVENT**](https://msdn.microsoft.com/en-us/library/Dd798448(v=VS.85).aspx)
-   [**midiOutLongMsg**](https://msdn.microsoft.com/en-us/library/Dd798474(v=VS.85).aspx)
-   [**midiOutReset**](https://msdn.microsoft.com/en-us/library/Dd798479(v=VS.85).aspx)
-   [**midiOutShortMsg**](https://msdn.microsoft.com/en-us/library/Dd798481(v=VS.85).aspx)
-   [**midiStreamOut**](https://msdn.microsoft.com/en-us/library/Dd798487(v=VS.85).aspx)
-   [**midiStreamPause**](https://msdn.microsoft.com/en-us/library/Dd798488(v=VS.85).aspx)
-   [**midiStreamRestart**](https://msdn.microsoft.com/en-us/library/Dd798491(v=VS.85).aspx)
-   [**midiStreamStop**](https://msdn.microsoft.com/en-us/library/Dd798492(v=VS.85).aspx)
-   [**MM\_MOM\_DONE**](mm-mom-done.md)
-   [**MM\_MOM\_POSITIONCB**](mm-mom-positioncb.md)
-   [**MOM\_DONE**](mom-done.md)
-   [**MOM\_POSITIONCB**](mom-positioncb.md)

## Recording

-   [**midiConnect**](https://msdn.microsoft.com/en-us/library/Dd798446(v=VS.85).aspx)
-   [**midiDisconnect**](https://msdn.microsoft.com/en-us/library/Dd798447(v=VS.85).aspx)
-   [**midiInReset**](https://msdn.microsoft.com/en-us/library/Dd798461(v=VS.85).aspx)
-   [**midiInStart**](https://msdn.microsoft.com/en-us/library/Dd798462(v=VS.85).aspx)
-   [**midiInStop**](https://msdn.microsoft.com/en-us/library/Dd798463(v=VS.85).aspx)
-   [**MIDIPROPTEMPO**](https://msdn.microsoft.com/en-us/library/Dd798483(v=VS.85).aspx)
-   [**MIDIPROPTIMEDIV**](https://msdn.microsoft.com/en-us/library/Dd798484(v=VS.85).aspx)
-   [**MIM\_DATA**](mim-data.md)
-   [**MIM\_LONGDATA**](mim-longdata.md)
-   [**MIM\_MOREDATA**](mim-moredata.md)
-   [**MM\_MIM\_DATA**](mm-mim-data.md)
-   [**MM\_MIM\_MOREDATA**](mm-mim-moredata.md)
-   [**MM\_MIM\_LONGDATA**](mm-mim-longdata.md)

## Sending Messages to Devices

-   [**midiInMessage**](https://msdn.microsoft.com/en-us/library/Dd798457(v=VS.85).aspx)
-   [**midiOutMessage**](https://msdn.microsoft.com/en-us/library/Dd798475(v=VS.85).aspx)

## Related topics

<dl> <dt>

[Musical Instrument Digital Interface (MIDI)](musical-instrument-digital-interface--midi.md)
</dt> </dl>

 

 




