---
Description: As a manager of shared resources, Removable Storage Manager ensures that client applications do not corrupt each others data.
ms.assetid: 97180d9c-9ac7-4802-95a7-2832c94750c2
title: RSM Media Identification and Naming
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RSM Media Identification and Naming

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

As a manager of shared resources, Removable Storage Manager ensures that client applications do not corrupt each other's data. Securing media pools prevents an application from modifying the data of another application. For more information, see [RSM Security](rsm-security.md). Another way to accomplish this is to assign each medium a unique name which applications can use to refer to it, and to track the identities of all media in a system, ensuring that the mapping between the unique name and the physical media is always accurate.

A library management system could simply use a media's home slot as its identity. A request to mount a medium in a drive could be as simple as "Mount the medium in slot 6 of drive 2." There are problems with this minimalist approach, however. An administrator could exchange the medium in slot 6 for that in slot 7 during a door access. An application executing the request might get a medium it did not expect and not know it. To prevent this, Removable Storage Manager assigns each medium a unique name, which is used to refer to the medium programmatically. Removable Storage Manager uses globally unique identifiers (GUIDs) as the form for these names.

Removable Storage Manager identifies each medium side by reading its label. At various times, Removable Storage Manager reads the label to ensure that the name it has for a medium maps correctly. Consider a refinement of the example given earlier. If the name of a medium simply referred to the medium in slot 7, an administrator could change the contents of slot 7 during a door access and the next time an application used the name it would get a different medium. Removable Storage Manager prevents this by associating information stored in the medium's label with its name. Each time a medium is mounted, for example, Removable Storage Manager reads the label to ensure that the medium it mounted is correct. An inventory is an operation that an administrator can request or that Removable Storage Manager can initiate, which verifies the labels associated with each named medium in a library.

Administrators need to identify media uniquely, and since GUIDs are difficult to read in printed form, Removable Storage Manager also assigns each medium a display name. These names are changeable so if an administrator has a naming scheme for media, a display name can be assigned that is different from the one Removable Storage Manager initially assigned.

For more information, see the following topics:

-   [On-media Identifiers](on-media-identifiers.md)
-   [Duplicate Copies of Media](duplicate-copies-of-media.md)
-   [Bar Codes](bar-codes.md)
-   [Media Names](media-names.md)

 

 



