---
Description: Retrieves the name of the cryptographic key container used to store the private key.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 174eea00-adae-4f46-ac34-a9f39f78b337
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServicePrivateKeyProtectionInformation.KeyContainer property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ServicePrivateKeyProtectionInformation.KeyContainer property

The **KeyContainer** property retrieves the name of the cryptographic key container used to store the private key.

This property is read-only.

## Syntax


```VB
ServicePrivateKeyProtectionInformation.KeyContainer
```



## Property value

This property returns a string value.

## Remarks

For more information, see [Cryptographic Service Providers](https://msdn.microsoft.com/library/windows/desktop/aa380245).

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

  ' Retrieve the ServicePrivateKeyProtectionInformation object.
  SET keyInfo = _
    config_manager.Enterprise.ServicePrivateKeyProtectionInformation
  CheckError()

  ' Retrieve the name of the key container.
  CALL WScript.Echo("Container name: " & keyInfo.KeyContainer)
  CheckError()
 
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

 

 




