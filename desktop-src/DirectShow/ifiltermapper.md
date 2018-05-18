---
Description: 'Note  This interface has been deprecated.'
ms.assetid: 'e2f32235-e331-4c3c-925a-7cfa531e9ab3'
title: IFilterMapper interface
---

# IFilterMapper interface

> [!Note]  
> This interface has been deprecated. It will continue to be supported for backward compatibility with existing applications, but new applications should use the [**IFilterMapper2**](ifiltermapper2.md) interface.

 

This interface provides methods for registering and unregistering filters, and for looking up filters based on their characteristics.

## Members

The **IFilterMapper** interface inherits from the [**IUnknown**](com.iunknown) interface. **IFilterMapper** also has these types of members:

-   [Methods](#methods)

### Methods

The **IFilterMapper** interface has these methods.



| Method                                                                     | Description                                                  |
|:---------------------------------------------------------------------------|:-------------------------------------------------------------|
| [**EnumMatchingFilters**](ifiltermapper-enummatchingfilters.md)           | Finds all filters matching specific requirements.<br/> |
| [**RegisterFilter**](ifiltermapper-registerfilter.md)                     | Records the details of a filter in the registry.<br/>  |
| [**RegisterFilterInstance**](ifiltermapper-registerfilterinstance.md)     | Registers an identifiable instance of a filter.<br/>   |
| [**RegisterPin**](ifiltermapper-registerpin.md)                           | Records the details of a pin in the registry.<br/>     |
| [**RegisterPinType**](ifiltermapper-registerpintype.md)                   | Adds a type for the pin to the registry.<br/>          |
| [**UnregisterFilter**](ifiltermapper-unregisterfilter.md)                 | Deletes a filter from the registry.<br/>               |
| [**UnregisterFilterInstance**](ifiltermapper-unregisterfilterinstance.md) | Deletes an identifiable instance of a filter.<br/>     |
| [**UnregisterPin**](ifiltermapper-unregisterpin.md)                       | Deletes a pin from the registry.<br/>                  |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




