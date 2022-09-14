---
description: The midi/in device class consists of MIDI sequencers that are used for input. You access these devices by using the MIDI functions, which are described in the Platform Software Development Kit (SDK).
ms.assetid: 8997a391-bf61-4ec9-8ffc-fe3e6b92d63a
title: midi/in
ms.topic: article
ms.date: 05/31/2018
---

# midi/in

The midi/in device class consists of MIDI sequencers that are used for input. You access these devices by using the MIDI functions, which are described in the Platform Software Development Kit (SDK).

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) and [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) functions fill a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_BINARY value and appending this additional member:

``` syntax
DWORD DeviceId;  // identifier of MIDI device
```

The **DeviceId** member is the identifier of a closed MIDI device. You use this identifier in a call to the [**midiInOpen**](/windows/win32/api/mmeapi/nf-mmeapi-midiinopen) function to open the device for input. You can use the resulting device handle to record MIDI data from the line or phone device.

For more information about the MIDI functions, see [**Multimedia Functions**](../multimedia/multimedia-functions.md).

 

 
