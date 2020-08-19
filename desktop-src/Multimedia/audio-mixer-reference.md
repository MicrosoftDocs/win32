---
title: Audio Mixer Reference
description: Audio Mixer Reference
ms.assetid: 9d8751b1-9c0b-4238-a961-27c09a869bb3
keywords:
- multimedia audio,audio mixers
- audio,audio mixers
- multimedia audio,mixer reference
- audio,mixer reference
- audio mixers,reference
- mixers,reference
- reference for audio mixers,about
ms.topic: article
ms.date: 05/31/2018
---

# Audio Mixer Reference

This section describes the functions, structures, and messages associated with audio mixers. These elements are grouped as follows.

## Querying Devices

-   [**MIXERCAPS**](/windows/win32/api/mmeapi/ns-mmeapi-mixercaps)
-   [**mixerGetDevCaps**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetdevcaps)
-   [**mixerGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetnumdevs)

## Opening and Closing

-   [**mixerClose**](/windows/win32/api/mmeapi/nf-mmeapi-mixerclose)
-   [**mixerOpen**](/windows/win32/api/mmeapi/nf-mmeapi-mixeropen)

## Retrieving Mixer Identifiers

-   [**mixerGetID**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetid)

## Retrieving Line Controls

-   [**MIXERCONTROL**](/windows/win32/api/mmeapi/ns-mmeapi-mixercontrol)
-   [**mixerGetLineControls**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetlinecontrols)
-   [**MIXERLINECONTROLS**](/windows/win32/api/mmeapi/ns-mmeapi-mixerlinecontrols)

## Changing Control Attributes

-   [**MIXERCONTROLDETAILS**](/windows/win32/api/mmeapi/ns-mmeapi-mixercontroldetails_listtexta)
-   [**MIXERCONTROLDETAILS\_BOOLEAN**](/previous-versions//dd757295(v=vs.85))
-   [**MIXERCONTROLDETAILS\_LISTTEXT**](/previous-versions//dd757296(v=vs.85))
-   [**MIXERCONTROLDETAILS\_SIGNED**](/previous-versions//dd757297(v=vs.85))
-   [**MIXERCONTROLDETAILS\_UNSIGNED**](/previous-versions//dd757298(v=vs.85))
-   [**mixerGetControlDetails**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetcontroldetails)
-   [**mixerSetControlDetails**](/windows/win32/api/mmeapi/nf-mmeapi-mixersetcontroldetails)

## Retrieving Line Information

-   [**mixerGetLineInfo**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetlineinfo)
-   [**MIXERLINE**](/windows/win32/api/mmeapi/ns-mmeapi-mixerline)
-   [**MM\_MIXM\_CONTROL\_CHANGE**](mm-mixm-control-change.md)
-   [**MM\_MIXM\_LINE\_CHANGE**](mm-mixm-line-change.md)

## Sending User-Defined Messages

-   [**mixerMessage**](/windows/win32/api/mmeapi/nf-mmeapi-mixermessage)

## Related topics

<dl> <dt>

[Audio Mixer Reference](audio-mixer-reference.md)
</dt> </dl>

 

 