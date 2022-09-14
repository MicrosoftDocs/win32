---
title: Device I/O Control Codes
description: Device I/O Control Codes
ms.assetid: 46a5d166-ca8d-42df-9455-145332437153
keywords:
- Windows Media Player,device I/O control codes
- Windows Media Player,control codes
- Windows Media Device Manager
- device I/O control codes
- control codes
ms.topic: article
ms.date: 05/31/2018
---

# Device I/O Control Codes

Windows Media Player 10 or later defines Windows Media Device Manager device I/O control codes. The following table contains the control codes and their descriptions.



| I/O control code                      | Value      | Description                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **IOCTL\_WMP\_METADATA\_ROUND\_TRIP** | 0x31504d57 | Manages transfer of information about changes that occurred to metadata values. See [Device Extensions for Accelerated Metadata Transfer](device-extensions-for-accelerated-metadata-transfer.md).                                                                                                                                                                          |
| **IOCTL\_WMP\_DEVICE\_CAN\_SYNC**     | 0x32504d57 | Indicates whether a portable device supports automatic synchronization. Windows Media Player 10 or later provides no input buffer.The output buffer must return a **DWORD** value. A value of 1 means the device supports synchronization. A value of 0 means the device does not support automatic synchronization.<br/> See Remarks for more information.<br/> |



 

## Remarks

These control codes are defined in wmpdevices.h.

If the device does not support **IOCTL\_WMP\_DEVICE\_CAN\_SYNC**, Windows Media Player 10 or later assumes the device supports automatic synchronization. Note that while this value can disallow automatic synchronization, there are additional criteria used to determine whether the device supports automatic synchronization.

## Related topics

<dl> <dt>

[**Device Extensions for Accelerated Metadata Transfer**](device-extensions-for-accelerated-metadata-transfer.md)
</dt> <dt>

[**Windows Media Player**](windows-media-player.md)
</dt> </dl>

 

 





