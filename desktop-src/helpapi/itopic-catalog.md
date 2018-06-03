---
title: ITopic Catalog property
description: Returns the catalog interface associated with the topic
ms.assetid: 0A698974-A001-46BB-949E-26CFB7DAB1CB
keywords:
- Catalog property HelpAPI
- Catalog property HelpAPI , ITopic interface
- ITopic interface HelpAPI , Catalog property
topic_type:
- apiref
api_name:
- ITopic.Catalog
- ITopic.get_Catalog
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

# ITopic::Catalog property

Returns the catalog interface associated with the topic

This property is read-only.

## Syntax


```C++
HRESULT get_Catalog(
  [out, retval] ICatalog **pRetVal
);
```



## Property value

The ICatalog interface of the catalog that is associated with the topic.

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

 

 





