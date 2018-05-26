---
Description: This section describes the recognizer structures.
ms.assetid: 4c17391f-7af4-42ab-b77f-e3c39cadc0b6
title: Recognizer Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Recognizer Structures

This section describes the recognizer structures.

## In This Section



| Structure                                                    | Description                                                                                                                                                   |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CHARACTER\_RANGE**](/windows/win32/rectypes/ns-rectypes-tagcharacter_range?branch=master)                  | Specifies a range of Unicode points (characters).<br/>                                                                                                  |
| [**LATTICE\_METRICS**](/windows/win32/rectypes/ns-rectypes-taglattice_metrics?branch=master)                  | Describes the baseline and the midline height.<br/>                                                                                                     |
| [**LINE\_SEGMENT**](/windows/win32/rectypes/ns-rectypes-tagline_segment?branch=master)                        | Describes the start and end points of a line recognition segment, such as the baseline or midline.<br/>                                                 |
| [**PACKET\_DESCRIPTION**](/windows/win32/tpcshrd/ns-tpcshrd-_packet_description?branch=master)            | Describes the content of the packet for a particular tablet context.<br/>                                                                               |
| [**PACKET\_PROPERTY**](/windows/win32/tpcshrd/ns-tpcshrd-_packet_property?branch=master)                  | Describes a packet property that is reported by the tablet driver.<br/>                                                                                 |
| [**PROPERTY\_METRICS**](/windows/win32/tpcshrd/ns-tpcshrd-_property_metrics?branch=master)                | Defines the range and resolution of a packet property.<br/>                                                                                             |
| [**RECO\_ATTRS**](/windows/win32/rectypes/ns-rectypes-tagreco_attrs?branch=master)                            | Retrieves the attributes of a recognizer or specifies which attributes to use when you search for an installed recognizer.<br/>                         |
| [**RECO\_GUIDE**](/windows/win32/rectypes/ns-rectypes-tagreco_guide?branch=master)                            | Defines the boundaries of the ink to the recognizer.<br/>                                                                                               |
| [**RECO\_LATTICE**](/windows/win32/rectypes/ns-rectypes-tagreco_lattice?branch=master)                        | Serves as the entry point into a lattice.<br/>                                                                                                          |
| [**RECO\_LATTICE\_COLUMN**](/windows/win32/rectypes/ns-rectypes-tagreco_lattice_column?branch=master)         | Represents a column in the lattice.<br/>                                                                                                                |
| [**RECO\_LATTICE\_ELEMENT**](/windows/win32/rectypes/ns-rectypes-tagreco_lattice_element?branch=master)       | Corresponds to one word or one East Asian character, typically; however, an element may also correspond to a gesture, a shape, or some other code.<br/> |
| [**RECO\_LATTICE\_PROPERTIES**](/windows/win32/rectypes/ns-rectypes-tagreco_lattice_properties?branch=master) | Contains an array of pointers to property structures.<br/>                                                                                              |
| [**RECO\_LATTICE\_PROPERTY**](/windows/win32/rectypes/ns-rectypes-tagreco_lattice_property?branch=master)     | Contains a property used in the lattice.<br/>                                                                                                           |
| [**RECO\_RANGE**](/windows/win32/rectypes/ns-rectypes-tagreco_range?branch=master)                            | Identifies a range of characters in the result string.<br/>                                                                                             |
| [**STROKE\_RANGE**](/windows/win32/tpcshrd/ns-tpcshrd-tagstroke_range?branch=master)                        | Specifies a range of strokes in the [**InkDisp**](/windows/win32/msinkaut/?branch=master) object.<br/>                                                                       |



 

 

 




