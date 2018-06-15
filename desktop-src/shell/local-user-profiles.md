---
Description: The system automatically creates a local user profile for each user when the user logs on to the computer for the first time. The system automatically maintains the settings for each user's work environment in a user profile on the local computer.
title: Local User Profiles
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Local User Profiles

Windows security requires a user profile for each user account on a computer. The system automatically creates a *local user profile* for each user when the user logs on to the computer for the first time. The system automatically maintains the settings for each user's work environment in a user profile on the local computer.

Windows Vista and later: User profiles are managed through the **User Accounts** control panel item.

Windows 2000 and Windows XP: To copy or delete a user profile, select **System** from the Control Panel, then the **Advanced** tab, and then the **Settings** button in the **User Profile** area.

The user's profile is not loaded automatically when the user is logged on using the [**LogonUser**](https://msdn.microsoft.com/en-us/library/Aa378184(v=VS.85).aspx) function. To load a user profile programmatically, use the [**LoadUserProfile**](/windows/desktop/api/Userenv/nf-userenv-loaduserprofilea) function. To unload a user profile loaded by **LoadUserProfile**, call the [**UnloadUserProfile**](/windows/desktop/api/Userenv/nf-userenv-unloaduserprofile) function.

 

 



