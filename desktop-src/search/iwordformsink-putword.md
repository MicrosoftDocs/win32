---
description: Puts the original word form in the IWordFormSink object.
ms.assetid: 333A3109-6C0A-42AE-9E10-87F53C7F737C
title: IWordFormSink::PutWord method (Search.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWordFormSink.PutWord
api_type: 
- COM
api_location: 
- search.h
---

# IWordFormSink::PutWord method

Puts the original word form in the [**IWordFormSink**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordformsink) object.

## Syntax


```C++
HRESULT PutWord(
  [in] const WCHAR *pwcInBuf ,
  [in]       ULONG cwc
);
```



## Parameters

<dl> <dt>

*pwcInBuf* \[in\]
</dt> <dd>

A pointer to a buffer that contains the final alternative form of a word, which is always the original word.

</dd> <dt>

*cwc* \[in\]
</dt> <dd>

The number of characters in *pwcInBuf*.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                          | Description                                           |
|--------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The operation was completed successfully. <br/> |



 

## Remarks

**PutWord** is called from the [**GenerateWordForms**](/windows/win32/api/indexsrv/nf-indexsrv-istemmer-generatewordforms) method of the [**IStemmer**](/windows/win32/api/indexsrv/nn-indexsrv-istemmer) implementation. This method handles the original form of a word and is called last. All preceding alternative forms for a word are put in the [**IWordFormSink**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordformsink) object by calling [**IWordFormSink::PutAltWord**](iwordformsink-putphrase.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Search.h</dt> </dl> |



## See also

<dl> <dt>

[**IWordFormSink**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordformsink)
</dt> </dl>

 

 
