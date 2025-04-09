---
description: For a Main Mode or Connection Security rule, sets parameters for the main mode negotiation and describes the crypto proposals that should be negotiated.
ms.assetid: d8f8d4ac-f3e9-41d7-94c1-4724630d4374
title: MSFT\_NetIKEMMCryptoSet class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIKEMMCryptoSet
- MSFT_NetIKEMMCryptoSet.ForceDiffieHellman
- MSFT_NetIKEMMCryptoSet.MaxLifetimeSessions
- MSFT_NetIKEMMCryptoSet.MaxLifetimeMinutes
- MSFT_NetIKEMMCryptoSet.RuleGroup
- MSFT_NetIKEMMCryptoSet.DisplayGroup
- MSFT_NetIKEMMCryptoSet.Proposals
- MSFT_NetIKEMMCryptoSet.PrimaryStatus
- MSFT_NetIKEMMCryptoSet.StatusCode
- MSFT_NetIKEMMCryptoSet.Status
- MSFT_NetIKEMMCryptoSet.EnforcementStatus
- MSFT_NetIKEMMCryptoSet.PolicyStoreSourceType
- MSFT_NetIKEMMCryptoSet.PolicyStoreSource
- MSFT_NetIKEMMCryptoSet.ExchangeMode
- MSFT_NetIKEMMCryptoSet.UseIKEIdentityType
- MSFT_NetIKEMMCryptoSet.VendorID
- MSFT_NetIKEMMCryptoSet.AggressiveModeGroupID
- MSFT_NetIKEMMCryptoSet.MinLifetimeSeconds
- MSFT_NetIKEMMCryptoSet.IdleDurationSeconds
- MSFT_NetIKEMMCryptoSet.MinLifetimeKilobytes
- MSFT_NetIKEMMCryptoSet.DoPacketLogging
- MSFT_NetIKEMMCryptoSet.SystemCreationClassName
- MSFT_NetIKEMMCryptoSet.SystemName
- MSFT_NetIKEMMCryptoSet.PolicyRuleCreationClassName
- MSFT_NetIKEMMCryptoSet.PolicyRuleName
- MSFT_NetIKEMMCryptoSet.CreationClassName
- MSFT_NetIKEMMCryptoSet.PolicyActionName
- MSFT_NetIKEMMCryptoSet.DoActionLogging
- MSFT_NetIKEMMCryptoSet.CommonName
- MSFT_NetIKEMMCryptoSet.PolicyKeywords
- MSFT_NetIKEMMCryptoSet.InstanceID
- MSFT_NetIKEMMCryptoSet.Caption
- MSFT_NetIKEMMCryptoSet.DisplayName
- MSFT_NetIKEMMCryptoSet.Description
- MSFT_NetIKEMMCryptoSet.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIKEMMCryptoSet class

For a Main Mode or Connection Security rule, sets parameters for the main mode negotiation and describes the crypto proposals that should be negotiated.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetIKEMMCryptoSet : MSFT_NetIKECryptoSet
{
  boolean ForceDiffieHellman;
  uint32  MaxLifetimeSessions;
  uint32  MaxLifetimeMinutes;
  string  RuleGroup;
  string  DisplayGroup;
  string  Proposals[];
  uint16  PrimaryStatus;
  uint32  StatusCode;
  string  Status;
  uint16  EnforcementStatus[];
  uint16  PolicyStoreSourceType;
  string  PolicyStoreSource;
  uint16  ExchangeMode;
  uint16  UseIKEIdentityType;
  string  VendorID;
  uint16  AggressiveModeGroupID;
  uint64  MinLifetimeSeconds;
  uint64  IdleDurationSeconds;
  uint64  MinLifetimeKilobytes;
  boolean DoPacketLogging;
  string  SystemCreationClassName;
  string  SystemName;
  string  PolicyRuleCreationClassName;
  string  PolicyRuleName;
  string  CreationClassName;
  string  PolicyActionName;
  boolean DoActionLogging;
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

The **MSFT\_NetIKEMMCryptoSet** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetIKEMMCryptoSet** class has these methods.



| Method                                                    | Description                 |
|:----------------------------------------------------------|:----------------------------|
| [**CloneObject**](cloneobject-msft-netikemmcryptoset.md) | Copy this set.<br/>   |
| [**Rename**](rename-msft-netikemmcryptoset.md)           | Rename this set.<br/> |



 

### Properties

The **MSFT\_NetIKEMMCryptoSet** class has these properties.

<dl> <dt>

**AggressiveModeGroupID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

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

A brief description of the set. May be an indirect string. If it is an indirect string, then it may not be overwritten.

</dd> <dt>

**DisplayGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The group that this set belongs to. This field is based on the value of RuleGroup and changes to this field are ignored.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The localized name of this set. This field's value is based on the value of ElementName. Changes to this field are ignored.

</dd> <dt>

**DoActionLogging**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**DoPacketLogging**
</dt> <dd> <dl> <dt>

Data type: **boolean**
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

The locale-independent name of the set. May be an indirect string.

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

**ExchangeMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ForceDiffieHellman**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Require use of Diffie-Hellman for enhanced security.

</dd> <dt>

**IdleDurationSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that uniquely identifies this instance within the PolicyStore.

</dd> <dt>

**MaxLifetimeMinutes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount of time that can elapse before this MMSA must be re-established.

</dd> <dt>

**MaxLifetimeSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of QM SA's that may be established using this MMSA before it must be re-established.

</dd> <dt>

**MinLifetimeKilobytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**MinLifetimeSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**PolicyActionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**PolicyKeywords**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**PolicyRuleCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

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

**Proposals**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The proposals within this set, in order of preference.

</dd> <dt>

**RuleGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The locale-independent name for the group that this set belongs to.

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

**UseIKEIdentityType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**VendorID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




