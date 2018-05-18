---
title: ITopic Package property
description: Returns the package that the topic resides in
ms.assetid: 'b78fefaf-0bca-4c31-9b10-ab0d1348e2de'
keywords: ["Package property HelpAPI", "Package property HelpAPI , ITopic interface", "ITopic interface HelpAPI , Package property"]
topic_type:
- apiref
api_name:
- ITopic.Package
- ITopic.get_Package
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ITopic::Package property

Returns the package that the topic resides in

This property is read-only.

## Syntax


```C++
HRESULT get_Package(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The package that contains this topic.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITopic**](itopic.md)
</dt> </dl>

 

 





