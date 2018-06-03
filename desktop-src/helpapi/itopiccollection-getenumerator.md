---
title: ITopicCollection GetEnumerator method
description: Returns an enumerator that iterates through a collection
ms.assetid: 9fab0ad4-528f-4179-a2e6-7a2666d85d5a
keywords:
- GetEnumerator method HelpAPI
- GetEnumerator method HelpAPI , ITopicCollection interface
- ITopicCollection interface HelpAPI , GetEnumerator method
topic_type:
- apiref
api_name:
- ITopicCollection.GetEnumerator
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

# ITopicCollection::GetEnumerator method

Returns an enumerator that iterates through a collection

## Syntax


```C++
HRESULT GetEnumerator(
  [out, retval] IEnumVARIANT **pRetVal
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

 

 





