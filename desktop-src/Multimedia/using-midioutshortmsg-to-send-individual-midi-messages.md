---
title: Using midiOutShortMsg to Send Individual MIDI Messages
description: Using midiOutShortMsg to Send Individual MIDI Messages
ms.assetid: 7a8f7c6c-28ac-4aa6-9073-969fc8e59f4e
keywords:
- Musical Instrument Digital Interface (MIDI),sending messages
- MIDI (Musical Instrument Digital Interface),sending messages
- sending MIDI messages
- Musical Instrument Digital Interface (MIDI),midiOutShortMsg function
- MIDI (Musical Instrument Digital Interface),midiOutShortMsg function
- midiOutShortMsg function
ms.topic: article
ms.date: 05/31/2018
---

# Using midiOutShortMsg to Send Individual MIDI Messages

The following example uses the [**midiOutShortMsg**](/windows/win32/api/mmeapi/nf-mmeapi-midioutshortmsg) function to send a specified MIDI event to a given MIDI output device:


```C++
UINT sendMIDIEvent(HMIDIOUT hmo, BYTE bStatus, BYTE bData1, 
    BYTE bData2) 
{ 
    union { 
        DWORD dwData; 
        BYTE bData[4]; 
    } u; 
 
    // Construct the MIDI message. 
 
    u.bData[0] = bStatus;  // MIDI status byte 
    u.bData[1] = bData1;   // first MIDI data byte 
    u.bData[2] = bData2;   // second MIDI data byte 
    u.bData[3] = 0; 
 
    // Send the message. 
    return midiOutShortMsg(hmo, u.dwData); 
} 
```



> [!Note]  
> MIDI output drivers are not required to verify data before sending it to an output port. Applications must ensure that only valid data is sent.

 

 

 