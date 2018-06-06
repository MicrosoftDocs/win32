---
Description: The IPrintOemUni::TextOutAsBitmap method allows a rendering plug-in to create a bitmap image of a text string, in case a downloadable font is not available.
ms.assetid: 2c144eb7-6279-490a-813c-6c0ae995c6ad
title: IPrintOemUni::TextOutAsBitmap method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::TextOutAsBitmap method

The `IPrintOemUni::TextOutAsBitmap` method allows a rendering plug-in to create a bitmap image of a text string, in case a downloadable font is not available.

## Syntax


```C++
HRESULT TextOutAsBitmap(
   SURFOBJ  *pso,
   STROBJ   *pstro,
   FONTOBJ  *pfo,
   CLIPOBJ  *pco,
   RECTL    *prclExtra,
   RECTL    *prclOpaque,
   BRUSHOBJ *pboFore,
   BRUSHOBJ *pboOpaque,
   POINTL   *pptlOrg,
   MIX      mix
);
```



## Parameters

<dl> <dt>

*pso* 
</dt> <dd>

Pointer to a [**SURFOBJ**](https://msdn.microsoft.com/cee7cb50-1e8a-422b-aebe-7030ae96fb34) structure that describes the surface on which to write.

</dd> <dt>

*pstro* 
</dt> <dd>

Pointer to a [**STROBJ**](https://msdn.microsoft.com/efe53cb8-39b9-4931-bac2-9c61efd9d457) structure that defines the glyphs to be rendered and the positions in which to place them.

</dd> <dt>

*pfo* 
</dt> <dd>

Pointer to a [**FONTOBJ**](https://msdn.microsoft.com/09af2006-51f1-433e-9227-3c99b9860e75) structure from which to retrieve information about the font and its glyphs.

</dd> <dt>

*pco* 
</dt> <dd>

Pointer to a [**CLIPOBJ**](https://msdn.microsoft.com/c3f632ed-f8d1-44bb-b2fb-6f7f2c71fd63) structure that defines the clip region through which all rendering must be done. The driver cannot affect any pixels outside the clip region.

</dd> <dt>

*prclExtra* 
</dt> <dd>

Pointer to a RECTL structure. GDI always sets this parameter to **NULL** in calls to this function. It should be ignored by the driver.

</dd> <dt>

*prclOpaque* 
</dt> <dd>

Pointer to a [**RECTL**](https://msdn.microsoft.com/709f8262-829e-4cda-bb0b-564307edfd24) structure that represents a single opaque rectangle. This rectangle is bottom-right exclusive. Pixels within this rectangle (those that are not foreground and not clipped) are to be rendered with the opaque brush. This rectangle always bounds the text to be drawn. If this parameter is **NULL**, no opaque pixels are to be rendered.

</dd> <dt>

*pboFore* 
</dt> <dd>

Pointer to a [**BRUSHOBJ**](https://msdn.microsoft.com/81216bee-d13f-4880-a839-337a247a6c82) structure that represents the brush object to be used for the foreground pixels. This brush will always be a solid color brush.

</dd> <dt>

*pboOpaque* 
</dt> <dd>

Pointer to a BRUSHOBJ structure that represents the opaque pixels. Both the foreground and background mix modes for this brush are assumed to be R2\_COPYPEN. Unless the driver sets the GCAPS\_ARBRUSHOPAQUE capabilities bit in the *flGraphicsCaps* member of the DEVINFO structure, it will always be called with a solid color brush.

</dd> <dt>

*pptlOrg* 
</dt> <dd>

Pointer to a [**POINTL**](https://msdn.microsoft.com/68cd23d7-7898-4132-abfe-4dda527889b9) structure that defines the brush origin for both brushes.

</dd> <dt>

*mix* 
</dt> <dd>

The foreground and background raster operations (mix modes) for *pboFore*.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::TextOutAsBitmap` method is called from Unidrv's [**IPrintOemDriverUni::DrvUniTextOut**](iprintoemdriveruni-drvunitextout.md) method, if that method cannot create the text string using downloadable fonts, either because the font is not available or is rotated. `IPrintOemUni::TextOutAsBitmap` should create a bitmap image of the text and send it to the print device.

The `IPrintOemUni::TextOutAsBitmap` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "TextOutAsBitmap" as input.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni**](iprintoemuni-interface.md)
</dt> <dt>

[**IPrintOemDriverUni::DrvUniTextOut**](iprintoemdriveruni-drvunitextout.md)
</dt> <dt>

[**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::TextOutAsBitmap%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





