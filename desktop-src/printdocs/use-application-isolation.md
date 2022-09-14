---
description: Apps can declare printer-driver isolation in their app manifest to isolate the app from the printer driver and improve the apps reliability.
ms.assetid: 80650C46-AC96-46FD-894A-4F34B056AB79
ms.topic: article
title: "How To: Use Application Isolation"
ms.date: 05/31/2018
---

# How To: Use Application Isolation

Apps can declare printer-driver isolation in their app manifest to isolate the app from the printer driver and improve the app's reliability. The Windows print service allows printer drivers to run in processes that are separate from the process in which the print spooler runs. Using this feature your app prevents it from crashing in the event the printer driver has an error.

Printer-driver isolation is implemented in Windows 7 and Windows Server 2008 R2.

### Prerequisites

-   A managed-code or Windows Store app that uses Windows printing.

## Instructions

### Update the app manifest

Enabling printer-driver isolation requires you to add the **printerDriverIsolation** element to the app's manifest. Here's how:

1.  Edit the app manifest, adding the **printerDriverIsolation** element with a value of **true** to the **windowsSettings** element of the **application** element, as shown in this example.
    ```XML
    <application xmlns="urn:schemas-microsoft-com:asm.v3">
        <windowsSettings>
            <printerDriverIsolation xmlns="http://schemas.microsoft.com/SMI/2011/WindowsSettings">true</printerDriverIsolation>
        </windowsSettings>
    </application>
    ```

    

2.  Rebuild your app.

 

 



