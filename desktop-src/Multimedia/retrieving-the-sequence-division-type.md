---
title: Retrieving the Sequence Division Type
description: Retrieving the Sequence Division Type
ms.assetid: 9c7e3482-93a3-4f9c-8b70-a9c733de14fe
keywords:
- Musical Instrument Digital Interface (MIDI),sequence division type
- MIDI (Musical Instrument Digital Interface),sequence division type
- MCI MIDI sequencer,division type
- MCI_STATUS command
- sequence division type
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the Sequence Division Type

The *division type* of a MIDI sequence determines the amount of time between MIDI events in the sequence. To determine the division type of a sequence, use the [**MCI\_STATUS**](mci-status.md) command and set the **dwItem** member of the [**MCI\_STATUS\_PARMS**](mci-status-parms.md) structure to MCI\_SEQ\_STATUS\_DIVTYPE .

If the **MCI\_STATUS** command is successful, the **dwReturn** member of the **MCI\_STATUS\_PARMS** structure will contain one of the following values to indicate the division type.



| Value                        | Division type                     |
|------------------------------|-----------------------------------|
| MCI\_SEQ\_DIV\_PPQN          | PPQN (parts-per-quarter note)     |
| MCI\_SEQ\_DIV\_SMPTE\_24     | SMPTE, 24 fps (frames per second) |
| MCI\_SEQ\_DIV\_SMPTE\_25     | SMPTE, 25 fps                     |
| MCI\_SEQ\_DIV\_SMPTE\_30     | SMPTE, 30 fps                     |
| MCI\_SEQ\_DIV\_SMPTE\_30DROP | SMPTE, 30 fps drop frame          |



 

You must know the division type of a sequence to change or query its tempo. You cannot change the division type of a sequence by using the MCI sequencer.

 

 




