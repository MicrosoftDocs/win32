---
title: IKeywordCollection Load method
description: Loads the keyword index from the provided filename
ms.assetid: 'b6d80e0b-9b2a-42b1-b3ec-96cd7c9a2f1f'
keywords: ["Load method HelpAPI", "Load method HelpAPI , IKeywordCollection interface", "IKeywordCollection interface HelpAPI , Load method"]
topic_type:
- apiref
api_name:
- IKeywordCollection.Load
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IKeywordCollection::Load method

Loads the keyword index from the provided filename

## Syntax


```C++
HRESULT Load(
  [in] ICatalog *Catalog,
  [in] BSTR     fileName
);
```



## Parameters

<dl> <dt>

*Catalog* \[in\]
</dt> <dd></dd> <dt>

*fileName* \[in\]
</dt> <dd></dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 





