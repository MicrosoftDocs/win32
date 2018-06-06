---
Description: The IPrintOemUni::HalftonePattern method can be used with Unidrv-supported printers to create or modify a halftone pattern before it is used in a halftoning operation.
ms.assetid: 1b899492-f4a7-4c13-9e19-0f086b2b6b47
title: IPrintOemUni::HalftonePattern method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::HalftonePattern method

The `IPrintOemUni::HalftonePattern` method can be used with Unidrv-supported printers to create or modify a halftone pattern before it is used in a halftoning operation.

## Syntax


```C++
HRESULT HalftonePattern(
   PDEVOBJ pdevobj,
   PBYTE   pHTPattern,
   DWORD   dwHTPatternX,
   DWORD   dwHTPatternY,
   DWORD   dwHTNumPatterns,
   DWORD   dwCallbackID,
   PBYTE   pResource,
   DWORD   dwResourceSize
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*pHTPattern* 
</dt> <dd>

Caller-supplied pointer to a buffer that receives the method-supplied halftone pattern. Buffer size, in bytes, is:

(((*dwHTPatternX* \* *dwHTPatternY*) + 3)/4) \* 4 \* *dwHTNumPatterns*.

</dd> <dt>

*dwHTPatternX* 
</dt> <dd>

Caller-supplied length, in pixels, of the halftone pattern, as specified by the first value in the [*GPD*](wdkgloss.g#wdkgloss-generic-printer-description--gpd-) file's \***HTPatternSize** attribute.

</dd> <dt>

*dwHTPatternY* 
</dt> <dd>

Caller-supplied height, in pixels, of the halftone pattern, as specified by the second value in the GPD file's \***HTPatternSize** attribute.

</dd> <dt>

*dwHTNumPatterns* 
</dt> <dd>

Caller-supplied number of patterns, as specified by the GPD file's \***HTNumPatterns** attribute. The number of patterns can be either 1 or 3.

</dd> <dt>

*dwCallbackID* 
</dt> <dd>

Caller-supplied value identifying the halftone method, as specified by the GPD file's \***HTCallbackID** attribute.

</dd> <dt>

*pResource* 
</dt> <dd>

Caller-supplied pointer to a buffer containing a halftone pattern, as specified by the GPD file's \***rcHTPatternID** attribute. This can be **NULL**.

</dd> <dt>

*dwResourceSize* 
</dt> <dd>

Caller-supplied size of the halftone pattern contained in the buffer pointed to by *pResource*. This is zero if *pResource* is **NULL**.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::HalftonePattern` method is used to create or modify a halftone pattern before Unidrv passes it to GDI. Its purpose is to allow proprietary halftone patterns to be either stored as encrypted resources or generated at run time.

If the `IPrintOemUni::HalftonePattern` method is implemented, and if the GPD file entry for the currently selected halftoning method includes an \***HTCallbackID** attribute, Unidrv calls the `IPrintOemUni::HalftonePattern` method before passing a halftone pattern to GDI.

If the GPD file entry for the currently selected halftoning method contains an \*rcHTPatternID entry identifying an RC\_HTPATTERN resource, Unidrv obtains the pattern and passes a pointer to it as the *pResource* parameter value. This allows you to store the pattern as an encrypted resource, and to use the `IPrintOemUni::HalftonePattern` method to decode the pattern. The decoded pattern should be returned in the buffer pointed to by *pHTPattern*.

You can also use the `IPrintOemUni::HalftonePattern` method to generate a halftone pattern. In this case an RC\_HTPATTERN resource is not needed, so *pResource* is **NULL**. The `IPrintOemUni::HalftonePattern` method should generate a pattern and return it in the buffer pointed to by *pHTPattern*.

If the `IPrintOemUni::HalftonePattern` method returns one pattern, it is used for all colors. If the method returns three patterns, they must be specified in RGB order.

The following example shows an implementation of a rendering plug-in's `HalftonePattern` method. The method calculates the length in bytes of the HTPattern\_DDK pattern array, and then copies the bytes in the pattern array to the buffer pointed to by this method's *pHTPattern* parameter. The pattern array can contain either one or three patterns, depending on whether the pattern is used for all colors or has separate red, green, and blue patterns. For the sake of brevity, not all elements of the pattern array are listed.


```
static BYTE HTPattern_DDK[256] = {
    129,  44,  59, 124, 143, 232, 166, ...
    ...
    ...
    98, 202, 130, 148, 213,  101,  163, 72
};

HRESULT __stdcall IOemUni::HalftonePattern(
    PDEVOBJ     pdevobj,
    PBYTE       pHTPattern,
    DWORD       dwHTPatternX,
    DWORD       dwHTPatternY,
    DWORD       dwHTNumPatterns,
    DWORD       dwCallbackID,
    PBYTE       pResource,
    DWORD       dwResourceSize)
{
PBYTE  pSrcPattern;
DWORD  dwLen = sizeof(HTPattern_DDK);

if (dwLen != (((dwHTPatternX * dwHTPatternY) + 3) / 4) * 4 * dwHTNumPatterns)
 return E_FAIL;

pSrcPattern = HTPattern_DDK;
while (dwLen-- > 0)
 *pHTPattern++ = *pSrcPattern++;

return S_OK;
}
```



An implementation of a `HalftonePattern` method in the rendering plug-in must be accompanied by a Halftone feature in the GPD file. The following GPD example shows a Halftone feature whose HT\_PAT\_DDK\_16x16 option describes the customized pattern generated in the previous sample.

\*Feature: Halftone

{

\*rcNameID: =HALFTONING\_DISPLAY

\*HelpIndex: 12005

\*DefaultOption: HT\_PATSIZE\_AUTO

\*Option: HT\_PATSIZE\_AUTO

{

\*rcNameID: =HT\_AUTO\_SELECT\_DISPLAY

}

\*Option: HT\_PATSIZE\_SUPERCELL\_M

{

\*rcNameID: =HT\_SUPERCELL\_DISPLAY

}

\*Option: HT\_PATSIZE\_6x6\_M

{

\*rcNameID: =HT\_DITHER6X6\_DISPLAY

}

\*Option: HT\_PATSIZE\_8x8\_M

{

\*rcNameID: =HT\_DITHER8X8\_DISPLAY

}

\*Option: HT\_PAT\_DDK\_16x16

{

\*Name: "DDK 16x16"

\*HTPatternSize: PAIR(16, 16)

\*HTNumPatterns: 1

\*HTCallbackID: 1

}

}

The `IPrintOemUni::HalftonePattern` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "HalftonePattern" as input.

For more information about halftoning, see [Customized Halftoning](https://www.bing.com/search?q=Customized+Halftoning) and [Option Attributes for the Halftone Feature](https://www.bing.com/search?q=Option+Attributes+for+the+Halftone+Feature).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni**](iprintoemuni-interface.md)
</dt> <dt>

[**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::HalftonePattern%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





