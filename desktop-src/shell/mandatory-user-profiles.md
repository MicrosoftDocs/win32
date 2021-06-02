---
description: A mandatory user profile is a special type of pre-configured roaming user profile that administrators can use to specify settings for users.
title: Mandatory User Profiles
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 09616c7f-1cec-48a0-a953-d4ae35fbd2f6
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Mandatory User Profiles

A mandatory user profile is a special type of pre-configured [roaming user profile](roaming-user-profiles.md) that administrators can use to specify settings for users. With mandatory user profiles, a user can modify his or her desktop, but the changes are not saved when the user logs off. The next time the user logs on, the mandatory user profile created by the administrator is downloaded. There are two types of mandatory profiles: *normal mandatory* profiles and *super-mandatory* profiles.

User profiles become mandatory profiles when the administrator renames the NTuser.dat file (the registry hive) on the server to NTuser.man. The .man extension causes the user profile to be a read-only profile.

User profiles become *super-mandatory* when the folder name of the profile path ends in .man; for example, \\\\server\\share\\mandatoryprofile.man\\.

Super-mandatory user profiles are similar to normal mandatory profiles, with the exception that users who have super-mandatory profiles cannot log on when the server that stores the mandatory profile is unavailable. Users with normal mandatory profiles can log on with the locally cached copy of the mandatory profile.

Only system administrators can make changes to mandatory user profiles.

 

 



