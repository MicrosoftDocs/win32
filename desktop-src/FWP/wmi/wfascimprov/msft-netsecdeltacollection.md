---
description: IPSec policy delta.
ms.assetid: 21fcb024-f7f9-4fda-a760-0268f0d7855c
title: MSFT\_NetSecDeltaCollection class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSecDeltaCollection
- MSFT_NetSecDeltaCollection.Action
- MSFT_NetSecDeltaCollection.IPv6Addresses
- MSFT_NetSecDeltaCollection.IPv4Addresses
- MSFT_NetSecDeltaCollection.PolicyStore
- MSFT_NetSecDeltaCollection.IPsecRuleName
- MSFT_NetSecDeltaCollection.EndpointType
- MSFT_NetSecDeltaCollection.NameResolutionFailures
- MSFT_NetSecDeltaCollection.IPsecRuleDisplayName
- MSFT_NetSecDeltaCollection.InstanceID
- MSFT_NetSecDeltaCollection.Caption
- MSFT_NetSecDeltaCollection.Description
- MSFT_NetSecDeltaCollection.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetSecDeltaCollection class

IPSec policy delta

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetSecDeltaCollection : CIM_SettingData
{
  uint16 Action;
  string IPv6Addresses[];
  string IPv4Addresses[];
  string PolicyStore;
  string IPsecRuleName;
  uint16 EndpointType;
  string NameResolutionFailures[];
  string IPsecRuleDisplayName;
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT\_NetSecDeltaCollection** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetSecDeltaCollection** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Action

<dl> <dt>

<span id="Add"></span><span id="add"></span><span id="ADD"></span>**Add** (0)
</dt> <dt>

<span id="Delete_"></span><span id="delete_"></span><span id="DELETE_"></span>**Delete** (1 )
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

**EndpointType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

endpoint type

<dl> <dt>

<span id="Endpoint1"></span><span id="endpoint1"></span><span id="ENDPOINT1"></span>**Endpoint1** (0)
</dt> <dt>

<span id="Endpoint2_"></span><span id="endpoint2_"></span><span id="ENDPOINT2_"></span>**Endpoint2** (1 )
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

**IPsecRuleDisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The DisplayName of the IPsec rule.

</dd> <dt>

**IPsecRuleName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPsec rule name

</dd> <dt>

**IPv4Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of V4 addresses

</dd> <dt>

**IPv6Addresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of V6 addresses

</dd> <dt>

**NameResolutionFailures**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of names that failed name resolution

</dd> <dt>

**PolicyStore**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Policy Store

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




