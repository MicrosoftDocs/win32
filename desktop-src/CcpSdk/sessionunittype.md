---
Description: 'Defines values to indicate the type of hardware resources used to determine to nodes on which the service job for a service-oriented architecture (SOA) session can run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'BE43F8D0-2ED9-45E4-99CC-9E79156D4BE5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: SessionUnitType enumeration
---

# SessionUnitType enumeration

Defines values to indicate the type of hardware resources used to determine to nodes on which the service job for a service-oriented architecture (SOA) session can run.

## Syntax


```C++
typedef enum  { 
  SessionUnitType_Core    = 0,
  SessionUnitType_Socket  = 1,
  SessionUnitType_Node    = 2
} SessionUnitType;
```



## Constants

<dl> <dt>

<span id="SessionUnitType_Core"></span><span id="sessionunittype_core"></span><span id="SESSIONUNITTYPE_CORE"></span>**SessionUnitType\_Core**
</dt> <dd>

Uses cores to schedule the service job.

</dd> <dt>

<span id="SessionUnitType_Socket"></span><span id="sessionunittype_socket"></span><span id="SESSIONUNITTYPE_SOCKET"></span>**SessionUnitType\_Socket**
</dt> <dd>

Uses sockets to scheduler the service job.

</dd> <dt>

<span id="SessionUnitType_Node"></span><span id="sessionunittype_node"></span><span id="SESSIONUNITTYPE_NODE"></span>**SessionUnitType\_Node**
</dt> <dd>

Uses nodes to schedule the service job.

</dd> </dl>

## Remarks

The least granular resource unit is the node and the most granular resource unit is the core. For example, a node can have four cores on one socket and the node can contain multiple sockets. A job can specify that it needs a minimum of four nodes to run, regardless of how many cores are on each node. The job could also specify that it needs four cores to run, so it could run on one node that had four cores or on multiple nodes with one or two cores.

Use the values of this enumeration when you specify the resources that the SOA session for the [**IExcelClient**](iexcelclient.md) interface should use.

## Requirements



|                         |                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                       |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Excel.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IExcelClient::OpenSession**](iexcelclient-opensession.md)
</dt> </dl>

 

 




