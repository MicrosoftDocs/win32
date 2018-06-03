---
title: IOCTL\_STORAGE\_CHECK\_VERIFY2 control code
description: Determines whether the media has changed on a removable-media device - the caller has opened with FILE\_READ\_ATTRIBUTES.
ms.assetid: bac1e5ec-0e0c-4d7a-b260-2e73addd0abf
keywords:
- IOCTL_STORAGE_CHECK_VERIFY2 control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_CHECK_VERIFY2
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_CHECK\_VERIFY2 control code

Determines whether the media has changed on a removable-media device - the caller has opened with FILE\_READ\_ATTRIBUTES. Because no file system is mounted when a device is opened in this way, this request can be processed much more quickly than an IOCTL\_STORAGE\_CHECK\_VERIFY request.

## Input Buffer

Input is identical to the input for [**IOCTL\_STORAGE\_CHECK\_VERIFY**](ioctl-storage-check-verify.md).

## Input Buffer Length

Input length is identical to input length for [**IOCTL\_STORAGE\_CHECK\_VERIFY**](ioctl-storage-check-verify.md).

## Output Buffer

Output is identical to the output for [**IOCTL\_STORAGE\_CHECK\_VERIFY**](ioctl-storage-check-verify.md).

## Output Buffer Length

Output length is identical to output length for [**IOCTL\_STORAGE\_CHECK\_VERIFY**](ioctl-storage-check-verify.md).

## Status block

I/O status is identical to the I/O status for [**IOCTL\_STORAGE\_CHECK\_VERIFY**](ioctl-storage-check-verify.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_CHECK\_VERIFY**](ioctl-storage-check-verify.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_CHECK_VERIFY2%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






