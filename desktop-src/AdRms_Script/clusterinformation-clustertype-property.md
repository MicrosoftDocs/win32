---
Description: Retrieves an integer value that identifies whether the AD RMS cluster supports the RMS Licensing web service or the RMS Account Certification web service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f6ab610b-ac5c-4ce3-82db-8e88f3194eb0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ClusterInformation.ClusterType property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusterInformation.ClusterType property

The **ClusterType** property retrieves an integer value that identifies whether the AD RMS cluster supports the RMS Licensing web service or the RMS Account Certification web service.

This property is read-only.

## Syntax


```VB
ClusterInformation.ClusterType
```



## Property value

This read-only property returns a bitwise combination of the following values. You can test the return value by using the appropriate integer or the associated property from the [**Constants**](constants-object.md) object.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0x0)


</dt> <dd>

Licensing and certification are not supported.

</dd> <dt>

<span id="ClusterTypeLicensing"></span><span id="clustertypelicensing"></span><span id="CLUSTERTYPELICENSING"></span>

<span id="ClusterTypeLicensing"></span><span id="clustertypelicensing"></span><span id="CLUSTERTYPELICENSING"></span>**[**ClusterTypeLicensing**](constants-clustertypelicensing-property.md)** (0x1)


</dt> <dd>

The licensing service is supported.

</dd> <dt>

<span id="ClusterTypeCertification"></span><span id="clustertypecertification"></span><span id="CLUSTERTYPECERTIFICATION"></span>

<span id="ClusterTypeCertification"></span><span id="clustertypecertification"></span><span id="CLUSTERTYPECERTIFICATION"></span>**[**ClusterTypeCertification**](constants-clustertypecertification-property.md)** (0x2)


</dt> <dd>

The certification service is supported.

</dd> </dl>

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
' Retrieve the cluster type.

SUB GetClusterType()

  DIM cluster_info
 
  SET cluster_info = config_manager.ClusterInformation
  CheckError()

  CALL WScript.Echo("The cluster type is " _
                    & cluster_info.ClusterType)

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

 

 




