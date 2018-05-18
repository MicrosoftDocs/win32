---
Description: 'Sets the application-defined extended term for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4edf71ac-2a13-4e00-b554-bf003a0476d1'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::SetExtendedTaskTerm method'
---

# ITask::SetExtendedTaskTerm method

Sets the application-defined extended term for the task.

## Syntax


```C++
HRESULT SetExtendedTaskTerm(
  [in] BSTR Name,
  [in] BSTR Value
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the extended term. The term is limited to 80 Unicode characters.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

The value of the task term. The value is limited to 1,024 Unicode characters.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Use this method to define your own task terms that are passed to the submission and activation filters as part of the XML.

To retrieve the current extended terms, call the [**ITask::get\_ExtendedTaskTerms**](itask-get-extendedtaskterms.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJob::SetExtendedJobTerm**](ijob-setextendedjobterm.md)
</dt> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_ExtendedTaskTerms**](itask-get-extendedtaskterms.md)
</dt> </dl>

 

 




