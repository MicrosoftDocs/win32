---
Description: Can be used to manage Active Directory Federation Services (ADFS) support.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 59fe13b7-99e3-4564-a70c-f9ea62598565
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ADFederationService object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ADFederationService object

The **ADFederationService** object can be used to manage Active Directory Federation Services (ADFS) support. ADFS is a component available beginning with Windows Server 2003 R2 that enables a user to access multiple web applications during the life of a single online session. Using ADFS, organizations can share user identity within an organization and across federated organizations so that the users can access ADFS-configured resources. If ADFS is installed and enabled, an AD RMS server can grant content access to federated users. You can retrieve this object by calling the [**ADFederationService**](trustpolicy-adfederationservice-property.md) property on the [**TrustPolicy**](trustpolicy-object.md) object.

## Members

The **ADFederationService** object has these types of members:

-   [Properties](#properties)

### Properties

The **ADFederationService** object has these properties.



| Property                                                                                                                 | Description                                                                                                                                                                               |
|:-------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Enabled**](adfederationservice-enabled-property.md)<br/>                                                       | Specifies or retrieves a Boolean value that indicates whether ADFS trust is enabled.<br/>                                                                                           |
| [**IsProxyEmailAddressesAllowed**](adfederationservice-isproxyemailaddressesallowed-property.md)<br/>             | Specifies or retrieves a Boolean value that indicates whether proxy email addresses can be used to identify users.<br/>                                                             |
| [**IsSupported**](adfederationservice-issupported-property.md)<br/>                                               | Retrieves a Boolean value that specifies whether the Active Directory Federation Services (ADFS) component and the external and internal certification services are installed.<br/> |
| [**RightsAccountCertificateRequestUrl**](adfederationservice-rightsaccountcertificaterequesturl-property.md)<br/> | Specifies or retrieves the URL of a website from which a rights account certificate for a federated user can be requested.<br/>                                                     |
| [**ValidityPeriodInDays**](adfederationservice-validityperiodindays-property.md)<br/>                             | Specifies or retrieves the number of days for which a rights account certificate is valid.<br/>                                                                                     |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




