---
title: IMimeMessageW QueryPropW method
description: Returns the value of a property in the root header.
ms.assetid: '929f6de5-5494-485a-a886-535797f45b75'
keywords: ["QueryPropW method Windows Mail (formerly Outlook Express)", "QueryPropW method Windows Mail (formerly Outlook Express) , IMimeMessageW interface", "IMimeMessageW interface Windows Mail (formerly Outlook Express) , QueryPropW method"]
topic_type:
- apiref
api_name:
- IMimeMessageW.QueryPropW
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageW::QueryPropW method

\[**QueryPropW** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the value of a property in the root header.

## Syntax


```C++
HRESULT QueryPropW(
  [in] LPCWSTR pwszName,
  [in] LPCWSTR pwszCriteria,
  [in] boolean fSubString,
  [in] boolean fCaseSensitive
);
```



## Parameters

<dl> <dt>

*pwszName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the property name or ID.

</dd> <dt>

*pwszCriteria* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the string to compare the property to.

</dd> <dt>

*fSubString* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether *pwszCriteria* is a sub-string of the property.



| Value                                                                                                                                | Meaning                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <span id="false"></span><span id="FALSE"></span><dl> <dt>**false**</dt> </dl> | *pwszCriteria* equals the value of the property.<br/> |
| <span id="true"></span><span id="TRUE"></span><dl> <dt>**true**</dt> </dl>    | *pwszCriteria* is a sub-string of the property.<br/>  |



 

</dd> <dt>

*fCaseSensitive* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether the string comparison is case-sensitive.



| Value                                                                                                                                | Meaning                                               |
|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="false"></span><span id="FALSE"></span><dl> <dt>**false**</dt> </dl> | The string comparison is case-insensitive.<br/> |
| <span id="true"></span><span id="TRUE"></span><dl> <dt>**true**</dt> </dl>    | The string comparison is case-sensitive.<br/>   |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                  | Description                                                                                                   |
|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Indicates that the values are equal.<br/>                                                               |
| <dl> <dt>**S\_FALSE**</dt> </dl>                      | Indicates that the values are not equal.<br/>                                                           |
| <dl> <dt>**E\_FAIL**</dt> </dl>                       | Indicates that an unknown error has occurred. <br/>                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Indicates that *pwszName* or *pwszCriteria* is **NULL**.<br/>                                           |
| <dl> <dt>**MIME\_E\_VARTYPE\_NO\_CONVERT**</dt> </dl> | Indicates that the value of the property specified by *pwszName* cannot be converted to a string. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





