---
title: Creating a New Group
description: Joe Worden, the enterprise administrator, must create a new group.
ms.assetid: a1bea695-d43f-47e6-af74-ba5abb0116a2
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Creating a New Group

Joe Worden, the enterprise administrator, must create a new group. He would like to secure some resources, such as file, Active Directory objects, or other objects, based on the membership of this group. The following code example shows how to create a new group.


```VB
Set ou = GetObject("LDAP://OU=Sales,DC=Fabrikam,DC=COM")
Set grp = ou.Create("group", "CN=Management")
grp.Put "samAccountName", "mgmt"
grp.Put "groupType", ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP Or ADS_GROUP_TYPE_SECURITY_ENABLED
grp.SetInfo
```



This group, Management, will be created in the Sales organizational unit. First, Joe must create an ADSI object for the Sales organizational unit. Second, he must set the [**samAccountName**](/windows/desktop/AD/group-objects) attribute on this object, because it is a mandatory attribute for backward compatibility. For this example, when **samAccountName** is set, Windows NT 4.0 tools such as User Manager see the attribute as **mgmt** instead of **Management**.

Third, Joe must specify the type of group. In a Windows 2000 domain, there are three types of groups: Global, Domain Local, and Universal. In addition, the group carries its security characteristic. A group can be either a security-enabled or a non-secured group. Essentially, security-enabled groups are those that can be granted or denied access rights to resources, similar to a user. Granting a group access to a file share, for example, implies that all members of the group can access the file share. Distribution lists cannot be used in a similar manner—you cannot, for example, grant a distribution list the right to access a file share. During the upgrade, Windows NT 4.0 groups are migrated as security-enabled groups. Non-secured groups in Active Directory are similar to distribution lists in Exchange. Hence, creating groups or distribution lists are similar operations in Windows 2000. In the Windows 2000 native mode (native mode means that all domain controllers in a domain are computers running Windows 2000 Server), the groups can be nested to any level.

## Related topics

<dl> <dt>

[Enumerating Objects](enumerating-objects.md)
</dt> </dl>

 

 