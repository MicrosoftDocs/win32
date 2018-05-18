---
title: IHelpFilter Item method
description: method Item - returns the filter value of a provided filter key
ms.assetid: 'da856d11-8bee-48eb-aa7c-b1aeabccee72'
keywords: ["Item method HelpAPI", "Item method HelpAPI , IHelpFilter interface", "IHelpFilter interface HelpAPI , Item method"]
topic_type:
- apiref
api_name:
- IHelpFilter.Item
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IHelpFilter::Item method

method Item - returns the filter value of a provided filter key

## Syntax


```C++
HRESULT Item(
  [in]          BSTR      key,
  [out, retval] SAFEARRAY BSTR
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd></dd> <dt>

*BSTR* \[out, retval\]
</dt> <dd></dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**IHelpFilter**](ihelpfilter.md)
</dt> </dl>

 

 





