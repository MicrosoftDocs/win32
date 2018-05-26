---
Description: .
ms.assetid: 97D8FEEA-B6D7-4AD7-A067-B503AF8F23FF
title: ROUTER\_NOTIFY\_CALLBACK callback function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ROUTER\_NOTIFY\_CALLBACK callback function

## Syntax


```C++
ROUTER_NOTIFY_CALLBACK ROUTER_NOTIFY_CALLBACK;

 ROUTER_NOTIFY_CALLBACK(
  _In_  DWORD                    dwCommand,
  _In_  PVOID                    pContext,
  _In_  DWORD                    dwColor,
  _In_  PPRINTER_NOTIFY_INFO     pNofityInfo,
  _In_  DWORD                    fdwFlags,
  _Out_ PDWORD                   pdwResult
)
{ ... }
```



## Parameters

<dl> <dt>

*dwCommand* \[in\]
</dt> <dd></dd> <dt>

*pContext* \[in\]
</dt> <dd></dd> <dt>

*dwColor* \[in\]
</dt> <dd></dd> <dt>

*pNofityInfo* \[in\]
</dt> <dd></dd> <dt>

*fdwFlags* \[in\]
</dt> <dd></dd> <dt>

*pdwResult* \[out\]
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ROUTER_NOTIFY_CALLBACK%20callback%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




