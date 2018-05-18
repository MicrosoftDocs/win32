---
title: ISCPSecureAuthenticate GetSecureQuery method
description: The GetSecureQuery method is used to obtain a pointer to the ISCPSecureQuery interface.
ms.assetid: 'd0cee36c-5200-4951-9a83-a0f32658939b'
keywords: ["GetSecureQuery method windows Media Device Manager", "GetSecureQuery method windows Media Device Manager , ISCPSecureAuthenticate interface", "ISCPSecureAuthenticate interface windows Media Device Manager , GetSecureQuery method"]
topic_type:
- apiref
api_name:
- ISCPSecureAuthenticate.GetSecureQuery
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureAuthenticate::GetSecureQuery method

The **GetSecureQuery** method is used to obtain a pointer to the [**ISCPSecureQuery**](iscpsecurequery.md) interface.

## Syntax


```C++
HRESULT GetSecureQuery(
  [out] ISCPSecureQuery **ppSecureQuery
);
```



## Parameters

<dl> <dt>

*ppSecureQuery* \[out\]
</dt> <dd>

Pointer to an [**ISCPSecureQuery**](iscpsecurequery.md) object.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureAuthenticate Interface**](iscpsecureauthenticate.md)
</dt> <dt>

[**ISCPSecureQuery Interface**](iscpsecurequery.md)
</dt> </dl>

 

 





