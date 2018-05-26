---
title: TfClientId
description: The TfClientId data type is used to identify the client.
ms.assetid: ccb06ed3-67e2-4e46-8037-ff215ba23601
keywords:
- TfClientId
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TfClientId

The **TfClientId** data type is used to identify the client.


```C++
typedef DWORD TfClientId;
```



## Remarks

Within TSF, applications and text services are generally referred to as clients. Each client receives a unique identifier that it uses to identify itself when calling various TSF manager methods. This identifier is of the **TfClientId** type.

The **TfClientId** data type is supplied by the TSF manager. An application obtains a **TfClientId** value when it calls [ITfThreadMgr::Activate](/windows/win32/Msctf/nf-msctf-itfthreadmgr-activate?branch=master). The TfClientId value for a text service is passed to the [ITfTextInputProcessor::Activate](/windows/win32/Msctf/nf-msctf-itftextinputprocessor-activate?branch=master) method. Any object that does not fit the above categories can obtain a client identifier by calling [ITfClientId::GetClientId](/windows/win32/Msctf/nf-msctf-itfclientid-getclientid?branch=master).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                          |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITfClientId::GetClientId**](/windows/win32/Msctf/nf-msctf-itfclientid-getclientid?branch=master)
</dt> <dt>

[**ITfTextInputProcessor::Activate**](/windows/win32/Msctf/nf-msctf-itftextinputprocessor-activate?branch=master)
</dt> <dt>

[**ITfThreadMgr::Activate**](/windows/win32/Msctf/nf-msctf-itfthreadmgr-activate?branch=master)
</dt> </dl>

 

 





