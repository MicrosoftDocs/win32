---
Description: .
ms.assetid: 86D8D605-3620-4F43-B4A5-6AF568265E92
title: SpoolerRefreshPrinterChangeNotification function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SpoolerRefreshPrinterChangeNotification function

## Syntax


```C++
BOOL WINAPI SpoolerRefreshPrinterChangeNotification(
  _In_        HANDLE                    hPrinter,
  _In_        DWORD                     dwColor,
  _In_        PPRINTER_NOTIFY_OPTIONS   pOptions,
  _Inout_opt_ PPRINTER_NOTIFY_INFO      ppInfo
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd></dd> <dt>

*dwColor* \[in\]
</dt> <dd></dd> <dt>

*pOptions* \[in\]
</dt> <dd></dd> <dt>

*ppInfo* \[in, out, optional\]
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SpoolerRefreshPrinterChangeNotification%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




