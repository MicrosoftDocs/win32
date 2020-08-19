---
title: IEnumTfRenderingMarkup Next method
description: The IEnumTfRenderingMarkup Next method obtains, from the current position, the specified number of elements in the enumeration sequence.
ms.assetid: a3aec919-2c65-4e65-9430-d73fdaf5d28e
keywords:
- Next method Text Services Framework
- Next method Text Services Framework , IEnumTfRenderingMarkup interface
- IEnumTfRenderingMarkup interface Text Services Framework , Next method
topic_type:
- apiref
api_name:
- IEnumTfRenderingMarkup.Next
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IEnumTfRenderingMarkup::Next method

The **IEnumTfRenderingMarkup::Next** method obtains, from the current position, the specified number of elements in the enumeration sequence.

## Syntax


```C++
HRESULT Next(
  [out] ULONG ulCount,
  [out]       ppElement,
  [out] ULONG *pcFetched
);
```



## Parameters

<dl> <dt>

*ulCount* \[out\]
</dt> <dd>

\[out\] Specifies the number of elements to obtain.

</dd> <dt>

*ppElement* \[out\]
</dt> <dd>

\[out\] Pointer to an array of [TF\_RENDERINGMARKUP](/windows/desktop/TSF/tf-renderingmarkup) structures. This array must be at least *ulCount* elements in size.

</dd> <dt>

*pcFetched* \[out\]
</dt> <dd>

\[out\] Pointer to a ULONG value that receives the number of elements actually obtained. This value can be less than the number of items requested. This parameter can be **NULL**.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                                                                                         |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>                                                                               |
| <dl> <dt>**S\_FALSE**</dt> </dl>      | The method reached the end of the enumeration before the specified number of elements could be obtained.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One or more parameters are invalid.<br/>                                                                      |



 

## Remarks

> [!Note]  
> This method is not currently in the public header files. To use this API, you must MIDL-compile the [prototype](prototypes.md).

 

 

