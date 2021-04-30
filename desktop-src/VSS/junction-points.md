---
description: In Windows Vista and Windows Server 2008, the default locations for user data and system data have changed.
ms.assetid: 78679851-91f5-447f-8580-12cbf0323fb8
title: Junction Points
ms.topic: article
ms.date: 05/31/2018
---

# Junction Points

In Windows Vista and Windows Server 2008, the default locations for user data and system data have changed. For example, user data that was previously stored in the %SystemDrive%\\Documents and Settings directory is now stored in the %SystemDrive%\\Users directory. For backward compatibility, the old locations have junction points that point to the new locations. For example, C:\\Documents and Settings is now a junction point that points to C:\\Users. Backup applications must be capable of backing up and restoring junction points.

These junction points can be identified as follows:

-   They have the FILE\_ATTRIBUTE\_REPARSE\_POINT, FILE\_ATTRIBUTE\_HIDDEN, and FILE\_ATTRIBUTE\_SYSTEM file attributes set.
-   They also have their access control lists (ACLs) set to deny read access to everyone.

Applications that call out a specific path can traverse these junction points if they have the required permissions. However, attempts to enumerate the contents of the junction points will result in failures. It is important that backup applications do not traverse these junction points, or attempt to backup data under them, for two reasons:

-   Doing so can cause the backup application to back up the same data more than once.
-   It can also lead to cycles (circular references).

## Per-User Junctions and System Junctions

The junction points that are used to provide file and registry virtualization in Windows Vista and Windows Server 2008 can be divided into two classes: per-user junctions and system junctions.

Per-user junctions are created inside each individual user's profile to provide backward compatibility for user applications. The junction point at C:\\Users\\*username*\\My Documents that points to C:\\Users\\*username*\\Documents is an example of a per-user junction. Per-user junctions are created by the Profile service when the user's profile is created.

The other junctions are system junctions that do not reside under the Users\\*username* directory. Examples of system junctions include:

-   Documents and Settings
-   Junctions within the All Users, Public, and Default User profiles

System junctions are created by userenv.dll when it is invoked by Windows Welcome (also called the machine out-of-box-experience, or mOOBE).

> [!Note]  
> If the user changes the system language to a language other than English, the per-user and system junction points will be created with localized names.

 

 

 



