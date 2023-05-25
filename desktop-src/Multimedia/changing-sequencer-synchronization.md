---
title: Changing Sequencer Synchronization
description: Changing Sequencer Synchronization
ms.assetid: 5c3acb47-e6cc-4957-a306-7039ec110827
keywords:
- MCI_SET command message
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---



# Changing Sequencer Synchronization

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!NOTE]
> Bias-free Communication
Microsoft supports a diverse and inclusionary environment.  Within this document, there are references to the word 'slave.' Microsoft's [Style Guide for Bias-Free Communications](https://github.com/MicrosoftDocs/microsoft-style-guide/blob/master/styleguide/bias-free-communication.md) recognizes this as an exclusionary word.  This wording is used as it is currently the wording used within the software. For consistency, this document contains this word. When this word is removed from the software, we will correct this document to be in alignment.

To change the synchronization mode of a sequencer device, use the [**MCI\_SET**](mci-set.md) command message with the MCI\_SEQ\_SET\_MASTER and MCI\_SEQ\_SET\_SLAVE flags. Two members in the [**MCI\_SEQ\_SET\_PARMS**](mci-seq-set-parms.md) structure, **dwMaster** and **dwSlave**, are used to specify the master and subordinate synchronization modes.

The master synchronization mode controls synchronization information sent by the sequencer to an output port. Following are the constants for the **dwMaster** member and their corresponding master synchronization modes.



| Constant        | Synchronization mode                                                                             |
|-----------------|--------------------------------------------------------------------------------------------------|
| MCI\_SEQ\_MIDI  | MIDI Synchronization. Send timing information to output port using MIDI timing clock messages.   |
| MCI\_SEQ\_SMPTE | SMPTE Synchronization. Send timing information to output port using MIDI quarter-frame messages. |
| MCI\_SEQ\_NONE  | No Synchronization. Send no timing information.                                                  |



 

The subordinate synchronization mode controls where the sequencer gets its timing information to play a MIDI file. Following are the constants for the **dwSlave** member and their corresponding subordinate synchronization modes.



| Constant        | Synchronization mode                                                                                                                               |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| MCI\_SEQ\_FILE  | File Synchronization. Get timing information from MIDI file.                                                                                       |
| MCI\_SEQ\_MIDI  | MIDI Synchronization. Get timing information from input port using MIDI timing clock messages.                                                     |
| MCI\_SEQ\_SMPTE | SMPTE Synchronization. Get timing information from input port using MIDI quarter-frame messages.                                                   |
| MCI\_SEQ\_NONE  | No Synchronization. Get timing information from MCI commands only and ignore timing information (such as tempo changes) that are in the MIDI file. |



 

> [!Note]  
> Currently, for master synchronization, the MCI MIDI sequencer supports only the No Synchronization mode (MCI\_SEQ\_NONE). For subordinate synchronization, it supports only the File Synchronization mode (MCI\_SEQ\_FILE) and the No Synchronization mode (MCI\_SEQ\_NONE).

 

 

 




