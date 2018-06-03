---
Description: Distributes the licensor certificate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b2d75d0a-0e98-4782-9480-73d1d094e43a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServerLicensorCertificate.Export method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ServerLicensorCertificate.Export method

The **Export** method distributes the licensor certificate.

## Syntax


```VB
ServerLicensorCertificate.Export( _
  ByVal filePath _
)
```



## Parameters

<dl> <dt>

*filePath* 
</dt> <dd>

A string value that contains the path of the file to which the certificate is exported.

</dd> </dl>

## Return value

This method does not return a value.

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

  ' Export the server licensor certificate.
  slc.Export("c:\Cert.tmp")

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

 

 




