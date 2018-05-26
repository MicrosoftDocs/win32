---
title: DtcTransactionsTraceSession class
description: Represents a DTC transaction trace session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4ebf55a3-45ec-4932-bb42-59098079e877
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DtcTransactionsTraceSession class
- DtcTransactionsTraceSession class, described
topic_type:
- apiref
api_name:
- DtcTransactionsTraceSession
- DtcTransactionsTraceSession.SessionStatus
- DtcTransactionsTraceSession.BufferCount
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DtcTransactionsTraceSession class

Represents a DTC transaction trace session.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class DtcTransactionsTraceSession
{
  string SessionStatus;
  uint32 BufferCount;
};
```

## Members

The **DtcTransactionsTraceSession** class has these types of members:

-   [Properties](#properties)

### Properties

The **DtcTransactionsTraceSession** class has these properties.

<dl> <dt>

**BufferCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of objects stored in the output buffer for the trace session.

</dd> <dt>

**SessionStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the trace session.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





