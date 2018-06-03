---
title: IMimePropertySet GetPropInfo method
description: Gets the attributes for the specified property.
ms.assetid: 44c4b252-c5b7-467d-bd37-4e289a514593
keywords:
- GetPropInfo method Windows Mail (formerly Outlook Express)
- GetPropInfo method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , GetPropInfo method
topic_type:
- apiref
api_name:
- IMimePropertySet.GetPropInfo
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

# IMimePropertySet::GetPropInfo method

Gets the attributes for the specified property.

## Syntax


```C++
HRESULT GetPropInfo(
  [in]      LPCSTR         pszName,
  [in, out] LPMIMEPROPINFO pInfo
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name or ID.

</dd> <dt>

*pInfo* \[in, out\]
</dt> <dd>

Type: **LPMIMEPROPINFO**

Receives a pointer to a [**MIMEPROPINFO**](oe-mimepropinfo.md) structure that contains the property information. The **dwMask** should be initialized to indicate which **MIMEPROPINFO** fields to return.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                 |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success. <br/>                                              |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred. <br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pszName* or *pInfo* is **NULL**. <br/>                |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that *pszName* does not specify an existing property. <br/> |



 

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



 

 





