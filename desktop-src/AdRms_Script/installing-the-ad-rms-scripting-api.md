---
Description: A .NET assembly that is installed in the global assembly cache (GAC) when the operating system is installed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ac8c911a-e7c0-48a2-80ad-924afad27289
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Installing the AD RMS Scripting API
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Installing the AD RMS Scripting API

The AD RMS administration API is a .NET assembly that is installed in the global assembly cache (GAC) when the operating system is installed. The assembly contains public and private objects. To use the public objects in Windows Script Host (WSH) with VBScript, the objects must be registered. They are registered on a local server during the provisioning process.

**To add the API to a remote server**

1.  In the Server Manager, right-click the **Features** node and click **Add Features**.
2.  In the Add Features wizard, expand **Remote Server Administration Tools** and then expand the **Role Administration Tools** node.
3.  Select **Active Directory Rights Management Services** and click **Install**.

## Related topics

<dl> <dt>

[About the Active Directory Rights Management Services Scripting API](about-the-active-directory-rights-management-services-scripting-api.md)
</dt> </dl>

 

 



