---
title: OnWindowUpdate event
description: Called when one of the properties on the Window object changes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c1bc772-fa8d-486f-bb9c-fd34ee955d0f
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnWindowUpdate event RDP
topic_type:
- apiref
api_name:
- OnWindowUpdate
api_location:
- RdpEncom.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnWindowUpdate event

Called when one of the properties on the Window object changes.

## Syntax


```C++
void OnWindowUpdate(
  [in] IDispatch *pWindow
);
```



## Parameters

<dl> <dt>

*pWindow* \[in\]
</dt> <dd>

The window whose property values changed. Query the **IDispatch** interface for the [**IRDPSRAPIWindow**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiwindow?branch=master) interface that you use to retrieve information about the window.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

You should query all the properties of the window and update the user interface accordingly.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>RdpEncomAPI.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RdpEncomAPI.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RdpEncomAPI.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RdpEncom.dll</dt> </dl>    |



## See also

<dl> <dt>

[**\_IRDPSessionEvents**](/windows/win32/RdpEncomAPI/?branch=master)
</dt> </dl>

 

 





