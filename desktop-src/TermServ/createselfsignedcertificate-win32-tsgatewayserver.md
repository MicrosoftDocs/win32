---
title: CreateSelfSignedCertificate method of the Win32_TSGatewayServer class
description: Creates a self-signed certificate and returns the certificate hash as an \ 0034;out \ 0034; parameter.
ms.assetid: 2a5b8dee-50b8-44b7-9e29-25aff1c40f5d
ms.tgt_platform: multiple
keywords:
- CreateSelfSignedCertificate method Remote Desktop Services
- CreateSelfSignedCertificate method Remote Desktop Services , Win32_TSGatewayServer class
- Win32_TSGatewayServer class Remote Desktop Services , CreateSelfSignedCertificate method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServer.CreateSelfSignedCertificate
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CreateSelfSignedCertificate method of the Win32\_TSGatewayServer class

Creates a self-signed certificate and returns the certificate hash as an "out" parameter. Also, adds the text "TS\_GATEWAY\_SELF\_SIGNED\_CERTIFICATE" to the certificate context property so that the certificate is recognized as a Remote Desktop Gateway (RD Gateway) certificate. This method uses an RD Gateway-specific key container to create the certificate.

## Syntax


```mof
uint32 CreateSelfSignedCertificate(
  [in]  string SubjectName,
  [out] uint8  CertHash[]
);
```



## Parameters

<dl> <dt>

*SubjectName* \[in\]
</dt> <dd>

Subject name of the self-signed certificate.

</dd> <dt>

*CertHash* \[out\]
</dt> <dd>

The certificate hash.

</dd> </dl>

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayServer**](win32-tsgatewayserver.md)
</dt> </dl>

 

