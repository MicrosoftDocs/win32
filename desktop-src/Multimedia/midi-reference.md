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
ms.topic: article
ms.date: 05/31/2018
---

# MIDI Reference

This section describes the functions, macros, messages, and structures associated with the Musical Instrument Digital Interface (MIDI). These elements are grouped as follows.

## Allocating and Managing Buffers

-   [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr)
-   [**midiInAddBuffer**](/windows/win32/api/mmeapi/nf-mmeapi-midiinaddbuffer)
-   [**midiInPrepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midiinprepareheader)
-   [**midiInUnprepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midiinunprepareheader)
-   [**midiOutPrepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midioutprepareheader)
-   [**midiOutUnprepareHeader**](/windows/win32/api/mmeapi/nf-mmeapi-midioutunprepareheader)

## Callback Functions

-   [**MidiInProc**](/previous-versions//dd798460(v=vs.85))
-   [**MidiOutProc**](/previous-versions//dd798478(v=vs.85))

## Device Capabilities

-   [**MIDIINCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-midiincaps)
-   [**midiInGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-midiingetdevcaps)
-   [**midiInGetID**](/windows/win32/api/mmeapi/nf-mmeapi-midiingetid)
-   [**midiInGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-midiingetnumdevs)
-   [**MIDIOUTCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-midioutcaps)
-   [**midiOutGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-midioutgetdevcaps)
-   [**midiOutGetID**](/windows/win32/api/mmeapi/nf-mmeapi-midioutgetid)
-   [**midiOutGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-midioutgetnumdevs)
-   [**MIDISTRMBUFFVER**](/windows/win32/api/mmeapi/ns-mmeapi-midistrmbuffver)

## Error Processing

-   [**midiInGetErrorText**](/windows/win32/api/mmeapi/nf-mmeapi-midiingeterrortext)
-   [**midiOutGetErrorText**](/windows/win32/api/mmeapi/nf-mmeapi-midioutgeterrortext)
-   [**MIM\_ERROR**](mim-error.md)
-   [**MIM\_LONGERROR**](mim-longerror.md)
-   [**MM\_MIM\_ERROR**](mm-mim-error.md)
-   [**MM\_MIM\_LONGERROR**](mm-mim-longerror.md)

## Managing MIDI Streams

-   [**midiStreamClose**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamclose)
-   [**midiStreamOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamopen)
-   [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout)
-   [**midiStreamPause**](/windows/win32/api/mmeapi/nf-mmeapi-midistreampause)
-   [**midiStreamPosition**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamposition)
-   [**midiStreamProperty**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamproperty)
-   [**midiStreamRestart**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamrestart)
-   [**midiStreamStop**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamstop)

## Opening and Closing Devices

-   [**midiInClose**](/windows/win32/api/mmeapi/nf-mmeapi-midiinclose)
-   [**midiInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midiinopen)
-   [**midiOutClose**](/windows/win32/api/mmeapi/nf-mmeapi-midioutclose)
-   [**midiOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midioutopen)
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
-   [**midiOutCacheDrumPatches**](/windows/win32/api/mmeapi/nf-mmeapi-midioutcachedrumpatches)
-   [**midiOutCachePatches**](/windows/win32/api/mmeapi/nf-mmeapi-midioutcachepatches)
-   [**midiOutGetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-midioutgetvolume)
-   [**midiOutSetVolume**](/windows/win32/api/mmeapi/nf-mmeapi-midioutsetvolume)
-   [PATCHARRAY](patcharray.md)

## Playing a Message or Messages

-   [**MEVT\_EVENTPARM**](/windows/win32/api/mmeapi/nf-mmeapi-mevt_eventparm)
-   [**MEVT\_EVENTTYPE**](/windows/win32/api/mmeapi/nf-mmeapi-mevt_eventtype)
-   [**MIDIEVENT**](/windows/win32/api/mmeapi/ns-mmeapi-midievent)
-   [**midiOutLongMsg**](/windows/win32/api/mmeapi/nf-mmeapi-midioutlongmsg)
-   [**midiOutReset**](/windows/win32/api/mmeapi/nf-mmeapi-midioutreset)
-   [**midiOutShortMsg**](/windows/win32/api/mmeapi/nf-mmeapi-midioutshortmsg)
-   [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout)
-   [**midiStreamPause**](/windows/win32/api/mmeapi/nf-mmeapi-midistreampause)
-   [**midiStreamRestart**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamrestart)
-   [**midiStreamStop**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamstop)
-   [**MM\_MOM\_DONE**](mm-mom-done.md)
-   [**MM\_MOM\_POSITIONCB**](mm-mom-positioncb.md)
-   [**MOM\_DONE**](mom-done.md)
-   [**MOM\_POSITIONCB**](mom-positioncb.md)

## Recording

-   [**midiConnect**](/windows/win32/api/mmeapi/nf-mmeapi-midiconnect)
-   [**midiDisconnect**](/windows/win32/api/mmeapi/nf-mmeapi-mididisconnect)
-   [**midiInReset**](/windows/win32/api/mmeapi/nf-mmeapi-midiinreset)
-   [**midiInStart**](/windows/win32/api/mmeapi/nf-mmeapi-midiinstart)
-   [**midiInStop**](/windows/win32/api/mmeapi/nf-mmeapi-midiinstop)
-   [**MIDIPROPTEMPO**](/windows/win32/api/mmeapi/ns-mmeapi-midiproptempo)
-   [**MIDIPROPTIMEDIV**](/windows/win32/api/mmeapi/ns-mmeapi-midiproptimediv)
-   [**MIM\_DATA**](mim-data.md)
-   [**MIM\_LONGDATA**](mim-longdata.md)
-   [**MIM\_MOREDATA**](mim-moredata.md)
-   [**MM\_MIM\_DATA**](mm-mim-data.md)
-   [**MM\_MIM\_MOREDATA**](mm-mim-moredata.md)
-   [**MM\_MIM\_LONGDATA**](mm-mim-longdata.md)

## Sending Messages to Devices

-   [**midiInMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midiinmessage)
-   [**midiOutMessage**](/windows/win32/api/mmeapi/nf-mmeapi-midioutmessage)

## Related topics

<dl> <dt>

[Musical Instrument Digital Interface (MIDI)](musical-instrument-digital-interface--midi.md)
</dt> </dl>

 

 