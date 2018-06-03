---
title: IIMAPTransport2 SetIdleMode method
description: The IMAP IDLE extension allows the server to unilaterally report changes to the currently selected mailbox new email, flag updates, and message expunges.
ms.assetid: 7ec7a2af-e4ea-4dbb-8d2c-47e49df304c0
keywords:
- SetIdleMode method Windows Mail (formerly Outlook Express)
- SetIdleMode method Windows Mail (formerly Outlook Express) , IIMAPTransport2 interface
- IIMAPTransport2 interface Windows Mail (formerly Outlook Express) , SetIdleMode method
topic_type:
- apiref
api_name:
- IIMAPTransport2.SetIdleMode
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

# IIMAPTransport2::SetIdleMode method

\[**IIMAPTransport2::SetIdleMode** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The IMAP IDLE extension allows the server to unilaterally report changes to the currently selected mailbox: new email, flag updates, and message expunges. [**IIMAPTransport**](oe-iimaptransport.md) always enters IDLE mode when no IMAP commands are pending, but this can result in unnecessary entry and exit of IDLE mode when the caller tries to sequence IMAP commands. This function allows the caller to disable the use of the IDLE extension.

## Syntax


```C++
HRESULT SetIdleMode(
  [in] DWORD dwIdleFlags
);
```



## Parameters

<dl> <dt>

*dwIdleFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that indicates whether to enable the IDLE extension.



| Value                                                                                                                                                                                                                                      | Meaning                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <span id="IMAP_IDLE_DISABLE"></span><span id="imap_idle_disable"></span><dl> <dt>**IMAP\_IDLE\_DISABLE**</dt> <dt>0x00000000</dt> </dl> | Disable the IDLE extension. <br/> |
| <span id="IMAP_IDLE_ENABLE"></span><span id="imap_idle_enable"></span><dl> <dt>**IMAP\_IDLE\_ENABLE**</dt> <dt>0x00000001</dt> </dl>    | Enable the IDLE extension. <br/>  |



 

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



 

 





