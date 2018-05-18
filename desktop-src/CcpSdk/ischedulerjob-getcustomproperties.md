---
Description: 'Retrieves the application-defined properties.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '50f273ff-53e5-4a5c-a3a7-29f38a462d20'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::GetCustomProperties method'
---

# ISchedulerJob::GetCustomProperties method

Retrieves the application-defined properties.

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

An [**INameValueCollection**](inamevaluecollection2.md) interface that contains the collection of properties. Each item in the collection is an [**INameValue**](inamevalue2.md) interface that contains the property name and value. To retrieve the list of **INameValue** interfaces, call the [**INameValueCollection::GetEnumerator**](inamevaluecollection2-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **INameValue** interface. The collection is empty if no properties have been defined.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

To add application-defined properties to the job, call the [**ISchedulerJob::SetCustomProperty**](ischedulerjob-setcustomproperty.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::SetCustomProperty**](ischedulerjob-setcustomproperty.md)
</dt> </dl>

 

 




