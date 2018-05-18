---
title: WiaItemFlag enumeration
description: Supplies the bits that make up an Item's type. You can test an Item's type by using the AND operation with Item.Properties( \ 0034;Item Flags \ 0034;) and a member from the WiaItemFlag enumeration.
ms.assetid: '45ff1f7b-8080-4e79-95ad-bd3355816a8e'
keywords: ["WiaItemFlag enumeration WIA Automation", "WiaDeviceType enumeration WIA Automation"]
topic_type:
- apiref
api_name:
- WiaDeviceType
api_location:
- Wiaaut.h
api_type:
- HeaderDef
---

# WiaItemFlag enumeration

Supplies the bits that make up an [**Item**](-wiaaut-item.md)'s type. You can test an **Item**'s type by using the **AND** operation with `Item.Properties("Item Flags")` and a member from the **WiaItemFlag** enumeration.

## Members



| Member                     | Description                                                                                                                                 | Value      |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **FreeItemFlag**           | The item is uninitialized or has been deleted.<br/>                                                                                   | 0x0        |
| **ImageItemFlag**          | The item is an image file. Only valid for items that also have the FileItemFlag flag set.<br/>                                        | 0x1        |
| **FileItemFlag**           | The item is a file.<br/>                                                                                                              | 0x2        |
| **FolderItemFlag**         | The item is a folder.<br/>                                                                                                            | 0x4        |
| **RootItemFlag**           | Identifies the root item in the device.<br/>                                                                                          | 0x8        |
| **AnalyzeItemFlag**        | This item supports the Analyze method.<br/>                                                                                           | 0x10       |
| **AudioItemFlag**          | The item is an audio file. Only valid for items that also have the FileItemFlag flag set.<br/>                                        | 0x20       |
| **DeviceItemFlag**         | The item represents a connected device.<br/>                                                                                          | 0x40       |
| **DeletedItemFlag**        | The item is marked as deleted.<br/>                                                                                                   | 0x80       |
| **DisconnectedItemFlag**   | The item represents a disconnected device.<br/>                                                                                       | 0x100      |
| **HPanoramaItemFlag**      | The item represents a horizontal panoramic image.<br/>                                                                                | 0x200      |
| **VPanoramaItemFlag**      | The item represents a vertical panoramic image.<br/>                                                                                  | 0x400      |
| **BurstItemFlag**          | Images in this folder were taken in a continuous time sequence. Only valid for items that also have the FolderItemFlag flag set.<br/> | 0x800      |
| **StorageItemFlag**        | The item represents a storage medium.<br/>                                                                                            | 0x1000     |
| **TransferItemFlag**       | The item can be transferred.<br/>                                                                                                     | 0x2000     |
| **GeneratedItemFlag**      | This item was created and does not correspond to an item in a device.<br/>                                                            | 0x4000     |
| **HasAttachmentsItemFlag** | The item has file attachments.<br/>                                                                                                   | 0x8000     |
| **VideoItemFlag**          | The item represents streaming video.<br/>                                                                                             | 0x10000    |
| **RemovedItemFlag**        | The item has been removed from the device.<br/>                                                                                       | 0x80000000 |



## Remarks

An Item's type provides more information about exactly what kind of imaging device item the [**Item**](-wiaaut-item.md) object is associated with.

For example code, see [Count Root Level Images for Transfer](-wiaaut-shared-samples.md#count-root-level-images-for-transfer) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 





