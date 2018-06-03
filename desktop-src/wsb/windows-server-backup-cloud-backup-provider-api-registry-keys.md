---
title: Cloud Backup Provider API Registry Keys
description: A cloud backup provider must register or de-register with the Windows Server Backup feature using the RegisterOnlineBackupWithWindowsServerBackup and DeregisterOnlineBackupFromWindowsServerBackup functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: C405C560-DE54-46CF-9FBF-0FC89416CEE7
ms.prod: windows-server-dev
ms.technology: windows-server-backup
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cloud Backup Provider API Registry Keys

A cloud backup provider must register or de-register with the Windows Server Backup feature using the [**RegisterOnlineBackupWithWindowsServerBackup**](/previous-versions/windows/desktop/api/WsbOnline/nf-wsbonline-registeronlinebackupwithwindowsserverbackup) and [**DeregisterOnlineBackupFromWindowsServerBackup**](/previous-versions/windows/desktop/api/WsbOnline/nf-wsbonline-deregisteronlinebackupfromwindowsserverbackup) functions. The registry keys should not be manually modified.

Using the string representation of the snap-in's **CLSID** as the key name, snap-ins register under the following key:

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**MMC**\\**SnapIns**

The **CLSID** of the snap-in extension must also be registered under the following key:

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**MMC**\\**&lt;ParentNodeType&gt;**\\**&lt;ParentNodeTypeGUID&gt;**\\**Extensions**\\**Namespace**

Note the following behaviors and requirements:

-   The **&lt;ParentNodeType&gt;** key is created by the Windows Server Backup parent snap-in during its registration.
-   The **{ParentNodetypeGUID}** key specifies the string representation of the GUID of the parent node type. The string must begin with an opening brace ({) and end with a closing brace (}).
-   There must also be a corresponding **{nodetypeGUID}** value in the primary (parent) snap-in's **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns\\{snapinCLSID}\\NodeTypes** key, where **{snapinCLSID}** is the parent snap-in's **CLSID**.
-   The Extensions key contains subkeys and values that list the snap-ins registered to extend the node type specified by **{nodetypeGUID}**.
-   The **{extensionsnapinCLSID}** key specifies the string representation of the **CLSID** of an extension snap-in.

## Related topics

<dl> <dt>

[About the Windows Server Backup Cloud Backup Provider API](about-the-windows-server-backup-cloud-backup-provider-api.md)
</dt> </dl>

 

 




