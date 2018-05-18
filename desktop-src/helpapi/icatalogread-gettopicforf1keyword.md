---
title: ICatalogRead GetTopicForF1Keyword method
description: method GetTopicForF1Keyword - returns a stream containing the matching topic for the F1 keyword in XHTML format.
ms.assetid: '1f119c6d-172f-4f01-bcf5-625d20c83ac3'
keywords: ["GetTopicForF1Keyword method HelpAPI", "GetTopicForF1Keyword method HelpAPI , ICatalogRead interface", "ICatalogRead interface HelpAPI , GetTopicForF1Keyword method"]
topic_type:
- apiref
api_name:
- ICatalogRead.GetTopicForF1Keyword
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalogRead::GetTopicForF1Keyword method

method GetTopicForF1Keyword - returns a stream containing the matching topic for the F1 keyword in XHTML format. F1 keywords consists of an array of prioritized F1 keywords

## Syntax


```C++
HRESULT GetTopicForF1Keyword(
  [in]          ICatalog    *Catalog,
  [in]          SAFEARRAY   BSTR,
  [in]          IHelpFilter *filter,
  [out, retval] IUnknown    **pRetVal
);
```



## Parameters

<dl> <dt>

*Catalog* \[in\]
</dt> <dd></dd> <dt>

*BSTR* \[in\]
</dt> <dd></dd> <dt>

*filter* \[in\]
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

[**ICatalogRead**](icatalogread.md)
</dt> </dl>

 

 





