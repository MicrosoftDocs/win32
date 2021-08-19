---
title: Creating a User
description: To create a user in Active Directory Domain Services, create a user object in the domain container of the domain where you want to place the user.
ms.assetid: fb51895f-71e1-45b6-b8bc-ed674e822734
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , creating a user
ms.topic: article
ms.date: 05/31/2018
---

# Creating a User

To create a user in Active Directory Domain Services, create a user object in the domain container of the domain where you want to place the user. Users can be created at the root of the domain, within an organizational unit, or within a container.

When you create a user object, you must also set the attributes, listed in the following table, to set the object as a legal user that is recognized by Active Directory Domain Services and the Windows Security system.



| Attribute                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**cn**](/windows/desktop/ADSchema/a-cn)                         | Specifies the name of the user object in the directory. This will be the object's relative distinguished name (RDN).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**sAMAccountName**](/windows/desktop/ADSchema/a-samaccountname) | Specifies a string that is the name used to support clients and servers from a previous version of Windows. The [**sAMAccountName**](/windows/desktop/ADSchema/a-samaccountname) should be less than 20 characters to support clients from a previous version of Windows.<br/> The [**sAMAccountName**](/windows/desktop/ADSchema/a-samaccountname) must be unique among all security principal objects within the domain. You should perform a query against the domain to verify that the **sAMAccountName** is unique within the domain.<br/> [**sAMAccountName**](/windows/desktop/ADSchema/a-samaccountname) is an optional attribute. The server will create a random **sAMAccountName** value if none is specified.<br/> |



 

You can also set other attributes. The following user attributes are set with default values if you do not explicitly set them at creation time.




| Attribute | Description | 
|-----------|-------------|
| <a href="/windows/desktop/ADSchema/a-accountexpires"><strong>accountExpires</strong></a> | Specifies when the account will expire. The default is <strong>TIMEQ_FOREVER</strong>, which indicates that the account will never expire.<br /> | 
| <a href="/windows/desktop/ADSchema/a-ntsecuritydescriptor"><strong>nTSecurityDescriptor</strong></a> | A security descriptor is created based on specific rules. For more information, see <a href="how-security-descriptors-are-set-on-new-directory-objects.md">How Security Descriptors are Set on New Directory Objects</a>.<br /> | 
| <a href="/windows/desktop/ADSchema/a-objectcategory"><strong>objectCategory</strong></a> | Specifies the user category. The default is "Person".<br /> | 
| <a href="/windows/desktop/ADSchema/a-name"><strong>name</strong></a> | Specifies the user name. The default is the value set for <a href="/windows/desktop/ADSchema/a-cn"><strong>cn</strong></a>.<br /> | 
| <a href="/windows/desktop/ADSchema/a-pwdlastset"><strong>pwdLastSet</strong></a> | Specifies when the user last set the password. The default is zero, which indicates that the user must change the password at next logon.<br /> | 
| <a href="/windows/desktop/ADSchema/a-useraccountcontrol"><strong>userAccountControl</strong></a> | Contains values that determine several logon and account features for the user.<br /> By default, the following flags are set:<br /><ul><li><strong>UF_ACCOUNTDISABLE</strong> - The account is disabled.</li><li><strong>UF_PASSWD_NOTREQD</strong> - No password is required.</li><li><strong>UF_NORMAL_ACCOUNT</strong> - Default account type that represents a typical user.</li></ul> | 
| <a href="/windows/desktop/ADSchema/a-memberof"><strong>memberOf</strong></a> | Specifies the group or groups that the user is a direct member of. The default is "Domain Users".<br /> | 




 

A user is created by binding to the desired container and then using one of the following methods. The [**cn**](/windows/desktop/ADSchema/a-cn) and [**sAMAccountName**](/windows/desktop/ADSchema/a-samaccountname) attributes must be set before the user is committed to the server.



| Method                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IADsContainer.Create**](/windows/desktop/api/iads/nf-iads-iadscontainer-create)                        | The [**cn**](/windows/desktop/ADSchema/a-cn) attribute is taken from the *bstrRelativeName* parameter. The new user must be committed by calling [**IADs.SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) or the object will not be created. For more information, see [Example Code for Creating a User](example-code-for-creating-a-user.md).<br/>                                                                                            |
| [**IDirectoryObject::CreateDSObject**](/windows/desktop/api/iads/nf-iads-idirectoryobject-createdsobject) | The [**cn**](/windows/desktop/ADSchema/a-cn) attribute is taken from the *pszRDNName* parameter. The new user is committed when [**CreateDSObject**](/windows/desktop/api/iads/nf-iads-idirectoryobject-createdsobject) is called. For more information, see [Example Code for Creating a User](example-code-for-creating-a-user.md).<br/>                                                                                                                |
| [DirectoryEntries.Add](/dotnet/api/system.directoryservices.directoryentries.add?view=dotnet-plat-ext-3.1)       | The [**cn**](/windows/desktop/ADSchema/a-cn) attribute is taken from the *name* parameter. The new user object must be committed by calling [DirectoryEntry.CommitChanges](/dotnet/api/system.directoryservices.directoryentry.commitchanges#System_DirectoryServices_DirectoryEntry_CommitChanges) or the object will not be created. For more information, see [Adding Directory Objects](/previous-versions/ms180851(v=vs.90)).<br/> |



 

The new user must be committed to the server before any attributes other than [**cn**](/windows/desktop/ADSchema/a-cn) and [**sAMAccountName**](/windows/desktop/ADSchema/a-samaccountname) can be modified. This is because the user account does not actually exist until the user is committed. If an attribute is retrieved or modified for an object that does not exist on the server, an error will occur. This includes calling the [**IADsUser.SetPassword**](/windows/desktop/api/iads/nf-iads-iadsuser-setpassword) method. For example, the following sequence would be followed when creating a user with [**IADsContainer.Create**](/windows/desktop/api/iads/nf-iads-iadscontainer-create):

1.  Call [**IADsContainer.Create**](/windows/desktop/api/iads/nf-iads-iadscontainer-create) to create the user in the local cache with the specified [**cn**](/windows/desktop/ADSchema/a-cn).
2.  Set the [**sAMAccountName**](/windows/desktop/ADSchema/a-samaccountname) attribute to the desired value with the [**IADs.Put**](/windows/desktop/api/iads/nf-iads-iads-put) method.
3.  Now modify other attributes, such as [**userAccountControl**](/windows/desktop/ADSchema/a-useraccountcontrol). This restriction also applies to the ADSI properties, such as [**IADsUser.AccountDisabled**](/windows/desktop/ADSI/iadsuser-property-methods), and methods such as [**IADsUser.SetPassword**](/windows/desktop/api/iads/nf-iads-iadsuser-setpassword).
4.  Call [**IADs.SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) to commit the new user to the server.

When a new user account is created, it is disabled by default. The account must be enabled manually or programmatically. To programmatically enable a user account, remove the **ADS\_UF\_ACCOUNTDISABLE** flag from the [**userAccountControl**](/windows/desktop/ADSchema/a-useraccountcontrol) attribute.

When a new user account is created, the [**userAccountControl**](/windows/desktop/ADSchema/a-useraccountcontrol) attribute for the account automatically has the **UF\_PASSWD\_NOTREQD** flag set, which indicates that no password is required for the account. If the security policies of the domain that the account is created in requires a password for all user accounts, then the **UF\_PASSWD\_NOTREQD** flag must be removed from the **userAccountControl** attribute for the account.

## Related topics

<dl> <dt>

[Example Code for Creating a User](example-code-for-creating-a-user.md)
</dt> </dl>
