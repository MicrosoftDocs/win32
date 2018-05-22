---
Description: 'Contains information about the server licensor private key used to encrypt the content encryption key and sign all certificates and licenses issued by the server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '269293e6-f2c5-4446-b651-e1295b230025'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: ServicePrivateKeyProtectionInformation object
---

# ServicePrivateKeyProtectionInformation object

The **ServicePrivateKeyProtectionInformation** object contains information about the server licensor private key used to encrypt the content encryption key and sign all certificates and licenses issued by the server. The AD RMS service uses a 1024-bit RSA key pair. You can retrieve this object by calling the [**ServicePrivateKeyProtectionInformation**](enterprise-serviceprivatekeyprotectioninformation-property.md) property on the [**Enterprise**](enterprise-object.md) object.

## Members

The **ServicePrivateKeyProtectionInformation** object has these types of members:

-   [Properties](#properties)

### Properties

The **ServicePrivateKeyProtectionInformation** object has these properties.



| Property                                                                                                                                | Description                                                                                                                 |
|:----------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**CryptographicServiceProviderName**](serviceprivatekeyprotectioninformation-cryptographicserviceprovidername-property.md)<br/> | Retrieves the name of the cryptographic provider.<br/>                                                                |
| [**IsServicePrivateKeySoftwareBased**](serviceprivatekeyprotectioninformation-isserviceprivatekeysoftwarebased-property.md)<br/> | Retrieves a Boolean value that specifies whether the cryptographic provider is implemented entirely in software.<br/> |
| [**KeyContainer**](serviceprivatekeyprotectioninformation-keycontainer-property.md)<br/>                                         | Retrieves the name of the cryptographic key container used to store the private key.<br/>                             |



 

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




