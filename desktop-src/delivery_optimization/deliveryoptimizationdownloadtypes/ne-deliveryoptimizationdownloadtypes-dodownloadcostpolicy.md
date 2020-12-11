---
title: DODownloadCostPolicy enumeration
description: Specifies the ID of cost policies options associated with the **DODownloadProperty_CostPolicy** property.
keywords:
- DODownloadCostPolicy enumeration, DODownloadCostPolicy
topic_type:
- apiref
api_name:
- DODownloadCostPolicy
api_location:
- deliveryoptimizationdownloadtypes.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 07/02/2019
---

# DODownloadCostPolicy enumeration

The **DODownloadCostPolicy** enumeration specifies the ID of cost policies options associated with the **DODownloadProperty_CostPolicy** property.

## Syntax

```cpp
typedef enum _DODownloadCostPolicy
{
  DODownloadCostPolicy_Always = 0,
  DODownloadCostPolicy_Unrestricted,
  DODownloadCostPolicy_Standard,    
  DODownloadCostPolicy_NoRoaming,   
  DODownloadCostPolicy_NoSurcharge, 
  DODownloadCostPolicy_NoCellular
} DODownloadCostPolicy;
```

## Constants

| Requirement | Value |
|-|-|
| DODownloadCostPolicy_Always | Download runs regardless of the cost. |
| DODownloadCostPolicy_Unrestricted | Download runs unless imposes costs or traffic limits. |
| DODownloadCostPolicy_Standard | Download runs unless neither subject to a surcharge nor near exhaustion. |
| DODownloadCostPolicy_NoRoaming | Download runs unless that connectivity is subject to roaming surcharges. |
| DODownloadCostPolicy_NoSurcharge | Download runs unless subject to a surcharge. |
| DODownloadCostPolicy_NoCellular | Download runs unless network is on cellular. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1809 \[Win32 applications only\] |
| **Minimum supported server** | Windows Server, version 1809 \[Win32 applications only\] |
| **Header** | DeliveryOptimizationDownloadTypes.h |
