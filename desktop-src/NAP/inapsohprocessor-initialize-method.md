---
title: INapSoHProcessor Initialize method (NapProtocol.h)
description: Initializes the protocol packet and SoH processor system. This method must be called exactly once.
ms.assetid: 4fccc847-3c4d-4fc5-935d-28fb2964a9be
keywords:
- Initialize method NAP
- Initialize method NAP , INapSoHProcessor interface
- INapSoHProcessor interface NAP , Initialize method
topic_type:
- apiref
api_name:
- INapSoHProcessor.Initialize
api_location:
- qutil.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSoHProcessor::Initialize method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSoHProcessor::Initialize** method initializes the protocol packet and SoH processor system. This method must be called exactly once.

## Syntax


```C++
HRESULT Initialize(
  [in]  const SoH                  *soh,
  [in]        BOOL                 isRequest,
  [out]       SystemHealthEntityId *id
);
```



## Parameters

<dl> <dt>

*soh* \[in\]
</dt> <dd>

A pointer to the [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet to be processed.

</dd> <dt>

*isRequest* \[in\]
</dt> <dd>

A **BOOL** that is **TRUE** if the packet is an [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) and **FALSE** if it is an **SoHResponse**.

</dd> <dt>

*id* \[out\]
</dt> <dd>

A unique [SystemHealthEntityId](nap-datatypes.md) that contains the ID of the SHA or SHV that constructed the packet.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                            | Description                                                        |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                  | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>        | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>         | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**NAP\_E\_INVALID\_PACKET**</dt> </dl> | The SoH packet is invalid.<br/>                              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>NapProtocol.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapProtocol.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qutil.dll</dt> </dl>       |



## See also

<dl> <dt>

[**INapSoHProcessor**](inapsohprocessor.md)
</dt> </dl>

 

 





