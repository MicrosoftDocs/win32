---
Description: The IOCTL\_USBPRINT\_GET\_1284\_ID control code allows upper-layer software (such as a language monitor), to request and obtain the printer's IEEE 1284 device ID string.
ms.assetid: b5c5a0e4-0fd9-4950-ac38-4bf58a0af077
title: IOCTL\_USBPRINT\_GET\_1284\_ID control code
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_USBPRINT\_GET\_1284\_ID control code

The **IOCTL\_USBPRINT\_GET\_1284\_ID** control code allows upper-layer software (such as a language monitor), to request and obtain the printer's IEEE 1284 device ID string.

## Input Buffer

Not used in this operation; set this parameter to **NULL**.

## Input Buffer Length

Not used in this operation; set this parameter to 0.

## Output Buffer

The output buffer will contain UCHAR data. On success this buffer can hold the following: a two-byte prefix that specifies the size, in bytes, of the device's IEEE 1284 device ID; the device ID; and a null terminator. An IEEE 1284 device ID can be up to 64 KB in size. On failure, if **GetLastError**returns the error code **STATUS\_BUFFER\_TOO\_SMALL**, the output buffer was not large enough to hold the data intended for it.

## Output Buffer Length

The output buffer must be large enough to contain a two-byte quantity holding the length of the device's IEEE 1284 device ID, the device ID (up to 64 KB in size), and a terminating null.

## Status block

**Irp-&gt;IoStatus.Status** is set to **STATUS\_SUCCESS** if the request is successful. Otherwise, **Status** to the appropriate error condition as a [NTSTATUS](https://www.bing.com/search?q=NTSTATUS) code.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Usbprint.h</dt> </dl> |



## See also

<dl> <dt>

[Creating IOCTL Requests in Drivers](https://www.bing.com/search?q=Creating+IOCTL+Requests+in+Drivers)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlOthersSynchronously**](https://msdn.microsoft.com/53070b37-3836-49c2-91d1-369552afe214)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlSynchronously**](https://msdn.microsoft.com/4028b259-a157-4e50-b1a2-25da3050cced)
</dt> <dt>

[**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/1c43f6cd-0026-4654-b3ce-71fd51b3821d)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IOCTL_USBPRINT_GET_1284_ID%20control%20code%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





