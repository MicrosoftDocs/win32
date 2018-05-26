---
title: IHelpFilter AddRange method
description: method AddRange - Adds a criteria key and matching range of values to the filter list
ms.assetid: 589bdde8-7a1f-4427-ad06-414490bce3c0
keywords:
- AddRange method HelpAPI
- AddRange method HelpAPI , IHelpFilter interface
- IHelpFilter interface HelpAPI , AddRange method
topic_type:
- apiref
api_name:
- IHelpFilter.AddRange
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

# IHelpFilter::AddRange method

method AddRange - Adds a criteria key and matching range of values to the filter list

## Syntax


```C++
HRESULT AddRange(
  [in] BSTR      key,
  [in] SAFEARRAY BSTR
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd></dd> <dt>

*BSTR* \[in\]
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

[**IHelpFilter**](ihelpfilter.md)
</dt> </dl>

 

 





