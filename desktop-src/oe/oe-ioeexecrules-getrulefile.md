---
title: IOEExecRules GetRuleFile method
description: IOEExecRules GetRuleFile is no longer available for use as of Windows Vista.
ms.assetid: 'b889a798-360e-4df6-8d88-66f1bc76f47f'
keywords: ["GetRuleFile method Windows Mail (formerly Outlook Express)", "GetRuleFile method Windows Mail (formerly Outlook Express) , IOEExecRules interface", "IOEExecRules interface Windows Mail (formerly Outlook Express) , GetRuleFile method"]
topic_type:
- apiref
api_name:
- IOEExecRules.GetRuleFile
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IOEExecRules::GetRuleFile method

\[**IOEExecRules::GetRuleFile** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT GetRuleFile(
  [in]  LPCSTR  pszFile,
  [out] IStream **ppstmFile,
  [out] DWORD   *pdwType
);
```



## Parameters

<dl> <dt>

*pszFile* \[in\]
</dt> <dd>

Type: **LPCSTR**

</dd> <dt>

*ppstmFile* \[out\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\*\***

</dd> <dt>

*pdwType* \[out\]
</dt> <dd>

Type: **DWORD\***

<dl> <dt>

<span id="RFT_FILE"></span><span id="rft_file"></span>**RFT\_FILE** (0x00000000)
</dt> <dt>

<span id="RFT_HTML"></span><span id="rft_html"></span>**RFT\_HTML** (0x00000001)
</dt> <dt>

<span id="RFT_TEXT"></span><span id="rft_text"></span>**RFT\_TEXT** (0x00000002)
</dt> <dt>

<span id="RFT_MESSAGE"></span><span id="rft_message"></span>**RFT\_MESSAGE** (0x00000003)
</dt> </dl> </dd> </dl>

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



 

 





