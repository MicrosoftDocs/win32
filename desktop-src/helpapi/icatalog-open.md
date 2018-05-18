---
title: ICatalog Open method
description: method Open - opens a catalog given a valid catalog directory path and list of prioritized languages for fallback
ms.assetid: '83700b68-2a5d-4ae0-9ef3-82ebd3aa369b'
keywords: ["Open method HelpAPI", "Open method HelpAPI , ICatalog interface", "ICatalog interface HelpAPI , Open method"]
topic_type:
- apiref
api_name:
- ICatalog.Open
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalog::Open method

method Open - opens a catalog given a valid catalog directory path and list of prioritized languages for fallback

## Syntax


```C++
HRESULT Open(
  [in] BSTR      path,
  [in] SAFEARRAY BSTR
);
```



## Parameters

<dl> <dt>

*path* \[in\]
</dt> <dd></dd> <dt>

*BSTR* \[in\]
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

[**ICatalog**](icatalog.md)
</dt> </dl>

 

 





