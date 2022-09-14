---
title: User Object Attributes
description: A user object has multiple attributes. This section documents key attributes used by Windows, administrative tools, and the Windows Address Book (WAB). It does not describe all attributes; many attributes are not used for the user object.
ms.assetid: c173c5d1-2680-4b9c-961d-251fba6e2c7c
ms.tgt_platform: multiple
keywords:
- User Object Attributes AD
- Users AD , User Object Attributes
- Objects AD , User, Attributes
ms.topic: article
ms.date: 09/02/2022
---

# User Object Attributes

A user object has multiple attributes. This section documents key attributes used by Windows, administrative tools, and the Windows Address Book (WAB). It does not describe all attributes; many attributes are not used for the user object.

Some attributes are stored in the directory, such as [**cn**](/windows/win32/ADSchema/a-cn), [**nTSecurityDescriptor**](/windows/win32/ADSchema/a-ntsecuritydescriptor), [**objectGUID**](/windows/win32/ADSchema/a-objectguid), and so on, and replicated to all domain controllers within a domain. A subset of these attributes is also replicated to the global catalog.

Non-replicated attributes are stored on each domain controller, but are not replicated elsewhere, such as [**badPwdCount**](/windows/win32/ADSchema/a-badpwdcount), [**lastLogon**](/windows/win32/ADSchema/a-lastlogon), [**lastLogoff**](/windows/win32/ADSchema/a-lastlogoff), and so on. The non-replicated attributes are attributes that pertain to a particular domain controller. For example, **lastLogon** is the last date and time that the user network logon was validated by the particular domain controller that is returning the property.

A user object also has constructed attributes that are not stored in the directory, but are calculated by the domain controller, such as [**canonicalName**](/windows/win32/ADSchema/a-canonicalname), [**distinguishedName**](/windows/win32/ADSchema/a-distinguishedname), [**allowedAttributes**](/windows/win32/ADSchema/a-allowedattributes), and so on.

## User object attributes

Attributes for user objects have the following classifications.

### Base object attributes

This category includes attributes required for all directory objects, such as [**objectClass**](/windows/win32/ADSchema/a-objectclass), [**nTSecurityDescriptor**](/windows/win32/ADSchema/a-ntsecuritydescriptor), and so on.

### Naming attributes

This category includes attributes used to refer to or identify the object, such as [**distinguishedName**](/windows/win32/ADSchema/a-distinguishedname), [**objectGUID**](/windows/win32/ADSchema/a-objectguid), [**objectSID**](/windows/win32/ADSchema/a-objectsid), and so on. For more information about naming attributes for user objects, see [User Naming Attributes](naming-properties.md).

### Security attributes

This category includes attributes for logon and access control. For more information about security attributes for user objects, see [User Security Attributes](security-properties.md).

### Address book attributes

This category includes attributes for email and user data. For more information about address book attributes for user objects, see [User Address Book Attributes](address-book-properties.md).

### Application-specific attributes

This category includes user-specific configuration data for specific applications.

## More attribute information

For more information about reading and modifying attributes for a user object, see [Reading and Writing Attributes of Objects in Active Directory Domain Services](reading-and-writing-attributes-of-objects-in-active-directory-domain-services.md).

For more information about the User class, including a complete list of the [**mayContain**](/windows/win32/ADSchema/a-maycontain) and [**mustContain**](/windows/win32/ADSchema/a-mustcontain) attributes of the class, see [**User**](/windows/win32/ADSchema/c-user).

## Setting passwords

The password for a user cannot be modified directly because this would involve sending an unencrypted password over the network. To set the password for a user, it is necessary to use the [**IADsUser.ChangePassword**](/windows/win32/api/iads/nf-iads-iadsuser-changepassword) or [**IADsUser.SetPassword**](/windows/win32/api/iads/nf-iads-iadsuser-setpassword) method. The `IADsUser.ChangePassword` method is used when the application is allowing the user to change their own password. The `IADsUser.SetPassword` method is used when the application enables an administrator to reset a password.
