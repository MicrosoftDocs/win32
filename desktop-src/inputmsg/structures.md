---
title: Structures
description: The topics in this section provide the reference specifications for Pointer Input Messages and Notifications structures.
ms.assetid: 2224DCD0-DAE1-4AC2-AB36-23D114801138
ms.topic: article
ms.date: 05/31/2018
---

# Structures

The topics in this section provide the reference specifications for [Pointer Input Messages and Notifications](messages-and-notifications-portal.md) structures.

## In this section



| Topic                                                                            | Description                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**INPUT\_TRANSFORM**](/previous-versions/windows/desktop/api)<br/>                           | Defines the matrix that represents a transform on a message consumer. This matrix can be used to transform pointer input data from client coordinates to screen coordinates, while the inverse can be used to transform pointer input data from screen coordinates to client coordinates. <br/>                                                                 |
| [**POINTER\_INFO**](/previous-versions/windows/desktop/api)<br/>                          | Contains basic pointer information common to all pointer types. Applications can retrieve this information using the [**GetPointerInfo**](/previous-versions/windows/desktop/api), [**GetPointerFrameInfo**](/previous-versions/windows/desktop/api), [**GetPointerInfoHistory**](/previous-versions/windows/desktop/api) and [**GetPointerFrameInfoHistory**](/previous-versions/windows/desktop/api) functions. <br/> |
| [**POINTER\_PEN\_INFO**](/previous-versions/windows/desktop/api)<br/>                 | Defines basic pen information common to all pointer types. <br/>                                                                                                                                                                                                                                                                                                |
| [**POINTER\_TOUCH\_INFO**](/previous-versions/windows/desktop/api)<br/>             | Defines basic touch information common to all pointer types.<br/>                                                                                                                                                                                                                                                                                               |
| [**TOUCHPREDICTIONPARAMETERS**](/previous-versions/windows/desktop/api)<br/> | Contains hardware input details that can be used to predict touch targets and help compensate for hardware latency when processing touch and gesture input that contains distance and velocity data.<br/>                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[Pointer Input Message Reference](wmpointer-reference.md)
</dt> </dl>

 

 





