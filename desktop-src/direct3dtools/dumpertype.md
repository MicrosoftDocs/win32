---
description: An enum used to indicate what type of buffer IGenericBufferDataRequest returns.
MS-HAID: vspixengine.DUMPERTYPE
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: DUMPERTYPE enumeration
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 3F0E7F11-A11E-4843-AAE6-659BD602CB31
api_name: 
 - DUMPERTYPE
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.dumpertype"></span>DUMPERTYPE enumeration

An enum used to indicate what type of buffer IGenericBufferDataRequest returns.

## Syntax


```C++
};
```

## Constants

<span id="DT_HTML"></span><span id="dt_html"></span>**DT\_HTML**  
Not used.

<span id="DT_XML"></span><span id="dt_xml"></span>**DT\_XML**  
A value that corresponds to unfiltered XML.

<span id="DT_XML_PROCESSED"></span><span id="dt_xml_processed"></span>**DT\_XML\_PROCESSED**  
A value that corresponds to processed XML; processing filters out information that's not relevent.

<span id="DT_XML_ALL_TILES"></span><span id="dt_xml_all_tiles"></span>**DT\_XML\_ALL\_TILES**  
A value that corresponds to XML for data visualizer windows.

<span id="DT_XML_DETAILED_TREES"></span><span id="dt_xml_detailed_trees"></span>**DT\_XML\_DETAILED\_TREES**  
A value that corresponds to XML for the state window.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



