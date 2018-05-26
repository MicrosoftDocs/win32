---
title: ICatalogRead GetTopicDetailsForF1Keyword method
description: method GetTopicDetailsForF1Keyword - returns an ITopic interface containing the matching topic for the F1 keyword.
ms.assetid: 66e969a9-45a4-4b93-acba-f9c8f723078b
keywords:
- GetTopicDetailsForF1Keyword method HelpAPI
- GetTopicDetailsForF1Keyword method HelpAPI , ICatalogRead interface
- ICatalogRead interface HelpAPI , GetTopicDetailsForF1Keyword method
topic_type:
- apiref
api_name:
- ICatalogRead.GetTopicDetailsForF1Keyword
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

# ICatalogRead::GetTopicDetailsForF1Keyword method

method GetTopicDetailsForF1Keyword - returns an ITopic interface containing the matching topic for the F1 keyword. F1 keywords consists of an array of prioritized F1 keywords

## Syntax


```C++
HRESULT GetTopicDetailsForF1Keyword(
  [in]          ICatalog    *Catalog,
  [in]          SAFEARRAY   BSTR,
  [in]          IHelpFilter *filter,
  [out, retval] ITopic      **pRetVal
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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ICatalogRead**](icatalogread.md)
</dt> </dl>

 

 





