---
description: OpenXPS is the Open XML Paper Specification format for documents, and it’s based on the European Carton Makers Association (ECMA) standard specification.
ms.assetid: 52FB5B3F-BEBF-4851-8BE9-5DC7AE535313
title: App Support for OpenXPS Printing
ms.topic: article
ms.date: 05/31/2018
---

# App Support for OpenXPS Printing

OpenXPS is the Open XML Paper Specification format for documents, and it’s based on the European Computer Manufacturers Association (ECMA) standard specification.

Windows 8 provides full support for OpenXPS printing via the v4 print driver model, side-by-side with continued support for the Microsoft XPS format. And this topic focuses on the portion of this support that is relevant to Windows application developers. For information about driver requirements for OpenXPS support, see [Driver Support for OpenXPS](/windows-hardware/drivers/print/printer-driver-overview).

## Sending XPS data to the Print System

We recommend that you use [**IPrintDocumentPackageTarget**](/windows/win32/api/documenttarget/nn-documenttarget-iprintdocumentpackagetarget) for sending all XPS print jobs to the print system. **IPrintDocumentPackageTarget** accepts the XPS object model (OM) without serialization, and that helps to improve the overall performance.

Here's a brief summary of the **IPrintDocumentPackageTarget** interface:

-   This interface supports printing from tailored solutions as well as desktop applications.

-   For desktops apps, this can be used in place of [**StartXpsPrintJob1**](/windows/win32/api/xpsprint/nf-xpsprint-startxpsprintjob1).

-   Available on Windows 7 with Service Pack 1 (SP1) + Platform Update, and Windows 8.

-   Include *DocumentTarget.h* in projects to use these APIs.

Applications that consume OpenXPS documents should note that the MIME type for OpenXPS is as follows:

<dl> application\\oxps  
</dl>

## Sending OpenXPS data to the XPS Print API

Specific to OpenXPS, XPS OM accepts both MSXPS and OpenXPS, and provides methods for conversion and serialization to either format. This allows application developers to be agnostic of the target driver, if they want. This also means that app developers can always submit print jobs as XPS OM to either StartXpsPrintJob1 or IDocumentPackageTarget, knowing that the print system will handle any necessary conversion.

Of course, preventing conversion between XPS formats will improve end-to-end performance. From the application, the developer can check the following registry key to determine the preferred XPS format of the targeted print driver:

``` syntax
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Print\Printers\[PrintDriverName]\PrintDriverData\XpsFormat
```

Once the preferred XPS format has been determined, the application can provide XPS OM objects that will not require conversion. Of particular note is the use of HD Photo in MSXPS and JPEGXR in OpenXPS. Converting from JPEGXR to HD Photo is relatively lightweight since the primary difference in this conversion is that HD Photo ignores 4 control bits that JPEGXR requires. However, converting from HD Photo to JPEGXR requires the entire image to be re-encoded in order to generate the required control bits. Thus, providing JPEGXR images for high-resolution images will ensure compatibility with OpenXPS and minimize the conversion cost of the image for MSXPS.

The *Xpsobjectmodel\_1.h* header defines the additional APIs and objects for OpenXPS. And the IXpsOMObjectFactory1 interface provides additional methods for image conversion. Here's the syntax:


```C++
IXpsOMObjectFactory1->ConvertHDPhotoToJpegXR(IXpsOMImageResource *imageResource);

IXpsOMObjectFactory1->ConvertJpegXRToHDPhoto(IXpsOMImageResource *imageResource);
```



Windows 8 provides the following new and updated enumerations.

New enumeration:

<dl>

[**XPS\_DOCUMENT\_TYPE**](/windows/win32/api/xpsobjectmodel_1/ne-xpsobjectmodel_1-xps_document_type)  
</dl>

Updated enumeration

<dl>

[**XPS\_IMAGE\_TYPE**](/windows/win32/api/xpsobjectmodel/ne-xpsobjectmodel-xps_image_type)  
</dl>

The new GetDocumentType methods allow an application to determine the XPS format of documents. These are available in [**IXpsOMObjectFactory1**](/windows/desktop/api/XpsObjectModel_1/nn-xpsobjectmodel_1-ixpsomobjectfactory1), [**IXpsOMPackage1**](/windows/desktop/api/XpsObjectModel_1/nn-xpsobjectmodel_1-ixpsompackage1), and [**IXpsOMPage1**](/windows/desktop/api/XpsObjectModel_1/nn-xpsobjectmodel_1-ixpsompage1). Here's a list of the methods.

<dl>

[**IXpsOMObjectFactory1::GetDocumentTypeFromFile**](/windows/desktop/api/XpsObjectModel_1/nf-xpsobjectmodel_1-ixpsomobjectfactory1-getdocumenttypefromfile)  
[**IXpsOMObjectFactory1::GetDocumentTypeFromStream**](/windows/desktop/api/XpsObjectModel_1/nf-xpsobjectmodel_1-ixpsomobjectfactory1-getdocumenttypefromstream)  
[**IXpsOMPackage1::GetDocumentType**](/windows/desktop/api/XpsObjectModel_1/nf-xpsobjectmodel_1-ixpsompackage1-getdocumenttype)  
[**IXpsOMPage1::GetDocumentType**](/windows/desktop/api/XpsObjectModel_1/nf-xpsobjectmodel_1-ixpsompage1-getdocumenttype)  
</dl>

Windows 8 provides the following new error codes in support of OpenXPS:

<dl> XPS\_E\_MISMATCHED\_NAMESPACE. <dl> This error is returned, if there is a mismatched namespace.  
</dl> </dd> XPS\_E\_ABSOLUTE\_REFERENCE. <dl> This error is returned if MSXPS uses absolute URIs in internal references, or attempts to use internal references to serialize in the stream. That is because XPS OM generates relative URIs. And although MSXPS supports both relative and absolute URIs, OpenXPS requires relative URIs.  
</dl> </dd> </dl>

## Related topics

<dl> <dt>

[Driver Support for OpenXPS](/windows-hardware/drivers/print/printer-driver-overview)
</dt> <dt>

[**IPrintDocumentPackageTarget**](/windows/win32/api/documenttarget/nn-documenttarget-iprintdocumentpackagetarget)
</dt> <dt>

[**IXpsOMObjectFactory1::GetDocumentTypeFromFile**](/windows/desktop/api/XpsObjectModel_1/nf-xpsobjectmodel_1-ixpsomobjectfactory1-getdocumenttypefromfile)
</dt> <dt>

[**IXpsOMObjectFactory1::GetDocumentTypeFromStream**](/windows/desktop/api/XpsObjectModel_1/nf-xpsobjectmodel_1-ixpsomobjectfactory1-getdocumenttypefromstream)
</dt> <dt>

[**IXpsOMPackage1::GetDocumentType**](/windows/desktop/api/XpsObjectModel_1/nf-xpsobjectmodel_1-ixpsompackage1-getdocumenttype)
</dt> <dt>

[**IXpsOMPage1::GetDocumentType**](/windows/desktop/api/XpsObjectModel_1/nf-xpsobjectmodel_1-ixpsompage1-getdocumenttype)
</dt> <dt>

[**XPS\_DOCUMENT\_TYPE**](/windows/win32/api/xpsobjectmodel_1/ne-xpsobjectmodel_1-xps_document_type)
</dt> <dt>

[**XPS\_IMAGE\_TYPE**](/windows/win32/api/xpsobjectmodel/ne-xpsobjectmodel-xps_image_type)
</dt> </dl>

 

 
