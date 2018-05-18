---
Description: 'The PDEV\_HOSTFONT\_ENABLED structure indicates whether the Hostfont feature is enabled.'
ms.assetid: 'f7fc7e33-e80b-449e-a1d1-a93740cd967c'
title: 'PDEV\_HOSTFONT\_ENABLED structure'
---

# PDEV\_HOSTFONT\_ENABLED structure

The PDEV\_HOSTFONT\_ENABLED structure indicates whether the Hostfont feature is enabled.

## Syntax


```C++
typedef struct _PDEV_HOSTFONT_ENABLED {
  BOOL bHostfontEnabled;
} PDEV_HOSTFONT_ENABLED;
```



## Members

<dl> <dt>

**bHostfontEnabled**
</dt> <dd>

Specifies whether the Hostfont feature is enabled. If set to **TRUE**, the Hostfont feature is enabled. Otherwise, this feature is disabled.

</dd> </dl>

## Remarks

This structure is available in Windows XP and later.

The *pBuf* parameter of the [**IPrintOemPS2::GetPDEVAdjustment**](iprintoemps2-getpdevadjustment.md) method can point to a structure of this type.

Hostfont support is designed to improve the performance of a PostScript interpreter running on a host computer system, rather than on a physical printer. When the Hostfont feature is enabled, the Pscript5 driver stops converting and downloading host font data when there is already an identical font resident on the host on which the interpreter is running. This applies only to the following fonts:

-   a TrueType Font (TTF) converted to either a PostScript Type 42 or CID2 font

-   an OpenType Font (OTF) converted to either a PostScript Type 1 or CID0 font

-   a Printer Font Binary (PFB)

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemPS2::GetPDEVAdjustment**](iprintoemps2-getpdevadjustment.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PDEV_HOSTFONT_ENABLED%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





