---
Description: '.'
ms.assetid: '0C5E2279-79D0-40A2-BA5B-66994A22E963'
title: EnumJobNamedProperties function
---

# EnumJobNamedProperties function

## Syntax


```C++
DWORD WINAPI EnumJobNamedProperties(
  _In_  HANDLE              hPrinter,
  _In_  DWORD               JobId,
  _Out_ DWORD               *pcProperties,
  _Out_ PrintNamedProperty  **ppProperties
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd></dd> <dt>

*JobId* \[in\]
</dt> <dd></dd> <dt>

*pcProperties* \[out\]
</dt> <dd></dd> <dt>

*ppProperties* \[out\]
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winspool.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EnumJobNamedProperties%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




