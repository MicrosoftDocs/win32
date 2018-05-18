---
title: MIDI Reference
description: MIDI Reference
ms.assetid: '6229a4a7-be42-4e2a-af9d-695c4759a4ef'
keywords: ["Windows multimedia,Musical Instrument Digital Interface (MIDI)", "multimedia,Musical Instrument Digital Interface (MIDI)", "multimedia audio,Musical Instrument Digital Interface (MIDI)", "audio,Musical Instrument Digital Interface (MIDI)", "Windows multimedia,MIDI reference", "multimedia,MIDI reference", "multimedia audio,MIDI reference", "audio,MIDI reference", "Musical Instrument Digital Interface (MIDI),reference", "MIDI (Musical Instrument Digital Interface),reference", "reference for MIDI,about", "MIDI reference,about"]
---

# MIDI Reference

This section describes the functions, macros, messages, and structures associated with the Musical Instrument Digital Interface (MIDI). These elements are grouped as follows.

## Allocating and Managing Buffers

-   [**MIDIHDR**](midihdr.md)
-   [**midiInAddBuffer**](midiinaddbuffer.md)
-   [**midiInPrepareHeader**](midiinprepareheader.md)
-   [**midiInUnprepareHeader**](midiinunprepareheader.md)
-   [**midiOutPrepareHeader**](midioutprepareheader.md)
-   [**midiOutUnprepareHeader**](midioutunprepareheader.md)

## Callback Functions

-   [**MidiInProc**](midiinproc.md)
-   [**MidiOutProc**](midioutproc.md)

## Device Capabilities

-   [**MIDIINCAPS**](midiincaps.md)
-   [**midiInGetDevCaps**](midiingetdevcaps.md)
-   [**midiInGetID**](midiingetid.md)
-   [**midiInGetNumDevs**](midiingetnumdevs.md)
-   [**MIDIOUTCAPS**](midioutcaps.md)
-   [**midiOutGetDevCaps**](midioutgetdevcaps.md)
-   [**midiOutGetID**](midioutgetid.md)
-   [**midiOutGetNumDevs**](midioutgetnumdevs.md)
-   [**MIDISTRMBUFFVER**](midistrmbuffver.md)

## Error Processing

-   [**midiInGetErrorText**](midiingeterrortext.md)
-   [**midiOutGetErrorText**](midioutgeterrortext.md)
-   [**MIM\_ERROR**](mim-error.md)
-   [**MIM\_LONGERROR**](mim-longerror.md)
-   [**MM\_MIM\_ERROR**](mm-mim-error.md)
-   [**MM\_MIM\_LONGERROR**](mm-mim-longerror.md)

## Managing MIDI Streams

-   [**midiStreamClose**](midistreamclose.md)
-   [**midiStreamOpen**](midistreamopen.md)
-   [**midiStreamOut**](midistreamout.md)
-   [**midiStreamPause**](midistreampause.md)
-   [**midiStreamPosition**](midistreamposition.md)
-   [**midiStreamProperty**](midistreamproperty.md)
-   [**midiStreamRestart**](midistreamrestart.md)
-   [**midiStreamStop**](midistreamstop.md)

## Opening and Closing Devices

-   [**midiInClose**](midiinclose.md)
-   [**midiInOpen**](midiinopen.md)
-   [**midiOutClose**](midioutclose.md)
-   [**midiOutOpen**](midioutopen.md)
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
-   [**midiOutCacheDrumPatches**](midioutcachedrumpatches.md)
-   [**midiOutCachePatches**](midioutcachepatches.md)
-   [**midiOutGetVolume**](midioutgetvolume.md)
-   [**midiOutSetVolume**](midioutsetvolume.md)
-   [PATCHARRAY](patcharray.md)

## Playing a Message or Messages

-   [**MEVT\_EVENTPARM**](mevt-eventparm.md)
-   [**MEVT\_EVENTTYPE**](mevt-eventtype.md)
-   [**MIDIEVENT**](midievent.md)
-   [**midiOutLongMsg**](midioutlongmsg.md)
-   [**midiOutReset**](midioutreset.md)
-   [**midiOutShortMsg**](midioutshortmsg.md)
-   [**midiStreamOut**](midistreamout.md)
-   [**midiStreamPause**](midistreampause.md)
-   [**midiStreamRestart**](midistreamrestart.md)
-   [**midiStreamStop**](midistreamstop.md)
-   [**MM\_MOM\_DONE**](mm-mom-done.md)
-   [**MM\_MOM\_POSITIONCB**](mm-mom-positioncb.md)
-   [**MOM\_DONE**](mom-done.md)
-   [**MOM\_POSITIONCB**](mom-positioncb.md)

## Recording

-   [**midiConnect**](midiconnect.md)
-   [**midiDisconnect**](mididisconnect.md)
-   [**midiInReset**](midiinreset.md)
-   [**midiInStart**](midiinstart.md)
-   [**midiInStop**](midiinstop.md)
-   [**MIDIPROPTEMPO**](midiproptempo.md)
-   [**MIDIPROPTIMEDIV**](midiproptimediv.md)
-   [**MIM\_DATA**](mim-data.md)
-   [**MIM\_LONGDATA**](mim-longdata.md)
-   [**MIM\_MOREDATA**](mim-moredata.md)
-   [**MM\_MIM\_DATA**](mm-mim-data.md)
-   [**MM\_MIM\_MOREDATA**](mm-mim-moredata.md)
-   [**MM\_MIM\_LONGDATA**](mm-mim-longdata.md)

## Sending Messages to Devices

-   [**midiInMessage**](midiinmessage.md)
-   [**midiOutMessage**](midioutmessage.md)

## Related topics

<dl> <dt>

[Musical Instrument Digital Interface (MIDI)](musical-instrument-digital-interface--midi.md)
</dt> </dl>

 

 




