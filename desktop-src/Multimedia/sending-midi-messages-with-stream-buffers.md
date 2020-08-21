---
title: Sending MIDI Messages with Stream Buffers
description: Sending MIDI Messages with Stream Buffers
ms.assetid: f9e77637-098c-4ee8-bca9-a05ecce0c569
keywords:
- Musical Instrument Digital Interface (MIDI),stream buffers
- MIDI (Musical Instrument Digital Interface),stream buffers
- playing MIDI files,stream buffers
- stream buffers,sending MIDI messages
- Musical Instrument Digital Interface (MIDI),sending messages
- MIDI (Musical Instrument Digital Interface),sending messages
- playing MIDI files,sending messages
- sending MIDI messages
ms.topic: article
ms.date: 05/31/2018
---

# Sending MIDI Messages with Stream Buffers

When your application works with stream buffers, it uses the [**midiStreamOut**](/windows/win32/api/mmeapi/nf-mmeapi-midistreamout) function to send all (short and long) MIDI messages to the device. To specify stream data blocks, use the [**MIDIHDR**](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) and [**MIDIEVENT**](/windows/win32/api/mmeapi/ns-mmeapi-midievent) structures. The **MIDIHDR** structure contains an address of a locked data block, the data-block length, and some assorted flags. The data is stored in the form of **MIDIEVENT** structures. The system imposes a size limit of 64K on stream buffers.

After you use **midiStreamOut** to send a stream buffer of data, you must wait until the device driver is finished with the data block before freeing it. If you are sending multiple data blocks, you must monitor the completion of each data block so you know when to send additional blocks. For information about different techniques for monitoring data-block completion, see [Managing MIDI Data Blocks](managing-midi-data-blocks.md).

 

 