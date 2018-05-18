---
title: Structures
description: The topics in this section provide the reference specifications for Pointer Input Messages and Notifications structures.
ms.assetid: '2224DCD0-DAE1-4AC2-AB36-23D114801138'
---

# Structures

The topics in this section provide the reference specifications for [Pointer Input Messages and Notifications](messages-and-notifications.md) structures.

## In this section



| Topic                                                                            | Description                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**INPUT\_TRANSFORM**](input-transform.md)<br/>                           | Defines the matrix that represents a transform on a message consumer. This matrix can be used to transform pointer input data from client coordinates to screen coordinates, while the inverse can be used to transform pointer input data from screen coordinates to client coordinates. <br/>                                                                 |
| [**POINTER\_INFO**](pointer-info-struct.md)<br/>                          | Contains basic pointer information common to all pointer types. Applications can retrieve this information using the [**GetPointerInfo**](getpointerinfo.md), [**GetPointerFrameInfo**](getpointerframeinfo.md), [**GetPointerInfoHistory**](getpointerinfohistory.md) and [**GetPointerFrameInfoHistory**](getpointerframeinfohistory.md) functions. <br/> |
| [**POINTER\_PEN\_INFO**](pointer-pen-info-struct.md)<br/>                 | Defines basic pen information common to all pointer types. <br/>                                                                                                                                                                                                                                                                                                |
| [**POINTER\_TOUCH\_INFO**](pointer-touch-info-struct.md)<br/>             | Defines basic touch information common to all pointer types.<br/>                                                                                                                                                                                                                                                                                               |
| [**TOUCHPREDICTIONPARAMETERS**](touchpredictionparameters-struct.md)<br/> | Contains hardware input details that can be used to predict touch targets and help compensate for hardware latency when processing touch and gesture input that contains distance and velocity data.<br/>                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[Pointer Input Message Reference](wmpointer-reference.md)
</dt> </dl>

 

 





