---
title: IMimePropertySchema ModifyProperty method
description: Modifies an existing property in the MimeOLE global property schema.
ms.assetid: 25ea8db6-403e-404b-b2d0-27915168c39b
keywords:
- ModifyProperty method Windows Mail (formerly Outlook Express)
- ModifyProperty method Windows Mail (formerly Outlook Express) , IMimePropertySchema interface
- IMimePropertySchema interface Windows Mail (formerly Outlook Express) , ModifyProperty method
topic_type:
- apiref
api_name:
- IMimePropertySchema.ModifyProperty
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

# IMimePropertySchema::ModifyProperty method

Modifies an existing property in the MimeOLE global property schema.

## Syntax


```C++
HRESULT ModifyProperty(
  [in] LPCSTR  pszName,
  [in] DWORD   dwFlags,
  [in] DWORD   dwRowNumber,
  [in] VARTYPE vtDefault
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a new [**MIMEPROPFLAGS**](oe-mimepropflags.md) value for the property.

</dd> <dt>

*dwRowNumber* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the new default relative position of the property.

</dd> <dt>

*vtDefault* \[in\]
</dt> <dd>

Type: **[VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127)**

Specifies the new default [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) for the property.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>S_OK</strong></dt> </dl></td>
<td>Indicates success. <br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>E_FAIL</strong></dt> </dl></td>
<td>Indicates that an unknown error has occurred. <br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>E_INVALIDARG</strong></dt> </dl></td>
<td>Indicates that <em>pszName</em> is <strong>NULL</strong>. <br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>MIME_E_UNSUPPORTED_VARTYPE</strong></dt> </dl></td>
<td>Indicates that <em>vtDefault</em> is equal to one of the following types. <br/>
<ul>
<li>VT_LPSTR</li>
<li>VT_LPWSTR</li>
<li>VT_FILETIME</li>
<li>VT_UI4</li>
<li>VT_I4</li>
<li>VT_STREAM</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





