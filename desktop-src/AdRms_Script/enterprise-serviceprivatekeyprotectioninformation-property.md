---
Description: Retrieves an object that contains information about the server licensor private key.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 32a7de32-3b30-48b5-ae20-afe719fc156f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Enterprise.ServicePrivateKeyProtectionInformation property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enterprise.ServicePrivateKeyProtectionInformation property

The **ServicePrivateKeyProtectionInformation** property retrieves an object that contains information about the server licensor private key.

This property is read-only.

## Syntax


```VB
Enterprise.ServicePrivateKeyProtectionInformation
```



## Property value

This property returns a [**ServicePrivateKeyProtectionInformation**](serviceprivatekeyprotectioninformation-object.md) object.

## Remarks

You can use a [**ServicePrivateKeyProtectionInformation**](serviceprivatekeyprotectioninformation-object.md) object to retrieve the names of the cryptographic provider and key container and to determine whether the provider is implemented entirely in software.

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

  ' Retrieve the name of the cryptographic provider.
  CALL WScript.Echo("CSP name: " _
                    & keyInfo.CryptographicServiceProviderName)
  CheckError()

  ' Retrieve the name of the key container.
  CALL WScript.Echo("Container name: " & keyInfo.KeyContainer)
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

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




