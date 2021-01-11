---
description: This section lists issues that can be encountered when working with Direct3D 9 on drivers written for versions of Direct3D earlier than Direct3D 9.
ms.assetid: 891198e8-6c45-4f03-99bb-e24a4082b0d8
title: Working with Earlier Drivers (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Working with Earlier Drivers (Direct3D 9)

This section lists issues that can be encountered when working with Direct3D 9 on drivers written for versions of Direct3D earlier than Direct3D 9.

-   When working with a T&L HAL device, the fog intensity is computed but the absolute value operation is not applied to this value. Rather, the value is left negative if that is what is computed. The best way to avoid this situation is to set up transforms appropriately. A less-preferred method is to make the fog-start and fog-end values negative to match.

To check for a Direct3D 9 driver, look for a nonzero value for D3DDEVCAPS2\_STREAMOFFSET in the DevCaps2 member of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9).

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 



