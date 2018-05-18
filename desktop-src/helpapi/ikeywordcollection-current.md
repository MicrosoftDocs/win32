---
title: IKeywordCollection Current property
description: Gets the current IKeyword element in the collection
ms.assetid: 'a92a74de-903b-4261-ae81-c7c737e1ec10'
keywords: ["Current property HelpAPI", "Current property HelpAPI , IKeywordCollection interface", "IKeywordCollection interface HelpAPI , Current property"]
topic_type:
- apiref
api_name:
- IKeywordCollection.Current
- IKeywordCollection.get_Current
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IKeywordCollection::Current property

Gets the current IKeyword element in the collection

This property is read-only.

## Syntax


```C++
HRESULT get_Current(
  [out, retval] IUnknown **pRetVal
);
```



## Property value

The current IKeyword element in the collection.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**IKeywordCollection**](ikeywordcollection.md)
</dt> </dl>

 

 





