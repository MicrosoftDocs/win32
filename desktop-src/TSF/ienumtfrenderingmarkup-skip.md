---
title: IEnumTfRenderingMarkup Skip method
description: The IEnumTfRenderingMarkup Skip method obtains, from the current position, the specified number of elements in the enumeration sequence.
ms.assetid: d328dfe3-36ab-4daf-8809-ad6686ca5dae
keywords:
- Skip method Text Services Framework
- Skip method Text Services Framework , IEnumTfRenderingMarkup interface
- IEnumTfRenderingMarkup interface Text Services Framework , Skip method
topic_type:
- apiref
api_name:
- IEnumTfRenderingMarkup.Skip
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IEnumTfRenderingMarkup::Skip method

The **IEnumTfRenderingMarkup::Skip** method obtains, from the current position, the specified number of elements in the enumeration sequence.

## Syntax


```C++
HRESULT Skip(
  [in] ULONG ulCount
);
```



## Parameters

<dl> <dt>

*ulCount* \[in\]
</dt> <dd>

\[in\] Specifies the number of elements to skip.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                   | Description                                                                                                        |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The method was successful.<br/>                                                                              |
| <dl> <dt>**S\_FALSE**</dt> </dl> | The method reached the end of the enumeration before the specified number of elements could be skipped.<br/> |



 

## Remarks

> [!Note]  
> This method is not currently in the public header files. To use this API, you must MIDL-compile the [prototype](prototypes.md).

 

 

 





