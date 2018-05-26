---
title: IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA control code
description: Metadata associated with a band is retrieved with an IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA request. The metadata for a band serves as a data area for a key manager application.
ms.assetid: 543EB710-9BF5-428E-B5CE-7088B98586EA
keywords:
- IOCTL_EHSTOR_BANDMGMT_GET_BAND_METADATA control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_GET_BAND_METADATA
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

# IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA control code

Metadata associated with a band is retrieved with an **IOCTL\_EHSTOR\_BANDMGMT\_GET\_BAND\_METADATA** request. The metadata for a band serves as a data area for a key manager application.

## Input Buffer

The input buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* must contain a [**GET\_BAND\_METADATA\_PARAMETERS**](get-band-metadata-parameters.md) structure.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* indicates the size, in bytes, of the buffer, which must be at least **sizeof** (GET\_BAND\_METADATA\_PARAMETERS).

## Output Buffer

The output buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* contains a byte array of band metadata specified by [**GET\_BAND\_METADATA\_PARAMETERS**](get-band-metadata-parameters.md).

## Output Buffer Length

The length of a [**GET\_BAND\_METADATA\_PARAMETERS**](get-band-metadata-parameters.md) structure.

## Status block

The **Information** field contains the number of bytes returned in the output buffer. One of the following values can be returned in the **Status** field.



| Status Value                     | Description                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                  | The metadata was returned in the system buffer.                                         |
| STATUS\_INVALID\_DEVICE\_REQUEST | The storage device does not support band management.                                    |
| STATUS\_INVALID\_BUFFER\_SIZE    | The output buffer size is incorrect.                                                    |
| STATUS\_INVALID\_PARAMETER       | Information in the input buffer is invalid.                                             |
| STATUS\_NOT\_FOUND               | The band was not found for the selection criteria provided.                             |
| STATUS\_IO\_DEVICE\_ERROR        | Communication failed. The storage device might be incompatible with security protocols. |



 

## Remarks

Authentication for this IOCTL is unnecessary and an authentication key is not included as input.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_GET_BAND_METADATA%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






