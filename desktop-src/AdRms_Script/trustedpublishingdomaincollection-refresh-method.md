---
Description: Updates the current collection instance from the collection of trusted publishing domains on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5b04bcc0-185b-452f-bc7e-6a7122b0ce0c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustedPublishingDomainCollection.Refresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TrustedPublishingDomainCollection.Refresh method

The **Refresh** method updates the current collection instance from the collection of trusted publishing domains on the server.

## Syntax


```VB
TrustedPublishingDomainCollection.Refresh()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

All of the trusted publishing domains in the current collection object will be overwritten when you call this method. Use this method to refresh your collection to ensure that you have the latest updates made by other administrators.

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

  ' Refresh the current collection object.
  ' This call displays syntax. A refresh is not needed here.
  TPDs.Refresh()
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

[**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md)
</dt> </dl>

 

 




