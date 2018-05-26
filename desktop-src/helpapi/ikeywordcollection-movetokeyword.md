---
title: IKeywordCollection MoveToKeyword method
description: Sets current element in the collection the first occurrence of the supplied string
ms.assetid: dcffc9ef-5c2d-41d0-a50d-5491d8de60d8
keywords:
- MoveToKeyword method HelpAPI
- MoveToKeyword method HelpAPI , IKeywordCollection interface
- IKeywordCollection interface HelpAPI , MoveToKeyword method
topic_type:
- apiref
api_name:
- IKeywordCollection.MoveToKeyword
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IKeywordCollection::MoveToKeyword method

Sets current element in the collection the first occurrence of the supplied string

## Syntax


```C++
HRESULT MoveToKeyword(
  [in]          BSTR partialKeyword,
  [out, retval] long *pRetVal
);
```



## Parameters

<dl> <dt>

*partialKeyword* \[in\]
</dt> <dd></dd> <dt>

*pRetVal* \[out, retval\]
</dt> <dd></dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**IKeywordCollection**](ikeywordcollection.md)
</dt> </dl>

 

 





