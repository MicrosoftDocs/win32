---
Description: 'Retrieves the application-defined extended job terms.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'be7903d8-0c23-46b8-9b3d-e74321c7e325'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_ExtendedJobTerms method'
---

# IJob::get\_ExtendedJobTerms method

Retrieves the application-defined extended job terms.

## Syntax


```C++
HRESULT get_ExtendedJobTerms(
  [out] INameValueCollection **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**INameValueCollection**](inamevaluecollection.md) interface that contains a collection of the extended terms. To retrieve the list of [**INameValue**](inamevalue.md) interfaces, call the [**INameValueCollection::GetEnumerator**](inamevaluecollection-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **INameValue** interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

To set the extended job terms, call the [**IJob::SetExtendedJobTerm**](ijob-setextendedjobterm.md) method.

For a list of job terms, see the Remarks section of [**ICluster::ModifyJobTerm**](icluster-modifyjobterm.md).

## Examples

For an example that enumerates the extended terms of a job, see [Listing Jobs](listing-jobs.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::SetExtendedJobTerm**](ijob-setextendedjobterm.md)
</dt> </dl>

 

 




