---
Description: The OEMPlgBlt function provides rotate bit-block transfer capabilities between combinations of device-managed and GDI-managed surfaces.
ms.assetid: c33a9592-8e1b-4028-bd34-72cc4885f17f
title: OEMPlgBlt function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OEMPlgBlt function

The `OEMPlgBlt` function provides rotate bit-block transfer capabilities between combinations of device-managed and GDI-managed surfaces.

## Syntax


```C++
BOOL APIENTRY OEMPlgBlt(
   SURFOBJ         *psoDst,
   SURFOBJ         *psoSrc,
   SURFOBJ         *psoMask,
   CLIPOBJ         *pco,
   XLATEOBJ        *pxlo,
   COLORADJUSTMENT *pca,
   POINTL          *pptlBrushOrg,
   POINTFIX        *pptfixDest,
   RECTL           *prclSrc,
   POINTL          *pptlMask,
   ULONG           iMode
);
```



## Parameters

<dl> <dt>

*psoDst* 
</dt> <dd></dd> <dt>

*psoSrc* 
</dt> <dd></dd> <dt>

*psoMask* 
</dt> <dd></dd> <dt>

*pco* 
</dt> <dd></dd> <dt>

*pxlo* 
</dt> <dd></dd> <dt>

*pca* 
</dt> <dd></dd> <dt>

*pptlBrushOrg* 
</dt> <dd></dd> <dt>

*pptfixDest* 
</dt> <dd></dd> <dt>

*prclSrc* 
</dt> <dd></dd> <dt>

*pptlMask* 
</dt> <dd></dd> <dt>

*iMode* 
</dt> <dd></dd> </dl>

## 

### Comments

See [**DrvPlgBlt**](https://www.bing.com/search?q=**DrvPlgBlt**).

This function is not supported on Windows NT 4.0 and earlier.

Do not directly hook out this drawing function. Instead, implement [**OEMEnableDriver**](oemenabledriver.md) so that it fills in a [**DRVENABLEDATA**](https://www.bing.com/search?q=**DRVENABLEDATA**) structure listing all of the drawing DDIs to be hooked out.

If you call into the core driver, cast the call using the **PFN\_DrvPlgBlt** function pointer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMPlgBlt%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




