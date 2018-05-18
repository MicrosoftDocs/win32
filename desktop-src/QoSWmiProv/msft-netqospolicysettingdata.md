---
Description: 'A QoS policy.'
ms.assetid: '3b172464-a565-4285-9253-2587569c7364'
title: 'MSFT\_NetQosPolicySettingData class'
---

# MSFT\_NetQosPolicySettingData class

A QoS policy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetQosCim")]
class MSFT_NetQosPolicySettingData : MSFT_NetSettingData
{
  string  Name;
  string  Version;
  string  Owner;
  uint32  NetworkProfile;
  uint32  Precedence;
  uint32  TemplateMatchCondition;
  string  UserMatchCondition;
  string  AppPathNameMatchCondition;
  uint32  IPProtocolMatchCondition;
  uint16  IPPortMatchCondition;
  string  IPSrcPrefixMatchCondition;
  uint16  IPSrcPortStartMatchCondition;
  uint16  IPSrcPortEndMatchCondition;
  string  IPDstPrefixMatchCondition;
  uint16  IPDstPortStartMatchCondition;
  uint16  IPDstPortEndMatchCondition;
  string  URIMatchCondition;
  boolean URIRecursiveMatchCondition;
  uint16  NetDirectPortMatchCondition;
  sint8   PriorityValue8021Action;
  sint8   DSCPAction;
  uint8   MinBandwidthWeightAction;
  uint64  ThrottleRateAction;
};
```

## Members

The **MSFT\_NetQosPolicySettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetQosPolicySettingData** class has these properties.

<dl> <dt>

**AppPathNameMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The application path name filter condition.

</dd> <dt>

**DSCPAction**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **MinValue** (-1), **MaxValue** (63)
</dt> </dl>

The DSCP action. Set to -1 if not used.

</dd> <dt>

**IPDstPortEndMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The upper-bound of the destination port filter condition. This field complements IPDstPortStartMatchCondition.

</dd> <dt>

**IPDstPortStartMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The optional lower-bound of the destination port filter condition. If only a single port value is required, then IPDstPortStartMatchCondition and IPDstPortEndMatchCondition must match. If the destination port filter condition is not required, set both fields to zero.

</dd> <dt>

**IPDstPrefixMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The optional destination IP prefix filter condition. Where applicable, both the source and destination prefix families must match. Examples of valid prefixes: 192.168.1.1, 192.168.1.0/24, or fe80::1001:2046/128

</dd> <dt>

**IPPortMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IP well-known port filter condition. This matches either the local port number or the remote port number of a supported IP connection. This type of filter is especially effective if the port number is a well-known number assigned by the IANA. If the value of this field is nonzero, then all the following fields are ignored: IPSrcPrefixMatchCondition, IPSrcPortStartMatchCondition, IPSrcPortEndMatchCondition, IPDstPrefixMatchCondition, IPDstPortMatchCondition, and IPDstPortEndMatchCondition.

</dd> <dt>

**IPProtocolMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IP protocol filter condition. If set to 0, then all the following fields are ignored: IPPortMatchCondition, IPSrcPrefixMatchCondition, IPSrcPortStartMatchCondition, IPSrcPortEndMatchCondition, IPDstPrefixMatchCondition, IPDstPrefixMatchCondition, and IPDstPortEndMatchCondition.

<dl> <dt>

<span id="N_A"></span><span id="n_a"></span>**N/A** (0)
</dt> <dt>

<span id="TCP"></span><span id="tcp"></span>**TCP** (1)
</dt> <dt>

<span id="UDP"></span><span id="udp"></span>**UDP** (2)
</dt> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (3)
</dt> </dl>

</dd> <dt>

**IPSrcPortEndMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The upper-bound of the source port filter condition. This field complements IPSrcPortStartMatchCondition.

</dd> <dt>

**IPSrcPortStartMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The optional lower-bound of the source port filter condition. If only a single port value is required, then IPSrcPortStartMatchCondition and IPSrcPortEndMatchCondition must match. If the source port filter condition is not required, set both fields to zero.

</dd> <dt>

**IPSrcPrefixMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The optional source IP prefix filter condition. Where applicable, both the source and destination prefix families must match. Examples of valid prefixes: 192.168.1.1, 192.168.1.0/24, or fe80::1001:2046/128

</dd> <dt>

**MinBandwidthWeightAction**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **MaxValue** (100)
</dt> </dl>

The minimum bandwidth weight action. Set to 0 if not used.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Policy name.

</dd> <dt>

**NetDirectPortMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The NetworkDirect port filter condition. This filter is only applicable if the Data Center Bridging server feature is installed. Otherwise, the policy is effectively no-op.

</dd> <dt>

**NetworkProfile**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The network profiles for which the policy applies.

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The owner of this policy.

</dd> <dt>

**Precedence**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **MinValue** (0), **MaxValue** (255)
</dt> </dl>

The precedence value of the policy.

</dd> <dt>

**PriorityValue8021Action**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **MinValue** (-1), **MaxValue** (7)
</dt> </dl>

The 802.1p priority action. Set to -1 if not used.

</dd> <dt>

**TemplateMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The optional match condition template that, if specified, overrides all other match conditions with predefined conditions. For example, the iSCSI template has a predefined match on TCP well-known port 3260.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (1)
</dt> <dt>

<span id="iSCSI"></span><span id="iscsi"></span><span id="ISCSI"></span>**iSCSI** (2)
</dt> <dt>

<span id="FCoE"></span><span id="fcoe"></span><span id="FCOE"></span>**FCoE** (3)
</dt> <dt>

<span id="SMB"></span><span id="smb"></span>**SMB** (4)
</dt> <dt>

<span id="NFS"></span><span id="nfs"></span>**NFS** (5)
</dt> <dt>

<span id="LiveMigration"></span><span id="livemigration"></span><span id="LIVEMIGRATION"></span>**LiveMigration** (6)
</dt> </dl>

</dd> <dt>

**ThrottleRateAction**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Units** ("Bytes per Second")
</dt> </dl>

The bandwidth throttle rate action in bytes per second unit. Set to 0 if not used.

</dd> <dt>

**URIMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The optional URI filter condition. This condition may only be combined with the URIRecursiveMatchCondition, IPDstAddressMatchCondition, IPDstPortStartMatchCondition, and IPDstPortEndMatchCondition fields.

</dd> <dt>

**URIRecursiveMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This filter condition supplements URIMatchCondition. If set, the URI match happens for all resources with the base path indicated by URIMatchCondition. Otherwise, a match only happens for a resource with the exact URI.

</dd> <dt>

**UserMatchCondition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user SID or name filter match condition.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Policy version if read from GPO.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>Qoswmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>QoSWmi.dll</dt> </dl> |



 

 




