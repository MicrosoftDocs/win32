---
title: EM_GETSTORYTYPE message
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

**[**tomCommentsStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomEndnotesStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomEvenPagesFooterStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomEvenPagesHeaderStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomFindStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomFirstPageFooterStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomFirstPageHeaderStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomFootnotesStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomMainTextStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomPrimaryFooterStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomPrimaryHeaderStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomReplaceStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomScratchStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomTextFrameStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
</dt> <dt>

**[**tomUnknownStory**](/windows/desktop/api/Tom/ne-tom-__midl___midl_itf_tom_0000_0000_0001)**
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

 

 





