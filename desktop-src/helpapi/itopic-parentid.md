---
title: ITopic ParentId property
description: Returns topic parent identifier.
ms.assetid: 'acf52f33-7527-46a6-9433-8c9eb0f822d2'
keywords: ["ParentId property HelpAPI", "ParentId property HelpAPI , ITopic interface", "ITopic interface HelpAPI , ParentId property"]
topic_type:
- apiref
api_name:
- ITopic.ParentId
- ITopic.get_ParentId
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ITopic::ParentId property

Returns topic parent identifier. The value will be -1 if the topic is a root (no parent) topic

This property is read-only.

## Syntax


```C++
HRESULT get_ParentId(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The identifier of the topic's parent. If the topic is a root topic and has no parent topic, the value is -1.

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

 

 





