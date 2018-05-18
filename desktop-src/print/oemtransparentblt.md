---
Description: 'The OEMTransparentBlt function provides bit-block transfer capabilities with transparency.'
ms.assetid: '0ffd4759-cabe-4efe-a725-5b8ff26fda77'
title: OEMTransparentBlt function
---

# OEMTransparentBlt function

The `OEMTransparentBlt` function provides bit-block transfer capabilities with transparency.

## Syntax


```C++
BOOL APIENTRY OEMTransparentBlt(
   SURFOBJ  *psoDst,
   STRFOBJ  *psoSrc,
   CLIPOBJ  *pco,
   XLATEOBJ *pxlo,
   RECTL    *prclDst,
   RECTL    *prclSrc,
   ULONG    iTransColor,
   ULONG    ulReserved
);
```



## Parameters

<dl> <dt>

*psoDst* 
</dt> <dd></dd> <dt>

*psoSrc* 
</dt> <dd></dd> <dt>

*pco* 
</dt> <dd></dd> <dt>

*pxlo* 
</dt> <dd></dd> <dt>

*prclDst* 
</dt> <dd></dd> <dt>

*prclSrc* 
</dt> <dd></dd> <dt>

*iTransColor* 
</dt> <dd></dd> <dt>

*ulReserved* 
</dt> <dd></dd> </dl>

## 

### Comments

See [**DrvTransparentBlt**](display.drvtransparentblt).

This function is not supported on Windows NT 4.0 and earlier.

Do not directly hook out this drawing function. Instead, implement [**OEMEnableDriver**](oemenabledriver.md) so that it fills in a [**DRVENABLEDATA**](display.drvenabledata) structure listing all of the drawing DDIs to be hooked out.

If you call into the core driver, cast the call using the **PFN\_DrvTransparentBlt** function pointer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMTransparentBlt%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




