---
title: IOEExecRules AddSoundFile method
description: IOEExecRules AddSoundFile is no longer available for use as of Windows Vista.
ms.assetid: 'e0b6cf81-ed03-42c3-81a4-711665d69f22'
keywords: ["AddSoundFile method Windows Mail (formerly Outlook Express)", "AddSoundFile method Windows Mail (formerly Outlook Express) , IOEExecRules interface", "IOEExecRules interface Windows Mail (formerly Outlook Express) , AddSoundFile method"]
topic_type:
- apiref
api_name:
- IOEExecRules.AddSoundFile
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IOEExecRules::AddSoundFile method

\[**IOEExecRules::AddSoundFile** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT AddSoundFile(
  [in] DWORD  dwFlags,
  [in] LPCSTR pszSndFile
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

<dl> <dt>

<span id="ASF_PLAYIFNEW"></span><span id="asf_playifnew"></span>**ASF\_PLAYIFNEW** (0x00000001)
</dt> </dl> </dd> <dt>

*pszSndFile* \[in\]
</dt> <dd>

Type: **LPCSTR**

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





