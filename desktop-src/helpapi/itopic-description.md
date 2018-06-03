---
title: ITopic Description property
description: Returns topic description
ms.assetid: 1403d8e9-581d-4b3f-a89e-4748ef805218
keywords:
- Description property HelpAPI
- Description property HelpAPI , ITopic interface
- ITopic interface HelpAPI , Description property
topic_type:
- apiref
api_name:
- ITopic.Description
- ITopic.get_Description
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITopic::Description property

Returns topic description

This property is read-only.

## Syntax


```C++
HRESULT get_Description(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The topic's description.

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

 

 





