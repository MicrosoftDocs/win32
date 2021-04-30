---
description: An HRECOWORDLIST handle is used to manage a word list you attach to a recognizer context. You use a word list to improve recognition results.
ms.assetid: 7333307b-1857-48a7-bb9f-bdbd8530f093
title: HRECOWORDLIST Handle (Recapis.h)
ms.topic: reference
ms.date: 05/31/2018
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
| [**AddWordsToWordList**](/windows/desktop/api/recapis/nf-recapis-addwordstowordlist) | Adds one or more words to the word list.<br/> |
| [**DestroyWordList**](/windows/desktop/api/recapis/nf-recapis-destroywordlist)       | Destroys the current word list.<br/>          |
| [**MakeWordList**](/windows/desktop/api/recapis/nf-recapis-makewordlist)             | Creates a word list.<br/>                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Recapis.h</dt> </dl> |



## See also

<dl> <dt>

[**SetWordList Function**](/windows/desktop/api/recapis/nf-recapis-setwordlist)
</dt> </dl>

 

 




