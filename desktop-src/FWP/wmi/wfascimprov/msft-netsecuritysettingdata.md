---
description: Global settings for IPsec.
ms.assetid: b053b16b-97ec-457f-92ed-e8051efe9177
title: MSFT\_NetSecuritySettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSecuritySettingData
- MSFT_NetSecuritySettingData.EnableStatefulFtp
- MSFT_NetSecuritySettingData.EnableStatefulPptp
- MSFT_NetSecuritySettingData.Profile
- MSFT_NetSecuritySettingData.CertValidationLevel
- MSFT_NetSecuritySettingData.MaxSAIdleTimeSeconds
- MSFT_NetSecuritySettingData.AllowIPsecThroughNAT
- MSFT_NetSecuritySettingData.KeyEncoding
- MSFT_NetSecuritySettingData.Exemptions
- MSFT_NetSecuritySettingData.RequireFullAuthSupport
- MSFT_NetSecuritySettingData.RemoteMachineTunnelAuthorizationList
- MSFT_NetSecuritySettingData.RemoteUserTunnelAuthorizationList
- MSFT_NetSecuritySettingData.RemoteMachineTransportAuthorizationList
- MSFT_NetSecuritySettingData.RemoteUserTransportAuthorizationList
- MSFT_NetSecuritySettingData.EnablePacketQueuing
- MSFT_NetSecuritySettingData.InstanceID
- MSFT_NetSecuritySettingData.Caption
- MSFT_NetSecuritySettingData.Description
- MSFT_NetSecuritySettingData.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetSecuritySettingData class

Global settings for IPsec.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetSecuritySettingData : MSFT_NetSettingData
{
  uint16 EnableStatefulFtp;
  uint16 EnableStatefulPptp;
  uint16 Profile;
  uint16 CertValidationLevel;
  uint32 MaxSAIdleTimeSeconds;
  uint16 AllowIPsecThroughNAT;
  uint16 KeyEncoding;
  uint32 Exemptions;
  uint16 RequireFullAuthSupport;
  string RemoteMachineTunnelAuthorizationList;
  string RemoteUserTunnelAuthorizationList;
  string RemoteMachineTransportAuthorizationList;
  string RemoteUserTransportAuthorizationList;
  uint16 EnablePacketQueuing;
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT\_NetSecuritySettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetSecuritySettingData** class has these properties.

<dl> <dt>

**AllowIPsecThroughNAT**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

When IPsec is in use, extra work is required to enable NAT traversal. This setting indicates on which side NAT traversal should be attempted.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>**Server** (1)
</dt> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (2)
</dt> <dt>

<span id="NotConfigured_"></span><span id="notconfigured_"></span><span id="NOTCONFIGURED_"></span>**NotConfigured** (65535 )
</dt> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used in CimInstance.ToString(). A short string for describing this instance when debugging.

</dd> <dt>

**CertValidationLevel**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies which kinds of certificate problems should cause a certificate to be rejected.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="Attempt_CRL_Check"></span><span id="attempt_crl_check"></span><span id="ATTEMPT_CRL_CHECK"></span>**Attempt CRL Check** (1)
</dt> <dt>

<span id="Require_CRL_Check"></span><span id="require_crl_check"></span><span id="REQUIRE_CRL_CHECK"></span>**Require CRL Check** (2)
</dt> <dt>

<span id="NotConfigured_"></span><span id="notconfigured_"></span><span id="NOTCONFIGURED_"></span>**NotConfigured** (65535 )
</dt> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**EnablePacketQueuing**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Toggle IPSec queuing of packets for RSS-like functionality

<dl> <dt>

<span id="NotConfigured"></span><span id="notconfigured"></span><span id="NOTCONFIGURED"></span>**NotConfigured** (0)
</dt> <dt>

<span id="Receive"></span><span id="receive"></span><span id="RECEIVE"></span>**Receive** (1)
</dt> <dt>

<span id="Forward_"></span><span id="forward_"></span><span id="FORWARD_"></span>**Forward** (2)
</dt> </dl>

</dd> <dt>

**EnableStatefulFtp**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to enable stateful FTP.

<dl> <dt>

<span id="False"></span><span id="false"></span><span id="FALSE"></span>**False** (0)
</dt> <dt>

<span id="True"></span><span id="true"></span><span id="TRUE"></span>**True** (1)
</dt> <dt>

<span id="NotConfigured_"></span><span id="notconfigured_"></span><span id="NOTCONFIGURED_"></span>**NotConfigured** (2 )
</dt> </dl>

</dd> <dt>

**EnableStatefulPptp**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to enable stateful PPTP.

<dl> <dt>

<span id="False"></span><span id="false"></span><span id="FALSE"></span>**False** (0)
</dt> <dt>

<span id="True"></span><span id="true"></span><span id="TRUE"></span>**True** (1)
</dt> <dt>

<span id="NotConfigured_"></span><span id="notconfigured_"></span><span id="NOTCONFIGURED_"></span>**NotConfigured** (2 )
</dt> </dl>

</dd> <dt>

**Exemptions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Traffic exemptions

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="NeighborDiscovery"></span><span id="neighbordiscovery"></span><span id="NEIGHBORDISCOVERY"></span>**NeighborDiscovery** (1)
</dt> <dt>

<span id="Icmp"></span><span id="icmp"></span><span id="ICMP"></span>**Icmp** (2)
</dt> <dt>

<span id="RouterDiscovery"></span><span id="routerdiscovery"></span><span id="ROUTERDISCOVERY"></span>**RouterDiscovery** (4)
</dt> <dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>**Dhcp** (8)
</dt> <dt>

<span id="NotConfigured"></span><span id="notconfigured"></span><span id="NOTCONFIGURED"></span>**NotConfigured** (4294967295)
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only

</dd> <dt>

**KeyEncoding**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

How to encode Pre-Shared Keys.

<dl> <dt>

<span id="UTF-16"></span><span id="utf-16"></span>**UTF-16** (0)
</dt> <dt>

<span id="UTF-8"></span><span id="utf-8"></span>**UTF-8** (1)
</dt> <dt>

<span id="NotConfigured_"></span><span id="notconfigured_"></span><span id="NOTCONFIGURED_"></span>**NotConfigured** (65535 )
</dt> </dl>

</dd> <dt>

**MaxSAIdleTimeSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum length of time, in seconds, that an SA may be idle before it will be torn down. 0 means Not Configured.

</dd> <dt>

**Profile**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current profile. This is only valid in the ActiveStore.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="Public"></span><span id="public"></span><span id="PUBLIC"></span>**Public** (0x4)
</dt> <dt>

<span id="Private"></span><span id="private"></span><span id="PRIVATE"></span>**Private** (0x2)
</dt> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>**Domain** (0x1)
</dt> <dt>

<span id="Not_Applicable_"></span><span id="not_applicable_"></span><span id="NOT_APPLICABLE_"></span>**Not Applicable** (0xffff )
</dt> </dl>

</dd> <dt>

**RemoteMachineTransportAuthorizationList**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SDDL for remote machine transport SA authorization

</dd> <dt>

**RemoteMachineTunnelAuthorizationList**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SDDL for remote machine tunnel SA authorization

</dd> <dt>

**RemoteUserTransportAuthorizationList**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SDDL for remote user transport SA authorization

</dd> <dt>

**RemoteUserTunnelAuthorizationList**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SDDL for remote user tunnel SA authorization

</dd> <dt>

**RequireFullAuthSupport**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Opportunistically match full auth set per key module

<dl> <dt>

<span id="False"></span><span id="false"></span><span id="FALSE"></span>**False** (0)
</dt> <dt>

<span id="True"></span><span id="true"></span><span id="TRUE"></span>**True** (1)
</dt> <dt>

<span id="NotConfigured_"></span><span id="notconfigured_"></span><span id="NOTCONFIGURED_"></span>**NotConfigured** (2 )
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




