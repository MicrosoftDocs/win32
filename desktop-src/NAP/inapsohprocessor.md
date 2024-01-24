---
title: INapSoHProcessor interface (NapProtocol.h)
description: Are used by SHAs to process the contents of SoHResponses and by SHVs to process the contents of SoHRequests.
ms.assetid: c2dd71ca-a4dd-44d2-81ab-b83e90599a2f
keywords:
- INapSoHProcessor interface NAP
- INapSoHProcessor interface NAP , described
topic_type:
- apiref
api_name:
- INapSoHProcessor
api_location:
- qutil.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSoHProcessor interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSoHProcessor** provides methods that are used by SHAs to process the contents of [**SoHResponses**](/windows/win32/api/naptypes/ns-naptypes-soh) and by SHVs to process the contents of **SoHRequests**.

## Members

The **INapSoHProcessor** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapSoHProcessor** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapSoHProcessor** interface has these methods.



| Method                                                                                           | Description                                                                           |
|:-------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**INapSoHProcessor::FindNextAttribute**](inapsohprocessor-findnextattribute-method.md)         | Finds the location index of the next SoH packet attribute.<br/>                 |
| [**INapSoHProcessor::GetAttribute**](inapsohprocessor-getattribute-method.md)                   | Retrieves the attribute type and value.<br/>                                    |
| [**INapSoHProcessor::GetNumberOfAttributes**](inapsohprocessor-getnumberofattributes-method.md) | Retrieves the number of attributes contained in the SoH.<br/>                   |
| [**INapSoHProcessor::Initialize**](inapsohprocessor-initialize-method.md)                       | Initializes the SoH protocol packet and NAP System for content processing.<br/> |



 

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

 

