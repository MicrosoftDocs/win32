---
Description: Create an access control list (ACL) by using the low-level functions, allocate a buffer for the ACL and then initialize it by calling the InitializeAcl function.
ms.assetid: 9dcbbd4c-b3b3-43fd-b3a6-0637a53a455a
title: Low-level ACL and ACE Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Low-level ACL and ACE Functions

To create an [*access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL) by using the low-level functions, allocate a buffer for the ACL and then initialize it by calling the [**InitializeAcl**](https://msdn.microsoft.com/en-us/library/Aa378853(v=VS.85).aspx) function. To add [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) to the end of a [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL), use the [**AddAccessAllowedAce**](https://msdn.microsoft.com/en-us/library/Aa374947(v=VS.85).aspx) and [**AddAccessDeniedAce**](https://msdn.microsoft.com/en-us/library/Aa374962(v=VS.85).aspx) functions. The [**AddAuditAccessAce**](https://msdn.microsoft.com/en-us/library/Aa374973(v=VS.85).aspx) function adds an ACE to the end of a [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). You can use the [**AddAce**](https://msdn.microsoft.com/en-us/library/Aa374970(v=VS.85).aspx) function to add one or more ACEs at a specified position in an ACL. The **AddAce** function also allows you to add an inheritable ACE to an ACL. The [**DeleteAce**](https://msdn.microsoft.com/en-us/library/Aa446612(v=VS.85).aspx) function removes an ACE from a specified position in an ACL. The [**GetAce**](https://msdn.microsoft.com/en-us/library/Aa446634(v=VS.85).aspx) function retrieves an ACE from a specified position in an ACL. The [**FindFirstFreeAce**](https://msdn.microsoft.com/en-us/library/Aa446628(v=VS.85).aspx) function retrieves a pointer to the first free byte in an ACL.

To modify an existing ACL in an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly), use the [**GetSecurityDescriptorDacl**](https://msdn.microsoft.com/en-us/library/Aa446648(v=VS.85).aspx) or [**GetSecurityDescriptorSacl**](https://msdn.microsoft.com/en-us/library/Aa446653(v=VS.85).aspx) function to get the existing ACL. You can use the [**GetAce**](https://msdn.microsoft.com/en-us/library/Aa446634(v=VS.85).aspx) function to copy ACEs from the existing ACL. After allocating and initializing a new ACL, use functions such as [**AddAccessAllowedAce**](https://msdn.microsoft.com/en-us/library/Aa374947(v=VS.85).aspx) and [**AddAce**](https://msdn.microsoft.com/en-us/library/Aa374970(v=VS.85).aspx) to add ACEs to it. When you have finished building the new ACL, use the [**SetSecurityDescriptorDacl**](https://msdn.microsoft.com/en-us/library/Aa379583(v=VS.85).aspx) or [**SetSecurityDescriptorSacl**](https://msdn.microsoft.com/en-us/library/Aa379587(v=VS.85).aspx) function to add the new ACL to the object's security descriptor.

You can use the [**AddAccessAllowedObjectAce**](https://msdn.microsoft.com/en-us/library/Aa374956(v=VS.85).aspx), [**AddAccessDeniedObjectAce**](https://msdn.microsoft.com/en-us/library/Aa374966(v=VS.85).aspx), or [**AddAuditAccessObjectAce**](https://msdn.microsoft.com/en-us/library/Aa374982(v=VS.85).aspx) functions to add [object-specific ACEs](object-specific-aces.md) to the end of an ACL.

 

 



