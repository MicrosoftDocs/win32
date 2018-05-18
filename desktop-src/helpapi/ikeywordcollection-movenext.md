---
title: IKeywordCollection MoveNext method
description: Advances the enumerator to the next element of the collection
ms.assetid: '6541a77c-3d21-4c69-ae13-7d0094184f16'
keywords: ["MoveNext method HelpAPI", "MoveNext method HelpAPI , IKeywordCollection interface", "IKeywordCollection interface HelpAPI , MoveNext method"]
topic_type:
- apiref
api_name:
- IKeywordCollection.MoveNext
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IKeywordCollection::MoveNext method

Advances the enumerator to the next element of the collection

## Syntax


```C++
HRESULT MoveNext(
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out, retval\]
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

 

 





