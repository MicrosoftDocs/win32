---
title: DtcTransactionInfo class
description: Represents information about a DTC transaction.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 728cea01-0c44-401c-ad4c-3a772e540521
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DtcTransactionInfo class
- DtcTransactionInfo class, described
topic_type:
- apiref
api_name:
- DtcTransactionInfo
- DtcTransactionInfo.TransactionId
- DtcTransactionInfo.IsolationLevel
- DtcTransactionInfo.State
- DtcTransactionInfo.Parent
- DtcTransactionInfo.Description
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DtcTransactionInfo class

Represents information about a DTC transaction.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class DtcTransactionInfo
{
  string TransactionId;
  uint32 IsolationLevel;
  string State;
  string Parent;
  string Description;
};
```

## Members

The **DtcTransactionInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **DtcTransactionInfo** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the transaction.

</dd> <dt>

**IsolationLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The isolation level of the transaction.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the parent transaction manager of this transaction.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The state of the transaction.

</dd> <dt>

**TransactionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the transaction.

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

 

 





