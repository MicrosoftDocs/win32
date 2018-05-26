---
title: IIMAPTransport2 SetDefaultCP method
description: Sets a default code page to use for Internet Message Access Protocol (IMAP) mailbox names and indicates whether IIMAPTransport should handle string conversions automatically.
ms.assetid: 40c8ef0b-f224-46cf-9dbb-d50673b24e8d
keywords:
- SetDefaultCP method Windows Mail (formerly Outlook Express)
- SetDefaultCP method Windows Mail (formerly Outlook Express) , IIMAPTransport2 interface
- IIMAPTransport2 interface Windows Mail (formerly Outlook Express) , SetDefaultCP method
topic_type:
- apiref
api_name:
- IIMAPTransport2.SetDefaultCP
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

# IIMAPTransport2::SetDefaultCP method

\[**IIMAPTransport2::SetDefaultCP** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sets a default code page to use for Internet Message Access Protocol (IMAP) mailbox names and indicates whether IIMAPTransport should handle string conversions automatically.

## Syntax


```C++
HRESULT SetDefaultCP(
  [in] DWORD dwTranslateFlags,
  [in] UINT  uiCodePage
);
```



## Parameters

<dl> <dt>

*dwTranslateFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains a flag that indicates how to enable automatic conversion of strings.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="IMAP_MBOXXLATE_DEFAULT"></span><span id="imap_mboxxlate_default"></span><dl> <dt><strong>IMAP_MBOXXLATE_DEFAULT</strong></dt> <dt>0x00000000</dt> </dl></td>
<td>Always convert. <br/></td>
</tr>
<tr class="even">
<td><span id="IMAP_MBOXXLATE_DISABLE"></span><span id="imap_mboxxlate_disable"></span><dl> <dt><strong>IMAP_MBOXXLATE_DISABLE</strong></dt> <dt>0x00000001</dt> </dl></td>
<td>Never convert. <br/></td>
</tr>
<tr class="odd">
<td><span id="IMAP_MBOXXLATE_DISABLEIMAP4"></span><span id="imap_mboxxlate_disableimap4"></span><dl> <dt><strong>IMAP_MBOXXLATE_DISABLEIMAP4</strong></dt> <dt>0x00000002</dt> </dl></td>
<td>Convert only for IMAP4 rev1. <br/></td>
</tr>
<tr class="even">
<td><span id="IMAP_MBOXXLATE_VERBATIMOK"></span><span id="imap_mboxxlate_verbatimok"></span><dl> <dt><strong>IMAP_MBOXXLATE_VERBATIMOK</strong></dt> <dt>0x00000004</dt> </dl></td>
<td>Unconvertable mailbox names can be returned verbatim. <br/>
<blockquote>
[!Note]<br />
If conversion is disabled, all mailbox names are returned verbatim.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><span id="IMAP_MBOXXLATE_RETAINCP"></span><span id="imap_mboxxlate_retaincp"></span><dl> <dt><strong>IMAP_MBOXXLATE_RETAINCP</strong></dt> <dt>0x00000008</dt> </dl></td>
<td>Keep the default code page and ignore <em>uiCodePage</em>. <br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

*uiCodePage* \[in\]
</dt> <dd>

Type: **UINT**

Specifies a **UINT** that indicates the default code page to use for translations.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





