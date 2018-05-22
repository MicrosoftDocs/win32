---
Description: 'Retrieves the intranet or extranet AD RMS Account Certification URL.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '2f07e155-4a57-497f-84ad-e445f5d92821'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'EnterpriseUrls.Certification property'
---

# EnterpriseUrls.Certification property

The **Certification** property retrieves the intranet or extranet AD RMS Account Certification URL.

## Syntax


```VB
EnterpriseUrls.Certification As String
```



## Property value

This property returns a **String** that contains the URL. The property is read-only.

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

[**EnterpriseUrls**](enterpriseurls-object.md)
</dt> </dl>

 

 




