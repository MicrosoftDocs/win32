---
Description: 'Specifies or retrieves the UNC path for the rights templates.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'fdbd3bd6-4bcd-4dff-8eba-99bb926bf61e'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'RightsTemplatePolicy.PublishingFilePath property'
---

# RightsTemplatePolicy.PublishingFilePath property

The **PublishingFilePath** property specifies or retrieves the UNC path for the rights templates.

## Syntax


```VB
RightsTemplatePolicy.PublishingFilePath
```



## Property value

This property specifies or returns a string that contains the path.

## Remarks

Before a template can be used, it must be distributed to the client computer. You can use a mechanism such as Group Policy to distribute templates throughout the organization from a shared folder. The shared folder path must be specified by using the Universal Naming Convention (UNC). The format is **\\\\***ServerName***\\***ShareName***\\***Path***\\***FileName*. Templates are also stored in the configuration database, and when a user requests a license, the server applies the template from the database.

> [!Note]  
> Templates can also be retrieved by using the [**AcquireTemplates**](https://msdn.microsoft.com/library/bb309050) web method in the AD RMS SDK.

 

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
' Retrieve the template collection path object.

SUB GetTemplatePath()

  DIM template_manager

  SET template_manager = config_manager.RightsTemplatePolicy
  CheckError()

  CALL WScript.Echo( "The collection path is " _
                     & template_manager.PublishingFilePath)

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

[**RightsTemplatePolicy**](rightstemplatepolicy-object.md)
</dt> </dl>

 

 




