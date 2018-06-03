---
title: ITopic TableOfContentsPosition property
description: Returns topics position in the table of contents
ms.assetid: a3bbe4f4-a14a-4118-9309-2c44cf54c88a
keywords:
- TableOfContentsPosition property HelpAPI
- TableOfContentsPosition property HelpAPI , ITopic interface
- ITopic interface HelpAPI , TableOfContentsPosition property
topic_type:
- apiref
api_name:
- ITopic.TableOfContentsPosition
- ITopic.get_TableOfContentsPosition
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITopic::TableOfContentsPosition property

Returns topics position in the table of contents

This property is read-only.

## Syntax


```C++
HRESULT get_TableOfContentsPosition(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The current position in the table of contents.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITopic**](itopic.md)
</dt> </dl>

 

 





