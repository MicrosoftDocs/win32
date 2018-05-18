---
Description: 'The TRANSDATA structure is one of the structures used to define the contents of glyph translation table files (.gtt files).'
ms.assetid: '75ddf007-0113-4967-a8d4-02fcc3cc2857'
title: TRANSDATA structure
---

# TRANSDATA structure

The TRANSDATA structure is one of the structures used to define the contents of [glyph translation table files](print.customized_font_management#ddk-glyph-translation-table-files-gg) (.gtt files).

## Syntax


```C++
typedef struct _TRANSDATA {
  BYTE  ubCodePageID;
  BYTE  ubType;
  union {
    SHORT sCode;
    BYTE  ubCode;
    BYTE  ubPairs[2];
  } uCode;
} TRANSDATA, *PTRANSDATA;
```



## Members

<dl> <dt>

**ubCodePageID**
</dt> <dd>

Specifies the zero-based index of a particular structure in the array of [**UNI\_CODEPAGEINFO**](uni-codepageinfo.md) structures. The first structure in this array has an index of 0, the second structure has an index of 1, and so on.

The **loCodePageOffset** member of the [**UNI\_GLYPHSETDATA**](uni-glyphsetdata.md) structure contains the offset from the beginning of the UNI\_GLYPHSETDATA structure to the beginning of the array of UNI\_CODEPAGEINFO structures.

</dd> <dt>

**ubType**
</dt> <dd>

Is a set of one or more bit flags, as follows:



Flag

Definition

**Format Flags**<br/>

One of the following three flags can be set.<br/>

MTYPE\_COMPOSE<br/>

The **sCode** member of the **uCode** union contains an offset to a string. The string contains a command to be sent to the printer.<br/>

MTYPE\_DIRECT<br/>

The **ubCode** member of the **uCode** union contains a one-byte character code to be sent to the printer.<br/>

MTYPE\_PAIRED<br/>

The **ubPairs** member of the **uCode** union contains a two-byte character code to be sent to the printer.<br/>

**Action Flags**<br/>

One of the following flags can be set. All are optional. Not valid if the **lPredefinedID** member of the [**UNI\_GLYPHSETDATA**](uni-glyphsetdata.md) structure is set to CC\_NOPRECNV.<br/>

MTYPE\_ADD<br/>

The specified mapping is added to the map table contained in the .gtt file specified by the **lPredefinedID** member of the UNI\_GLYPHSETDATA structure.<br/>

MTYPE\_DISABLE<br/>

The specified mapping, contained in the .gtt file specified by the **lPredefinedID** member of the [**UNI\_GLYPHSETDATA**](uni-glyphsetdata.md) structure, is disabled.<br/>

MTYPE\_REPLACE<br/>

The specified mapping replaces mapping in the map table contained in the .gtt file specified by the **lPredefinedID** member of the UNI\_GLYPHSETDATA structure.<br/>

**East Asian Flags**<br/>

One of the following flags can be set.<br/>

MTYPE\_SINGLE<br/>

Character data is single-byte.<br/>

MTYPE\_DOUBLE<br/>

Character data is double-byte.<br/>



 

</dd> <dt>

**uCode**
</dt> <dd> <dl> <dt>

**sCode**
</dt> <dd>

Specifies the offset to a command string. The offset is relative to the beginning of the [**MAPTABLE**](maptable.md) structure containing the TRANSDATA array. The first word of the command string must be the command size. Valid if the MTYPE\_COMPOSE flag is set in **uType**.

</dd> <dt>

**ubCode**
</dt> <dd>

Specifies a one-byte character code. Valid if the MTYPE\_DIRECT flag is set in **uType**.

</dd> <dt>

**ubPairs**
</dt> <dd>

Specifies a two-byte character code. Valid if the MTYPE\_PAIRED flag is set in **uType**.

</dd> </dl> </dd> </dl>

## Remarks

A .gtt file's TRANSDATA structure array, which contains glyph mapping information, is contained in the file's [**MAPTABLE**](maptable.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**UNI\_CODEPAGEINFO**](uni-codepageinfo.md)
</dt> <dt>

[**UNI\_GLYPHSETDATA**](uni-glyphsetdata.md)
</dt> <dt>

[**MAPTABLE**](maptable.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20TRANSDATA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





