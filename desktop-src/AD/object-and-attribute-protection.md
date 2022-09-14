---
title: Object and Attribute Protection
description: An access-control list (ACL) protects all objects in Active Directory Domain Services.
ms.assetid: 64ac1f88-57d6-4821-bd17-f7ef1004922c
ms.tgt_platform: multiple
keywords:
- Object and Attribute Protection
- security AD , object and attribute protection
ms.topic: article
ms.date: 05/31/2018
---

# Object and Attribute Protection

An access-control list (ACL) protects all objects in Active Directory Domain Services. ACLs determine who can view the object, what attributes they can read, and what actions each user can perform on the object. The existence of an object or an attribute is never revealed to an unauthorized user.

An ACL is a list of access-control entries (ACEs) stored with the object that it protects. In Windows NT and Windows 2000, an ACL is stored as a binary value, called a security descriptor. Each ACE contains a security identifier (SID), which identifies the principal (user or group) to whom the ACE applies, and data about what type of access the ACE grants or denies.

ACLs for directory objects contain ACEs that apply to the object as a whole and ACEs that apply to the individual attributes of the object. This allows an administrator to control not only which users can see an object, but also what properties those users can view. For example, all users might be granted read access to the email and telephone number attributes for all other users, but security properties of users might be denied to all but members of a special security administrators group. Individual users might be granted write access to personal attributes such as the telephone and mailing addresses on their own user objects.

 

 




