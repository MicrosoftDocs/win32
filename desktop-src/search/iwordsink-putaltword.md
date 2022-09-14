---
description: Puts an alternative word and its position in the IWordSink object.
ms.assetid: 5C8A9B30-F9B5-42E9-ADAC-A11230F0C2FA
title: IWordSink::PutAltWord method (Search.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWordSink.PutAltWord
api_type: 
- COM
api_location: 
- search.h
---

# IWordSink::PutAltWord method

Puts an alternative word and its position in the [**IWordSink**](iwordsink.md) object.

## Syntax


```C++
HRESULT PutAltWord(
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

A pointer to a buffer that contains an alternative form of a word from the source text. This parameter is not modified by **PutAltWord**. You can pass the *pTextSource* parameter from [**IWordBreaker::BreakText**](/windows/win32/api/indexsrv/nf-indexsrv-iwordbreaker-breaktext) as appropriate.

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
| <dl> <dt>**S\_OK**</dt> </dl>                     | The operation was completed successfully. Also indicates that no more text remains to be processed.<br/>                                            |
| <dl> <dt>**LANGUAGE\_S\_LARGE\_WORD** </dt> </dl> | Value of *cwc* is larger than the value for *ulMaxTokenSize* that is specified in [**IWordBreaker::Init**](/windows/win32/api/indexsrv/nf-indexsrv-iwordbreaker-init). <br/> |



 

## Remarks

**PutAltWord** puts an alternative form of a word in the [**IWordSink**](iwordsink.md). The word is put in the same position as the original word in the text source (*pTextSource* in [**IWordBreaker::BreakText**](/windows/win32/api/indexsrv/nf-indexsrv-iwordbreaker-breaktext)). By default, **PutAltWord** terminates words with a **WORDREP\_BREAK\_EOW** break type from the [**WORDREP\_BREAK\_TYPE**](/previous-versions/windows/desktop/legacy/ff819130(v=vs.85)) enumerated type.

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

 

 
