---
title: IKeyword value property
description: Actual value of the keyword
ms.assetid: '1eb03f48-6bbb-4123-9149-ec4573f0bdd3'
keywords: ["value property HelpAPI", "value property HelpAPI , IKeyword interface", "IKeyword interface HelpAPI , value property"]
topic_type:
- apiref
api_name:
- IKeyword.value
- IKeyword.get_value
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IKeyword::value property

Actual value of the keyword

This property is read-only.

## Syntax


```C++
HRESULT get_value(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The keyword value.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**IKeyword**](ikeyword.md)
</dt> </dl>

 

 





