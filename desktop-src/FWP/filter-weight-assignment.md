---
title: Filter Weight Assignment
description: Every filter in the Windows Filtering Platform (WFP) has an associated weight, which is used during filter arbitration.
ms.assetid: c78854c2-9aa1-408f-82d6-4b9e52f38e84
ms.topic: article
ms.date: 05/31/2018
---

# Filter Weight Assignment

Every filter in the Windows Filtering Platform (WFP) has an associated weight, which is used during [filter arbitration](filter-arbitration.md).

The filter weight used by the Base Filtering Engine (BFE) is of type [**FWP\_UINT64**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_data_type). Callers have three options when adding filters.

-   Set the weight to an [**FWP\_UINT64**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_data_type). BFE uses the supplied weight as is.
-   Set the weight to [**FWP\_EMPTY**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_data_type). BFE automatically generates a weight in the range \[0, 2⁶⁰).
-   Set the weight to an [**FWP\_UINT8**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_data_type) in the range \[0, 15\]. BFE uses the supplied weight as a weight range identifier.

    BFE automatically generates the low-order 60 bits (exactly as if the weight had been set to [**FWP\_EMPTY**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_data_type)), and then uses the supplied value to set the 4 high-order bits. This allows callers to manually divide the weight space into 16 ranges, while still using automatic weighting within a range.

> [!Note]  
> When two or more callouts are registered at the same sublayer, problems may occur when the same weight is assigned to the filters. This issue can be prevented by having callouts create their own sublayer by using [**FwpmSubLayerAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmsublayeradd0).

 

## Related topics

<dl> <dt>

[**Filter Weight Identifiers**](filter-weight-identifiers.md)
</dt> </dl>

 

 




