---
title: Moving Existing Users to the Organizational Unit
description: When the enterprise administrator, Joe Worden, upgrades the Windows NT 4.0 domain to Active Directory, all users and groups are migrated to the Users containers in the Fabrikam domain.
ms.assetid: 230a594f-70c2-4ab6-a7e8-d5a77f2d6dd1
ms.tgt_platform: multiple
keywords:
- Moving Existing Users to the Organizational Unit AD
ms.topic: article
ms.date: 05/31/2018
---

# Moving Existing Users to the Organizational Unit

When the enterprise administrator, Joe Worden, upgrades the Windows NT 4.0 domain to Active Directory, all users and groups are migrated to the Users containers in the Fabrikam domain. Joe can now move those users and groups to the appropriate organizational units. An object can also be moved between related Windows 2000 domains using ADSI.

In the following code example, Joe moves "jeffsmith" to the Sales organization.


```VB
Set usr = salesOU.MoveHere("LDAP://CN=jeffsmith,CN=Users,DC=fabrikam,DC=com", vbNullString)
```



The [**IADsContainer.MoveHere**](/windows/desktop/api/Iads/nf-iads-iadscontainer-movehere) method takes the ADsPath of the object to be moved and the new object name (RDN). To keep the same name, you can specify **NULL** (**vbNullString**) for the *bstrNewName* parameter. To rename the object when it is moved, specify the new relative distinguished name for the *bstrNewName* parameter. For example, to move jeffsmith to the sales organization and rename the "jeffsmith" object to "jeff\_smith" in the same operation, Joe would execute the following code:


```VB
Set usr = salesOU.MoveHere("LDAP://CN=jeffsmith,CN=Users,DC=Fabrikam,DC=com", "CN=jeff_smith")
```



## Related topics

<dl> <dt>

[Creating New Users in the Organizational Unit](creating-new-users-in-the-organizational-unit.md)
</dt> </dl>

 

 




