---
title: IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES control code
description: The IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES request retrieves the banded security capabilities for a storage device. The IOCTL returns the capabilities as a BAND\_MANAGEMENT\_CAPABILITIES structure in the system buffer.
ms.assetid: '16D035EF-2234-4D5A-8D19-8CF3BA8B3590'
keywords: ["IOCTL_EHSTOR_BANDMGMT_QUERY_CAPABILITIES control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_QUERY_CAPABILITIES
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
---

# IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES control code

The **IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES** request retrieves the banded security capabilities for a storage device. The IOCTL returns the capabilities as a [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md) structure in the system buffer.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The output buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md) structure.

## Output Buffer Length

The length of a [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md) structure.

## Status block

The **Information** field contains the number of bytes returned in the output buffer. One of the following values can be returned in the **Status** field.



| Status Value                     | Description                                                                                                      |
|----------------------------------|------------------------------------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                  | The device supports band management and the security capabilities are returned in the system buffer.             |
| STATUS\_INVALID\_DEVICE\_REQUEST | Band management is not supported on the storage device.                                                          |
| STATUS\_INVALID\_DEVICE\_STATE   | The device provides band management support but not in its present configuration.                                |
| STATUS\_BUFFER\_OVERFLOW         | A buffer is not provided or its size is set to zero. The required size is returned in the **Information** field. |
| STATUS\_BUFFER\_TOO\_SMALL       | The buffer size is too small to return the output.                                                               |



 

## Remarks

A driver or application can query for the necessary output buffer size by setting the output buffer for the request to NULL and the output size to 0. The **IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES** request will return with the **Status** field of the *IoStatus* block set to STATUS\_BUFFER\_OVERFLOW and the **Information** field will contain the required buffer size.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_QUERY_CAPABILITIES%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






