---
Description: 'Retrieves a Boolean value that specifies whether the Active Directory Federation Services (ADFS) component and the external and internal certification services are installed.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '2a4df1af-2442-419c-a100-c07e9062320e'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ADFederationService.IsSupported property'
---

# ADFederationService.IsSupported property

The **IsSupported** property retrieves a Boolean value that specifies whether the Active Directory Federation Services (ADFS) component and the external and internal certification services are installed.

This property is read-only.

## Syntax


```VB
ADFederationService.IsSupported
```



## Property value

This property returns a Boolean value.

## Remarks

If the **IsSupported** property value is not **True**, the following [**ADFederationService**](adfederationservice-object.md) properties throw exceptions:

-   [**Enabled**](adfederationservice-enabled-property.md)
-   [**IsProxyEmailAddressesAllowed**](adfederationservice-isproxyemailaddressesallowed-property.md)
-   [**RightsAccountCertificateRequestUrl**](adfederationservice-rightsaccountcertificaterequesturl-property.md)
-   [**ValidityPeriodInDays**](adfederationservice-validityperiodindays-property.md)

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ADFederationService**](adfederationservice-object.md)
</dt> </dl>

 

 




