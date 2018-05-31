---
Description: This topic provides a detailed description of the five ways in which a fax can be sent.
ms.assetid: 7ce686c3-f095-465f-a479-f731e98f9d00
title: About Sending a Fax
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Sending a Fax

This topic provides a detailed description of the five ways in which a fax can be sent.

-   Printing from an application to the fax printer
-   Sending a cover-page-only fax
-   Sending a body file as a fax (C/C++ or Component Object Model (COM) APIs)
-   Sending a message from Microsoft Outlook 2000 or Microsoft Outlook 2002
-   Sending a fax by direct device context (DC) rendering

## Printing from an application to the fax printer

In this process, the fax is sent from within the application. The printing application directly renders the image to be printed (faxed) and no further conversion is required.

The fax printer driver saves the rendered image as a temporary Tagged Image File Format (TIFF) file and sends it to the fax service for queuing and transmission. The fax send wizard is displayed so the user can provide specific fax transmission data.

## Sending a cover-page-only fax

> [!Note]  
> This section applies only to Windows 2000, Windows XP and Windows Server 2003, not to any earlier or later versions of Windows.

 

This is useful if you want to send a single-page fax with a short note. To do this, click **Start**, point to **All Programs**, point to **Accessories**, point to **Communication**, point to **Fax**, and then click **Send a Fax** and complete the fax wizard. There is no document involved in the process. The cover page is rendered by the fax wizard to a temporary TIFF file and sent to the fax service for queuing and transmission.

## Sending a body file as a fax (C/C++ or COM APIs)

You can use the Windows 2000 C/C++ or COM APIs to send faxes locally or the Windows XP/Windows Server 2003 Extended Fax COM API to send faxes to a fax server.

If you specify a body in the fax message, it is considered a file path to a document which should be rendered to a temporary TIFF file. This is done on the fax client machine (not the server) by calling **ShellExecuteEx** with the *PrintTo* verb. The associated application is launched by the system and renders the document to the fax printer driver which saves it to a temporary file. That temporary file is then sent to the fax service for queuing and transmission. If the document is in itself a [TIFF file](#about-tiff-files), it is sent directly to the fax service for queuing and transmission, without calling **ShellExecuteEx**.

This process requires the following:

-   The application associated with the document type must be installed on the same machine where the program is running.
-   The application associated with the document type must support the *PrintTo* verb and silently print a document to the specified printer.

If one of these conditions is not met, the rendering of the body file to a fax message fails.

> [!Note]  
> Some document-based applications are designed for interaction with a user. These applications may not be capable of fully-automated printing or of running from a non-interactive context, such as a service context. If you encounter problems with specific document types, contact the vendor of the software that is used to render those documents.

 

## Sending a fax message from Outlook 2000 or Outlook 2002

Fax installs a MAPI transport that accepts messages from Outlook and sends them to the fax server. This is done by rendering the subject and body of the message to a temporary TIFF file and sending it to the fax service for queuing and transmission. If the body contains one or more attachments (not embedded objects but real message attachments), they are rendered to TIFF files by calling **ShellExecuteEx** with the *PrintTo* verb. The associated application is launched by the system and renders the document to the fax printer driver which saves it to a temporary file. That temporary file is then merged into the final fax message. If the document is in itself a [TIFF file](#about-tiff-files), it is sent directly to the fax service for queuing and transmission, without calling **ShellExecuteEx**.

This process requires the following:

-   The application associated with the document type must be installed on the same machine on which Outlook is running.
-   The application associated with the document type must support the *PrintTo* verb and silently print a document to the specified printer.

If one of these conditions is not met, the rendering of the Outlook message to a fax message fails and the user receives a non-deliverable receipt by email.

## Sending a fax by direct device context (DC) rendering

You can use the Windows 2000 C/C++ APIs [**FaxStartPrintJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxstartprintjoba) and [**FaxPrintCoverPage**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxprintcoverpagea) functions to receive a Windows Graphics Device Interface (GDI) DC construct and use the GDI APIs to render directly to that DC. The rendered DC is then submitted to the fax service for queuing and transmission. No document association is required in this process. This method is limited to C/C++ applications. This method can be used locally or remotely.

## About TIFF Files

The fax service will accept a TIFF file for transmission if it has the following properties:

-   Compression is either 1 (no compression) or 4 (CCITT Group 4 fax encoding)
-   Image width is 1728 pixels
-   X-Resolution &lt;= 204 dots per inch (dpi) and Y-Resolution &lt;= 200 dpi
-   All the pages have the same Y-resolution

 

 



