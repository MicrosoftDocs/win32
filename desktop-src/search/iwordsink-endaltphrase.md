---
description: Indicates the end of the final phrase in a sequence of alternative phrases that a word breaker generates during index time.
ms.assetid: 50E4E208-A290-42B7-9152-9472C01B20D5
title: IWordSink::EndAltPhrase method (Search.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWordSink.EndAltPhrase
api_type: 
- COM
api_location: 
- search.h
---

# IWordSink::EndAltPhrase method

Indicates the end of the final phrase in a sequence of alternative phrases that a word breaker generates during index time.

## Syntax


```C++
HRESULT EndAltPhrase();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                           | Description                                                                            |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**WBREAK\_E\_QUERY\_ONLY**</dt> </dl> | [**EndAltPhrase**](iwordsink-endaltphrase.md) is called during query time.<br/> |



 

## Remarks

[**IWordBreaker**](/windows/win32/api/indexsrv/nn-indexsrv-iwordbreaker) implementations call **IWordSink::EndAltPhrase** from the [**IWordBreaker::BreakText**](/windows/win32/api/indexsrv/nf-indexsrv-iwordbreaker-breaktext) method to terminate a sequence of alternative phrases. The [**IWordSink::StartAltPhrase**](iwordsink-startaltphrase.md) method is called to indicate the end of one phrase and the beginning of another in a sequence of phrases. Only the last phrase in a sequence is terminated with a call to **EndAltPhrase**.

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

 

 
