---
Description: 'Retrieves the external service URLs for enterprise.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '436a79ae-b2bb-4e37-b795-4e25a6d51bfc'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'Urls.Extranets property'
---

# Urls.Extranets property

The **Extranets** property retrieves the external service URLs for enterprise.

This property is read-only.

## Syntax


```VB
Urls.Extranets
```



## Property value

This property returns an [**EnterpriseUrls**](enterpriseurls-object.md) object. The property is read-only.

## Remarks

The URL can identify the AD RMS Licensing service or the AD RMS Account Certification service.

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
' Retrieve the URL of the extranet RMS Account Certification service.

SUB GetServiceUrl()

  DIM cluster_info

  SET cluster_info = config_manager.ClusterInformation
  CheckError()

  CALL WScript.Echo("The Certification service URL is " _
                    & cluster_info.Urls.Extranets.Certification)

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

[**Urls**](urls-object.md)
</dt> </dl>

 

 




