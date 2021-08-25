---
title: Control Access Rights (AD DS)
description: All objects in Active Directory Domain Services support a standard set of access rights defined in the ADS\_RIGHTS\_ENUM enumeration.
ms.assetid: 27ad74bd-ad87-422e-a4a2-02c0d51c4dd4
ms.tgt_platform: multiple
keywords:
- Control Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Control Access Rights (AD DS)

All objects in Active Directory Domain Services support a standard set of access rights defined in the [**ADS\_RIGHTS\_ENUM**](/windows/win32/api/iads/ne-iads-ads_rights_enum) enumeration. These access rights can be used in the Access Control Entries (ACEs) of an object's security descriptor to control access to the object; that is, to control who can perform standard operations, such as creating and deleting child objects, or reading and writing the object attributes. However, for some object classes, it may be desirable to control access in a way not supported by the standard access rights. To facilitate this, Active Directory Domain Services allow the standard access control mechanism to be extended through the **controlAccessRight** object.

Control access rights are used in three ways:

-   For extended rights, which are special operations not covered by the standard set of access rights. For example, the user class can be granted a "Send As" right that can be used by Exchange, Outlook, or any other mail application, to determine whether a particular user can have another user send mail on their behalf. Extended rights are created on **controlAccessRight** objects by setting the **validAccesses** attribute to equal the **ADS\_RIGHT\_DS\_CONTROL\_ACCESS** (256) access right.
-   For defining property sets, to enable controlling access to a subset of an object's attributes, rather than just to the individual attributes. Using the standard access rights, a single ACE can grant or deny access to all of an object's attributes or to a single attribute. Control access rights provide a way for a single ACE to control access to a set of attributes. For example, the user class supports the **Personal-Information** property set that includes attributes such as street address and telephone number. Property set rights are created on **controlAccessRight** objects by setting the **validAccesses** attribute to contain both the **ACTR\_DS\_READ\_PROP** (16) and the **ACTRL\_DS\_WRITE\_PROP** (32) access rights.
-   For validated writes, to require that the system perform value checking, or validation, beyond that which is required by the schema, before writing a value to an attribute on a DS object. This ensures that the value entered for the attribute conforms to required semantics, is within a legal range of values, or undergoes some other special checking that would not be performed for a simple low-level write to the attribute. A validated write is associated to a special permission that is distinct from the "Write &lt;attribute&gt;" permission that would allow any value to be written to the attribute with no value checking performed. The validated write is the only one of the three control access rights that cannot be created as a new control access right for an application. This is because the existing system cannot be programmatically modified to enforce validation. If a control access right was set up in the system as a validated write, the **validAccesses** attribute on the **controlAccessRight** objects will contain the **ADS\_RIGHT\_DS\_SELF** (8) access right.

    There are only three validated writes defined in the Windows 2000 Active Directory schema:

    -   Self-Membership permission on a Group object, which allows the caller's account, but no other account, to be added or removed from a group's membership.
    -   Validated-DNS-Host-Name permission on a Computer object, which allows a DNS host name attribute that is compliant with the computer name and domain name to be set.
    -   Validated-SPN permission on a Computer object, which allows an SPN attribute which is compliant with the DNS host name of the computer to be set.

For convenience, each control access right is represented by a **controlAccessRight** object in the Extended-Rights container of the Configuration partition, even though property sets and validated writes are not considered to be extended rights. Because the Configuration container is replicated across the entire forest, control rights are propagated across all domains in a forest. There are a number of predefined control access rights, and of course, custom access rights can also be defined.

All control access rights can be viewed as permissions in the ACL Editor.

For more information and a C++ and Visual Basic code example that sets an ACE to control read/write access to a property set, see [Example Code for Setting an ACE on a Directory Object](example-code-for-setting-an-ace-on-a-directory-object.md).

For more information about using control access rights to control access to special operations, see:

-   [Creating a Control Access Right](creating-a-control-access-right.md)
-   [Setting a Control Access Right ACE in an Object's ACL](setting-a-control-access-right-ace-in-an-objectampaposs-acl.md)
-   [Checking a Control Access Right in an Object's ACL](checking-a-control-access-right-in-an-objectampaposs-acl.md)
-   [Reading a Control Access Right Set in an Object's ACL](reading-a-control-access-right-set-in-an-objectampaposs-acl.md)

 

 
