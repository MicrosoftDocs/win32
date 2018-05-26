---
Description: Specifies or retrieves the value portion of a name-value pair.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d6e9263d-538d-41f4-bec1-3ef6d8bb27ef
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ApplicationSpecificDataItem.Value property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ApplicationSpecificDataItem.Value property

The **Value** property specifies or retrieves the value portion of a name-value pair.

## Syntax


```VB
ApplicationSpecificDataItem.Value
```



## Property value

This property specifies or retrieves a string.

## Remarks

The value can be used in conjunction with the [**Name**](applicationspecificdataitem-name-property.md) property to identify additional information to be added to a rights template.

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
' Create a template and add it to the template collection. 

SUB ExcludeApplication()

  DIM templateMgr
  DIM templateColl
  DIM templateObj

  ' Retrieve the RightsTemplatePolicy object.
  SET templateMgr = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the rights template collection.
  SET templateColl = templateMgr.RightsTemplateCollection
  CheckError()

  ' Retrieve the first template in the collection.
  SET templateObj = templateMgr.RightsTemplateCollection.Item(0)
  CheckError()

  ' Create and add a name-value pair to the template.
  SET appData = CreateObject( "Microsoft." _
      & "RightsManagementServices.Admin.ApplicationSpecificDataItem")
  appData.Name = "xxx"
  appData.Value = "yyy"
  templateObj.ApplicationSpecificDataItems.Add( appData )
  CheckError()

  ' Update the templates on the server.
  templateMgr.RightsTemplateCollection.Update( templateObj )
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

[**ApplicationSpecificDataItem**](applicationspecificdataitem-object.md)
</dt> </dl>

 

 




