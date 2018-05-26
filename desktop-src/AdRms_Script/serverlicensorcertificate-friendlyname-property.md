---
Description: Specifies or retrieves the certificate display name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 775267b4-75ab-42c0-b8f6-18a392dab5e0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServerLicensorCertificate.FriendlyName property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ServerLicensorCertificate.FriendlyName property

The **FriendlyName** property specifies or retrieves the certificate display name.

This property is read/write.

## Syntax


```VB
' Data type: 

ServerLicensorCertificate.FriendlyName
```



## Property value

This property sets or returns a string value.

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
' Retrieve the server licensor certificate.

SUB GetSLC()

  DIM slc

  ' Retrieve the ServerLicensorCertificate object.
  SET slc = config_manager.Enterprise.ServerLicensorCertificate
  CheckError()

  ' Retrieve the certificate display name.
  CALL WScript.Echo("SLC name: " & slc.FriendlyName)

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

[**ServerLicensorCertificate**](serverlicensorcertificate-object.md)
</dt> </dl>

 

 




