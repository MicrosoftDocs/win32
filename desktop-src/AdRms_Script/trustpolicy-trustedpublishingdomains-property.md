---
Description: 'Retrieves a collection of trusted publishing domain objects.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '6d704514-1688-4c07-a9e5-3d59aa686e27'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: 'TrustPolicy.TrustedPublishingDomains property'
---

# TrustPolicy.TrustedPublishingDomains property

The **TrustedPublishingDomains** property retrieves a collection of trusted publishing domain objects.

This property is read-only.

## Syntax


```VB
TrustPolicy.TrustedPublishingDomains
```



## Property value

This property returns a [**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md) object.

## Remarks

A trusted publishing domain contains the information necessary to enable an AD RMS server in one domain to issue end-user licenses for content that is published by an AD RMS server that resides in another domain under a different root of trust.

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

[**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md)
</dt> <dt>

[**TrustPolicy**](trustpolicy-object.md)
</dt> </dl>

 

 




