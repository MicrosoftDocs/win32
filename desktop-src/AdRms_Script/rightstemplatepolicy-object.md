---
Description: 'Can be used to retrieve a collection of rights policy templates and specify the shared folder through which those templates are distributed.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '4f83fc2e-3f49-4450-b5bf-168b9d88f0e1'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: RightsTemplatePolicy object
---

# RightsTemplatePolicy object

The **RightsTemplatePolicy** object can be used to retrieve a collection of rights policy templates and specify the shared folder through which those templates are distributed. This object is created when the [**Initialize**](configurationmanager-initialize-method.md) method on the [**ConfigurationManager**](configurationmanager-object.md) object is called if the role is TemplateEditor (0x2) or Administrator (0x4).

## Members

The **RightsTemplatePolicy** object has these types of members:

-   [Properties](#properties)

### Properties

The **RightsTemplatePolicy** object has these properties.



| Property                                                                                              | Description                                                                                                 |
|:------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**PublishingFilePath**](rightstemplatepolicy-publishingfilepath-property.md)<br/>             | Specifies or retrieves the UNC path for the folder where the rights policy templates are stored.<br/> |
| [**RightsTemplateCollection**](rightstemplatepolicy-rightstemplatecollection-property.md)<br/> | Retrieves a collection of rights policy templates.<br/>                                               |



 

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
' Retrieve a RightsTemplatePolicy object.

SUB TestRightsTemplate()

  DIM template_manager
  DIM templateColl
  DIM templateObj
  DIM summary
  DIM rights
  DIM appData
  DIM itemIndex
    
  SET template_manager = config_manager.RightsTemplatePolicy
  CheckError()
    
  ' Clear the template collection.
  template_manager.RightsTemplateCollection.Clear()
  CheckError()

  ' Add a template.
  SET templateObj = CreateObject( _
    "Microsoft.RightsManagementServices.Admin.RightsTemplate")
  CheckError()
    
  templateObj.RightsRequestUrl = "http://rms_test/"
  CheckError()
    
  ' Create a template summary.
  SET summary = CreateObject( _
    "Microsoft.RightsManagementServices.Admin.TemplateSummary")
  summary.LanguageId = 1033
  summary.Name = "Summary_Name"
  summary.Description = "Template_Description"
  templateObj.Summaries.Add( summary )
  CheckError()
    
  ' Create template rights.
  SET rights = CreateObject( _
    "Microsoft.RightsManagementServices.Admin.UserRightsItem")
  rights.WellKnownRights = _
    config_manager.Constants.TemplateRightExtract + _
    config_manager.Constants.TemplateRightPrint + _
    config_manager.Constants.TemplateRightForward
  rights.CustomRights.Add("CUSTOMRIGHTA")
  rights.CustomRights.Add("CUSTOMRIGHTB")
  Err.Clear()
  templateObj.UserRightsItems.Add( rights )
  CheckError()
    
  ' Create a template expiration condition.
  templateObj.ExpirationCondition.ExpirationData.ExpirationType = 2
  templateObj.ExpirationCondition.ExpirationData.Value = Now
  templateObj.ExpirationCondition.RenewalDays = 120
  CheckError()

  ' Create a template extended condition.
  templateObj.ExtendedCondition.EnableViewInTrustedBrowser = true
  templateObj.ExtendedCondition.EnableOnetimeLicense = true
  CheckError()
    
  ' Create an ApplicationSpecificDataItems object.
  SET appData = CreateObject( _
    "Microsoft.RightsManagementServices.Admin.ApplicationSpecificDataItem")
  appData.Name = "NOTE PAD"
  appData.Value = "Notepad.exe"
  templateObj.ApplicationSpecificDataItems.Add( appData )
  CheckError()
    
  ' Create a template revocation condition.
  templateObj.RevocationCondition.Url = "http://test"
  templateObj.RevocationCondition.RefreshPerDays = 30
  templateObj.RevocationCondition.PublicKeyFile = _
    "Rohita3SLCRevPublicKey.dat"
  CheckError()
    
  ' Create a template Collection.
  SET templateColl = template_manager.RightsTemplateCollection
  CheckError()
        
  ' Add the template to collection.
  itemIndex = templateColl.Add( templateObj )
  CheckError()
    
  ' Test for each template in the collection.
  template_manager.RightsTemplateCollection.Refresh()
    CheckError()
    
  IF template_manager.RightsTemplateCollection.Count <> 1 THEN
    CALL RaiseError(-401, "Fail to add RightsTemplate.")
  END IF

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

 

 




