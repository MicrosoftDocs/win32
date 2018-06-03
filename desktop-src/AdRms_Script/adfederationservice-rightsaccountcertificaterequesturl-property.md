---
Description: Specifies or retrieves the URL of a website from which a rights account certificate can be requested by using ADFS.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d97fe7ac-ea1f-48e4-8d5f-62a3e1a7c34e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ADFederationService.RightsAccountCertificateRequestUrl property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ADFederationService.RightsAccountCertificateRequestUrl property

The **RightsAccountCertificateRequestUrl** property specifies or retrieves the URL of a website from which a rights account certificate can be requested by using ADFS.

## Syntax


```VB
ADFederationService.RightsAccountCertificateRequestUrl
```



## Property value

This property specifies or returns a string value.

## Remarks

The property value must be a well-formatted URL or an empty string. If the string is empty when you specify the property, AD RMS uses the default URL. Currently, this is the certification URL in Active Directory.

If the [**IsSupported**](adfederationservice-issupported-property.md) property value is **false**, the **RightsAccountCertificateRequestUrl** property throws an exception.

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

 

 




