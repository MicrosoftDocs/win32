---
Description: Specifies or retrieves the name portion of a name-value pair.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 78dbc680-8766-4468-8ce4-2bf41d5fdb28
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ApplicationSpecificDataItem.Name property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ApplicationSpecificDataItem.Name property

The **Name** property specifies or retrieves the name portion of a name-value pair.

## Syntax


```VB
ApplicationSpecificDataItem.Name
```



## Property value

This property specifies or retrieves a string that contains the name.

## Remarks

The name can be used in conjunction with the [**Value**](applicationspecificdataitem-value-property.md) property to identify additional information to be added to a rights template.

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

 

 




