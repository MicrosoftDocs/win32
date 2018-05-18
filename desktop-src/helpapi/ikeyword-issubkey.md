---
title: IKeyword IsSubkey property
description: Returns a Boolean value indicating if the key is a subkey
ms.assetid: '7514e184-d3fd-413f-abf3-fa2d4c0f5d8f'
keywords: ["IsSubkey property HelpAPI", "IsSubkey property HelpAPI , IKeyword interface", "IKeyword interface HelpAPI , IsSubkey property"]
topic_type:
- apiref
api_name:
- IKeyword.IsSubkey
- IKeyword.get_IsSubkey
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IKeyword::IsSubkey property

Returns a Boolean value indicating if the key is a subkey

This property is read-only.

## Syntax


```C++
HRESULT get_IsSubkey(
  [out, retval] long *pRetVal
);
```



## Property value

True if the key is a subkey; otherwise, false.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**IKeyword**](ikeyword.md)
</dt> </dl>

 

 





