---
description: Represents a particular firewall profile. Multiple profiles may be in effect on any interface at any given time.
ms.assetid: 655385bd-9836-4645-b4b8-f61451e0a25f
title: MSFT\_NetFirewallProfile class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetFirewallProfile
- MSFT_NetFirewallProfile.Name
- MSFT_NetFirewallProfile.Enabled
- MSFT_NetFirewallProfile.DefaultInboundAction
- MSFT_NetFirewallProfile.DefaultOutboundAction
- MSFT_NetFirewallProfile.AllowInboundRules
- MSFT_NetFirewallProfile.AllowLocalFirewallRules
- MSFT_NetFirewallProfile.AllowLocalIPsecRules
- MSFT_NetFirewallProfile.AllowUserApps
- MSFT_NetFirewallProfile.AllowUserPorts
- MSFT_NetFirewallProfile.AllowUnicastResponseToMulticast
- MSFT_NetFirewallProfile.NotifyOnListen
- MSFT_NetFirewallProfile.LogFileName
- MSFT_NetFirewallProfile.LogMaxSizeKilobytes
- MSFT_NetFirewallProfile.LogAllowed
- MSFT_NetFirewallProfile.LogBlocked
- MSFT_NetFirewallProfile.LogIgnored
- MSFT_NetFirewallProfile.DisabledInterfaceAliases
- MSFT_NetFirewallProfile.EnableStealthModeForIPsec
- MSFT_NetFirewallProfile.InstanceID
- MSFT_NetFirewallProfile.Caption
- MSFT_NetFirewallProfile.Description
- MSFT_NetFirewallProfile.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetFirewallProfile class

Represents a particular firewall profile. Multiple profiles may be in effect on any interface at any given time.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetFirewallProfile : CIM_ManagedElement
{
  string Name;
  uint16 Enabled;
  uint16 DefaultInboundAction;
  uint16 DefaultOutboundAction;
  uint16 AllowInboundRules;
  uint16 AllowLocalFirewallRules;
  uint16 AllowLocalIPsecRules;
  uint16 AllowUserApps;
  uint16 AllowUserPorts;
  uint16 AllowUnicastResponseToMulticast;
  uint16 NotifyOnListen;
  string LogFileName;
  uint64 LogMaxSizeKilobytes;
  uint16 LogAllowed;
  uint16 LogBlocked;
  uint16 LogIgnored;
  string DisabledInterfaceAliases[];
  uint16 EnableStealthModeForIPsec;
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT\_NetFirewallProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetFirewallProfile** class has these properties.

<dl> <dt>

**AllowInboundRules**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this is true, administrators will be able to create firewall rules which allow unsolicited inbound traffic to be accepted. If this is false, such rules will be ignored.

</dd> <dt>

**AllowLocalFirewallRules**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Determines whether local firewall rules should be merged into the effective policy along with Group Policy settings.

</dd> <dt>

**AllowLocalIPsecRules**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Determines whether local IPsec rules should be merged into the effective policy along with rules from Group Policy.

</dd> <dt>

**AllowUnicastResponseToMulticast**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to allow unicast responses to multicast traffic.

</dd> <dt>

**AllowUserApps**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to respect user allowed applications created in the legacy firewall.

</dd> <dt>

**AllowUserPorts**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to respect globally opened ports created in the legacy firewall.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used in CimInstance.ToString(). A short string for describing this instance when debugging.

</dd> <dt>

**DefaultInboundAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The default action for Inbound traffic.

</dd> <dt>

**DefaultOutboundAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The default action for outbound traffic.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**DisabledInterfaceAliases**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Interfaces that the firewall profile is disabled on.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the firewall is enabled on this profile.

</dd> <dt>

**EnableStealthModeForIPsec**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to use Stealth Mode for IPsec-protected traffic.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

Reserved for internal use by the WMI provider only

</dd> <dt>

**LogAllowed**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to log allowed packets.

</dd> <dt>

**LogBlocked**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to log blocked traffic.

</dd> <dt>

**LogFileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The filename in which to store the firewall log.

</dd> <dt>

**LogIgnored**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to log an event when rules are ignored.

</dd> <dt>

**LogMaxSizeKilobytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum size the log file can reach before being rotated. May be a **uint32** value, or **MAXUINT64** for Not Configured.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the profile.

</dd> <dt>

**NotifyOnListen**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If true, users will be notified when an application listens on a port that is closed.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




