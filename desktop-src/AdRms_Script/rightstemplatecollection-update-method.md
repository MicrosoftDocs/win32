---
Description: Updates the template collection on the server database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7dd0018d-e545-4063-ad85-c1e90f9b7419
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RightsTemplateCollection.Update method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RightsTemplateCollection.Update method

The **Update** method updates the template collection on the server database.

## Syntax


```VB
RightsTemplateCollection.Update( _
  ByVal template _
)
```



## Parameters

<dl> <dt>

*template* \[in\]
</dt> <dd>

The [**RightsTemplate**](rightstemplate-object.md) object to be updated. The object must exist on the AD RMS server.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method updates the collection on the server with your changes while preserving the changes made by others. Call the [**Refresh**](rightstemplatecollection-refresh-method.md) method to update your collection from the server database.

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
' Update a Rights Template.

SUB UpdateRightsTest()

  DIM template_manager

  SET template_manager = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the first template in the collection and change its
  ' summary information.
  SET firstObj = template_manager.RightsTemplateCollection.Item(0)
  firstObj.Summaries.Item(0).Description = "Updated description"
  CheckError()

  ' Update the template on the server.
  template_manager.RightsTemplateCollection.Update( firstObj )
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

 

 




