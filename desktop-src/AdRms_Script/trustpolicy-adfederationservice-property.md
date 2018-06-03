---
Description: Retrieves an object that manages AD RMS use of Active Directory Federation Services (ADFS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e96bc598-ec90-41ab-8601-7ec30fcbc88b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustPolicy.ADFederationService property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TrustPolicy.ADFederationService property

The **ADFederationService** property retrieves an object that manages AD RMS use of Active Directory Federation Services (ADFS).

This property is read-only.

## Syntax


```VB
TrustPolicy.ADFederationService
```



## Property value

This property returns an [**ADFederationService**](adfederationservice-object.md) object.

## Remarks

ADFS is a component available beginning with Windows Server 2003 R2 that enables a user to access multiple web applications during the life of a single online session. If ADFS is installed and enabled, an AD RMS server can grant content access to federated users.

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
' Specify ADFS information.

SUB SetADFS()
    
  DIM objADFS

  SET objADFS = _
    config_manager.Enterprise.TrustPolicy.ADFederationService
  CheckError()
        
  IF objADFS.IsSupported = TRUE THEN
    objADFS.Enabled = true
    CheckError()

    objADFS.ValidityPeriodInDays = 10
    CheckError()

    objADFS.RightsAccountCertificateRequestUrl = _
        "https://www.example.com"
    CheckError()

    objADFS.IsProxyEmailAddressesAllowed = TRUE
    CheckError()
  END IF

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

' *******************************************************************
' Generate a runtime error.

SUB RaiseError(errId, desc)
  CALL Err.Raise( errId, "", desc )
  CheckError()
END SUB
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ADFederationService**](adfederationservice-object.md)
</dt> <dt>

[**TrustPolicy**](trustpolicy-object.md)
</dt> </dl>

 

 




