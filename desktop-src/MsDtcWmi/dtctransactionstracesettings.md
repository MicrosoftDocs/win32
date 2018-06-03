---
title: DtcTransactionsTraceSettings class
description: Represents DTC transaction trace settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e8726c5c-b630-442d-a811-d0d098995157
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DtcTransactionsTraceSettings class
- DtcTransactionsTraceSettings class, described
topic_type:
- apiref
api_name:
- DtcTransactionsTraceSettings
- DtcTransactionsTraceSettings.AllTransactionsTracingEnabled
- DtcTransactionsTraceSettings.AbortedTransactionsTracingEnabled
- DtcTransactionsTraceSettings.LongLivedTransactionsTracingEnabled
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DtcTransactionsTraceSettings class

Represents DTC transaction trace settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class DtcTransactionsTraceSettings
{
  boolean AllTransactionsTracingEnabled;
  boolean AbortedTransactionsTracingEnabled;
  boolean LongLivedTransactionsTracingEnabled;
};
```

## Members

The **DtcTransactionsTraceSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **DtcTransactionsTraceSettings** class has these properties.

<dl> <dt>

**AbortedTransactionsTracingEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if tracing for aborted transactions is enabled; otherwise, **false**.

</dd> <dt>

**AllTransactionsTracingEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if tracing for all transactions is enabled; otherwise, **false**.

</dd> <dt>

**LongLivedTransactionsTracingEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if tracing for long-lived transactions is enabled; otherwise, **false**.

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

 

 





