---
description: Puts a break after the preceding word.
ms.assetid: C8622067-D8CE-4099-8B9F-941720F4706B
title: IWordSink::PutBreak method (Search.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWordSink.PutBreak
api_type: 
- COM
api_location: 
- search.h
---

# IWordSink::PutBreak method

Puts a break after the preceding word.

## Syntax


```C++
HRESULT PutBreak(
  [in] WORDREP_BREAK_TYPE breakType
);
```



## Parameters

<dl> <dt>

*breakType* \[in\]
</dt> <dd>

A value from [**WORDREP\_BREAK\_TYPE**](/previous-versions/windows/desktop/legacy/ff819130(v=vs.85)) that indicates the type of break that the WordSink inserts after the preceding word. Each break occupies a unique position in the index. Therefore, inserting breaks between words changes the relative distance between words.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                          | Description                                          |
|--------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The operation was completed successfully.<br/> |



 

## Remarks

The [**IWordSinkPutWord**](iwordsink-putword.md) and [**IWordSink::PutAltWord**](iwordsink-putaltword.md) methods automatically insert an end-of-word break (EOW, indicated by the WORDREP\_BREAK\_EOW element of the [**WORDREP\_BREAK\_TYPE**](/previous-versions/windows/desktop/legacy/ff819130(v=vs.85)) enumerated type) after each word. Call the **PutBreak** method to insert a break type other than end of word. This method does not change the source text buffer (*pSourceText*) or increment the character count (*cwc*). However, it does increment the current position in the index and affects query results.

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

 

 
