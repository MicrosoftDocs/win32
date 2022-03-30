---
description: The system creates a user profile the first time that a user logs on to a computer. At subsequent logons, the system loads the user's profile, and then other system components configure the user's environment according to the information in the profile.
title: About User Profiles
ms.topic: article
ms.date: 03/28/2022
ms.assetid: 333f1861-91fe-4796-af13-dd300a5c6ec3
topic_type: 
 - kbArticle
---

# About User Profiles

The system creates a user profile the first time that a user logs on to a computer. At subsequent logons, the system loads the user's profile, and then other system components configure the user's environment according to the information in the profile.

## Types of User Profiles

- [Local User Profiles](local-user-profiles.md). A local user profile is created the first time that a user logs on to a computer. The profile is stored on the computer's local hard disk. Changes made to the local user profile are specific to the user and to the computer on which the changes are made.
- [Roaming User Profiles](roaming-user-profiles.md). A roaming user profile is a copy of the local profile that is copied to, and stored on, a server share. This profile is downloaded to any computer that a user logs onto on a network. Changes made to a roaming user profile are synchronized with the server copy of the profile when the user logs off. The advantage of roaming user profiles is that users do not need to create a profile on each computer they use on a network.
- [Mandatory User Profiles](mandatory-user-profiles.md). A mandatory user profile is a type of profile that administrators can use to specify settings for users. Only system administrators can make changes to mandatory user profiles. Changes made by users to desktop settings are lost when the user logs off.
- [Temporary User Profiles](temporary-user-profiles.md). A temporary profile is issued each time that an error condition prevents the user's profile from loading. Temporary profiles are deleted at the end of each session, and changes made by the user to desktop settings and files are lost when the user logs off.

## Elements of a user profile

A user profile consists of the following elements:

- A registry hive. The registry hive is the file **NTuser.dat**. The hive is loaded by the system at user logon, and it is mapped to the **HKEY\_CURRENT\_USER** registry key. The user's registry hive maintains the users registry-based preferences and configuration.
- A set of profile folders stored in the file system. User-profile files are stored in the **Profiles** directory, on a folder per-user basis. The user-profile folder is a container for applications and other system components to populate with sub-folders, and per-user data such as documents and configuration files. Windows Explorer uses the user-profile folders extensively for such items as the user's Desktop, **Start** menu and **Documents** folder.

User profiles provide the following advantages:

- When the user logs on to a computer, the system uses the same settings that were in use when the user last logged off.
- When sharing a computer with other users, each user receives their customized desktop after logging on.
- Settings in the user profile are unique to each user. The settings cannot be accessed by other users. Changes made to one user's profile do not affect other users or other users' profiles.

## User profile pictures

Each user profile has an associated image presented as a user tile. These tiles can be set on the **Accounts** page in the Settings App. The image files for the default Guest and default User accounts also appear here if you have Administrator access rights.

> [!NOTE]
> If a Microsoft Account is linked to a user profile, the user profile image is the Microsoft Account image.

- %ProgramData%\\Microsoft\\User Account Pictures\\Guest.bmp
- %ProgramData%\\Microsoft\\User Account Pictures\\User.bmp

## Related topics

- [Local User Profiles](local-user-profiles.md)
- [Roaming User Profiles](roaming-user-profiles.md)
- [Mandatory User Profiles](mandatory-user-profiles.md)
- [Temporary User Profiles](temporary-user-profiles.md)
- [Profiles Directory](profiles-directory.md)
- [User Environment Variables](user-environment-variables.md)
- [Fast User Switching](fast-user-switching.md)
