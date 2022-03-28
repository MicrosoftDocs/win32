---
description: The system creates a user profile the first time that a user logs on to a computer. At subsequent logons, the system loads the user's profile, and then other system components configure the user's environment according to the information in the profile.
title: About User Profiles
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 333f1861-91fe-4796-af13-dd300a5c6ec3
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# About User Profiles

The system creates a user profile the first time that a user logs on to a computer. At subsequent logons, the system loads the user's profile, and then other system components configure the user's environment according to the information in the profile.

## Types of User Profiles

- [Local User Profiles](local-user-profiles.md). A local user profile is created the first time that a user logs on to a computer. The profile is stored on the computer's local hard disk. Changes made to the local user profile are specific to the user and to the computer on which the changes are made.
- [Roaming User Profiles](roaming-user-profiles.md). A roaming user profile is a copy of the local profile that is copied to, and stored on, a server share. This profile is downloaded to any computer that a user logs onto on a network. Changes made to a roaming user profile are synchronized with the server copy of the profile when the user logs off. The advantage of roaming user profiles is that users do not need to create a profile on each computer they use on a network.
- [Mandatory User Profiles](mandatory-user-profiles.md). A mandatory user profile is a type of profile that administrators can use to specify settings for users. Only system administrators can make changes to mandatory user profiles. Changes made by users to desktop settings are lost when the user logs off.
- [Temporary User Profiles](temporary-user-profiles.md). A temporary profile is issued each time that an error condition prevents the user's profile from loading. Temporary profiles are deleted at the end of each session, and changes made by the user to desktop settings and files are lost when the user logs off. Temporary profiles are only available on computers running Windows 2000 and later.

A user profile consists of the following elements:

-   A registry hive. The registry hive is the file NTuser.dat. The hive is loaded by the system at user logon, and it is mapped to the **HKEY\_CURRENT\_USER** registry key. The user's registry hive maintains the user's registry-based preferences and configuration.
-   A set of profile folders stored in the file system. User-profile files are stored in the **Profiles** directory, on a folder per-user basis. The user-profile folder is a container for applications and other system components to populate with sub-folders, and per-user data such as documents and configuration files. Windows Explorer uses the user-profile folders extensively for such items as the user's Desktop, **Start** menu and **Documents** folder.

User profiles provide the following advantages:

-   When the user logs on to a computer, the system uses the same settings that were in use when the user last logged off.
-   When sharing a computer with other users, each user receives their customized desktop after logging on.
-   Settings in the user profile are unique to each user. The settings cannot be accessed by other users. Changes made to one user's profile do not affect other users or other users' profiles.

## User Profile Tiles in Windows 7 and Later

In Windows 7 or later, each user profile has an associated image presented as a user tile. These tiles appear to users on the **User Accounts** Control Panel item and its **Manage Accounts** subpage.. The image files for the default Guest and default User accounts also appear here if you have Administrator access rights.

> [!Note]  
> The **Manage Accounts** subpage is accessed through the **Manage another account** link in the **User Accounts** Control Panel item.

 

-   %ProgramData%\\Microsoft\\User Account Pictures\\Guest.bmp
-   %ProgramData%\\Microsoft\\User Account Pictures\\User.bmp

The user's tile image is stored in the %SystemDrive%\\Users\\&lt;username&gt;\\AppData\\Local\\Temp folder as &lt;username&gt;.bmp. Any slash characters (\\) are converted to plus sign characters (+). For example, DOMAIN\\user is converted to DOMAIN+user.

The image file appears in the user's **Temp** folder:

-   After the user completes the initial system setup (OOBE).
-   When the user first launches the **User Accounts** Control Panel item.
-   When the user goes to the **Manage Accounts** subpage of the **User Accounts** Control Panel item. In addition, tiles for all other users on the computer are shown.

Those instances are the only times that the images are created or updated. Therefore, there are several caveats to keep in mind when using the **Temp** folder location programmatically:

1.  The user's tile is not guaranteed to be present. If the user deletes the .bmp file, for instance manually or through a utility that deletes temporary files, that user tile is not automatically recreated until the user launches the **User Accounts** Control Panel item or **Manage Accounts** subpage.

2.  User tiles for other users on the computer might not be present in the currently logged-on user's **Temp** folder. For example, if User A creates User B through the **User Accounts** Control Panel item, User B's tile is created in User A's **Temp** folder when Windows sends User A to the **Manage Accounts** subpage. Because the directory structure is not created for User B until he or she logs on, User A's **Temp** folder is the only location that User B's tile is stored. When User B logs on, the only image stored in User B's **Temp** folder is his or her own.

    1.  To get all user tiles for users on a system, applications might need to search in each user's **Temp** directory.
    2.  Because the access control list (ACL) of these **Temp** directories allows access to SYSTEM, Administrator, and the current user, applications need to elevate to access for other users.

3.  Other users' tiles are not guaranteed to be up-to-date in their **Temp** folders. If User B updates his or her user tile, User A will not see the change until User A accesses the **Manage Accounts** subpage. Therefore, if applications use User A's **Temp** folder to obtain User B's tile, those applications can get an out-of-date image file.

## Related topics

<dl> <dt>

[Local User Profiles](local-user-profiles.md)
</dt> <dt>

[Roaming User Profiles](roaming-user-profiles.md)
</dt> <dt>

[Mandatory User Profiles](mandatory-user-profiles.md)
</dt> <dt>

[Temporary User Profiles](temporary-user-profiles.md)
</dt> <dt>

[Profiles Directory](profiles-directory.md)
</dt> <dt>

[User Environment Variables](user-environment-variables.md)
</dt> <dt>

[Fast User Switching](fast-user-switching.md)
</dt> </dl>

 

 



