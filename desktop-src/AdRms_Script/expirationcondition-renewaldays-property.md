---
Description: Specifies or retrieves the number of days after issuance that a use license expires.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3885e992-c0be-4752-ab86-25ed5f3e164a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExpirationCondition.RenewalDays property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExpirationCondition.RenewalDays property

The **RenewalDays** property specifies or retrieves the number of days after issuance that a use license expires.

## Syntax


```VB
ExpirationCondition.RenewalDays
```



## Property value

This property specifies or retrieves an integer value.

## Remarks

You can use this property to specify the number of days after license acquisition that a license must be renewed. For example, if you specify 10, users must renew their licenses every 10 days. After 10 days, the license expires and the protected content can no longer be used.

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
' Add expiration information to the template. 

SUB AddExpirationData()

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

  ' Add expiration information.
  templateObj.ExpirationCondition.ExpirationData.ExpirationType = 2
  templateObj.ExpirationCondition.ExpirationData.Value = Now
  templateObj.ExpirationCondition.RenewalDays = 120
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

[**ExpirationCondition**](expirationcondition-object.md)
</dt> </dl>

 

 




