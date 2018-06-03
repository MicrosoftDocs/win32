---
Description: Contains predefined constant values that can be used in various methods and properties to improve code readability.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 84f0f9a3-91e7-4407-a6db-5676b5e5c04d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Constants object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Constants object

The **Constants** object contains predefined constant values that can be used in various methods and properties to improve code readability. You can retrieve the object by calling the [**Constants**](configurationmanager-constants-property.md) property on the [**ConfigurationManager**](configurationmanager-object.md) object.

## Members

The **Constants** object has these types of members:

-   [Properties](#properties)

### Properties

The **Constants** object has these properties.



| Property                                                                                                 | Description                                                                                                      |
|:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**ClusterTypeCertification**](constants-clustertypecertification-property.md)<br/>               | Retrieves a value that specifies that an RMS cluster supports a certification service.<br/>                |
| [**ClusterTypeLicensing**](constants-clustertypelicensing-property.md)<br/>                       | Retrieves a value that specifies that an RMS cluster supports a licensing service.<br/>                    |
| [**ExcludedDomainUserType**](constants-excludeddomainusertype-property.md)<br/>                   | Retrieves a value that specifies a domain user account.<br/>                                               |
| [**ExcludedExternalUserType**](constants-excludedexternalusertype-property.md)<br/>               | Retrieves a value that specifies an external user account.<br/>                                            |
| [**ExcludedFederationUserType**](constants-excludedfederationusertype-property.md)<br/>           | Retrieves a value that specifies a federated user account.<br/>                                            |
| [**KeyHierarchyOther**](constants-keyhierarchyother-property.md)<br/>                             | Retrieves a value that specifies an undefined certificate hierarchy.<br/>                                  |
| [**KeyHierarchyPreproduction**](constants-keyhierarchypreproduction-property.md)<br/>             | Retrieves a value that specifies a Pre-production certificate hierarchy.<br/>                              |
| [**KeyHierarchyProduction**](constants-keyhierarchyproduction-property.md)<br/>                   | Retrieves a value that specifies a production certificate hierarchy.<br/>                                  |
| [**ProxySchemeBasic**](constants-proxyschemebasic-property.md)<br/>                               | Retrieves a value that specifies Basic authentication for a proxy server.<br/>                             |
| [**ProxySchemeDigest**](constants-proxyschemedigest-property.md)<br/>                             | Retrieves a value that specifies Digest authentication for a proxy server.<br/>                            |
| [**ProxySchemeWindowsIntegrated**](constants-proxyschemewindowsintegrated-property.md)<br/>       | Retrieves a value that specifies Windows Integrated authentication for a proxy server.<br/>                |
| [**RoleAdministrator**](constants-roleadministrator-property.md)<br/>                             | Retrieves a value that specifies administrator privileges.<br/>                                            |
| [**RoleAuditor**](constants-roleauditor-property.md)<br/>                                         | Retrieves a value that specifies auditor privileges.<br/>                                                  |
| [**RoleTemplateEditor**](constants-roletemplateeditor-property.md)<br/>                           | Retrieves a value that specifies template editor privileges.<br/>                                          |
| [**TemplateExpirationTypeNever**](constants-templateexpirationtypenever-property.md)<br/>         | Retrieves a value that specifies that protected content never expires.<br/>                                |
| [**TemplateExpirationTypeOnDate**](constants-templateexpirationtypeondate-property.md)<br/>       | Retrieves a value that specifies the date on which protected content expires.<br/>                         |
| [**TemplateExpirationTypeUntilDays**](constants-templateexpirationtypeuntildays-property.md)<br/> | Retrieves a value that specifies the number of days after publication that protected content expires.<br/> |
| [**TemplateRightAllowMacros**](constants-templaterightallowmacros-property.md)<br/>               | Retrieves a value that specifies a right to allow macros in content.<br/>                                  |
| [**TemplateRightEdit**](constants-templaterightedit-property.md)<br/>                             | Retrieves a value that specifies a right to edit content.<br/>                                             |
| [**TemplateRightExport**](constants-templaterightexport-property.md)<br/>                         | Retrieves a value that specifies a right to export content.<br/>                                           |
| [**TemplateRightExtract**](constants-templaterightextract-property.md)<br/>                       | Retrieves a value that specifies a right to extract content.<br/>                                          |
| [**TemplateRightForward**](constants-templaterightforward-property.md)<br/>                       | Retrieves a value that specifies a right to forward content.<br/>                                          |
| [**TemplateRightFullControl**](constants-templaterightfullcontrol-property.md)<br/>               | Retrieves a value that specifies a right to fully control content.<br/>                                    |
| [**TemplateRightPrint**](constants-templaterightprint-property.md)<br/>                           | Retrieves a value that specifies a right to print content.<br/>                                            |
| [**TemplateRightReply**](constants-templaterightreply-property.md)<br/>                           | Retrieves a value that specifies a right to reply to an email message.<br/>                                |
| [**TemplateRightReplyAll**](constants-templaterightreplyall-property.md)<br/>                     | Retrieves a value that specifies a right to reply all members identified in an email message.<br/>         |
| [**TemplateRightSave**](constants-templaterightsave-property.md)<br/>                             | Retrieves a value that specifies a right to save content.<br/>                                             |
| [**TemplateRightView**](constants-templaterightview-property.md)<br/>                             | Retrieves a value that specifies a right to view content.<br/>                                             |
| [**TemplateRightViewRights**](constants-templaterightviewrights-property.md)<br/>                 | Retrieves a value that specifies a right to view content rights.<br/>                                      |



 

## Examples


```VB
DIM config_manager
DIM admin_role
DIM constant

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

  ' Retrieve the Constants object.
  SET constant = config_manager.Constants

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

 

 




