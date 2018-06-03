---
Description: Contains read-only AD RMS configuration information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c7333663-55f3-4e8c-9aab-d74b953940d8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ClusterInformation object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ClusterInformation object

The **ClusterInformation** object contains read-only AD RMS configuration information. You can retrieve the object by calling the [**ClusterInformation**](configurationmanager-clusterinformation-property.md) property on the [**ConfigurationManager**](configurationmanager-object.md) object.

## Members

The **ClusterInformation** object has these types of members:

-   [Properties](#properties)

### Properties

The **ClusterInformation** object has these properties.



| Property                                                                              | Description                                                                                                                                                           |
|:--------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdminContactEmail**](clusterinformation-admincontactemail-property.md)<br/> | Retrieves the email address of the AD RMS administrator.<br/>                                                                                                   |
| [**ClusterType**](clusterinformation-clustertype-property.md)<br/>             | Retrieves an integer value that identifies whether the AD RMS cluster supports the RMS Licensing web service or the RMS Account Certification web service.<br/> |
| [**IsDecommissioned**](clusterinformation-isdecommissioned-property.md)<br/>   | Retrieves a Boolean value that specifies whether the AD RMS Licensing service and the AD RMS Account Certification service have been decommissioned.<br/>       |
| [**Servers**](clusterinformation-servers-property.md)<br/>                     | Retrieves a collection that contains the names of the servers in the AD RMS cluster.<br/>                                                                       |
| [**Urls**](clusterinformation-urls-property.md)<br/>                           | Retrieves an [**Urls**](urls-object.md) object that contains enterprise service URLs.<br/>                                                                     |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




