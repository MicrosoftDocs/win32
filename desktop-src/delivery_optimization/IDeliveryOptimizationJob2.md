---
title: IDeliveryOptimizationJob2 interface
description: "Learn more about: IDeliveryOptimizationJob2 interface"
keywords:
- IDeliveryOptimizationJob2 interface
topic_type:
- apiref
api_name:
- IDeliveryOptimizationJob2
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 01/18/2019
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationJob2 interface

The IDeliveryOptimizationJob2 enables adding a single file to the download job, and retrieving the file immediately. This interface also supports setting and getting optional job properties.

## Members

The **IDeliveryOptimizationJob2** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IDeliveryOptimizationJob2** also has these types of members:

- [Methods](#methods)

### Methods

The **IDeliveryOptimizationJob2** interface has these methods.

| Method                                              | Description                                                          |
|:----------------------------------------------------|----------------------------------------------------------------------|
| [**AddFile**](ideliveryoptimizationjob2-addfile.md) | The AddFile method adds a single file to an existing DO job.         |
| [**GetProperty**](ideliveryoptimizationjob2-getproperty.md) | The AddFile method adds a single file to an existing DO job. |
| [**SetProperty**](ideliveryoptimizationjob2-setproperty.md) | This method is unused.                                       |

## Requirements

| Requirement | Value |
|--------------------------|----------------------------------------------------------------------------------|
| Minimum supported client | Windows 10, version 1803 \[desktop apps only\]                                   |
| Minimum supported server | Windows Server, version 1709 \[desktop apps only\]                               |
| Header                   | Deliveryoptimization.h                                                           |
| IDL                      | DeliveryOptimization.idl                                                         |
| Library                  | Dosvc.lib                                                                        |
| DLL                      | Dosvc.dll                                                                        |
| IID                      | IID_IDeliveryOptimizationJob2 is defined as 18995A26-BF59-4ABE-9F8B-D5092D5A2405 |
