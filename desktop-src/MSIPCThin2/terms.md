---
title: Terms
description: A collection of terminology definitions specific to Rights Management Services.
Robots: noindex, nofollow
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: adb1f868-0da7-431b-83d1-86f41c2da4ae
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Terms

A collection of terminology definitions specific to Rights Management Services.

<dl> <dt>

<span id="msipcthin2.depracated_algorithm"></span><span id="MSIPCTHIN2.DEPRACATED_ALGORITHM"></span>**Deprecated Algorithm**
</dt> <dd>

A modal setting that implements an older content protection scheme, specifically referring to electronic cookbook cipher mode (ECB). In this SDK, the setting allows you to generate licenses compatible with the MSDRM library used by the [AD Rights Management Services SDK](https://msdn.microsoft.com/library/windows/desktop/cc530379.aspx).

This setting may cause your application to protect content in a way that does not conform to your customers' standards for content protection.

This setting will prevent your application from benefitting from any cryptographic enhancements added to Microsoft Rights Management SDK 3.0 or later.

</dd> <dt>

<span id="msipcthin2.pfile"></span><span id="MSIPCTHIN2.PFILE"></span>**Microsoft Protected File Format**
</dt> <dd>

Also referred to as PFile format, it is the default file format for AD RMS and functions as a standard across RMS-enabled applications.

PFile format is transparent to the application developer as it is embedded in the way Rights Management SDK 4.2 is designed.

</dd> </dl>

 

 




