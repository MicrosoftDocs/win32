---
Description: Retrieves a value that specifies a right to export content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 971fb631-1cc2-4bbe-bf39-bfb186c8d883
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Constants.TemplateRightExport property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Constants.TemplateRightExport property

The **TemplateRightExport** property retrieves a value that specifies a right to export content.

This property is read-only.

## Syntax


```VB
Constants.TemplateRightExport
```



## Property value

This property returns an integer value (256).

## Remarks

You can use this property value in the [**WellKnownRights**](userrightsitem-wellknownrights-property.md) property on the [**UserRightsItem**](userrightsitem-object.md) object.

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

  DIM templMgr
  DIM template
  DIM userColl
  DIM user
  DIM constant
  DIM CommonRights

  ' Retrieve the Constants object.
  SET constant = config_manager.Constants

  ' Retrieve the RightsTemplatePolicy object.
  SET templMgr = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the first template in the collection.
  SET template = templMgr.RightsTemplateCollection.Item(0)
  CheckError()

  ' Retrieve the user rights collection.
  SET userColl = template.UserRightsItems

  ' Retrieve and display the user data from the collection.
  FOR EACH user IN userColl
    CALL WScript.Echo("UserId: " & user.UserId)
    CommonRights = user.WellKnownRights

    IF CommonRights = 0 THEN
      CALL WScript.Echo("No rights are defined.")
    ELSE
      IF constant.TemplateRightAllowMacros AND CommonRights THEN
        CALL WScript.Echo("Right: AllowMacros.")
       END IF
      IF constant.TemplateRightEdit AND CommonRights THEN
        CALL WScript.Echo("Right: Edit.")
      END IF
      IF constant.TemplateRightExport AND CommonRights THEN
        CALL WScript.Echo("Right: Export.")
      END IF
      IF constant.TemplateRightExtract AND CommonRights THEN
        CALL WScript.Echo("Right: Extract.")
      END IF
      IF constant.TemplateRightForward AND CommonRights THEN
        CALL WScript.Echo("Right: Forward.")
      END IF
      IF constant.TemplateRightFullControl AND CommonRights THEN
        CALL WScript.Echo("Right: Owner.")
      END IF
      IF constant.TemplateRightPrint AND CommonRights THEN
        CALL WScript.Echo("Right: Print.")
      END IF
      IF constant.TemplateRightReply AND CommonRights THEN
        CALL WScript.Echo("Right: Reply.")
      END IF
      IF constant.TemplateRightReplyAll AND CommonRights THEN
        CALL WScript.Echo("Right: ReplyAll.")
      END IF
      IF constant.TemplateRightSave AND CommonRights THEN
        CALL WScript.Echo("Right: Save.")
      END IF
      IF constant.TemplateRightView AND CommonRights THEN
        CALL WScript.Echo("Right: View.")
      END IF
      IF constant.TemplateRightViewRights AND CommonRights THEN
        CALL WScript.Echo("Right: ViewRights.")
      END IF
    END IF
  NEXT
 
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
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**Constants**](constants-object.md)
</dt> </dl>

 

 




