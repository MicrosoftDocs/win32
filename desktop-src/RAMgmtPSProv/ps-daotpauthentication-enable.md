---
title: Enable method of the PS\_DAOtpAuthentication class
description: Enables and configures OTP authentication for DirectAccess users.
audience: developer
ms.assetid: a768b45b-65d7-4197-ac80-ddf5d5c24fe7
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Enable method
- Enable method, PS_DAOtpAuthentication class
- PS_DAOtpAuthentication class, Enable method
topic_type:
- apiref
api_name:
- PS_DAOtpAuthentication.Enable
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enable method of the PS\_DAOtpAuthentication class

Enables and configures OTP authentication for DirectAccess users.

## Syntax


```mof
uint32 Enable(
  [in]  string              RadiusServer,
  [in]  string              ComputerName,
  [in]  uint16              RadiusPort,
  [in]  string              CAServer[],
  [in]  string              CertificateTemplateName,
  [in]  string              SharedSecret,
  [in]  string              UserSecurityGroupName,
  [in]  boolean             Force,
  [in]  boolean             PassThru,
  [in]  string              SigningCertificateTemplateName,
  [out] DAOtpAuthentication cmdletOutput
);
```



## Parameters

<dl> <dt>

*RadiusServer* \[in\]
</dt> <dd>

Specifies the FQDN or IP address (IPv4 or IPv6) of the RADIUS server used for OTP authentication.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the name or IP address of the server on which the cmdlet should run.

</dd> <dt>

*RadiusPort* \[in\]
</dt> <dd>

Specifies the RADIUS server port listening for authentication requests.

</dd> <dt>

*CAServer* \[in\]
</dt> <dd>

Specifies CA servers that issue certificates for OTP authentication. Specify a server in the format CAServer\_Name\\CAService\_Name.

</dd> <dt>

*CertificateTemplateName* \[in\]
</dt> <dd>

Specifies the name of the certificate template used for OTP certificate enrollment.

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Specifies the shared password used for communications between the Remote Access server and the RADIUS server.

</dd> <dt>

*UserSecurityGroupName* \[in\]
</dt> <dd>

Specifies the security group containing users who are exempt from two-factor authentication.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Turns off the option that allows a user to confirm or cancel an action initiated by the cmdlet.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the DAOtpAuthentication object that contains OTP authentication configuration settings for DirectAccess.

</dd> <dt>

*SigningCertificateTemplateName* \[in\]
</dt> <dd>

Specifies the name of the certificate template used to enroll the certificate used by Remote Access to sign certificates used for OTP authentication.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, contains a [**DAOtpAuthentication**](daotpauthentication.md) that contains the OTP authentication configuration settings.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAOtpAuthentication**](ps-daotpauthentication.md)
</dt> </dl>

 

 





