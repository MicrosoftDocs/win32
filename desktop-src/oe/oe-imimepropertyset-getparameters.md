---
title: IMimePropertySet GetParameters method
description: Gets the parameters that are associated with a property. Not all properties support parameters.
ms.assetid: a8409186-3ead-482d-8d20-f888574f4b49
keywords:
- GetParameters method Windows Mail (formerly Outlook Express)
- GetParameters method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , GetParameters method
topic_type:
- apiref
api_name:
- IMimePropertySet.GetParameters
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimePropertySet::GetParameters method

Gets the parameters that are associated with a property. Not all properties support parameters.

## Syntax


```C++
HRESULT GetParameters(
  [in]  LPCSTR          pszName,
  [out] ULONG           *pcParams,
  [out] LPMIMEPARAMINFO *pprgParam
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name or ID.

</dd> <dt>

*pcParams* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of valid parameters in the *pprgParam* array.

</dd> <dt>

*pprgParam* \[out\]
</dt> <dd>

Type: **LPMIMEPARAMINFO\***

Receives a pointer to an array of [**MIMEPARAMINFO**](oe-mimeparaminfo.md) structures that contain parameter information. The client is responsible for freeing this array by calling [**FreeParamInfoArray**](oe-imimeallocator-freeparaminfoarray.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                   |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success. <br/>                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred. <br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pszName*, *pcParams*, or *pprgParam* is **NULL**. <br/> |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that *pszName* does not specify an existing property. <br/>   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates that an attempt to allocate memory failed.<br/>               |



 

## Remarks

A property ID can also be passed into this method through the *pszName* parameter using the PIDTOSTR macro.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





