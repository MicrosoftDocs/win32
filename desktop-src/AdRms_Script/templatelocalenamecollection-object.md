---
Description: Manages a collection of TemplateLocaleName objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 440b7e05-efe8-4fc4-974e-1312edbba406
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TemplateLocaleNameCollection object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# TemplateLocaleNameCollection object

The **TemplateLocaleNameCollection** object manages a collection of [**TemplateLocaleName**](templatelocalename-object.md) objects. Each object in the collection defines a name and locale ID (LCID) pair for a template. The collection is used by the [**Copy**](rightstemplatecollection-copy-method.md) method on the [**RightsTemplateCollection**](rightstemplatecollection-object.md) object.

## Members

The **TemplateLocaleNameCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **TemplateLocaleNameCollection** object has these methods.



| Method                                                     | Description                                                                                                                                                          |
|:-----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Add](http://go.microsoft.com/fwlink/p/?linkid=87269)      | Adds an object to the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                                |
| [Clear](http://go.microsoft.com/fwlink/p/?linkid=87270)    | Removes all objects from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                         |
| [Contains](http://go.microsoft.com/fwlink/p/?linkid=87271) | Determines whether the collection contains a specific object (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                    |
| [CopyTo](http://go.microsoft.com/fwlink/p/?linkid=87281)   | Copies the collection elements to an array, starting at a specified index (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [IndexOf](http://go.microsoft.com/fwlink/p/?linkid=87273)  | Retrieves the index of a specific object in the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Insert](http://go.microsoft.com/fwlink/p/?linkid=87274)   | Inserts an object in the collection at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Remove](http://go.microsoft.com/fwlink/p/?linkid=87276)   | Removes the first occurrence of the specified object from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>        |
| [RemoveAt](http://go.microsoft.com/fwlink/p/?linkid=87277) | Removes the object at the specified index from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                   |



 

### Properties

The **TemplateLocaleNameCollection** object has these properties.



| Property                                                           | Description                                                                                                                                            |
|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Count](http://go.microsoft.com/fwlink/p/?linkid=87280)<br/> | Retrieves the number of objects contained in the collection (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [Item](http://go.microsoft.com/fwlink/p/?linkid=87278)<br/>  | Specifies or retrieves the object at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>          |



 

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
</dt> <dt>

[**TemplateLocaleName**](templatelocalename-object.md)
</dt> </dl>

 

 




