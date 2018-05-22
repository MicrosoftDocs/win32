---
Description: 'Can be used to manage the AD RMS server licensor certificate.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '18809d67-87dc-4b4c-8e09-b5fdd522a8c3'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: ServerLicensorCertificate object
---

# ServerLicensorCertificate object

The **ServerLicensorCertificate** object can be used to manage the AD RMS server licensor certificate. You can retrieve this object by calling the [**ServerLicensorCertificate**](enterprise-serverlicensorcertificate-property.md) property on the [**Enterprise**](enterprise-object.md) object.

The server licensor certificate is the certificate that signs all licenses and certificates granted by the AD RMS cluster. The certificate can be exported to establish trust with other clusters.

The Microsoft Enrollment Service distributes a server licensor certificate when you deploy AD RMS and provision a root certification server. The certificate is signed by the enrollment service and contains the public key of the root certification server. When you add a licensing server, it is also issued a server licensor certificate, but the certificate is signed by the root certification server.

The following rights can be granted by server licensor certificates. The rights that can be granted depend on the type of server for which the certificate is issued.

| Right                                          | When issued to a root certification server | When issued to a licensing server |
|------------------------------------------------|--------------------------------------------|-----------------------------------|
| Issue rights account certificates              | Yes                                        | No                                |
| Issue publishing licenses                      | Yes                                        | Yes                               |
| Issue use licenses                             | Yes                                        | Yes                               |
| Issue subordinate server licensor certificates | Yes                                        | No                                |
| Issue client licensor certificates             | Yes                                        | Yes                               |



 

## Members

The **ServerLicensorCertificate** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ServerLicensorCertificate** object has these methods.



| Method                                             | Description                                      |
|:---------------------------------------------------|:-------------------------------------------------|
| [**Export**](serverlicensorcertificate-export.md) | Distributes the licensor certificate.<br/> |



 

### Properties

The **ServerLicensorCertificate** object has these properties.



| Property                                                                           | Description                                                                                                  |
|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| [**FriendlyName**](serverlicensorcertificate-friendlyname-property.md)<br/> | Specifies or retrieves the certificate display name.<br/>                                              |
| [**KeyHierarchy**](serverlicensorcertificate-keyhierarchy-property.md)<br/> | Retrieves a value that identifies the certificate hierarchy in which the application is enrolled.<br/> |



 

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
' Retrieve the server licensor certificate.

SUB GetSLC()

  DIM slc
  DIM environment
  DIM preProd
  DIM production

  production = config_manager.Constants.KeyHierarchyProduction
  preProd = config_manager.Constants.KeyHierarchyPreproduction

  ' Retrieve the ServerLicensorCertificate object.
  SET slc = config_manager.Enterprise.ServerLicensorCertificate
  CheckError()

  ' Retrieve the certificate display name.
  CALL WScript.Echo("SLC name: " & slc.FriendlyName)

  ' Retrieve the certificate hierarchy.
  environment = slc.KeyHierarchy
  IF environment = preProd THEN
    CALL WScript.Echo("Environment = Pre-Production")
  ELSEIF environment = production THEN
    CALL WScript.Echo("Environment = Production")
  ELSE
    CALL WScript.Echo("Environment = Other")
  END IF

  ' Export the server licensor certificate.
  slc.Export("c:\Cert.tmp")

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
</dt> </dl>

 

 




