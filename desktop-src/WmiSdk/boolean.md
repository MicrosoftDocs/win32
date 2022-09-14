---
title: boolean (WMI)
description: Is a VT\_BOOL parameter that takes on the value of VARIANT\_TRUE (&\#8211;1) or VARIANT\_FALSE (0).
ms.assetid: 3928ff39-ed17-4a61-bb72-a3c9be16ae45
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# boolean (WMI)

The boolean data type is a VT\_BOOL parameter that takes on the value of VARIANT\_TRUE (–1) or VARIANT\_FALSE (0). The following table lists the difference between the programmatic representations of logical **TRUE** in C/C++ and the Automation type.

| Language   | Value         | Numerical value |
|------------|---------------|-----------------|
| C/C++      | **TRUE**      | 1               |
| Automation | VARIANT\_TRUE | –1              |

Both types are nonzero and therefore not **FALSE**, but have different representations for **TRUE**.
