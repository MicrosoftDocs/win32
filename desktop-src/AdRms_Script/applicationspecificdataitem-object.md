---
Description: 'Defines a name-value pair that can be added to a rights template and used by any AD RMS&\#8211;enabled application that understands it.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '50c210a8-e38f-472a-9c07-0d3899260bcf'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: ApplicationSpecificDataItem object
---

# ApplicationSpecificDataItem object

The **ApplicationSpecificDataItem** object defines a name-value pair that can be added to a rights template and used by any AD RMS–enabled application that understands it. The name-value pair can contain any information. It is not recognized by AD RMS but may be understood by an application that uses the template. A collection of these objects is contained in the [**ApplicationSpecificDataItemCollection**](applicationspecificdataitemcollection-object.md) object. You can retrieve the collection by calling the [**ApplicationSpecificDataItems**](rightstemplate-applicationspecificdataitems-property.md) property on the [**RightsTemplate**](rightstemplate-object.md) object.

## Members

The **ApplicationSpecificDataItem** object has these types of members:

-   [Properties](#properties)

### Properties

The **ApplicationSpecificDataItem** object has these properties.



| Property                                                               | Description                                                                 |
|:-----------------------------------------------------------------------|:----------------------------------------------------------------------------|
| [**Name**](applicationspecificdataitem-name-property.md)<br/>   | Specifies or retrieves the name portion of the name-value pair.<br/>  |
| [**Value**](applicationspecificdataitem-value-property.md)<br/> | Specifies or retrieves the value portion of the name-value pair.<br/> |



 

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
' Create a template and add it to the template collection. 

SUB ExcludeApplication()

  DIM templateMgr
  DIM templateColl
  DIM templateObj

  ' Retrieve the RightsTemplatePolicy object.
  SET templateMgr = config_manager.RightsTemplatePolicy
  CheckError()

  ' Retrieve the rights template collection.
  SET templateColl = templateMgr.RightsTemplateCollection
  CheckError()

  ' Retrieve the first template in the collection.
  SET templateObj = templateMgr.RightsTemplateCollection.Item(0)
  CheckError()

  ' Create and add a name-value pair to the template.
  SET appData = CreateObject( "Microsoft." _
      & "RightsManagementServices.Admin.ApplicationSpecificDataItem")
  appData.Name = "xxx"
  appData.Value = "yyy"
  templateObj.ApplicationSpecificDataItems.Add( appData )
  CheckError()

  ' Update the templates on the server.
  templateMgr.RightsTemplateCollection.Update( templateObj )
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

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> <dt>

[**ApplicationSpecificDataItemCollection**](applicationspecificdataitemcollection-object.md)
</dt> <dt>

[**RightsTemplate**](rightstemplate-object.md)
</dt> </dl>

 

 




