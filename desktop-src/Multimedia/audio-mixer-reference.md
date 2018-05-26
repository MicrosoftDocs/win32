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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audio Mixer Reference

This section describes the functions, structures, and messages associated with audio mixers. These elements are grouped as follows.

## Querying Devices

-   [**MIXERCAPS**](mixercaps.md)
-   [**mixerGetDevCaps**](mixergetdevcaps.md)
-   [**mixerGetNumDevs**](mixergetnumdevs.md)

## Opening and Closing

-   [**mixerClose**](mixerclose.md)
-   [**mixerOpen**](mixeropen.md)

## Retrieving Mixer Identifiers

-   [**mixerGetID**](mixergetid.md)

## Retrieving Line Controls

-   [**MIXERCONTROL**](mixercontrol.md)
-   [**mixerGetLineControls**](mixergetlinecontrols.md)
-   [**MIXERLINECONTROLS**](mixerlinecontrols.md)

## Changing Control Attributes

-   [**MIXERCONTROLDETAILS**](/windows/win32/mmeapi/ns-mmeapi-tagmixercontroldetails_listtexta?branch=master)
-   [**MIXERCONTROLDETAILS\_BOOLEAN**](/windows/win32/mmeapi/?branch=master)
-   [**MIXERCONTROLDETAILS\_LISTTEXT**](/windows/win32/mmeapi/?branch=master)
-   [**MIXERCONTROLDETAILS\_SIGNED**](/windows/win32/mmeapi/?branch=master)
-   [**MIXERCONTROLDETAILS\_UNSIGNED**](/windows/win32/mmeapi/?branch=master)
-   [**mixerGetControlDetails**](mixergetcontroldetails.md)
-   [**mixerSetControlDetails**](mixersetcontroldetails.md)

## Retrieving Line Information

-   [**mixerGetLineInfo**](mixergetlineinfo.md)
-   [**MIXERLINE**](mixerline.md)
-   [**MM\_MIXM\_CONTROL\_CHANGE**](mm-mixm-control-change.md)
-   [**MM\_MIXM\_LINE\_CHANGE**](mm-mixm-line-change.md)

## Sending User-Defined Messages

-   [**mixerMessage**](mixermessage.md)

## Related topics

<dl> <dt>

[Audio Mixer Reference](audio-mixer-reference.md)
</dt> </dl>

 

 




