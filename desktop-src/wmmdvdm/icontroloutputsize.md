---
title: IControlOutputSize interface
description: The transform can optionally implement the IControlOutputSize interface to enable it to change its output buffer requirements before each call to IMediaTransform Process is processed.
ms.assetid: 23edf7c3-dffd-4f4b-aad4-07a42f2a3af8
keywords:
- IControlOutputSize interface Windows Movie Maker and DVD Maker
- IControlOutputSize interface Windows Movie Maker and DVD Maker , described
topic_type:
- apiref
api_name:
- IControlOutputSize
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IControlOutputSize interface

The transform can optionally implement the **IControlOutputSize** interface to enable it to change its output buffer requirements before each call to [**IMediaTransform::Process**](imediatransform-process.md) is processed. This allows Windows Movie Maker to allot the minimal buffer space that is required for a transition or effect that requires a varying screen size at different times (for example, when rotating a rectangular image).

## Members

The **IControlOutputSize** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IControlOutputSize** also has these types of members:

-   [Methods](#methods)

### Methods

The **IControlOutputSize** interface has these methods.



| Method                                                    | Description                                                                                                                                                           |
|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetOutputSize**](icontroloutputsize-getoutputsize.md) | Gets the output buffer size that Windows Movie Maker intends to allocate for the next call to [**IMediaTransform::Process**](imediatransform-process.md).<br/> |



 

## See also

<dl> <dt>

[**Transform Interfaces**](transform-interfaces.md)
</dt> </dl>

 

 





