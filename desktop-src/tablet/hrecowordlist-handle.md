---
Description: 'An HRECOWORDLIST handle is used to manage a word list you attach to a recognizer context. You use a word list to improve recognition results.'
ms.assetid: '7333307b-1857-48a7-bb9f-bdbd8530f093'
title: HRECOWORDLIST Handle
---

# HRECOWORDLIST Handle

An **HRECOWORDLIST** handle is used to manage a word list you attach to a recognizer context. You use a word list to improve recognition results.


```C++
typedef HANDLE HRECOWORDLIST;
```



## Remarks

The following function use an **HRECOWORDLIST**.



| Function                                         | Description                                         |
|--------------------------------------------------|-----------------------------------------------------|
| [**AddWordsToWordList**](addwordstowordlist.md) | Adds one or more words to the word list.<br/> |
| [**DestroyWordList**](destroywordlist.md)       | Destroys the current word list.<br/>          |
| [**MakeWordList**](makewordlist.md)             | Creates a word list.<br/>                     |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Recapis.h</dt> </dl> |



## See also

<dl> <dt>

[**SetWordList Function**](setwordlist.md)
</dt> </dl>

 

 




