---
title: INapEnforcementClientConnection SetIsolationInfo method
description: Is used by the NapAgent to set the isolation information of the client.
ms.assetid: e92d8762-4ae9-40e5-a18e-7da757aa6f9e
keywords:
- SetIsolationInfo method NAP
- SetIsolationInfo method NAP , INapEnforcementClientConnection interface
- INapEnforcementClientConnection interface NAP , SetIsolationInfo method
topic_type:
- apiref
api_name:
- INapEnforcementClientConnection.SetIsolationInfo
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

# INapEnforcementClientConnection::SetIsolationInfo method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapEnforcementClientConnection::SetIsolationInfo** method is used by the NapAgent to set the isolation information of the client.

## Syntax


```C++
HRESULT SetIsolationInfo(
  [in] const IsolationInfo *isolationInfo
);
```



## Parameters

<dl> <dt>

*isolationInfo* \[in\]
</dt> <dd>

A pointer to an [**IsolationInfo**](/windows/win32/NapTypes/ns-naptypes-tagisolationinfo?branch=master) structure that contains the connectivity state of the client.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

This information is set by NapAgent after processing an SoHResponse and must not be set by the enforcer.

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

 

 





