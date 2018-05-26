---
Description: Retrieves an object that can be used to manage the server licensor certificate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 22aa06f9-3e3e-479f-9015-304d63cf6df0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Enterprise.ServerLicensorCertificate property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enterprise.ServerLicensorCertificate property

The **ServerLicensorCertificate** property retrieves an object that can be used to manage the server licensor certificate.

This property is read-only.

## Syntax


```VB
Enterprise.ServerLicensorCertificate
```



## Property value

This property returns a [**ServerLicensorCertificate**](serverlicensorcertificate-object.md) object.

## Remarks

A licensor certificate grants the AD RMS server the right to issue certificates and use licenses.

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
  DIM environment
  DIM preProd
  DIM production

  production = config_manager.Constants.KeyHierarchyProduction
  preProd = config_manager.Constants.KeyHierarchyPreproduction

  ' Retrieve the ServerLicensorCertificate object.
  SET slc = config_manager.Enterprise.ServerLicensorCertificate
  CheckError()

  ' Retrieve the certificate display name.
  CALL WScript.Echo("SLC name: " & slc.FriendlyName)

  ' Retrieve the certificate hierarchy.
  environment = slc.KeyHierarchy
  If environment = preProd Then
    CALL WScript.Echo("Environment = Pre-Production")
  Elseif environment = production
    CALL WScript.Echo("Environment = Production")
  Else
    CALL WScript.Echo("Environment = Other")
  Endif

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

[**Enterprise**](enterprise-object.md)
</dt> </dl>

 

 




