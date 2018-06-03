---
Description: .
ms.assetid: 429A5DF5-46A6-4A41-A77B-4D5743C841DC
title: SpoolerFindFirstPrinterChangeNotification function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SpoolerFindFirstPrinterChangeNotification function

## Syntax


```C++
BOOL WINAPI SpoolerFindFirstPrinterChangeNotification(
  _In_      HANDLE                   hPrinter,
            DWORD                    fdwFilterFlags,
            DWORD                    fdwOptions,
  _In_      PVOID                    pPrinterNotifyOptions,
  _In_opt_  PVOID                    pvReserved,
  _In_      PVOID                    pNotificationConfig,
  _Out_opt_ PHANDLE                  phNotify,
  _Out_opt_ PHANDLE                  phEvent
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd></dd> <dt>

*fdwFilterFlags* 
</dt> <dd></dd> <dt>

*fdwOptions* 
</dt> <dd></dd> <dt>

*pPrinterNotifyOptions* \[in\]
</dt> <dd></dd> <dt>

*pvReserved* \[in, optional\]
</dt> <dd></dd> <dt>

*pNotificationConfig* \[in\]
</dt> <dd></dd> <dt>

*phNotify* \[out, optional\]
</dt> <dd></dd> <dt>

*phEvent* \[out, optional\]
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SpoolerFindFirstPrinterChangeNotification%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




