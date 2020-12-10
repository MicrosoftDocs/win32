---
title: INapSoHConstructor interface (NapProtocol.h)
description: Are used by SHAs to construct SoHRequests and by SHVs to construct SoHResponses.
ms.assetid: ad79c80a-3003-4465-b350-77890c217d63
keywords:
- INapSoHConstructor interface NAP
- INapSoHConstructor interface NAP , described
topic_type:
- apiref
api_name:
- INapSoHConstructor
api_location:
- qutil.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSoHConstructor interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSoHConstructor** provides methods that are used by SHAs to construct [**SoHRequests**](/windows/win32/api/naptypes/ns-naptypes-soh) and by SHVs to construct **SoHResponses**.

## Members

The **INapSoHConstructor** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapSoHConstructor** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapSoHConstructor** interface has these methods.



| Method                                                                                   | Description                                         |
|:-----------------------------------------------------------------------------------------|:----------------------------------------------------|
| [**INapSoHConstructor::AppendAttribute**](inapsohconstructor-appendattribute-method.md) | Adds a TLV to the end of the SoH buffer.<br/> |
| [**INapSoHConstructor::GetSoH**](inapsohconstructor-getsoh-method.md)                   | Retrieves the constructed SoH packet.<br/>    |
| [**INapSoHConstructor::Initialize**](inapsohconstructor-initialize-method.md)           | Initializes the SoH packet.<br/>              |
| [**INapSoHConstructor::Validate**](inapsohconstructor-validate-method.md)               | Checks the validity of the SoH packet.<br/>   |



 

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

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

