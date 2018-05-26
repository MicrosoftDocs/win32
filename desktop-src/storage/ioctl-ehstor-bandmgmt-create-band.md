---
title: IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND control code
description: New bands are created on a band-managed storage device with the IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND request. A new band is added to the table of band entries, which includes band location and security properties.
ms.assetid: B5AEA98A-223D-4D14-A36B-EB5266F80AF8
keywords:
- IOCTL_EHSTOR_BANDMGMT_CREATE_BAND control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_CREATE_BAND
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

# IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND control code

New bands are created on a band-managed storage device with the **IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND** request. A new band is added to the table of band entries, which includes band location and security properties.

## Input Buffer

The buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* must contain an [**CREATE\_BAND\_PARAMETERS**](create-band-parameters.md) structure followed by the [**BAND\_LOCATION\_INFO**](band-location-info.md), [**BAND\_SECURITY\_INFO**](band-security-info.md), and **AUTH\_KEY** structures.

If the **AuthKeyOffset** member of [**CREATE\_BAND\_PARAMETERS**](create-band-parameters.md) is set to **EHSTOR\_BANDMGR\_NO\_KEY**, the input data in the system buffer need not include an **AUTH\_KEY** structure.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* indicates the size, in bytes, of the buffer, which must be at least **sizeof** (CREATE\_BAND\_PARAMETERS) + **sizeof**(BAND\_LOCATION\_INFO) + **sizeof** (BAND\_SECURITY\_INFO) + **sizeof**(AUTH\_KEY).

## Output Buffer

The output buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* optionally contains a ULONG value for the identifier of the newly created band.

## Output Buffer Length

*Parameters.DeviceIoControl.OutputBufferLength* must be at least **sizeof**(ULONG) to receive the band identifier. If return of the band identifier is not wanted, set *Parameters.DeviceIoControl.OutputBufferLength* to 0.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value                     | Description                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                  | The new band was created.                                                               |
| STATUS\_INVALID\_DEVICE\_REQUEST | The storage device does not support band management.                                    |
| STATUS\_INVALID\_BUFFER\_SIZE    | The input buffer size is invalid.                                                       |
| STATUS\_INVALID\_PARAMETER       | Information in the input buffer is invalid.                                             |
| STATUS\_CONFLICTING\_ADDRESSES   | The band was not created due to overlapping locations.                                  |
| STATUS\_INSUFFICIENT\_RESOURCES  | The band was not created because the band table is already full.                        |
| STATUS\_IO\_DEVICE\_ERROR        | Communication failed. The storage device might be incompatible with security protocols. |



 

## Remarks

Assigning an authentication key to a newly created band is optional. If no key is provided, where **AuthKeyOffset** = **EHSTOR\_BANDMGR\_NO\_KEY** in the [**CREATE\_BAND\_PARAMETERS**](create-band-parameters.md) structure, a default authentication key is used. However, this leaves the band vulnerable to another caller who may take control over the band immediately after its creation by changing its authentication key. It is recommended to assign a non-default authentication key to the band at creation time.

The changes made to the band table by this request are committed to the device atomically before the IOCTL request completes. Therefore, it is guaranteed that the band is created with all of its properties set or not created at all should a system or power failure occur.

The location of the new band must not overlap with an existing band or this request will fail with STATUS\_CONFLICTING\_ADDRESSES.

If the band is unlocked, either the **ReadLock** or **WriteLock** members of [**BAND\_SECURITY\_INFO**](band-security-info.md) are set to FALSE, and **CREATEBAND\_AUTHKEY\_CACHING\_ENABLED** is set in the **Flags** member of [**CREATE\_BAND\_PARAMETERS**](create-band-parameters.md), then credential caching is enabled. The authentication silo driver will cache the band authentication key in memory. This allows the silo driver to automatically authenticate host access to the storage device when volume maintenance is required, such as resizing the band.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_LOCATION\_INFO**](band-location-info.md)
</dt> <dt>

[**BAND\_SECURITY\_INFO**](band-security-info.md)
</dt> <dt>

[**CREATE\_BAND\_PARAMETERS**](create-band-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_CREATE_BAND%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






