---
title: IEnumTfRenderingMarkup Clone method
description: The IEnumTfRenderingMarkup Clone method creates a copy of the enumerator object.
ms.assetid: f1b0ccf9-36d1-4eff-af7c-d7fb4f0e9104
keywords:
- Clone method Text Services Framework
- Clone method Text Services Framework , IEnumTfRenderingMarkup interface
- IEnumTfRenderingMarkup interface Text Services Framework , Clone method
topic_type:
- apiref
api_name:
- IEnumTfRenderingMarkup.Clone
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IEnumTfRenderingMarkup::Clone method

The **IEnumTfRenderingMarkup::Clone** method creates a copy of the enumerator object.

## Syntax


```C++
HRESULT Clone(
  [out] IEnumTfRenderingMarkup **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* \[out\]
</dt> <dd>

\[out\] A pointer to a [IEnumTfRenderingMarkup](/windows/desktop/TSF/ienumtfrenderingmarkup) interface.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                    |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>          |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | An unspecified error occurred.<br/>      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One or more parameters are invalid.<br/> |



 

## Remarks

> [!Note]  
> This method is not currently in the public header files. To use this API, you must MIDL-compile the [prototype](prototypes.md).

 

 

