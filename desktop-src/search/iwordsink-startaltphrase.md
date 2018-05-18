---
Description: 'Indicates the boundary between phrases in a sequence of alternative phrases that a word breaker generates during index time.'
ms.assetid: '3F3B6761-887B-426E-A44F-E636397180C7'
title: 'IWordSink::StartAltPhrase method'
---

# IWordSink::StartAltPhrase method

Indicates the boundary between phrases in a sequence of alternative phrases that a word breaker generates during index time.

## Syntax


```C++
HRESULT StartAltPhrase();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                           | Description                                                                                |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| <dl> <dt>**WBREAK\_E\_QUERY\_ONLY**</dt> </dl> | [**StartAltPhrase**](iwordsink-startaltphrase.md) is called during query time.<br/> |



 

## Remarks

Each alternative phrase starts with a **StartAltPhrase** call. The phrase is put in the [**IWordSink**](iwordsink.md) object through subsequent calls to the [**IWordSink::PutWord**](iwordsink-putword.md) or [**IWordSink::PutAltWord**](iwordsink-putaltword.md) method. The final alternative phrase in a sequence of phrases is terminated with a call to the [**IWordSink::EndAltPhrase**](iwordsink-endaltphrase.md) method.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Search.h</dt> </dl> |



## See also

<dl> <dt>

[**IWordSink**](iwordsink.md)
</dt> </dl>

 

 




