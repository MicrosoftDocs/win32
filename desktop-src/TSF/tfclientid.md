---
title: TfClientId
description: The TfClientId data type is used to identify the client.
ms.assetid: 'ccb06ed3-67e2-4e46-8037-ff215ba23601'
keywords: ["TfClientId"]
---

# TfClientId

The **TfClientId** data type is used to identify the client.


```C++
typedef DWORD TfClientId;
```



## Remarks

Within TSF, applications and text services are generally referred to as clients. Each client receives a unique identifier that it uses to identify itself when calling various TSF manager methods. This identifier is of the **TfClientId** type.

The **TfClientId** data type is supplied by the TSF manager. An application obtains a **TfClientId** value when it calls [ITfThreadMgr::Activate](itfthreadmgr-activate.md). The TfClientId value for a text service is passed to the [ITfTextInputProcessor::Activate](itftextinputprocessor-activate.md) method. Any object that does not fit the above categories can obtain a client identifier by calling [ITfClientId::GetClientId](itfclientid-getclientid.md).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                          |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITfClientId::GetClientId**](itfclientid-getclientid.md)
</dt> <dt>

[**ITfTextInputProcessor::Activate**](itftextinputprocessor-activate.md)
</dt> <dt>

[**ITfThreadMgr::Activate**](itfthreadmgr-activate.md)
</dt> </dl>

 

 





