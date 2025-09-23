---
description: Filters traffic based on certain high-level security constraints, like whether or not the traffic is encrypted. Connection Security rules will have to be created in order for traffic to pass the rule.
ms.assetid: c15bbfa6-5f0f-4500-b717-9522f05c67bb
title: MSFT\_NetNetworkLayerSecurityFilter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetNetworkLayerSecurityFilter
- MSFT_NetNetworkLayerSecurityFilter.Authentication
- MSFT_NetNetworkLayerSecurityFilter.Encryption
- MSFT_NetNetworkLayerSecurityFilter.OverrideBlockRules
- MSFT_NetNetworkLayerSecurityFilter.LocalUsers
- MSFT_NetNetworkLayerSecurityFilter.RemoteUsers
- MSFT_NetNetworkLayerSecurityFilter.RemoteMachines
- MSFT_NetNetworkLayerSecurityFilter.Name
- MSFT_NetNetworkLayerSecurityFilter.SystemCreationClassName
- MSFT_NetNetworkLayerSecurityFilter.SystemName
- MSFT_NetNetworkLayerSecurityFilter.CreationClassName
- MSFT_NetNetworkLayerSecurityFilter.IsNegated
- MSFT_NetNetworkLayerSecurityFilter.InstallDate
- MSFT_NetNetworkLayerSecurityFilter.OperationalStatus
- MSFT_NetNetworkLayerSecurityFilter.StatusDescriptions
- MSFT_NetNetworkLayerSecurityFilter.Status
- MSFT_NetNetworkLayerSecurityFilter.HealthState
- MSFT_NetNetworkLayerSecurityFilter.CommunicationStatus
- MSFT_NetNetworkLayerSecurityFilter.DetailedStatus
- MSFT_NetNetworkLayerSecurityFilter.OperatingStatus
- MSFT_NetNetworkLayerSecurityFilter.PrimaryStatus
- MSFT_NetNetworkLayerSecurityFilter.InstanceID
- MSFT_NetNetworkLayerSecurityFilter.Caption
- MSFT_NetNetworkLayerSecurityFilter.Description
- MSFT_NetNetworkLayerSecurityFilter.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetNetworkLayerSecurityFilter class

Filters traffic based on certain high-level security constraints, like whether or not the traffic is encrypted. Connection Security rules will have to be created in order for traffic to pass the rule.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetNetworkLayerSecurityFilter : CIM_FilterEntryBase
{
  uint16   Authentication;
  uint16   Encryption;
  boolean  OverrideBlockRules;
  string   LocalUsers;
  string   RemoteUsers;
  string   RemoteMachines;
  string   Name;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  boolean  IsNegated;
  datetime InstallDate;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  string   InstanceID;
  string   Caption;
  string   Description;
  string   ElementName;
};
```

## Members

The **MSFT\_NetNetworkLayerSecurityFilter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetNetworkLayerSecurityFilter** class has these properties.

<dl> <dt>

**Authentication**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to require Authentication. NoEncapsulation means that authentication is still required, but only once at the beginning of the traffic flow, instead of on every packet.

<dl> <dt>

<span id="NotRequired"></span><span id="notrequired"></span><span id="NOTREQUIRED"></span>**NotRequired** (0)
</dt> <dt>

<span id="Required"></span><span id="required"></span><span id="REQUIRED"></span>**Required** (1)
</dt> <dt>

<span id="NoEncapsulation_"></span><span id="noencapsulation_"></span><span id="NOENCAPSULATION_"></span>**NoEncapsulation** (2 )
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

**CommunicationStatus**
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

This field is ignored.

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
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

**Encryption**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to require Encryption. Dynamic encryption means that the first packet may be protected but not encrypted.

<dl> <dt>

<span id="NotRequired"></span><span id="notrequired"></span><span id="NOTREQUIRED"></span>**NotRequired** (0)
</dt> <dt>

<span id="Required"></span><span id="required"></span><span id="REQUIRED"></span>**Required** (1)
</dt> <dt>

<span id="Dynamic_"></span><span id="dynamic_"></span><span id="DYNAMIC_"></span>**Dynamic** (2 )
</dt> </dl>

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
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

**IsNegated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**LocalUsers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SDDL string describing Local Users that are allowed by this rule. If this is empty, all users are allowed. If LocalUsers/RemoteUsers/RemoteMachines are specified, then they apply conjunctively, and this is an 'Allow-Bypass' rule and ProtectionLevel must be set above None (so that authentication is required).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OverrideBlockRules**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to allow this rule to take precedence over Block rules. This setting may only be applied on Allow rules that require Authentication with specific RemoteUsers and/or RemoteMachines.

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**RemoteMachines**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SDDL string describing Remote Machines that are allowed by this rule. If this is empty, all users are allowed. If LocalUsers/RemoteUsers/RemoteMachines are specified, then they apply conjunctively, and this is an 'Allow-Bypass' rule and ProtectionLevel must be set above None (so that authentication is required).

</dd> <dt>

**RemoteUsers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SDDL string describing Remote Users that are allowed by this rule. If this is empty, all users are allowed. If LocalUsers/RemoteUsers/RemoteMachines are specified, then they apply conjunctively, and this is an 'Allow-Bypass' rule and ProtectionLevel must be set above None (so that authentication is required).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

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

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




