---
title: ITopic TopicLocale property
description: Returns topic locale
ms.assetid: '45c80206-30b6-42b7-8e9f-a2bea3c41daa'
keywords: ["TopicLocale property HelpAPI", "TopicLocale property HelpAPI , ITopic interface", "ITopic interface HelpAPI , TopicLocale property"]
topic_type:
- apiref
api_name:
- ITopic.TopicLocale
- ITopic.get_TopicLocale
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ITopic::TopicLocale property

Returns topic locale

This property is read-only.

## Syntax


```C++
HRESULT get_TopicLocale(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The topic locale.

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

 

 





