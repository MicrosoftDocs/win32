---
description: Gets a handle to the dialog box that displays error messages and provides one or more buttons to continue, cancel, or abort the application.
ms.assetid: 54deac2e-a395-45dc-b9f9-ecf8140fd9d7
title: IWiaAppErrorHandler::GetWindow method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaAppErrorHandler.GetWindow
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaAppErrorHandler::GetWindow method

Gets a handle to the dialog box that displays error messages and provides one or more buttons to continue, cancel, or abort the application.

## Syntax


```C++
HRESULT GetWindow(
  [out] HWND *phwnd
);
```



## Parameters

<dl> <dt>

*phwnd* \[out\]
</dt> <dd>

Type: **HWND\***

HWND used by the application error handler, the driver error handler, and the default error handler for device message dialog boxes (both error and informational). The output value may be **NULL**.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

*phwnd* points to the window passed into [**ReportStatus**](-wia-iwiaerrorhandler-reportstatus.md) by the Windows Image Acquisition (WIA) 2.0 Proxy. This window must remain valid for the duration of the data transfer.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 




