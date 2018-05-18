---
title: IOERule SetProp method
description: IOERule SetProp is no longer available for use as of Windows Vista.
ms.assetid: '23a2ebe4-357e-449e-8a2a-14d7db6315c8'
keywords: ["SetProp method Windows Mail (formerly Outlook Express)", "SetProp method Windows Mail (formerly Outlook Express) , IOERule interface", "IOERule interface Windows Mail (formerly Outlook Express) , SetProp method"]
topic_type:
- apiref
api_name:
- IOERule.SetProp
api_location:
- Msoe.dll
api_type:
- COM
---

# IOERule::SetProp method

\[**IOERule::SetProp** is no longer available for use as of Windows Vista.\]

Sets a value for the specified rule property.

## Syntax


```C++
HRESULT SetProp(
  [in] RULE_PROP   prop,
  [in] DWORD       dwFlags,
  [in] PROPVARIANT *pvarValue
);
```



## Parameters

<dl> <dt>

*prop* \[in\]
</dt> <dd>

Type: **[**RULE\_PROP**](oe-rule-prop.md)**

Specifies a [**RULE\_PROP**](oe-rule-prop.md) value that indicates the property type.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*pvarValue* \[in\]
</dt> <dd>

Type: **[PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072)\***

Specifies a pointer to a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure that contains the value type and property value.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                                                                                                                                                                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *prop* is invalid or equal to [**RULE\_PROP\_STATE**](oe-rule-prop.md), **RULE\_PROP\_READONLY**, **RULE\_PROP\_JUNKPCT**, **RULE\_PROP\_EXCPT\_WAB**, or **RULE\_PROP\_MAX**, or that *pvarValue* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                                                             |



 

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| End of client support<br/>    | Windows XP<br/>                                                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                                             |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





