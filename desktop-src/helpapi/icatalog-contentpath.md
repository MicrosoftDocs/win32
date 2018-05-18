---
title: ICatalog ContentPath property
description: property ContentPath - returns the content path for this catalog
ms.assetid: '3f44cecf-3628-4341-baaf-b4f7aebdbcfa'
keywords: ["ContentPath property HelpAPI", "ContentPath property HelpAPI , ICatalog interface", "ICatalog interface HelpAPI , ContentPath property"]
topic_type:
- apiref
api_name:
- ICatalog.ContentPath
- ICatalog.get_ContentPath
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalog::ContentPath property

property ContentPath - returns the content path for this catalog

This property is read-only.

## Syntax


```C++
HRESULT get_ContentPath(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The content path for this catalog.

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

 

 





