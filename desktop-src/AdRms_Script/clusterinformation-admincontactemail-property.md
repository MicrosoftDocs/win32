---
Description: Retrieves the email address of the AD RMS administrator.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ef6b99be-30c5-49d5-8885-db11994a5cd1
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ClusterInformation.AdminContactEmail property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusterInformation.AdminContactEmail property

The **AdminContactEmail** property retrieves the email address of the AD RMS administrator.

This property is read-only.

## Syntax


```VB
ClusterInformation.AdminContactEmail
```



## Property value

This property returns a **String**. The property is read-only.

## Remarks

You can set this property value by calling the [**UpdateAdminContactEmail**](enterprise-updateadmincontactemail-method.md) method on the [**Enterprise**](enterprise-object.md) object.

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
' Retrieve the administrator email account name.

SUB GetAdminMail()

  DIM cluster_info

  SET cluster_info = config_manager.ClusterInformation
  CheckError()

  CALL WScript.Echo("The administrator email is" _
                    & cluster_info.AdminContactEmail)

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

 

 




