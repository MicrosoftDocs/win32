---
title: IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_LOCATION control code
description: The location properties of bands in a band-managed storage device are modified with the IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_LOCATION request.
ms.assetid: FE6DA52C-6EE3-450E-A559-A7BCE47FA327
keywords:
- IOCTL_EHSTOR_BANDMGMT_SET_BAND_LOCATION control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_SET_BAND_LOCATION
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

# IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_LOCATION control code

The location properties of bands in a band-managed storage device are modified with the **IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_LOCATION** request.

## Input Buffer

The buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* must contain a [**SET\_BAND\_LOCATION\_PARAMETERS**](set-band-location-parameters.md) structure followed by the **AUTH\_KEY** and [**BAND\_LOCATION\_INFO**](band-location-info.md) structures.

If the **AuthKeyOffset** member of [**SET\_BAND\_LOCATION\_PARAMETERS**](set-band-location-parameters.md) is set to **EHSTOR\_BANDMGR\_NO\_KEY**, the input data in the system buffer need not include an **AUTH\_KEY** structure.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* indicates the size, in bytes, of the buffer, which must be at least **sizeof** (SET\_BAND\_LOCATION\_PARAMETERS) + **sizeof**(AUTH\_KEY) + **sizeof**(BAND\_LOCATION\_INFO).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value                     | Description                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                  | The location properties for the band were changed.                                      |
| STATUS\_INVALID\_DEVICE\_REQUEST | The storage device does not support band management.                                    |
| STATUS\_INVALID\_BUFFER\_SIZE    | The input buffer size is invalid.                                                       |
| STATUS\_INVALID\_PARAMETER       | Information in the input buffer is invalid.                                             |
| STATUS\_NOT\_FOUND               | The band was not found for the selection criteria provided.                             |
| STATUS\_ACCESS\_DENIED           | The authentication key provided is not valid.                                           |
| STATUS\_IO\_DEVICE\_ERROR        | Communication failed. The storage device might be incompatible with security protocols. |



 

## Remarks

Data in LBAs that remains after resizing is not modified by the operation. Also, it is unnecessary to unmount a volume during a resize operation if the LBA range that spans the volume remains within the band after resizing.

The changes made to the band table by this request are committed to the device atomically before the IOCTL request completes. Therefore, it is guaranteed that the band is modified with all of its properties set or no properties set at all should a system or power failure occur.

The **BandSize** member of [**BAND\_LOCATION\_INFO**](band-location-info.md) must be greater than 0. This IOCTL cannot resize a band to 0 to cause a band deletion. To delete a band, the [**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md) request is used.

If [**BAND\_LOCATION\_INFO**](band-location-info.md) specifies properties for the global band, **BandStart** must be set to 0 and **BandSize** must be set to  1.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_LOCATION\_INFO**](band-location-info.md)
</dt> <dt>

[**SET\_BAND\_LOCATION\_PARAMETERS**](set-band-location-parameters.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-delete-band.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_SET_BAND_LOCATION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






