---
description: To retrieve the elements of a path, call the PdhParseCounterPath function. The function parses the elements of a counter path and returns them in a PDH\_COUNTER\_PATH\_ELEMENTS structure.
ms.assetid: 65c722f9-6f9d-4e3d-abf3-867cf260ef9f
title: Obtaining Counter Path Elements from a Counter Path
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Counter Path Elements from a Counter Path

To retrieve the elements of a path, call the [**PdhParseCounterPath**](/windows/desktop/api/Pdh/nf-pdh-pdhparsecounterpatha) function. The function parses the elements of a counter path and returns them in a [**PDH\_COUNTER\_PATH\_ELEMENTS**](/windows/desktop/api/Pdh/ns-pdh-pdh_counter_path_elements_a) structure.

If you have a complex instance name (one that contains a parent instance and instance index), you can call the [**PdhParseInstanceName**](/windows/desktop/api/Pdh/nf-pdh-pdhparseinstancenamea) function to extract the instance name, instance index, and parent name.

 

 



