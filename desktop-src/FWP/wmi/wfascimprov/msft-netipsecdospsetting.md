---
description: Denial of Service Prevention Settings for IPsec.
ms.assetid: 53e414c1-aab1-468e-8795-2c63878ca4bb
title: MSFT\_NetIPsecDoSPSetting class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIPsecDoSPSetting
- MSFT_NetIPsecDoSPSetting.StateIdleTimeoutSeconds
- MSFT_NetIPsecDoSPSetting.PerIPRateLimitQueueIdleTimeoutSeconds
- MSFT_NetIPsecDoSPSetting.IpV6IPsecUnauthDscp
- MSFT_NetIPsecDoSPSetting.IpV6IPsecUnauthRateLimitBytesPerSec
- MSFT_NetIPsecDoSPSetting.IpV6IPsecUnauthPerIPRateLimitBytesPerSec
- MSFT_NetIPsecDoSPSetting.IpV6IPsecAuthDscp
- MSFT_NetIPsecDoSPSetting.IpV6IPsecAuthRateLimitBytesPerSec
- MSFT_NetIPsecDoSPSetting.IcmpV6Dscp
- MSFT_NetIPsecDoSPSetting.IcmpV6RateLimitBytesPerSec
- MSFT_NetIPsecDoSPSetting.IpV6FilterExemptDscp
- MSFT_NetIPsecDoSPSetting.IpV6FilterExemptRateLimitBytesPerSec
- MSFT_NetIPsecDoSPSetting.DefBlockExemptDscp
- MSFT_NetIPsecDoSPSetting.DefBlockExemptRateLimitBytesPerSec
- MSFT_NetIPsecDoSPSetting.MaxStateEntries
- MSFT_NetIPsecDoSPSetting.MaxPerIPRateLimitQueues
- MSFT_NetIPsecDoSPSetting.EnabledKeyingModules
- MSFT_NetIPsecDoSPSetting.FilteringFlags
- MSFT_NetIPsecDoSPSetting.PublicInterfaceAliases
- MSFT_NetIPsecDoSPSetting.PrivateInterfaceAliases
- MSFT_NetIPsecDoSPSetting.PublicV6Address
- MSFT_NetIPsecDoSPSetting.PrivateV6Address
- MSFT_NetIPsecDoSPSetting.EffectiveAddressFamily
- MSFT_NetIPsecDoSPSetting.InstanceID
- MSFT_NetIPsecDoSPSetting.Caption
- MSFT_NetIPsecDoSPSetting.Description
- MSFT_NetIPsecDoSPSetting.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIPsecDoSPSetting class

Denial of Service Prevention Settings for IPsec.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetIPsecDoSPSetting : MSFT_NetSettingData
{
  uint32 StateIdleTimeoutSeconds;
  uint32 PerIPRateLimitQueueIdleTimeoutSeconds;
  uint32 IpV6IPsecUnauthDscp;
  uint32 IpV6IPsecUnauthRateLimitBytesPerSec;
  uint32 IpV6IPsecUnauthPerIPRateLimitBytesPerSec;
  uint16 IpV6IPsecAuthDscp;
  uint32 IpV6IPsecAuthRateLimitBytesPerSec;
  uint16 IcmpV6Dscp;
  uint32 IcmpV6RateLimitBytesPerSec;
  uint32 IpV6FilterExemptDscp;
  uint32 IpV6FilterExemptRateLimitBytesPerSec;
  uint16 DefBlockExemptDscp;
  uint32 DefBlockExemptRateLimitBytesPerSec;
  uint32 MaxStateEntries;
  uint32 MaxPerIPRateLimitQueues;
  uint32 EnabledKeyingModules;
  uint32 FilteringFlags;
  string PublicInterfaceAliases[];
  string PrivateInterfaceAliases[];
  string PublicV6Address;
  string PrivateV6Address;
  uint16 EffectiveAddressFamily;
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT\_NetIPsecDoSPSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIPsecDoSPSetting** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used in CimInstance.ToString(). A short string for describing this instance when debugging.

</dd> <dt>

**DefBlockExemptDscp**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DSCP (RFC 2474) marking for inbound default-block exempted traffic. Value must be less than or equal to 63.

</dd> <dt>

**DefBlockExemptRateLimitBytesPerSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Rate limit for inbound default-block exempted traffic.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**EffectiveAddressFamily**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address family(or families) that are currently protected.

<dl> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>**IPv4** (1)
</dt> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>**IPv6** (2 )
</dt> </dl>

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**EnabledKeyingModules**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

One of the enabled keying modules.

<dl> <dt>

<span id="IkeV1"></span><span id="ikev1"></span><span id="IKEV1"></span>**IkeV1** (1)
</dt> <dt>

<span id="IkeV2"></span><span id="ikev2"></span><span id="IKEV2"></span>**IkeV2** (2)
</dt> <dt>

<span id="AuthIp"></span><span id="authip"></span><span id="AUTHIP"></span>**AuthIp** (4 )
</dt> </dl>

</dd> <dt>

**FilteringFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A bitwise combination of the filtering flags.

<dl> <dt>

<span id="DisableDefaultBlock"></span><span id="disabledefaultblock"></span><span id="DISABLEDEFAULTBLOCK"></span>**DisableDefaultBlock** (8)
</dt> <dt>

<span id="FilterBlock"></span><span id="filterblock"></span><span id="FILTERBLOCK"></span>**FilterBlock** (16)
</dt> <dt>

<span id="FilterExempt"></span><span id="filterexempt"></span><span id="FILTEREXEMPT"></span>**FilterExempt** (32 )
</dt> </dl>

</dd> <dt>

**IcmpV6Dscp**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DSCP (RFC 2474) marking for inbound ICMPv6 traffic. Value must be less than or equal to 63.

</dd> <dt>

**IcmpV6RateLimitBytesPerSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Rate limit for inbound ICMPv6 traffic.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that uniquely identifies this instance within the PolicyStore.

</dd> <dt>

**IpV6FilterExemptDscp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DSCP (RFC 2474) marking for inbound IPv6 filter exempted traffic. Value must be less than or equal to 63.

</dd> <dt>

**IpV6FilterExemptRateLimitBytesPerSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Rate limit for inbound IPv6 filter exempted traffic.

</dd> <dt>

**IpV6IPsecAuthDscp**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DSCP (RFC 2474) marking for authenticated inbound IPv6 IPsec traffic. Value must be less than or equal to 63.

</dd> <dt>

**IpV6IPsecAuthRateLimitBytesPerSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Rate limit for authenticated inbound IPv6 IPsec traffic.

</dd> <dt>

**IpV6IPsecUnauthDscp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DSCP (RFC 2474) marking for unauthenticated inbound IPv6 IPsec traffic. Value must be less than or equal to 63.

</dd> <dt>

**IpV6IPsecUnauthPerIPRateLimitBytesPerSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Per internal IP address rate limit for unauthenticated inbound IPv6 IPsec traffic.

</dd> <dt>

**IpV6IPsecUnauthRateLimitBytesPerSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Per internal IP address rate limit for unauthenticated inbound IPv6 IPsec traffic.

</dd> <dt>

**MaxPerIPRateLimitQueues**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of per internal IP address rate limit queues for inbound unauthenticated IPv6 IPsec traffic. Value must be greater than 0.

</dd> <dt>

**MaxStateEntries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of state entries in the table. Value must be greater than 0.

</dd> <dt>

**PerIPRateLimitQueueIdleTimeoutSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Per internal IP address rate limit queue idle timeout in seconds. Value must be greater than 0.

</dd> <dt>

**PrivateInterfaceAliases**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Private network interfaces.

</dd> <dt>

**PrivateV6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Optional private IPv6 address or subnet, for which this policy is specified.

</dd> <dt>

**PublicInterfaceAliases**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Public network aliases.

</dd> <dt>

**PublicV6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Optional public IPv6 address or subnet, for which this policy is specified.

</dd> <dt>

**StateIdleTimeoutSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

State entry idle timeout in seconds. Value must be greater than 0.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




