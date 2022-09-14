---
title: INapSoHConstructor Validate method (NapProtocol.h)
description: Checks the validity of the SoH packet.
ms.assetid: 66338213-43c0-461a-a794-5f18d56bd505
keywords:
- Validate method NAP
- Validate method NAP , INapSoHConstructor interface
- INapSoHConstructor interface NAP , Validate method
topic_type:
- apiref
api_name:
- INapSoHConstructor.Validate
api_location:
- qutil.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSoHConstructor::Validate method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSoHConstructor::Validate** method checks the validity of the SoH packet.

## Syntax


```C++
HRESULT Validate(
  [in] const SoH  *soh,
  [in]       BOOL isRequest
);
```



## Parameters

<dl> <dt>

*soh* \[in\]
</dt> <dd>

A pointer to the constructed [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet.

</dd> <dt>

*isRequest* \[in\]
</dt> <dd>

A **BOOL** that is **TRUE** if the packet is an [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) and **FALSE** if it is an **SoHResponse**.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                            | Description                                                        |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                  | The SoH packet is valid.<br/>                                |
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

[**INapSoHConstructor**](inapsohconstructor.md)
</dt> </dl>

 

 





