---
title: Creating New Users in the Organizational Unit
description: Terry Adams was hired into the Fabrikam Sales organization. His direct report is Patrick Hines.
ms.assetid: bc31ed04-e505-4d64-9fa3-d06af7351db0
ms.tgt_platform: multiple
keywords:
- Creating New Users in the Organizational Unit ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Creating New Users in the Organizational Unit

Terry Adams was hired into the Fabrikam Sales organization. His direct report is Patrick Hines.

As shown in the following code example, Joe Andreshak, the enterprise administrator, will create a new account for him.


```VB
Dim salesOU as IADsContainer
Set salesOU = GetObject("LDAP://OU=Sales,DC=Fabrikam,DC=COM")
Set usr = salesOU.Create("user", "CN=Terry Adams")
usr.Put "sAMAccountName", "terryadams"
usr.Put "userPrincipalName", "terryadams@fabrikam.com" 
usr.Put "title" "Marketing Manager"
usr.SetInfo

usr.SetPassword "seahorse"
usr.AccountDisabled = False
usr.SetInfo
```



When creating a new user, you must specify a **sAMAccountName**. This is a mandatory attribute for the user class. Before an instance of an object can be created, all mandatory attributes must be set. The **sAMAccountName** will automatically be generated if one is not specified for a new user.

When creating a new user, all of the required attributes must be set in the local cache before the [**IADs.SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) method is called.

Joe, as an administrator, can assign Terry's password using the [**IADsUser.SetPassword**](/windows/desktop/api/Iads/nf-iads-iadsuser-setpassword) method. The **IADsUser.SetPassword** method will not work until the [**IADs.SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) method has been called.

Then, Joe enables the user account by setting the [**IADsUser.AccountDisabled**](iadsuser-property-methods.md) property to **FALSE**.

The following code example shows how to set Terry as Patrick's manager.


```VB
Set usr = GetObject("LDAP://CN=patrickhines,OU=Sales,DC=Fabrikam,DC=COM")
usr.Put "manager", "CN=Terry Adams,OU=Sales,DC=Fabrikam,DC=COM"
usr.SetInfo
```



You may wonder what happens if Terry changes his name, moves to a different organization, or leaves the company. Who maintains this manager-direct report link? For more information, and the solution to this problem, see [Reorganization](reorganization.md). Because the Active Directory schema is extensible, you can model your objects to include similar manager-direct report style relationships.

Before going on to the next task, look at a code example that shows how Joe would view Terry's direct reports.


```VB
Set usr = GetObject("LDAP://CN=Terry Adams,OU=Sales,DC=Fabrikam,DC=COM")
reports = usr.GetEx ("directReports")

For each directReport in reports
    Debug.Print directReport
Next
```



In this code example, Patrick will display as Terry's direct report, even though the **directReports** attribute was never modified. Active Directory does this automatically.

In the directory world, an attribute can have single or multiple values. Because **directReports** has multiple values, you can get this information by looking at the schema, it is easier to use the [**IADs.GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) method, which returns an array of values regardless of whether single or multiple values are returned.

The Active Directory Users and Computers snap-in lets you view direct reports and manager relationships on the user's property page.

## Related topics

<dl> <dt>

[Adding Users to a Group](adding-users-to-a-group.md)
</dt> </dl>

 

 




