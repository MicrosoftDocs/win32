---
description: Sriov Capabilities.
ms.assetid: 35a6d096-8cf5-4893-921e-4f9799a355f6
title: MSFT\_NetAdapterSriovCapabilities class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterSriovCapabilities
- MSFT_NetAdapterSriovCapabilities.VlanSupported
- MSFT_NetAdapterSriovCapabilities.PerVportInterruptModerationSupported
- MSFT_NetAdapterSriovCapabilities.AsymmetricQueuePairsForNonDefaultVPortsSupported
- MSFT_NetAdapterSriovCapabilities.VfRssSupported
- MSFT_NetAdapterSriovCapabilities.SingleVportPoolSupported
- MSFT_NetAdapterSriovCapabilities.MaxNumSwitches
- MSFT_NetAdapterSriovCapabilities.MaxNumVPorts
- MSFT_NetAdapterSriovCapabilities.MaxNumVFs
- MSFT_NetAdapterSriovCapabilities.MaxNumQueuePairs
- MSFT_NetAdapterSriovCapabilities.MaxNumQueuePairsPerNonDefaultVPort
- MSFT_NetAdapterSriovCapabilities.MaxNumMacAddresses
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterSriovCapabilities class

Sriov Capabilities

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterSriovCapabilities
{
  boolean VlanSupported;
  boolean PerVportInterruptModerationSupported;
  boolean AsymmetricQueuePairsForNonDefaultVPortsSupported;
  boolean VfRssSupported;
  boolean SingleVportPoolSupported;
  uint32  MaxNumSwitches;
  uint32  MaxNumVPorts;
  uint32  MaxNumVFs;
  uint32  MaxNumQueuePairs;
  uint32  MaxNumQueuePairsPerNonDefaultVPort;
  uint32  MaxNumMacAddresses;
};
```

## Members

The **MSFT\_NetAdapterSriovCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterSriovCapabilities** class has these properties.

<dl> <dt>

**AsymmetricQueuePairsForNonDefaultVPortsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if asymmetric queue pairs are supported for non default vports

</dd> <dt>

**MaxNumMacAddresses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of MAC addresses that can be allocated on the adapter

</dd> <dt>

**MaxNumQueuePairs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of queue pairs that can be allocated on the adapter

</dd> <dt>

**MaxNumQueuePairsPerNonDefaultVPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of queue pairs for the non default vport

</dd> <dt>

**MaxNumSwitches**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of switches that can be created on the adapter

</dd> <dt>

**MaxNumVFs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of Virtual functions that can be created on the adapter

</dd> <dt>

**MaxNumVPorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of vports that can be created on the adapter

</dd> <dt>

**PerVportInterruptModerationSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if Interrupt moderation is supported per vport

</dd> <dt>

**SingleVportPoolSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if a single Vport Pool is supported

</dd> <dt>

**VfRssSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if VF Rss is supported

</dd> <dt>

**VlanSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if Vlans are supported

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




