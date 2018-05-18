---
title: Set method of the PS\_DAOtpAuthentication class
description: Configures OTP authentication settings for DirectAccess.
audience: developer
ms.assetid: '2f9b1984-3c48-4119-a6d7-af6ebb5c7ebf'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, PS_DAOtpAuthentication class", "PS_DAOtpAuthentication class, Set method"]
topic_type:
- apiref
api_name:
- PS_DAOtpAuthentication.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Set method of the PS\_DAOtpAuthentication class

Configures OTP authentication settings for DirectAccess.

## Syntax


```mof
uint32 Set(
  [in]  string              ComputerName,
  [in]  string              CertificateTemplateName,
  [in]  string              CAServer[],
  [in]  string              UserSecurityGroupName,
  [in]  boolean             DisableTwoFactorBypass,
  [in]  boolean             PassThru,
  [in]  string              SigningCertificateTemplateName,
  [out] DAOtpAuthentication cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the name or IP address of the server on which the cmdlet should run.

</dd> <dt>

*CertificateTemplateName* \[in\]
</dt> <dd>

Specifies the name of the certificate template used for OTP.

</dd> <dt>

*CAServer* \[in\]
</dt> <dd>

Specifies CA servers that issue certificates for OTP authentication.

</dd> <dt>

*UserSecurityGroupName* \[in\]
</dt> <dd>

Specifies a security group containing users who are exempt from two-factor authentication.

</dd> <dt>

*DisableTwoFactorBypass* \[in\]
</dt> <dd>

Disables the option to allow users in a specific security group to be exempt from two-factor authentication, when two-factor authentication is enabled.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the [**DAOtpAuthentication**](daotpauthentication.md) object that contains the OTP authentication configuration settings for DirectAccess.

</dd> <dt>

*SigningCertificateTemplateName* \[in\]
</dt> <dd>

Specifies the name of the certificate template used to enroll the certificate used by Remote Access to sign certificates used for OTP authentication.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, contains a [**DAOtpAuthentication**](daotpauthentication.md) that describes the authentication settings.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAOtpAuthentication**](ps-daotpauthentication.md)
</dt> </dl>

 

 





