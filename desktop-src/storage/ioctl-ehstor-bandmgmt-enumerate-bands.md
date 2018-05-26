---
title: IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS control code
description: This IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS request is sent to retrieve the list of bands for a storage device under band management. Banding information is returned in a table of band entries that includes band location and security properties.
ms.assetid: 80F7546C-3683-460B-A0D9-AD41386E6195
keywords:
- IOCTL_EHSTOR_BANDMGMT_ENUMERATE_BANDS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_ENUMERATE_BANDS
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

# IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS control code

This **IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS** request is sent to retrieve the list of bands for a storage device under band management. Banding information is returned in a table of band entries that includes band location and security properties.

## Input Buffer

The buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* must contain an [**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md) structure.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* indicates the size, in bytes, of the buffer, which must be at least **sizeof** (ENUMERATE\_BANDS\_PARAMETERS).

## Output Buffer

The buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* contains a [**BAND\_TABLE**](enumerate-bands-parameters.md) structure followed by **BandTableEntryCount** band entries.

## Output Buffer Length

The length of a [**BAND\_TABLE**](enumerate-bands-parameters.md) structure followed by **BandTableEntryCount** band entries.

## Status block

The **Information** field contains the number of bytes returned in the output buffer. One of the following values can be returned in the **Status** field.



| Status Value                     | Description                                                                                                   |
|----------------------------------|---------------------------------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                  | Security features on the storage device were deactivated.                                                     |
| STATUS\_INVALID\_DEVICE\_REQUEST | The storage device does not support band management.                                                          |
| STATUS\_INVALID\_BUFFER\_SIZE    | The input buffer size is invalid.                                                                             |
| STATUS\_INVALID\_PARAMETER       | Information in the input buffer is invalid.                                                                   |
| STATUS\_NOT\_FOUND               | No bands are configured for the enumeration parameters provided.                                              |
| STATUS\_BUFFER\_OVERFLOW         | A buffer is not provided or its size set to zero. The required size is returned in the **Information** field. |
| STATUS\_IO\_DEVICE\_ERROR        | Communication failed. The storage device might be incompatible with security protocols.                       |
| STATUS\_BUFFER\_TOO\_SMALL       | The output buffer supplied is not large enough to hold the output data returned.                              |



 

## Remarks

A driver or application can query for the necessary output buffer size by setting the output buffer for the request to NULL and the output size to 0. The **IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS** request will return with the **Status** field of the *IoStatus* block set to STATUS\_BUFFER\_OVERFLOW and the **Information** field will contain the required buffer size.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                          |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_TABLE**](enumerate-bands-parameters.md)
</dt> <dt>

**ENUMERATE\_BANDS\_PARAMETERS**
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_ENUMERATE_BANDS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






