---
title: IKeywordCollection Save method
description: Saves the keyword index to the provided filename
ms.assetid: '761c41ba-57fc-464d-a417-5cde17a3d7b1'
keywords: ["Save method HelpAPI", "Save method HelpAPI , IKeywordCollection interface", "IKeywordCollection interface HelpAPI , Save method"]
topic_type:
- apiref
api_name:
- IKeywordCollection.Save
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IKeywordCollection::Save method

Saves the keyword index to the provided filename

## Syntax


```C++
HRESULT Save(
  [in] BSTR fileName
);
```



## Parameters

<dl> <dt>

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

 

 





