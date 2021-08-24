---
title: Adding Domain Objects to Local Groups
description: The users and groups that belong to the domain can be added to groups on the local computer to grant rights to the domain user or group on that particular computer.
ms.assetid: 07287190-88a1-4d4d-a91c-1e95d9903a4d
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , adding domain objects to local groups
ms.topic: article
ms.date: 05/31/2018
---

# Adding Domain Objects to Local Groups

When a member server or a computer running on Windows 2000 Professional is a member of a Windows 2000 domain, the users and groups that belong to the domain can be added to groups on the local computer to grant rights to the domain user or group on that particular computer.

When managing domain local groups on a Windows 2000 domain using ADSI, the LDAP provider is normally used. When managing local groups on member servers and a computer running Windows 2000 Professional, however, the WinNT provider must be used.

Only local groups can be created on member servers and Windows 2000 Professional. However, the local groups can contain:

-   Universal and global groups from the forest that contains the domain that the computer is a member.
-   Domain local groups from that computer domain.
-   Users from any domain in the forest.

**To add a domain object to a local group**

1.  Bind to the [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) interface of the computer that contains the local group to add a member to. The binding must be performed using an account that has sufficient rights to access that computer. The binding string must take the form "WinNT://<computer name>,computer" where "&lt;computer name&gt;" is the name of the computer group to add a member to. The ",computer" parameter instructs ADSI that it is binding to a computer. ADSI exposes this data to the WinNT provider's parser so that it can skip some ambiguity-resolution queries to determine what type of object you are binding to. This can save the user a 5 to 20 second wait for the ambiguity to be resolved.
2.  Use the [**IADsContainer.GetObject**](/windows/desktop/api/iads/nf-iads-iadscontainer-getobject) method with "group" as the class and the local group name as the name of the object to bind to the group.
3.  Bind to the [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup) interface of the local group to which a member will be added.
4.  Construct the ADsPath of the object to add to the local group in the form "WinNT://&lt;domain&gt;/&lt;name&gt;", where "&lt;domain&gt;" is the name of the domain that contains the object to add and "&lt;name&gt;" is the name of the object to add.
5.  Add the user or group to the local group with the [**IADsGroup.Add**](/windows/desktop/api/iads/nf-iads-iadsgroup-add) method, passing the ADsPath constructed in Step 4.

For more information and a code example that shows how to add a domain user or group object to a local group, see [Example Code for Adding a Domain User or Group to a Local Group](example-code-for-adding-a-domain-user-or-group-to-a-local-group.md).

 

 
