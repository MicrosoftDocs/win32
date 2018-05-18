---
title: ITopic Id property
description: Returns topic identifier
ms.assetid: 'b8a4e440-d27d-4caf-a580-03c6d6756eaa'
keywords: ["Id property HelpAPI", "Id property HelpAPI , ITopic interface", "ITopic interface HelpAPI , Id property"]
topic_type:
- apiref
api_name:
- ITopic.Id
- ITopic.get_Id
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ITopic::Id property

Returns topic identifier

This property is read-only.

## Syntax


```C++
HRESULT get_Id(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The topic's identifier.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITopic**](itopic.md)
</dt> </dl>

 

 





