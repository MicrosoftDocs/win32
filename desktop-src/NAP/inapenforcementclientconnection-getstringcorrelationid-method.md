---
title: INapEnforcementClientConnection GetStringCorrelationId method
description: Gets the string version of the ID used to correlate requests and responses.
ms.assetid: d744fa4e-5e30-429e-810d-7326047bb3f8
keywords:
- GetStringCorrelationId method NAP
- GetStringCorrelationId method NAP , INapEnforcementClientConnection interface
- INapEnforcementClientConnection interface NAP , GetStringCorrelationId method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection.GetStringCorrelationId
api_location:
- qagent.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INapEnforcementClientConnection::GetStringCorrelationId method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection::GetStringCorrelationId** method gets the string version of the ID used to correlate requests and responses.

## Syntax


```C++
HRESULT GetStringCorrelationId(
  [out] CountedString **correlationId
);
```



## Parameters

<dl> <dt>

*correlationId* \[out\]
</dt> <dd>

A pointer to a [**CountedString**](/windows/win32/NapTypes/ns-naptypes-tagcountedstring?branch=master) structure that contains the string version of the connection's [**CorrelationId**](/windows/win32/NapTypes/ns-naptypes-tagcorrelationid?branch=master).

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapEnforcementClient.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapEnforcementClient.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qagent.dll</dt> </dl>               |



## See also

<dl> <dt>

[**INapEnforcementClientConnection**](inapenforcementclientconnection.md)
</dt> </dl>

 

 





