---
description: The system automatically creates a local user profile for each user when the user logs on to the computer for the first time. The system automatically maintains the settings for each user's work environment in a user profile on the local computer.
title: Local User Profiles
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 0e6c060e-025e-4d00-9b92-4f3b7bf66dda
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Local User Profiles

Windows security requires a user profile for each user account on a computer. The system automatically creates a *local user profile* for each user when the user logs on to the computer for the first time. The system automatically maintains the settings for each user's work environment in a user profile on the local computer.

Windows Vista and later: User profiles are managed through the **User Accounts** control panel item.

Windows 2000 and Windows XP: To copy or delete a user profile, select **System** from the Control Panel, then the **Advanced** tab, and then the **Settings** button in the **User Profile** area.

The user's profile is not loaded automatically when the user is logged on using the [**LogonUser**](/windows/win32/api/winbase/nf-winbase-logonusera) function. To load a user profile programmatically, use the [**LoadUserProfile**](/windows/desktop/api/Userenv/nf-userenv-loaduserprofilea) function. To unload a user profile loaded by **LoadUserProfile**, call the [**UnloadUserProfile**](/windows/desktop/api/Userenv/nf-userenv-unloaduserprofile) function.

 

 
