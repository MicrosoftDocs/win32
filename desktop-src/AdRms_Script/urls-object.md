---
Description: 'Can be used to retrieve internal and external web service URLs contained in an EnterpriseUrls object.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '0635b668-41f2-43ff-990b-db9feefd17a5'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: Urls interface
---

# Urls interface

The **Urls** object can be used to retrieve internal and external web service URLs contained in an [**EnterpriseUrls**](enterpriseurls-object.md) object. Currently, URLs can be retrieved for the AD RMS Licensing service and the AD RMS Account Certification service. You can retrieve the object by calling the [**Urls**](clusterinformation-urls-property.md) property on the [**ClusterInformation**](clusterinformation-object.md) object.

## Members

The **Urls** interface has these types of members:

-   [Properties](#properties)

### Properties

The **Urls** interface has these properties.



| Property                                                | Description                                                        |
|:--------------------------------------------------------|:-------------------------------------------------------------------|
| [**Extranets**](urls-extranets-property.md)<br/> | Retrieves the external service URLs for enterprise.<br/>     |
| [**Intranets**](urls-intranets-property.md)<br/> | Retrieves the internal service URLs for the enterprise.<br/> |



 

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
' Retrieve the Urls object.

SUB GetUrls()

  DIM cluster_info
  DIM urls

  SET cluster_info = config_manager.ClusterInformation
  CheckError()

  SET urls = cluster_info.Urls
  CheckError()

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

 

 




