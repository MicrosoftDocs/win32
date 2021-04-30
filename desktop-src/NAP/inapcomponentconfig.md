---
title: INapComponentConfig interface (NapCommon.h)
description: Provides NAP system configuration methods for system health validators (SHVs).
ms.assetid: 979b5c34-8efe-4c48-8236-53fbd25d4249
keywords:
- INapComponentConfig interface NAP
- INapComponentConfig interface NAP , described
topic_type:
- apiref
api_name:
- INapComponentConfig
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapComponentConfig** interface provides NAP system configuration methods for system health validators (SHVs).

> [!Note]  
> [**INapComponentConfig2**](inapcomponentconfig2.md) and [**INapComponentConfig3**](inapcomponentconfig3.md) inherit all the methods of this interface and should be used instead.

 

## Members

The **INapComponentConfig** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapComponentConfig** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapComponentConfig** interface has these methods.



| Method                                                                          | Description                                                                          |
|:--------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**INapComponentConfig::GetConfig**](inapcomponentconfig-getconfig.md)         | Retrieves the SHV component configuration.<br/>                                |
| [**INapComponentConfig::InvokeUI**](inapcomponentconfig-invokeui.md)           | Launches the customized user interface for an SHV component.<br/>              |
| [**INapComponentConfig::IsUISupported**](inapcomponentconfig-isuisupported.md) | Specifies whether the SHV component supports a customized user interface.<br/> |
| [**INapComponentConfig::SetConfig**](inapcomponentconfig-setconfig.md)         | Sets the SHV component configuration.<br/>                                     |



 

## Remarks

This interface should not be implemented by system health agents (SHAs) or quarantine enforcement clients (QECs).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

