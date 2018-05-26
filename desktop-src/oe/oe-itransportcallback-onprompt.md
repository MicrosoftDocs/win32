---
title: ITransportCallback OnPrompt method
description: Called when the transport requires user input.
ms.assetid: 3f66167e-63d3-45e1-8fc9-e4bd35829824
keywords:
- OnPrompt method Windows Mail (formerly Outlook Express)
- OnPrompt method Windows Mail (formerly Outlook Express) , ITransportCallback interface
- ITransportCallback interface Windows Mail (formerly Outlook Express) , OnPrompt method
topic_type:
- apiref
api_name:
- ITransportCallback.OnPrompt
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

# ITransportCallback::OnPrompt method

\[**ITransportCallback::OnPrompt** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called when the transport requires user input.

## Syntax


```C++
INT OnPrompt(
  [in] HRESULT            hrError,
  [in] LPCTSTR            pszText,
  [in] LPCTSTR            pszCaption,
  [in] UINT               uType,
  [in] IInternetTransport *pTransport
);
```



## Parameters

<dl> <dt>

*hrError* \[in\]
</dt> <dd>

Type: **HRESULT**

Specifies the HRESULT for the reason for user prompt. This is usually an error.

</dd> <dt>

*pszText* \[in\]
</dt> <dd>

Type: **LPCTSTR**

Specifies an **LPCTSTR** that contains the suggested text of the question to be displayed.

</dd> <dt>

*pszCaption* \[in\]
</dt> <dd>

Type: **LPCTSTR**

Specifies an **LPCTSTR** that contains the suggested caption of the message box.

</dd> <dt>

*uType* \[in\]
</dt> <dd>

Type: **UINT**

Specifies a **UINT** to be passed through to the Win32 [**MessageBox**](https://msdn.microsoft.com/library/windows/desktop/ms645505) function. See the *uType* parameter of **MessageBox** for more information.

</dd> <dt>

*pTransport* \[in\]
</dt> <dd>

Type: **[**IInternetTransport**](oe-iinternettransport.md)\***

Specifies a pointer to the [**IInternetTransport**](oe-iinternettransport.md) object that called **OnPrompt**.

</dd> </dl>

## Return value

Type: **INT**

Returns the same values as the [**MessageBox**](https://msdn.microsoft.com/library/windows/desktop/ms645505) function.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





