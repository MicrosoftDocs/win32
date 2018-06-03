---
Description: Retrieves an ExpirationData object that specifies when protected content expires.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 41a5bc4d-0749-49ad-9cbc-bfbf727e87b8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ExpirationCondition.ExpirationData property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExpirationCondition.ExpirationData property

The **ExpirationData** property retrieves an [**ExpirationData**](expirationdata-object.md) object that specifies when protected content expires.

This property is read-only.

## Syntax


```VB
ExpirationCondition.ExpirationData
```



## Property value

This property returns an [**ExpirationData**](expirationdata-object.md) object. The property is read-only.

## Remarks

The [**ExpirationData**](expirationdata-object.md) object can be used to specify or retrieve the type of expiration period and the associated value.

| ExpirationData.ExpirationType                                                                       | ExpirationData.Value                                                        | Description                                                                 |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**TemplateExpirationTypeNever**](constants-templateexpirationtypenever-property.md) (0x1)         | **Null** (**Nothing**)                                                      | The content never expires.                                                  |
| [**TemplateExpirationTypeOnDate**](constants-templateexpirationtypeondate-property.md) (0x2)       | A **Date** value. You can use **Now** to specify the current date and time. | The content expires on the date specified.                                  |
| [**TemplateExpirationTypeUntilDays**](constants-templateexpirationtypeuntildays-property.md) (0x3) | An integer value that contains the number of days.                          | The content expires the specified number of days after the publishing date. |



 

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
</dt> <dt>

[**ExpirationData**](expirationdata-object.md)
</dt> </dl>

 

 




