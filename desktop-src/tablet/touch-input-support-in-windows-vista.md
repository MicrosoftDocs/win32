---
description: Starting with Windows Vista, Tablet PC Technology has support for touch input on Tablet PC's with touch capable digitizers. This support includes an enhanced user interface to aid in targeting and commanding Windows when using a finger for input.
ms.assetid: 63f1d71f-03d8-4d83-a174-e3dc7c57bad0
title: Touch Input Support in Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# Touch Input Support in Windows Vista

Starting with Windows Vista, Tablet PC Technology has support for touch input on Tablet PC's with touch capable digitizers. This support includes an enhanced user interface to aid in targeting and commanding Windows when using a finger for input.

## Touch Digitizer Support

### Pen and Touch Input Not Exclusive

Do not assume pen and touch input are mutually exclusive in [**InkCollector**](inkcollector-class.md), [**InkOverlay**](inkoverlay-class.md), and [**RealTimeStylus**](realtimestylus-class.md) applications.

In Windows Vista, when the system recognizes a pen it ignores touch input. That is, the touch stroke ends and the pen stroke begins. Because this could possibly change in the future, your code should not assume pen and touch input are mutually exclusive.

### Other Mouse Message Sources

There are other sources of mouse messages even when the user is only interacting using finger or pen. Sources include touchpads, as well as movement intended to let an application behind a layered window be aware that the mouse is moving above the application.

### Enabling and Disabling the Touch Input User Interface

You may wish to enable or disable the touch input user interface depending on the requirements of your application. To accomplish this, intercept operating system window messages in a window procedure and modify the Windows message. Override [WndProc](/dotnet/api/system.windows.forms.control.wndproc?view=netcore-3.1&preserve-view=true) in your application to intercept these messages. The following C\# pseudo-code shows how to enable and disable the touch input user interface. The code also shows using the same technique to disable the press-and-hold gesture. This method also works for disabling the stylus.


```C++
const int WM_TABLET_QUERY_SYSTEM_GESTURE_STATUS = 716;

const uint SYSTEM_GESTURE_STATUS_NOHOLD           = 0x00000001;
const uint SYSTEM_GESTURE_STATUS_TOUCHUI_FORCEON  = 0x00000100;
const uint SYSTEM_GESTURE_STATUS_TOUCHUI_FORCEOFF = 0x00000200;

protected override void WndProc(ref Message msg)
{
    switch (msg.Msg)
    {
        case WM_TABLET_QUERY_SYSTEM_GESTURE_STATUS:
        {
            uint result = 0;
            if (...)
            {
                result |= SYSTEM_GESTURE_STATUS_NOHOLD;
            }

            if (...)
            {
                result |= SYSTEM_GESTURE_STATUS_TOUCHUI_FORCEON;
            }

            if (...)
            {
                result |= SYSTEM_GESTURE_STATUS_TOUCHUI_FORCEOFF;
            }

            msg.Result = (IntPtr)result;
        }
        break;

        default:
            base.WndProc(ref msg);
            break;
    }
}
```



## Related topics

<dl> <dt>

[Windows Touch](../wintouch/windows-touch-portal.md)
</dt> </dl>

 

 
