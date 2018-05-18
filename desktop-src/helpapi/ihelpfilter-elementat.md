---
title: IHelpFilter ElementAt method
description: method ElementAt - returns filter value at a particular index in the collection
ms.assetid: '3beef150-da64-4558-926b-251b2849bec3'
keywords: ["ElementAt method HelpAPI", "ElementAt method HelpAPI , IHelpFilter interface", "IHelpFilter interface HelpAPI , ElementAt method"]
topic_type:
- apiref
api_name:
- IHelpFilter.ElementAt
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IHelpFilter::ElementAt method

method ElementAt - returns filter value at a particular index in the collection

## Syntax


```C++
HRESULT ElementAt(
  [in]          long              index,
  [out, retval] IHelpKeyValuePair **pRetVal
);
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd></dd> <dt>

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

[**IHelpFilter**](ihelpfilter.md)
</dt> </dl>

 

 





