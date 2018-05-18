---
title: VpnAuthProtocol class
description: Represents an authorization protocol for an site-to-site (S2S) VPN service.
audience: developer
ms.assetid: 'd086ef02-d7d6-4da3-ba77-77ddff8d75af'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VpnAuthProtocol class", "VpnAuthProtocol class, described"]
topic_type:
- apiref
api_name:
- VpnAuthProtocol
- VpnAuthProtocol.UserAuthProtocolAccepted
- VpnAuthProtocol.TunnelAuthProtocolsAdvertised
- VpnAuthProtocol.RootCertificateNameToAccept
- VpnAuthProtocol.CertificateAdvertised
- VpnAuthProtocol.CertificateEKUsToAccept
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# VpnAuthProtocol class

Represents an authorization protocol for an site-to-site (S2S) VPN service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnAuthProtocol
{
  string UserAuthProtocolAccepted[];
  string TunnelAuthProtocolsAdvertised;
  uint8  RootCertificateNameToAccept[];
  uint8  CertificateAdvertised[];
  string CertificateEKUsToAccept[];
};
```

## Members

The **VpnAuthProtocol** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnAuthProtocol** class has these properties.

<dl> <dt>

**CertificateAdvertised**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The certificate to send to peers.

</dd> <dt>

**CertificateEKUsToAccept**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of allowed Certificate EKUs

**Windows Server 2012:** This property is supported starting with Windows Server 2012 R2.

</dd> <dt>

**RootCertificateNameToAccept**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of the allowed root certificates

</dd> <dt>

**TunnelAuthProtocolsAdvertised**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The remote authentication method for the Routing and Remote Access Service (RRAS) server

</dd> <dt>

**UserAuthProtocolAccepted**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Array of the allowed local authentication protocols

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





