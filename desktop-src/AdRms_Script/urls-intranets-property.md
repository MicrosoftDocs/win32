---
Description: Retrieves the internal service URLs for the enterprise.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8daac996-1773-42f1-bf0a-075617ef7308
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Urls.Intranets property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Urls.Intranets property

The **Intranets** property retrieves the internal service URLs for the enterprise.

This property is read-only.

## Syntax


```VB
Urls.Intranets
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**Urls**](urls-object.md)
</dt> </dl>

 

 




