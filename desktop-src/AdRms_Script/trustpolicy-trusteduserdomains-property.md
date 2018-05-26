---
Description: Retrieves a collection of trusted user domain objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 813cecfb-5cc9-40bb-9033-63d04cde5e2d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustPolicy.TrustedUserDomains property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TrustPolicy.TrustedUserDomains property

The **TrustedUserDomains** property retrieves a collection of trusted user domain objects.

This property is read-only.

## Syntax


```VB
TrustPolicy.TrustedUserDomains
```



## Property value

This property returns a [**TrustedUserDomainCollection**](trusteduserdomaincollection-object.md) object.

## Remarks

The collection enables AD RMS to process license requests from users whose rights account certificates were issued by AD RMS installations in other forests.

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

[**TrustedUserDomainCollection**](trusteduserdomaincollection-object.md)
</dt> <dt>

[**TrustPolicy**](trustpolicy-object.md)
</dt> </dl>

 

 




