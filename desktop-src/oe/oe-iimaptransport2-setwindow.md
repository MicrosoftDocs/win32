---
title: IIMAPTransport2 SetWindow method
description: Creates a new window used for asynchronous Windows Sockets (Winsock) processing.
ms.assetid: dd5d17d9-f947-4caf-a841-9a76b69447a5
keywords:
- SetWindow method Windows Mail (formerly Outlook Express)
- SetWindow method Windows Mail (formerly Outlook Express) , IIMAPTransport2 interface
- IIMAPTransport2 interface Windows Mail (formerly Outlook Express) , SetWindow method
topic_type:
- apiref
api_name:
- IIMAPTransport2.SetWindow
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

# IIMAPTransport2::SetWindow method

\[**IIMAPTransport2::SetWindow** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a new window used for asynchronous Windows Sockets (Winsock) processing.

## Syntax


```C++
HRESULT SetWindow();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                   |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**NOERROR**</dt> </dl>       | Indicates success. <br/>                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that a new window could not be created. <br/> |
| <dl> <dt>**IXP\_E\_CONN**</dt> </dl>  | Indicates that the socket could not be connected. <br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Indicates that an unknown error has occurred. <br/>     |



 

## Remarks

You must call the [**IIMAPTransport2::ResetWindow**](oe-iimaptransport2-resetwindow.md) method before you call this method to avoid window handle leaks.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





