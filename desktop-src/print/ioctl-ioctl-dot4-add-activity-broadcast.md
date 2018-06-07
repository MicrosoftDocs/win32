---
Description: This topic describes IOCTL\_DOT4\_ADD\_ACTIVITY\_BROADCAST.
ms.assetid: 5B4E96FB-3214-4303-B8EB-9AB5CB42D8C7
title: IOCTL\_DOT4\_ADD\_ACTIVITY\_BROADCAST control code
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_DOT4\_ADD\_ACTIVITY\_BROADCAST control code

This topic describes **IOCTL\_DOT4\_ADD\_ACTIVITY\_BROADCAST**.

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

[Creating IOCTL Requests in Drivers](https://www.bing.com/search?q=Creating+IOCTL+Requests+in+Drivers)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlOthersSynchronously**](https://msdn.microsoft.com/53070b37-3836-49c2-91d1-369552afe214)
</dt> <dt>

[**WdfIoTargetSendInternalIoctlSynchronously**](https://msdn.microsoft.com/4028b259-a157-4e50-b1a2-25da3050cced)
</dt> <dt>

[**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/1c43f6cd-0026-4654-b3ce-71fd51b3821d)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IOCTL_DOT4_ADD_ACTIVITY_BROADCAST%20control%20code%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





