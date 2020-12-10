---
title: INapServerInfo GetNapServerInfo method (NapServerManagement.h)
description: Retrieves information about the NAP server.
ms.assetid: 02f7ce40-3443-4263-86b2-4276cbc7b694
keywords:
- GetNapServerInfo method NAP
- GetNapServerInfo method NAP , INapServerInfo interface
- INapServerInfo interface NAP , GetNapServerInfo method
topic_type:
- apiref
api_name:
- INapServerInfo.GetNapServerInfo
api_location:
- qsvrmgmt.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapServerInfo::GetNapServerInfo method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapServerInfo::GetNapServerInfo** method retrieves information about the NAP server.

## Syntax


```C++
HRESULT GetNapServerInfo(
  [out] CountedString **serverName,
  [out] CountedString **serverDescription,
  [out] CountedString **protocolVersion
);
```



## Parameters

<dl> <dt>

*serverName* \[out\]
</dt> <dd>

A pointer to a pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure that contains the server name.

</dd> <dt>

*serverDescription* \[out\]
</dt> <dd>

A pointer to a pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure that contains the server description.

</dd> <dt>

*protocolVersion* \[out\]
</dt> <dd>

A pointer to a pointer to a [**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring) structure that contains the protocol version.

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
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>NapServerManagement.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapServerManagement.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qsvrmgmt.dll</dt> </dl>            |



## See also

<dl> <dt>

[**INapServerInfo**](inapserverinfo.md)
</dt> <dt>

[**CountedString**](/windows/win32/api/naptypes/ns-naptypes-countedstring)
</dt> </dl>

 

 





