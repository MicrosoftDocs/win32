---
title: INapEnforcementClientConnection GetPrivateData method (NapEnforcementClient.h)
description: Is used by the NapAgent to get private data.
ms.assetid: d38ef523-b645-401f-b3a9-1315ef39931a
keywords:
- GetPrivateData method NAP
- GetPrivateData method NAP , INapEnforcementClientConnection interface
- INapEnforcementClientConnection interface NAP , GetPrivateData method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection.GetPrivateData
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection::GetPrivateData method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection::GetPrivateData** method is used by the NapAgent to get private data.

## Syntax


```C++
HRESULT GetPrivateData(
  [out] PrivateData **privateData
);
```



## Parameters

<dl> <dt>

*privateData* \[out\]
</dt> <dd>

A pointer to a pointer to a [**PrivateData**](/windows/win32/api/naptypes/ns-naptypes-privatedata) opaque data blob that only the NapAgent can interpret.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Requirements



| Requirement | Value |
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

 

 





