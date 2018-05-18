---
title: ITransportCallback OnLogonPrompt method
description: Called when the transport requires logon information.
ms.assetid: '03179c32-497b-4b3d-b463-a932bf896211'
keywords: ["OnLogonPrompt method Windows Mail (formerly Outlook Express)", "OnLogonPrompt method Windows Mail (formerly Outlook Express) , ITransportCallback interface", "ITransportCallback interface Windows Mail (formerly Outlook Express) , OnLogonPrompt method"]
topic_type:
- apiref
api_name:
- ITransportCallback.OnLogonPrompt
api_location:
- Msoe.dll
api_type:
- COM
---

# ITransportCallback::OnLogonPrompt method

\[**ITransportCallback::OnLogonPrompt** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called when the transport requires logon information.

## Syntax


```C++
HRESULT OnLogonPrompt(
  [in, out] LPINETSERVER       pInetServer,
  [in]      IInternetTransport *pTransport
);
```



## Parameters

<dl> <dt>

*pInetServer* \[in, out\]
</dt> <dd>

Type: **LPINETSERVER**

Specifies a pointer to the [**INETSERVER**](oe-inetserver.md) structure that contains information about the current Internet server.

</dd> <dt>

*pTransport* \[in\]
</dt> <dd>

Type: **[**IInternetTransport**](oe-iinternettransport.md)\***

Specifies a pointer to the [**IInternetTransport**](oe-iinternettransport.md) object that called **OnLogonPrompt**.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                             | Description                                                                                                                     |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the user entered new logon information and that the transport should try to reconnect to the server. <br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the user wants to cancel the current logon attempt. The transport returns to the disconnected state. <br/> |



 

## Remarks

The client should prompt the user and fill the **szUserName** and **szPassword** fields of the specified [**INETSERVER**](oe-inetserver.md) structure. The client should not attempt to change any other fields in this structure; they should be used only for display.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





