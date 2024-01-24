---
description: Puts a word and its position in the IWordSink object.
ms.assetid: 3D645BF6-895E-46E2-92A3-3E301CD228D8
title: IWordSink::PutWord method (Search.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWordSink.PutWord
api_type: 
- COM
api_location: 
- search.h
---

# IWordSink::PutWord method

Puts a word and its position in the [**IWordSink**](iwordsink.md) object.

## Syntax


```C++
HRESULT PutWord(
  [in]       ULONG cwc,
  [in] const WCHAR *pwcInBuf,
  [in]       ULONG cwcSrcLen,
  [in]       ULONG cwcSrcPos
);
```



## Parameters

<dl> <dt>

*cwc* \[in\]
</dt> <dd>

The number of characters in *pwcInBuf*.

</dd> <dt>

*pwcInBuf* \[in\]
</dt> <dd>

A pointer to a buffer that contains an alternative form of a word from the source text. This parameter is not modified by **PutWord**. You can pass the *pTextSource* parameter from [**IWordBreaker::BreakText**](/windows/win32/api/indexsrv/nf-indexsrv-iwordbreaker-breaktext) as appropriate.

</dd> <dt>

*cwcSrcLen* \[in\]
</dt> <dd>

The number of characters in the source text buffer (indicated by the *pTextSource* parameter to [**IWordBreaker::BreakText**](/windows/win32/api/indexsrv/nf-indexsrv-iwordbreaker-breaktext)) that correspond to the word contained in *pwcInBuf*.

</dd> <dt>

*cwcSrcPos* \[in\]
</dt> <dd>

The starting position of the word in *pwcInBuf* in the source text buffer (indicated by the *pTextSource* parameter to [**IWordBreaker::BreakText**](/windows/win32/api/indexsrv/nf-indexsrv-iwordbreaker-breaktext)).

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                              | Description                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | The operation was completed successfully. Also indicates that no more text is available to refill the buffer.<br/>                                  |
| <dl> <dt>**LANGUAGE\_S\_LARGE\_WORD** </dt> </dl> | Value of *cwc* is larger than the value for *ulMaxTokenSize* that is specified in [**IWordBreaker::Init**](/windows/win32/api/indexsrv/nf-indexsrv-iwordbreaker-init). <br/> |



 

## Remarks

We recommend that the **IWordSink::PutWord** method always contain the original word as found in *pTextSource*. Alternative forms of the word are passed to WordSink by using [**IWordSink::PutAltWord**](iwordsink-putaltword.md). We also recommend that the words in *pwcInBuf* match the source text as closely as possible. For example, retain capitalization and accents where possible.

This call must be made for every word retrieved from *pTextSource* except those for which the [**IWordSink::PutAltWord**](iwordsink-putaltword.md) call was made. The word is terminated with an EOW character when it is saved to the WordSink.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Search.h</dt> </dl> |



## See also

<dl> <dt>

[**IWordSink**](iwordsink.md)
</dt> </dl>

 

 
