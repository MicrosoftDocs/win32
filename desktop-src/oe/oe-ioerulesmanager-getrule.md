---
title: IOERulesManager GetRule method
description: IOERulesManager GetRule is no longer available for use as of Windows Vista.
ms.assetid: a493ec0c-2ff3-47c2-ad01-ae8cc280e827
keywords:
- GetRule method Windows Mail (formerly Outlook Express)
- GetRule method Windows Mail (formerly Outlook Express) , IOERulesManager interface
- IOERulesManager interface Windows Mail (formerly Outlook Express) , GetRule method
topic_type:
- apiref
api_name:
- IOERulesManager.GetRule
api_location:
- Msoe.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOERulesManager::GetRule method

\[**IOERulesManager::GetRule** is no longer available for use as of Windows Vista.\]

Gets the first rule of the specified type.

## Syntax


```C++
HRESULT GetRule(
  [in]  RULEID    ridRule,
  [in]  RULE_TYPE type,
  [in]  DWORD     dwFlags,
  [out] IOERule   **ppIRule
);
```



## Parameters

<dl> <dt>

*ridRule* \[in\]
</dt> <dd>

Type: **RULEID**

Specifies one of the following values.



| Value                                                                                                                                                                                                                                                | Meaning                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="RULEID_SENDERS"></span><span id="ruleid_senders"></span><dl> <dt>**RULEID\_SENDERS**</dt> <dt></dt> </dl>                               | Indicates a Mail or News rule. <br/>    |
| <span id="RULEID_JUNK"></span><span id="ruleid_junk"></span><dl> <dt>**RULEID\_JUNK**</dt> <dt></dt> </dl>                                        | Indicates a Blocked Senders rule. <br/> |
| <span id="RULEID_VIEW_ALL"></span><span id="ruleid_view_all"></span><dl> <dt>**RULEID\_VIEW\_ALL**</dt> <dt>0xffa</dt> </dl>                      |                                               |
| <span id="RULEID_VIEW_UNREAD"></span><span id="ruleid_view_unread"></span><dl> <dt>**RULEID\_VIEW\_UNREAD**</dt> <dt>0xffb</dt> </dl>             |                                               |
| <span id="RULEID_VIEW_DOWNLOADED"></span><span id="ruleid_view_downloaded"></span><dl> <dt>**RULEID\_VIEW\_DOWNLOADED**</dt> <dt>0xffc</dt> </dl> |                                               |
| <span id="RULEID_VIEW_DELETED"></span><span id="ruleid_view_deleted"></span><dl> <dt>**RULEID\_VIEW\_DELETED**</dt> <dt>0xffd</dt> </dl>          |                                               |
| <span id="RULEID_VIEW_REPLIES"></span><span id="ruleid_view_replies"></span><dl> <dt>**RULEID\_VIEW\_REPLIES**</dt> <dt>0xffe</dt> </dl>          |                                               |
| <span id="RULEID_VIEW_IGNORED"></span><span id="ruleid_view_ignored"></span><dl> <dt>**RULEID\_VIEW\_IGNORED**</dt> <dt>0xfff</dt> </dl>          |                                               |



 

</dd> <dt>

*type* \[in\]
</dt> <dd>

Type: **[**RULE\_TYPE**](oe-rule-type.md)**

Specifies a [**RULE\_TYPE**](oe-rule-type.md) value.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*ppIRule* \[out\]
</dt> <dd>

Type: **[**IOERule**](oe-ioerule.md)\*\***

Receives the address of a pointer to the [**IOERule**](oe-ioerule.md) object found.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *ridRule* is invalid. <br/> |



 

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| End of client support<br/>    | Windows XP<br/>                                                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                                             |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





