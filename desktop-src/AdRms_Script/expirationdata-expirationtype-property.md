---
Description: 'Specifies or retrieves a value that identifies the expiration period for protected content.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '46bc55f8-96bc-47db-877d-d7da7062d3ac'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'ExpirationData.ExpirationType property'
---

# ExpirationData.ExpirationType property

The **ExpirationType** property specifies or retrieves a value that identifies the expiration period for protected content.

## Syntax


```VB
ExpirationData.ExpirationType
```



## Property value

This property specifies and returns one of the following integer values. You can use the integer or the associated value from the [**Constants**](constants-object.md) object.

<dt>



 (0x0)


</dt> <dd>

No expiration period is defined.

</dd> <dt>

<span id="TemplateExpirationTypeNever"></span><span id="templateexpirationtypenever"></span><span id="TEMPLATEEXPIRATIONTYPENEVER"></span>

<span id="TemplateExpirationTypeNever"></span><span id="templateexpirationtypenever"></span><span id="TEMPLATEEXPIRATIONTYPENEVER"></span>**[**TemplateExpirationTypeNever**](constants-templateexpirationtypenever-property.md)** (0x1)


</dt> <dd>

The content never expires.

</dd> <dt>

<span id="TemplateExpirationTypeOnDate"></span><span id="templateexpirationtypeondate"></span><span id="TEMPLATEEXPIRATIONTYPEONDATE"></span>

<span id="TemplateExpirationTypeOnDate"></span><span id="templateexpirationtypeondate"></span><span id="TEMPLATEEXPIRATIONTYPEONDATE"></span>**[**TemplateExpirationTypeOnDate**](constants-templateexpirationtypeondate-property.md)** (0x2)


</dt> <dd>

The content expires on the date specified by the [**Value**](expirationdata-value-property.md) property.

</dd> <dt>

<span id="TemplateExpirationTypeUntilDays"></span><span id="templateexpirationtypeuntildays"></span><span id="TEMPLATEEXPIRATIONTYPEUNTILDAYS"></span>

<span id="TemplateExpirationTypeUntilDays"></span><span id="templateexpirationtypeuntildays"></span><span id="TEMPLATEEXPIRATIONTYPEUNTILDAYS"></span>**[**TemplateExpirationTypeUntilDays**](constants-templateexpirationtypeuntildays-property.md)** (0x3)


</dt> <dd>

The content expires the specified number of days after publishing. For more information, see the [**Value**](expirationdata-value-property.md) property.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExpirationData**](expirationdata-object.md)
</dt> </dl>

 

 




