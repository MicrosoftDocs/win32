---
Description: This topic describes the Fax Service Client API.
ms.assetid: 823cc4fc-358f-43af-9799-1d0793cabe71
title: Fax Service Client API Functionality
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Service Client API Functionality

The Fax Service Client API enables fax client applications to perform the following tasks.

-   **Transmit a document stored on a computer.** The application can send a document as a fax to one recipient, or broadcast it to multiple application-defined recipients. For more information, see [Transmitting Faxes](-mfax-transmitting-faxes.md).

-   **Transmit a cover page.** Users can transmit a cover page with a fax. The cover page can be a common cover page located on a server, or it can be a personal cover page. For more information, see [Cover Pages](-mfax-cover-pages.md) and [Sending a Cover Page](-mfax-sending-a-cover-page.md).

-   **Transmit an active document by printing to a device context.** A document-based application can prevent the display of the Fax Send Wizard. The application can provide transmission information directly to the fax client Windows Graphics Device Interface (GDI) functions, and transmit an active document by printing it to a fax device context. For more information, see [Printing a Fax to a Device Context](-mfax-printing-a-fax-to-a-device-context.md).

-   **Transmit an active document using the Fax Send Wizard.** A user can transmit a document by printing it to a fax printer. The Fax Send Wizard collects transmission information from the user. A developer need only enable printing for this functionality to work.

-   **Change fax device and fax server configuration.** An application can provide configuration capabilities, or it can use the fax service administration application, a Microsoft Management Console (MMC) snap-in component, for configuration. For more information, see [Fax Server Configuration Management](-mfax-fax-server-configuration-management.md) and [Fax Device Management](-mfax-fax-device-management.md).

 

 



