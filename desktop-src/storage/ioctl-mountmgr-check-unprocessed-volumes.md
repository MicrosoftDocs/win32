---
title: IOCTL\_MOUNTMGR\_CHECK\_UNPROCESSED\_VOLUMES control code
description: When a volume arrives in the system, it registers for the MOUNTDEV\_MOUNTED\_DEVICE\_GUID interface class and the mount manager receives a Plug and Play notification (see Mount Manager I/O Control Codes for a discussion of this process).
ms.assetid: '39f486b4-a22e-473b-9a0d-ba2c1046995a'
keywords: ["IOCTL_MOUNTMGR_CHECK_UNPROCESSED_VOLUMES control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_MOUNTMGR_CHECK_UNPROCESSED_VOLUMES
api_location:
- Mountmgr.h
api_type:
- HeaderDef
---

# IOCTL\_MOUNTMGR\_CHECK\_UNPROCESSED\_VOLUMES control code

When a volume arrives in the system, it registers for the MOUNTDEV\_MOUNTED\_DEVICE\_GUID interface class and the mount manager receives a Plug and Play notification (see [Mount Manager I/O Control Codes](mount-manager-i-o-control-codes.md) for a discussion of this process). When the mount manager receives this notification, it queries the client driver that manages the volume for the volume's unique ID. In some cases, however, particularly with clusters, the client notifies the mount manager of the arrival of its volume, but then does not respond when queried for the volume's unique ID. The mount manager keeps these volumes in a *dead mounted device* list. Clients can use the IOCTL\_MOUNTMGR\_CHECK\_UNPROCESSED\_VOLUMES IOCTL to request that the mount manager rescan its dead mounted device list and make another attempt to query the clients on the list for the unique IDs of their respective volumes.

This IOCTL is used primarily for cluster support.

## Input Buffer

None

## Input Buffer Length

None

## Output Buffer

None

## Output Buffer Length

None

## Status block

If the operation is successful, the **Status** field is set to STATUS\_SUCCESS.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTMGR_CHECK_UNPROCESSED_VOLUMES%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





