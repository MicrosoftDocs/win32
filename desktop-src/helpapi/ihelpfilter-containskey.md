---
title: IHelpFilter ContainsKey method
description: method ContainsKey - Check to see if a filter key is in the filter list
ms.assetid: 3d224357-9574-4302-8708-55a47b974b06
keywords:
- ContainsKey method HelpAPI
- ContainsKey method HelpAPI , IHelpFilter interface
- IHelpFilter interface HelpAPI , ContainsKey method
topic_type:
- apiref
api_name:
- IHelpFilter.ContainsKey
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

# IHelpFilter::ContainsKey method

method ContainsKey - Check to see if a filter key is in the filter list

## Syntax


```C++
HRESULT ContainsKey(
  [in]          BSTR         key,
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

*key* \[in\]
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

[**IHelpFilter**](ihelpfilter.md)
</dt> </dl>

 

 





