---
description: Create an access control list (ACL) by using the low-level functions, allocate a buffer for the ACL and then initialize it by calling the InitializeAcl function.
ms.assetid: 9dcbbd4c-b3b3-43fd-b3a6-0637a53a455a
title: Low-level ACL and ACE Functions
ms.topic: article
ms.date: 05/31/2018
---

# Low-level ACL and ACE Functions

To create an [*access control list*](/windows/desktop/SecGloss/a-gly) (ACL) by using the low-level functions, allocate a buffer for the ACL and then initialize it by calling the [**InitializeAcl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-initializeacl) function. To add [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) to the end of a [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL), use the [**AddAccessAllowedAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addaccessallowedace) and [**AddAccessDeniedAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addaccessdeniedace) functions. The [**AddAuditAccessAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addauditaccessace) function adds an ACE to the end of a [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL). You can use the [**AddAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addace) function to add one or more ACEs at a specified position in an ACL. The **AddAce** function also allows you to add an inheritable ACE to an ACL. The [**DeleteAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-deleteace) function removes an ACE from a specified position in an ACL. The [**GetAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getace) function retrieves an ACE from a specified position in an ACL. The [**FindFirstFreeAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-findfirstfreeace) function retrieves a pointer to the first free byte in an ACL.

To modify an existing ACL in an object's [*security descriptor*](/windows/desktop/SecGloss/s-gly), use the [**GetSecurityDescriptorDacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptordacl) or [**GetSecurityDescriptorSacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorsacl) function to get the existing ACL. You can use the [**GetAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getace) function to copy ACEs from the existing ACL. After allocating and initializing a new ACL, use functions such as [**AddAccessAllowedAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addaccessallowedace) and [**AddAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addace) to add ACEs to it. When you have finished building the new ACL, use the [**SetSecurityDescriptorDacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptordacl) or [**SetSecurityDescriptorSacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorsacl) function to add the new ACL to the object's security descriptor.

You can use the [**AddAccessAllowedObjectAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addaccessallowedobjectace), [**AddAccessDeniedObjectAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addaccessdeniedobjectace), or [**AddAuditAccessObjectAce**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addauditaccessobjectace) functions to add [object-specific ACEs](object-specific-aces.md) to the end of an ACL.

 

 
