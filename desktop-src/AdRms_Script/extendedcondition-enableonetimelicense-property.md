---
Description: 'Specifies or retrieves a Boolean value that indicates whether a new license is required each time content is consumed.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '2ec5a2d0-ca92-4ddc-bb4d-d51e80ae6310'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ExtendedCondition.EnableOnetimeLicense property'
---

# ExtendedCondition.EnableOnetimeLicense property

The **EnableOnetimeLicense** property specifies or retrieves a Boolean value that indicates whether a new license is required each time content is consumed. If you specify **True**, you will not be able to cache licenses on the client.

## Syntax


```VB
ExtendedCondition.EnableOnetimeLicense
```



## Property value

This property specifies or retrieves a Boolean value. **True** indicates that a one-time license is required and that caching the license on the client is prohibited.

## Remarks

This property controls whether users must acquire a new use license each time they attempt to consume content that was published with the associated rights policy template. When this property value is defined, users must be able to connect to the AD RMS server to retrieve licenses.

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

[**ExtendedCondition**](extendedcondition-object.md)
</dt> </dl>

 

 




