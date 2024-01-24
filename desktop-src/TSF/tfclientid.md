---
title: TfClientId (Msctf.h)
description: The TfClientId data type is used to identify the client.
ms.assetid: '984dc390-6e15-4491-8c06-77c27c5bdd6f'
keywords:
- TfClientId
ms.topic: article
ms.date: 05/31/2018
---

# TfClientId

The **TfClientId** data type is used to identify the client.


```C++
typedef DWORD TfClientId;
```



## Remarks

Within TSF, applications and text services are generally referred to as clients. Each client receives a unique identifier that it uses to identify itself when calling various TSF manager methods. This identifier is of the **TfClientId** type.

The **TfClientId** data type is supplied by the TSF manager. An application obtains a **TfClientId** value when it calls [ITfThreadMgr::Activate](/windows/desktop/api/Msctf/nf-msctf-itfthreadmgr-activate). The TfClientId value for a text service is passed to the [ITfTextInputProcessor::Activate](/windows/desktop/api/Msctf/nf-msctf-itftextinputprocessor-activate) method. Any object that does not fit the above categories can obtain a client identifier by calling [ITfClientId::GetClientId](/windows/desktop/api/Msctf/nf-msctf-itfclientid-getclientid).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                          |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITfClientId::GetClientId**](/windows/desktop/api/Msctf/nf-msctf-itfclientid-getclientid)
</dt> <dt>

[**ITfTextInputProcessor::Activate**](/windows/desktop/api/Msctf/nf-msctf-itftextinputprocessor-activate)
</dt> <dt>

[**ITfThreadMgr::Activate**](/windows/desktop/api/Msctf/nf-msctf-itfthreadmgr-activate)
</dt> </dl>

 

 





