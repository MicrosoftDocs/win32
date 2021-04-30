---
description: The following globally unique identifiers (GUIDs) are used by Windows Journal to identify custom properties on strokes or drawing attributes.
ms.assetid: a7488c26-b61f-47d8-a19b-d630a8c00875
title: Custom Property GUIDs
ms.topic: article
ms.date: 05/31/2018
---

# Custom Property GUIDs

The following globally unique identifiers (GUIDs) are used by Windows Journal to identify custom properties on strokes or drawing attributes.

## GUID\_STROKE\_TIMESTAMP


```C++
GUID_STROKE_TIMESTAMP = {4EA66C4-F33A-461B-B8FE-68070D9C7575}
```



This is a [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) structure that indicates the time at which the stroke was created or added to the document.


```C++
typedef struct _FILETIME {
    DWORD dwLowDateTime;
    DWORD dwHighDateTime;
} FILETIME, *PFILETIME;
```



## GUID\_STROKE\_TIMEID


```C++
GUID_STROKE_TIMEID = {50B6BC8-3B7D-4816-8C61-BC7E905B2132}
```



This is a **TIMEID** structure. It allows stroke order to be maintained across paste and drop operations. Without the **TIMEID** structure, the timestamp for all [**IInkStrokeDisp Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects cut and pasted in a [InkStrokes Collection](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) will be the same.


```C++
typedef struct tagTIMEID {
    FILETIME  tmFiletime;
    ULONG     uiOrder;
} TIMEID;
```



## GUID\_HIGHLIGHTER

This is a **BOOL**, where **TRUE**=highlighter ink, **FALSE**=regular ink. This is applied to drawing attributes.


```C++
GUID_HIGHLIGHTER = {9B6267B8-3968-4048-AB74-F490406A2DFA}
```



## GUID\_INK\_STYLE\_BOLD

This is a **BOOL**, where **TRUE**=bold ink, **FALSE**=normal. This is applied to drawing attributes.


```C++
GUID_INK_STYLE_BOLD = {E02FB5C1-9693-4312-A434-00DE7F3AD493}
```



## GUID\_INK\_STYLE\_ITALICS

This is a **BOOL**, where **TRUE**=italicized ink, **FALSE**=normal. This is applied to drawing attributes.


```C++
GUID_INK_STYLE_ITALICS = {05253B51-49C6-4A04-8993-64DD9ABD842A}
```



## Related topics

<dl> <dt>

[**IJournalReader Interface**](ijournalreader.md)
</dt> </dl>

 

 
