---
Description: 'Puts the original word form in the IWordFormSink object.'
ms.assetid: '333A3109-6C0A-42AE-9E10-87F53C7F737C'
title: 'IWordFormSink::PutWord method'
---

# IWordFormSink::PutWord method

Puts the original word form in the [**IWordFormSink**](iwordformsink.md) object.

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

**PutWord** is called from the [**GenerateWordForms**](search._search_istemmer_generatewordforms) method of the [**IStemmer**](search._search_istemmer) implementation. This method handles the original form of a word and is called last. All preceding alternative forms for a word are put in the [**IWordFormSink**](iwordformsink.md) object by calling [**IWordFormSink::PutAltWord**](iwordformsink-putphrase.md).

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Search.h</dt> </dl> |



## See also

<dl> <dt>

[**IWordFormSink**](iwordformsink.md)
</dt> </dl>

 

 




