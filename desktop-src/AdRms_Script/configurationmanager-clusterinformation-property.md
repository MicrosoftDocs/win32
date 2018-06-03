---
Description: Retrieves a ClusterInformation object that contains cluster configuration information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2ad52d35-d072-4d02-a25f-a4f610bbfb48
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ConfigurationManager.ClusterInformation property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConfigurationManager.ClusterInformation property

The **ClusterInformation** property retrieves a [**ClusterInformation**](clusterinformation-object.md) object that contains cluster configuration information.

This property is read-only.

## Syntax


```VB
ConfigurationManager.ClusterInformation
```



## Property value

This property returns a [**ClusterInformation**](clusterinformation-object.md) object. The property is read-only.

## Remarks

If you are deploying AD RMS in a cluster, you can use this property to retrieve configuration information about the cluster. The [**ClusterInformation**](clusterinformation-object.md) object is created when the [**Initialize**](configurationmanager-initialize-method.md) method is called if the access control list on the AD RMS Administration website supports the Administrator (0x4), Auditor (0x1), or TemplateEditor (0x2) roles.

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
' referenced site has been decommissioned.

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

[**ConfigurationManager**](configurationmanager-object.md)
</dt> </dl>

 

 




