---
Description: 'The PUBLISHERINFO structure is used as an input parameter to the IPrintOemPS::GetInfo method.'
ms.assetid: '6749b2e8-a9db-48a3-96e1-8592bcfa580d'
title: PUBLISHERINFO structure
---

# PUBLISHERINFO structure

The PUBLISHERINFO structure is used as an input parameter to the [**IPrintOemPS::GetInfo**](iprintoemps-getinfo.md) method.

## Syntax


```C++
typedef struct _PUBLISHERINFO {
  DWORD dwMode;
  WORD  wMinoutlinePPEM;
  WORD  wMaxbitmapPPEM;
} PUBLISHERINFO, *PPUBLISHERINFO;
```



## Members

<dl> <dt>

**dwMode**
</dt> <dd>

Is a set of bit flags. The only flag defined is OEM\_MODE\_PUBLISHER, which must be set if a rendering plug-in for Pscript5 is using "publishing mode".

</dd> <dt>

**wMinoutlinePPEM**
</dt> <dd>

Specifies the minimum font size, in pixels, for which the Pscript5 driver will download TrueType fonts as outline (Type 1) fonts. A font smaller than the minimum setting will be downloaded as a bitmap (Type 3) font.

</dd> <dt>

**wMaxbitmapPPEM**
</dt> <dd>

Specifies the maximum font size, in pixels, for which the Pscript5 driver will download TrueType fonts as bitmap (Type 3) fonts. A font larger than the maximum setting will be downloaded as an outline (Type 1) font.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemPS::GetInfo**](iprintoemps-getinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PUBLISHERINFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





