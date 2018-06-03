---
Description: Specifies or returns a Boolean value that indicates whether computers running legacy operating systems are excluded. AD RMS support begins with Windows 2000.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 83175603-c3d4-4af0-819d-6f7c0d56441f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExclusionPolicy.DisableLegacyWindowsVersions property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExclusionPolicy.DisableLegacyWindowsVersions property

\[Note The DisableLegacyWindowsVersions property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The **DisableLegacyWindowsVersions** property specifies or returns a Boolean value that indicates whether computers running legacy operating systems are excluded. AD RMS support begins with Windows 2000.

## Syntax


```VB
ExclusionPolicy.DisableLegacyWindowsVersions
```



## Property value

This property is read/write.

## Remarks

The RMS version 1.0 client is supported on legacy operating systems that do not support NTLM authentication. To help enforce NTLM authentication, you can call the **DisableLegacyWindowsVersions** property to prevent users from consuming rights-protected content on computers that are running operating systems earlier than Windows 2000.

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
| End of client support<br/>    | Windows Vista<br/>                                                                                                |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExclusionPolicy**](exclusionpolicy-object.md)
</dt> </dl>

 

 




