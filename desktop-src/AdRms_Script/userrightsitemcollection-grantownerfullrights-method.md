---
Description: Grants full rights to the content owner.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d2afb45d-e4ca-4996-aaa2-d8fd5773b44d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: UserRightsItemCollection.GrantOwnerFullRights method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserRightsItemCollection.GrantOwnerFullRights method

The **GrantOwnerFullRights** method grants full rights to the content owner.

## Syntax


```VB
UserRightsItemCollection.GrantOwnerFullRights()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

You can use this property to grant the owner full rights without expiration. The rights are applied even if you identify a content expiration date. You can use the [**UserRightsItem**](userrightsitem-object.md) object to grant a subset of rights, or you can use the **GrantOwnerFullRights** method to grant all rights at once.

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
' Grant the content owner full rights

SUB AddOwnerRights()

  DIM templMgr
  DIM templObj

  ' Retrieve the RightsTemplatePolicy object.
  SET templMgr = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the first template in the collection.
  SET templObj = templMgr.RightsTemplateCollection.Item(0)
  CheckError()

 ' Grant all rights to the owner.
  templObj.UserRightsItems.GrantOwnerFullRights()
  CheckError()
  
  ' Update the templates on the server.
  templMgr.RightsTemplateCollection.Update( templObj )
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

[**UserRightsItemCollection**](userrightsitemcollection-object.md)
</dt> </dl>

 

 




