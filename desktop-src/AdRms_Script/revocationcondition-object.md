---
Description: Contains the revocation policy for a rights policy template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bf4b674a-9e14-444d-9928-460f6ede59ff
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RevocationCondition object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# RevocationCondition object

The **RevocationCondition** object contains the revocation policy for a rights policy template. Revocation is implemented by using revocation lists that are distributed to client computers by an administrator and to a public location such as a web server. Each list is a signed XrML file that specifies the content, application, user, or other principal that has been revoked.

When the user of an RMS-enabled application attempts to open protected content, the application sends a binding request to the AD RMS software installed on the client computer. The AD RMS client:

-   Evaluates the use license for revocation list requirements.
-   Retrieves the list locally or from the public URL.
-   Determines whether the list is current.
-   Verifies that the list signer is identified in the license as a principal that can revoke the license.
-   Determines whether any principals involved in the initial binding requests have been revoked.
-   Verifies the revocation list signature by using the associated public key.

If any of these steps fail, the binding request is denied. You can use the **RevocationCondition** object to specify the public URL and identify a file that contains the public key. The object can be retrieved by calling the [**RevocationCondition**](rightstemplate-revocationcondition-property.md) property on the [**RightsTemplate**](rightstemplate-object.md) object.

## Members

The **RevocationCondition** object has these types of members:

-   [Properties](#properties)

### Properties

The **RevocationCondition** object has these properties.



| Property                                                                         | Description                                                                                                                         |
|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [**PublicKeyFile**](revocationcondition-publickeyfile-property.md)<br/>   | Specifies the path of the file that contains the public key associated with the private key that signed revocation list.<br/> |
| [**RefreshPerDays**](revocationcondition-refreshperdays-property.md)<br/> | Specifies or retrieves the maximum number of days after a revocation list has been created before it must be refreshed.<br/>  |
| [**Url**](revocationcondition-url-property.md)<br/>                       | Specifies or retrieves the URL or UNC path from which the revocation list can be obtained.<br/>                               |



 

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
' Add revocation information to a template. 

SUB AddRevocation()

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

  ' Retrieve the rights template collection.
  SET templateColl = template_manager.RightsTemplateCollection
  CheckError()

  ' Retrieve the first template in the collection.
  SET templateObj = template_manager.RightsTemplateCollection.Item(0)
  CheckError()
    
  ' Add revocation information to the first template.
  templateObj.RevocationCondition.Url = "http://test"
  templateObj.RevocationCondition.RefreshPerDays = 30
  templateObj.RevocationCondition.PublicKeyFile = "PublicKey.dat"
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
</dt> <dt>

[**RightsTemplate**](rightstemplate-object.md)
</dt> </dl>

 

 




