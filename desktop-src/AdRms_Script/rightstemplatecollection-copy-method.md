---
Description: Copies a rights template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d45993f1-6809-4e81-af3b-1d4a944e05d1
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RightsTemplateCollection.Copy method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RightsTemplateCollection.Copy method

The **Copy** method copies a rights template.

## Syntax


```VB
RightsTemplateCollection.Copy( _
  ByVal sourceTemplateId, _
  ByVal localeNames _
)
```



## Parameters

<dl> <dt>

*sourceTemplateId* \[in\]
</dt> <dd>

A string value that contains the ID of the template being copied. The ID is a GUID assigned by the AD RMS server when the template is created. You can retrieve it by calling the [**Id**](rightstemplate-id-property.md) property on the [**RightsTemplate**](rightstemplate-object.md) object.

</dd> <dt>

*localeNames* \[in\]
</dt> <dd>

A [**TemplateLocaleNameCollection**](templatelocalenamecollection-object.md) object that contains a collection of template names and associated locale IDs (LCIDs). No name/LCID pair in this collection can duplicate a name/LCID pair that already exists.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

You can use this method to create a new template from an existing template. The template name/LCID pair must be unique. The RMS server creates a new ID and assigns it to the template.

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

[**RightsTemplateCollection**](rightstemplatecollection-object.md)
</dt> </dl>

 

 




