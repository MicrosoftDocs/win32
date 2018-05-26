---
Description: Retrieves a collection of user-defined rights.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ca2b5196-a9e0-49ac-a354-dc567278ec1b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: UserRightsItem.CustomRights property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserRightsItem.CustomRights property

The **CustomRights** property retrieves a collection of user-defined rights.

This property is read-only.

## Syntax


```VB
UserRightsItem.CustomRights
```



## Property value

This property returns a [**StringCollection**](stringcollection-object.md) object that contains the rights.

## Remarks

A custom right must be unique, and its name cannot exceed 256 characters. The following names are reserved and cannot be used to identify a custom right. The names are not case-sensitive.

-   View
-   Extract
-   ObjModel
-   ViewRightsData
-   Print
-   Forward
-   Reply
-   ReplyAll
-   Export
-   Edit
-   DocEdit

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

 

 




