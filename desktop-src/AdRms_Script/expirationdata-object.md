---
Description: Can be used to specify when AD RMS&\#8211;protected content expires and can no longer be opened.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dd4b2928-9ffc-4cb0-89a9-3e9e4bdd9de3
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExpirationData object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ExpirationData object

The **ExpirationData** object can be used to specify when AD RMS protected content expires and can no longer be opened. This object specifies both the type of expiration and the value associated with that type as shown by the following table.

| ExpirationData.ExpirationType                                                                       | ExpirationData.Value                                                        | Description                                                                 |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**TemplateExpirationTypeNever**](constants-templateexpirationtypenever-property.md) (0x1)         | **Null** (**Nothing**)                                                      | The content never expires.                                                  |
| [**TemplateExpirationTypeOnDate**](constants-templateexpirationtypeondate-property.md) (0x2)       | A **Date** value. You can use **Now** to specify the current date and time. | The content expires on the date specified.                                  |
| [**TemplateExpirationTypeUntilDays**](constants-templateexpirationtypeuntildays-property.md) (0x3) | An integer value that contains the number of days.                          | The content expires the specified number of days after the publishing date. |



 

You can retrieve this object by calling the [**ExpirationData**](expirationcondition-expirationdata-property.md) property on the [**ExpirationCondition**](expirationcondition-object.md) object.

## Members

The **ExpirationData** object has these types of members:

-   [Properties](#properties)

### Properties

The **ExpirationData** object has these properties.



| Property                                                                    | Description                                                                                            |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| [**ExpirationType**](expirationdata-expirationtype-property.md)<br/> | Specifies or retrieves a value that identifies the expiration period for protected content.<br/> |
| [**Value**](expirationdata-value-property.md)<br/>                   | Specifies or retrieves the value associated with the content expiration period.<br/>             |



 

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
</dt> </dl>

 

 




