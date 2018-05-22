---
Description: 'Contains enterprise service URLs. Currently URLs can be retrieved for the AD RMS Licensing web service and the AD RMS Account Certification web service.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '0b5eab85-4468-49c5-bdee-e9e17512aa76'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: EnterpriseUrls object
---

# EnterpriseUrls object

The **EnterpriseUrls** object contains enterprise service URLs. Currently URLs can be retrieved for the AD RMS Licensing web service and the AD RMS Account Certification web service.

## Members

The **EnterpriseUrls** object has these types of members:

-   [Properties](#properties)

### Properties

The **EnterpriseUrls** object has these properties.



| Property                                                                  | Description                                                                     |
|:--------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| [**Certification**](enterpriseurls-certification-property.md)<br/> | Retrieves the intranet or extranet AD RMS Account Certification URL.<br/> |
| [**Licensing**](enterpriseurls-licensing-property.md)<br/>         | Retrieves the intranet or extranet AD RMS Licensing URL.<br/>             |



 

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
' Retrieve the URL of the intranet RMS Account Certification service.

SUB GetServiceUrl()

  DIM cluster_info
 
  SET cluster_info = config_manager.ClusterInformation
  CheckError()

  CALL WScript.Echo("The Certification service URL is " _
                    & cluster_info.Urls.Intranets.Certification)

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




