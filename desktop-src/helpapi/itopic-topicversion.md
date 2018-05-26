---
title: ITopic TopicVersion property
description: Returns topic version
ms.assetid: 2a926040-074d-4433-af13-498a9331b3f9
keywords:
- TopicVersion property HelpAPI
- TopicVersion property HelpAPI , ITopic interface
- ITopic interface HelpAPI , TopicVersion property
topic_type:
- apiref
api_name:
- ITopic.TopicVersion
- ITopic.get_TopicVersion
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

# ITopic::TopicVersion property

Returns topic version

This property is read-only.

## Syntax


```C++
HRESULT get_TopicVersion(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The topic version.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITopic**](itopic.md)
</dt> </dl>

 

 





