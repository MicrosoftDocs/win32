---
Description: 'Retrieves an ExtendedCondition object that identifies additional predefined conditions that can be applied to the rights contained in the template.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '521d7b91-26d1-4338-8f7e-cb60aaec3459'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'RightsTemplate.ExtendedCondition property'
---

# RightsTemplate.ExtendedCondition property

The **ExtendedCondition** property retrieves an [**ExtendedCondition**](extendedcondition-object.md) object that identifies additional predefined conditions that can be applied to the rights contained in the template.

This property is read-only.

## Syntax


```VB
RightsTemplate.ExtendedCondition As ExtendedCondition
```



## Property value

This property returns an [**ExtendedCondition**](extendedcondition-object.md) object. The property is read-only.

## Remarks

The [**ExtendedCondition**](extendedcondition-object.md) object contains properties that enable you to specify whether an end user license can be used more than once and whether a client can view protected content in a browser.

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
' Add extended condition information to a template. 

SUB AddExtendedCondition()

  DIM template_manager
  DIM templateColl
  DIM templateObj
  DIM summary
  DIM rights
  DIM appData
  DIM itemIndex

  ' Retrieve the RightsTemplatePolicy object.
  SET template_manager = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the rights template collection.
  SET templateColl = template_manager.RightsTemplateCollection
  CheckError()

  ' Retrieve the first template in the collection.
  SET templateObj = template_manager.RightsTemplateCollection.Item(0)
  CheckError()

  ' Add extended condition information.
  templateObj.ExtendedCondition.EnableViewInTrustedBrowser = true
  templateObj.ExtendedCondition.EnableOnetimeLicense = true
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

 

 




