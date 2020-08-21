---
title: ITfContextRenderingMarkup GetRenderingMarkup method
description: The ITfContextRenderingMarkup GetRenderingMarkup method retrieves an enumerator of the rendering markups for the given range.
ms.assetid: fe060eab-8a6b-4eb7-9c7f-353b887657d8
keywords:
- GetRenderingMarkup method Text Services Framework
- GetRenderingMarkup method Text Services Framework , ITfContextRenderingMarkup interface
- ITfContextRenderingMarkup interface Text Services Framework , GetRenderingMarkup method
topic_type:
- apiref
api_name:
- ITfContextRenderingMarkup.GetRenderingMarkup
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ITfContextRenderingMarkup::GetRenderingMarkup method

The **ITfContextRenderingMarkup::GetRenderingMarkup** method retrieves an enumerator of the rendering markups for the given range.

## Syntax


```C++
HRESULT GetRenderingMarkup(
  [in]  TfEditCookie           ec,
  [in]  DWORD                  dwFlags,
  [in]  ITfRange               *pRangeCover,
  [out] IEnumTfRenderingMarkup **ppEnum
);
```



## Parameters

<dl> <dt>

*ec* \[in\]
</dt> <dd>

\[in\] A read only edit cookie to access the context.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

\[in\]



| Value                                                                                                                                                                                         | Meaning                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="TF_GRM_INCLUDE_PROPERTY"></span><span id="tf_grm_include_property"></span><dl> <dt>**TF\_GRM\_INCLUDE\_PROPERTY**</dt> </dl> | If this bit is 1, the enumerator will include the GUID\_PROP\_ATTRIBUTE property.<br/> |



 

</dd> <dt>

*pRangeCover* \[in\]
</dt> <dd>

\[in\] A pointer to an [ITfRange](/windows/desktop/api/Msctf/nn-msctf-itfrange) interface of the range to enumerate the rendering markups.

</dd> <dt>

*ppEnum* \[out\]
</dt> <dd>

\[out\] A pointer to retrieve [IEnumTfRenderingMarkup](/windows/desktop/TSF/ienumtfrenderingmarkup) interface pointer.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                | Description                           |
|--------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method was successful.<br/> |



 

## Remarks

> [!Note]  
> This method is not currently in the public header files. To use this API, you must MIDL-compile the [prototype](prototypes.md).

 

 

