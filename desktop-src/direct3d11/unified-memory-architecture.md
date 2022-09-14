---
title: Unified Memory Architecture
description: Querying for whether Unified Memory Architecture (UMA) is supported can help determine how to handle some resources.
ms.assetid: E43892F9-E7CD-4D18-BDDE-3C4F03F8F4EA
ms.topic: article
ms.date: 05/31/2018
---

# Unified Memory Architecture

Querying for whether Unified Memory Architecture (UMA) is supported can help determine how to handle some resources.

A boolean, set by the driver, can be read from the [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS2**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options2) structure to determine if the hardware supports UMA.

Applications running on UMA may want to have more resources with CPU access enabled than if it is not available. UMA enables applications to avoiding copying resource data around, instead of staying efficient solely for non-UMA graphics adapters. [Direct3D 11.3 Features](direct3d-11-3-features.md)

## Related topics

<dl> <dt>

[Direct3D 11.3 Features](direct3d-11-3-features.md)
</dt> </dl>

 

 




