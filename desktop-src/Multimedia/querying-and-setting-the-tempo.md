---
title: Querying and Setting the Tempo
description: Querying and Setting the Tempo
ms.assetid: 84eba230-88b6-4cba-9e90-ba0b4bcfc691
keywords:
- Musical Instrument Digital Interface (MIDI),tempo
- MIDI (Musical Instrument Digital Interface),tempo
- MCI MIDI sequencer,tempo
- MCI_STATUS command
- sequence tempo
- tempo
ms.topic: article
ms.date: 05/31/2018
---

# Querying and Setting the Tempo

To retrieve the tempo of a sequence, use the [**MCI\_STATUS**](mci-status.md) command and set the **dwItem** member of the [**MCI\_STATUS\_PARMS**](mci-status-parms.md) structure to MCI\_SEQ\_STATUS\_TEMPO. If the **MCI\_STATUS** command is successful, the **dwReturn** member of the **MCI\_STATUS\_PARMS** structure contains the current tempo.

To change tempo, use the [**MCI\_SET**](mci-set.md) command with the [**MCI\_SEQ\_SET\_PARMS**](mci-seq-set-parms.md) structure, specifying the MCI\_SEQ\_SET\_TEMPO flag and setting the **dwTempo** member of the structure to the desired tempo.

The way tempo is represented depends on the division type of the sequence. If the division type is PPQN, the tempo is represented in beats per minute. If the division type is one of the SMPTE division types, the tempo is represented in frames per second. For information about determining the division type of a sequence, see [Retrieving the Sequence Division Type](retrieving-the-sequence-division-type.md).

 

 




