---
Description: Retrieves a value that specifies the number of days after publication that protected content expires.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8b50d015-5ce6-48dd-aac6-0a105a74316f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Constants.TemplateExpirationTypeUntilDays property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Constants.TemplateExpirationTypeUntilDays property

The **TemplateExpirationTypeUntilDays** property retrieves a value that specifies the number of days after publication that protected content expires.

This property is read-only.

## Syntax


```VB
Constants.TemplateExpirationTypeUntilDays
```



## Property value

This property returns an integer value (0x3).

## Remarks

You can use this property value with the [**ExpirationType**](expirationdata-expirationtype-property.md) property on the [**ExpirationData**](expirationdata-object.md) object.

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
' Add expiration information to the template. 

SUB AddExpirationData()

  DIM tempMgr
  DIM template
  DIM constant
  DIM type

  ' Retrieve the RightsTemplatePolicy object.
  SET tempMgr = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the Constants object.
  SETt constant = config_manager.Constants
  CheckError()

  ' Retrieve the first template in the template collection.
  SET template = tempMgr.RightsTemplateCollection.Item(0)
  CheckError()

  ' Retrieve the content expiration type.
  type = template.ExpirationCondition.ExpirationData.ExpirationType

  ' Display the type.
  IF type = constant.TemplateExpirationTypeNever THEN
    CALL WScript.Echo("Type: TemplateExpirationTypeNever")
  ELSEIF type = constant.TemplateExpirationTypeOnDate THEN
    CALL WScript.Echo("Type: TemplateExpirationTypeOnDate")
  ELSEIF type = constant.TemplateExpirationTypeUntilDays THEN
    CALL WScript.Echo("Type: TemplateExpirationTypeUntilDays")
  ELSEIF type = 0 THEN
    CALL WScript.Echo("Type: Expiration not identified")
  ELSE
    CALL WScript.Echo("Error: ExpirationType")
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

[**Constants**](constants-object.md)
</dt> </dl>

 

 




