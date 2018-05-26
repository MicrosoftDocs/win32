---
Description: .
ms.assetid: AFDA244D-D692-44C1-8BA3-5E1F013558D6
title: ProvidorFindFirstPrinterChangeNotification function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ProvidorFindFirstPrinterChangeNotification function

## Syntax


```C++
BOOL WINAPI ProvidorFindFirstPrinterChangeNotification(
  _In_      HANDLE                   hPrinter,
            DWORD                    fdwFlags,
            DWORD                    fdwOptions,
  _In_      HANDLE                   hNotify,
  _In_opt_  PVOID                    pPrinterNotifyOptions,
  _Out_opt_ PVOID                    pvReserved1
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd></dd> <dt>

*fdwFlags* 
</dt> <dd></dd> <dt>

*fdwOptions* 
</dt> <dd></dd> <dt>

*hNotify* \[in\]
</dt> <dd></dd> <dt>

*pPrinterNotifyOptions* \[in, optional\]
</dt> <dd></dd> <dt>

*pvReserved1* \[out, optional\]
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ProvidorFindFirstPrinterChangeNotification%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




