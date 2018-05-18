---
title: ITopic TableOfContentsHasChildren property
description: For TableOfContents calls, returns true if the topic has children. It will not be relevant data for non-TOC calls.
ms.assetid: 'c6182457-93d7-440e-84b8-01d902de50c2'
keywords: ["TableOfContentsHasChildren property HelpAPI", "TableOfContentsHasChildren property HelpAPI , ITopic interface", "ITopic interface HelpAPI , TableOfContentsHasChildren property"]
topic_type:
- apiref
api_name:
- ITopic.TableOfContentsHasChildren
- ITopic.get_TableOfContentsHasChildren
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ITopic::TableOfContentsHasChildren property

For TableOfContents calls, returns true if the topic has children. It will not be relevant data for non-TOC calls.

This property is read-only.

## Syntax


```C++
HRESULT get_TableOfContentsHasChildren(
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Property value

True if the topic has children; otherwise false.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITopic**](itopic.md)
</dt> </dl>

 

 





