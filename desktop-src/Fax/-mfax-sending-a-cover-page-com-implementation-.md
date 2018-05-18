---
Description: 'This topic describes how to send common and personal cover pages in the Component Object Model (COM) implementation environment.'
ms.assetid: '2946976d-96b8-4ac3-85a5-30f49292314c'
title: 'Sending a Cover Page (COM Implementation)'
---

# Sending a Cover Page (COM Implementation)

You can send a common cover page or a personal cover page with a fax transmission by setting the following properties of the [FaxDoc](-mfax-faxdoc.md) object.

## To send a common cover page

-   Set the [**SendCoverpage**](-mfax-ifaxdoc-mfax-ifaxdoc-get-sendcoverpage-cpp.md) property equal to **TRUE**.
-   Set the [**ServerCoverpage**](-mfax-ifaxdoc-mfax-ifaxdoc-get-servercoverpage-cpp.md) property equal to **TRUE**.
-   Set the [**CoverpageName**](-mfax-ifaxdoc-mfax-ifaxdoc-get-coverpagename-cpp.md) property to a valid common cover page file.

## To send a personal cover page

-   Set the [**SendCoverpage**](-mfax-ifaxdoc-mfax-ifaxdoc-get-sendcoverpage-cpp.md) property equal to **TRUE**.
-   Set the [**ServerCoverpage**](-mfax-ifaxdoc-mfax-ifaxdoc-get-servercoverpage-cpp.md) property equal to **FALSE**.
-   Set the [**CoverpageName**](-mfax-ifaxdoc-mfax-ifaxdoc-get-coverpagename-cpp.md) property to a valid personal cover page file.

For more information, see [**IFaxDoc::SendCoverpage Property**](-mfax-ifaxdoc-mfax-ifaxdoc-get-sendcoverpage-cpp.md), [**IFaxDoc::ServerCoverpage Property**](-mfax-ifaxdoc-mfax-ifaxdoc-get-servercoverpage-cpp.md), and [**IFaxDoc::CoverpageName Property**](-mfax-ifaxdoc-mfax-ifaxdoc-get-coverpagename-cpp.md). If you are writing a Microsoft Visual Basic application, see [**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md) for more information about setting these properties.

To determine if the fax server is configured to permit personal cover pages, you can call the [**IFaxServer::get\_ServerCoverpage**](-mfax-ifaxserver-client-mfax-ifaxserver-get-servercoverpage-cpp.md) method.

To transmit a cover page with a fax, call the [**IFaxDoc::Send**](-mfax-ifaxdoc-mfax-ifaxdoc-send-cpp.md) method (the **Send** method of the [**FaxDoc**](-mfax-faxdoc-object-visual-basic-.md) object).

 

 



