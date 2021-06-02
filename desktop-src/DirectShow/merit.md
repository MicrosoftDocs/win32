---
description: Merit values define the order in which the Filter Graph Manager tries to add filters during graph building.
ms.assetid: 9e026675-e0a9-4c82-9b57-ab0e7d9592ea
title: Merit (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Merit

Merit values define the order in which the Filter Graph Manager tries to add filters during graph building.

<dl> <span id="MERIT_PREFERRED"></span><span id="merit_preferred"></span>**MERIT\_PREFERRED** (0x800000)  
<span id="MERIT_NORMAL"></span><span id="merit_normal"></span>**MERIT\_NORMAL** (0x600000)  
<span id="MERIT_UNLIKELY"></span><span id="merit_unlikely"></span>**MERIT\_UNLIKELY** (0x400000)  
<span id="MERIT_DO_NOT_USE"></span><span id="merit_do_not_use"></span>**MERIT\_DO\_NOT\_USE** (0x200000)  
<span id="MERIT_SW_COMPRESSOR"></span><span id="merit_sw_compressor"></span>**MERIT\_SW\_COMPRESSOR** (0x100000)  
<span id="MERIT_HW_COMPRESSOR"></span><span id="merit_hw_compressor"></span>**MERIT\_HW\_COMPRESSOR** (0x100050)  
</dl>

## Remarks

Each filter is registered with a merit value. When the filter graph manager builds a graph, it enumerates all the filters registered with the correct media type. Then it tries them in order of merit, from highest to lowest. (It uses additional criteria to choose between filters with equal merit.) It never tries filters with a merit value less than or equal to **MERIT\_DO\_NOT\_USE**.

A filter that should never be considered for ordinary playback should have a merit of **MERIT\_DO\_NOT\_USE** or less. Filters can be registered with intermediate values not defined by this enumeration, such as **MERIT\_NORMAL** + 1.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Constants and GUIDs](constants-and-guids.md)
</dt> <dt>

[Guidelines for Registering Filters](guidelines-for-registering-filters.md)
</dt> <dt>

[Intelligent Connect](intelligent-connect.md)
</dt> </dl>

 

 




