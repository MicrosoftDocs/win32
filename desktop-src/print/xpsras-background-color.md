---
ms.assetid: '0B4C1BAC-173E-42E9-8805-028FE165D49D'
title: 'XPSRAS\_BACKGROUND\_COLOR enumeration'
---

# XPSRAS\_BACKGROUND\_COLOR enumeration

**XPSRAS\_BACKGROUND\_COLOR** specifies the background clear color to be used by an XPS rasterizer:

## Syntax


```C++
typedef enum _XPSRAS_BACKGROUND_COLOR { 
  XPSRAS_BACKGROUND_COLOR_TRANSPARENT  = 0,
  XPSRAS_BACKGROUND_COLOR_OPAQUE       = 1
} XPSRAS_BACKGROUND_COLOR;
```



## Constants

<dl> <dt>

<span id="XPSRAS_BACKGROUND_COLOR_TRANSPARENT"></span><span id="xpsras_background_color_transparent"></span>**XPSRAS\_BACKGROUND\_COLOR\_TRANSPARENT**
</dt> <dd>

Use transparent white as clear color.

</dd> <dt>

<span id="XPSRAS_BACKGROUND_COLOR_OPAQUE"></span><span id="xpsras_background_color_opaque"></span>**XPSRAS\_BACKGROUND\_COLOR\_OPAQUE**
</dt> <dd>

Use opaque white as clear color.

</dd> </dl>

## Requirements



|                            |                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------|
| Minimum support<br/> | Windows 10<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Xpsrassvc.h (include Xpsrassvc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IXpsRasterizationFactory2::CreateRasterizer**](ixpsrasterizationfactory2-createrasterizer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSRAS_BACKGROUND_COLOR%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





