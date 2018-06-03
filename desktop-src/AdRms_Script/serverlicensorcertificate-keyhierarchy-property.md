---
Description: Retrieves a value that identifies the certificate hierarchy in which the application is enrolled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f5726214-f9f3-4b01-bc3c-096108547779
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ServerLicensorCertificate.KeyHierarchy property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ServerLicensorCertificate.KeyHierarchy property

The **KeyHierarchy** property retrieves a value that identifies the certificate hierarchy in which the application is enrolled.

This property is read/write.

## Syntax


```VB
' Data type: 

ServerLicensorCertificate.KeyHierarchy
```



## Property value

This property returns one of the following integer values.

<dt>

<span id="KeyHierarchyOther"></span><span id="keyhierarchyother"></span><span id="KEYHIERARCHYOTHER"></span>

<span id="KeyHierarchyOther"></span><span id="keyhierarchyother"></span><span id="KEYHIERARCHYOTHER"></span>**[**KeyHierarchyOther**](constants-keyhierarchyother-property.md)** (0x3)


</dt> <dd>

The certificate hierarchy is not identified.

</dd> <dt>

<span id="KeyHierarchyPreproduction"></span><span id="keyhierarchypreproduction"></span><span id="KEYHIERARCHYPREPRODUCTION"></span>

<span id="KeyHierarchyPreproduction"></span><span id="keyhierarchypreproduction"></span><span id="KEYHIERARCHYPREPRODUCTION"></span>**[**KeyHierarchyPreproduction**](constants-keyhierarchypreproduction-property.md)** (0x1)


</dt> <dd>

Pre-production hierarchy.

</dd> <dt>

<span id="KeyHierarchyProduction"></span><span id="keyhierarchyproduction"></span><span id="KEYHIERARCHYPRODUCTION"></span>

<span id="KeyHierarchyProduction"></span><span id="keyhierarchyproduction"></span><span id="KEYHIERARCHYPRODUCTION"></span>**[**KeyHierarchyProduction**](constants-keyhierarchyproduction-property.md)** (0x2)


</dt> <dd>

Production hierarchy.

</dd> </dl>

## Remarks

For more information, see [Setting Up the Pre-production Development Environment](https://msdn.microsoft.com/library/cc542540) and [Certificate Hierarchy](https://msdn.microsoft.com/library/cc530431).

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

  ' Retrieve the certificate hierarchy.
  environment = slc.KeyHierarchy
  IF environment = preProd THEN
    CALL WScript.Echo("Environment = Pre-Production")
  ELSEIF environment = production THEN
    CALL WScript.Echo("Environment = Production")
  ELSE
    CALL WScript.Echo("Environment = Other")
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
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[**ServerLicensorCertificate**](serverlicensorcertificate-object.md)
</dt> </dl>

 

 




