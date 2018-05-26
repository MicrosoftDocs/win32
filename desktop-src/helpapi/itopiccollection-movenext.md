---
title: ITopicCollection MoveNext method
description: Advances the enumerator to the next element of the collection
ms.assetid: 2afd911e-4101-4a05-bb93-3ff4a91ea1bd
keywords:
- MoveNext method HelpAPI
- MoveNext method HelpAPI , ITopicCollection interface
- ITopicCollection interface HelpAPI , MoveNext method
topic_type:
- apiref
api_name:
- ITopicCollection.MoveNext
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

# ITopicCollection::MoveNext method

Advances the enumerator to the next element of the collection

## Syntax


```C++
HRESULT MoveNext(
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

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

[**ITopicCollection**](itopiccollection.md)
</dt> </dl>

 

 





