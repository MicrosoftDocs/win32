---
title: ITopicCollection MoveTo method
description: Sets current element in the collection the specified index
ms.assetid: 02022698-d5eb-44f1-809d-51398119dcf3
keywords:
- MoveTo method HelpAPI
- MoveTo method HelpAPI , ITopicCollection interface
- ITopicCollection interface HelpAPI , MoveTo method
topic_type:
- apiref
api_name:
- ITopicCollection.MoveTo
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

# ITopicCollection::MoveTo method

Sets current element in the collection the specified index

## Syntax


```C++
HRESULT MoveTo(
  [in] long index
);
```



## Parameters

<dl> <dt>

*index* \[in\]
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

 

 





