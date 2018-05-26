---
Description: GDI Functions for Print Processors
ms.assetid: aecf6d40-780c-4fba-9f1e-a8c848d2e6a4
title: GDI Functions for Print Processors
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GDI Functions for Print Processors

## 

This section describes the functions that a print processor can call when it processes EMF-formatted spool files.

> [!Note]  
> In versions of the Microsoft Windows operating system before Windows Vista, you should not read EMF data directly from a spool file. This type of access is not supported.

 

Function prototypes can be found in winppi.h, a header file that is included in the Windows Driver Kit (WDK).

The functions described in this section are:

<dl>

[**GdiDeleteSpoolFileHandle**](gdideletespoolfilehandle.md)  
[**GdiEndDocEMF**](gdienddocemf.md)  
[**GdiEndPageEMF**](gdiendpageemf.md)  
[**GdiGetDC**](gdigetdc.md)  
[**GdiGetDevmodeForPage**](gdigetdevmodeforpage.md)  
[**GdiGetPageCount**](gdigetpagecount.md)  
[**GdiGetPageHandle**](gdigetpagehandle.md)  
[**GdiGetSpoolFileHandle**](gdigetspoolfilehandle.md)  
[**GdiPlayPageEMF**](gdiplaypageemf.md)  
[**GdiResetDCEMF**](gdiresetdcemf.md)  
[**GdiStartDocEMF**](gdistartdocemf.md)  
[**GdiStartPageEMF**](gdistartpageemf.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDI%20Functions%20for%20Print%20Processors%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



