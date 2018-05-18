---
Description: 'Creates a new IWSDXMLContext object.'
ms.assetid: 'fb0d8c28-1dc3-43be-a1cf-c00de6c1f43e'
title: WSDXMLCreateContext function
---

# WSDXMLCreateContext function

Creates a new [**IWSDXMLContext**](iwsdxmlcontext.md) object.

## Syntax


```C++
HRESULT WINAPI WSDXMLCreateContext(
  _Out_ IWSDXMLContext **ppContext
);
```



## Parameters

<dl> <dt>

*ppContext* \[out\]
</dt> <dd>

Pointer to a newly allocated [**IWSDXMLContext**](iwsdxmlcontext.md) object. If the function fails, this parameter can be **NULL**.

</dd> </dl>

## Return value

Possible return values include, but are not limited to, the following:



| Return code                                                                                   | Description                                               |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method completed successfully.<br/>                 |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | *ppContext* is **NULL**.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory to complete the operation.<br/> |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Library<br/>                  | <dl> <dt>WsdApi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WsdApi.dll</dt> </dl> |



 

 




