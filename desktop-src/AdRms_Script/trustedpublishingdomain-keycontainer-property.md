---
Description: Retrieves the name of the key container in the cryptographic service provider (CSP).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5f1fed4f-a714-4104-8133-60275f5f221a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustedPublishingDomain.KeyContainer property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TrustedPublishingDomain.KeyContainer property

The **KeyContainer** property retrieves the name of the key container in the cryptographic service provider (CSP).

This property is read-only.

## Syntax


```VB
TrustedPublishingDomain.KeyContainer
```



## Property value

This property returns a string value.

## Remarks

To import a trusted publishing domain, you must call the [**Import**](trustedpublishingdomaincollection-import-method.md) method on the [**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md) object and specify the name of an encrypted file that includes the private key used by the AD RMS server in that domain to sign end-user licenses. If the private key is not stored in hardware, it is stored in a key container in a CSP. You can call the [**CryptoSvcProvider**](trustedpublishingdomain-cryptosvcprovider-property.md) property to retrieve the name of the CSP.

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
  DIM Index

  ' Retrieve the trust policy object.
  SET trustPolicy = config_manager.Enterprise.TrustPolicy
  CheckError()

  ' Retrieve the trusted publishing domain collection object.
  SET TPDs = trustPolicy.TrustedPublishingDomains
  CheckError()

  ' Import a trusted publishing domain into the collection.
  SET TPD = TPDs.Import( "TPD_Name", _
                         "password", _
                         "c:\TPDfile.dat")
  CheckError()

  IF TPDs.Count < 1 OR IsNull(TPD.Id) THEN
    CALL RaiseError(-610, "Import failed.")
  END IF

  CALL WScript.Echo("Trusted publishing domain information: ")
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**TrustedPublishingDomain**](trustedpublishingdomain-object.md)
</dt> </dl>

 

 




