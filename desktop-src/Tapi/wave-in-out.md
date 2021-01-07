---
description: The wave/in/out device class consists of full duplex audio devices.
ms.assetid: 1b49c9ae-da64-4415-95ce-785ffedc65bc
title: wave/in/out
ms.topic: article
ms.date: 05/31/2018
---

# wave/in/out

The wave/in/out device class consists of full duplex audio devices. You access these devices by using the wave functions, which are described in the Platform Software Development Kit (SDK). Devices in this class are associated with line devices that support the LINEMEDIAMODE\_AUTOMATEDVOICE media type, which is specified in the **dwMediaModes** member of the [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps) structure for the line device.

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) and [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) functions fill a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_BINARY value and appending two additional members:

``` syntax
DWORD DeviceInId;  // identifier of wave in audio device
DWORD DeviceOutId;  // identifier of wave out audio device
```

The **DeviceInId** and **DeviceOutId** members are identifiers of a closed audio device. You use these identifiers in a call to the [**waveOutOpen**](/windows/win32/api/mmeapi/nf-mmeapi-waveoutopen) function to open the device for output. You can use the resulting device handle to play digitized audio data at the line or phone device.

For more information about the wave functions, see [**Multimedia Functions**](../multimedia/multimedia-functions.md).

 

 
