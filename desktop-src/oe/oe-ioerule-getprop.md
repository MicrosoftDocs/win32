---
title: IOERule GetProp method
description: IOERule GetProp is no longer available for use as of Windows Vista.
ms.assetid: 'c1de1dfc-52fb-464d-9e55-1090217b51a9'
keywords: ["GetProp method Windows Mail (formerly Outlook Express)", "GetProp method Windows Mail (formerly Outlook Express) , IOERule interface", "IOERule interface Windows Mail (formerly Outlook Express) , GetProp method"]
topic_type:
- apiref
api_name:
- IOERule.GetProp
api_location:
- Msoe.dll
api_type:
- COM
---

# IOERule::GetProp method

\[**IOERule::GetProp** is no longer available for use as of Windows Vista.\]

Gets the specified rule property value.

## Syntax


```C++
HRESULT GetProp(
  [in]      RULE_PROP   prop,
  [in]      DWORD       dwFlags,
  [in, out] PROPVARIANT *pvarResult
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

*pvarResult* \[in, out\]
</dt> <dd>

Type: **[PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072)\***

Receives a pointer to a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure that contains the value type and property value.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                                                                                                                                                                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *prop* is invalid or equal to [**RULE\_PROP\_STATE**](oe-rule-prop.md), **RULE\_PROP\_READONLY**, **RULE\_PROP\_JUNKPCT**, **RULE\_PROP\_EXCPT\_WAB**, or **RULE\_PROP\_MAX**, or that *pvarResult* is **NULL**. <br/> |



 

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



 

 





