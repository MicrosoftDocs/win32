---
title: MTP Device Extensions for Metadata Transfer
description: MTP Device Extensions for Metadata Transfer
ms.assetid: 9cf68373-e84f-4568-a9da-16ddee0fc4e9
keywords:
- Windows Media Player,MTP device extensions
- Windows Media Player,device extensions
- Windows Media Player,extensions
- Windows Media Player,metadata
- Windows Media Player,Media Transfer Protocol (MTP)
- Media Transfer Protocol (MTP)
- MTP (Media Transfer Protocol)
- metadata,MTP device extensions
- metadata,device extensions
- metadata,extensions
- device extensions,metadata transfer
- extensions,metadata transfer
- MTP device extensions for metadata transfer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MTP Device Extensions for Metadata Transfer

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Media Transfer Protocol (MTP) is a protocol designed for portable media devices. The primary purpose of this protocol is to provide a common protocol for exchanging data between a computer and a portable media device. This includes receiving and sending media objects and enumerating the contents and capabilities of the device.

MTP uses persistent unique object identifiers (PUOIDs) to uniquely identify digital media items (and other objects) stored on a device. When exchanging information about changes that have occurred on a device that supports MTP, the device and Windows Media Player use PUOIDs to identify which objects have changed.

The header file named wmpdevices.h, which is installed as part of the Windows Media Player SDK, defines the structures and constants needed to support Windows Media Player device extensions.

For a device to be recognized as supporting metadata transfer through the Windows Media Player MTP device extension set, it must include the following information in the DeviceInfo dataset. (For more information about this dataset, see section 4.6.1 of the MTP specification.)



| Dataset field          | Field order | Data type  | Value                       |
|------------------------|-------------|------------|-----------------------------|
| VendorExtensionID      | 2           | **UINT32** | 0x00000006                  |
| VendorExtensionVersion | 3           | **UINT16** | 0x0064 (100)                |
| VendorExtensionDesc    | 4           | **String** | "microsoft.com/WMPPD: 10.0" |



 

The following table provides details about the MTP operation for accelerated metadata transfer.



| Item                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operation Code        | 0x9201                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Operation Parameter 1 | The transaction ID supplied by the device during the previous session. This value is zero for the first session.                                                                                                                                                                                                                                                                                                                                                                                       |
| Operation Parameter 2 | Starting index. This value is always zero on the first call of a session. On subsequent calls within the same synchronization session, this value increases by the sum of the count of the modified and the deleted items from the previous response data.                                                                                                                                                                                                                                             |
| Operation Parameter 3 | 0x10000. This constant, defined in wmpdevices.h, is the maximum number of PUOIDs that can be returned in the response. Note that the value of this constant may be revised in future releases of this header file.                                                                                                                                                                                                                                                                                     |
| Operation Parameter 4 | 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Operation Parameter 5 | 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Data                  | The device returns two contiguous MTP arrays containing PUOIDs. Each MTP array begins with a **DWORD** value indicating the count of items in the array, followed by the array of elements. The first MTP array contains the list of PUOIDs that have been added or changed. The second MTP array contains the list of PUOIDs that have been deleted from the portable device.Note that the sum of PUOID count in the two arrays must not exceed the value passed in Operation Parameter 3.<br/> |
| Data Direction        | R->I                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Response Code Options | **MTP\_RESPONSE\_OK** (0x2001) or valid error response code.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Response Parameter 1  | The device's current transaction ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Response Parameter 2  | The number of PUOIDs that remain to be retrieved by future requests.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Response Parameter 3  | **DWORD** containing status information. Status is indicated in a bitwise fashion. See Remarks for information about flags to use.                                                                                                                                                                                                                                                                                                                                                                     |
| Response Parameter 4  | 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Response Parameter 5  | 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

## Remarks

Status is indicated through Response Parameter 3 in a bitwise fashion by using the following flags.



| Flag                                             | Value | Description                                                                                                                                                                                                                          |
|--------------------------------------------------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WMP\_MDRT\_FLAGS\_UNREPORTED\_DELETED\_ITEMS** | 0x1   | Items were deleted before the first object path name being reported. This often indicates that the device was reformatted.                                                                                                           |
| **WMP\_MDRT\_FLAGS\_UNREPORTED\_ADDED\_ITEMS**   | 0x2   | The device contains some added items that cannot be returned in the list of PUOIDS. Note that this flag is not redundant with Response Parameter 2. Set this flag only when there are requested items that the device cannot return. |



 

Bits 2 through 31 are reserved for future use. These bits should be set to zero.

Windows Media Player sends the MTP command to a device at the start of a synchronization session before media files are transferred. The device should return its response as quickly as possible to avoid delays in the synchronization operation.

Windows Media Player will request values for the attributes listed in [About the Metadata](about-the-metadata.md) for each modified POUID returned in the response. Windows Media Player might send updated values for these attributes to the device in subsequent commands.

Files reported as having been removed from the device can be copied to the device again if the user's settings require it.

## Related topics

<dl> <dt>

[**Device Extensions for Accelerated Metadata Transfer**](device-extensions-for-accelerated-metadata-transfer.md)
</dt> </dl>

 

 





