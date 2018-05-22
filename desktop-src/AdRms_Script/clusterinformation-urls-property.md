---
Description: 'Retrieves an Urls object that contains enterprise service URLs.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '43f77d5c-89a2-4654-8350-54cac18792c7'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ClusterInformation.Urls property'
---

# ClusterInformation.Urls property

The **Urls** property retrieves an [**Urls**](urls-object.md) object that contains enterprise service URLs.

This property is read-only.

## Syntax


```VB
ClusterInformation.Urls
```



## Property value

This property returns an [**Urls**](urls-object.md) object. The property is read-only.

## Remarks

You can use the [**Urls**](urls-object.md) object to retrieve internal or external URLs for the AD RMS Licensing service or the AD RMS Account Certification service.

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
' Retrieve the intranet URL of the RMS Account Certification service.

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

[**ClusterInformation**](clusterinformation-object.md)
</dt> </dl>

 

 




