---
title: INapEnforcementClientConnection SetPrivateData method (NapEnforcementClient.h)
description: Is used by the NapAgent to set private data.
ms.assetid: 2559a612-8857-4e60-b5bc-dd8235ff69f9
keywords:
- SetPrivateData method NAP
- SetPrivateData method NAP , INapEnforcementClientConnection interface
- INapEnforcementClientConnection interface NAP , SetPrivateData method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection.SetPrivateData
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapEnforcementClientConnection::SetPrivateData method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection::SetPrivateData** method is used by the NapAgent to set private data.

## Syntax


```C++
HRESULT SetPrivateData(
  [in] const PrivateData *privateData
);
```



## Parameters

<dl> <dt>

*privateData* \[in\]
</dt> <dd>

A pointer to a [**PrivateData**](/windows/win32/api/naptypes/ns-naptypes-privatedata) data blob that only the NapAgent can interpret.

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

 

 





