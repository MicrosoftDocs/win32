---
Description: 'Note  This interface has been deprecated.'
ms.assetid: '59cb809d-84f5-42c4-a385-0f586af4d048'
title: IEnumRegFilters interface
---

# IEnumRegFilters interface

> [!Note]  
> This interface has been deprecated. New applications should call [**IFilterMapper2::EnumMatchingFilters**](ifiltermapper2-enummatchingfilters.md), which enumerates monikers and returns a pointer to the **IEnumMoniker** interface.

 

This interface provides methods for enumerating registered filters. The [**IFilterMapper::EnumMatchingFilters**](ifiltermapper-enummatchingfilters.md) method returns a pointer to this interface. However, [**IFilterMapper**](ifiltermapper.md) has been deprecated in favor of [**IFilterMapper2**](ifiltermapper2.md).

## Members

The **IEnumRegFilters** interface inherits from the [**IUnknown**](com.iunknown) interface. **IEnumRegFilters** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumRegFilters** interface has these methods.



| Method                                 | Description                                                                                                  |
|:---------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| [**Clone**](ienumregfilters-clone.md) | Not currently implemented.<br/>                                                                        |
| [**Next**](ienumregfilters-next.md)   | Fills an array with the next filters that meet the requirements.<br/>                                  |
| [**Reset**](ienumregfilters-reset.md) | Makes the [**Next**](ienumregfilters-next.md) method start again, beginning at the first filter.<br/> |
| [**Skip**](ienumregfilters-skip.md)   | Not currently implemented.<br/>                                                                        |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




