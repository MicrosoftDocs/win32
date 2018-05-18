---
title: CoStartOutlookExpress function
description: Do not use. Starts Microsoft Outlook Express.
ms.assetid: 'bb02a1fe-945d-44bc-915f-4903f64a9bc3'
keywords: ["CoStartOutlookExpress function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- CoStartOutlookExpress
api_location:
- Msoe.dll
api_type:
- DllExport
---

# CoStartOutlookExpress function

Do not use. Starts Microsoft Outlook Express.

## Syntax


```C++
HRESULT CoStartOutlookExpress(
  _In_ DWORD  dwFlags,
  _In_ LPCSTR pszCmdLine,
  _In_ INT    nCmdShow
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

*pszCmdLine* \[in\]
</dt> <dd>

Type: **LPCSTR**

Command line switches. When this parameter is not **NULL**, then the launch of the application will not show a splash screen even if you have set *dwFlags* to **MSOEAPI\_START\_SHOWSPLASH**.

</dd> <dt>

*nCmdShow* \[in\]
</dt> <dd>

Type: **INT**

Flag that specifies how to display the Outlook Express window. To run the application in the background with no UI, use SW\_HIDE.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                       |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msoe.dll</dt> </dl>  |



 

 





