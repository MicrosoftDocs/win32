---
title: DAServerConfiguration class
description: DirectAccess Server Configuration.
audience: developer
ms.assetid: '712d8e0b-92fe-4f3a-890b-e7d8566a0f4c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DAServerConfiguration class", "DAServerConfiguration class, described"]
topic_type:
- apiref
api_name:
- DAServerConfiguration
- DAServerConfiguration.DAInstallType
- DAServerConfiguration.InternalIPv6Prefix
- DAServerConfiguration.ClientIPv6Prefix
- DAServerConfiguration.ConnectToAddress
- DAServerConfiguration.UserAuthentication
- DAServerConfiguration.IPsecRootCertificate
- DAServerConfiguration.IntermediateRootCertificate
- DAServerConfiguration.GpoName
- DAServerConfiguration.ComputerCertAuthentication
- DAServerConfiguration.TeredoState
- DAServerConfiguration.IsNatDeployed
- DAServerConfiguration.IsSingleNic
- DAServerConfiguration.HealthCheck
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# DAServerConfiguration class

DirectAccess Server Configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("2.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DAServerConfiguration
{
  string  DAInstallType;
  string  InternalIPv6Prefix[];
  string  ClientIPv6Prefix;
  string  ConnectToAddress;
  string  UserAuthentication;
  uint8   IPsecRootCertificate[];
  boolean IntermediateRootCertificate;
  string  GpoName;
  string  ComputerCertAuthentication;
  string  TeredoState;
  boolean IsNatDeployed;
  boolean IsSingleNic;
  string  HealthCheck;
};
```

## Members

The **DAServerConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **DAServerConfiguration** class has these properties.

<dl> <dt>

**ClientIPv6Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

IP-HTTPS Prefix

</dd> <dt>

**ComputerCertAuthentication**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether machine certificate is used to authenticate the DA client machine for the first IPsec tunnel

The possible values are.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> <dt>

**ConnectToAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether clients connect to the Direct Access server or NAT public address

</dd> <dt>

**DAInstallType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Tells whether DA is Installed in ManageOut-Mode or Full Mode

The possible values are.

<dt>

<span id="FullInstall"></span><span id="fullinstall"></span><span id="FULLINSTALL"></span>

**FullInstall** ("FullInstall")


</dt> <dd></dd> <dt>

<span id="ManageOut"></span><span id="manageout"></span><span id="MANAGEOUT"></span>

**ManageOut** ("ManageOut")


</dt> <dd></dd> </dl>

</dd> <dt>

**GpoName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the DA Server GPO

</dd> <dt>

**HealthCheck**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is not supported starting with Windows Server 2016.

**Windows Server 2012 R2 and Windows Server 2012:** Indicates whether health check for Direct Access clients is enabled.

The possible values are.

"Enabled"

"Disabled"

</dd> <dt>

**IntermediateRootCertificate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provisioning usage of Intermediate Certificate

</dd> <dt>

**InternalIPv6Prefix**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Corp IPv6 Prefixes

</dd> <dt>

**IPsecRootCertificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

IPsec certificate

</dd> <dt>

**IsNatDeployed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether NAT is deployed

</dd> <dt>

**IsSingleNic**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this is a Single Nic deployment

</dd> <dt>

**TeredoState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the state of Teredo on the DA Server

The possible values are.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> <dt>

**UserAuthentication**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Type of authentication

The possible values are.

<dt>

<span id="TwoFactor"></span><span id="twofactor"></span><span id="TWOFACTOR"></span>

**TwoFactor** ("TwoFactor")


</dt> <dd></dd> <dt>

<span id="UserPasswd"></span><span id="userpasswd"></span><span id="USERPASSWD"></span>

**UserPasswd** ("UserPasswd")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





