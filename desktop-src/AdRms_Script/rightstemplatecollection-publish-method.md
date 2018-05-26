---
Description: Identifies whether a template can be either published or archived.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e96e1b3f-359d-42f4-8615-1dd8f2ceb8e8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RightsTemplateCollection.Publish method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RightsTemplateCollection.Publish method

The **Publish** method identifies whether a template can be either published or archived.

## Syntax


```VB
RightsTemplateCollection.Publish( _
  ByVal templateId, _
  ByVal isPublished _
)
```



## Parameters

<dl> <dt>

*templateId* \[in\]
</dt> <dd>

A **String** value that contains the ID of the template being copied. The ID is a GUID assigned by the AD RMS server when the template is created. You can retrieve it by calling the [**Id**](rightstemplate-id-property.md) property on the [**RightsTemplate**](rightstemplate-object.md) object.

</dd> <dt>

*isPublished* \[in\]
</dt> <dd>

A Boolean value that specifies whether the template is to be published (**True**) or archived (**False**).

</dd> </dl>

## Return value

This method returns (**True**) if it succeeds and (**False**) if it fails.

## Remarks

When a template is archived, it can be used only to issue licenses to consume content. An archived template cannot be distributed or used to publish new content. Published templates can be distributed and used to publish new content or issue licenses.

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
' Publish a Rights Template.

SUB PublishTemplate()

  DIM templateMgr
  DIM template

  ' Retrieve the RightsTemplatePolicy object.
  SET templateMgr = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the first object in the collection.
  SET template = templateMgr.RightsTemplateCollection.Item(0)
  CheckError()

  ' Specify that the template is to be archived.
  templateMgr.RightsTemplateCollection.Publish template.Id, false
  CheckError()

  ' Or specify that the template is to be published.
  templateMgr.RightsTemplateCollection.Publish template.Id, true
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

[**RightsTemplateCollection**](rightstemplatecollection-object.md)
</dt> </dl>

 

 




