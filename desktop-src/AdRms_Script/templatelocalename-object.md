---
Description: Defines a name and locale ID (LCID) pair for a template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5d886415-e337-4757-bcae-9b401a101b03
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TemplateLocaleName object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# TemplateLocaleName object

The **TemplateLocaleName** object defines a name and locale ID (LCID) pair for a template. It is used by the [**Copy**](rightstemplatecollection-copy-method.md) method on the [**RightsTemplateCollection**](rightstemplatecollection-object.md) object.

## Members

The **TemplateLocaleName** object has these types of members:

-   [Properties](#properties)

### Properties

The **TemplateLocaleName** object has these properties.



| Property                                                                | Description                                                                   |
|:------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**LanguageId**](templatelocalename-languageid-property.md)<br/> | Specifies or retrieves the locale ID (LCID) for the template name.<br/> |
| [**Name**](templatelocalename-name-property.md)<br/>             | Specifies or retrieves the name of the template.<br/>                   |



 

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
' Copy a Rights Template.

SUB CopyTemplate()

 DIM templateMgr
 DIM template
 DIM localeInfo
 DIM localeInfoColl
 DIM retTemplate

 ' Retrieve the RightsTemplatePolicy object.
 SET templateMgr = config_manager.RightsTemplatePolicy
 CheckError()

 ' Retrieve the first item in the collection.
 Set template = templateMgr.RightsTemplateCollection.Item(0)
 CheckError()

 ' Create a locale name collection object and locale name object.
 SET localeInfo = CreateObject( "Microsoft." _
  & "RightsManagementServices.Admin.TemplateLocaleName")
 SET localeInfoColl = CreateObject( "Microsoft." _
  & "RightsManagementServices.Admin.TemplateLocaleNameCollection")
 CheckError()

 ' For the U.S. English language (LCID = 1033), create a new
 ' template name. Create a new name for each relevant LCID.
 localeInfo.LanguageId = 1033
 localeInfo.Name = "New name"
 localeInfoColl.Add( localeInfo )
 CheckError()

 ' Create the new template.
 SET retTemplate = templateMgr.RightsTemplateCollection.Copy( _
  template.Id, _
  localeInfoColl)
 CheckError()

 IF IsNull(retTemplate.Id) OR LEN(retTemplate.Id) = 0 THEN
  CALL RaiseError(-408, "Fail to call Copy().")
 END IF

 CALL WScript.Echo( "Template.Copy(): Count=" _
              & templateMgr.RightsTemplateCollection.Count _
              & " New-ID=" & retTemplate.Id)

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

[**RightsTemplateCollection**](rightstemplatecollection-object.md)
</dt> </dl>

 

 




