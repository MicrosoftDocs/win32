---
Description: Specifies or retrieves the validity period for a temporary rights account certificate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c79e0117-6cf3-44be-ba48-64a382e54c07
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: IssuancePolicy.TemporaryCertificateValidityPeriodInMinutes property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IssuancePolicy.TemporaryCertificateValidityPeriodInMinutes property

The **TemporaryCertificateValidityPeriodInMinutes** property specifies or retrieves the validity period for a temporary rights account certificate.

## Syntax


```VB
IssuancePolicy.TemporaryCertificateValidityPeriodInMinutes
```



## Property value

This property sets or returns an integer value that contains the validity period, in minutes.

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
' Define a rights account certificate (RAC) issuance policy.

SUB SetIssuancePolicy()

  DIM issuePolicy

  ' Retrieve the IssuancePolicy object.
  SET issuePolicy = config_manager.Enterprise.IssuancePolicy
  CheckError()

  ' Set the validity period on the standard RAC to 120 days.
  issuePolicy.StandardCertificateValidityPeriodInDays = 120

  ' Set the validity period on the temporary RAC to 60 minutes.
  issuePolicy.TemporaryCertificateValidityPeriodInMinutes = 60

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

[**IssuancePolicy**](issuancepolicy-object.md)
</dt> </dl>

 

 




