---
Description: 'Retrieves the application-defined extended terms for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a791681c-2ada-433e-8972-21af43374907'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_ExtendedTaskTerms method'
---

# ITask::get\_ExtendedTaskTerms method

Retrieves the application-defined extended terms for the task.

## Syntax


```C++
HRESULT get_ExtendedTaskTerms(
  [out] INameValueCollection **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**INameValueCollection**](inamevaluecollection.md) interface that contains the collection of extended terms. To retrieve the list, call the [**INameValueCollection::GetEnumerator**](inamevaluecollection-getenumerator.md) method. The variant type for each item in the collection is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INameValue**](inamevalue.md) interface. The collection is empty if no terms have been set.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

For more information about task terms, see [**ITask::SetExtendedTaskTerm**](itask-setextendedtaskterm.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::SetExtendedTaskTerm**](itask-setextendedtaskterm.md)
</dt> </dl>

 

 




