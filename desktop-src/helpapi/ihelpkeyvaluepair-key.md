---
title: IHelpKeyValuePair key property
description: property Key - get the key of a key/value pair
ms.assetid: 2ce6fe03-7d50-4729-8163-9e6f9b92951c
keywords:
- key property HelpAPI
- key property HelpAPI , IHelpKeyValuePair interface
- IHelpKeyValuePair interface HelpAPI , key property
topic_type:
- apiref
api_name:
- IHelpKeyValuePair.key
- IHelpKeyValuePair.get_key
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IHelpKeyValuePair::key property

property Key - get the key of a key/value pair

This property is read-only.

## Syntax


```C++
HRESULT get_key(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The key of a key/value pair.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**IHelpKeyValuePair**](ihelpkeyvaluepair.md)
</dt> </dl>

 

 





