---
title: INapEnforcementClientConnection2 SetIsolationInfoEx method
description: Is used by the NapAgent to set the isolation information for the client.
ms.assetid: 1b1a41a1-73a6-4c81-8366-15d06c67e228
keywords:
- SetIsolationInfoEx method NAP
- SetIsolationInfoEx method NAP , INapEnforcementClientConnection2 interface
- INapEnforcementClientConnection2 interface NAP , SetIsolationInfoEx method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection2.SetIsolationInfoEx
api_location:
- qagent.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INapEnforcementClientConnection2::SetIsolationInfoEx method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection2::SetIsolationInfoEx** method is used by the NapAgent to set the isolation information for the client.

## Syntax


```C++
HRESULT SetIsolationInfoEx(
  [in] const IsolationInfoEx *isolationInfo
);
```



## Parameters

<dl> <dt>

*isolationInfo* \[in\]
</dt> <dd>

A pointer to an [**IsolationInfoEx**](/windows/desktop/api/NapTypes/ns-naptypes-tagisolationinfoex) structure that contains the connectivity state of the client.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

This information is set by NapAgent after processing an [**SoHResponse**](/windows/desktop/api/NapTypes/ns-naptypes-tagsoh) and must not be set by the enforcer.

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

[**INapEnforcementClientConnection2**](inapenforcementclientconnection2.md)
</dt> </dl>

 

 





