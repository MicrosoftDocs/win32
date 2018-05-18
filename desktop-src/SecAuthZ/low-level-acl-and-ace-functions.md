---
Description: 'Create an access control list (ACL) by using the low-level functions, allocate a buffer for the ACL and then initialize it by calling the InitializeAcl function.'
ms.assetid: '9dcbbd4c-b3b3-43fd-b3a6-0637a53a455a'
title: 'Low-level ACL and ACE Functions'
---

# Low-level ACL and ACE Functions

To create an [*access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL) by using the low-level functions, allocate a buffer for the ACL and then initialize it by calling the [**InitializeAcl**](initializeacl.md) function. To add [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) to the end of a [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL), use the [**AddAccessAllowedAce**](addaccessallowedace.md) and [**AddAccessDeniedAce**](addaccessdeniedace.md) functions. The [**AddAuditAccessAce**](addauditaccessace.md) function adds an ACE to the end of a [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). You can use the [**AddAce**](addace.md) function to add one or more ACEs at a specified position in an ACL. The **AddAce** function also allows you to add an inheritable ACE to an ACL. The [**DeleteAce**](deleteace.md) function removes an ACE from a specified position in an ACL. The [**GetAce**](getace.md) function retrieves an ACE from a specified position in an ACL. The [**FindFirstFreeAce**](findfirstfreeace.md) function retrieves a pointer to the first free byte in an ACL.

To modify an existing ACL in an object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly), use the [**GetSecurityDescriptorDacl**](getsecuritydescriptordacl.md) or [**GetSecurityDescriptorSacl**](getsecuritydescriptorsacl.md) function to get the existing ACL. You can use the [**GetAce**](getace.md) function to copy ACEs from the existing ACL. After allocating and initializing a new ACL, use functions such as [**AddAccessAllowedAce**](addaccessallowedace.md) and [**AddAce**](addace.md) to add ACEs to it. When you have finished building the new ACL, use the [**SetSecurityDescriptorDacl**](setsecuritydescriptordacl.md) or [**SetSecurityDescriptorSacl**](setsecuritydescriptorsacl.md) function to add the new ACL to the object's security descriptor.

You can use the [**AddAccessAllowedObjectAce**](addaccessallowedobjectace.md), [**AddAccessDeniedObjectAce**](addaccessdeniedobjectace.md), or [**AddAuditAccessObjectAce**](addauditaccessobjectace.md) functions to add [object-specific ACEs](object-specific-aces.md) to the end of an ACL.

 

 



