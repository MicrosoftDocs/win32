---
title: Creating a User
description: To create a user in Active Directory Domain Services, create a user object in the domain container of the domain where you want to place the user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fb51895f-71e1-45b6-b8bc-ed674e822734
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , creating a user
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a User

To create a user in Active Directory Domain Services, create a user object in the domain container of the domain where you want to place the user. Users can be created at the root of the domain, within an organizational unit, or within a container.

When you create a user object, you must also set the attributes, listed in the following table, to set the object as a legal user that is recognized by Active Directory Domain Services and the Windows Security system.



| Attribute                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**cn**](https://msdn.microsoft.com/library/ms675449)                         | Specifies the name of the user object in the directory. This will be the object's relative distinguished name (RDN).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**sAMAccountName**](https://msdn.microsoft.com/library/ms679635) | Specifies a string that is the name used to support clients and servers from a previous version of Windows. The [**sAMAccountName**](https://msdn.microsoft.com/library/ms679635) should be less than 20 characters to support clients from a previous version of Windows.<br/> The [**sAMAccountName**](https://msdn.microsoft.com/library/ms679635) must be unique among all security principal objects within the domain. You should perform a query against the domain to verify that the **sAMAccountName** is unique within the domain.<br/> [**sAMAccountName**](https://msdn.microsoft.com/library/ms679635) is an optional attribute. The server will create a random **sAMAccountName** value if none is specified.<br/> |



 

You can also set other attributes. The following user attributes are set with default values if you do not explicitly set them at creation time.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/ms675098"><strong>accountExpires</strong></a></td>
<td>Specifies when the account will expire. The default is <strong>TIMEQ_FOREVER</strong>, which indicates that the account will never expire.<br/></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/ms679006"><strong>nTSecurityDescriptor</strong></a></td>
<td>A security descriptor is created based on specific rules. For more information, see <a href="how-security-descriptors-are-set-on-new-directory-objects">How Security Descriptors are Set on New Directory Objects</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/ms679011"><strong>objectCategory</strong></a></td>
<td>Specifies the user category. The default is &quot;Person&quot;.<br/></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/ms678697"><strong>name</strong></a></td>
<td>Specifies the user name. The default is the value set for <a href="https://msdn.microsoft.com/library/ms675449"><strong>cn</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/ms679430"><strong>pwdLastSet</strong></a></td>
<td>Specifies when the user last set the password. The default is zero, which indicates that the user must change the password at next logon.<br/></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/ms680832"><strong>userAccountControl</strong></a></td>
<td>Contains values that determine several logon and account features for the user.<br/> By default, the following flags are set:<br/>
<ul>
<li><strong>UF_ACCOUNTDISABLE</strong> - The account is disabled.</li>
<li><strong>UF_PASSWD_NOTREQD</strong> - No password is required.</li>
<li><strong>UF_NORMAL_ACCOUNT</strong> - Default account type that represents a typical user.</li>
</ul></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/ms677099"><strong>memberOf</strong></a></td>
<td>Specifies the group or groups that the user is a direct member of. The default is &quot;Domain Users&quot;.<br/></td>
</tr>
</tbody>
</table>



 

A user is created by binding to the desired container and then using one of the following methods. The [**cn**](https://msdn.microsoft.com/library/ms675449) and [**sAMAccountName**](https://msdn.microsoft.com/library/ms679635) attributes must be set before the user is committed to the server.



| Method                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IADsContainer.Create**](https://msdn.microsoft.com/library/aa705987)                        | The [**cn**](https://msdn.microsoft.com/library/ms675449) attribute is taken from the *bstrRelativeName* parameter. The new user must be committed by calling [**IADs.SetInfo**](https://msdn.microsoft.com/library/aa746354) or the object will not be created. For more information, see [Example Code for Creating a User](example-code-for-creating-a-user.md).<br/>                                                                                            |
| [**IDirectoryObject::CreateDSObject**](https://msdn.microsoft.com/library/aa746356) | The [**cn**](https://msdn.microsoft.com/library/ms675449) attribute is taken from the *pszRDNName* parameter. The new user is committed when [**CreateDSObject**](https://msdn.microsoft.com/library/aa746356) is called. For more information, see [Example Code for Creating a User](example-code-for-creating-a-user.md).<br/>                                                                                                                |
| [DirectoryEntries.Add](http://go.microsoft.com/fwlink/p/?linkid=83864)       | The [**cn**](https://msdn.microsoft.com/library/ms675449) attribute is taken from the *name* parameter. The new user object must be committed by calling [DirectoryEntry.CommitChanges](https://msdn.microsoft.com/library/system.directoryservices.directoryentry.commitchanges.aspx) or the object will not be created. For more information, see [Adding Directory Objects](http://go.microsoft.com/fwlink/p/?linkid=83965).<br/> |



 

The new user must be committed to the server before any attributes other than [**cn**](https://msdn.microsoft.com/library/ms675449) and [**sAMAccountName**](https://msdn.microsoft.com/library/ms679635) can be modified. This is because the user account does not actually exist until the user is committed. If an attribute is retrieved or modified for an object that does not exist on the server, an error will occur. This includes calling the [**IADsUser.SetPassword**](https://msdn.microsoft.com/library/aa746344) method. For example, the following sequence would be followed when creating a user with [**IADsContainer.Create**](https://msdn.microsoft.com/library/aa705987):

1.  Call [**IADsContainer.Create**](https://msdn.microsoft.com/library/aa705987) to create the user in the local cache with the specified [**cn**](https://msdn.microsoft.com/library/ms675449).
2.  Set the [**sAMAccountName**](https://msdn.microsoft.com/library/ms679635) attribute to the desired value with the [**IADs.Put**](https://msdn.microsoft.com/library/aa746352) method.
3.  Now modify other attributes, such as [**userAccountControl**](https://msdn.microsoft.com/library/ms680832). This restriction also applies to the ADSI properties, such as [**IADsUser.AccountDisabled**](https://msdn.microsoft.com/library/aa746343), and methods such as [**IADsUser.SetPassword**](https://msdn.microsoft.com/library/aa746344).
4.  Call [**IADs.SetInfo**](https://msdn.microsoft.com/library/aa746354) to commit the new user to the server.

When a new user account is created, it is disabled by default. The account must be enabled manually or programmatically. To programmatically enable a user account, remove the **ADS\_UF\_ACCOUNTDISABLE** flag from the [**userAccountControl**](https://msdn.microsoft.com/library/ms680832) attribute.

When a new user account is created, the [**userAccountControl**](https://msdn.microsoft.com/library/ms680832) attribute for the account automatically has the **UF\_PASSWD\_NOTREQD** flag set, which indicates that no password is required for the account. If the security policies of the domain that the account is created in requires a password for all user accounts, then the **UF\_PASSWD\_NOTREQD** flag must be removed from the **userAccountControl** attribute for the account.

## Related topics

<dl> <dt>

[Example Code for Creating a User](example-code-for-creating-a-user.md)
</dt> </dl>

 

 





