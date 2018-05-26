---
title: IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND control code
description: A configured band on a storage device is deleted with the IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND request. An erase option in the input parameters allows the request to perform a cryptographic erase of the band data.
ms.assetid: CA0002E6-D9E7-417B-AD48-32E25E24EC32
keywords:
- IOCTL_EHSTOR_BANDMGMT_DELETE_BAND control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_DELETE_BAND
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND control code

A configured band on a storage device is deleted with the **IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND** request. An erase option in the input parameters allows the request to perform a cryptographic erase of the band data.

## Input Buffer

The input buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* must contain a [**DELETE\_BAND\_PARAMETERS**](set-band-metadata-parameters.md) and possibly an **AUTH\_KEY** structure.

If the **AuthKeyOffset** member of [**DELETE\_BAND\_PARAMETERS**](set-band-metadata-parameters.md) is set to **EHSTOR\_BANDMGR\_NO\_KEY**, the input data in the system buffer need not include an **AUTH\_KEY** structure.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* indicates the size, in bytes, of the buffer, which must be at least **sizeof** (DELETE\_BAND\_PARAMETERS) + **sizeof**(AUTH\_KEY).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value                     | Description                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                  | The band was successfully deleted.                                                      |
| STATUS\_INVALID\_DEVICE\_REQUEST | The storage device does not support band management.                                    |
| STATUS\_INVALID\_BUFFER\_SIZE    | The input buffer size is incorrect.                                                     |
| STATUS\_INVALID\_PARAMETER       | Information in the input buffer is invalid.                                             |
| STATUS\_ACCESS\_DENIED           | The authentication key is invalid or band is locked for writing.                        |
| STATUS\_NOT\_FOUND               | The band was not found for the selection criteria provided.                             |
| STATUS\_IO\_DEVICE\_ERROR        | Communication failed. The storage device might be incompatible with security protocols. |



 

## Remarks

An authentication key is required to delete a band without performing an erase first. To request a band erase, the **DELBAND\_ERASE\_BEFORE\_DELETE** flag is set in the **Flags** member of [**DELETE\_BAND\_PARAMETERS**](delete-band-parameters.md).

After a band delete, all LBAs contained in the deleted band are returned to the global band. The locking conditions for the global band now apply to the LBAs returned to the global band. The LBAs returned to the global band are now associated with the media key for the global band and encrypted data in those LBAs is unrecoverable.

The deleted band remains in the silo driver's band table but becomes unconfigured. The authentication key is reset to the default value, band and key metadata contains zeros, and the lock states revert to **PERSISTENT\_UNLOCK**. The band is now available for reconfiguration with an [**IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md) request.

Deleting a band without a cryptographic erase will not remove the encryption key for that band. It is possible to later create a band with the same configuration and band identifier as the deleted band. In this case, data previously stored in the band and not overwritten since the deletion of the previous band will be available. To avoid this situation, delete the band with the **DELBAND\_ERASE\_BEFORE\_DELETE** flag set in [**DELETE\_BAND\_PARAMETERS**](delete-band-parameters.md).

The **IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND** will not delete the global band. A request to do so will return **STATUS\_INVALID\_PARAMETER**.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                          |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**DELETE\_BAND\_PARAMETERS**](delete-band-parameters.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND**](ioctl-ehstor-bandmgmt-erase-band.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_DELETE_BAND%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






