---
Description: The OEMGradientFill function shades the specified primitives.
ms.assetid: 8a25d44b-c83b-4454-858b-117dbb6cc4b7
title: OEMGradientFill function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OEMGradientFill function

The `OEMGradientFill` function shades the specified primitives.

## Syntax


```C++
BOOL APIENTRY OEMGradientFill(
   SURFOBJ   *psoDest,
   CLIPOBJ   *pco,
   XLATEOBJ  *pxlo,
   TRIVERTEX *pVertex,
   ULONG     nVertex,
   PVOID     pMesh,
   ULONG     nMesh,
   RECTL     *prclExtents,
   POINTL    *pptlDitherOrg,
   ULONG     ulMode
);
```



## Parameters

<dl> <dt>

*psoDest* 
</dt> <dd></dd> <dt>

*pco* 
</dt> <dd></dd> <dt>

*pxlo* 
</dt> <dd></dd> <dt>

*pVertex* 
</dt> <dd></dd> <dt>

*nVertex* 
</dt> <dd></dd> <dt>

*pMesh* 
</dt> <dd></dd> <dt>

*nMesh* 
</dt> <dd></dd> <dt>

*prclExtents* 
</dt> <dd></dd> <dt>

*pptlDitherOrg* 
</dt> <dd></dd> <dt>

*ulMode* 
</dt> <dd></dd> </dl>

## 

### Comments

See [**DrvGradientFill**](https://msdn.microsoft.com/c8a51b5f-5509-4801-8432-c4d895cefbda).

This function is not supported on Windows NT 4.0 and earlier.

Do not directly hook out this drawing function. Instead, implement [**OEMEnableDriver**](oemenabledriver.md) so that it fills in a [**DRVENABLEDATA**](https://msdn.microsoft.com/dbeaecf8-dea1-4412-babb-6e40bf5dc7b0) structure listing all of the drawing DDIs to be hooked out.

If you call into the core driver, cast the call using the **PFN\_DrvGradientFill** function pointer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMGradientFill%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




