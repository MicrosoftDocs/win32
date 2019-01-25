---
title: Creating an Organizational Unit
description: Now that you have the domain object, you can start creating organizational units.
ms.assetid: c9955b44-5ca1-4b4b-85c8-e0d55a4304ca
ms.tgt_platform: multiple
keywords:
- Creating an Organizational Unit ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Organizational Unit

Now that you have the domain object, you can start creating organizational units. Fabrikam has two divisions: Sales and Production. The company is planning to hire two Windows 2000 administrators to manage each division. Joe Worden, as the enterprise administrator, will create two new organizational units under the Fabrikam domain. By creating an organizational unit, Joe can group multiple objects together and let someone else manage these objects. The following code example creates the Sales Organizational Unit (OU).


```VB
Dim dom as IADsContainer
Set dom = GetObject("LDAP://DC=Fabrikam,DC=Com")
Set salesOrg = dom.Create("organizationalUnit", "OU=Sales")
salesOrg.Put "description", "Sales Headquarter,SF"
salesOrg.Put "wwwHomePage", "https://fabrikam.com/sales"
salesOrg.SetInfo
```



The [**IADsContainer.Create**](/windows/desktop/api/Iads/nf-iads-iadscontainer-create) method accepts the class name and the name of the new object. At this point the object is not committed to Active Directory. You, however, will have an ADSI/COM object reference on the client. With this ADSI object, you can set or modify attributes using the [**IADs.Put**](/windows/desktop/api/Iads/nf-iads-iads-put) method. The **IADs.Put** method accepts the attribute name and the value of the attribute. Still, nothing is committed to the directory; everything is cached at the client. When you call the [**IADs.SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) method, the changes, in this case, object creation and attribute modification, are committed to the directory. These changes are transacted, meaning that you will see either the new object with all attributes you set, or no object at all.

You can also nest organizational units. The following code example assumes that the Sales division is divided further into the East and West regions.


```VB
Set east = salesOrg.Create("organizationalUnit", "OU=East")
east.SetInfo
```



This also applies for the West region.

To bind directly to the East region in the Sales organization, specify the distinguished name.


```VB
Set east = GetObject("LDAP://OU=East,OU=Sales,DC=Fabrikam,DC=COM")
Debug.Print east.Get "description"
east.Put "wwwHomePage", "https://fabrikam.com/sales/east"
```



If you have already bound to the parent object (Sales), you can bind to the child object (East) from the parent object using the relative name of the child object.


```VB
Set east = salesOU.GetObject("organizationalUnit", "OU=East")
```



To ensure that the objects have been created, use the Active Directory Users and Computers MMC snap-in to view the new organizational units.

## Related topics

<dl> <dt>

[Moving Existing Users to the Organizational Unit](moving-existing-users-to-the-organizational-unit.md)
</dt> </dl>

 

 




