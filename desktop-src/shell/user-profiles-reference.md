---
Description: 'The following API elements are used with user profiles.'
title: User Profiles Reference
---

# User Profiles Reference

The following API elements are used with user profiles.

## Functions



| Function                                                                   | Description                                                                                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**CreateEnvironmentBlock**](createenvironmentblock.md)                   | Retrieves the environment variables for the specified user.                                                   |
| [**CreateProfile**](createprofile.md)                                     | Creates a new user profile. (Windows Vista and later only.)                                                   |
| [**DeleteProfile**](deleteprofile.md)                                     | Deletes the user profile and all user-related settings from the specified computer.                           |
| [**DestroyEnvironmentBlock**](destroyenvironmentblock.md)                 | Frees environment variables created by the [**CreateEnvironmentBlock**](createenvironmentblock.md) function. |
| [**ExpandEnvironmentStringsForUser**](expandenvironmentstringsforuser.md) | Expands the source string by using the environment block established for the specified user.                  |
| [**GetAllUsersProfileDirectory**](getallusersprofiledirectory.md)         | Retrieves the path to the root of the All Users profile.                                                      |
| [**GetDefaultUserProfileDirectory**](getdefaultuserprofiledirectory.md)   | Retrieves the path to the root of the Default User profile.                                                   |
| [**GetProfilesDirectory**](getprofilesdirectory.md)                       | Retrieves the path to the root directory where all user profiles are stored.                                  |
| [**GetProfileType**](getprofiletype.md)                                   | Retrieves the type of profile loaded for the current user.                                                    |
| [**GetUserProfileDirectory**](getuserprofiledirectory.md)                 | Retrieves the path to the root directory of the specified user's profile.                                     |
| [**LoadUserProfile**](loaduserprofile.md)                                 | Loads the specified user's profile.                                                                           |
| [**UnloadUserProfile**](unloaduserprofile.md)                             | Unloads a user's profile that was loaded by the [**LoadUserProfile**](loaduserprofile.md) function.          |



 

The [**CreateUserProfileEx**](createuserprofileex.md) function is not supported.

## Structures



| Structure                          | Description                                |
|------------------------------------|--------------------------------------------|
| [**PROFILEINFO**](profileinfo.md) | Contains information about a user profile. |



 

 

 



