---
title: How Security Descriptors are Set on New Directory Objects
description: When you create a new object in Active Directory Domain Services, you can explicitly create a security descriptor and then set that security descriptor as the object's nTSecurityDescriptor property.
ms.assetid: 07c367f8-cb5a-49ef-8e13-d31673c2ceee
ms.tgt_platform: multiple
keywords:
- objects AD ,how security descriptors are set on new directory objects
- security descriptors AD ,how to set on new directory objects
ms.topic: article
ms.date: 05/31/2018
---

# How Security Descriptors are Set on New Directory Objects

When you create a new object in Active Directory Domain Services, you can explicitly create a security descriptor and then set that security descriptor as the object's **nTSecurityDescriptor** property. For more information, see [Creating a Security Descriptor for a New Directory Object](creating-a-security-descriptor-for-a-new-directory-object.md).

Active Directory Domain Services use the following rules to set the DACL in the new object's security descriptor:

-   If you explicitly specify a security descriptor when you create the object, the system merges any inheritable ACEs from the parent object into the specified DACL unless the **SE\_DACL\_PROTECTED** bit is set in the security descriptor's control bits.
-   If you do not specify a security descriptor, the system builds the object's DACL by merging any inheritable ACEs from the parent object into the default DACL from the **classSchema** object for the object's class.
-   If the schema does not have a default DACL, the object's DACL is the default DACL from the primary or impersonation token of the creator.
-   If there is no specified, inherited, or default DACL, the system creates the object with no DACL, which allows everyone full access to the object.

The system uses a similar algorithm to build a SACL for a directory service object.

The owner and primary group in the new object's security descriptor are set to the values you specify in the **nTSecurityDescriptor** property when you create the object. If you do not set these values, Active Directory Domain Services use the rules listed in the following table to set them.



| Rule          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Owner         | The owner in a default security descriptor is set to the default owner SID from the primary or impersonation token of the creating process. For most users, the default owner SID is the same as the SID that identifies the user's account. Be aware that for users who are members of the built-in administrators group, the system automatically sets the default owner SID in the access token to the administrators group; therefore, objects created by a member of the administrators group are typically owned by the administrators group. To get or set the default owner in an access token, call the [**GetTokenInformation**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) or [**SetTokenInformation**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-settokeninformation) function with the [**TOKEN\_OWNER**](/windows/desktop/api/winnt/ns-winnt-token_owner) structure. |
| Primary Group | The primary group in a default security descriptor is set to the default primary group from the creator's primary or impersonation token. Be aware that primary group is not used in the context of Active Directory Domain Services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |



 

For more information about ACE inheritance, see [Inheritance and Delegation of Administration](inheritance-and-delegation-of-administration.md).

For more information about the default security descriptors in the schema, see [Default Security Descriptor](default-security-descriptor.md).

For more information about **classSchema** objects, see [Active Directory Schema](active-directory-schema.md).

 

 