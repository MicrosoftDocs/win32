---
title: WM_GESTURE message (Winuser.h)
description: Passes information about a gesture.
ms.assetid: 4167aeb0-2c31-4b7b-ad1b-e6d37da09ef8
keywords:
- WM_GESTURE message Windows Touch
topic_type:
- apiref
api_name:
- WM_GESTURE
api_location:
- winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GESTURE message

Passes information about a gesture.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Provides information identifying the gesture command and gesture-specific argument values. This information is the same information passed in the **ullArguments** member of the [**GESTUREINFO**](/windows/win32/api/winuser/ns-winuser-gestureinfo) structure.

</dd> <dt>

*lParam* 
</dt> <dd>

Provides a handle to information identifying the gesture command and gesture-specific argument values. This information is retrieved by calling [**GetGestureInfo**](/windows/desktop/api/winuser/nf-winuser-getgestureinfo).

</dd> </dl>

## Return value

If an application processes this message, it should return 0.

If the application does not process the message, it must call [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca). Not doing so will cause the application to leak memory because the touch input handle will not be closed and associated process memory will not be freed.

## Remarks

The following table lists the supported gesture commands.



| Gesture ID            | Value (*dwID*) | Description                                                                                                                                                                                                                                                                          |
|-----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **GID\_BEGIN**        | 1              | Indicates a generic gesture is beginning.                                                                                                                                                                                                                                            |
| **GID\_END**          | 2              | Indicates a generic gesture end.                                                                                                                                                                                                                                                     |
| **GID\_ZOOM**         | 3              | Indicates zoom start, zoom move, or zoom stop. The first **GID\_ZOOM** command message begins a zoom but does not cause any zooming. The second **GID\_ZOOM** command triggers a zoom relative to the state contained in the first **GID\_ZOOM**.                                    |
| **GID\_PAN**          | 4              | Indicates pan move or pan start. The first **GID\_PAN** command indicates a pan start but does not perform any panning. With the second **GID\_PAN** command message, the application will begin panning.                                                                            |
| **GID\_ROTATE**       | 5              | Indicates rotate move or rotate start. The first **GID\_ROTATE** command message indicates a rotate move or rotate start but will not rotate. The second **GID\_ROTATE** command message will trigger a rotation operation relative to state contained in the first **GID\_ROTATE**. |
| **GID\_TWOFINGERTAP** | 6              | Indicates two-finger tap gesture.                                                                                                                                                                                                                                                    |
| **GID\_PRESSANDTAP**  | 7              | Indicates the press and tap gesture.                                                                                                                                                                                                                                                 |



 

> [!Note]  
> In order to enable legacy support, messages with the **GID\_BEGIN** and **GID\_END** gesture commands need to be forwarded using [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca).

 

The following table indicates the gesture arguments passed in the *lParam* and *wParam* parameters.



| Gesture ID            | Gesture        | *ullArgument*                                                                                                                                                                                                                                                                                                                                                                                            | *ptsLocation* in [**GestureInfo**](/windows/desktop/api/winuser/nf-winuser-getgestureinfo) structure                                                  |
|-----------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **GID\_ZOOM**         | Zoom In/Out    | Indicates the distance between the two points.                                                                                                                                                                                                                                                                                                                                                           | Indicates the center of the zoom.                                                                                 |
| **GID\_PAN**          | Pan            | Indicates the distance between the two points.                                                                                                                                                                                                                                                                                                                                                           | Indicates the current position of the pan.                                                                        |
| **GID\_ROTATE**       | Rotate (pivot) | Indicates the angle of rotation if the **GF\_BEGIN** flag is set. Otherwise, this is the angle change since the rotation has started. This is signed to indicate the direction of the rotation. Use the [**GID\_ROTATE\_ANGLE\_FROM\_ARGUMENT**](/windows/desktop/api/winuser/nf-winuser-gid_rotate_angle_from_argument) and [**GID\_ROTATE\_ANGLE\_TO\_ARGUMENT**](/windows/desktop/api/winuser/nf-winuser-gid_rotate_angle_to_argument) macros to get and set the angle value. | This indicates the center of the rotation which is the stationary point that the target object is rotated around. |
| **GID\_TWOFINGERTAP** | Two-finger Tap | Indicates the distance between the two fingers.                                                                                                                                                                                                                                                                                                                                                          | Indicates the center of the two fingers.                                                                          |
| **GID\_PRESSANDTAP**  | Press and Tap  | Indicates the delta between the first finger and the second finger. This value is stored in the lower 32 bits of the *ullArgument* in a **POINT** structure.                                                                                                                                                                                                                                             | Indicates the position that the first finger comes down on.                                                       |



 

> [!Note]  
> All distances and positions are provided in physical screen coordinates.

 

> [!Note]  
> The *dwID* and *ullArgument* parameters should only be considered to be accompanying the GID\_\* commands and should not be altered by applications.

 

## Examples

The following code illustrates how to obtain gesture-specific information associated with this message.

> [!Note]  
> You should always forward unhandled messages to [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca) and should close the gesture input handle for messages that you do handle with a call to [**CloseGestureInfoHandle**](/windows/desktop/api/winuser/nf-winuser-closegestureinfohandle). In this example, the default gesture handler behavior will be suppressed because the TOUCHINPUT handle is closed in each of the gesture cases. If you removed the cases in the above code for unhandled messages, the default gesture handler would process the messages by getting forwarded to [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca) in the default case.

 


```C++
  LRESULT DecodeGesture(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam){
    // Create a structure to populate and retrieve the extra message info.
    GESTUREINFO gi;  
    
    ZeroMemory(&gi, sizeof(GESTUREINFO));
    
    gi.cbSize = sizeof(GESTUREINFO);

    BOOL bResult  = GetGestureInfo((HGESTUREINFO)lParam, &gi);
    BOOL bHandled = FALSE;

    if (bResult){
        // now interpret the gesture
        switch (gi.dwID){
           case GID_ZOOM:
               // Code for zooming goes here     
               bHandled = TRUE;
               break;
           case GID_PAN:
               // Code for panning goes here
               bHandled = TRUE;
               break;
           case GID_ROTATE:
               // Code for rotation goes here
               bHandled = TRUE;
               break;
           case GID_TWOFINGERTAP:
               // Code for two-finger tap goes here
               bHandled = TRUE;
               break;
           case GID_PRESSANDTAP:
               // Code for roll over goes here
               bHandled = TRUE;
               break;
           default:
               // A gesture was not recognized
               break;
        }
    }else{
        DWORD dwErr = GetLastError();
        if (dwErr > 0){
            //MessageBoxW(hWnd, L"Error!", L"Could not retrieve a GESTUREINFO structure.", MB_OK);
        }
    }
    if (bHandled){
        return 0;
    }else{
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
  }
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Notifications](notifications.md)
</dt> <dt>

[Windows Touch Gestures Programming Guide](guide-multi-touch-gestures.md)
</dt> </dl>

 

