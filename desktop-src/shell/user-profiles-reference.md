---
Description: The following API elements are used with user profiles.
title: User Profiles Reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# User Profiles Reference

The following API elements are used with user profiles.

## Functions



| Function                                                                   | Description                                                                                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**CreateEnvironmentBlock**](/windows/win32/Userenv/nf-userenv-createenvironmentblock?branch=master)                   | Retrieves the environment variables for the specified user.                                                   |
| [**CreateProfile**](/windows/win32/Userenv/nf-userenv-createprofile?branch=master)                                     | Creates a new user profile. (Windows Vista and later only.)                                                   |
| [**DeleteProfile**](/windows/win32/Userenv/nf-userenv-deleteprofilea?branch=master)                                     | Deletes the user profile and all user-related settings from the specified computer.                           |
| [**DestroyEnvironmentBlock**](/windows/win32/Userenv/nf-userenv-destroyenvironmentblock?branch=master)                 | Frees environment variables created by the [**CreateEnvironmentBlock**](/windows/win32/Userenv/nf-userenv-createenvironmentblock?branch=master) function. |
| [**ExpandEnvironmentStringsForUser**](/windows/win32/Userenv/nf-userenv-expandenvironmentstringsforusera?branch=master) | Expands the source string by using the environment block established for the specified user.                  |
| [**GetAllUsersProfileDirectory**](/windows/win32/Userenv/nf-userenv-getallusersprofiledirectorya?branch=master)         | Retrieves the path to the root of the All Users profile.                                                      |
| [**GetDefaultUserProfileDirectory**](/windows/win32/Userenv/nf-userenv-getdefaultuserprofiledirectorya?branch=master)   | Retrieves the path to the root of the Default User profile.                                                   |
| [**GetProfilesDirectory**](/windows/win32/Userenv/nf-userenv-getprofilesdirectorya?branch=master)                       | Retrieves the path to the root directory where all user profiles are stored.                                  |
| [**GetProfileType**](/windows/win32/Userenv/nf-userenv-getprofiletype?branch=master)                                   | Retrieves the type of profile loaded for the current user.                                                    |
| [**GetUserProfileDirectory**](/windows/win32/Userenv/nf-userenv-getuserprofiledirectorya?branch=master)                 | Retrieves the path to the root directory of the specified user's profile.                                     |
| [**LoadUserProfile**](/windows/win32/Userenv/nf-userenv-loaduserprofilea?branch=master)                                 | Loads the specified user's profile.                                                                           |
| [**UnloadUserProfile**](/windows/win32/Userenv/nf-userenv-unloaduserprofile?branch=master)                             | Unloads a user's profile that was loaded by the [**LoadUserProfile**](/windows/win32/Userenv/nf-userenv-loaduserprofilea?branch=master) function.          |



 

The [**CreateUserProfileEx**](createuserprofileex.md) function is not supported.

## Structures



| Structure                          | Description                                |
|------------------------------------|--------------------------------------------|
| [**PROFILEINFO**](/windows/win32/Profinfo/ns-profinfo-_profileinfoa?branch=master) | Contains information about a user profile. |



 

 

 



