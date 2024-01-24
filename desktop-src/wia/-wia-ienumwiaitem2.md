---
description: Used by applications to enumerate IWiaItem2 objects in the item tree's current folder.
ms.assetid: a82298e0-fbe7-4ef5-99c5-18ff60538e03
title: IEnumWiaItem2 interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEnumWiaItem2
api_type: 
- COM
api_location: 
- Wia.h
---

# IEnumWiaItem2 interface

Used by applications to enumerate [**IWiaItem2**](-wia-iwiaitem2.md) objects in the item tree's current folder.

## Members

The **IEnumWiaItem2** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IEnumWiaItem2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumWiaItem2** interface has these methods.



| Method                                          | Description                                                                                                                    |
|:------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**Clone**](-wia-ienumwiaitem2-clone.md)       | Creates an additional instance of the **IEnumWiaItem2** interface and sends back a pointer to it. <br/>                  |
| [**GetCount**](-wia-ienumwiaitem2-getcount.md) | Returns the number of elements stored by this enumerator. <br/>                                                          |
| [**Next**](-wia-ienumwiaitem2-next.md)         | Fills an array of pointers to [**IWiaItem2**](-wia-iwiaitem2.md) interfaces.<br/>                                       |
| [**Reset**](-wia-ienumwiaitem2-reset.md)       | Resets the enumeration reference to the first [**IWiaItem2**](-wia-iwiaitem2.md) object. <br/>                          |
| [**Skip**](-wia-ienumwiaitem2-skip.md)         | Skips the specified number of items during an enumeration of available [**IWiaItem2**](-wia-iwiaitem2.md) objects.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
