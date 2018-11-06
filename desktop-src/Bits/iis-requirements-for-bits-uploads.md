---
title: IIS Requirements for BITS Uploads
description: For uploads, BITS requires IIS 6.0 on Windows Server 2003, and IIS 7.0 on Windows Server 2008; BITS does not support IIS 5.1 on Windows XP.
ms.assetid: 8ab07af5-3b59-4c98-8e57-f614deb8b594
ms.topic: article
ms.date: 05/31/2018
---

# IIS Requirements for BITS Uploads

For uploads, BITS requires IIS 6.0 on Windows Server 2003, and IIS 7.0 on Windows Server 2008; BITS does not support IIS 5.1 on Windows XP. The IIS virtual directory must be enabled for uploads and have the BITS IIS extensions configured.

**Core installations of Windows Server:** BITS IIS extensions are not supported.

On Windows Server 2008, use the **Server Manager** to install the BITS Server Extensions feature. From **Server Manager**, click **Features** in the left pane. In the **Add Features Wizard**, check BITS Server Extensions. Note that the IIS 6 Management Compatibility roles must be installed.

On Windows Server 2003, use the **Windows Components Wizard** to install the BITS server extension. From **Control Panel**, select **Add or Remove Programs**. Then, select **Add/Remove Windows Components** to display the **Windows Components Wizard**. The BITS server extension is a subcomponent of Internet Information Services (IIS) which is a sub-component of Web Application Server.

> [!Note]  
> If the IISAdmin service is restarted, the IIS worker process must be recycled before the BITS service can resume uploads. The IIS worker process can be manually recycled by using the **IISReset.exe** command line utility.

 

For information on configuring IIS for uploads, see [Setting Up the Server for Uploads](setting-up-the-server-for-uploads.md).

For details on the properties that BITS adds to IIS, see [BITS Server Settings for Upload Jobs](bits-server-settings-for-upload-jobs.md).

 

 




