---
Description: This topic describes how to send common and personal cover pages in the Component Object Model (COM) implementation environment.
ms.assetid: 2946976d-96b8-4ac3-85a5-30f49292314c
title: Sending a Cover Page (COM Implementation)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sending a Cover Page (COM Implementation)

You can send a common cover page or a personal cover page with a fax transmission by setting the following properties of the [FaxDoc](-mfax-faxdoc.md) object.

## To send a common cover page

-   Set the [**SendCoverpage**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxdoc-get_sendcoverpage?branch=master) property equal to **TRUE**.
-   Set the [**ServerCoverpage**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxdoc-get_servercoverpage?branch=master) property equal to **TRUE**.
-   Set the [**CoverpageName**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxdoc-get_coverpagename?branch=master) property to a valid common cover page file.

## To send a personal cover page

-   Set the [**SendCoverpage**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxdoc-get_sendcoverpage?branch=master) property equal to **TRUE**.
-   Set the [**ServerCoverpage**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxdoc-get_servercoverpage?branch=master) property equal to **FALSE**.
-   Set the [**CoverpageName**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxdoc-get_coverpagename?branch=master) property to a valid personal cover page file.

For more information, see [**IFaxDoc::SendCoverpage Property**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxdoc-get_sendcoverpage?branch=master), [**IFaxDoc::ServerCoverpage Property**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxdoc-get_servercoverpage?branch=master), and [**IFaxDoc::CoverpageName Property**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxdoc-get_coverpagename?branch=master). If you are writing a Microsoft Visual Basic application, see [**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md) for more information about setting these properties.

To determine if the fax server is configured to permit personal cover pages, you can call the [**IFaxServer::get\_ServerCoverpage**](/windows/previous-versions/faxcomex/?branch=master) method.

To transmit a cover page with a fax, call the [**IFaxDoc::Send**](/windows/previous-versions/Faxcom/?branch=master) method (the **Send** method of the [**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md) object).

 

 



