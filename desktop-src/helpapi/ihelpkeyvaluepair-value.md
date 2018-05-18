---
title: IHelpKeyValuePair value method
description: method Value - get the value of a key/value pair
ms.assetid: '1c53188a-f439-43d5-8605-bdfd5488f57c'
keywords: ["value method HelpAPI", "value method HelpAPI , IHelpKeyValuePair interface", "IHelpKeyValuePair interface HelpAPI , value method"]
topic_type:
- apiref
api_name:
- IHelpKeyValuePair.value
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# IHelpKeyValuePair::value method

method Value - get the value of a key/value pair

## Syntax


```C++
HRESULT value(
  [out, retval] SAFEARRAY BSTR
);
```



## Parameters

<dl> <dt>

*BSTR* \[out, retval\]
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

[**IHelpKeyValuePair**](ihelpkeyvaluepair.md)
</dt> </dl>

 

 





