---
Description: 'Use the GetSecurityInfo and GetNamedSecurityInfo functions to retrieve a pointer to an object's security descriptor.'
ms.assetid: '834f1b58-d403-4899-865e-5721a37587e9'
title: Security Descriptor Operations
---

# Security Descriptor Operations

The Windows API provides functions for getting and setting the components of the [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) associated with a securable object. Use the [**GetSecurityInfo**](getsecurityinfo.md) and [**GetNamedSecurityInfo**](getnamedsecurityinfo.md) functions to retrieve a pointer to an object's security descriptor. These functions can also retrieve pointers to the individual components of the security descriptor: DACL, SACL, owner SID, and primary group SID. Use the [**SetSecurityInfo**](setsecurityinfo.md) and [**SetNamedSecurityInfo**](setnamedsecurityinfo.md) functions to set the components of an object's security descriptor.

In general, you should use [**GetSecurityInfo**](getsecurityinfo.md) and [**SetSecurityInfo**](setsecurityinfo.md) with objects identified by a handle, and [**SetNamedSecurityInfo**](setnamedsecurityinfo.md) and [**GetNamedSecurityInfo**](getnamedsecurityinfo.md) with objects identified by a name. For more information about the specific functions to use when working with the various types of objects, see [Securable Objects](securable-objects.md).

The Windows API provides additional functions for manipulating the components of a security descriptor. For information about working with access control lists (DACLs or SACLs), see [Getting Information from an ACL](getting-information-from-an-acl.md) and [Creating or Modifying an ACL](creating-or-modifying-an-acl.md). For information about SIDs, see [Security Identifiers](security-identifiers.md) (SIDs).

To get the control information in a security descriptor, call the [**GetSecurityDescriptorControl**](getsecuritydescriptorcontrol.md) function. To set the control bits that relate to automatic ACE inheritance, call the [**SetSecurityDescriptorControl**](setsecuritydescriptorcontrol.md) function. Other control bits are set by the various functions that set a security descriptor component. For example, if you use [**SetSecurityInfo**](setsecurityinfo.md) to change an object's DACL, the function sets or clears the bits as appropriate to indicate whether the security descriptor has a DACL, whether it is a default DACL, and so on. Another example is the [*resource manager*](https://msdn.microsoft.com/library/windows/desktop/ms721604#-security-resource-manager-gly) (RM) control bits contained in the security descriptor. These bits are used according to the implementation of the resource manager, and are accessed through the [**GetSecurityDescriptorRMControl**](getsecuritydescriptorrmcontrol.md) and [**SetSecurityDescriptorRMControl**](setsecuritydescriptorrmcontrol.md) functions.

 

 



