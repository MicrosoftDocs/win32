---
Description: Specifies or retrieves the number of days for which a rights account certificate is valid.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 35ce32a8-5479-4621-b900-7cfdadb91788
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ADFederationService.ValidityPeriodInDays property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ADFederationService.ValidityPeriodInDays property

The **ValidityPeriodInDays** property specifies or retrieves the number of days for which a rights account certificate is valid.

## Syntax


```VB
ADFederationService.ValidityPeriodInDays
```



## Property value

This property specifies or returns an integer value. This value must be between 1 and 9999 inclusive.

## Remarks

A rights account certificate (RAC) binds a computer to an end-user license. The AD RMS service issues a RAC when the [**Enabled**](adfederationservice-enabled-property.md) property is set to **True**.

If the [**IsSupported**](adfederationservice-issupported-property.md) property value is **false**, the **ValidityPeriodInDays** property throws an exception.

The ADFS service must be enabled before this property is called. For more information, see [**Enabled**](adfederationservice-enabled-property.md).

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
</dt> </dl>

 

 




