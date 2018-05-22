---
Description: 'Retrieves an ApplicationSpecificDataItemCollection object that contains application specific name-value pairs.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '78b66bfc-2463-40c8-9f0b-da9e438bd6ec'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'RightsTemplate.ApplicationSpecificDataItems property'
---

# RightsTemplate.ApplicationSpecificDataItems property

The **ApplicationSpecificDataItems** property retrieves an [**ApplicationSpecificDataItemCollection**](applicationspecificdataitemcollection-object.md) object that contains application specific name-value pairs.

This property is read-only.

## Syntax


```VB
RightsTemplate.ApplicationSpecificDataItems
```



## Property value

This property returns an [**ApplicationSpecificDataItemCollection**](applicationspecificdataitemcollection-object.md) object. The property is read-only.

## Remarks

Each name-value pair in the collection is represented by an [**ApplicationSpecificDataItem**](applicationspecificdataitem-object.md) object that contains a user-defined application display name and the name of the corresponding executable file.

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

  ' Identify an excluded application.
  SET appData = CreateObject( _
      "Microsoft.RightsManagementServices.Admin.ApplicationSpecificDataItem")
  appData.Name = "NOTE PAD"
  appData.Value = "Notepad.exe"
  templateObj.ApplicationSpecificDataItems.Add( appData )
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**RightsTemplate**](rightstemplate-object.md)
</dt> </dl>

 

 




