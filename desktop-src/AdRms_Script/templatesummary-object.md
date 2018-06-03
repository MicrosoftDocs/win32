---
Description: Contains descriptive information about a template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 54c1f4fd-eb46-458a-bc67-af832703ffa5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TemplateSummary object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# TemplateSummary object

The **TemplateSummary** object contains descriptive information about a template.

## Members

The **TemplateSummary** object has these types of members:

-   [Properties](#properties)

### Properties

The **TemplateSummary** object has these properties.



| Property                                                               | Description                                                                         |
|:-----------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| [**Description**](templatesummary-description-property.md)<br/> | Specifies or retrieves a description of the rights template.<br/>             |
| [**LanguageId**](templatesummary-languageid-property.md)<br/>   | Specifies or retrieves an LCID for the template name.<br/>                    |
| [**Name**](templatesummary-name-property.md)<br/>               | Specifies or retrieves the name of the rights template for a given LCID.<br/> |



 

## Remarks

The **TemplateSummary** object contains a template description, a locale ID (LCID), and the template name. The name and the description are both written in the language identified by the LCID. For example, if the LCID equals 1033, the name and the descriptive information are both written in U.S. English. For a complete list of the LCIDs supported by Microsoft, see [List of Locale ID (LCID) Values as Assigned by Microsoft](http://go.microsoft.com/fwlink/p/?linkid=63028). A collection of **TemplateSummary** objects is contained in the [**TemplateSummaryCollection**](templatesummarycollection-object.md) object. You can retrieve the collection by calling the [**Summaries**](rightstemplate-summaries-property.md) property on the [**RightsTemplate**](rightstemplate-object.md) object.

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**TemplateSummaryCollection**](templatesummarycollection-object.md)
</dt> </dl>

 

 




