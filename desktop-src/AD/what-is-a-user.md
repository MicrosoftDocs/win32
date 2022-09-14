---
title: What is a User
description: User accounts are created and stored as objects in Active Directory Domain Services.
ms.assetid: da13d21a-1d8b-4d03-8880-7146e6fc4ba9
ms.tgt_platform: multiple
keywords:
- What is a User Active Directory
- users Active Directory , what is a user
ms.topic: article
ms.date: 05/31/2018
---

# What is a User?

User accounts are created and stored as objects in Active Directory Domain Services. User accounts can be used by human users or programs such as system services use to log on to a computer. When a user logs on, the system verifies the user's password by comparing it with data stored in the user's user object in the Active Directory server. If the password is authenticated, that is, the password presented matches the password stored in the user object, the system produces an access token. An access token is an object that describes the security context of a process or thread. The data in a token includes the security identity and group memberships of the user account associated with the process or thread. Every process executed on behalf of this user has a copy of this access token.

Each user or application that accesses resources in a Windows domain must have an account in the Active Directory server. Windows uses this user account to verify that the user or application has permission to use a resource.

A user account can be used to:

-   Enable human users to log on to a computer and to access resources based on that user account's identity.
-   Enable programs and services to run under a specific security context.
-   Manage user access to shared resources such as objects and their properties, network shares, files, directories, printer queues, and so on.

Groups can contain members, which are references to users and other groups. Groups can also be used to control access to shared resources. When assigning permissions for resources, for example file shares, printers, and so on, administrators should assign those permissions to a group rather than to the individual users. The permissions are assigned once to the group, instead of several times to each individual user. This helps simplify the maintenance and administration of a network.

## Users compared to Contacts

Both users and contacts can be used to represent human users. However, a user is a security principal; a contact is not.

A user can be used to enable a human user to log on and access shared resources.

A contact is used only for distribution list and email purposes. However, a contact can contain most of the data stored in a user object such as address, phone numbers, and so on because both user and contact are derived from the person **classSchema** object. A contact has no security context; therefore, a contact cannot be used to control access to shared resources and cannot be used to log on to a computer.

## Users compared to Computers

The computer object class inherits from the user object class. A computer object represents a computer; however, the computer and the computer's local services often require access to the network and shared resources. When the computer accesses shared resources, not the user logged on to the computer, it needs an access token just as a human user logged on as a user does. When a computer accesses the network, it uses an access token that contains the security identifier for the computer's computer account and the groups that account is a member.

A service can run in the context of LocalSystem or a specific service account. On computers running Windows 2000, a service that runs in the context of the LocalSystem account uses the credentials of the computer.

 

 




