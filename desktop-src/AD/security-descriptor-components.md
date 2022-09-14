---
title: Security Descriptor Components
description: Having used the IADs.Get method to retrieve an IADsSecurityDescriptor interface pointer, you can use the IADsSecurityDescriptor properties to read or write the components of a directory object's security descriptor.
ms.assetid: 35d3d16b-d7fc-4967-ba5c-5a77e058a9ae
ms.tgt_platform: multiple
keywords:
- Security Descriptor Components AD
ms.topic: article
ms.date: 05/31/2018
---

# Security Descriptor Components

Having used the [**IADs.Get**](/windows/desktop/api/iads/nf-iads-iads-get) method to retrieve an [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) interface pointer, you can use the **IADsSecurityDescriptor** properties to read or write the components of a directory object's security descriptor. For example, to get or set the object's DACL, use the [**DiscretionaryAcl**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) property.

A security descriptor can store the following data:

-   A security identifier (SID) that identifies the owner of the object: The owner of an object has the implicit right to modify the DACL and owner data in the object's security descriptor.
-   A discretionary access-control list (DACL) that identifies the users and groups who can perform various operations on the object: A DACL contains a list of access-control entries (ACEs). Each ACE allows or denies a specified set of access rights to a specified user account, group account, or other trustee. For more information, see [Retrieving an Object's DACL](retrieving-an-objectampaposs-dacl.md).
-   A system access-control list (SACL) that controls how the system audits attempts to access the object: Each ACE in a SACL specifies the types of access attempts that generate an audit log entry for a specified user account, group account, or other trustee. For more information, see [Retrieving an Object's SACL](retrieving-an-objectampaposs-sacl.md).
-   A set of **SECURITY\_DESCRIPTOR\_CONTROL** control flags that qualify the meaning of a security descriptor or its components: For example, the **SE\_DACL\_PROTECTED** flag protects the security descriptor's DACL from inheriting ACEs from its parent object.
-   A security identifier (SID) that identifies the primary group of the object: Active Directory Domain Services do not use this component.

For more information and a code example that can be used to read and display the data in an object security descriptor and DACL, see [Reading an Object's Security Descriptor](reading-an-objectampaposs-security-descriptor.md).

 

 