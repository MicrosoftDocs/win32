---
title: IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY control code
description: The security properties of bands in a band-managed storage device are modified with the IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY request.
ms.assetid: CBA94AF4-649D-47C9-879B-4B939DE32BE2
keywords:
- IOCTL_EHSTOR_BANDMGMT_SET_BAND_SECURITY control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_SET_BAND_SECURITY
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY control code

The security properties of bands in a band-managed storage device are modified with the **IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY** request.

## Input Buffer

The buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* must contain a [**SET\_BAND\_SECURITY\_PARAMETERS**](set-band-security-parameters.md) structure followed by the **AUTH\_KEY** and [**BAND\_SECURITY\_INFO**](band-security-info.md) structures.

If the **AuthKeyOffset** member of [**SET\_BAND\_SECURITY\_PARAMETERS**](set-band-security-parameters.md) is set to **EHSTOR\_BANDMGR\_NO\_KEY**, the input data in the system buffer need not include an **AUTH\_KEY** structure. Also, if a new authentication key is not given, no updated key structure is included.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* indicates the size, in bytes, of the buffer, which must be at least **sizeof** (SET\_BAND\_SECURITY\_PARAMETERS) + 2 \* **sizeof**(AUTH\_KEY) + **sizeof**(BAND\_SECURITY\_INFO) when all input structures are required.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value                     | Description                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                  | Security properties for the band were changed.                                          |
| STATUS\_INVALID\_DEVICE\_REQUEST | The storage device does not support band management.                                    |
| STATUS\_INVALID\_BUFFER\_SIZE    | The input buffer size is invalid.                                                       |
| STATUS\_INVALID\_PARAMETER       | Information in the input buffer is invalid.                                             |
| STATUS\_NOT\_FOUND               | A band was not found for the selection criteria provided.                               |
| STATUS\_ACCESS\_DENIED           | The authentication key provided is not valid.                                           |
| STATUS\_IO\_DEVICE\_ERROR        | Communication failed. The storage device might be incompatible with security protocols. |



 

## Remarks

Read and write locking and unlocking for bands are set with this IOCTL in the [**BAND\_SECURITY\_INFO**](band-security-info.md) structure included as input in the system buffer.

Authentication key changes will not affect the lock state of the band. It is not necessary to unmount a volume to change an authentication key with this request.

When a band is unlocked, meaning either the **Readlock** or **WriteLock** members of [**BAND\_SECURITY\_INFO**](band-security-info.md) are FALSE, the silo driver will cache the provided authentication key if **SETBANDSEC\_AUTHKEY\_CACHING\_ENABLED** is set in the **Flags** member of [**SET\_BAND\_SECURITY\_PARAMETERS**](set-band-security-parameters.md).

As a special case, this IOCTL can be used to notify the silo driver that a band was unlocked without the use of the locking members in [**BAND\_SECURITY\_INFO**](band-security-info.md). To do this, the **NewAuthKeyOffset** member of [**SET\_BAND\_SECURITY\_PARAMETERS**](set-band-security-parameters.md) is set to **CurrentAuthKeyOffset** with **BandSecurityInfoOffset** set to 0. In this case, no security changes occur, but the key provided at **CurrentAuthKeyOffset** is cached in memory, provided that **SETBANDSEC\_AUTHKEY\_CACHING\_ENABLED** is set in **Flags**.

The changes made to the band table by this request are committed to the device atomically before the IOCTL request completes. Therefore, it is guaranteed that the band is modified with all of its properties set or no properties set at all should a system or power failure occur.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_SECURITY\_INFO**](band-security-info.md)
</dt> <dt>

[**SET\_BAND\_SECURITY\_PARAMETERS**](set-band-security-parameters.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-delete-band.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_SET_BAND_SECURITY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






