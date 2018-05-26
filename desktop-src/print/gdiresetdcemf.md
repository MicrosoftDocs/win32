---
Description: The GdiResetDCEMF function resets a printers device context during playback of a spooled EMF print job.
ms.assetid: ea97cc22-6057-427d-90c1-4f23ced932aa
title: GdiResetDCEMF function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GdiResetDCEMF function

The **GdiResetDCEMF** function resets a printer's device context during playback of a spooled EMF print job.

## Syntax


```C++
BOOL GdiResetDCEMF(
   HANDLE    SpoolFileHandle,
   PDEVMODEW pCurrDM
);
```



## Parameters

<dl> <dt>

*SpoolFileHandle* 
</dt> <dd>

Caller-supplied spool file handle, obtained by a previous call to [**GdiGetSpoolFileHandle**](gdigetspoolfilehandle.md).

</dd> <dt>

*pCurrDM* 
</dt> <dd>

Caller-supplied pointer to a [**DEVMODEW**](display.devmodew) structure, obtained by a previous call to [**GdiGetDevmodeForPage**](gdigetdevmodeforpage.md).

</dd> </dl>

## Return value

If the operation succeeds, the function returns **TRUE**. Otherwise the function returns **FALSE**.

## Remarks

The **GdiResetDCEMF** function is exported by gdi32.dll for use within a print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function.

Print processors must call **GdiResetDCEMF** whenever it is necessary to reset the printer's device context. The function must be called whenever the [**GdiGetDevmodeForPage**](gdigetdevmodeforpage.md) function indicates that the current document page's [**DEVMODEW**](display.devmodew) structure is not identical to that of the previous document page.

For additional information, see [Using GDI Functions in Print Processors](print.using_gdi_functions_in_print_processors).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Winppi.h (include Winppi.h)</dt> </dl>                                  |
| Library<br/>         | <dl> <dt>Gdi32.Lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Gdi32.dll</dt> </dl>                                                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GdiResetDCEMF%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




