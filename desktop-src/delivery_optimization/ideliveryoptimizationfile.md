---
title: IDeliveryOptimizationFile interface
description: Implement the IDeliveryOptimizationFile interface to identify the status of a specific file.
ms.assetid: 4D1D82E1-B39C-4634-A0B7-BC4322796AB2
keywords:
- IDeliveryOptimizationFile interface
- IDeliveryOptimizationFile interface, described
topic_type:
- apiref
api_name:
- IDeliveryOptimizationFile
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IDeliveryOptimizationFile interface

Implement the **IDeliveryOptimizationFile** interface to identify the status of a specific file.

## Members

The **IDeliveryOptimizationFile** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IDeliveryOptimizationFile** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDeliveryOptimizationFile** interface has these methods.



| Method                                                 | Description                                                       |
|:-------------------------------------------------------|:------------------------------------------------------------------|
| [**GetStats**](ideliveryoptimizationfile-getstats.md) | Returns download and upload stats for a specific file.<br/> |

## Requirements

| Requirement | Value |
|-------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client      | Windows 10, version 1709 \[desktop apps only\]                                   |
| Minimum supported server      | Windows Server, version 1709 \[desktop apps only\]                               |
| Header                        | Deliveryoptimization.h                                                           |
| IDL                           | DeliveryOptimization.idl                                                         |
| Library                       | Dosvc.lib                                                                        |
| DLL                           | Dosvc.dll                                                                        |
| IID                           | IID_IDeliveryOptimizationFile is defined as B76B9699-E99E-4101-803F-A20E325D93E2 |
