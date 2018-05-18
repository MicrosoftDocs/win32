---
title: DAOtpAuthentication class
description: Describes the DirectAccess OTP settings.
audience: developer
ms.assetid: 'f1186a77-410d-4c28-97a6-0267bbe8b003'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DAOtpAuthentication class", "DAOtpAuthentication class, described"]
topic_type:
- apiref
api_name:
- DAOtpAuthentication
- DAOtpAuthentication.OtpStatus
- DAOtpAuthentication.RadiusServer
- DAOtpAuthentication.UserSecurityGroupName
- DAOtpAuthentication.CAServers
- DAOtpAuthentication.CertificateTemplateName
- DAOtpAuthentication.SigningCertificateTemplateName
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# DAOtpAuthentication class

Describes the DirectAccess OTP settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAOtpAuthentication
{
  string OtpStatus;
  string RadiusServer[];
  string UserSecurityGroupName;
  string CAServers[];
  string CertificateTemplateName;
  string SigningCertificateTemplateName;
};
```

## Members

The **DAOtpAuthentication** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAOtpAuthentication** class has these properties.

<dl> <dt>

**CAServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The array of CA servers used for OTP authentication.

</dd> <dt>

**CertificateTemplateName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the OTP certificate template.

</dd> <dt>

**OtpStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether OTP authentication is enabled or disabled.

The possible values are:

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> <dt>

**RadiusServer**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPv4/IPv6 addresses or host names of RADIUS servers that are defined for OTP authentication.

</dd> <dt>

**SigningCertificateTemplateName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the certificate template used to enroll the certificate used by Remote Access to sign certificates used for OTP authentication.

</dd> <dt>

**UserSecurityGroupName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security group of users exempt from two-factor authentication.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





