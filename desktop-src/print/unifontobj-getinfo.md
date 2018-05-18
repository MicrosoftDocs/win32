---
Description: 'The UNIFONTOBJ\_GetInfo callback function is provided by the Unidrv driver so that rendering plug-ins can obtain font or glyph information.'
ms.assetid: '2c0d350d-dcdf-4da7-8cca-7f36d4ca622e'
title: 'UNIFONTOBJ\_GetInfo routine'
---

# UNIFONTOBJ\_GetInfo routine

The **UNIFONTOBJ\_GetInfo** callback function is provided by the Unidrv driver so that rendering plug-ins can obtain font or glyph information.

## Syntax


```C++
PFNGETINFO UNIFONTOBJ_GetInfo;

BOOL APIENTRY UNIFONTOBJ_GetInfo(
   struct _UNIFONTOBJ *pUFObj,
   DWORD              dwInfoID,
   PVOID              pData,
   DWORD              dwDataSize,
   PDWORD             pcbNeeded
)
{ ... }
```



## Parameters

<dl> <dt>

*pUFObj* 
</dt> <dd>

Pointer to the [**UNIFONTOBJ**](unifontobj.md) structure received by the function that is making the callback to **UNIFONTOBJ\_GetInfo**. Supplied by the caller.

</dd> <dt>

*dwInfoID* 
</dt> <dd>

Specifies the type of structure pointed to by *pData*. Supplied by the caller. See the following table.

</dd> <dt>

*pData* 
</dt> <dd>

Pointer to a structure, as indicated in the following table. Supplied by the caller.



| dwInfoID Value                       | *pData* Structure                                              |
|--------------------------------------|----------------------------------------------------------------|
| UFO\_GETINFO\_FONTOBJ<br/>     | [**GETINFO\_FONTOBJ**](getinfo-fontobj.md)<br/>         |
| UFO\_GETINFO\_GLYPHBITMAP<br/> | [**GETINFO\_GLYPHBITMAP**](getinfo-glyphbitmap.md)<br/> |
| UFO\_GETINFO\_GLYPHSTRING<br/> | [**GETINFO\_GLYPHSTRING**](getinfo-glyphstring.md)<br/> |
| UFO\_GETINFO\_GLYPHWIDTH<br/>  | [**GETINFO\_GLYPHWIDTH**](getinfo-glyphwidth.md)<br/>   |
| UFO\_GETINFO\_MEMORY<br/>      | [**GETINFO\_MEMORY**](getinfo-memory.md)<br/>           |
| UFO\_GETINFO\_STDVARIABLE<br/> | [**GETINFO\_STDVAR**](getinfo-stdvar.md)<br/>           |



 

<dl> <dd>

For a summary of structure contents, see the following **Remarks** section.

</dd> </dl> </dd> <dt>

*dwDataSize* 
</dt> <dd>

Specifies the size, in bytes, of the buffer pointed to by *pData*. Supplied by the caller.

</dd> <dt>

*pcbNeeded* 
</dt> <dd>

Pointer to a location that receives the minimum buffer size, in bytes, required to contain the structure identified by *dwInfoID*. Supplied by the caller.

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise it returns **FALSE**.

## Remarks

The **UNIFONTOBJ\_GetInfo** callback function allows a [rendering plug-in](print.rendering_plug_ins) to call back into Unidrv to obtain font or glyph information from GDI, needed for handling [customized font management](print.customized_font_management) operations.

A rendering plug-in receives the **UNIFONTOBJ\_GetInfo** function's address in the [**UNIFONTOBJ**](unifontobj.md) structure that is passed to the font customization methods.

The type of information returned by the function is dependent on the input arguments. The caller supplies values for *dwInfoID*, *pData*, and *dwDataSize* to indicate the type of information wanted. The following table summarizes the types of information returned. For more information, see the structure descriptions.



| *pData* Structure                                              | Returned Information                                                                                     |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**GETINFO\_FONTOBJ**](getinfo-fontobj.md)<br/>         | A FONTOBJ structure describing the current font.<br/>                                              |
| [**GETINFO\_GLYPHBITMAP**](getinfo-glyphbitmap.md)<br/> | A single glyph bitmap.<br/>                                                                        |
| [**GETINFO\_GLYPHSTRING**](getinfo-glyphstring.md)<br/> | An array of glyph specifiers in a specified format.<br/>                                           |
| [**GETINFO\_GLYPHWIDTH**](getinfo-glyphwidth.md)<br/>   | Total width of a set of glyphs.<br/>                                                               |
| [**GETINFO\_MEMORY**](getinfo-memory.md)<br/>           | Amount of available printer memory remaining.<br/>                                                 |
| [**GETINFO\_STDVAR**](getinfo-stdvar.md)<br/>           | The current value for one or more of Unidrv's [standard variables](print.standard_variables).<br/> |



 

If the buffer described by *pData* and *dwDataSize* is too small to receive the structure indicated by *dwInfoID*, the function loads the required buffer size into the location pointed by *pcbNeeded* and returns **FALSE**.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UNIFONTOBJ_GetInfo%20routine%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




