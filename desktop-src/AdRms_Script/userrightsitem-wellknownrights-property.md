---
Description: Specifies or retrieves common rights.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a74f8e60-5947-4bb7-8a93-82911f4f8f23
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: UserRightsItem.WellKnownRights property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserRightsItem.WellKnownRights property

The **WellKnownRights** property specifies or retrieves common rights.

## Syntax


```VB
UserRightsItem.WellKnownRights
```



## Property value

This property specifies or returns an integer value that contains the right or rights. This can be a combination of the following values defined by the [**Constants**](constants-object.md) object:

-   [**TemplateRightAllowMacros**](constants-templaterightallowmacros-property.md)
-   [**TemplateRightEdit**](constants-templaterightedit-property.md)
-   [**TemplateRightExport**](constants-templaterightexport-property.md)
-   [**TemplateRightExtract**](constants-templaterightextract-property.md)
-   [**TemplateRightForward**](constants-templaterightforward-property.md)
-   [**TemplateRightFullControl**](constants-templaterightfullcontrol-property.md)
-   [**TemplateRightPrint**](constants-templaterightprint-property.md)
-   [**TemplateRightReply**](constants-templaterightreply-property.md)
-   [**TemplateRightReplyAll**](constants-templaterightreplyall-property.md)
-   [**TemplateRightSave**](constants-templaterightsave-property.md)
-   [**TemplateRightView**](constants-templaterightview-property.md)
-   [**TemplateRightViewRights**](constants-templaterightviewrights-property.md)

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
' Add user rights to the template. 

SUB AddRights()

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

  ' Add rights information.
  SET rights = CreateObject( _
      "Microsoft.RightsManagementServices.Admin.UserRightsItem")
  rights.UserId = "someone@example.com"
  rights.WellKnownRights = _
        config_manager.Constants.TemplateRightExtract + _
        config_manager.Constants.TemplateRightPrint + _
        config_manager.Constants.TemplateRightForward
  rights.CustomRights.Add("CUSTOMRIGHTA")
  rights.CustomRights.Add("CUSTOMRIGHTB")
  Err.Clear()
  templateObj.UserRightsItems.Add( rights )
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

[**UserRightsItem**](userrightsitem-object.md)
</dt> </dl>

 

 




