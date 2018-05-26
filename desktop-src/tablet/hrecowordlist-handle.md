---
Description: An HRECOWORDLIST handle is used to manage a word list you attach to a recognizer context. You use a word list to improve recognition results.
ms.assetid: 7333307b-1857-48a7-bb9f-bdbd8530f093
title: HRECOWORDLIST Handle
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**AddWordsToWordList**](/windows/win32/recapis/nf-recapis-addwordstowordlist?branch=master) | Adds one or more words to the word list.<br/> |
| [**DestroyWordList**](/windows/win32/recapis/nf-recapis-destroywordlist?branch=master)       | Destroys the current word list.<br/>          |
| [**MakeWordList**](/windows/win32/recapis/nf-recapis-makewordlist?branch=master)             | Creates a word list.<br/>                     |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Recapis.h</dt> </dl> |



## See also

<dl> <dt>

[**SetWordList Function**](/windows/win32/recapis/nf-recapis-setwordlist?branch=master)
</dt> </dl>

 

 




