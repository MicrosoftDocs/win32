---
title: IHelpFilter Add method
description: method Add - Adds a filter key/value pair to the filter list
ms.assetid: '13f857e8-5b0c-46fb-bc2c-c19d146daa5b'
keywords: ["Add method HelpAPI", "Add method HelpAPI , IHelpFilter interface", "IHelpFilter interface HelpAPI , Add method"]
topic_type:
- apiref
api_name:
- IHelpFilter.Add
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IHelpFilter::Add method

method Add - Adds a filter key/value pair to the filter list

## Syntax


```C++
HRESULT Add(
  [in] BSTR key,
  [in] BSTR value
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd></dd> <dt>

*value* \[in\]
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

 

 





