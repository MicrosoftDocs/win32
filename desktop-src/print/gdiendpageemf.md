---
Description: 'The GdiEndPageEMF function ends EMF playback operations for a physical page of an EMF-formatted print job.'
ms.assetid: 'e15344a5-32ed-43a8-93c2-d5201617d595'
title: GdiEndPageEMF function
---

# GdiEndPageEMF function

The **GdiEndPageEMF** function ends EMF playback operations for a physical page of an EMF-formatted print job.

## Syntax


```C++
BOOL GdiEndPageEMF(
   HANDLE SpoolFileHandle,
   DWORD  dwOptimization
);
```



## Parameters

<dl> <dt>

*SpoolFileHandle* 
</dt> <dd>

Caller-supplied spool file handle, obtained by a previous call to [**GdiGetSpoolFileHandle**](gdigetspoolfilehandle.md).

</dd> <dt>

*dwOptimization* 
</dt> <dd>

Caller-supplied flags. The following flag is defined:

<dl> <dt>

<span id="EMF_PP_COLOR_OPTIMIZATION"></span><span id="emf_pp_color_optimization"></span>EMF\_PP\_COLOR\_OPTIMIZATION
</dt> <dd>

Enable color optimization. For more information, see Remarks.

</dd> </dl> </dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise the function returns **FALSE**, and an error code can be obtained by calling **GetLastError**.

## Remarks

The **GdiEndPageEMF** function is exported by gdi32.dll for use within a print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.

The **GdiEndPageEMF** function ends the processing of a physical page and causes it to be ejected from the printer. A print processor should call **GdiEndPageEMF** at the following times:

-   After the appropriate number of document pages have been placed on the physical page by making calls to [**GdiPlayPageEMF**](gdiplaypageemf.md). Note that **GdiPlayPageEMF** does not actually print on the device context, but instead prepares a data structure that describes the text and graphics that are to be printed on the physical page(s). The text and graphics are printed to the device context when **GdiEndPageEMF** is called.

-   Whenever a call to [**GdiGetDevmodeForPage**](gdigetdevmodeforpage.md) indicates a document page's [**DEVMODEW**](display.devmodew) structure is different from the previous page's DEVMODE structure.

If this function is called with the *dwOptimization* parameter set to EMF\_PP\_COLOR\_OPTIMIZATION, color optimization is enabled. If *dwOptimization* is set to 0, no optimization is performed. When color optimization is enabled, the presence of color in the spool file causes the spool file to be played in color; the lack of color in the spool file causes the spool file to be played in monochrome.

If you are creating a Unidrv rendering plug-in to generate color watermarks, be advised that color optimization causes color watermarks to be printed in black and white when they are printed on black-and-white documents. To ensure that color watermarks print correctly with color and black-and-white documents, disable color optimization.

The color optimization controlled by the *dwOptimization* parameter can also be controlled by setting the **dwColorOptimization** member of the [**ATTRIBUTE\_INFO\_2**](attribute-info-2.md) or [**ATTRIBUTE\_INFO\_3**](attribute-info-3.md) structures. This optimization also can be controlled by the Unidrv \***ChangeColorModeOnDoc?** color attribute (see [Color Attributes](print.color_attributes)).

For additional information, see [Using GDI Functions in Print Processors](print.using_gdi_functions_in_print_processors).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Winppi.h (include Winppi.h)</dt> </dl>                                  |
| Library<br/>         | <dl> <dt>Gdi32.Lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Gdi32.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**GdiStartPageEMF**](gdistartpageemf.md)
</dt> <dt>

[**GdiPlayPageEMF**](gdiplaypageemf.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GdiEndPageEMF%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





