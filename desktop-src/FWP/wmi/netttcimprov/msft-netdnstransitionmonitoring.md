---
description: Provides counters for DNS64 queries.
ms.assetid: 9dcb0ceb-8122-4683-8c0a-20dc6db22cd7
title: MSFT\_NetDnsTransitionMonitoring class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetDnsTransitionMonitoring
- MSFT_NetDnsTransitionMonitoring.NumAAAAQueriesSucceeded
- MSFT_NetDnsTransitionMonitoring.NumAAAAQueriesFailed
- MSFT_NetDnsTransitionMonitoring.NumAAAAQueriesSynthesized
- MSFT_NetDnsTransitionMonitoring.NumAAAAQueriesIn6ArpaPtr
- MSFT_NetDnsTransitionMonitoring.NumOtherQueriesSucceeded
- MSFT_NetDnsTransitionMonitoring.NumOtherQueriesFailed
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetDnsTransitionMonitoring class

Provides counters for DNS64 queries.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetDnsTransitionMonitoring : MSFT_NetSettingData
{
  uint32 NumAAAAQueriesSucceeded;
  uint32 NumAAAAQueriesFailed;
  uint32 NumAAAAQueriesSynthesized;
  uint32 NumAAAAQueriesIn6ArpaPtr;
  uint32 NumOtherQueriesSucceeded;
  uint32 NumOtherQueriesFailed;
};
```

## Members

The **MSFT\_NetDnsTransitionMonitoring** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetDnsTransitionMonitoring** class has these properties.

<dl> <dt>

**NumAAAAQueriesFailed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the number failed AAAA queries.

</dd> <dt>

**NumAAAAQueriesIn6ArpaPtr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the number of translated PTR (record containing a FQDN pointer) queries.

</dd> <dt>

**NumAAAAQueriesSucceeded**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the number of successful AAAA (128-bit IPv6 address) queries.

</dd> <dt>

**NumAAAAQueriesSynthesized**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the number of synthesized AAAA queries.

</dd> <dt>

**NumOtherQueriesFailed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the number of failed non-AAAA queries.

</dd> <dt>

**NumOtherQueriesSucceeded**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the number successful non-AAAA queries.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




