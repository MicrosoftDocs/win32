---
title: INapSoHConstructor GetSoH method (NapProtocol.h)
description: Retrieves the constructed SoHRequest or SoHResponse packet.
ms.assetid: 402c72fd-9e23-453a-8c95-57615295e056
keywords:
- GetSoH method NAP
- GetSoH method NAP , INapSoHConstructor interface
- INapSoHConstructor interface NAP , GetSoH method
topic_type:
- apiref
api_name:
- INapSoHConstructor.GetSoH
api_location:
- qutil.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSoHConstructor::GetSoH method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSoHConstructor::GetSoH** method retrieves the constructed SoHRequest or SoHResponse packet.

## Syntax


```C++
HRESULT GetSoH(
  [out] SoH **soh
);
```



## Parameters

<dl> <dt>

*soh* \[out\]
</dt> <dd>

A pointer to a pointer to the constructed [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) or **SoHResponse** packet.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation successful.<br/>                                   |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

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

 

 





