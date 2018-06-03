---
Description: ImpersonatePrinterClient resumes impersonation of the client, completing the operation begun by RevertToPrinterSelf.
ms.assetid: 8e110b2a-9d13-4e2e-8f27-5a48d838fb3c
title: ImpersonatePrinterClient function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ImpersonatePrinterClient function

ImpersonatePrinterClient resumes impersonation of the client, completing the operation begun by [**RevertToPrinterSelf**](reverttoprinterself.md).

## Syntax


```C++
BOOL ImpersonatePrinterClient(
  _In_ HANDLE hToken
);
```



## Parameters

<dl> <dt>

*hToken* \[in\]
</dt> <dd>

Caller-supplied handle to a thread. This parameter must have been previously returned by a call to [**RevertToPrinterSelf**](reverttoprinterself.md).

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise the function returns **FALSE**. The caller can obtain an error code by calling GetLastError (described in the Microsoft Windows SDK documentation).

## Remarks

This function must be called after a successful call to [**RevertToPrinterSelf**](reverttoprinterself.md). It resumes impersonation of the client and cleans up the thread handle.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                   |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**RevertToPrinterSelf**](reverttoprinterself.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ImpersonatePrinterClient%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





