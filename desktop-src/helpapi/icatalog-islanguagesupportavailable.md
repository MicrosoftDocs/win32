---
title: ICatalog IsLanguageSupportAvailable method
description: Method IsLanguageSupportAvailable - Check to see if the natural language support is installed on the system for a given language
ms.assetid: 'c3fde805-2d1a-492e-9deb-40aa588fff35'
keywords: ["IsLanguageSupportAvailable method HelpAPI", "IsLanguageSupportAvailable method HelpAPI , ICatalog interface", "ICatalog interface HelpAPI , IsLanguageSupportAvailable method"]
topic_type:
- apiref
api_name:
- ICatalog.IsLanguageSupportAvailable
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalog::IsLanguageSupportAvailable method

Method IsLanguageSupportAvailable - Check to see if the natural language support is installed on the system for a given language

## Syntax


```C++
HRESULT IsLanguageSupportAvailable(
  [in]          BSTR lang,
  [out, retval] long *pRetVal
);
```



## Parameters

<dl> <dt>

*lang* \[in\]
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

[**ICatalog**](icatalog.md)
</dt> </dl>

 

 





