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

To create an [*access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL) by using the low-level functions, allocate a buffer for the ACL and then initialize it by calling the [**InitializeAcl**](https://www.bing.com/search?q=**InitializeAcl**) function. To add [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) to the end of a [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL), use the [**AddAccessAllowedAce**](https://www.bing.com/search?q=**AddAccessAllowedAce**) and [**AddAccessDeniedAce**](https://www.bing.com/search?q=**AddAccessDeniedAce**) functions. The [**AddAuditAccessAce**](https://www.bing.com/search?q=**AddAuditAccessAce**) function adds an ACE to the end of a [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). You can use the [**AddAce**](https://www.bing.com/search?q=**AddAce**) function to add one or more ACEs at a specified position in an ACL. The **AddAce** function also allows you to add an inheritable ACE to an ACL. The [**DeleteAce**](https://www.bing.com/search?q=**DeleteAce**) function removes an ACE from a specified position in an ACL. The [**GetAce**](https://www.bing.com/search?q=**GetAce**) function retrieves an ACE from a specified position in an ACL. The [**FindFirstFreeAce**](https://www.bing.com/search?q=**FindFirstFreeAce**) function retrieves a pointer to the first free byte in an ACL.

To modify an existing ACL in an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly), use the [**GetSecurityDescriptorDacl**](https://www.bing.com/search?q=**GetSecurityDescriptorDacl**) or [**GetSecurityDescriptorSacl**](https://www.bing.com/search?q=**GetSecurityDescriptorSacl**) function to get the existing ACL. You can use the [**GetAce**](https://www.bing.com/search?q=**GetAce**) function to copy ACEs from the existing ACL. After allocating and initializing a new ACL, use functions such as [**AddAccessAllowedAce**](https://www.bing.com/search?q=**AddAccessAllowedAce**) and [**AddAce**](https://www.bing.com/search?q=**AddAce**) to add ACEs to it. When you have finished building the new ACL, use the [**SetSecurityDescriptorDacl**](https://www.bing.com/search?q=**SetSecurityDescriptorDacl**) or [**SetSecurityDescriptorSacl**](https://www.bing.com/search?q=**SetSecurityDescriptorSacl**) function to add the new ACL to the object's security descriptor.

You can use the [**AddAccessAllowedObjectAce**](https://www.bing.com/search?q=**AddAccessAllowedObjectAce**), [**AddAccessDeniedObjectAce**](https://www.bing.com/search?q=**AddAccessDeniedObjectAce**), or [**AddAuditAccessObjectAce**](https://www.bing.com/search?q=**AddAuditAccessObjectAce**) functions to add [object-specific ACEs](object-specific-aces.md) to the end of an ACL.

 

 



