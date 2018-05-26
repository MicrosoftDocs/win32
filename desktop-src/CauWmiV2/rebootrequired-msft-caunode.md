---
title: RebootRequired method of the MSFT\_CAUNode class
description: Gets a value that indicates whether the node must be restarted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e240ea84-420d-450a-8536-e69fb09628a1
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RebootRequired method
- RebootRequired method, MSFT_CAUNode class
- MSFT_CAUNode class, RebootRequired method
topic_type:
- apiref
api_name:
- MSFT_CAUNode.RebootRequired
api_location:
- CauWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RebootRequired method of the MSFT\_CAUNode class

Gets a value that indicates whether the node must be restarted.

## Syntax


```mof
boolean RebootRequired();
```



## Parameters

This method has no parameters.

## Return value

**True** if the node must be restarted; otherwise, **false**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_CAUNode**](msft-caunode.md)
</dt> </dl>

 

 





