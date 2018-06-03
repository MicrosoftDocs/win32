---
Description: The GETINFO\_STDVAR structure is used as input to the UNIFONTOBJ\_GetInfo callback function.
ms.assetid: 9f2ae88c-34a4-46b3-9571-5f2f023b7d6b
title: GETINFO\_STDVAR structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# GETINFO\_STDVAR structure

The GETINFO\_STDVAR structure is used as input to the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

## Syntax


```C++
typedef struct _GETINFO_STDVAR {
  DWORD  dwSize;
  DWORD  dwNumOfVariable;
  struct {
    DWORD dwStdVarID;
    LONG  lStdVariable;
  } StdVar[1];
} GETINFO_STDVAR, *PGETINFO_STDVAR;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Specifies the size, in bytes, of the GETINFO\_STDVAR structure. Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**dwNumOfVariable**
</dt> <dd></dd> <dt>

**StdVar**
</dt> <dd>

Is an array specifying standard variable indexes and values. Each array element contains two members: a **dwStdVarID** member and an **lStdVariable** member.

<dl> <dt>

**dwStdVarID**
</dt> <dd>

Specifies the [standard variables](https://www.bing.com/search?q=standard variables) for which a value should be returned. Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller. Valid values are contained in the following table.



| Identifier                                | Standard Variable                |
|-------------------------------------------|----------------------------------|
| FNT\_INFO\_CURRENTFONTID<br/>       | `CurrentFontID`<br/>       |
| FNT\_INFO\_FONTBOLD<br/>            | `FontBold`<br/>            |
| FNT\_INFO\_FONTHEIGHT<br/>          | `FontHeight`<br/>          |
| FNT\_INFO\_FONTITALIC<br/>          | `FontItalic`<br/>          |
| FNT\_INFO\_FONTMAXWIDTH<br/>        | `FontMaxWidth`<br/>        |
| FNT\_INFO\_FONTSTRIKETHRU<br/>      | `FontStrikeThru`<br/>      |
| FNT\_INFO\_FONTUNDERLINE<br/>       | `FontUnderline`<br/>       |
| FNT\_INFO\_FONTWIDTH<br/>           | `FontWidth`<br/>           |
| FNT\_INFO\_GRAYPERCENTAGE<br/>      | `GrayPercentage`<br/>      |
| FNT\_INFO\_NEXTFONTID<br/>          | `NextFontID`<br/>          |
| FNT\_INFO\_NEXTGLYPH<br/>           | `NextGlyph`<br/>           |
| FNT\_INFO\_PRINTDIRINCCDEGREES<br/> | `PrintDirInCCDegrees`<br/> |
| FNT\_INFO\_TEXTXRES<br/>            | `TextXRes`<br/>            |
| FNT\_INFO\_TEXTYRES<br/>            | `TextYRes`<br/>            |



 

Supplied by the [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) caller.

</dd> <dt>

**lStdVariable**
</dt> <dd>

Specifies the current value of the specified standard variable. Supplied by Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

</dd> </dl> </dd> </dl>

## Remarks

To obtain the current value for one or more of Unidrv's standard variables, a rendering plug-in can supply the address of a GETINFO\_STDVAR structure when calling Unidrv's [*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md) callback function.

For more information about [standard variables](https://www.bing.com/search?q=standard variables), see [Microsoft Universal Printer Driver](https://www.bing.com/search?q=Microsoft Universal Printer Driver).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[*UNIFONTOBJ\_GetInfo*](unifontobj-getinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GETINFO_STDVAR%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





