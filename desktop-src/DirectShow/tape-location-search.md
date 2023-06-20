---
description: Tape Location Search
ms.assetid: 17fb4eba-4b2c-41c2-94e2-e58586f92e53
title: Tape Location Search
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Tape Location Search

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Although DV devices support a command to search by time code or by absolute track number (ATN), the MSDV driver does not have a standard, device-independent way to access these functions. The only option is to send a raw AV/C command to the driver as described in the topic [Issuing Raw AV/C Commands](issuing-raw-av-c-commands.md).

The UVC driver supports a property set for tape location searches. To send a search command, use the **IKsControl** interface and set the PROPSETID\_EXT\_TRANSPORT property. Using a property set is safer than sending raw AV/C commands to the device, because AV/C commands bypass the filter and go directly to the device driver.

## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> <dt>

[External Device Transport Property Set](external-device-transport-property-set.md)
</dt> </dl>

 

 



