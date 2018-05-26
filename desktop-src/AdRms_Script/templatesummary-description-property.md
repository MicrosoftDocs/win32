---
Description: Specifies or retrieves a description of the rights template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c21fab4d-0205-4671-a7e4-5015cafb8f60
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TemplateSummary.Description property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TemplateSummary.Description property

The **Description** property specifies or retrieves a description of the rights template.

## Syntax


```VB
TemplateSummary.Description
```



## Property value

This property specifies or retrieves a string value.

## Remarks

The description must be written in the language specified by the [**LanguageId**](templatesummary-languageid-property.md) property.

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
' Add summary information to the template. 

SUB AddSummaryData()

  DIM template_manager
  DIM templateColl
  DIM templateObj

  ' Retrieve the RightsTemplatePolicy object.
  SET template_manager = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the rights template collection.
  SET templateColl = template_manager.RightsTemplateCollection
  CheckError()

  ' Retrieve the first template in the collection.
  SET templateObj = template_manager.RightsTemplateCollection.Item(0)
  CheckError()

  ' Add summary information.
  SET summary = CreateObject( _
      "Microsoft.RightsManagementServices.Admin.TemplateSummary")
  summary.LanguageId = 1033
  summary.Name = "Scripting test template"
  summary.Description = "Scripting test template Desc"
  templateObj.Summaries.Add( summary )
  CheckError()
  
  ' Update the templates on the server.
  template_manager.RightsTemplateCollection.Update( templateObj )
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

[**TemplateSummary**](templatesummary-object.md)
</dt> </dl>

 

 




