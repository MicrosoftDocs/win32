---
Description: 'Although Removable Storage Manager tries to uniquely identify each cartridge that it manages, it also handles media duplicates.'
ms.assetid: '508e2642-67a1-46f0-9488-0071a72ddf46'
title: Duplicate Copies of Media
---

# Duplicate Copies of Media

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

Although Removable Storage Manager tries to uniquely identify each cartridge that it manages, it also handles media duplicates. It treats identical media as separate media that are identical in every way and can be used interchangeably. For example, if a user has two copies of a CD and places both in a changer, Removable Storage Manager shows both media and each can be mounted, ejected, and so on, separately. Because each has its own record in the database, it is possible to attach different attributes to each media. You can give each a different display name, for example, although this is discouraged because there is no guarantee that these differing attributes will always be associated with the same cartridge. If both are ejected, the attributes may be reversed when both are inserted again.

 

 



