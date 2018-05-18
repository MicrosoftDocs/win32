---
title: IMimePropertySet QueryProp method
description: Compares the value of a property in the property set with the specified string.
ms.assetid: '3c383ca9-de90-4a00-960f-babea9b3429e'
keywords: ["QueryProp method Windows Mail (formerly Outlook Express)", "QueryProp method Windows Mail (formerly Outlook Express) , IMimePropertySet interface", "IMimePropertySet interface Windows Mail (formerly Outlook Express) , QueryProp method"]
topic_type:
- apiref
api_name:
- IMimePropertySet.QueryProp
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimePropertySet::QueryProp method

Compares the value of a property in the property set with the specified string.

## Syntax


```C++
HRESULT QueryProp(
  [in] LPCSTR  pszName,
  [in] LPCSTR  pszCriteria,
  [in] boolean fSubString,
  [in] boolean fCaseSensitive
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name or ID.

</dd> <dt>

*pszCriteria* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the string to compare the property to.

</dd> <dt>

*fSubString* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether *pszCriteria* is a sub-string of the property.



| Value                                                                                                                                | Meaning                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="false"></span><span id="FALSE"></span><dl> <dt>**false**</dt> </dl> | *pszCriteria* equals the value of the property.<br/> |
| <span id="true"></span><span id="TRUE"></span><dl> <dt>**true**</dt> </dl>    | *pszCriteria* is a sub-string of the property.<br/>  |



 

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



| Return code                                                                                                  | Description                                                                                                  |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Indicates that the values are equal.<br/>                                                              |
| <dl> <dt>**S\_FALSE**</dt> </dl>                      | Indicates that the values are not equal.<br/>                                                          |
| <dl> <dt>**E\_FAIL**</dt> </dl>                       | Indicates that an unknown error has occurred. <br/>                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Indicates that *pszName* or *pszCriteria* is **NULL**.<br/>                                            |
| <dl> <dt>**MIME\_E\_VARTYPE\_NO\_CONVERT**</dt> </dl> | Indicates that the value of the property specified by *pszName* cannot be converted to a string. <br/> |



 

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



 

 





