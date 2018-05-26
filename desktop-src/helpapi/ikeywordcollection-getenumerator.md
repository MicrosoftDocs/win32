---
title: IKeywordCollection GetEnumerator method
description: Returns an enumerator that iterates through a collection
ms.assetid: b8537cc6-c98c-4145-b7ce-d869586a2c70
keywords:
- GetEnumerator method HelpAPI
- GetEnumerator method HelpAPI , IKeywordCollection interface
- IKeywordCollection interface HelpAPI , GetEnumerator method
topic_type:
- apiref
api_name:
- IKeywordCollection.GetEnumerator
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

# IKeywordCollection::GetEnumerator method

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

[**IKeywordCollection**](ikeywordcollection.md)
</dt> </dl>

 

 





