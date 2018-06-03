---
Description: Can be used to specify the amount of time for which rights account certificates (RACs) are valid.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 85ca9f7f-950a-46f8-b4c6-5b31a168f1b0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: IssuancePolicy object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IssuancePolicy object

The **IssuancePolicy** object can be used to specify the amount of time for which rights account certificates (RACs) are valid. You can specify the validity periods for both standard and temporary RACs. You can retrieve this object by calling the [**IssuancePolicy**](enterprise-issuancepolicy-property.md) property on the [**Enterprise**](enterprise-object.md) object.

## Members

The **IssuancePolicy** object has these types of members:

-   [Properties](#properties)

### Properties

The **IssuancePolicy** object has these properties.



| Property                                                                                                                              | Description                                                                |
|:--------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**StandardCertificateValidityPeriodInDays**](issuancepolicy-standardcertificatevalidityperiodindays-property.md)<br/>         | Specifies or retrieves the validity period for a standard RAC.<br/>  |
| [**TemporaryCertificateValidityPeriodInMinutes**](issuancepolicy-temporarycertificatevalidityperiodinminutes-property.md)<br/> | Specifies or retrieves the validity period for a temporary RAC.<br/> |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




