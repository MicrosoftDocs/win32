---
Description: 'Contains a collection of TrustedPublishingDomain objects.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'a1857449-84a0-40a2-8a95-16c586dbb23c'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: TrustedPublishingDomainCollection object
---

# TrustedPublishingDomainCollection object

The **TrustedPublishingDomainCollection** object contains a collection of [**TrustedPublishingDomain**](trustedpublishingdomain-object.md) objects. A trusted publishing domain contains the information necessary to enable an AD RMS server in one domain to issue end-user licenses for content that is published by an AD RMS server that resides in another domain under a different root of trust. This information includes the server licensor certificate, private signing key, and rights policy templates associated with the other server.

## Members

The **TrustedPublishingDomainCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **TrustedPublishingDomainCollection** object has these methods.



| Method                                                              | Description                                                                                                                                                          |
|:--------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Clear](http://go.microsoft.com/fwlink/p/?linkid=87270)             | Removes all objects from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                         |
| [Contains](http://go.microsoft.com/fwlink/p/?linkid=87271)          | Determines whether the collection contains a specific object (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                    |
| [CopyTo](http://go.microsoft.com/fwlink/p/?linkid=87281)            | Copies the collection elements to an array, starting at a specified index (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [**Export**](trustedpublishingdomaincollection-export-method.md)   | Exports the trusted publishing domain data for the current AD RMS server to a file.<br/>                                                                       |
| [**Import**](trustedpublishingdomaincollection-import-method.md)   | Imports an external trusted publishing domain into the collection.<br/>                                                                                        |
| [IndexOf](http://go.microsoft.com/fwlink/p/?linkid=87273)           | Retrieves the index of a specific object in the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [**Refresh**](trustedpublishingdomaincollection-refresh-method.md) | Updates the current collection instance from the collection of trusted publishing domains on the server.<br/>                                                  |
| [Remove](http://go.microsoft.com/fwlink/p/?linkid=87276)            | Removes the first occurrence of the specified object from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>        |
| [RemoveAt](http://go.microsoft.com/fwlink/p/?linkid=87277)          | Removes the object at the specified index from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                   |



 

### Properties

The **TrustedPublishingDomainCollection** object has these properties.



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
' Retrieve trusted publishing domain information.

SUB GetTPDInfo()

  DIM trustPolicy
  DIM TPDs
  DIM TPD

  ' Retrieve the trust policy object.
  SET trustPolicy = config_manager.Enterprise.TrustPolicy
  CheckError()

  ' Retrieve the trusted publishing domain collection object.
  SET TPDs = trustPolicy.TrustedPublishingDomains
  CheckError()

  ' Import a trusted publishing domain into the collection.
  SET TPD = TPDs.Import( "TPD_Name", _
                         "password"
                         "c:\TPDfile.xml")
  CheckError()

  IF TPDs.Count < 1 OR IsNull(TPD.Id) THEN
    CALL RaiseError(-610, "Import failed.")
  END IF

  CALL WScript.Echo("Trusted publishing domain information: ");
  CALL WScript.Echo("Display name = " & _
                    TPD.DisplayName)
  CALL WScript.Echo("Unique ID = " & _
                    TPD.Id)
  CALL WScript.Echo("Imported = " & _
                    TPD.IsImported)
  CALL WScript.Echo("CSP name = " & _
                    TPD.CryptoSvcProvider)
  CALL WScript.Echo("Key container name = " & _
                    TPD.KeyContainer)

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

[**TrustedPublishingDomain**](trustedpublishingdomain-object.md)
</dt> <dt>

[**TrustPolicy**](trustpolicy-object.md)
</dt> </dl>

 

 




