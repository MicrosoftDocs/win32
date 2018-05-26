---
Description: Imports an external trusted publishing domain into the collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9ab03770-e7aa-4f97-9203-294629df4fec
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustedPublishingDomainCollection.Import method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TrustedPublishingDomainCollection.Import method

The **Import** method imports an external trusted publishing domain into the collection.

## Syntax


```VB
TrustedPublishingDomainCollection.Import( _
  ByVal displayName, _
  ByVal password, _
  ByVal filePath _
)
```



## Parameters

<dl> <dt>

*displayName* 
</dt> <dd>

A string value that contains the display name of the password-protected file identified by the *filePath* parameter. For more information, see Remarks.

</dd> <dt>

*password* 
</dt> <dd>

A string value that contains the password used to encrypt the file identified by the *filePath* parameter. The string represents a Base64-encoded byte array that contains the password.

</dd> <dt>

*filePath* 
</dt> <dd>

The path to the file that contains the data necessary to add a trusted domain to the collection. For more information about the contents of this file, see Remarks.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

A trusted publishing domain contains the information necessary to enable an AD RMS server in one domain to issue end-user licenses for content that is published by an AD RMS server that resides in another domain under a different root of trust. The following items are imported:

-   The server licensor certificate
-   The private key used to sign end-user licenses
-   All rights policy templates

These items are saved in a password-protected file. The file and password must be securely shared to the current AD RMS server before the **Import** method can be called. The **Import** method automatically updates the collection on the server.

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md)
</dt> </dl>

 

 




