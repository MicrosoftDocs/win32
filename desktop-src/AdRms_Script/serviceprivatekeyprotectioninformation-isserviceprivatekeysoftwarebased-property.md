---
Description: Retrieves a Boolean value that specifies whether the cryptographic provider is implemented entirely in software.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 337f822f-a2ad-450d-b5c3-883457c22be1
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServicePrivateKeyProtectionInformation.IsServicePrivateKeySoftwareBased property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ServicePrivateKeyProtectionInformation.IsServicePrivateKeySoftwareBased property

The **IsServicePrivateKeySoftwareBased** property retrieves a Boolean value that specifies whether the cryptographic provider is implemented entirely in software.

This property is read-only.

## Syntax


```VB
ServicePrivateKeyProtectionInformation.IsServicePrivateKeySoftwareBased
```



## Property value

This property is read-only.

## Examples


```VB
DIM config_manager
DIM admin_role

' *******************************************************************
' Create and initialize a ConfigurationManager object.

SUB InitObject()

  CALL WScript.Echo( "Create ConfigurationManager object...")
  SET config_manager = CreateObject _
    ("Microsoft.RightsManagementServices.Admin.ConfigurationManager")      
  CheckError()
    
  CALL WScript.Echo( "Initialize...")
  admin_role=config_manager.Initialize(false,"localhost",80,"","","")
  CheckError()

END SUB

' *******************************************************************
' Retrieve information about the server licensor private  key.

SUB GetKeyInfo()

  DIM keyInfo
  Dim isSoftware

  ' Retrieve the ServicePrivateKeyProtectionInformation object.
  SET keyInfo = _
    config_manager.Enterprise.ServicePrivateKeyProtectionInformation
  CheckError()

  ' Retrieve a value that specifies whether the cryptographic
  ' provider is implemented entirely in software.
  isSoftware = "True"
  If keyInfo.IsServicePrivateKeySoftwareBased <> True Then
    isSoftware = "False"
  End If
  CALL WScript.Echo("IsSoftwareBased: " & isSoftware)
 
END SUB

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

[**ServicePrivateKeyProtectionInformation**](serviceprivatekeyprotectioninformation-object.md)
</dt> </dl>

 

 




