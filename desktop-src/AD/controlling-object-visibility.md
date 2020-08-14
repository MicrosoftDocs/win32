---
title: Controlling Object Visibility
description: Active Directory Domain Services provide the ability to hide objects from users who have been denied certain rights.
ms.assetid: 3a65ec79-7de0-4d14-b980-1ca6a972ac70
ms.tgt_platform: multiple
keywords:
- controlling object visibility Active Directory
- Active Directory Active Directory , using, controlling object visibility
ms.topic: article
ms.date: 05/31/2018
---

# Controlling Object Visibility

Active Directory Domain Services provide the ability to hide objects from users who have been denied certain rights. If an object is hidden, an application that is running with a user's credentials will not be able to enumerate or bind to the object.

If a user is granted the [**ADS\_RIGHT\_ACTRL\_DS\_LIST**](/windows/win32/api/iads/ne-iads-ads_rights_enum) access control right on a container, the user can view any of the child objects of the container. Likewise, if a user is denied the **ADS\_RIGHT\_ACTRL\_DS\_LIST** access control right on a container, the user cannot view any of the child objects of the container. This allows the contents of entire containers to be hidden.

The Active Directory server can also be put into a special list object mode by setting the third character of the [**dSHeuristics**](/windows/desktop/ADSchema/a-dsheuristics) property to "1". The list object mode can be disabled by setting the third character of the **dSHeuristics** property to "0". When the Active Directory server is in the list object mode, an object will still be visible if the user has been granted the [**ADS\_RIGHT\_ACTRL\_DS\_LIST**](/windows/win32/api/iads/ne-iads-ads_rights_enum) right on the parent object. If, however, the user has been denied the **ADS\_RIGHT\_ACTRL\_DS\_LIST** right on the parent, specific child objects can still be made visible if the user is granted the **ADS\_RIGHT\_DS\_LIST\_OBJECT** right on both the parent and child objects. The list object mode allows the system administrator to grant or deny access to individual objects for users or groups. The list object mode should be used sparingly because it requires a significantly higher number of access check calls to be made by the directory service to determine if an object is visible to a user. Thus it can have a negative effect on the performance of browsing or reading objects from Active Directory Domain Services.

 

 