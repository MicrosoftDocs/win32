---
title: ITopic Title property
description: Returns topic title
ms.assetid: 77ca327b-10fa-41ff-9e03-549a747b84a2
keywords:
- Title property HelpAPI
- Title property HelpAPI , ITopic interface
- ITopic interface HelpAPI , Title property
topic_type:
- apiref
api_name:
- ITopic.Title
- ITopic.get_Title
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

# ITopic::Title property

Returns topic title

This property is read-only.

## Syntax


```C++
HRESULT get_Title(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The topic's title.

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

 

 





