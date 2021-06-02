---
description: Users and applications with administrative privileges can retrieve and modify network, URL, and media source list information for Windows Installer applications and patches on the system.
ms.assetid: e8c66bad-f594-4926-b3b4-c8b245dcfa83
title: Managing Installation Sources
ms.topic: article
ms.date: 05/31/2018
---

# Managing Installation Sources

Users and applications with administrative privileges can retrieve and modify network, URL, and media source list information for Windows Installer applications and patches on the system.

**Windows Installer 2.0:** Not supported. Administrators cannot read, reorder, or replace entries in the source list and cannot modify or retrieve source list properties. It is possible to manage Network sources, but not URL or Media sources. Administrators can only manage source lists for per-machine applications or applications installed as per-user for the current user. This prevents administrators using versions earlier than Windows Installer version 3.0 from managing source list information for all users in the system.

**Windows Installer 3.0 and later:** Users and applications that have administrator privileges can retrieve and modify source list information for Windows Installer applications and patches installed on the system for all users. The source list functions can be used to manage source lists and source list properties for network, URL and media sources. The installer can reorder source lists from an external process.

Users and applications that have administrative privileges can read and modify the following types of source list information:

-   Source lists for applications and patches installed for all users on the system.
-   Source lists for patch sources that exist apart from the application sources.
-   Source lists for URL and media sources that exist apart from network sources.
-   Source list properties such as [**MEDIAPACKAGEPATH**](mediapackagepath.md), [**DiskPrompt**](diskprompt.md), **LastUsedSource**, **LastUsedType**, and **PackageName**.

The source lists functions can limit the scope of the source lists found by specifying the installation context and user context. There are three possible installation contexts: per-user (unmanaged), per-machine, and per-user managed. The user context can be a particular user or all users on the system.

Non-administrators cannot modify the source list of an instance of an application or patch that exists under another user's per-user (managed or unmanaged) context. Non-administrators can modify the source lists of an instance of an application or patch installed under the following contexts:

-   Their own per-user(unmanaged) context.
-   The machine context, but only if the [DisableBrowse](disablebrowse.md), [AllowLockdownBrowse](allowlockdownbrowse.md), and [AlwaysInstallElevated](alwaysinstallelevated.md) policies allows them to browse for an application or patch source.
-   Their own per-user managed context, but only if the [DisableBrowse](disablebrowse.md), [AllowLockdownBrowse](allowlockdownbrowse.md), and [AlwaysInstallElevated](alwaysinstallelevated.md) policies allows them to browse for an application or patch source.

Administrators can modify any source list that a non-administrator can modify. In addition, administrators and applications that have administrative privileges can modify the source lists of an application or patch installed under the following contexts:

-   Per-machine context.
-   Their own per-user (unmanaged) or their own per-user managed context.
-   Another user's per-user managed context.

> [!Note]  
> Users and applications that have administrative privileges cannot modify the source list of an instance of an application or patch installed in the per-user (unmanaged) context of another user.

 

## Managing Network and URL sources for Products and Patches

Use the [**MsiSourceListAddSourceEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourceexa) function to add or reorder the source list of network and URL sources for a patch or application in a particular context. Use the *dwContext* parameter to specify the installation context. Use the *szUserSid* parameter to specify the user context.

Use the [**MsiSourceListAddSourceEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddsourceexa) function to create a source list for a patch that has not yet been applied to any application in the specified context. This can be useful when registering a patch to have elevated privileges. For more information about registering elevated privileges for a patch, see [Patching Per-User Managed Applications](patching-per-user-managed-applications.md).

Use the [**MsiSourceListClearSource**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearsourcea) function to remove an existing source for an application or patch in a specified context. Removing the current source for an application or patch forces the installer to search the source list for a source the next time a source is required.

Use the [**MsiSourceListEnumSources**](/windows/desktop/api/Msi/nf-msi-msisourcelistenumsourcesa) function to enumerate sources in the source list of a specified patch or application.

## Managing Media sources for Products and Patches

Use the [**MsiSourceListAddMediaDisk**](/windows/desktop/api/Msi/nf-msi-msisourcelistaddmediadiska) function to add or update the disk information of the media source of a registered application or patch. Each entry is uniquely identified by a disk ID. If the disk already exists, it is updated with the new volume label and disk prompt values. If the disk does not exist, a new disk entry is created with the new values.

Use the [**MsiSourceListClearMediaDisk**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearmediadiska) function to remove an existing registered disk under the media source for an application or patch in a specific context.

Use the [**MsiSourceListEnumMediaDisks**](/windows/desktop/api/Msi/nf-msi-msisourcelistenummediadisksa) function to enumerate a list of disks registered under the media source for an application or patch.

## Retrieval and modification of source list information

Use the [**MsiSourceListGetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistgetinfoa) and [**MsiSourceListSetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistsetinfoa) functions to retrieve or modify information about the source list for an application or patch in a specific context. Use the *dwContext* parameter to specify the installation context. Use the *szUserSid* parameter to specify the user context.

Source list properties such as [**MEDIAPACKAGEPATH**](mediapackagepath.md), [**DiskPrompt**](diskprompt.md), **LastUsedSource**, **LastUsedType**, and **PackageName** can be accessed.

> [!Note]  
> The **LastUsedType** source list property can only be read. It cannot be set directly using the [**MsiSourceListSetInfo**](/windows/desktop/api/Msi/nf-msi-msisourcelistsetinfoa) function.

 

## Clearing the complete source list or forcing a source resolution

Use the [**MsiSourceListClearAllEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistclearallexa) function to remove all the existing sources of a given source type for the specified application or patch instance. The patch registration is also removed if the patch is not installed by any application in the same context. Use the *dwContext* parameter to specify the installation context. Use the *szUserSid* parameter to specify the user context.

Use the [**MsiSourceListForceResolutionEx**](/windows/desktop/api/Msi/nf-msi-msisourcelistforceresolutionexa) to clear the last used source entry for an application or patch in the specified context. This function removes the registration of the property called **LastUsedSource**. This function does not affect the registered source list. Clearing the **LastUsedSource** registration forces the installer to do a source resolution against the registered sources the next time it requires the source.

 

 



