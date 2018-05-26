---
Description: Specifies or retrieves the value associated with the content expiration period.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1b073238-c856-4ffc-9ff3-b022704de8f6
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExpirationData.Value property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExpirationData.Value property

The **Value** property specifies or retrieves the value associated with the content expiration period.

## Syntax


```VB
ExpirationData.Value
```



## Property value

This property specifies and retrieves a generic object that depends on the value of the [**ExpirationType**](expirationdata-expirationtype-property.md) property. The list below shows the **Value** for each **ExpirationType**.

<dt>

<span id="TemplateExpirationTypeNever"></span><span id="templateexpirationtypenever"></span><span id="TEMPLATEEXPIRATIONTYPENEVER"></span>

<span id="TemplateExpirationTypeNever"></span><span id="templateexpirationtypenever"></span><span id="TEMPLATEEXPIRATIONTYPENEVER"></span>**[**TemplateExpirationTypeNever**](constants-templateexpirationtypenever-property.md)** (0x1)


</dt> <dd>

**Null** (**Nothing**)

The content never expires.

</dd> <dt>

<span id="TemplateExpirationTypeOnDate"></span><span id="templateexpirationtypeondate"></span><span id="TEMPLATEEXPIRATIONTYPEONDATE"></span>

<span id="TemplateExpirationTypeOnDate"></span><span id="templateexpirationtypeondate"></span><span id="TEMPLATEEXPIRATIONTYPEONDATE"></span>**[**TemplateExpirationTypeOnDate**](constants-templateexpirationtypeondate-property.md)** (0x2)


</dt> <dd>

A **Date** value. You can use **Now** to specify the current date and time.

The content expires on the date specified.

</dd> <dt>

<span id="TemplateExpirationTypeUntilDays"></span><span id="templateexpirationtypeuntildays"></span><span id="TEMPLATEEXPIRATIONTYPEUNTILDAYS"></span>

<span id="TemplateExpirationTypeUntilDays"></span><span id="templateexpirationtypeuntildays"></span><span id="TEMPLATEEXPIRATIONTYPEUNTILDAYS"></span>**[**TemplateExpirationTypeUntilDays**](constants-templateexpirationtypeuntildays-property.md)** (0x3)


</dt> <dd>

An integer value that contains the number of days.

The content expires the specified number of days after the publishing date.

</dd> </dl>

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

[**ExpirationData**](expirationdata-object.md)
</dt> </dl>

 

 




