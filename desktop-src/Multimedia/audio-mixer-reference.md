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

-   [**MIXERCAPS**](https://msdn.microsoft.com/en-us/library/Dd757291(v=VS.85).aspx)
-   [**mixerGetDevCaps**](https://msdn.microsoft.com/en-us/library/Dd757300(v=VS.85).aspx)
-   [**mixerGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd757304(v=VS.85).aspx)

## Opening and Closing

-   [**mixerClose**](https://msdn.microsoft.com/en-us/library/Dd757292(v=VS.85).aspx)
-   [**mixerOpen**](https://msdn.microsoft.com/en-us/library/Dd757308(v=VS.85).aspx)

## Retrieving Mixer Identifiers

-   [**mixerGetID**](https://msdn.microsoft.com/en-us/library/Dd757301(v=VS.85).aspx)

## Retrieving Line Controls

-   [**MIXERCONTROL**](https://msdn.microsoft.com/en-us/library/Dd757293(v=VS.85).aspx)
-   [**mixerGetLineControls**](https://msdn.microsoft.com/en-us/library/Dd757302(v=VS.85).aspx)
-   [**MIXERLINECONTROLS**](https://msdn.microsoft.com/en-us/library/Dd757306(v=VS.85).aspx)

## Changing Control Attributes

-   [**MIXERCONTROLDETAILS**](/windows/win32/api/mmeapi/ns-mmeapi-mixercontroldetails_listtexta)
-   [**MIXERCONTROLDETAILS\_BOOLEAN**](https://msdn.microsoft.com/en-us/library/Dd757295(v=VS.85).aspx)
-   [**MIXERCONTROLDETAILS\_LISTTEXT**](https://msdn.microsoft.com/en-us/library/Dd757296(v=VS.85).aspx)
-   [**MIXERCONTROLDETAILS\_SIGNED**](https://msdn.microsoft.com/en-us/library/Dd757297(v=VS.85).aspx)
-   [**MIXERCONTROLDETAILS\_UNSIGNED**](https://msdn.microsoft.com/en-us/library/Dd757298(v=VS.85).aspx)
-   [**mixerGetControlDetails**](https://msdn.microsoft.com/en-us/library/Dd757299(v=VS.85).aspx)
-   [**mixerSetControlDetails**](https://msdn.microsoft.com/en-us/library/Dd757309(v=VS.85).aspx)

## Retrieving Line Information

-   [**mixerGetLineInfo**](https://msdn.microsoft.com/en-us/library/Dd757303(v=VS.85).aspx)
-   [**MIXERLINE**](https://msdn.microsoft.com/en-us/library/Dd757305(v=VS.85).aspx)
-   [**MM\_MIXM\_CONTROL\_CHANGE**](mm-mixm-control-change.md)
-   [**MM\_MIXM\_LINE\_CHANGE**](mm-mixm-line-change.md)

## Sending User-Defined Messages

-   [**mixerMessage**](https://msdn.microsoft.com/en-us/library/Dd757307(v=VS.85).aspx)

## Related topics

<dl> <dt>

[Audio Mixer Reference](audio-mixer-reference.md)
</dt> </dl>

 

 




