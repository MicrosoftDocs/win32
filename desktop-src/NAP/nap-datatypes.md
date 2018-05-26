---
title: NAP Datatypes
description: Note The Network Access Protection platform is not available starting with Windows 10 The datatypes for the Network Access Protection (NAP) API are as follows.
ms.assetid: 54f2866b-4333-4fc8-bb25-b7d4ae72b7dc
keywords:
- ProbationTime
- ProtocolMaxSize
- NapComponentId
- SystemHealthEntityId
- EnforcementEntityId
- SystemHealthEntityCount
- EnforcementEntityCount
- StringCorrelationId
- ConnectionId
- Percentage
- MessageId
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NAP Datatypes

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The datatypes for the Network Access Protection (NAP) API are as follows.


```C++
typedef FILETIME ProbationTime;
typedef UINT32 ProtocolMaxSize;
typedef UINT32 NapComponentId;
typedef NapComponentId SystemHealthEntityId;
typedef NapComponentId EnforcementEntityId;
typedef UINT16 SystemHealthEntityCount;
typedef UINT16 EnforcementEntityCount;
typedef CountedString StringCorrelationId;
typedef GUID ConnectionId;
typedef UINT8 Percentage;
typedef UINT32 MessageId;
```



<dl> <dt>

**ProbationTime**
</dt> <dd>

A [FILETIME](http://go.microsoft.com/fwlink/p/?linkid=90006) structure that contains a time related to a client machine's probation.

</dd> <dt>

**ProtocolMaxSize**
</dt> <dd>

A value that specifies the range of possible values for the maximum size, in bytes, of an [**SoH**](/windows/win32/NapTypes/ns-naptypes-tagsoh?branch=master) packet as defined by range([**minProtocolMaxSize, maxProtocolMaxSize**](nap-type-constants.md)).

</dd> <dt>

**NapComponentId**
</dt> <dd>

A unique 4-byte identifier used by SHAs, SHVs and enforcement clients to identify themselves. The first three bytes are the IETF-assigned SMI code of the vendor, and the last byte identifies the component itself.

</dd> <dt>

**SystemHealthEntityId**
</dt> <dd>

A **NapComponentId** value used to identify SHA/SHV pairs.

</dd> <dt>

**EnforcementEntityId**
</dt> <dd>

A **NapComponentId** value used to identify enforcement clients.

</dd> <dt>

**SystemHealthEntityCount**
</dt> <dd>

A value that specifies the number of registered SHAs in the NAP system in the range 0 (zero) to [**maxSystemHealthEntityCount**](nap-type-constants.md).

</dd> <dt>

**EnforcementEntityCount**
</dt> <dd>

A value that specifies the number of enforcement clients in the NAP system in the range 0 (zero) to [**maxEnforcerCount**](nap-type-constants.md).

</dd> <dt>

**StringCorrelationId**
</dt> <dd>

The [**CountedString**](/windows/win32/NapTypes/ns-naptypes-tagcountedstring?branch=master) version of a [**CorrelationId**](/windows/win32/NapTypes/ns-naptypes-tagcorrelationid?branch=master) structure used to pair [**SoHRequests**](/windows/win32/NapTypes/ns-naptypes-tagsoh?branch=master) to **SoHResponses**.

</dd> <dt>

**ConnectionId**
</dt> <dd>

A unique Globally Unique Identifier (GUID) used to identify a NAP connections maintained by enforcement clients.

</dd> <dt>

**Percentage**
</dt> <dd>

A value that contains the percentage between 0 (zero) and 100 of remediation that is complete

</dd> <dt>

**MessageId**
</dt> <dd>

A unique value used to identify NAP system messages.

</dd> </dl>

## Requirements



|                                     |                                                                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                |
| Header<br/>                   | <dl> <dt>NapTypes.h; </dt> <dt>NapEnforcementClient.h</dt> </dl> |



 

 





