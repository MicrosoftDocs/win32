---
Description: 'The XPSRAS\_RENDERING\_MODE enumeration specifies the rendering mode to be used by an XPS rasterizer.'
ms.assetid: '8b0b2bde-6ada-4a73-9737-7150605b79c8'
title: 'XPSRAS\_RENDERING\_MODE enumeration'
---

# XPSRAS\_RENDERING\_MODE enumeration

The XPSRAS\_RENDERING\_MODE enumeration specifies the rendering mode to be used by an XPS rasterizer.

## Syntax


```C++
typedef enum  { 
  XPSRAS_RENDERING_MODE_ANTIALIASED  = 0,
  XPSRAS_RENDERING_MODE_ALIASED      = 1
} XPSRAS_RENDERING_MODE;
```



## Constants

<dl> <dt>

<span id="XPSRAS_RENDERING_MODE_ANTIALIASED"></span><span id="xpsras_rendering_mode_antialiased"></span>**XPSRAS\_RENDERING\_MODE\_ANTIALIASED**
</dt> <dd>

Use antialiasing to rasterize the specified graphics elements.

</dd> <dt>

<span id="XPSRAS_RENDERING_MODE_ALIASED"></span><span id="xpsras_rendering_mode_aliased"></span>**XPSRAS\_RENDERING\_MODE\_ALIASED**
</dt> <dd>

Do not use antialiasing to rasterize the specified graphics elements.

</dd> </dl>

## Remarks

The values defined in this enumeration are used by the [**IXpsRasterizationFactory::CreateRasterizer**](ixpsrasterizationfactory-createrasterizer.md) method.

For more information about rasterizing XPS documents, see [Using the XPS Rasterization Service](print.using_the_xps_rasterization_service).

## Requirements



|                            |                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------|
| Minimum support<br/> | Windows 7<br/>                                                                                         |
| Header<br/>          | <dl> <dt>Xpsrassvc.h (include Xpsrassvc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IXpsRasterizationFactory::CreateRasterizer**](ixpsrasterizationfactory-createrasterizer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSRAS_RENDERING_MODE%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





