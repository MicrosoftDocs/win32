---
Description: 'Is the top-level object in the AD RMS scripting API.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '14b32192-da9d-4521-9d1c-5d29e64e9f76'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: ConfigurationManager object
---

# ConfigurationManager object

The **ConfigurationManager** object is the top-level object in the AD RMS scripting API. It can be used to initiate a connection with the AD RMS server and to retrieve the following objects:

-   [**AuditReport**](auditreport-object.md)
-   [**Constants**](constants-object.md)
-   [**ClusterInformation**](clusterinformation-object.md)
-   [**Enterprise**](enterprise-object.md)
-   [**RightsTemplatePolicy**](rightstemplatepolicy-object.md)
-   [**ServiceIdentity**](serviceidentity-object.md)

## Members

The **ConfigurationManager** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ConfigurationManager** object has these methods.



| Method                                                       | Description                                                                                                               |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| [**Initialize**](configurationmanager-initialize-method.md) | Initializes the administration environment, connects to the AD RMS server, and retrieves the appropriate role.<br/> |
| [**IsInRoles**](configurationmanager-isinroles-method.md)   | Retrieves a Boolean value that specifies whether a role is permitted.<br/>                                          |



 

### Properties

The **ConfigurationManager** object has these properties.



| Property                                                                                          | Description                                                                                                                                           |
|:--------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AuditReport**](configurationmanager-auditreport-property.md)<br/>                       | Retrieves an [**AuditReport**](auditreport-object.md) object that can be used to obtain the number of federated and domain user accounts.<br/> |
| [**ClusterInformation**](configurationmanager-clusterinformation-property.md)<br/>         | Retrieves a [**ClusterInformation**](clusterinformation-object.md) object that contains cluster configuration information.<br/>                |
| [**Constants**](configurationmanager-constants-property.md)<br/>                           | Retrieves a [**Constants**](constants-object.md) object that contains common constant values supported by the AD RMS service.<br/>             |
| [**Enterprise**](configurationmanager-enterprise-property.md)<br/>                         | Retrieves an [**Enterprise**](enterprise-object.md) object that can be used for enterprise administration.<br/>                                |
| [**IsServerOnLocalMachine**](configurationmanager-isserveronlocalmachine-property.md)<br/> | Retrieves a Boolean value that specifies whether the client and server are on the same computer.<br/>                                           |
| [**RightsTemplatePolicy**](configurationmanager-rightstemplatepolicy-property.md)<br/>     | Retrieves a [**RightsTemplatePolicy**](rightstemplatepolicy-object.md) object that can be used to manage AD RMS rights templates.<br/>         |
| [**Roles**](configurationmanager-roles-property.md)<br/>                                   | Retrieves a value that identifies the role.<br/>                                                                                                |
| [**ServiceIdentity**](configurationmanager-serviceidentity-property.md)<br/>               | Retrieves a [**ServiceIdentity**](serviceidentity-object.md) object that can be used to manage an AD RMS service account.<br/>                 |



 

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
</dt> </dl>

 

 




