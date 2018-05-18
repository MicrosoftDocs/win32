---
title: ITopic ParentTopicVersion property
description: Returns parent topic version
ms.assetid: 'e67e6caa-24fa-481f-b5ab-552328cbfa4a'
keywords: ["ParentTopicVersion property HelpAPI", "ParentTopicVersion property HelpAPI , ITopic interface", "ITopic interface HelpAPI , ParentTopicVersion property"]
topic_type:
- apiref
api_name:
- ITopic.ParentTopicVersion
- ITopic.get_ParentTopicVersion
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ITopic::ParentTopicVersion property

Returns parent topic version

This property is read-only.

## Syntax


```C++
HRESULT get_ParentTopicVersion(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The version of the parent topic.

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

 

 





