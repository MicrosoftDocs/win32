---
title: IDeliveryOptimizationJob interface (Deliveryoptimization.h)
description: Use the IDeliveryOptimizationJob interface to download ranges of a file.
ms.assetid: 7549F3B2-47E9-44DA-BD9C-AEFB0C36FF15
keywords:
- IDeliveryOptimizationJob interface
- IDeliveryOptimizationJob interface, described
topic_type:
- apiref
api_name:
- IDeliveryOptimizationJob
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationJob interface

Use the **IDeliveryOptimizationJob** interface to download ranges of a file.

## Members

The **IDeliveryOptimizationJob** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IDeliveryOptimizationJob** also has these types of members:

- [Methods](#methods)

### Methods

The **IDeliveryOptimizationJob** interface has these methods.



| Method                                                                  | Description                                                                                         |
|:------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**AddFileWithRanges**](ideliveryoptimizationjob-addfilewithranges.md) | Adds a file to a download job and specifies the ranges of the file you want to download.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IDeliveryOptimizationJob is defined as EE2584CF-A69C-4848-B633-2649962B3EF7<br/>         |



 

