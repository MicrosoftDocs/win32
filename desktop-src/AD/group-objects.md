---
title: Group Objects
description: A group is represented as a group object in Active Directory Domain Services.
ms.assetid: 2dd5a293-047a-4639-9c95-7074578952be
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Group Objects

A group is represented as a [**group**](/windows/desktop/ADSchema/c-group) object in Active Directory Domain Services. The following table lists important attributes of the **group** object.




| Attribute | Description | 
|-----------|-------------|
| <strong>cn</strong> | The <strong>cn</strong> (or Common-Name) is a single-value attribute that is the object's relative distinguished name. The <strong>cn</strong> is the name of the group in Active Directory Domain Services. As with all other objects, the <strong>cn</strong> of a group must be unique among the sibling objects in the container that contains the group.<br /> | 
| <strong>member</strong> | The <strong>member</strong> attribute is a multi-value attribute that contains the list of distinguished names for the user, group, and contact objects that are members of the group. Each item in the list is a linked reference to the object that represents the member; therefore, the Active Directory server automatically updates the distinguished names in the member property when a member object is moved or renamed.<br /> | 
| <strong>groupType</strong> | The <strong>groupType</strong> attribute is a single-value attribute that is an integer that specifies the group type and scope using the following bit flags:<ul><li><strong>ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP</strong></li><li><strong>ADS_GROUP_TYPE_GLOBAL_GROUP</strong></li><li><strong>ADS_GROUP_TYPE_UNIVERSAL_GROUP</strong></li><li><strong>ADS_GROUP_TYPE_SECURITY_ENABLED</strong></li></ul><br /> The first three flags specify the group scope. The <strong>ADS_GROUP_TYPE_SECURITY_ENABLED</strong> flag indicates the group type. If this flag is set, the group is a security group. If this flag is not set, the group is a distribution group. For more information, see <a href="#group-types">Group Types</a>.<br /> | 
| <strong>memberOf</strong> | The <strong>memberOf</strong> attribute is a multiple-value attribute that contains the list of distinguished names for groups that contain the group as a member. This attribute lists the groups beneath which the group is directly nested it does not contain the recursive list of nested predecessors. For example, if group D were nested in group C and group B and group B were nested in group A, the <strong>memberOf</strong> attribute of group D would list group C and group B, but not group A.<br /> | 
| <strong>objectGUID</strong> | The <strong>objectGUID</strong> attribute is a single-value attribute that is the unique identifier for the object. This attribute is a Globally Unique Identifier (GUID). When an object is created in the directory, the Active Directory server generates a GUID and assigns it to the object's <strong>objectGUID</strong> attribute. The GUID is unique across the enterprise and anywhere else.<br /> The <strong>objectGUID</strong> is a 128-bit GUID structure stored as an OctetString.<br /> | 
| <strong>objectSid</strong> | The <strong>objectSid</strong> attribute is a single-value attribute that specifies the security identifier (SID) of the group. The SID is a unique value used to identify the group as a security principal. It is a binary value that the system sets when the group is created.<br /> Each group has a unique SID that the Windows NT/Windows 2000 Server domain issues that is stored in the <strong>objectSid</strong> attribute of the group object in the directory. Each time a user logs on, the system retrieves the SID for the groups of which the user is a member and places it in the user's access token. The system uses the SIDs in the user's access token to identify the user and his/her group memberships in all subsequent interactions with Windows NT/Windows 2000 security.<br /> When an SID has been used as the unique identifier for a user or group, it cannot ever be used again to identify another user or group.<br /> | 
| <strong>sAMAccountName</strong> | The <strong>sAMAccountName</strong> attribute is a single-value attribute that is the logon name used to support clients and servers from a previous version (Windows 95, Windows 98, and LAN Manager). The <strong>sAMAccountName</strong> should be less than 20 characters to support clients and servers from a previous version.<br /> The <strong>sAMAccountName</strong> must be unique among all security principal objects within a domain.<br /> | 




 

## Group Types

There are two types of groups defined by Active Directory Domain Services, *Security Groups* and *Distribution Groups*.

A security group provides a logical grouping of objects and the group itself can be used as a security principal in an Access Control List (ACL). When a security group is given access to an object, all members of the security group automatically receive the same access to the object. Security groups with Universal scope can also be used as an email entity. Sending an email message to a universal security group sends the message to all the members of the group.

A distribution group also provides a logical grouping of objects, but cannot provide any access privileges. Distribution groups are not security enabled and cannot be used as a security principal in an ACL. Distribution groups are only used for grouping purposes. For example, distribution lists can be used with email applications, such as Exchange, to send email to a collection of users.

For more information about group types in Active Directory Domain Services, see the [Group types](/previous-versions/windows/it-pro/windows-server-2003/cc781446(v=ws.10)) topic on [Microsoft TechNet](https://technet.microsoft.com/default.aspx).

## Group Scope

There are three group scopes that are defined by Active Directory Domain Services, *Universal*, *Global* and *Domain Local*. The scope of the group defines what types of object can belong to the group, what types of groups the group can be a member of and the scope of objects that security groups can be given access to. When the domain functional level is set to Windows 2000 mixed mode, security groups with universal scope cannot be created.

The following table lists the three group scopes and more information about each scope for a security group.

| Scope                   | Possible members                                                                                                                                                                                                                                      | Scope conversion                                                                                                                                                 | Can grant permissions                                                       | Possible member of                                                                                                                                                                                                  |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Universal<br/>    | Accounts from any domain in the same forest.<br/> Global groups from any domain in the same forest.<br/> Other universal groups from any domain in the same forest.<br/>                                                            | Can be converted to domain local scope.<br/> Can be converted to global scope as long as the group does not contain any other universal groups.<br/> | On any domain in the same forest or trusting forests.<br/>            | Other universal groups in the same forest.<br/> Domain local groups in the same forest or trusting forests.<br/> Local groups on machines in the same forest or trusting forests.<br/>            |
| Global<br/>       | Accounts from the same domain.<br/> Other global groups from the same domain.<br/>                                                                                                                                                        | Can be converted to universal scope as long as the group is not a member of any other global group.<br/>                                                   | On any domain in the same forest or trusting domains or forests.<br/> | Universal groups from any domain in the same forest.<br/> Other global groups from the same domain.<br/> Domain local groups from any domain in the same forest or from any trusting domain.<br/> |
| Domain Local<br/> | Accounts from any domain or any trusted domain.<br/> Global groups from any domain or any trusted domain.<br/> Universal groups from any domain in the same forest.<br/> Other domain local groups from the same domain.<br/> | Can be converted to universal scope as long as the group does not contain any other domain local groups.<br/>                                              | Within the same domain.<br/>                                          | Other domain local groups from the same domain.<br/> Local groups on machines in the same domain, excluding built-in groups that have well-known SIDs.<br/>                                             |



 

 

