---
Description: 'Retrieves the cluster's configuration parameters.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c36e3fd4-b669-46db-98e1-63c4694489c3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::ClusterParameters property'
---

# IScheduler::ClusterParameters property

Retrieves the cluster's configuration parameters.

This property is read-only.

## Syntax


```C++
HRESULT get_ClusterParameters(
  [out] INameValueCollection **pParameters
);
```



## Property value

An [**INameValueCollection**](inamevaluecollection2.md) interface that contains a collection of configuration parameters for the cluster. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INameValue**](inamevalue2.md) interface.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To set the configuration parameters, call the [**IScheduler::SetClusterParameter**](ischeduler-setclusterparameter.md) method. For a list of parameters, see the Remarks section of **SetClusterParameter**.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::SetClusterParameter**](ischeduler-setclusterparameter.md)
</dt> </dl>

 

 




