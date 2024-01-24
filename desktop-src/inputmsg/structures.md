---
title: Structures (Pointer Input Messages and Notifications)
description: The topics in this section provide the reference specifications for Pointer Input Messages and Notifications structures.
ms.assetid: 2224DCD0-DAE1-4AC2-AB36-23D114801138
ms.topic: article
ms.date: 02/03/2020
---

# Pointer Input Messages and Notifications structures

The topics in this section provide the reference specifications for [Pointer Input Messages and Notifications](messages-and-notifications-portal.md) structures.

## In this section



| Topic                                                                            | Description                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**INPUT_TRANSFORM**](/windows/win32/api/winuser/ns-winuser-input_transform)<br/>                           | Defines the matrix that represents a transform on a message consumer. This matrix can be used to transform pointer input data from client coordinates to screen coordinates, while the inverse can be used to transform pointer input data from screen coordinates to client coordinates. <br/>                                                                 |
| [**POINTER_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_info)<br/>                          | Contains basic pointer information common to all pointer types. Applications can retrieve this information using the [**GetPointerInfo**](/windows/win32/api/winuser/ns-winuser-pointer_info), [**GetPointerFrameInfo**](/windows/win32/api/winuser/ns-winuser-pointer_info), [**GetPointerInfoHistory**](/windows/win32/api/winuser/ns-winuser-pointer_info) and [**GetPointerFrameInfoHistory**](/windows/win32/api/winuser/ns-winuser-pointer_info) functions. <br/> |
| [**POINTER_PEN_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_pen_info)<br/>                 | Defines basic pen information common to all pointer types. <br/>                                                                                                                                                                                                                                                                                                |
| [**POINTER_TOUCH_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_touch_info)<br/>             | Defines basic touch information common to all pointer types.<br/>                                                                                                                                                                                                                                                                                               |
| [**POINTER_TYPE_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_type_info)<br/>             | Defines basic touch information common to all pointer types.<br/>                                                                                                                                                                                                                                                                                               |
| [**TOUCHPREDICTIONPARAMETERS**](/windows/win32/api/winuser/ns-winuser-touchpredictionparameters)<br/> | Contains hardware input details that can be used to predict touch targets and help compensate for hardware latency when processing touch and gesture input that contains distance and velocity data.<br/>                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[Pointer Input Message Reference](wmpointer-reference.md)
</dt> </dl>

 

 





