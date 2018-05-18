---
Description: 'If a computer is running Windows 2000 Server or later on a network, users can store their profiles on the server. These profiles are called roaming user profiles.'
title: Roaming User Profiles
---

# Roaming User Profiles

If a computer is running Windows 2000 Server or later on a network, users can store their profiles on the server. These profiles are called *roaming user profiles*.

Roaming user profiles have the following advantages:

-   Automatic resource availability. A user's unique profile is automatically available when he or she logs on to any computer on the network. Users do not need to create a profile on each computer they use on a network.
-   Simplified computer replacement and backup. When a user's computer must be replaced, it can be replaced easily because all of the user's profile information is maintained separately on the network, independent of an individual computer. When the user logs on to the new computer for the first time, the server copy of the user's profile is copied to the new computer.

The user's profile is not loaded automatically when the user is logged on using the [**LogonUser**](security.logonuser) function. To load a roaming user profile programmatically, use the [**LoadUserProfile**](loaduserprofile.md) function. To unload a roaming user profile loaded by **LoadUserProfile**, call the [**UnloadUserProfile**](unloaduserprofile.md) function.

 

 



