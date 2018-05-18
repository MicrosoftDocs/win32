---
title: ISMTPTransport2 SetWindow method
description: Creates a new window used for asynchronous Windows Sockets (Winsock) processing.
ms.assetid: '68f842e2-d04c-46f2-8639-7971670044de'
keywords: ["SetWindow method Windows Mail (formerly Outlook Express)", "SetWindow method Windows Mail (formerly Outlook Express) , ISMTPTransport2 interface", "ISMTPTransport2 interface Windows Mail (formerly Outlook Express) , SetWindow method"]
topic_type:
- apiref
api_name:
- ISMTPTransport2.SetWindow
api_location:
- Inetcomm.dll
api_type:
- COM
---

# ISMTPTransport2::SetWindow method

\[**ISMTPTransport2::SetWindow** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

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

You must call the [**ISMTPTransport2::ResetWindow**](oe-ismtptransport2-resetwindow.md) method before you call this method to avoid window handle leaks.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





