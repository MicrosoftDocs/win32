---
Description: Retrieves a Boolean value that specifies whether the AD RMS Licensing service and the AD RMS Account Certification service have been decommissioned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 18fffad8-a8ea-4b09-bb3f-2b32ba18a6c5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ClusterInformation.IsDecommissioned property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusterInformation.IsDecommissioned property

The **IsDecommissioned** property retrieves a Boolean value that specifies whether the AD RMS Licensing service and the AD RMS Account Certification service have been decommissioned.

This property is read-only.

## Syntax


```VB
ClusterInformation.IsDecommissioned
```



## Property value

This property returns a Boolean value. The property is read-only.

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
' Retrieve a ClusterInformation object. Determine whether the
' site has been decommissioned.

SUB ChkClusterInfo()

  DIM cluster_info

  SET cluster_info = config_manager.ClusterInformation
  CheckError()

  IF cluster_info.IsDecommissioned THEN
    CALL WScript.Echo( "   ***The site is decommissioned***" )
    EXIT SUB
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

[**ClusterInformation**](clusterinformation-object.md)
</dt> </dl>

 

 




