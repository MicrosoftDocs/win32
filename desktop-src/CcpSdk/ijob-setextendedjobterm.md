---
Description: 'Sets the application-defined extended term on the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0a6dd44c-2496-495b-9015-e00b250193f2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::SetExtendedJobTerm method'
---

# IJob::SetExtendedJobTerm method

Sets the application-defined extended term on the job.

## Syntax


```C++
HRESULT SetExtendedJobTerm(
  [in] BSTR Name,
  [in] BSTR Value
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the extended term to add. The term is limited to 80 Unicode characters.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

The value of the extended term. The value is limited to 1,024 Unicode characters.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Use this method to add or update your own terms that are passed to the submission and activation filters. For a list of predefined job terms, see the Remarks section of [**ICluster::ModifyJobTerm**](icluster-modifyjobterm.md).

After adding the job to the cluster, use the [**ICluster::ModifyJobTerm**](icluster-modifyjobterm.md) to add or update the extended job terms.

To retrieve the current extended terms, call the [**IJob::get\_ExtendedJobTerms**](ijob-get-extendedjobterms.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_ExtendedJobTerms**](ijob-get-extendedjobterms.md)
</dt> <dt>

[**ITask::SetExtendedTaskTerm**](itask-setextendedtaskterm.md)
</dt> </dl>

 

 




