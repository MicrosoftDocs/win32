---
Description: The DrvUnidriverTextOut function is obsolete.
ms.assetid: 72ba09b2-a889-439d-bbf2-ee6f9ebf5535
title: PFN\_DrvUnidriverTextOut callback function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PFN\_DrvUnidriverTextOut callback function

The **DrvUnidriverTextOut** function is obsolete.

Windows 2000 and later printer drivers should use [**IPrintOemDriverUni::DrvUniTextOut**](iprintoemdriveruni-drvunitextout.md).

This function pointer prototype defines the type of the **DrvUnidriverTextOut** member of the [**DRVPROCS**](drvprocs.md) structure.

## Syntax


```C++
 PFN_DrvUnidriverTextOut;

typedef BOOL APIENTRY* PFN_DrvUnidriverTextOut(
   SURFOBJ  *pso,
   STROBJ   *pstro,
   FONTOBJ  *pfo,
   CLIPOBJ  *pco,
   RECTL    *prclExtra,
   RECTL    *prclOpaque,
   BRUSHOBJ *pboFore,
   BRUSHOBJ *pboOpaque,
   POINTL   *pptlBrushOrg,
   MIX      mix
)
{ ... }
```



## Parameters

<dl> <dt>

*pso* 
</dt> <dd></dd> <dt>

*pstro* 
</dt> <dd></dd> <dt>

*pfo* 
</dt> <dd></dd> <dt>

*pco* 
</dt> <dd></dd> <dt>

*prclExtra* 
</dt> <dd></dd> <dt>

*prclOpaque* 
</dt> <dd></dd> <dt>

*pboFore* 
</dt> <dd></dd> <dt>

*pboOpaque* 
</dt> <dd></dd> <dt>

*pptlBrushOrg* 
</dt> <dd></dd> <dt>

*mix* 
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PFN_DrvUnidriverTextOut%20callback%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




