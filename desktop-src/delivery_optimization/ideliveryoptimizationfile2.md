---
title: IDeliveryOptimizationFile2 interface
description: The IDeliveryOptimizationFile2 supports setting and getting optional file properties. 
keywords:
- IDeliveryOptimizationFile2 interface
- IDeliveryOptimizationFile2 interface, described
topic_type:
- apiref
api_name:
- IDeliveryOptimizationFile2
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 01/18/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationFile2 interface

The **IDeliveryOptimizationFile2** supports setting and getting optional file properties. 

## Members

The **IDeliveryOptimizationFile2** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IDeliveryOptimizationFile2** also has these types of members:

- [Methods](#methods)

### Methods

The **IDeliveryOptimizationFile2** interface has these methods.

| Method                                                 | Description                                                  |
|:-------------------------------------------------------|:-------------------------------------------------------------|
| [**GetProperty**](ideliveryoptimizationfile2-getproperty.md)  | This method returns a single property of the Delivery Optimization file. |
| [**SetProperty**](ideliveryoptimizationfile2-setproperty.md)  | This method sets a single property of the Delivery Optimization file.    |

## Requirements

| Requirement | Value |
|-------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client      | Windows 10, version 1803 \[desktop apps only\]                                    |
| Minimum supported server      | Windows Server, version 1709 \[desktop apps only\]                                |
| Header                        | Deliveryoptimization.h                                                            |
| IDL                           | DeliveryOptimization.idl                                                          |
| Library                       | Dosvc.lib                                                                         |
| DLL                           | Dosvc.dll                                                                         |
| IID                           | IID_IDeliveryOptimizationFile2 is defined as 3A87296F-6EC2-4126-AB29-E3F8DC4CC390 |
