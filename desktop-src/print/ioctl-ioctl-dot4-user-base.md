---
Description: This topic describes IOCTL\_DOT4\_USER\_BASE.
ms.assetid: 600AF104-C80B-4ECE-A662-68CF38235078
title: IOCTL\_DOT4\_USER\_BASE control code
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_DOT4\_USER\_BASE control code

This topic describes **IOCTL\_DOT4\_USER\_BASE**.

## Input Buffer

## Input Buffer Length

## Output Buffer

## Output Buffer Length

## Input/Output Buffer

## Input/Output Buffer Length

## Status block

**Irp-&gt;IoStatus.Status** is set to STATUS\_SUCCESS if the request is successful. Otherwise, **Status** to the appropriate error condition as a [NTSTATUS](https://www.bing.com/search?q=NTSTATUS) code.

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D4drvif.h</dt> </dl> |



## See also

<dl> <dt>

[Creating IOCTL Requests in Drivers](https://www.bing.com/search?q=Creating IOCTL Requests in Drivers)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlOthersSynchronously**](https://www.bing.com/search?q=**WdfIoTargetSendInternalIoctlOthersSynchronously**)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlSynchronously**](https://www.bing.com/search?q=**WdfIoTargetSendInternalIoctlSynchronously**)
</dt> <dt>

[**WdfIoTargetSendIoctlSynchronously**](https://www.bing.com/search?q=**WdfIoTargetSendIoctlSynchronously**)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IOCTL_DOT4_USER_BASE%20control%20code%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





