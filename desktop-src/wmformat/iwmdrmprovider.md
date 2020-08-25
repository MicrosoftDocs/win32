---
title: IWMDRMProvider interface
description: The IWMDRMProvider interface provides a method that creates the other objects of the Microsoft Windows Media DRM Client Extended APIs.You can obtain a pointer to an instance of this interface by calling the WMDRMCreateProvider function.
ms.assetid: bcd346e3-a79f-49a8-b5f9-b9ae8b54527a
keywords:
- IWMDRMProvider interface windows Media Format
- IWMDRMProvider interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMProvider
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMProvider interface

The **IWMDRMProvider** interface provides a method that creates the other objects of the Microsoft Windows Media DRM Client Extended APIs.

You can obtain a pointer to an instance of this interface by calling the [**WMDRMCreateProvider**](wmdrmcreateprovider.md) function. To obtain a pointer to an instance of this interface that can create secure objects, you must call the [**WMDRMCreateProtectedProvider**](wmdrmcreateprotectedprovider.md) function.

## Members

The **IWMDRMProvider** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMProvider** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMProvider** interface has these methods.



| Method                                              | Description                                                                                          |
|:----------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**CreateObject**](iwmdrmprovider-createobject.md) | Retrieves a pointer to a specified interface, creating the implementing object if needed.<br/> |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> </dl>

 

