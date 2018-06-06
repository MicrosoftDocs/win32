---
title: EM\_GETSTORYTYPE message
description: Gets the story type.
ms.assetid: 06D87AA1-5AA3-4235-AC1D-045CE9975384
keywords:
- EM_GETSTORYTYPE message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETSTORYTYPE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EM\_GETSTORYTYPE message

Gets the story type.


```C++
#define EM_GETSTORYTYPE       (WM_USER + 290)
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The story index.

</dd> <dt>

*lParam* 
</dt> <dd>

Reserved; must be 0.

</dd> </dl>

## Return value

Returns the story type, which can be a client-defined custom value, or one of the following values:

<dl> <dt>

**[**tomCommentsStory**](tomconstants.md#tomcommentsstory)**
</dt> <dt>

**[**tomEndnotesStory**](tomconstants.md#tomendnotesstory)**
</dt> <dt>

**[**tomEvenPagesFooterStory**](tomconstants.md#tomevenpagesfooterstory)**
</dt> <dt>

**[**tomEvenPagesHeaderStory**](tomconstants.md#tomevenpagesheaderstory)**
</dt> <dt>

**[**tomFindStory**](tomconstants.md#tomfindstory)**
</dt> <dt>

**[**tomFirstPageFooterStory**](tomconstants.md#tomfirstpagefooterstory)**
</dt> <dt>

**[**tomFirstPageHeaderStory**](tomconstants.md#tomfirstpageheaderstory)**
</dt> <dt>

**[**tomFootnotesStory**](tomconstants.md#tomfootnotesstory)**
</dt> <dt>

**[**tomMainTextStory**](tomconstants.md#tommaintextstory)**
</dt> <dt>

**[**tomPrimaryFooterStory**](tomconstants.md#tomprimaryfooterstory)**
</dt> <dt>

**[**tomPrimaryHeaderStory**](tomconstants.md#tomprimaryheaderstory)**
</dt> <dt>

**[**tomReplaceStory**](tomconstants.md#tomreplacestory)**
</dt> <dt>

**[**tomScratchStory**](tomconstants.md#tomscratchstory)**
</dt> <dt>

**[**tomTextFrameStory**](tomconstants.md#tomtextframestory)**
</dt> <dt>

**[**tomUnknownStory**](tomconstants.md#tomunknownstory)**
</dt> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETSTORYTYPE**](em-setstorytype.md)
</dt> <dt>

[**ITextStoryRanges::Item**](/windows/desktop/api/Tom/nf-tom-itextstoryranges-item)
</dt> </dl>

 

 





