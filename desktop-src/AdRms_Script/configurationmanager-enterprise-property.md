---
Description: Retrieves an Enterprise object that can be used for enterprise administration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 73db9798-d909-4367-9c66-d26e238f3677
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ConfigurationManager.Enterprise property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConfigurationManager.Enterprise property

The **Enterprise** property retrieves an [**Enterprise**](enterprise-object.md) object that can be used for enterprise administration.

This property is read-only.

## Syntax


```VB
ConfigurationManager.Enterprise
```



## Property value

This property returns an [**Enterprise**](enterprise-object.md) object. The property is read-only.

## Remarks

The [**Enterprise**](enterprise-object.md) object is created when the [**Initialize**](configurationmanager-initialize-method.md) method is called if the access control list on the AD RMS Administration website supports the Administrator (0x4) role.

## Examples


```VB
DIM config_manager
DIM admin_role
DIM enterprise_manager
DIM database_info

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
' Retrieve an Enterprise object and the associated database.

SUB GetEnterpriseDataBase()

  SET enterprise_manager = config_manager.Enterprise
  CheckError()

  SET database_info = enterprise_manager.EnterpriseDatabase
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ConfigurationManager**](configurationmanager-object.md)
</dt> </dl>

 

 




