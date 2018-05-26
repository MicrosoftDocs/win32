---
Description: OEMEnablePDEV function
ms.assetid: 0088f5f6-eb68-4081-8cca-3d34fd10593a
title: OEMEnablePDEV function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OEMEnablePDEV function

## Syntax


```C++
PDEVOEM APIENTRY OEMEnablePDEV(
          PDEVOBJ                            pdevobj,
  _In_    PWSTR                              pPrinterName,
          ULONG                              cPatterns,
  _In_    _updates_(cPatterns) HSURF         *phsurfPatterns,
          ULONG                              cjGdiInfo,
  _Inout_ _updates_bytes_(cjGdiInfo) GDIINFO *pGdiInfo,
          ULONG                              cjDevInfo,
  _Inout_ _updates_bytes_(cjDevInfo) DEVINFO *pDevInfo,
  _In_    DRVENABLEDATA                      *pded
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd></dd> <dt>

*pPrinterName* \[in\]
</dt> <dd></dd> <dt>

*cPatterns* 
</dt> <dd></dd> <dt>

*phsurfPatterns* \[in\]
</dt> <dd></dd> <dt>

*cjGdiInfo* 
</dt> <dd></dd> <dt>

*pGdiInfo* \[in, out\]
</dt> <dd></dd> <dt>

*cjDevInfo* 
</dt> <dd></dd> <dt>

*pDevInfo* \[in, out\]
</dt> <dd></dd> <dt>

*pded* \[in\]
</dt> <dd></dd> </dl>

## 

This function is obsolete for Windows XP and later. It is supported only for earlier plug-ins. Use [**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md) (Pscript) or [**IPrintOemUni::EnablePDEV**](iprintoemuni-enablepdev.md) (Unidrv).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMEnablePDEV%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




