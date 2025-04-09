---
description: Filters traffic based on its protocol and port.
ms.assetid: 66b3779a-aef3-4079-8a2f-7dfdd9924d27
title: MSFT\_NetProtocolPortFilter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetProtocolPortFilter
- MSFT_NetProtocolPortFilter.Protocol
- MSFT_NetProtocolPortFilter.RemotePort
- MSFT_NetProtocolPortFilter.LocalPort
- MSFT_NetProtocolPortFilter.IcmpType
- MSFT_NetProtocolPortFilter.DynamicTransport
- MSFT_NetProtocolPortFilter.Name
- MSFT_NetProtocolPortFilter.SystemCreationClassName
- MSFT_NetProtocolPortFilter.SystemName
- MSFT_NetProtocolPortFilter.CreationClassName
- MSFT_NetProtocolPortFilter.IsNegated
- MSFT_NetProtocolPortFilter.InstallDate
- MSFT_NetProtocolPortFilter.OperationalStatus
- MSFT_NetProtocolPortFilter.StatusDescriptions
- MSFT_NetProtocolPortFilter.Status
- MSFT_NetProtocolPortFilter.HealthState
- MSFT_NetProtocolPortFilter.CommunicationStatus
- MSFT_NetProtocolPortFilter.DetailedStatus
- MSFT_NetProtocolPortFilter.OperatingStatus
- MSFT_NetProtocolPortFilter.PrimaryStatus
- MSFT_NetProtocolPortFilter.InstanceID
- MSFT_NetProtocolPortFilter.Caption
- MSFT_NetProtocolPortFilter.Description
- MSFT_NetProtocolPortFilter.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetProtocolPortFilter class

Filters traffic based on its protocol and port.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetProtocolPortFilter : CIM_FilterEntryBase
{
  string   Protocol;
  string   RemotePort[];
  string   LocalPort[];
  string   IcmpType[];
  uint32   DynamicTransport;
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

The **MSFT\_NetProtocolPortFilter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetProtocolPortFilter** class has these properties.

<dl> <dt>

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

**DynamicTransport**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Allows filtering traffic to/from endpoints by certain kinds of virtual transports, rather than traditional tuples of addresses, protocols, and ports.

<dl><span id="0"></span><dt>

**0**
</dt><span id="1"></span><dt>

**1**
</dt><span id="2_"></span><dt>

**2** 
</dt><span id="4"></span><dt>

**4**
</dt><span id="8"></span><dt>

**8**
</dt><span id="16_"></span><dt>

**16** 
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

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**IcmpType**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Applies only when Protocol is ICMPv4 or ICMPv6. ICMP Type/Code pairs this filter applies to. May be an ICMP type (0-255), or an ICMP type/code pair in the format Type.Code, where type and code values are numbers from 0 to 255.

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

**LocalPort**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Applies only when Protocol is TCP or UDP. Local ports this filter applies to. May be a number or range 0-65535, or one of the following: Any, RPC, RPC-EPMap, IPHTTPSIn, PlayToDiscovery.

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

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP Protocol Number that this filter applies to. May be 0-255 or one of the following: ICMPv4, ICMPv6, TCP, UDP.

</dd> <dt>

**RemotePort**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Applies only when Protocol is TCP or UDP. Remote ports this filter applies to. May be a number or range 0-65535, or one of the following: Any, IPHTTPSOut.

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



 

 




