---
Description: Retrieves an object that can be used to manage server exclusion policies.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4a73bb99-932a-4d56-9148-6d2bf5ddf038
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Enterprise.ExclusionPolicy property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enterprise.ExclusionPolicy property

The **ExclusionPolicy** property retrieves an object that can be used to manage server exclusion policies.

This property is read-only.

## Syntax


```VB
Enterprise.ExclusionPolicy
```



## Property value

This property returns an [**ExclusionPolicy**](exclusionpolicy-object.md) object.

## Remarks

Exclusion policies deny new certificate and license requests made by compromised principals.

## Examples


```VB
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

  ' Exclude legacy operating systems. AD RMS support begins with 
  ' Windows 2000.
  exclusionPolicy.DisableLegacyWindowsVersions = TRUE
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

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




