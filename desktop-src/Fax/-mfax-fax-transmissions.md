---
Description: This topic describes the elements of an outbound fax transmission.
ms.assetid: 90d7680d-948f-4d90-ad00-b0cf4886f5ec
title: Fax Transmissions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Transmissions

An outbound fax transmission includes the following elements:

-   **A document file.** The fax service converts the data to the Tagged Image File Format Class F (TIFF Class F) for facsimile. For more information, see [Fax Image Format](-mfax-fax-image-format.md).

-   **Transmission information.** Information includes the fax number, sender and recipient data, an optional billing code, and job scheduling information. In the Microsoft Win32 environment, if the application is printing to a device context, a [**FAX\_PRINT\_INFO**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_print_infoa) structure contains this information. In other instances, a [**FAX\_JOB\_PARAM**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_job_parama) structure contains this information.

    If you are using the Microsoft Component Object Model (COM) implementation, you can set multiple properties of the [**IFaxJob**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjob) object to specify transmission information. For more information, see [Transmitting Faxes](-mfax-transmitting-faxes.md).

-   **An optional cover page file.** In the Win32 environment, the [**FAX\_COVERPAGE\_INFO**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_coverpage_infoa) structure contains this data. The structure supplies the name of a cover page template file (.cov) and user-defined information for the template.

    If you are using the Microsoft COM implementation, you can set multiple properties of the [FaxDoc](-mfax-faxdoc.md) object to specify cover page information. For more information, see [Cover Pages](-mfax-cover-pages.md) and [Sending a Cover Page](-mfax-sending-a-cover-page.md).

## Related topics

<dl> <dt>

[Transmitting Faxes](-mfax-transmitting-faxes.md)
</dt> </dl>

 

 



