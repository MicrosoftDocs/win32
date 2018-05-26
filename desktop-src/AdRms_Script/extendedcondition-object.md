---
Description: Contains predefined policies that can be set on a rights template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c8f9210f-977c-40f1-9ce0-d370867b5e4f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExtendedCondition object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ExtendedCondition object

The **ExtendedCondition** object contains predefined policies that can be set on a rights template. This object can be retrieved by calling the [**ExtendedCondition**](rightstemplate-extendedcondition-property.md) property on the [**RightsTemplate**](rightstemplate-object.md) object.

## Members

The **ExtendedCondition** object has these types of members:

-   [Properties](#properties)

### Properties

The **ExtendedCondition** object has these properties.



| Property                                                                                               | Description                                                                                                                       |
|:-------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**EnableOnetimeLicense**](extendedcondition-enableonetimelicense-property.md)<br/>             | Specifies or retrieves a Boolean value that indicates whether a new license is required each time content is consumed.<br/> |
| [**EnableViewInTrustedBrowser**](extendedcondition-enableviewintrustedbrowser-property.md)<br/> | Specifies or retrieves a Boolean value that indicates whether a client can view protected content in a browser.<br/>        |



 

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**RightsTemplate**](rightstemplate-object.md)
</dt> </dl>

 

 




