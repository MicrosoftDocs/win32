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

**[**tomCommentsStory**](https://www.bing.com/search?q=**tomCommentsStory**)**
</dt> <dt>

**[**tomEndnotesStory**](https://www.bing.com/search?q=**tomEndnotesStory**)**
</dt> <dt>

**[**tomEvenPagesFooterStory**](https://www.bing.com/search?q=**tomEvenPagesFooterStory**)**
</dt> <dt>

**[**tomEvenPagesHeaderStory**](https://www.bing.com/search?q=**tomEvenPagesHeaderStory**)**
</dt> <dt>

**[**tomFindStory**](https://www.bing.com/search?q=**tomFindStory**)**
</dt> <dt>

**[**tomFirstPageFooterStory**](https://www.bing.com/search?q=**tomFirstPageFooterStory**)**
</dt> <dt>

**[**tomFirstPageHeaderStory**](https://www.bing.com/search?q=**tomFirstPageHeaderStory**)**
</dt> <dt>

**[**tomFootnotesStory**](https://www.bing.com/search?q=**tomFootnotesStory**)**
</dt> <dt>

**[**tomMainTextStory**](https://www.bing.com/search?q=**tomMainTextStory**)**
</dt> <dt>

**[**tomPrimaryFooterStory**](https://www.bing.com/search?q=**tomPrimaryFooterStory**)**
</dt> <dt>

**[**tomPrimaryHeaderStory**](https://www.bing.com/search?q=**tomPrimaryHeaderStory**)**
</dt> <dt>

**[**tomReplaceStory**](https://www.bing.com/search?q=**tomReplaceStory**)**
</dt> <dt>

**[**tomScratchStory**](https://www.bing.com/search?q=**tomScratchStory**)**
</dt> <dt>

**[**tomTextFrameStory**](https://www.bing.com/search?q=**tomTextFrameStory**)**
</dt> <dt>

**[**tomUnknownStory**](https://www.bing.com/search?q=**tomUnknownStory**)**
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

 

 





