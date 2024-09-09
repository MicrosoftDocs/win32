---
title: Device Types
description: Device Types
ms.assetid: 6556fa6a-5906-4afb-ab7d-ef41a0e22d13
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Types

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

MCI recognizes a basic set of *device types*. A device type is a set of MCI drivers that share a common command set and are used to control similar multimedia devices or data files. Many MCI commands, such as [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)), require you to specify a device type.

The following table lists the defined device types. The current implementation of MCI includes command sets for a subset of these devices.



| Device type      | Constant                      | Description                                      |
|------------------|-------------------------------|--------------------------------------------------|
| **cdaudio**      | MCI\_DEVTYPE\_CD\_AUDIO       | CD audio player                                  |
| **dat**          | MCI\_DEVTYPE\_DAT             | Digital-audio tape player                        |
| **digitalvideo** | MCI\_DEVTYPE\_DIGITAL\_VIDEO  | Digital video in a window (not GDI-based)        |
| **other**        | MCI\_DEVTYPE\_OTHER           | Undefined MCI device                             |
| **overlay**      | MCI\_DEVTYPE\_OVERLAY         | Overlay device (analog video in a window)        |
| **scanner**      | MCI\_DEVTYPE\_SCANNER         | Image scanner                                    |
| **sequencer**    | MCI\_DEVTYPE\_SEQUENCER       | MIDI sequencer                                   |
| **vcr**          | MCI\_DEVTYPE\_VCR             | Video-cassette recorder or player                |
| **videodisc**    | MCI\_DEVTYPE\_VIDEODISC       | Videodisc player                                 |
| **waveaudio**    | MCI\_DEVTYPE\_WAVEFORM\_AUDIO | Audio device that plays digitized waveform files |



 

In this document, the names of device types are bold. Device-type names are used with the command-string interface. Device-type constants are used with the command-message interface.

 

 




