---
title: IOutlookExpress Start method
description: Starts the application.
ms.assetid: f0e9d882-7b8c-4b16-88f4-fd8f1b8cc76b
keywords:
- Start method Windows Mail (formerly Outlook Express)
- Start method Windows Mail (formerly Outlook Express) , IOutlookExpress interface
- IOutlookExpress interface Windows Mail (formerly Outlook Express) , Start method
topic_type:
- apiref
api_name:
- IOutlookExpress.Start
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

# IOutlookExpress::Start method

\[**IOutlookExpress::Start** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Starts the application.

## Syntax


```C++
HRESULT Start(
  [in] DWORD   dwFlags,
  [in] LPCWSTR pwszCmdLine,
  [in] INT     nCmdShow
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Flags used in start.

<dl> <dt>

<span id="MSOEAPI_START_SHOWSPLASH"></span><span id="msoeapi_start_showsplash"></span>**MSOEAPI\_START\_SHOWSPLASH** (0x00000001)
</dt> <dt>

<span id="MSOEAPI_START_MESSAGEPUMP"></span><span id="msoeapi_start_messagepump"></span>**MSOEAPI\_START\_MESSAGEPUMP** (0x00000002)
</dt> <dt>

<span id="MSOEAPI_START_ALLOWCOMPACTION"></span><span id="msoeapi_start_allowcompaction"></span>**MSOEAPI\_START\_ALLOWCOMPACTION** (0x00000004)
</dt> <dt>

<span id="MSOEAPI_START_INSTANCEMUTEX"></span><span id="msoeapi_start_instancemutex"></span>**MSOEAPI\_START\_INSTANCEMUTEX** (0x00000008)
</dt> <dt>

<span id="MSOEAPI_START_SHOWERRORS"></span><span id="msoeapi_start_showerrors"></span>**MSOEAPI\_START\_SHOWERRORS** (0x00000010)
</dt> <dt>

<span id="MSOEAPI_START_APPWINDOW"></span><span id="msoeapi_start_appwindow"></span>**MSOEAPI\_START\_APPWINDOW** (0x00000020)
</dt> <dt>

<span id="MSOEAPI_START_DEFAULTIDENTITY"></span><span id="msoeapi_start_defaultidentity"></span>**MSOEAPI\_START\_DEFAULTIDENTITY** (0x00000040)
</dt> </dl> </dd> <dt>

*pwszCmdLine* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies string identifying desired action.

</dd> <dt>

*nCmdShow* \[in\]
</dt> <dd>

Type: **INT**

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
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





