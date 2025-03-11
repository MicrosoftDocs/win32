---
description: Represents an IPsec Rule. Subtypes differentiate between Connection Security Rules (MSFT\_NetConSecRule) and Main Mode Rules (MSFT\_NetMainModeRule).
ms.assetid: 6852040f-ba00-4f48-b468-d4a204370d3a
title: MSFT\_NetSARule class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSARule
- MSFT_NetSARule.Platforms
- MSFT_NetSARule.RuleGroup
- MSFT_NetSARule.DisplayName
- MSFT_NetSARule.DisplayGroup
- MSFT_NetSARule.Profiles
- MSFT_NetSARule.MainModeCryptoSet
- MSFT_NetSARule.QuickModeCryptoSet
- MSFT_NetSARule.Phase1AuthSet
- MSFT_NetSARule.Phase2AuthSet
- MSFT_NetSARule.PrimaryStatus
- MSFT_NetSARule.StatusCode
- MSFT_NetSARule.Status
- MSFT_NetSARule.EnforcementStatus
- MSFT_NetSARule.PolicyStoreSourceType
- MSFT_NetSARule.PolicyStoreSource
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetSARule class

Represents an IPsec Rule. Subtypes differentiate between Connection Security Rules (MSFT\_NetConSecRule) and Main Mode Rules (MSFT\_NetMainModeRule).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetSARule : CIM_SARule
{
  string Platforms[];
  string RuleGroup;
  string DisplayName;
  string DisplayGroup;
  uint16 Profiles;
  string MainModeCryptoSet;
  string QuickModeCryptoSet;
  string Phase1AuthSet;
  string Phase2AuthSet;
  uint16 PrimaryStatus;
  uint32 StatusCode;
  string Status;
  uint16 EnforcementStatus[];
  uint16 PolicyStoreSourceType;
  string PolicyStoreSource;
};
```

## Members

The **MSFT\_NetSARule** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetSARule** class has these properties.

<dl> <dt>

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

**MainModeCryptoSet**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The InstanceID of the MainModeCryptoSet to use for Main Mode.

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

**RuleGroup**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The locale-independent name for the group that this rule belongs to. If this field is non-null, then Windows Firewall with Advanced Security assumes that this rule belongs to a Windows component or an installed application, and some parts of the rule are protected (including but not limited to the Name, Description, Program, and Service).

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

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




