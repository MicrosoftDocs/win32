---
Description: 'Retrieves a collection of rights policy templates.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'f1f91a54-d5df-4d59-a8c6-346c279ad3b5'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'RightsTemplatePolicy.RightsTemplateCollection property'
---

# RightsTemplatePolicy.RightsTemplateCollection property

The **RightsTemplateCollection** property retrieves a collection of rights policy templates.

This property is read-only.

## Syntax


```VB
RightsTemplatePolicy.RightsTemplateCollection
```



## Property value

This read-only property returns a [**RightsTemplateCollection**](rightstemplatecollection-object.md) object.

## Remarks

Rights policy templates define content use rights and conditions for a set of users. For more information, see the [**RightsTemplate**](rightstemplate-object.md) object.

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
' Retrieve a rights template collection.

SUB CreateTemplateColl()

  DIM template_manager
  DIM templateColl

  SET template_manager = config_manager.RightsTemplatePolicy
  CheckError()

  SET templateColl = template_manager.RightsTemplateCollection
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

[**RightsTemplatePolicy**](rightstemplatepolicy-object.md)
</dt> </dl>

 

 




