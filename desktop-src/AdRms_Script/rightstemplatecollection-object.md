---
Description: Can be used to manage a collection of RightsTemplate objects that represent individual rights policy templates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 207ad6a5-7cd6-49e0-845d-2caddf20de0f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RightsTemplateCollection object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# RightsTemplateCollection object

The **RightsTemplateCollection** object can be used to manage a collection of [**RightsTemplate**](rightstemplate-object.md) objects that represent individual rights policy templates. Templates define content use rights and conditions for a set of users. You can retrieve the collection by calling the [**RightsTemplateCollection**](rightstemplatepolicy-rightstemplatecollection-property.md) property on the [**RightsTemplatePolicy**](rightstemplatepolicy-object.md) object.

## Members

The **RightsTemplateCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **RightsTemplateCollection** object has these methods.



| Method                                                     | Description                                                                                                                                                          |
|:-----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Add](http://go.microsoft.com/fwlink/p/?linkid=87269)      | Adds an object to the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                                |
| [Clear](http://go.microsoft.com/fwlink/p/?linkid=87270)    | Removes all objects from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                         |
| [Contains](http://go.microsoft.com/fwlink/p/?linkid=87271) | Determines whether the collection contains a specific object (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                    |
| [**Copy**](rightstemplatecollection-copy-method.md)       | Copies a rights template.<br/>                                                                                                                                 |
| [CopyTo](http://go.microsoft.com/fwlink/p/?linkid=87281)   | Copies the collection elements to an array, starting at a specified index (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [IndexOf](http://go.microsoft.com/fwlink/p/?linkid=87273)  | Retrieves the index of a specific object in the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Insert](http://go.microsoft.com/fwlink/p/?linkid=87274)   | Inserts an object in the collection at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [**Publish**](rightstemplatecollection-publish-method.md) | Identifies whether a template can be either published or archived.<br/>                                                                                        |
| [**Refresh**](rightstemplatecollection-refresh-method.md) | Refreshes the collection from the collection saved on the server.<br/>                                                                                         |
| [Remove](http://go.microsoft.com/fwlink/p/?linkid=87276)   | Removes the first occurrence of the specified object from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>        |
| [RemoveAt](http://go.microsoft.com/fwlink/p/?linkid=87277) | Removes the object at the specified index from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                   |
| [**Update**](rightstemplatecollection-update-method.md)   | Updates the template collection on the server database.<br/>                                                                                                   |



 

### Properties

The **RightsTemplateCollection** object has these properties.



| Property                                                           | Description                                                                                                                                            |
|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Count](http://go.microsoft.com/fwlink/p/?linkid=87280)<br/> | Retrieves the number of objects contained in the collection (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [Item](http://go.microsoft.com/fwlink/p/?linkid=87278)<br/>  | Specifies or retrieves the object at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>          |



 

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

  DIM templateMgr
  DIM templateColl
  DIM templateObj
  DIM summary
  DIM rights
  DIM appData
  DIM itemIndex

  ' Retrieve the RightsTemplatePolicy object.
  SET templateMgr = config_manager.RightsTemplatePolicy
  CheckError()
    
  ' Retrieve the template publishing path.
  CALL WScript.Echo("RightsTemplatePolicy.PublishingFilePath: " _
                    & templateMgr.PublishingFilePath)

  ' Clear the template collection.
  templateMgr.RightsTemplateCollection.Clear()
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
  SET appData = CreateObject( "Microsoft." _
    & "RightsManagementServices.Admin.ApplicationSpecificDataItem")
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
  SET templateColl = templateMgr.RightsTemplateCollection
  CheckError()

  ' Add the new template to the collection.
  CALL WScript.Echo("Add template to template collection...")
  itemIndex = templateColl.Add( templateObj )
  CheckError()

  ' Verify that the template was added. Because the collection
  ' was earlier cleared, it should contain only one template. 
  IF templateMgr.RightsTemplateCollection.Count <> 1 THEN
      CALL RaiseError(-401, "Fail to add RightsTemplate.")
  END IF

  ' Update the templates on the server with the template that
  ' you just added to the collection.
  SET firstObj = templateMgr.RightsTemplateCollection.Item(0)
  CheckError()
  templateMgr.RightsTemplateCollection.Update( firstObj )
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

 

 




