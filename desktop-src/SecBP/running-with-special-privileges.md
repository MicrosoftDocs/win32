---
description: Some functions require special privileges to run correctly.
ms.assetid: b25db548-d5ab-4276-9b50-36d030909384
title: Running with Special Privileges
ms.topic: article
ms.date: 05/31/2018
---

# Running with Special Privileges

Some functions require special [privileges](/windows/desktop/SecAuthZ/privileges) to run correctly. In some cases, the function can only be run by certain users or by members of certain groups. The most common requirement is that the user be a local administrator. Other functions require the user's account to have specific privileges enabled.

To reduce the possibility of unauthorized code being able to get control, the system should run with the least privilege necessary. Applications that need to call functions that require special privileges can leave the system open to attack by hackers. Such applications should be designed to run for short periods of time and should inform the user of the security implications involved.

For information about how to run as different users and how to enable privileges in your application, see the following topics:<dl>

[Running with Administrator Privileges](running-with-administrator-privileges.md)  
[Asking the User for Credentials](asking-the-user-for-credentials.md)  
[Changing Privileges in a Token](changing-privileges-in-a-token.md)  
[Assigning Privileges to an Account](assigning-privileges-to-an-account.md)  
</dl>

 

 
