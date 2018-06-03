---
title: IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_METADATA control code
description: Metadata associated with a band is set with an IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_METADATA request. The metadata for a band serves as a data area for a key manager application.
ms.assetid: 5FBEAB29-C256-47EF-B673-6584679B8908
keywords:
- IOCTL_EHSTOR_BANDMGMT_SET_BAND_METADATA control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_SET_BAND_METADATA
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

# IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_METADATA control code

Metadata associated with a band is set with an **IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_METADATA** request. The metadata for a band serves as a data area for a key manager application.

## Input Buffer

The input buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* must contain a [**SET\_BAND\_METADATA\_PARAMETERS**](set-band-metadata-parameters.md) and possibly an **AUTH\_KEY** structure along with the new metadata to set for the band.

If the **AuthKeyOffset** member of [**SET\_BAND\_METADATA\_PARAMETERS**](set-band-metadata-parameters.md) is set to **EHSTOR\_BANDMGR\_NO\_KEY**, the input data in the system buffer need not include an **AUTH\_KEY** structure.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* indicates the size, in bytes, of the buffer, which must be at least **sizeof** (SET\_BAND\_METADATA\_PARAMETERS) + **MetadataSize** + **sizeof**(AUTH\_KEY).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values may be returned in the **Status** field:



| Status Value                     | Description                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                  | The metadata was set for the selected band.                                             |
| STATUS\_INVALID\_DEVICE\_REQUEST | Storage device does not support band management.                                        |
| STATUS\_INVALID\_BUFFER\_SIZE    | The input buffer size is incorrect.                                                     |
| STATUS\_INVALID\_PARAMETER       | Information in the input buffer is invalid.                                             |
| STATUS\_NOT\_FOUND               | Band was not found for the selection criteria provided.                                 |
| STATUS\_IO\_DEVICE\_ERROR        | Communication failed. The storage device might be incompatible with security protocols. |



 

## Remarks

Metadata can also be erased by using this IOCTL. To erase metadata for a band, set the metadata portion of input buffer to all zeros or some other erase pattern. To ensure removal of sensitive information in metadata blobs, this erase operation should be performed prior to deleting a band from the silo driver's band table.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 8 and later versions of Windows.<br/>                                                       |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**SET\_BAND\_METADATA\_PARAMETERS**](set-band-metadata-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_SET_BAND_METADATA%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






