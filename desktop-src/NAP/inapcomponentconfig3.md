---
title: INapComponentConfig3 interface (NapCommon.h)
description: Provides NAP system configuration methods for system health validators (SHVs) to set and modify configuration data for a specific configuration ID.
ms.assetid: dbb78f7a-7c6b-4bf1-b471-374857d5dafe
keywords:
- INapComponentConfig3 interface NAP
- INapComponentConfig3 interface NAP , described
topic_type:
- apiref
api_name:
- INapComponentConfig3
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentConfig3 interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapComponentConfig3** interface provides NAP system configuration methods for system health validators (SHVs) to set and modify configuration data for a specific configuration ID.

> [!Note]  
> This interface inherits all the methods of [**INapComponentConfig2**](inapcomponentconfig2.md) and should be used instead.

 

## Members

The **INapComponentConfig3** interface inherits from [**INapComponentConfig2**](inapcomponentconfig2.md). **INapComponentConfig3** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapComponentConfig3** interface has these methods.



| Method                                                                                | Description                                                                                                    |
|:--------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**INapComponentConfig3::DeleteAllConfig**](inapcomponentconfig3-deleteallconfig.md) | Implemented by SHVs to provide a way to reset the SHV store to its original state after setup.<br/>      |
| [**INapComponentConfig3::DeleteConfig**](inapcomponentconfig3-deleteconfig.md)       | Implemented by SHVs to provide a way to delete configuration data for a specific configuration ID.<br/>  |
| [**INapComponentConfig3::GetConfigFromID**](inapcomponentconfig3-getconfigfromid.md) | Implemented by SHVs to provide a way to obtain configuration data for a specific configuration ID.<br/>  |
| [**INapComponentConfig3::NewConfig**](inapcomponentconfig3-newconfig.md)             | Implemented by SHVs to provide a way to create configuration data for a specific configuration ID.<br/>  |
| [**INapComponentConfig3::SetConfigToID**](inapcomponentconfig3-setconfigtoid.md)     | Implemented by SHVs to provide a way to set the configuration data for a specific configuration ID.<br/> |



 

## Remarks

This interface should not be implemented by system health agents (SHAs) or quarantine enforcement clients (QECs).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapComponentConfig2**](inapcomponentconfig2.md)
</dt> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

 





