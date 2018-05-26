---
Description: Represents a template condition that can be used to specify when protected content or a use license expires.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4481b661-2a21-40c7-8020-64bb737e423b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExpirationCondition object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ExpirationCondition object

The **ExpirationCondition** object represents a template condition that can be used to specify when protected content or a use license expires. If protected content expires it must be republished before it can be used again. If a use license expires or is not cached, the user must connect to the AD RMS cluster to obtain a new license. This object can be retrieved by calling the [**ExpirationCondition**](rightstemplate-expirationcondition-property.md) property on the [**RightsTemplate**](rightstemplate-object.md) object.

## Members

The **ExpirationCondition** object has these types of members:

-   [Properties](#properties)

### Properties

The **ExpirationCondition** object has these properties.



| Property                                                                         | Description                                                                                                                   |
|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**ExpirationData**](expirationcondition-expirationdata-property.md)<br/> | Retrieves an [**ExpirationData**](expirationdata-object.md) object that specifies when protected content expires.<br/> |
| [**RenewalDays**](expirationcondition-renewaldays-property.md)<br/>       | Specifies or retrieves the number of days after issuance that a use license expires.<br/>                               |



 

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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**RightsTemplate**](rightstemplate-object.md)
</dt> </dl>

 

 




