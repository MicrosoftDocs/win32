---
Description: 'Retrieves a RevocationCondition object that contains information about template revocation.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '1c751dd2-1e29-42ba-92b9-f58dfd63732f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'RightsTemplate.RevocationCondition property'
---

# RightsTemplate.RevocationCondition property

The **RevocationCondition** property retrieves a [**RevocationCondition**](revocationcondition-object.md) object that contains information about template revocation.

This property is read-only.

## Syntax


```VB
RightsTemplate.RevocationCondition
```



## Property value

This property returns a [**RevocationCondition**](revocationcondition-object.md) object. The property is read-only.

## Remarks

The [**RevocationCondition**](revocationcondition-object.md) object contains the following information:

-   The URL at which one can find information about the revocation policy.
-   The maximum number of days that a template can exist before it must be refreshed.
-   The path to the revocation public key.

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
' Add revocation information to a template. 

SUB AddRevocation()

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
    
  ' Add revocation information to the first template.
  templateObj.RevocationCondition.Url = "http://test"
  templateObj.RevocationCondition.RefreshPerDays = 30
  templateObj.RevocationCondition.PublicKeyFile = "PublicKey.dat"
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

 

 




