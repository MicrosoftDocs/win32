---
Description: The CreateRasterize method creates an XPS rasterizer object.
ms.assetid: 07d4f1ed-5dbe-47c1-96e8-dfe21e0c1d0d
title: IXpsRasterizationFactory::CreateRasterizer method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IXpsRasterizationFactory::CreateRasterizer method

The `CreateRasterize` method creates an XPS rasterizer object.

## Syntax


```C++
HRESULT CreateRasterizer(
  [in, optional]  IXpsOMPage            *xpsPage,
  [in]            FLOAT                 DPI,
  [in]            XPSRAS_RENDERING_MODE nonTextRenderingMode,
  [in]            XPSRAS_RENDERING_MODE textRenderingMode,
  [out, optional] IXpsRasterizer        **ppIXPSRasterizer
);
```



## Parameters

<dl> <dt>

*xpsPage* \[in, optional\]
</dt> <dd>

Pointer to an **IXpsOMPage** object that represents the XPS fixed page to render. This object encapsulates a FixedPage section from an XPS document. For more information about **IXpsOMPage**, see [IXpsOMPage](http://go.microsoft.com/fwlink/p/?linkid=146349)<span class="underline">.</span>

</dd> <dt>

*DPI* \[in\]
</dt> <dd>

Dots per inch in the rasterized output. This parameter applies to both the x and y dimensions of the output bitmap. The *DPI* value is the resolution of the device that is to print or display the XPS fixed page.

</dd> <dt>

*nonTextRenderingMode* \[in\]
</dt> <dd>

Rendering mode for nontext items in the rasterized output. This parameter indicates whether to generate antialiased output. Set this parameter to one of the following [**XPSRAS\_RENDERING\_MODE**](xpsras-rendering-mode-enumeration.md) enumeration values:

-   XPSRAS\_RENDERING\_MODE\_ANTIALIASED

-   XPSRAS\_RENDERING\_MODE\_ALIASED

</dd> <dt>

*textRenderingMode* \[in\]
</dt> <dd>

Rendering mode for text in the rasterized output. This parameter indicates whether to generate antialiased output. Set this parameter to one of the following XPSRAS\_RENDERING\_MODE enumeration values:

-   XPSRAS\_RENDERING\_MODE\_ANTIALIASED

-   XPSRAS\_RENDERING\_MODE\_ALIASED

</dd> <dt>

*ppIXPSRasterizer* \[out, optional\]
</dt> <dd>

This parameter points to a location into which the method writes a pointer to the [IXpsRasterizer](ixpsrasterizer-interface.md) interface of the newly created XPS rasterizer object. If the method fails, it writes **NULL** to this location and returns an error code.

</dd> </dl>

## Return value

`CreateRasterizer` returns S\_OK if the call was successful. Otherwise, the method returns an error code. Possible error return values include:



| Return code                                                                                   | Description                                                                                                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl>     | Parameter *xpsPage* or *ppIXPSRasterizer* is **NULL**.<br/>                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Parameter *nonTextRenderingMode* or *textRenderingMode* is not a valid XPSRAS\_RENDERING\_MODE enumeration value.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                                                                                                    |



 

## Remarks

This method is supported in Windows 7 and later. It is not supported in versions of the Windows operating system before Windows 7.

Typically, an XPSDrv filter in an XPS pipeline calls this method to obtain an XPS rasterizer. It then uses the rasterizer to rasterize the XPS fixed page encapsulated by the object to which the parameter *xpsPage* points .

The parameter *DPI* specifies the printer resolution, which is assumed to be the same in both the horizontal and vertical dimensions. The width and height of the XPS fixed page, which can be obtained from the **IXpsOMPage::GetPageDimensions** method, are expressed in 1/96-inch units. Multiply these width and height values by *DPI*/96 to determine the width and height, in pixels, of the rasterized page. For more information about **IXpsOMPage::GetPageDimensions**, see [IXpsOMPage](http://go.microsoft.com/fwlink/p/?linkid=146350). For more information about how the XPS rasterizer object uses the DPI value, see [**IXpsRasterizer::RasterizeRect**](ixpsrasterizer-rasterizerect.md).

If successful, the method creates an XPS rasterizer object and passes to the caller a counted reference to the object's **IXpsRasterizer** interface. When the object is no longer needed, the caller is responsible for releasing the object by calling the [Release](http://go.microsoft.com/fwlink/p/?linkid=98433) method on the object's **IXpsRasterizer** interface.

If the method fails and *ppIXPSRasterizer* is non-**NULL**, the method sets \**ppIXPSRasterizer* = **NULL**.

For a code example that calls the `CreateRasterizer` method, see the XPSRasFilter sample in the WDK. This sample is located in the Src\\Print\\Xpsrasfilter folder in your WDK installation.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>     |
| Version<br/>         | Available in Windows 7 and later versions of the Windows operating system.<br/>  |
| Header<br/>          | <dl> <dt>Xpsrassvc.h</dt> </dl> |



## See also

<dl> <dt>

[**IXpsRasterizationFactory**](ixpsrasterizationfactory-interface.md)
</dt> <dt>

[IXpsRasterizer](ixpsrasterizer-interface.md)
</dt> <dt>

[**IXpsRasterizer::RasterizeRect**](ixpsrasterizer-rasterizerect.md)
</dt> <dt>

[**XPSRAS\_RENDERING\_MODE**](xpsras-rendering-mode-enumeration.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsRasterizationFactory::CreateRasterizer%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





