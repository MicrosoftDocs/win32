---
Description: Exports trusted publishing domain data for the current AD RMS server to a file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bee822a3-dde5-445f-8959-623a4cd28363
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: TrustedPublishingDomainCollection.Export method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TrustedPublishingDomainCollection.Export method

The **Export** method exports trusted publishing domain data for the current AD RMS server to a file.

## Syntax


```VB
TrustedPublishingDomainCollection.Export( _
  ByVal certificateId, _
  ByVal password, _
  ByVal filePath, _
  ByVal v1Compatible _
)
```



## Parameters

<dl> <dt>

*certificateId* 
</dt> <dd>

An integer value that contains a unique ID for the trusted domain. You can call the [**Id**](trustedpublishingdomain-id-property.md) property to retrieve this value.

</dd> <dt>

*password* 
</dt> <dd>

A string value that contains the password used to encrypt the file identified by the *filePath* parameter.

</dd> <dt>

*filePath* 
</dt> <dd>

A string value that contains the path to the file to be created. For more information about the contents of this file, see Remarks.

</dd> <dt>

*v1Compatible* 
</dt> <dd>

A Boolean value that specifies whether the exported file will be used with AD RMS version 1.0 or version 2.0. Specify **False** if the file will only be used with version 2.0. When the value is **False**, a version 2.0 encryption algorithm is used to encrypt the file.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The trusted publishing domain contains information necessary to enable an AD RMS server that resides under a different root of trust than the current AD RMS server to issue end-user licenses for content that is published by the current server. The following items are included in the file:

-   The server licensor certificate
-   The private key used to sign end-user licenses
-   All rights policy templates

The **Export** method saves these items in a file and uses the password specified in the *password* parameter to encrypt the file. After you export the data, you must securely share the encrypted file and password so that the target RMS server can import it. For more information, see [**Import**](trustedpublishingdomaincollection-import-method.md).

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
  DIM objFileSys
  Dim Result

  ' Retrieve the trust policy object.
  SET trustPolicy = config_manager.Enterprise.TrustPolicy
  CheckError()

  ' Retrieve the trusted publishing domain collection object.
  SET TPDs = trustPolicy.TrustedPublishingDomains
  CheckError()

  ' Import a trusted publishing domain into the collection.
  SET TPD = TPDs.Import( "TPD_Name", _
                         "password"
                         "c:\TPDfile_Import.xml")
  CheckError()

  IF TPDs.Count < 1 OR IsNull(TPD.Id) THEN
    CALL RaiseError(-610, "Import failed.")
  END IF

  ' Export the trusted domain you just imported
  TPDs.Export(TPD.Id, "password", "c:\TPDfile_Export.xml", False);
  CheckError()

  ' Verify that the export file was created.
  Set objFileSys = CreateObject("Scripting.FileSystemObject")
  Result = objFileSys.FileExists("c:\TPDfile_Export.xml")
  IF result <> TRUE THEN
    CALL RaiseError(-650, "Export failed.")
  END IF

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

 

 




