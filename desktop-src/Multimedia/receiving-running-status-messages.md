---
title: Receiving Running-Status Messages
description: Receiving Running-Status Messages
ms.assetid: 4f2e8e41-89f6-45e3-ae16-47b856f0e63e
keywords:
- Musical Instrument Digital Interface (MIDI),running status
- MIDI (Musical Instrument Digital Interface),running status
- recording MIDI audio,running status
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Receiving Running-Status Messages

The *Standard MIDI Files 1.0* specification allows the use of *running status* when a message has the same status byte as the previous message. When running status is used, the status byte of subsequent messages can be omitted. All MIDI input device drivers are required to expand messages using running status into complete messages, so that you always receive complete MIDI messages from a MIDI input device driver.

## Related topics

<dl> <dt>

[Recording MIDI Audio](recording-midi-audio.md)
</dt> </dl>

 

 




