---
title: IHelpFilter Remove method
description: method Remove - Remove a criteria key/value pair from the filter list
ms.assetid: debfc19e-e2a3-4177-9fe9-6c88756f6f00
keywords:
- Remove method HelpAPI
- Remove method HelpAPI , IHelpFilter interface
- IHelpFilter interface HelpAPI , Remove method
topic_type:
- apiref
api_name:
- IHelpFilter.Remove
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

# IHelpFilter::Remove method

method Remove - Remove a criteria key/value pair from the filter list

## Syntax


```C++
HRESULT Remove(
  [in]          BSTR         key,
  [out, retval] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

*key* \[in\]
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

[**IHelpFilter**](ihelpfilter.md)
</dt> </dl>

 

 





