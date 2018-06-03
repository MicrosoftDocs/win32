---
Description: Specifies or retrieves the locale ID (LCID) for the template name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6dd95c0f-f626-4eb2-86fb-2be5be863894
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TemplateLocaleName.LanguageId property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TemplateLocaleName.LanguageId property

The **LanguageId** property specifies or retrieves the locale ID (LCID) for the template name.

## Syntax


```VB
TemplateLocaleName.LanguageId
```



## Property value

This property specifies or retrieves an integer value that contains the LCID. For example, the LCID for U.S. English is 1033. For a complete list of the LCIDs supported by Microsoft, see [List of Locale ID (LCID) Values as Assigned by Microsoft](http://go.microsoft.com/fwlink/p/?linkid=63028).

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

[**TemplateLocaleName**](templatelocalename-object.md)
</dt> </dl>

 

 




