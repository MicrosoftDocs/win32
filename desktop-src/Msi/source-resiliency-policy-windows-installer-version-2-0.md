---
description: Windows Installer version 2.0 begins searching for a source by checking the most recently used source location in the source list, then the list of network sources, then media sources, and finally URL sources.
ms.assetid: 21b1a31e-efe3-4d45-b1c5-fe6ed9b19fed
title: Source Resiliency Policy
ms.topic: article
ms.date: 05/31/2018
---

# Source Resiliency Policy

The installer begins searching for a source by checking the most recently used source location in the source list, then the list of network sources, then media sources, and finally URL sources. For more information, see [Source Resiliency](source-resiliency.md). If the search fails, the installer may present a [Browse Dialog](browse-dialog.md) enabling the user to search for the source manually. The browse dialog box cannot be displayed if the [user interface levels](user-interface-levels.md) is set to None. An administrator controls the display of the browse dialog box to users by setting system policy.

With Windows Installer, nonadministrators by default cannot use the browse dialog box to locate managed application sources on media and cannot install managed applications. An administrator enables a nonadministrator to browse or install managed applications from media by using the [AllowLockdownBrowse](allowlockdownbrowse.md) and [AllowLockdownMedia](allowlockdownmedia.md) policies. An administrator disables the capability to browse or install applications from media by using the [DisAbleBrowse](disablebrowse.md) and [DisAbleMedia](disablemedia.md) policies.

The following table summarizes the use of these system policies in Windows Installer.



| System Policy                                  | NonAdministrator User NonManaged Application                                                                                                             | NonAdministrator User Managed Application                                                                                                                 | Administrator Managed Application NonManaged Application                                                                                               |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AllowLockdownBrowse](allowlockdownbrowse.md) | Users can install unmanaged applications using sources located on media. Users can browse media for the sources of unmanaged applications.<br/>    | Users cannot install managed applications using sources located on media. Users can browse media for the sources of managed applications.<br/>      | Administrators can install applications using sources located on media. Administrators can browse media for the sources of applications.<br/>    |
| [AllowLockdownMedia](allowlockdownmedia.md)   | Users can install unmanaged applications using sources located on media. Users can browse media for the sources of unmanaged applications.<br/>    | Users can install managed applications using sources located on media. Users cannot browse media for the sources of managed applications.<br/>      | Administrators can install applications using sources located on media. Administrators can browse media for the sources of applications.<br/>    |
| *Default*                                      | Users can install unmanaged applications using sources located on media. Users can browse media for the sources of unmanaged applications.<br/>    | Users cannot install managed applications using sources located on media. Users cannot browse media for the sources of managed applications.<br/>   | Administrators can install applications using sources located on media. Administrators can browse media for the sources of applications.<br/>    |
| [DisAbleBrowse](disablebrowse.md)             | Users can install unmanaged applications using sources located on media. Users cannot browse media for the sources of unmanaged applications.<br/> | Users cannot install managed applications using sources located on media. Users cannot browse media for the sources of managed applications. .<br/> | Administrators can install applications using sources located on media. Administrators cannot browse media for the sources of applications.<br/> |
| [DisAbleMedia](disablemedia.md)               | Users cannot install unmanaged applications using sources located on media. Users can browse media for the sources of unmanaged applications.<br/> | Users cannot install managed applications using sources located on media. Users cannot browse media for the sources of managed applications.<br/>   | Administrators cannot install applications using sources located on media. Administrators can browse media for the sources of applications.<br/> |



 

## Related topics

<dl> <dt>

[Source Resiliency](source-resiliency.md)
</dt> </dl>

 

 




