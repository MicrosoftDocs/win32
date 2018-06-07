---
Description: When RevertToPrinterSelf is called on an impersonating thread, it returns the token for the thread that is being impersonated.
ms.assetid: 3d94d363-fc8b-4b12-b90d-43dfc5923bdf
title: RevertToPrinterSelf function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RevertToPrinterSelf function

When `RevertToPrinterSelf` is called on an impersonating thread, it returns the token for the thread that is being impersonated.

## Syntax


```C++
HANDLE RevertToPrinterSelf(
    void
);
```



## Parameters

<dl> <dt>

*void* 
</dt> <dd></dd> </dl>

## Return value

If the operation succeeds, the function returns the token of the impersonated thread. If the current thread is not impersonating another thread, this function returns **NULL**.

## Remarks

`RevertToPrinterSelf` should be called when a component needs access to resources from the local system context, such as the registry. The local system context is the security context (the collection of settings that define the security behavior of a process or thread) of the system process. The system process is the process that runs in the logon session that is created for the local system account when the operating system boots.

If `RevertToPrinterSelf` returns a non-**NULL** value, [**ImpersonatePrinterClient**](impersonateprinterclient.md) must be called with the return value to complete the operation and clean up the thread handle.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                   |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**ImpersonatePrinterClient**](impersonateprinterclient.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RevertToPrinterSelf%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





