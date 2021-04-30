---
description: The following API elements are used with user profiles.
title: User Profiles Reference
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 86871866-bb90-4287-9640-0a6cd136a800
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# User Profiles Reference

The following API elements are used with user profiles.

## Functions



| Function                                                                   | Description                                                                                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**CreateEnvironmentBlock**](/windows/desktop/api/Userenv/nf-userenv-createenvironmentblock)                   | Retrieves the environment variables for the specified user.                                                   |
| [**CreateProfile**](/windows/desktop/api/Userenv/nf-userenv-createprofile)                                     | Creates a new user profile. (Windows Vista and later only.)                                                   |
| [**DeleteProfile**](/windows/desktop/api/Userenv/nf-userenv-deleteprofilea)                                     | Deletes the user profile and all user-related settings from the specified computer.                           |
| [**DestroyEnvironmentBlock**](/windows/desktop/api/Userenv/nf-userenv-destroyenvironmentblock)                 | Frees environment variables created by the [**CreateEnvironmentBlock**](/windows/desktop/api/Userenv/nf-userenv-createenvironmentblock) function. |
| [**ExpandEnvironmentStringsForUser**](/windows/desktop/api/Userenv/nf-userenv-expandenvironmentstringsforusera) | Expands the source string by using the environment block established for the specified user.                  |
| [**GetAllUsersProfileDirectory**](/windows/desktop/api/Userenv/nf-userenv-getallusersprofiledirectorya)         | Retrieves the path to the root of the All Users profile.                                                      |
| [**GetDefaultUserProfileDirectory**](/windows/desktop/api/Userenv/nf-userenv-getdefaultuserprofiledirectorya)   | Retrieves the path to the root of the Default User profile.                                                   |
| [**GetProfilesDirectory**](/windows/desktop/api/Userenv/nf-userenv-getprofilesdirectorya)                       | Retrieves the path to the root directory where all user profiles are stored.                                  |
| [**GetProfileType**](/windows/desktop/api/Userenv/nf-userenv-getprofiletype)                                   | Retrieves the type of profile loaded for the current user.                                                    |
| [**GetUserProfileDirectory**](/windows/desktop/api/Userenv/nf-userenv-getuserprofiledirectorya)                 | Retrieves the path to the root directory of the specified user's profile.                                     |
| [**LoadUserProfile**](/windows/desktop/api/Userenv/nf-userenv-loaduserprofilea)                                 | Loads the specified user's profile.                                                                           |
| [**UnloadUserProfile**](/windows/desktop/api/Userenv/nf-userenv-unloaduserprofile)                             | Unloads a user's profile that was loaded by the [**LoadUserProfile**](/windows/desktop/api/Userenv/nf-userenv-loaduserprofilea) function.          |



 

The [**CreateUserProfileEx**](createuserprofileex.md) function is not supported.

## Structures



| Structure                          | Description                                |
|------------------------------------|--------------------------------------------|
| [**PROFILEINFO**](/windows/desktop/api/Profinfo/ns-profinfo-profileinfoa) | Contains information about a user profile. |



 

 

 



