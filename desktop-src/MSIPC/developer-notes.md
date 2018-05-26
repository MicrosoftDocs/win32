---
title: Developer guidance and information
description: This section covers specific guidance for several important development scenarios as well as general information about developing with this SDK.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 5A9F04FD-0FCD-482F-8671-36FE93B783B0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- RMS SDK Active Directory Rights Management Services SDK 2.0 , development scenarios
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Developer guidance and information

This section covers specific guidance for several important development scenarios as well as general information about developing with this SDK. The scenarios in this section are specific to this release of the Rights Management Services SDK 2.1 and may be altered in subsequent releases.

## In this section

<dl> <dt>

[How-to: use ADAL authentication](authentication-with-adal.md)
</dt> <dd>

Authentication with Azure RMS for your app using Azure Active Directory Authentication Library (ADAL).

</dd> <dt>

[How-to: add explicit owner rights](add-explicit-owner-rights.md)
</dt> <dd>

Your application should explicitly add "Owner" rights when creating a license from scratch ([**IpcCreateLicenseFromScratch**](ipccreatelicensefromscratch.md)).

</dd> <dt>

[How-to: debug a rights-enabled application](debugging-applications-that-use-ad-rms.md)
</dt> <dd>

The following topic shows how to debug your application and use the Windows Event Log.

</dd> <dt>

[How-to: enable document tracking and revocation](tracking-content.md)
</dt> <dd>

This topic covers the basic guidance for implementing document tracking of content as well as example code for metadata updates and for creating a **Track Usage** button for your app.

</dd> <dt>

[How-to: enable email notification](how-to--enable-email-notification.md)
</dt> <dd>

Email notification allows for a protected content owner to be notified when his or her content is accessed.

</dd> <dt>

[How-to: enable your service application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md)
</dt> <dd>

This topic outlines steps for setting up your service application to use Azure Rights Management.

</dd> <dt>

[How-to: install and configure an RMS server](how-to-install-and-configure-an-rms-server.md)
</dt> <dd>

This topic covers the steps to connect to an RMS Sever for testing your rights-enabled application.

</dd> <dt>

[How-to: set the API security mode](setting-the-api-security-mode--api-mode-.md)
</dt> <dd>

You can choose which security mode your File API application runs in by using the [**IpcSetGlobalProperty**](ipcsetglobalproperty.md) function.

</dd> <dt>

[How-to: work with encryption settings](working-with-encryption.md)
</dt> <dd>

This topic orients you to our encryption packages and shows some code snips for their use.

</dd> <dt>

[Application types](application-types.md)
</dt> <dd>

This topic covers types of applications that you might choose to create as rights-enabled.

</dd> <dt>

[File API configuration](file-api-configuration.md)
</dt> <dd>

The File API's behavior can be configured through settings in the registry.

</dd> <dt>

[Supported file formats](supported-file-formats.md)
</dt> <dd>

The File API supports native and Pfile formats.

</dd> <dt>

[Supported platforms](supported-platforms.md)
</dt> <dd>

This topic identifies the RMS SDK 2.1 supported client and server platforms.

</dd> <dt>

[Understanding usage restrictions](understanding-usage-restrictions.md)
</dt> <dd>

All RMS enabled applications must enforce usage restrictions.

</dd> <dt>

[Usage restriction reference](usage-restriction-reference.md)
</dt> <dd>

Usage restrictions are defined by the constants listed in this topic.

</dd> </dl>

## Related topics

<dl> <dt>

[Overview](ad-rms-overview.md)
</dt> </dl>

 

 




