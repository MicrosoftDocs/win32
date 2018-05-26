---
Description: Refreshes the collection from the collection saved on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5c09a91b-62fb-40ec-8d72-4376dd536621
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustedUserDomainCollectionRefresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TrustedUserDomainCollection::Refresh method

The **Refresh** method refreshes the collection from the collection saved on the server.

## Syntax


```VB
Sub Refresh()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

All of the trusted user domains in the current collection object will be overwritten when you call this method. Use this method to refresh your collection to ensure that you have the latest updates made by other administrators.

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

  ' Refresh the collection from the server.
  tudColl.Refresh()
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

[**TrustedUserDomain**](trusteduserdomain-object.md)
</dt> <dt>

[**TrustedUserDomainCollection**](trusteduserdomaincollection-object.md)
</dt> </dl>

 

 




