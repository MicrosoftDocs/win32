---
title: IHelpFilter Count method
description: method Count - returns the number of filter elements in the collection
ms.assetid: 36c077dc-731a-46f2-8a99-ccf29df036a3
keywords:
- Count method HelpAPI
- Count method HelpAPI , IHelpFilter interface
- IHelpFilter interface HelpAPI , Count method
topic_type:
- apiref
api_name:
- IHelpFilter.Count
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

# IHelpFilter::Count method

method Count - returns the number of filter elements in the collection

## Syntax


```C++
HRESULT Count(
  [out, retval] long *pRetVal
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

[**IHelpFilter**](ihelpfilter.md)
</dt> </dl>

 

 





