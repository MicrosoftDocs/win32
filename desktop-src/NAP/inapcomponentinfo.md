---
title: INapComponentInfo interface (NapCommon.h)
description: Provides methods that plug-in components (such as SHAs and SHVs) must implement for the NAP system to communicate with them.
ms.assetid: eeff4f57-72e0-465f-9a18-ed72dad82bc7
keywords:
- INapComponentInfo interface NAP
- INapComponentInfo interface NAP , described
topic_type:
- apiref
api_name:
- INapComponentInfo
api_location:
- NapCommon.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapComponentInfo interface

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapComponentInfo** interface provides methods that plug-in components (such as SHAs and SHVs) must implement for the NAP system to communicate with them. The NAP system calls your implementation of these methods to retrieve static administrative information (for example, friendly name or localized strings).

## Members

The **INapComponentInfo** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **INapComponentInfo** also has these types of members:

-   [Methods](#methods)

### Methods

The **INapComponentInfo** interface has these methods.



| Method                                                                                                         | Description                                                                                                   |
|:---------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**INapComponentInfo::ConvertErrorCodeToMessageId**](inapcomponentinfo-converterrorcodetomessageid-method.md) | Used by the NAP System to request the health client convert an HRESULT error code to a message ID.<br/> |
| [**INapComponentInfo::GetDescription**](inapcomponentinfo-getdescription-method.md)                           | Used by the NAP System to get the description of a health client.<br/>                                  |
| [**INapComponentInfo::GetFriendlyName**](inapcomponentinfo-getfriendlyname-method.md)                         | Used by the NAP System to get the friendly name of a health client.<br/>                                |
| [**INapComponentInfo::GetIcon**](inapcomponentinfo-geticon-method.md)                                         | Used by the NAP System to get the icon of a health client.<br/>                                         |
| [**INapComponentInfo::GetLocalizedString**](inapcomponentinfo-getlocalizedstring-method.md)                   | Used by the NAP System to get localized strings.<br/>                                                   |
| [**INapComponentInfo::GetVendorName**](inapcomponentinfo-getvendorname-method.md)                             | Used by the NAP System to get the vendor name of a health client.<br/>                                  |
| [**INapComponentInfo::GetVersion**](inapcomponentinfo-getversion-method.md)                                   | Used by the NAP System to get the version of a health client.<br/>                                      |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>NapCommon.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapCommon.idl</dt> </dl> |



## See also

<dl> <dt>

[NAP Interfaces](nap-interfaces.md)
</dt> <dt>

[NAP Reference](nap-reference.md)
</dt> </dl>

 

