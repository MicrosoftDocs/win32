---
title: IMimePropertySet SetPropInfo method
description: Sets certain attributes about a property.
ms.assetid: '78c9a6ad-3c9d-4204-8319-b5b7b94aa2de'
keywords: ["SetPropInfo method Windows Mail (formerly Outlook Express)", "SetPropInfo method Windows Mail (formerly Outlook Express) , IMimePropertySet interface", "IMimePropertySet interface Windows Mail (formerly Outlook Express) , SetPropInfo method"]
topic_type:
- apiref
api_name:
- IMimePropertySet.SetPropInfo
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimePropertySet::SetPropInfo method

Sets certain attributes about a property.

## Syntax


```C++
HRESULT SetPropInfo(
  [in] LPCSTR          pszName,
  [in] LPCMIMEPROPINFO pInfo
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name or ID.

</dd> <dt>

*pInfo* \[in\]
</dt> <dd>

Type: **LPCMIMEPROPINFO**

Specifies a pointer to a [**MIMEPROPINFO**](oe-mimepropinfo.md) structure that contains the property information. The **dwMask** should be initialized to indicate which **MIMEPROPINFO** fields to return. This method supports only [**PIM\_CHARSET**](oe-propinfomask.md), **PIM\_ENCODINGTYPE**, and **PIM\_ROWNUMBER**.

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
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





