---
Description: 'Specifies or retrieves the name of the template.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'e8dfbb08-3000-4075-a748-a9cd6c318873'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'TemplateLocaleName.Name property'
---

# TemplateLocaleName.Name property

The **Name** property specifies or retrieves the name of the template.

## Syntax


```VB
TemplateLocaleName.Name
```



## Property value

This property specifies or retrieves a string value that contains the name.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**TemplateLocaleName**](templatelocalename-object.md)
</dt> </dl>

 

 




