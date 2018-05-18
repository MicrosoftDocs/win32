---
title: IMimeMessageTree QueryBodyProp method
description: Compares the value of a property in a body with a specified string.
ms.assetid: 'bc7cfae2-1cf5-4c61-8110-1e3827feee86'
keywords: ["QueryBodyProp method Windows Mail (formerly Outlook Express)", "QueryBodyProp method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface", "IMimeMessageTree interface Windows Mail (formerly Outlook Express) , QueryBodyProp method"]
topic_type:
- apiref
api_name:
- IMimeMessageTree.QueryBodyProp
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageTree::QueryBodyProp method

Compares the value of a property in a body with a specified string.

## Syntax


```C++
HRESULT QueryBodyProp(
  [in] HBODY   hBody,
  [in] LPCSTR  pszName,
  [in] LPCSTR  pszCriteria,
  [in] boolean fSubString,
  [in] boolean fCaseSensitive
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body. Use HBODY\_ROOT (0xffffffff) to indicate the root body.

</dd> <dt>

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

Specifies how to compare the string to the property value.



| Value                                                                                                                                | Meaning                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Indicates that *pszCriteria* should match the property value. <br/>                |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Indicates that *pszCriteria* should match a substring of the property value. <br/> |



 

</dd> <dt>

*fCaseSensitive* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether the string comparison is case sensitive.



| Value                                                                                                                                | Meaning                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Indicates that the comparison is case insensitive. <br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Indicates that the comparison is case sensitive. <br/>   |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                  | Description                                                                                        |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Indicates that a match has been found. <br/>                                                 |
| <dl> <dt>**S\_FALSE**</dt> </dl>                      | Indicates that there is no match. <br/>                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Indicates that *hBody*, *pszName*, or *pszCriteria* is **NULL**. <br/>                       |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>             | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl>      | Indicates that *hBody* is an invalid handle. <br/>                                           |
| <dl> <dt>**MIME\_E\_VARTYPE\_NO\_CONVERT**</dt> </dl> | Indicates that the property specified by *pszName* cannot be converted to a string. <br/>    |



 

## Remarks

A property ID can also be passed into this method through the *pszName* parameter using the PIDTOSTR macro.

This method is equivalent to:

pMessageTree-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(*hBody*, IID\_IMimePropertySet, (LPVOID \*)&pPropertySet);

pPropertySet-&gt;[**QueryProp**](oe-imimepropertyset-queryprop.md)(*pszName*, *pszCriteria*, *fSubString*,*fCaseSensitive*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





