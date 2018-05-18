---
Description: 'Changes the owner of a user profile to a different user.'
ms.assetid: 'a0ba12a6-6fe6-4e06-9346-a54cc19143e6'
title: 'ChangeOwner method of the Win32\_UserProfile class'
---

# ChangeOwner method of the Win32\_UserProfile class

Changes the owner of a user profile to a different user.

## Syntax


```mof
uint32 ChangeOwner(
  [in] string NewOwnerSID,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*NewOwnerSID* \[in\]
</dt> <dd>

The SID of the new owner of the profile.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Bit flags to replace or delete a profile. This parameter can be set to one or more of the following values.



| Value                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ReplaceNewOwnerProfile"></span><span id="replacenewownerprofile"></span><span id="REPLACENEWOWNERPROFILE"></span><dl> <dt>**ReplaceNewOwnerProfile**</dt> <dt>0</dt> </dl> | If the new owner already has a profile, calling the **ChangeOwner** method with this flag replaces the existing profile. If the new owner already has a profile, calling this method without this flag fails and returns **HRESULT\_FROM\_WIN32**(**ERROR\_ALREADY\_EXISTS**).<br/>                                                                                                                               |
| <span id="DeleteReplacedProfile"></span><span id="deletereplacedprofile"></span><span id="DELETEREPLACEDPROFILE"></span><dl> <dt>**DeleteReplacedProfile**</dt> <dt>1</dt> </dl>     | If the new owner has a profile and **ReplaceNewOwnerProfile** and **DeleteReplacedProfile** properties are specified, the replaced profile is deleted. If **DeleteReplacedProfile** is not set, the replaced profile is unchanged. The profile is not deleted, not enumerated, and no user automatically uses the replaced profile. If **ReplaceNewOwnerProfile** is not specified, this flag has no effect.<br/> |



 

</dd> </dl>

## Remarks

Because the **ChangeOwner** method modifies the SID of the user profile, the user of the WMI object must perform one of these steps when using this method

-   Call **ChangeOwner**, and then reinstall all apps.

    > [!Note]  
    > If this step is taken, access control lists (ACLs) may contain incorrect settings.

     

-   Remove all apps before calling **ChangeOwner**, and then reinstall those apps after the call.

    > [!Note]  
    > This step is the cleaner solution, but app state and settings may be lost.

     

## Examples

To use [**Win32\_UserProfile**](win32-userprofile.md) to migrate a user to a new domain, see the following [Vista’s MoveUser.exe replacement](http://blogs.technet.com/b/askds/archive/2008/09/09/vista-s-moveuser-exe-replacement.aspx) article on TechNet.

## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                                |
| MOF<br/>                      | <dl> <dt>UserProfileWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Profprov.dll</dt> </dl>               |



## See also

<dl> <dt>

[**Win32\_UserProfile**](win32-userprofile.md)
</dt> </dl>

 

 




