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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IWMDRMProvider interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

