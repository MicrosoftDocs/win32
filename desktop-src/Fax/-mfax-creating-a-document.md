---
Description: The following steps describe a typical scenario for creating a document.
ms.assetid: 53f88ab5-26a3-4e84-8254-3838d27aa5ff
title: Creating a Document
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a Document

The following steps describe a typical scenario for creating a document.

## To create a document

1.  Create a [**FaxDocument**](-mfax-faxdocument.md) object.
2.  Set the cover page and fax body information for the object. A document can consist of a cover page, the fax body, or both, but must have at least one of these elements in order to be sent.
3.  Set other document properties. Note that many document properties have default values. These are described on the reference pages for the [**FaxDocument**](-mfax-faxdocument.md) properties.
4.  Set the information for one or more recipients. A document must have at least one recipient.
5.  Set the transmission information for the object.
6.  Submit the document to a fax server and receive a collection of outgoing fax jobs in return.
7.  Discard the [**FaxDocument**](-mfax-faxdocument.md) object or repeat steps 2 through 6.

The topic [Programmatic Fax Management](-mfax-programmatic-fax-management.md) provides a Microsoft Visual Basic [example](-mfax-sending-a-fax.md) of how to send a fax programmatically.

 

 



