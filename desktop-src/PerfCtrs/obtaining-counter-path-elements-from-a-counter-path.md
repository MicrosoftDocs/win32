---
Description: 'To retrieve the elements of a path, call the PdhParseCounterPath function. The function parses the elements of a counter path and returns them in a PDH\_COUNTER\_PATH\_ELEMENTS structure.'
ms.assetid: '65c722f9-6f9d-4e3d-abf3-867cf260ef9f'
title: Obtaining Counter Path Elements from a Counter Path
---

# Obtaining Counter Path Elements from a Counter Path

To retrieve the elements of a path, call the [**PdhParseCounterPath**](pdhparsecounterpath.md) function. The function parses the elements of a counter path and returns them in a [**PDH\_COUNTER\_PATH\_ELEMENTS**](pdh-counter-path-elements-str.md) structure.

If you have a complex instance name (one that contains a parent instance and instance index), you can call the [**PdhParseInstanceName**](pdhparseinstancename.md) function to extract the instance name, instance index, and parent name.

 

 



