---
Description: Manages AD RMS server exclusion policies.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e9b00e0b-187f-475d-9a71-48e1e30edf2e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExclusionPolicy object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ExclusionPolicy object

The **ExclusionPolicy** object manages AD RMS server exclusion policies. Exclusion policies deny new certificate and license requests made by compromised principals. They do not, however, revoke the principal. Administrators can use this object to exclude applications, legacy operating systems, user accounts, and legacy lockbox versions. You can retrieve this object by calling the [**ExclusionPolicy**](enterprise-exclusionpolicy-property.md) property on the [**Enterprise**](enterprise-object.md) object.

## Members

The **ExclusionPolicy** object has these types of members:

-   [Properties](#properties)

### Properties

The **ExclusionPolicy** object has these properties.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>Applications</strong>](exclusionpolicy-applications-property.md)<br/></td>
<td style="text-align: left;">Retrieves a collection of excluded applications.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>DisableLegacyWindowsVersions</strong>](exclusionpolicy-disablelegacywindowsversions-property.md)<br/></td>
<td style="text-align: left;">Specifies or returns a Boolean value that indicates whether computers running legacy operating systems are excluded. AD RMS support begins with Windows 2000.<br/>
<blockquote>
[!Important]<br />
This property may be altered or unavailable in subsequent versions of the operating system. See the [<strong>DisableLegacyWindowsVersions</strong>](exclusionpolicy-disablelegacywindowsversions-property.md) property page for further information about which operating systems support this property.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Lockbox</strong>](exclusionpolicy-lockbox-property.md)<br/></td>
<td style="text-align: left;">Retrieves the minimum lockbox version that must be installed before a use license can be granted.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>UserAccounts</strong>](exclusionpolicy-useraccounts-property.md)<br/></td>
<td style="text-align: left;">Retrieves a collection of excluded user accounts.<br/></td>
</tr>
</tbody>
</table>



 

## Examples


```VB
DIM admin_role
DIM config_manager
DIM exclusionPolicy
DIM excludedAppColl
DIM lockbox
DIM excludedUserColl

  ' Create a Configuration Manager.
  CALL WScript.Echo( "Create ConfigurationManager object...")
  SET config_manager = CreateObject _
    ("Microsoft.RightsManagementServices.Admin.ConfigurationManager")      
  CheckError()

  CALL WScript.Echo( "Initialize...")
  admin_role=config_manager.Initialize(false,"localhost",80,"","","")
  CheckError()
    
   ' Retrieve the ExclusionPolicy object.
  SET exclusionPolicy = config_manager.Enterprise.ExclusionPolicy
  CheckError()

  ' Retrieve the collection of excluded applications.
  Set excludedAppColl = exclusionPolicy.Applications
  CheckError()

  ' Retrieve the ExcludedLockbox object.
  SET lockbox = exclusionPolicy.Lockbox
  CheckError()

  ' Retrieve the ExcludedUSerAccountCollection object.
  SET excludedUserColl = exclusionPolicy.UserAccounts
  CheckError()

' *******************************************************************
' Error checking function.

FUNCTION CheckError()
  CheckError = Err.number
  IF Err.number <> 0 THEN
    CALL WScript.Echo( vbTab & "*****Error Number: " _
                       & Err.number _
                       & " Desc:" _
                       & Err.Description _
                       & "*****")
    WScript.StdErr.Write(Err.Description)
    WScript.Quit( Err.number )
  END IF
END FUNCTION


```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




