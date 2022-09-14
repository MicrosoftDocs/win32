---
title: IBackgroundCopyFile5 interface (Deliveryoptimization.h)
description: Use this interface to get or set generic properties of Delivery Optimization file transfers.
ms.assetid: 2D729717-62D2-4C69-92FE-F4289EC48DF1
keywords:
- IBackgroundCopyFile5 interface
- IBackgroundCopyFile5 interface, described
topic_type:
- apiref
api_name:
- IBackgroundCopyFile5
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyFile5 interface

Use this interface to get or set generic properties of Delivery Optimization file transfers.

To get an **IBackgroundCopyFile5** interface pointer, call the **IBackgroundCopyFile::QueryInterface** method using __uuidof(IBackgroundCopyFile5) for the interface identifier.

## Members

The **IBackgroundCopyFile5** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IBackgroundCopyFile5** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBackgroundCopyFile5** interface has these methods.



| Method                                                  | Description                                                         |
|:--------------------------------------------------------|:--------------------------------------------------------------------|
| [**GetProperty**](ibackgroundcopyfile5-getproperty.md) | Gets the value of a generic BackgroundCopyFile property.<br/> |
| [**SetProperty**](ibackgroundcopyfile5-setproperty.md) | Sets the value of a generic BackgroundCopyFile property.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyFile5 is defined as 85C1657F-DAFC-40E8-8834-DF18EA25717E<br/>             |



## See also

<dl> <dt>

[**IBackgroundCopyFile**](ibackgroundcopyfile.md)
</dt> <dt>

[**IBackgroundCopyFile2**](ibackgroundcopyfile2.md)
</dt> </dl>

 

