---
Description: 'Retrieves a Boolean value that specifies whether the template can be exported.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '40eab223-b6e4-4613-857b-8c4adb4af130'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'RightsTemplate.IsPublished property'
---

# RightsTemplate.IsPublished property

The **IsPublished** property retrieves a Boolean value that specifies whether the template can be exported.

## Syntax


```VB
RightsTemplate.IsPublished
```



## Property value

This read-only property returns a Boolean value.

## Remarks

You can call the [**Publish**](rightstemplatecollection-publish-method.md) method to set the **IsPublished** property. A value of **True** specifies that the template is published, and a value of **false** specifies that the template is archived. When a template is archived, it cannot be used to publish new content and it cannot be distributed. Published templates can be distributed and used to issue licenses.

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
' Display template properties. 

SUB GetTemplateValues()

  DIM template_manager
  DIM templateColl
  DIM templateObj

  ' Retrieve the RightsTemplatePolicy object.
  SET template_manager = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the rights template collection.
  SET templateColl = template_manager.RightsTemplateCollection
  CheckError()

  ' Retrieve property values for each template in the collection.
  For Each templateObj in template_manager.RightsTemplateCollection
    CALL WScript.Echo( "Id: " _
                       & templateObj.Id)
    CALL WScript.Echo( "CreatedTime: " _
                       & templateObj.CreatedTime)
    CALL WScript.Echo( "UpdatedTime: " _
                       & templateObj.UpdatedTime)
    CALL WScript.Echo( "Author: " _
                       & templateObj.Author)
    CALL WScript.Echo( "Name: " _
                       & templateObj.Summaries.Item(0).Name)
    CALL WScript.Echo( "Description: " _
                       & templateObj.Summaries.Item(0).Description)
    CALL WScript.Echo( "IsPublished: " _
                       & templateObj.Summaries.Item(0).IsPublished)
  Next
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**RightsTemplate**](rightstemplate-object.md)
</dt> </dl>

 

 




