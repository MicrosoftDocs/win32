---
title: IOCTL\_STORAGE\_LOAD\_MEDIA2 control code
description: Causes media to be loaded in a device that the caller has opened with FILE\_READ\_ATTRIBUTES.
ms.assetid: 'ba458d46-9b5f-4ee3-80fa-59277e97fb4a'
keywords: ["IOCTL_STORAGE_LOAD_MEDIA2 control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_LOAD_MEDIA2
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# IOCTL\_STORAGE\_LOAD\_MEDIA2 control code

Causes media to be loaded in a device that the caller has opened with FILE\_READ\_ATTRIBUTES. Because no file system is mounted when a device is opened in this way, this request can be processed much more quickly than an [**IOCTL\_STORAGE\_LOAD\_MEDIA**](ioctl-storage-load-media.md) request.

Input, output, and I/O status block values for IOCTL\_STORAGE\_LOAD\_MEDIA2 are identical to those for IOCTL\_STORAGE\_LOAD\_MEDIA.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_NO\_MEDIA\_IN\_DEVICE, STATUS\_BUFFER\_TOO\_SMALL, or STATUS\_DEVICE\_NOT\_CONNECTED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_LOAD\_MEDIA**](ioctl-storage-load-media.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_LOAD_MEDIA2%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






