---
Description: 'Gets a specified name from the built-in namespace.'
ms.assetid: 'b7a5ac45-ee87-4290-9cbb-de523c0f2775'
title: WSDXMLGetNameFromBuiltinNamespace function
---

# WSDXMLGetNameFromBuiltinNamespace function

Gets a specified name from the built-in namespace.

## Syntax


```C++
HRESULT WINAPI WSDXMLGetNameFromBuiltinNamespace(
   LPCWSTR     pszNamespace,
   LPCWSTR     pszName,
   WSDXML_NAME **ppName
);
```



## Parameters

<dl> <dt>

*pszNamespace* 
</dt> <dd>

The namespace to match with a built-in namespace.

</dd> <dt>

*pszName* 
</dt> <dd>

The name to match with a built-in name.

</dd> <dt>

*ppName* 
</dt> <dd>

Reference to a [**WSDXML\_NAME**](wsdxml-name-struct.md) structure that contains the returned built-in name. The memory usage of *ppName* is managed elsewhere. Consequently, the calling application should not attempt to deallocate *ppName*.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                  | Description                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Method completed successfully.<br/>                                                                                                                                                                                                                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | *pszNamespace* is **NULL**, *pszName* is **NULL**, the length in characters of *pszNamespace* exceeds WSD\_MAX\_TEXT\_LENGTH (8192), the length in characters of *pszName* exceeds WSD\_MAX\_TEXT\_LENGTH (8192), or there was no matching name in the built-in namespace.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | *ppName* is **NULL**.<br/>                                                                                                                                                                                                                                                      |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Library<br/>                  | <dl> <dt>Wsdapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wsdapi.dll</dt> </dl> |



 

 




