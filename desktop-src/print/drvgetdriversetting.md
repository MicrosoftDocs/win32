---
Description: 'The DrvGetDriverSetting function is obsolete.'
ms.assetid: '04473567-42ac-4d99-947d-6ec7b3bde90b'
title: 'PFN\_DrvGetDriverSetting callback function'
---

# PFN\_DrvGetDriverSetting callback function

The **DrvGetDriverSetting** function is obsolete.

Windows 2000 and later printer drivers should use [**IPrintOemDriverUI::DrvGetDriverSetting**](iprintoemdriverui-drvgetdriversetting.md), [**IPrintCoreUI2::DrvGetDriverSetting**](iprintcoreui2-drvgetdriversetting.md) (UI plug-ins), [**IPrintOemDriverUni::DrvGetDriverSetting**](iprintoemdriveruni-drvgetdriversetting.md) (Unidrv plug-ins) or [**IPrintOemDriverPS::DrvGetDriverSetting**](iprintoemdriverps-drvgetdriversetting.md) (Pscript plug-ins)

This function pointer type defines the type of the **DrvGetDriverSetting** member of the [**OEMUIPROCS**](oemuiprocs.md) and [**DRVPROCS**](drvprocs.md) structures.

## Syntax


```C++
PFN_DrvGetDriverSetting DrvGetDriverSetting;

BOOL APIENTRY* DrvGetDriverSetting(
            PVOID                                pdriverobj,
            PCSTR                                Feature,
            _Out_writes_bytes_opt_(cbSize) PVOID pOutput,
            DWORD                                cbSize,
  _Out_opt_ PDWORD                               pcbNeeded,
  _Out_opt_  PDWORD                              pdwOptionsReturned
)
{ ... }
```



## Parameters

<dl> <dt>

*pdriverobj* 
</dt> <dd></dd> <dt>

*Feature* 
</dt> <dd></dd> <dt>

*pOutput* 
</dt> <dd></dd> <dt>

*cbSize* 
</dt> <dd></dd> <dt>

*pcbNeeded* \[out, optional\]
</dt> <dd></dd> <dt>

*pdwOptionsReturned* \[out, optional\]
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PFN_DrvGetDriverSetting%20callback%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




