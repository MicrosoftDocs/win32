---
title: Windows Media Device Manager Device Extensions for Metadata Transfer
description: Windows Media Device Manager Device Extensions for Metadata Transfer
ms.assetid: c1d84225-b5b1-4f9e-8694-a229653e53de
keywords:
- Windows Media Player,device extensions
- Windows Media Player,extensions
- Windows Media Player,metadata
- Windows Media Player,accelerated metadata transfer
- Windows Media Player,metadata accelerated transfer
- metadata,device extensions
- metadata,extensions
- device extensions,metadata transfer
- extensions,metadata transfer
- accelerated metadata transfer
- metadata,accelerated transfer
- device extensions,accelerated metadata transfer
- extensions,accelerated metadata transfer
ms.topic: article
ms.date: 05/31/2018
---

# Windows Media Device Manager Device Extensions for Metadata Transfer

To enable accelerated metadata transfer, manufacturers of devices that do not support MTP must do the following in source code:

-   Define **WMP\_WMDM\_DEVICE\_SUPPORT**.
-   Include wmpdevices.h, which is installed as part of the Windows Media Player SDK.

Wmpdevices.h defines the following structures.



| Structure                                                                                 | Description                                                                                                                                       |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [WMP\_WMDM\_METADATA\_ROUND\_TRIP\_PC2DEVICE](/previous-versions/windows/desktop/api/wmpdevices/ns-wmpdevices-wmp_wmdm_metadata_round_trip_pc2device) | Structure used by Windows Media Player to request accelerated metadata synchronization information from portable devices that do not support MTP. |
| [WMP\_WMDM\_METADATA\_ROUND\_TRIP\_DEVICE2PC](/previous-versions/windows/desktop/api/wmpdevices/ns-wmpdevices-wmp_wmdm_metadata_round_trip_device2pc) | Structure used by Windows Media Player to receive accelerated metadata synchronization information from portable devices that do not support MTP. |



 

To request information from the device about metadata that has changed, Windows Media Player 10 or later calls the Windows Media Device Manager method **IWMDMDevice3::DeviceIoControl**. When making this call, the Player follows specific steps, as follows:

-   The first parameter, *dwIoControlCode*, contains the constant **IOCTL\_WMP\_METADATA\_ROUND\_TRIP**. This constant is defined in wmpdevices.h.
-   The second parameter, *lpInBuffer*, points to a **WMP\_WMDM\_METADATA\_ROUND\_TRIP\_PC2DEVICE** structure.
-   The third parameter, *nInBufferSize*, contains the size of the input buffer.
-   The fourth parameter, *lpOutBuffer*, points to a **WMP\_WMDM\_METADATA\_ROUND\_TRIP\_DEVICE2PC** structure. The device must fill in this structure with information about changes.
-   The fifth parameter, *pnOutBufferSize*, receives the size of the output buffer.

## Related topics

<dl> <dt>

[**Device Extensions for Accelerated Metadata Transfer**](device-extensions-for-accelerated-metadata-transfer.md)
</dt> </dl>

 

 




