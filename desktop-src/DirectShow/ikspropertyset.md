---
description: The IKsPropertySet interface was originally designed as an efficient way to set and retrieve device properties on WDM drivers, using KSProxy to translate the user-mode COM method calls into the kernel-mode property sets used by WDM streaming class drivers. This interface is now also used to pass information strictly between software components.In some cases, software components must implement either this interface, or else the IKsControl interface (documented in the DirectShow DDK). For example, if you are writing a software MPEG-2 decoder for use with the DVD Navigator, you must implement one of these interfaces and also support the DVD-related property sets that the Navigator will send to the decoder. Pins may support one of these interfaces to allow other pins or filters to set or retrieve their properties.Note  Another interface by this name exists in the dsound.h header file. The two interfaces are not compatible. The IKsControl interface, documented in the DirectShow DDK, is now the recommended interface for passing property sets between WDM drivers and user mode components. .
ms.assetid: df26341d-f2d5-4a4e-954e-705e07415808
title: IKsPropertySet interface (Ksproxy.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IKsPropertySet
api_type: 
- COM
api_location: 
- Strmiids.lib
- Strmiids.dll
---

# IKsPropertySet interface

The `IKsPropertySet` interface was originally designed as an efficient way to set and retrieve device properties on WDM drivers, using KSProxy to translate the user-mode COM method calls into the kernel-mode property sets used by WDM streaming class drivers. This interface is now also used to pass information strictly between software components.

In some cases, software components must implement either this interface, or else the **IKsControl** interface (documented in the DirectShow DDK). For example, if you are writing a software MPEG-2 decoder for use with the [DVD Navigator](dvd-navigator-filter.md), you must implement one of these interfaces and also support the DVD-related property sets that the Navigator will send to the decoder. Pins may support one of these interfaces to allow other pins or filters to set or retrieve their properties.

> [!Note]  
> Another interface by this name exists in the dsound.h header file. The two interfaces are not compatible. The **IKsControl** interface, documented in the DirectShow DDK, is now the recommended interface for passing property sets between WDM drivers and user mode components.

 

## Members

The **IKsPropertySet** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IKsPropertySet** also has these types of members:

-   [Methods](#methods)

### Methods

The **IKsPropertySet** interface has these methods.



| Method                                                  | Description                                                                          |
|:--------------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**Get**](ikspropertyset-get.md)                       | Retrieves a property identified by a property set GUID and a property ID.<br/> |
| [**QuerySupported**](ikspropertyset-querysupported.md) | Determines whether an object supports a specified property set.<br/>           |
| [**Set**](ikspropertyset-set.md)                       | Sets a property identified by a property set GUID and a property ID.<br/>      |



 

## Remarks

You must include Ks.h before Ksproxy.h.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Ksproxy.h</dt> </dl>    |
| Library<br/>                  | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 
