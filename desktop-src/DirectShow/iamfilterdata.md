---
Description: 'Note  This interface has been deprecated.'
ms.assetid: 'd9800850-b0ee-44f7-bcb4-f2bac8d17693'
title: IAMFilterData interface
---

# IAMFilterData interface

> [!Note]  
> This interface has been deprecated. New applications should use the [**IFilterMapper2**](ifiltermapper2.md) interface instead.

 

The `IAMFilterData` interface converts filter information to packed binary data, which can be stored in the registry. The Filter Mapper object exposes this interface.

## Members

The **IAMFilterData** interface inherits from the [**IUnknown**](com.iunknown) interface. **IAMFilterData** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMFilterData** interface has these methods.



| Method                                                     | Description                                               |
|:-----------------------------------------------------------|:----------------------------------------------------------|
| [**CreateFilterData**](iamfilterdata-createfilterdata.md) | Creates binary registry data for a filter.<br/>     |
| [**ParseFilterData**](iamfilterdata-parsefilterdata.md)   | Unpacks the binary registry data for a filter.<br/> |



 

## Remarks

> [!Note]  
> The header Fil\_data.h is located in the [Mapper Sample](mapper-sample.md) directory in the Windows SDK.

 

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Fil\_data.h</dt> </dl> |



## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




