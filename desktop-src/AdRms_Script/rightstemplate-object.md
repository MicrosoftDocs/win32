---
Description: Can be used to manage a rights policy template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ea139d76-efbf-46f2-afea-7e8478ce0ec6
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RightsTemplate object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# RightsTemplate object

The **RightsTemplate** object can be used to manage a rights policy template. Templates identify rights and conditions that can be applied to AD RMS protected content, and they identify the users who can access the content. Different templates typically contain a different mix of rights or a different set of conditions. The following template elements can be defined by using the AD RMS Scripting API:

-   A collection of template names and descriptions with a different name-description pair for each locale ID (LCID) entered.
-   Users and groups that can be granted content licenses.
-   The rights granted to each user or user group.
-   The content expiration policy.
-   A set of extended policies.
-   A collection of application-specific name-value pairs.
-   The revocation policy for the template.
-   A revocation list.
-   A revocation list refresh interval.
-   A revocation list public key file.

Individual **RightsTemplate** objects can be retrieved from the [**RightsTemplateCollection**](rightstemplatecollection-object.md) object that is initialized from the existing templates on the server when the [**ConfigurationManager**](configurationmanager-object.md) object is initialized. You can create a new template by using the **CreateObject()** function or the [**Copy**](rightstemplatecollection-copy-method.md) method on the **RightsTemplateCollection** object.

## Members

The **RightsTemplate** object has these types of members:

-   [Properties](#properties)

### Properties

The **RightsTemplate** object has these properties.



| Property                                                                                                | Description                                                                                                                                                                            |
|:--------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ApplicationSpecificDataItems**](rightstemplate-applicationspecificdataitems-property.md)<br/> | Retrieves an [**ApplicationSpecificDataItemCollection**](applicationspecificdataitemcollection-object.md) object that contains application specific name-value pairs.<br/>      |
| [**Author**](rightstemplate-author-property.md)<br/>                                             | Retrieves the name of the individual who created or last updated the template.<br/>                                                                                              |
| [**CreatedTime**](rightstemplate-createdtime-property.md)<br/>                                   | Retrieves the date and time at which the template was created.<br/>                                                                                                              |
| [**ExpirationCondition**](rightstemplate-expirationcondition-property.md)<br/>                   | Retrieves an [**ExpirationCondition**](expirationcondition-object.md) object that identifies expiration policy for the content associated with the template.<br/>               |
| [**ExtendedCondition**](rightstemplate-extendedcondition-property.md)<br/>                       | Retrieves an [**ExtendedCondition**](extendedcondition-object.md) object that identifies additional policies that can be contained in the rights policy template.<br/>          |
| [**Id**](rightstemplate-id-property.md)<br/>                                                     | Retrieves a GUID for the template.<br/>                                                                                                                                          |
| [**IsPublished**](rightstemplate-ispublished-property.md)<br/>                                   | Retrieves a Boolean value that specifies whether the template can be exported.<br/>                                                                                              |
| [**RevocationCondition**](rightstemplate-revocationcondition-property.md)<br/>                   | Retrieves a [**RevocationCondition**](revocationcondition-object.md) object that contains revocation information for the template.<br/>                                         |
| [**RightsRequestUrl**](rightstemplate-rightsrequesturl-property.md)<br/>                         | Specifies and retrieves a URL that identifies the location used to respond to client rights requests.<br/>                                                                       |
| [**Summaries**](rightstemplate-summaries-property.md)<br/>                                       | Retrieves a [**TemplateSummaryCollection**](templatesummarycollection-object.md) object that contains descriptive information, in one or more languages, for the template.<br/> |
| [**UpdatedTime**](rightstemplate-updatedtime-property.md)<br/>                                   | Retrieves the date and time at which the template was last updated.<br/>                                                                                                         |
| [**UserRightsItems**](rightstemplate-userrightsitems-property.md)<br/>                           | Retrieves a [**UserRightsItemCollection**](userrightsitemcollection-object.md) object that contains a collection of user IDs and associated rights.<br/>                        |



 

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

SUB CreateRightsTemplate()

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
    
  ' Retrieve the template publishing path.
  CALL WScript.Echo("RightsTemplatePolicy.PublishingFilePath: " _
                    & template_manager.PublishingFilePath)

  ' Clear the template collection.
  template_manager.RightsTemplateCollection.Clear()
  CheckError()

  ' Create a template object and specify the request URL.
  SET templateObj = CreateObject( _
      "Microsoft.RightsManagementServices.Admin.RightsTemplate")
  templateObj.RightsRequestUrl = "http://rms_test/"
  CheckError()

  ' Create a template summary object.
  CALL WScript.Echo("Create a template summary.")
  SET summary = CreateObject( _
      "Microsoft.RightsManagementServices.Admin.TemplateSummary")
  summary.LanguageId = 1033
  summary.Name = "Scripting test template"
  summary.Description = "Scripting test template Desc"
  templateObj.Summaries.Add( summary )
  CheckError()
    
  ' Add rights to the template object.
  CALL WScript.Echo("Create template rights...")
  SET rights = CreateObject( _
      "Microsoft.RightsManagementServices.Admin.UserRightsItem")
  rights.UserId = "someone@example.com"
  rights.WellKnownRights = _
           config_manager.Constants.TemplateRightExtract + _
           config_manager.Constants.TemplateRightPrint + _
           config_manager.Constants.TemplateRightForward
  rights.CustomRights.Add("CUSTOMRIGHTA")
  rights.CustomRights.Add("CUSTOMRIGHTB")
  Err.Clear()
  templateObj.UserRightsItems.Add( rights )
  CheckError()

  ' Add an expiration condition.
  CALL WScript.Echo("Create template ExpirationCondition.")
  templateObj.ExpirationCondition.ExpirationData.ExpirationType = 2
  templateObj.ExpirationCondition.ExpirationData.Value = Now
  templateObj.ExpirationCondition.RenewalDays = 120
  CheckError()

  ' Add an extended condition.
  CALL WScript.Echo("Create template ExtendedCondition.")
  templateObj.ExtendedCondition.EnableViewInTrustedBrowser = true
  templateObj.ExtendedCondition.EnableOnetimeLicense = true
  CheckError()

  ' Identify an excluded application.
  CALL WScript.Echo("Create template ApplicationSpecificDataItems.")
  SET appData = CreateObject( _
      "Microsoft.RightsManagementServices.Admin.ApplicationSpecificDataItem")
  appData.Name = "NOTE PAD"
  appData.Value = "Notepad.exe"
  templateObj.ApplicationSpecificDataItems.Add( appData )
  CheckError()

  ' Add revocation information.
  CALL WScript.Echo("Create template RevocationCondition.")
  templateObj.RevocationCondition.Url = "http://test"
  templateObj.RevocationCondition.RefreshPerDays = 30
  templateObj.RevocationCondition.PublicKeyFile = "PublicKey.dat"
  CheckError()
  
  ' Retrieve the RightsTemplateCollection object.
  CALL WScript.Echo("Create template Collection.")
  SET templateColl = template_manager.RightsTemplateCollection
  CheckError()

  ' Add the new template to the collection.
  CALL WScript.Echo("Add template to template collection...")
  itemIndex = templateColl.Add( templateObj )
  CheckError()

  ' Verify that the template was added. Because the collection
  ' was earlier cleared, it should contain only one template. 
  IF template_manager.RightsTemplateCollection.Count <> 1 THEN
      CALL RaiseError(-401, "Fail to add RightsTemplate.")
  END IF

  ' Update the templates on the server with the template that
  ' you just added to the collection.
  SET firstObj = template_manager.RightsTemplateCollection.Item(0)
  CheckError()
  template_manager.RightsTemplateCollection.Update( firstObj )
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

[**ConfigurationManager**](configurationmanager-object.md)
</dt> <dt>

[**RightsTemplateCollection**](rightstemplatecollection-object.md)
</dt> </dl>

 

 




