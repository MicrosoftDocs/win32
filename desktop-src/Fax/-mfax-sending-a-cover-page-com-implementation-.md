---
Description: This topic describes how to send common and personal cover pages in the Component Object Model (COM) implementation environment.
ms.assetid: 2946976d-96b8-4ac3-85a5-30f49292314c
title: Sending a Cover Page (COM Implementation)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sending a Cover Page (COM Implementation)

You can send a common cover page or a personal cover page with a fax transmission by setting the following properties of the [FaxDoc](-mfax-faxdoc.md) object.

## To send a common cover page

-   Set the [**SendCoverpage**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxdoc-get_sendcoverpage) property equal to **TRUE**.
-   Set the [**ServerCoverpage**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxdoc-get_servercoverpage) property equal to **TRUE**.
-   Set the [**CoverpageName**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxdoc-get_coverpagename) property to a valid common cover page file.

## To send a personal cover page

-   Set the [**SendCoverpage**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxdoc-get_sendcoverpage) property equal to **TRUE**.
-   Set the [**ServerCoverpage**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxdoc-get_servercoverpage) property equal to **FALSE**.
-   Set the [**CoverpageName**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxdoc-get_coverpagename) property to a valid personal cover page file.

For more information, see [**IFaxDoc::SendCoverpage Property**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxdoc-get_sendcoverpage), [**IFaxDoc::ServerCoverpage Property**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxdoc-get_servercoverpage), and [**IFaxDoc::CoverpageName Property**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxdoc-get_coverpagename). If you are writing a Microsoft Visual Basic application, see [**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md) for more information about setting these properties.

To determine if the fax server is configured to permit personal cover pages, you can call the [**IFaxServer::get\_ServerCoverpage**](/previous-versions/windows/desktop/api/faxcomex/) method.

To transmit a cover page with a fax, call the [**IFaxDoc::Send**](/previous-versions/windows/desktop/api/Faxcom/) method (the **Send** method of the [**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md) object).

 

 



