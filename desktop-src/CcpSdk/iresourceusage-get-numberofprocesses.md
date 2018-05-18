---
Description: 'Retrieves the number of processes being used by the job or task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '57623126-e69b-456b-acbb-cb340db34d39'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IResourceUsage::get\_NumberOfProcesses method'
---

# IResourceUsage::get\_NumberOfProcesses method

Retrieves the number of processes being used by the job or task.

## Syntax


```C++
HRESULT get_NumberOfProcesses(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of processes.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Use this value only when the status of the job or task is Running.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IResourceUsage**](iresourceusage.md)
</dt> </dl>

 

 




