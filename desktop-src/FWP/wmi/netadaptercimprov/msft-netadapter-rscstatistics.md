---
description: RSC statistics supported by a network adapter.
ms.assetid: 61d9c882-51f1-48cc-90f0-d851f3eb6f04
title: MSFT\_NetAdapter\_RscStatistics class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_RscStatistics
- MSFT_NetAdapter_RscStatistics.CoalescedPackets
- MSFT_NetAdapter_RscStatistics.CoalescedBytes
- MSFT_NetAdapter_RscStatistics.CoalescingEvents
- MSFT_NetAdapter_RscStatistics.CoalescingExceptions
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_RscStatistics class

RSC statistics supported by a network adapter

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetAdapter_RscStatistics
{
  uint64 CoalescedPackets;
  uint64 CoalescedBytes;
  uint64 CoalescingEvents;
  uint64 CoalescingExceptions;
};
```

## Members

The **MSFT\_NetAdapter\_RscStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_RscStatistics** class has these properties.

<dl> <dt>

**CoalescedBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of bytes that have resulted from one or more coalescing events

</dd> <dt>

**CoalescedPackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of packets that have resulted from one or more coalescing events

</dd> <dt>

**CoalescingEvents**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of cases where an incoming packet is found eligible for coalescing

</dd> <dt>

**CoalescingExceptions**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of cases where an incoming packet is found ineligible for coalescing

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




