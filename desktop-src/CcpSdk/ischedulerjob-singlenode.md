---
Description: 'Retrieves or sets a value that indicates whether all resources such as cores or sockets should be allocated on one node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '202AD79B-94D8-4EAC-B436-F52014155570'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::SingleNode property'
---

# ISchedulerJob::SingleNode property

Retrieves or sets a value that indicates whether all resources such as cores or sockets should be allocated on one node.

This property is read/write.

## Syntax


```C++
HRESULT put_SingleNode(
  [in]  VARIANT_BOOL value
);

HRESULT get_SingleNode(
  [out] VARIANT_BOOL *pValue
);
```



## Property value

VARIANT\_TRUE if all resources should be allocated on one node; otherwise, VARIANT\_FALSE. The default is VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Requirements



|                         |                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Pack 2012 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>      |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




