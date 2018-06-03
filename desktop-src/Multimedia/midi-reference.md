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

-   [**MIDIHDR**](https://www.bing.com/search?q=**MIDIHDR**)
-   [**midiInAddBuffer**](https://www.bing.com/search?q=**midiInAddBuffer**)
-   [**midiInPrepareHeader**](https://www.bing.com/search?q=**midiInPrepareHeader**)
-   [**midiInUnprepareHeader**](https://www.bing.com/search?q=**midiInUnprepareHeader**)
-   [**midiOutPrepareHeader**](https://www.bing.com/search?q=**midiOutPrepareHeader**)
-   [**midiOutUnprepareHeader**](https://www.bing.com/search?q=**midiOutUnprepareHeader**)

## Callback Functions

-   [**MidiInProc**](/windows/desktop/api/Mmsystem/)
-   [**MidiOutProc**](/windows/desktop/api/Mmsystem/)

## Device Capabilities

-   [**MIDIINCAPS**](https://www.bing.com/search?q=**MIDIINCAPS**)
-   [**midiInGetDevCaps**](https://www.bing.com/search?q=**midiInGetDevCaps**)
-   [**midiInGetID**](https://www.bing.com/search?q=**midiInGetID**)
-   [**midiInGetNumDevs**](https://www.bing.com/search?q=**midiInGetNumDevs**)
-   [**MIDIOUTCAPS**](https://www.bing.com/search?q=**MIDIOUTCAPS**)
-   [**midiOutGetDevCaps**](https://www.bing.com/search?q=**midiOutGetDevCaps**)
-   [**midiOutGetID**](https://www.bing.com/search?q=**midiOutGetID**)
-   [**midiOutGetNumDevs**](https://www.bing.com/search?q=**midiOutGetNumDevs**)
-   [**MIDISTRMBUFFVER**](https://www.bing.com/search?q=**MIDISTRMBUFFVER**)

## Error Processing

-   [**midiInGetErrorText**](https://www.bing.com/search?q=**midiInGetErrorText**)
-   [**midiOutGetErrorText**](https://www.bing.com/search?q=**midiOutGetErrorText**)
-   [**MIM\_ERROR**](mim-error.md)
-   [**MIM\_LONGERROR**](mim-longerror.md)
-   [**MM\_MIM\_ERROR**](mm-mim-error.md)
-   [**MM\_MIM\_LONGERROR**](mm-mim-longerror.md)

## Managing MIDI Streams

-   [**midiStreamClose**](https://www.bing.com/search?q=**midiStreamClose**)
-   [**midiStreamOpen**](https://www.bing.com/search?q=**midiStreamOpen**)
-   [**midiStreamOut**](https://www.bing.com/search?q=**midiStreamOut**)
-   [**midiStreamPause**](https://www.bing.com/search?q=**midiStreamPause**)
-   [**midiStreamPosition**](https://www.bing.com/search?q=**midiStreamPosition**)
-   [**midiStreamProperty**](https://www.bing.com/search?q=**midiStreamProperty**)
-   [**midiStreamRestart**](https://www.bing.com/search?q=**midiStreamRestart**)
-   [**midiStreamStop**](https://www.bing.com/search?q=**midiStreamStop**)

## Opening and Closing Devices

-   [**midiInClose**](https://www.bing.com/search?q=**midiInClose**)
-   [**midiInOpen**](https://www.bing.com/search?q=**midiInOpen**)
-   [**midiOutClose**](https://www.bing.com/search?q=**midiOutClose**)
-   [**midiOutOpen**](https://www.bing.com/search?q=**midiOutOpen**)
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
-   [**midiOutCacheDrumPatches**](https://www.bing.com/search?q=**midiOutCacheDrumPatches**)
-   [**midiOutCachePatches**](https://www.bing.com/search?q=**midiOutCachePatches**)
-   [**midiOutGetVolume**](https://www.bing.com/search?q=**midiOutGetVolume**)
-   [**midiOutSetVolume**](https://www.bing.com/search?q=**midiOutSetVolume**)
-   [PATCHARRAY](patcharray.md)

## Playing a Message or Messages

-   [**MEVT\_EVENTPARM**](https://www.bing.com/search?q=**MEVT\_EVENTPARM**)
-   [**MEVT\_EVENTTYPE**](https://www.bing.com/search?q=**MEVT\_EVENTTYPE**)
-   [**MIDIEVENT**](https://www.bing.com/search?q=**MIDIEVENT**)
-   [**midiOutLongMsg**](https://www.bing.com/search?q=**midiOutLongMsg**)
-   [**midiOutReset**](https://www.bing.com/search?q=**midiOutReset**)
-   [**midiOutShortMsg**](https://www.bing.com/search?q=**midiOutShortMsg**)
-   [**midiStreamOut**](https://www.bing.com/search?q=**midiStreamOut**)
-   [**midiStreamPause**](https://www.bing.com/search?q=**midiStreamPause**)
-   [**midiStreamRestart**](https://www.bing.com/search?q=**midiStreamRestart**)
-   [**midiStreamStop**](https://www.bing.com/search?q=**midiStreamStop**)
-   [**MM\_MOM\_DONE**](mm-mom-done.md)
-   [**MM\_MOM\_POSITIONCB**](mm-mom-positioncb.md)
-   [**MOM\_DONE**](mom-done.md)
-   [**MOM\_POSITIONCB**](mom-positioncb.md)

## Recording

-   [**midiConnect**](https://www.bing.com/search?q=**midiConnect**)
-   [**midiDisconnect**](https://www.bing.com/search?q=**midiDisconnect**)
-   [**midiInReset**](https://www.bing.com/search?q=**midiInReset**)
-   [**midiInStart**](https://www.bing.com/search?q=**midiInStart**)
-   [**midiInStop**](https://www.bing.com/search?q=**midiInStop**)
-   [**MIDIPROPTEMPO**](https://www.bing.com/search?q=**MIDIPROPTEMPO**)
-   [**MIDIPROPTIMEDIV**](https://www.bing.com/search?q=**MIDIPROPTIMEDIV**)
-   [**MIM\_DATA**](mim-data.md)
-   [**MIM\_LONGDATA**](mim-longdata.md)
-   [**MIM\_MOREDATA**](mim-moredata.md)
-   [**MM\_MIM\_DATA**](mm-mim-data.md)
-   [**MM\_MIM\_MOREDATA**](mm-mim-moredata.md)
-   [**MM\_MIM\_LONGDATA**](mm-mim-longdata.md)

## Sending Messages to Devices

-   [**midiInMessage**](https://www.bing.com/search?q=**midiInMessage**)
-   [**midiOutMessage**](https://www.bing.com/search?q=**midiOutMessage**)

## Related topics

<dl> <dt>

[Musical Instrument Digital Interface (MIDI)](musical-instrument-digital-interface--midi.md)
</dt> </dl>

 

 




