---
title: Setting Rights to Specific Properties of Specific Types of Objects
description: Property-specific permissions can be used in combination with object specific inheritance to provide the powerful and detailed delegation of administration.
ms.assetid: d2ebbe3a-78f7-4bb5-bac0-13236031b7b1
ms.tgt_platform: multiple
keywords:
- setting rights to specific properties of specific types of objects AD
- Active Directory, using, security, setting rights to specific properties
ms.topic: article
ms.date: 05/31/2018
---

# Setting Rights to Specific Properties of Specific Types of Objects

Property-specific permissions can be used in combination with object specific inheritance to provide the powerful and detailed delegation of administration. You can set a property-specific object-inheritable ACE to allow a specified user or group to read and/or write a specific attribute on a specified class of child objects in a container. For example, you can set an ACE on an organizational unit (OU) to enable a group to read and write the telephone number attribute of all user objects in the OU.

**To set property-specific object-inheritable ACEs**

1.  Set [**IADsAccessControlEntry.AceType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) to **ADS\_ACETYPE\_ACCESS\_ALLOWED\_OBJECT** or **ADS\_ACETYPE\_ACCESS\_DENIED\_OBJECT**.
2.  Set [**IADsAccessControlEntry.ObjectType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) to the **schemaIDGUID** of the attribute. For example, the **schemaIDGUID** of the **telephoneNumber** attribute is {bf967a49-0de6-11d0-a285-00aa003049e2}.
3.  Set [**IADsAccessControlEntry.AceFlags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) to **ADS\_ACEFLAG\_INHERIT\_ACE**.
4.  Set [**IADsAccessControlEntry.InheritedObjectType**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) to the **schemaIDGUID** of the object class that can inherit the ACE. For example, the **schemaIDGUID** of the **user** class is {bf967aba-0de6-11d0-a285-00aa003049e2}.
5.  Set [**IADsAccessControlEntry.Flags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) to **ADS\_FLAG\_OBJECT\_TYPE\_PRESENT** and **ADS\_FLAG\_INHERITED\_OBJECT\_TYPE\_PRESENT**.

> [!IMPORTANT]
> Set ADS\_ACEFLAG\_INHERIT\_ACE to cause the ACE to be inherited. In addition, set ADS\_ACEFLAG\_INHERIT\_ONLY\_ACE if the object type this ACE applies to does not match the object type of the container where the ACE is specified. If this is not done, the ACE will also become effective on the container and can grant unexpected rights.

 

For more information and code examples that can be used to set this kind of ACE, see [Example Code for Setting an ACE on a Directory Object](example-code-for-setting-an-ace-on-a-directory-object.md).

 

 