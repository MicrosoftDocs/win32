---
Description: 'Retrieves the application-defined properties that were added to the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8e25180f-05c8-416b-a6c9-6fa270adac01'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::GetCustomProperties method'
---

# ISchedulerTask::GetCustomProperties method

Retrieves the application-defined properties that were added to the task.

## Syntax


```C++
HRESULT GetCustomProperties(
  [out] INameValueCollection **ppProperties
);
```



## Parameters

<dl> <dt>

*ppProperties* \[out\]
</dt> <dd>

An [**INameValueCollection**](inamevaluecollection2.md) interface that contains the collection of properties. Each item in the collection is an [**INameValue**](inamevalue2.md) interface that contains the property name and value. To retrieve the list of **INameValue** interfaces, call the [**INameValueCollection::GetEnumerator**](inamevaluecollection2-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **INameValue** interface. The collection is empty if no properties have been set.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

To set custom properties, call the [**ISchedulerTask::SetCustomProperty**](ischedulertask-setcustomproperty.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask::SetCustomProperty**](ischedulertask-setcustomproperty.md)
</dt> </dl>

 

 




