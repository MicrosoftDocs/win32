---
title: ITopic Vendor property
description: Returns the vendor name for the topic
ms.assetid: '2f5fd641-f6af-4684-b616-097bc2d7f881'
keywords: ["Vendor property HelpAPI", "Vendor property HelpAPI , ITopic interface", "ITopic interface HelpAPI , Vendor property"]
topic_type:
- apiref
api_name:
- ITopic.Vendor
- ITopic.get_Vendor
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ITopic::Vendor property

Returns the vendor name for the topic

This property is read-only.

## Syntax


```C++
HRESULT get_Vendor(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The name of the topic's vendor.

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

 

 





