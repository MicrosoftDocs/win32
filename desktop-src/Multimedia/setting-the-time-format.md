---
title: Setting the Time Format
description: Setting the Time Format
ms.assetid: c670d47e-30fc-4637-b468-b6a415605dca
keywords:
- MCI_SET command message
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting the Time Format

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Use the [**MCI\_SET**](mci-set.md) command message along with the [**MCI\_SET\_PARMS**](mci-set-parms.md) structure to set the time format for an open device. Set the **dwTimeFormat** member to one of the following constants.



| Constant                   | Time format                                          |
|----------------------------|------------------------------------------------------|
| MCI\_FORMAT\_BYTES         | Bytes (in pulse code modulated \[PCM\] format files) |
| MCI\_FORMAT\_MILLISECONDS  | Milliseconds                                         |
| MCI\_FORMAT\_MSF           | Minute/second/frame                                  |
| MCI\_FORMAT\_SAMPLES       | Samples                                              |
| MCI\_FORMAT\_SMPTE\_24     | SMPTE, 24 frame                                      |
| MCI\_FORMAT\_SMPTE\_25     | SMPTE, 25 frame                                      |
| MCI\_FORMAT\_SMPTE\_30     | SMPTE, 30 frame                                      |
| MCI\_FORMAT\_SMPTE\_30DROP | SMPTE, 30 frame drop                                 |
| MCI\_FORMAT\_TMSF          | Track/minute/second/frame                            |
| MCI\_SEQ\_FORMAT\_SONGPTR  | MIDI song pointer                                    |



 

The following example sets the time format to milliseconds on the device specified by the wDeviceID variable using the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function.


```C++
UINT wDeviceID; 
MCI_SET_PARMS mciSetParms; 

// Set time format to milliseconds. 

mciSetParms.dwTimeFormat = MCI_FORMAT_MILLISECONDS; 
if( mciSendCommand(wDeviceID, MCI_SET, MCI_SET_TIME_FORMAT, 
                  (DWORD) &mciSetParms)) 
{
    // Error, unable to set time format. 
    return FALSE; 
}
else 
{
    // Time format set successfully. 
    return TRUE; 
}
```



 

 