---
title: INapComponentConfig2 interface (NapCommon.h)
description: Provides NAP system configuration methods for system health validators (SHVs) to configure a network policy server (NPS) user interface remotely.
ms.assetid: 35150184-300c-4ea4-bff9-b3c33fa3156b
keywords:
- INapComponentConfig2 interface NAP
- INapComponentConfig2 interface NAP , described
topic_type:
- apiref
api_name:
- INapComponentConfig2
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig2 interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapComponentConfig2** interface provides NAP system configuration methods for system health validators (SHVs) to configure a network policy server (NPS) user interface remotely.

> [!Note]  
> This interface inherits all the methods of [**INapComponentConfig**](inapcomponentconfig.md) and should be used instead.

 

## Members

The **INapComponentConfig2** interface inherits from [**INapComponentConfig**](inapcomponentconfig.md). **INapComponentConfig2** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapComponentConfig2** interface has these methods.



| Method                                                                                                | Description                                                                                                                                                                |
|:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**INapComponentConfig2::InvokeUIForMachine**](inapcomponentconfig2-invokeuiformachine.md)           | Implemented by SHVs as needed to manage remote configuration directly on the machine specified.<br/>                                                                 |
| [**INapComponentConfig2::InvokeUIFromConfigBlob**](inapcomponentconfig2-invokeuifromconfigblob.md)   | Implemented by SHVs as needed to load the configuration of the remote machine in memory and to display a UI that allows manipulation of the configuration data.<br/> |
| [**INapComponentConfig2::IsRemoteConfigSupported**](inapcomponentconfig2-isremoteconfigsupported.md) | Implemented by SHVs to indicate whether remote configuration is supported.<br/>                                                                                      |



 

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

[**INapComponentConfig**](inapcomponentconfig.md)
</dt> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

 





