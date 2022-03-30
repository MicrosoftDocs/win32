---
description: If a computer is running Windows 2000 Server or later on a network, users can store their profiles on the server. These profiles are called roaming user profiles.
title: Roaming User Profiles
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 8af06fdf-be99-4295-8f11-7d7f68e66956
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Roaming User Profiles

If a computer is running Windows 2000 Server or later on a network, users can store their profiles on the server. These profiles are called *roaming user profiles*.

Roaming user profiles have the following advantages:

- Automatic resource availability. A user's unique profile is automatically available when he or she logs on to any computer on the network. Users do not need to create a profile on each computer they use on a network.
- Simplified computer replacement and backup. When a user's computer must be replaced, it can be replaced easily because all of the user's profile information is maintained separately on the network, independent of an individual computer. When the user logs on to the new computer for the first time, the server copy of the user's profile is copied to the new computer.

The user's profile is not loaded automatically when the user is logged on using the [**LogonUser**](/windows/win32/api/winbase/nf-winbase-logonusera) function. To load a roaming user profile programmatically, use the [**LoadUserProfile**](/windows/desktop/api/Userenv/nf-userenv-loaduserprofilea) function. To unload a roaming user profile loaded by **LoadUserProfile**, call the [**UnloadUserProfile**](/windows/desktop/api/Userenv/nf-userenv-unloaduserprofile) function.

 

 
