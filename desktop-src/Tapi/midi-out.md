---
Description: The midi/out device class consists of MIDI sequencers that are used for output. You access these devices by using the MIDI functions, which are described in the Platform Software Development Kit (SDK).
ms.assetid: 398119ec-2d08-4c37-a993-a9b5ce52bcc8
title: midi/out
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# midi/out

The midi/out device class consists of MIDI sequencers that are used for output. You access these devices by using the MIDI functions, which are described in the Platform Software Development Kit (SDK).

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) and [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) functions fill a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring_tag) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_BINARY value and appending this additional member:

``` syntax
DWORD DeviceId;  // identifier of MIDI device
```

The **DeviceId** member is the identifier of a closed MIDI device. You use this identifier in a call to the [**midiOutOpen**](https://msdn.microsoft.com/en-us/library/Dd798476(v=VS.85).aspx) function to open the device for output. You can use the resulting device handle to play MIDI data at the line or phone device.

For more information about the MIDI functions, see [**Multimedia Functions**](https://msdn.microsoft.com/en-us/library/Dd743586(v=VS.85).aspx).

 

 



