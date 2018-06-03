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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IDeliveryOptimizationFile interface

Implement the **IDeliveryOptimizationFile** interface to identify the status of a specific file.

## Members

The **IDeliveryOptimizationFile** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IDeliveryOptimizationFile** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDeliveryOptimizationFile** interface has these methods.



| Method                                                 | Description                                                       |
|:-------------------------------------------------------|:------------------------------------------------------------------|
| [**GetStats**](ideliveryoptimizationfile-getstats.md) | Returns download and upload stats for a specific file.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID\_IDeliveryOptimizationFile is defined as B76B9699-E99E-4101-803F-A20E325D93E2<br/>        |



 

 





