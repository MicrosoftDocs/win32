---
description: A Connection Security Rule.
ms.assetid: b418de78-1e79-4048-81ad-8f1809038cd7
title: MSFT\_NetConSecRule class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRule
- MSFT_NetConSecRule.Mode
- MSFT_NetConSecRule.AllowSetKey
- MSFT_NetConSecRule.AllowWatchKey
- MSFT_NetConSecRule.MaxReturnPathLifetimeSeconds
- MSFT_NetConSecRule.InboundSecurity
- MSFT_NetConSecRule.OutboundSecurity
- MSFT_NetConSecRule.KeyModule
- MSFT_NetConSecRule.RequireAuthorization
- MSFT_NetConSecRule.Users
- MSFT_NetConSecRule.Machines
- MSFT_NetConSecRule.LocalTunnelEndpoint
- MSFT_NetConSecRule.RemoteTunnelEndpointDNSName
- MSFT_NetConSecRule.RemoteTunnelEndpoint
- MSFT_NetConSecRule.BypassTunnelIfEncrypted
- MSFT_NetConSecRule.Platforms
- MSFT_NetConSecRule.RuleGroup
- MSFT_NetConSecRule.DisplayGroup
- MSFT_NetConSecRule.Profiles
- MSFT_NetConSecRule.MainModeCryptoSet
- MSFT_NetConSecRule.QuickModeCryptoSet
- MSFT_NetConSecRule.Phase1AuthSet
- MSFT_NetConSecRule.Phase2AuthSet
- MSFT_NetConSecRule.PrimaryStatus
- MSFT_NetConSecRule.StatusCode
- MSFT_NetConSecRule.Status
- MSFT_NetConSecRule.EnforcementStatus
- MSFT_NetConSecRule.PolicyStoreSourceType
- MSFT_NetConSecRule.PolicyStoreSource
- MSFT_NetConSecRule.SystemCreationClassName
- MSFT_NetConSecRule.SystemName
- MSFT_NetConSecRule.CreationClassName
- MSFT_NetConSecRule.PolicyRuleName
- MSFT_NetConSecRule.ConditionListType
- MSFT_NetConSecRule.RuleUsage
- MSFT_NetConSecRule.Priority
- MSFT_NetConSecRule.Mandatory
- MSFT_NetConSecRule.SequencedActions
- MSFT_NetConSecRule.ExecutionStrategy
- MSFT_NetConSecRule.PolicyDecisionStrategy
- MSFT_NetConSecRule.PolicyRoles
- MSFT_NetConSecRule.Enabled
- MSFT_NetConSecRule.CommonName
- MSFT_NetConSecRule.PolicyKeywords
- MSFT_NetConSecRule.InstanceID
- MSFT_NetConSecRule.Caption
- MSFT_NetConSecRule.DisplayName
- MSFT_NetConSecRule.Description
- MSFT_NetConSecRule.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetConSecRule class

A Connection Security Rule.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetConSecRule : MSFT_NetSARule
{
  uint16  Mode;
  boolean AllowSetKey;
  boolean AllowWatchKey;
  uint32  MaxReturnPathLifetimeSeconds;
  uint16  InboundSecurity;
  uint16  OutboundSecurity;
  uint16  KeyModule;
  boolean RequireAuthorization;
  string  Users;
  string  Machines;
  string  LocalTunnelEndpoint[];
  string  RemoteTunnelEndpointDNSName;
  string  RemoteTunnelEndpoint[];
  boolean BypassTunnelIfEncrypted;
  string  Platforms[];
  string  RuleGroup;
  string  DisplayGroup;
  uint16  Profiles;
  string  MainModeCryptoSet;
  string  QuickModeCryptoSet;
  string  Phase1AuthSet;
  string  Phase2AuthSet;
  uint16  PrimaryStatus;
  uint32  StatusCode;
  string  Status;
  uint16  EnforcementStatus[];
  uint16  PolicyStoreSourceType;
  string  PolicyStoreSource;
  string  SystemCreationClassName;
  string  SystemName;
  string  CreationClassName;
  string  PolicyRuleName;
  uint16  ConditionListType;
  string  RuleUsage;
  uint16  Priority;
  boolean Mandatory;
  uint16  SequencedActions;
  uint16  ExecutionStrategy;
  uint16  PolicyDecisionStrategy;
  string  PolicyRoles[];
  uint16  Enabled = 1;
  string  CommonName;
  string  PolicyKeywords[];
  string  InstanceID;
  string  Caption;
  string  DisplayName;
  string  Description;
  string  ElementName;
};
```

## Members

The **MSFT\_NetConSecRule** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetConSecRule** class has these methods.



| Method                                                        | Description                                                  |
|:--------------------------------------------------------------|:-------------------------------------------------------------|
| [**CloneObject**](cloneobject-msft-netconsecrule.md)         | Copy this rule.<br/>                                   |
| [**Disable**](disable-msft-netconsecrule.md)                 | Disable this rule.<br/>                                |
| [**Enable**](enable-msft-netconsecrule.md)                   | Enable this rule.<br/>                                 |
| [**EnumerateFull**](enumeratefull-msft-netconsecrule.md)     | Enumerate all parts of all rules<br/>                  |
| [**Find**](find-msft-netconsecrule.md)                       | Retrieves the specified connection security rule.<br/> |
| [**Rename**](rename-msft-netconsecrule.md)                   | Rename this rule.<br/>                                 |
| [**SetPolicyDelta**](setpolicydelta-msft-netconsecrule.md)   | Apply IPsec policy deltas<br/>                         |
| [**SyncPolicyDelta**](syncpolicydelta-msft-netconsecrule.md) | Synchronize IPsec policy<br/>                          |



 

### Properties

The **MSFT\_NetConSecRule** class has these properties.

<dl> <dt>

**AllowSetKey**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to allow Trusted Intermediaries to set the key of SA's created by this rule.

</dd> <dt>

**AllowWatchKey**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to allow Trusted Intermediaries to be notified when the encryption keys for this SA change.

</dd> <dt>

**BypassTunnelIfEncrypted**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Allow traffic that is already encrypted to bypass the tunnel.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Override**, **MaxLen** ( 64 )
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

</dd> <dt>

**CommonName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ConditionListType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A brief description of the rule. May be an indirect string. If it is an indirect string, then it may not be overwritten.

</dd> <dt>

**DisplayGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The group that this rule belongs to. This field is based on the value of RuleGroup and changes to this field are ignored.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The localized name of this rule. This field's value is based on the value of ElementName. Changes to this field are ignored.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The locale-independent name of the rule. May be an indirect string.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this rule is administratively enabled or disabled.

<dl> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (1)
</dt> <dt>

<span id="Disabled_"></span><span id="disabled_"></span><span id="DISABLED_"></span>**Disabled** (2 )
</dt> </dl>

</dd> <dt>

**EnforcementStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this object is retrieved from the ActiveStore, describes the current enforcement status of the rule.

<dl> <dt>

<span id="Invalid"></span><span id="invalid"></span><span id="INVALID"></span>**Invalid** (0)
</dt> <dt>

<span id="Full"></span><span id="full"></span><span id="FULL"></span>**Full** (1)
</dt> <dt>

<span id="FirewallOffInProfile"></span><span id="firewalloffinprofile"></span><span id="FIREWALLOFFINPROFILE"></span>**FirewallOffInProfile** (2)
</dt> <dt>

<span id="CategoryOff"></span><span id="categoryoff"></span><span id="CATEGORYOFF"></span>**CategoryOff** (3)
</dt> <dt>

<span id="DisabledObject"></span><span id="disabledobject"></span><span id="DISABLEDOBJECT"></span>**DisabledObject** (4)
</dt> <dt>

<span id="InactiveProfile"></span><span id="inactiveprofile"></span><span id="INACTIVEPROFILE"></span>**InactiveProfile** (5)
</dt> <dt>

<span id="LocalAddressResolutionEmpty"></span><span id="localaddressresolutionempty"></span><span id="LOCALADDRESSRESOLUTIONEMPTY"></span>**LocalAddressResolutionEmpty** (6)
</dt> <dt>

<span id="RemoteAddressResolutionEmpty"></span><span id="remoteaddressresolutionempty"></span><span id="REMOTEADDRESSRESOLUTIONEMPTY"></span>**RemoteAddressResolutionEmpty** (7)
</dt> <dt>

<span id="LocalPortResolutionEmpty"></span><span id="localportresolutionempty"></span><span id="LOCALPORTRESOLUTIONEMPTY"></span>**LocalPortResolutionEmpty** (8)
</dt> <dt>

<span id="RemotePortResolutionEmpty"></span><span id="remoteportresolutionempty"></span><span id="REMOTEPORTRESOLUTIONEMPTY"></span>**RemotePortResolutionEmpty** (9)
</dt> <dt>

<span id="InterfaceResolutionEmpty"></span><span id="interfaceresolutionempty"></span><span id="INTERFACERESOLUTIONEMPTY"></span>**InterfaceResolutionEmpty** (10)
</dt> <dt>

<span id="ApplicationResolutionEmpty"></span><span id="applicationresolutionempty"></span><span id="APPLICATIONRESOLUTIONEMPTY"></span>**ApplicationResolutionEmpty** (11)
</dt> <dt>

<span id="RemoteMachineEmpty"></span><span id="remotemachineempty"></span><span id="REMOTEMACHINEEMPTY"></span>**RemoteMachineEmpty** (12)
</dt> <dt>

<span id="RemoteUserEmpty"></span><span id="remoteuserempty"></span><span id="REMOTEUSEREMPTY"></span>**RemoteUserEmpty** (13)
</dt> <dt>

<span id="LocalGlobalOpenPortsDisallowed"></span><span id="localglobalopenportsdisallowed"></span><span id="LOCALGLOBALOPENPORTSDISALLOWED"></span>**LocalGlobalOpenPortsDisallowed** (14)
</dt> <dt>

<span id="LocalAuthorizedApplicationsDisallowed"></span><span id="localauthorizedapplicationsdisallowed"></span><span id="LOCALAUTHORIZEDAPPLICATIONSDISALLOWED"></span>**LocalAuthorizedApplicationsDisallowed** (15)
</dt> <dt>

<span id="LocalFirewallRulesDisallowed"></span><span id="localfirewallrulesdisallowed"></span><span id="LOCALFIREWALLRULESDISALLOWED"></span>**LocalFirewallRulesDisallowed** (16)
</dt> <dt>

<span id="LocalConsecRulesDisallowed"></span><span id="localconsecrulesdisallowed"></span><span id="LOCALCONSECRULESDISALLOWED"></span>**LocalConsecRulesDisallowed** (17)
</dt> <dt>

<span id="NotTargetPlatform"></span><span id="nottargetplatform"></span><span id="NOTTARGETPLATFORM"></span>**NotTargetPlatform** (18)
</dt> <dt>

<span id="OptimizedOut"></span><span id="optimizedout"></span><span id="OPTIMIZEDOUT"></span>**OptimizedOut** (19)
</dt> <dt>

<span id="LocalUserEmpty"></span><span id="localuserempty"></span><span id="LOCALUSEREMPTY"></span>**LocalUserEmpty** (20)
</dt> <dt>

<span id="TransportMachinesEmpty"></span><span id="transportmachinesempty"></span><span id="TRANSPORTMACHINESEMPTY"></span>**TransportMachinesEmpty** (21)
</dt> <dt>

<span id="TunnelMachinesEmpty"></span><span id="tunnelmachinesempty"></span><span id="TUNNELMACHINESEMPTY"></span>**TunnelMachinesEmpty** (22)
</dt> <dt>

<span id="TupleResolutionEmpty_"></span><span id="tupleresolutionempty_"></span><span id="TUPLERESOLUTIONEMPTY_"></span>**TupleResolutionEmpty** (23 )
</dt> </dl>

</dd> <dt>

**ExecutionStrategy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**InboundSecurity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Determines how aggressively to enforce security on inbound traffic.

<dl> <dt>

<span id="Never"></span><span id="never"></span><span id="NEVER"></span>**Never** (0)
</dt> <dt>

<span id="Request"></span><span id="request"></span><span id="REQUEST"></span>**Request** (1)
</dt> <dt>

<span id="Require_"></span><span id="require_"></span><span id="REQUIRE_"></span>**Require** (2 )
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that uniquely identifies this instance within the PolicyStore.

</dd> <dt>

**KeyModule**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Which keying modules to use.

<dl> <dt>

<span id="IKEv1"></span><span id="ikev1"></span><span id="IKEV1"></span>**IKEv1** (0x1)
</dt> <dt>

<span id="IKEv2"></span><span id="ikev2"></span><span id="IKEV2"></span>**IKEv2** (0x4)
</dt> <dt>

<span id="AuthIP_"></span><span id="authip_"></span><span id="AUTHIP_"></span>**AuthIP** (0x2 )
</dt> </dl>

</dd> <dt>

**LocalTunnelEndpoint**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local tunnel endpoint address.

</dd> <dt>

**Machines**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Authorized machines for transport mode, specified as an SDDL string.

</dd> <dt>

**MainModeCryptoSet**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The InstanceID of the MainModeCryptoSet to use for Main Mode.

</dd> <dt>

**Mandatory**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**MaxReturnPathLifetimeSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum lifetime, in seconds, for SA's created by this rule across the forwarding path.

</dd> <dt>

**Mode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IPsec Encapsulation Mode that should be used.

<dl> <dt>

<span id="Transport_Mode"></span><span id="transport_mode"></span><span id="TRANSPORT_MODE"></span>**Transport Mode** (1)
</dt> <dt>

<span id="Tunnel_Mode_"></span><span id="tunnel_mode_"></span><span id="TUNNEL_MODE_"></span>**Tunnel Mode** (2 )
</dt> </dl>

</dd> <dt>

**OutboundSecurity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Determines how aggressively to enforce security on outbound traffic.

<dl> <dt>

<span id="Never"></span><span id="never"></span><span id="NEVER"></span>**Never** (0)
</dt> <dt>

<span id="Request"></span><span id="request"></span><span id="REQUEST"></span>**Request** (1)
</dt> <dt>

<span id="Require_"></span><span id="require_"></span><span id="REQUIRE_"></span>**Require** (2 )
</dt> </dl>

</dd> <dt>

**Phase1AuthSet**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The InstanceID of the Phase1AuthenticationSet to use for Phase 1 auth.

</dd> <dt>

**Phase2AuthSet**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The InstanceID of the Phase2AuthenticationSet to use for Phase 2 auth.

</dd> <dt>

**Platforms**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies which platforms the rule is applicable on. If null, the rule applies to all platforms (the default). Each entry takes the form Major.Minor+, for instance 6.0, 6.1+, or 6.2. If + is specified, then it means that the rule applies to that version or greater. For instance, Windows Vista could be represented as 6 or 6.0, and Windows 7 or later would be represented as 6.1+. + may only be attached to the final item in the list. 6.0+ is not valid because it means the same thing as null (all platforms).

</dd> <dt>

**PolicyDecisionStrategy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**PolicyKeywords**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**PolicyRoles**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**PolicyRuleName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**PolicyStoreSource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this object is retrieved from the ActiveStore, with the TracePolicyStoreSource option set, contains the path to the PolicyStore where this rule originally came from.

</dd> <dt>

**PolicyStoreSourceType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this object is retrieved from the ActiveStore, with the TracePolicyStoreSource option set, describes the type of PolicyStore where this rule originally came from.

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

PrimaryStatus provides a high level status value, intended to align with Red-Yellow-Green type representation of status. It should be used in conjunction with DetailedStatus to provide high level and detailed health status of the ManagedElement and its subcomponents. PrimaryStatus consists of one of the following values: Unknown, OK, Degraded or Error. "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. "OK" indicates the ManagedElement is functioning normally. "Degraded" indicates the ManagedElement is functioning below normal. "Error" indicates the ManagedElement is in an Error condition.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="OK"></span><span id="ok"></span>**OK** (1)
</dt> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (2)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (3)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Reserved_"></span><span id="vendor_reserved_"></span><span id="VENDOR_RESERVED_"></span>**Vendor Reserved** (0x8000.. )
</dt> </dl>

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**Profiles**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Which profiles this rule is active on.

<dl> <dt>

<span id="Any"></span><span id="any"></span><span id="ANY"></span>**Any** (0)
</dt> <dt>

<span id="Public"></span><span id="public"></span><span id="PUBLIC"></span>**Public** (0x4)
</dt> <dt>

<span id="Private"></span><span id="private"></span><span id="PRIVATE"></span>**Private** (0x2)
</dt> <dt>

<span id="Domain_"></span><span id="domain_"></span><span id="DOMAIN_"></span>**Domain** (0x1 )
</dt> </dl>

</dd> <dt>

**QuickModeCryptoSet**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The InstanceID of the QuickModeCryptoSet to use for Quick Mode.

</dd> <dt>

**RemoteTunnelEndpoint**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The remote tunnel endpoint(s).

</dd> <dt>

**RemoteTunnelEndpointDNSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A Fully-Qualified Domain Name that resolves to a list of allowed Remote Endpoints. If present, the value in RemoteEndpoint will be used initially, but will be replaced with all the IP addresses that this name resolves to.

</dd> <dt>

**RequireAuthorization**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Require authorization for endpoints. The authorization list is part of the IPsec Globals.

</dd> <dt>

**RuleGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The locale-independent name for the group that this rule belongs to. If this field is non-null, then Windows Firewall with Advanced Security assumes that this rule belongs to a Windows component or an installed application, and some parts of the rule are protected (including but not limited to the Name, Description, Program, and Service).

</dd> <dt>

**RuleUsage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**SequencedActions**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The detailed status of the rule, as a string.

</dd> <dt>

**StatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The detailed status of the rule, as a numeric error code.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**Users**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Authorized users for transport mode, specified as an SDDL string.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




