---
Description: OEMGetInfo function
ms.assetid: '69df63ac-2468-49d3-87ac-1930b718dddf'
title: OEMGetInfo function
---

# OEMGetInfo function

## Syntax


```C++
BOOL APIENTRY OEMGetInfo(
        DWORD                        dwMode,
  _Out_ _writes_bytes_(cbSize) PVOID pBuffer,
        DWORD                        cbSize,
  _Out_ DWORD                        pcbNeeded
);
```



## Parameters

<dl> <dt>

*dwMode* 
</dt> <dd></dd> <dt>

*pBuffer* \[out\]
</dt> <dd></dd> <dt>

*cbSize* 
</dt> <dd></dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd></dd> </dl>

## 

This function is obsolete for Windows XP and later. It is supported only for earlier plug-ins. For a UI plug-in, use [**IPrintOemUI::GetInfo**](iprintoemui-getinfo.md); for a Pscript plug-in, use [**IPrintOemPS::GetInfo**](iprintoemps-getinfo.md); for a Unidrv plug-in, use [**IPrintOemUni::GetInfo**](iprintoemuni-getinfo.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMGetInfo%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




