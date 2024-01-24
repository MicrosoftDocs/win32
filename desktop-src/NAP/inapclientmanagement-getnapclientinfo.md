---
title: INapClientManagement GetNapClientInfo method (NapManagement.h)
description: Retrieves information about the NAP client.
ms.assetid: c0b57cab-729b-40b2-81d2-32a961e377a5
keywords:
- GetNapClientInfo method NAP
- GetNapClientInfo method NAP , INapClientManagement interface
- INapClientManagement interface NAP , GetNapClientInfo method
topic_type:
- apiref
api_name:
- INapClientManagement.GetNapClientInfo
api_location:
- qagent.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapClientManagement::GetNapClientInfo method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **GetNapClientInfo** method retrieves information about the NAP client.

## Syntax


```C++
HRESULT GetNapClientInfo(
  [out] BOOL          *isNapEnabled,
  [out] CountedString **clientName,
  [out] CountedString **clientDescription,
  [out] CountedString **protocolVersion
) const;
```



## Parameters

<dl> <dt>

*isNapEnabled* \[out\]
</dt> <dd>

A pointer to a BOOL that is set to **TRUE** if NAP is enabled; otherwise it is set to **FALSE**.

</dd> <dt>

*clientName* \[out\]
</dt> <dd>

A pointer to a pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure that contains the client name.

</dd> <dt>

*clientDescription* \[out\]
</dt> <dd>

A pointer to a pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure that contains the client description.

</dd> <dt>

*protocolVersion* \[out\]
</dt> <dd>

A pointer to a pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure that contains the protocol version.

</dd> </dl>

## Return value

The method returns an HRESULT status code including but not limited to one of the following.



| Return code                                                                                         | Description                                                        |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | Operation successful.<br/>                                   |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>      | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>       | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**RPC\_E\_DISCONNECTED**</dt> </dl> | The NapAgent is not running.<br/>                            |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                         |
| Header<br/>                   | <dl> <dt>NapManagement.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapManagement.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qagent.dll</dt> </dl>        |



## See also

<dl> <dt>

[**INapClientManagement**](inapclientmanagement.md)
</dt> </dl>

 

 





