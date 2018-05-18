---
title: DtcTransactionsStatistics class
description: Represents the transaction statistics for a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '36240e73-92d9-44a1-97c1-1759dae2320a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DtcTransactionsStatistics class", "DtcTransactionsStatistics class, described"]
---

# DtcTransactionsStatistics class

Represents the transaction statistics for a DTC instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class DtcTransactionsStatistics
{
  uint32 Open;
  uint32 Committed;
  uint32 Aborted;
  uint32 InDoubt;
  uint32 Heuristic;
  uint32 OpenMax;
  uint32 CommittedMax;
  uint32 AbortedMax;
  uint32 InDoubtMax;
  uint32 HeuristicMax;
  uint32 ForcedCommit;
  uint32 ForcedAbort;
  uint32 SinglePhaseInDoubt;
};
```

## Members

The **DtcTransactionsStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DtcTransactionsStatistics** class has these properties.

<dl> <dt>

**Aborted**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of transactions that were shut down before they were completed.

</dd> <dt>

**AbortedMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The highest number of aborted transactions since DTC last started.

</dd> <dt>

**Committed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of commited transactions for the instance.

</dd> <dt>

**CommittedMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The highest number of committed transactions since DTC last started.

</dd> <dt>

**ForcedAbort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of aborted transactions that were manually shut down before they were completed.

</dd> <dt>

**ForcedCommit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of committed transactions that were manually committed.

</dd> <dt>

**Heuristic**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**HeuristicMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**InDoubt**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of in doubt transactions.

</dd> <dt>

**InDoubtMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The highest number of in doubt transactions since DTC last started.

</dd> <dt>

**Open**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of running transactions for the instance.

</dd> <dt>

**OpenMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The highest number of concurrently running transactions since DTC last started.

</dd> <dt>

**SinglePhaseInDoubt**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





