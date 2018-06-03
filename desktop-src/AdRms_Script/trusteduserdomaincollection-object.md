---
Description: Contains a collection of TrustedUserDomain objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 59bb6973-1b4e-4dc4-bba8-996c6c79fabc
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustedUserDomainCollection object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# TrustedUserDomainCollection object

The **TrustedUserDomainCollection** object contains a collection of [**TrustedUserDomain**](trusteduserdomain-object.md) objects. The collection enables AD RMS to process license requests from users whose rights account certificates (RACs) were issued by AD RMS installations in other forests. To import the external domains associated with another AD RMS installation, you can call the [**Import**](trusteduserdomaincollection-import-method.md) method and specify the external server licensor certificate. You can retrieve the collection by calling the [**TrustedUserDomains**](trustpolicy-trusteduserdomains-property.md) property on the [**TrustPolicy**](trustpolicy-object.md) object.

## Members

The **TrustedUserDomainCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **TrustedUserDomainCollection** object has these methods.



| Method                                                        | Description                                                                                                                                                          |
|:--------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Clear](http://go.microsoft.com/fwlink/p/?linkid=87270)       | Removes all objects from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                         |
| [Contains](http://go.microsoft.com/fwlink/p/?linkid=87271)    | Determines whether the collection contains a specific object (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                    |
| [CopyTo](http://go.microsoft.com/fwlink/p/?linkid=87281)      | Copies the collection elements to an array, starting at a specified index (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [**Import**](trusteduserdomaincollection-import-method.md)   | Imports external trusted user domains into the collection.<br/>                                                                                                |
| [IndexOf](http://go.microsoft.com/fwlink/p/?linkid=87273)     | Retrieves the index of a specific object in the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [**Refresh**](trusteduserdomaincollection-refresh-method.md) | Updates the current collection instance from the collection of trusted user domains on the server.<br/>                                                        |
| [Remove](http://go.microsoft.com/fwlink/p/?linkid=87276)      | Removes the first occurrence of the specified object from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>        |
| [RemoveAt](http://go.microsoft.com/fwlink/p/?linkid=87277)    | Removes the object at the specified index from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                   |



 

### Properties

The **TrustedUserDomainCollection** object has these properties.



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
' Retrieve trusted user domain collection.

SUB GetTrustedUsers()

  DIM trustPolicy
  DIM tudColl
  DIM Tud

  ' Retrieve the trust policy object.
  SET trustPolicy = config_manager.Enterprise.TrustPolicy
  CheckError()

  ' Retrieve the trusted user domain collection object.
  SET tudColl = trustPolicy.TrustedUserDomains
  CheckError()

  ' Remove all domains from the collection.
  tudColl.Clear()
  CheckError()

  ' Import new trusted user domains into the collection.
  SET Tud = tudColl.Import( "TUD_Name", _
                            "c:\certFile.bin", _
                            False)
  CheckError() 

  IF tudColl.Count < 1 OR IsNull(Tud.Id) THEN
    CALL RaiseError(-610, "Import failed.")
  END IF
 
  ' Remove the trusted user domain object.
  tudColl.Remove( Tud )
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

[**TrustedUserDomain**](trusteduserdomain-object.md)
</dt> </dl>

 

 




