---
Description: Handles words identified by word breaks during both index time and query time.
ms.assetid: 220FCAE5-D22D-45ED-9689-E78C0D8E0BB3
title: IWordSink interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IWordSink interface

Handles words identified by word breaks during both index time and query time.

## Members

The **IWordSink** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IWordSink** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWordSink** interface has these methods.



| Method                                             | Description                                                                                                                             |
|:---------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**EndAltPhrase**](iwordsink-endaltphrase.md)     | Indicates the end of the final phrase in a sequence of alternative phrases that a word breaker generates during index time.<br/>  |
| [**PutAltWord**](iwordsink-putaltword.md)         | Puts an alternative word and its position in the **IWordSink** object.<br/>                                                       |
| [**PutBreak**](iwordsink-putbreak.md)             | Puts a break after the preceding word.<br/>                                                                                       |
| [**PutWord**](iwordsink-putword.md)               | Puts a word and its position in the **IWordSink** object.<br/>                                                                    |
| [**StartAltPhrase**](iwordsink-startaltphrase.md) | Indicates the boundary between phrases in a sequence of alternative phrases that a word breaker generates during index time.<br/> |



 

## Remarks

Windows Search creates and initializes instances of the **IWordSink** object. The **IWordSink** object receives the *fQuery* parameter during initialization and uses this parameter to determine the word-breaking context in which the object is used.

[**IWordBreaker**](https://msdn.microsoft.com/VS|search|~\search\wds3x\reference\ifaces\dataaddins\iwordbreaker\iwordbreaker.htm) implementations receive a pointer to the **IWordSink** object in the [**IWordBreaker::BreakText**](https://msdn.microsoft.com/VS|search|~\search\wds3x\reference\ifaces\dataaddins\iwordbreaker\breaktext.htm) method.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Search.h</dt> </dl> |



 

 




