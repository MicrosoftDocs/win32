---
title: IMimePropertySchema RegisterProperty method
description: Registers a new property in the MimeOLE global property schema.
ms.assetid: d50bac09-18b2-4c08-b23c-2264136ffb43
keywords:
- RegisterProperty method Windows Mail (formerly Outlook Express)
- RegisterProperty method Windows Mail (formerly Outlook Express) , IMimePropertySchema interface
- IMimePropertySchema interface Windows Mail (formerly Outlook Express) , RegisterProperty method
topic_type:
- apiref
api_name:
- IMimePropertySchema.RegisterProperty
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimePropertySchema::RegisterProperty method

Registers a new property in the MimeOLE global property schema.

## Syntax


```C++
HRESULT RegisterProperty(
  [in]  LPCSTR  pszName,
  [in]  DWORD   dwFlags,
  [in]  DWORD   dwRowNumber,
  [in]  VARTYPE vtDefault,
  [out] LPDWORD pdwPropId
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

Specifies a [**MIMEPROPFLAGS**](oe-mimepropflags.md) value that describes the new property.

</dd> <dt>

*dwRowNumber* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the default relative position of the new property when persisted in the message header. This applies only for header properties.

</dd> <dt>

*vtDefault* \[in\]
</dt> <dd>

Type: **[VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127)**

Specifies the default [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) to use when a client requests a property value and [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072)::vt is set to VT\_EMPTY.

</dd> <dt>

*pdwPropId* \[out\]
</dt> <dd>

Type: **LPDWORD**

Receives the ID of the new property. This ID can be used along with PIDTOSTR to improve performance when getting and setting properties.

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
<tr class="odd">
<td><dl> <dt><strong>MIME_E_INVALID_HEADER_NAME</strong></dt> </dl></td>
<td>Indicates that <em>pszName</em> is a new property that contains invalid characters. <br/></td>
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



 

 





