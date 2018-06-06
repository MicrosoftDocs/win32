---
Description: The UNIFONTOBJ structure is used as an input parameter to font functions in rendering plug-ins.
ms.assetid: ff3ecef2-abf2-4ecb-b4af-81e6c6d8fb4c
title: UNIFONTOBJ structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# UNIFONTOBJ structure

The UNIFONTOBJ structure is used as an input parameter to font functions in rendering plug-ins.

## Syntax


```C++
typedef struct _UNIFONTOBJ {
  ULONG      ulFontID;
  DWORD      dwFlags;
  IFIMETRICS *pIFIMetrics;
  PFNGETINFO pfnGetInfo;
} UNIFONTOBJ, *PUNIFONTOBJ;
```



## Members

<dl> <dt>

**ulFontID**
</dt> <dd>

Specifies a resource identifier for an RC\_UFM resource contained in a Unidrv minidriver's resource DLL. Supplied by Unidrv.

</dd> <dt>

**dwFlags**
</dt> <dd>

Is a set of Unidrv-supplied bit flags. Flag definitions are as follows:



| Flag                                       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UFOFLAG\_TTDOWNLOAD\_BITMAP<br/>     | If set, the font is a bitmap font.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| UFOFLAG\_TTDOWNLOAD\_TTOUTLINE<br/>  | If set, the font is a TrueType outline font.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| UFOFLAG\_TTFONT<br/>                 | If set, the font is a downloadable TrueType font.<br/> If not set, the font is a device font.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| UFOFLAG\_TTOUTLINE\_BOLD\_SIM<br/>   | If set, the TrueType font has bold simulation done by GDI.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| UFOFLAG\_TTOUTLINE\_ITALIC\_SIM<br/> | If set, the TrueType font has italic simulation done by GDI.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| UFOFLAG\_TTOUTLINE\_VERTICAL<br/>    | If set, the TrueType font is a vertical font. Note that this flag is available only for those Asian fonts that can be written vertically.<br/> If not set, text is written horizontally.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| UFOFLAG\_TTSUBSTITUTED<br/>          | If set, the device font is a font substituted for the TrueType font. In the font substitution, GDI requests that Unidrv print using a TrueType font. For performance reasons, Unidrv substitutes a device font for the TrueType font. (The substitution is specified by a [*generic printer description (GPD)*](wdkgloss.g#wdkgloss-generic-printer-description--gpd-) file or in a table in the registry.) For this substitution, for some printers, it is necessary to adjust the baseline position of the device font, because the baseline position of the device font can be higher than that of the TrueType font. The adjustment causes the output of the substituted device font to be shifted down to correct this discrepancy. Depending on the flags set in the UNIFONTOBJ structure, the printer minidriver is able to adjust the baseline position of device fonts.<br/> |



 

</dd> <dt>

**pIFIMetrics**
</dt> <dd>

Pointer to an [**IFIMETRICS**](https://msdn.microsoft.com/fd2606ed-ec61-430a-aaad-38a4c3a207b6) structure. Supplied by Unidrv.

</dd> <dt>

**pfnGetInfo**
</dt> <dd>

Pointer to Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function. Supplied by Unidrv.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md)
</dt> <dt>

[**IFIMETRICS**](https://msdn.microsoft.com/fd2606ed-ec61-430a-aaad-38a4c3a207b6)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UNIFONTOBJ%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





