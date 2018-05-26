---
Description: Specifies or retrieves a Boolean value that indicates whether Active Directory Federation Services (ADFS) trust is enabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5c23f969-e8c8-46db-929b-fdf2a58aaa20
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ADFederationService.Enabled property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADFederationService.Enabled property

The **Enabled** property specifies or retrieves a Boolean value that indicates whether Active Directory Federation Services (ADFS) trust is enabled.

## Syntax


```VB
ADFederationService.Enabled
```



## Property value

This property is read/write.

## Remarks

Before a federated user can access rights-protected content, the ADFS service must be installed and enabled, and a rights account certificate must be issued. A rights account certificate (RAC) binds a computer to an end-user license. The AD RMS service issues a RAC when the **Enabled** property is set to **True**. For related information, see [**IsSupported**](adfederationservice-issupported-property.md) and [**RightsAccountCertificateRequestUrl**](adfederationservice-rightsaccountcertificaterequesturl-property.md).

If the [**IsSupported**](adfederationservice-issupported-property.md) property value is **false**, the **Enabled** property throws an exception.

The ADFS service must be enabled before any of the following properties can be set or retrieved:

-   [**IsProxyEmailAddressesAllowed**](adfederationservice-isproxyemailaddressesallowed-property.md)
-   [**RightsAccountCertificateRequestUrl**](adfederationservice-rightsaccountcertificaterequesturl-property.md)
-   [**ValidityPeriodInDays**](adfederationservice-validityperiodindays-property.md)

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

 

 




