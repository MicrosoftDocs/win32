---
title: Window Messages
description: .
ms.assetid: 90c20456-44ed-4f0f-a6d3-b6c5660f0bc7
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Window Messages

A GUI application must respond to events from the user and from the operating system.

-   **Events from the user** include all the ways that someone can interact with your program: mouse clicks, key strokes, touch-screen gestures, and so on.
-   **Events from the operating system** include anything "outside" of the program that can affect how the program behaves. For example, the user might plug in a new hardware device, or Windows might enter a lower-power state (sleep or hibernate).

These events can occur at any time while the program is running, in almost any order. How do you structure a program whose flow of execution cannot be predicted in advance?

To solve this problem, Windows uses a message-passing model. The operating system communicates with your application window by passing messages to it. A message is simply a numeric code that designates a particular event. For example, if the user presses the left mouse button, the window receives a message that has the following message code.


```C++
#define WM_LBUTTONDOWN    0x0201
```



Some messages have data associated with them. For example, the [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607) message includes the x-coordinate and y-coordinate of the mouse cursor.

To pass a message to a window, the operating system calls the window procedure registered for that window. (And now you know what the window procedure is for.)

## The Message Loop

An application will receive thousands of messages while it runs. (Consider that every keystroke and mouse-button click generates a message.) Additionally, an application can have several windows, each with its own window procedure. How does the program receive all these messages and deliver them to the correct window procedure? The application needs a loop to retrieve the messages and dispatch them to the correct windows.

For each thread that creates a window, the operating system creates a queue for window messages. This queue holds messages for all the windows that are created on that thread. The queue itself is hidden from your program. You cannot manipulate the queue directly. However, you can pull a message from the queue by calling the [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) function.


```C++
MSG msg;
GetMessage(&amp;msg, NULL, 0, 0);
```



This function removes the first message from the head of the queue. If the queue is empty, the function blocks until another message is queued. The fact that [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) blocks will not make your program unresponsive. If there are no messages, there is nothing for the program to do. If you have to perform background processing, you can create additional threads that continue to run while **GetMessage** waits for another message. (See [Avoiding Bottlenecks in Your Window Procedure](writing-the-window-procedure.md).)

The first parameter of [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) is the address of a [**MSG**](https://msdn.microsoft.com/library/windows/desktop/ms644958) structure. If the function succeeds, it fills in the **MSG** structure with information about the message. This includes the target window and the message code. The other three parameters let you filter which messages you get from the queue. In almost all cases, you will set these parameters to zero.

Although the [**MSG**](https://msdn.microsoft.com/library/windows/desktop/ms644958) structure contains information about the message, you will almost never examine this structure directly. Instead, you will pass it directly to two other functions.


```C++
TranslateMessage(&amp;msg); 
DispatchMessage(&amp;msg);
```



The [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) function is related to keyboard input. It translates keystrokes (key down, key up) into characters. You do not really have to know how this function works; just remember to call it before [**DispatchMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644934). The link to the MSDN documentation will give you more information, if you are curious.

The [**DispatchMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644934) function tells the operating system to call the window procedure of the window that is the target of the message. In other words, the operating system looks up the window handle in its table of windows, finds the function pointer associated with the window, and invokes the function.

For example, suppose that the user presses the left mouse button. This causes a chain of events:

1.  The operating system puts a [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607) message on the message queue.
2.  Your program calls the [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) function.
3.  [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) pulls the [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607) message from the queue and fills in the [**MSG**](https://msdn.microsoft.com/library/windows/desktop/ms644958) structure.
4.  Your program calls the [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) and [**DispatchMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644934) functions.
5.  Inside [**DispatchMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644934), the operating system calls your window procedure.
6.  Your window procedure can either respond to the message or ignore it.

When the window procedure returns, it returns back to [**DispatchMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644934). This returns to the message loop for the next message. As long as your program is running, messages will continue to arrive on the queue. Therefore, you must have a loop that continually pulls messages from the queue and dispatches them. You can think of the loop as doing the following:


```C++
// WARNING: Don't actually write your loop this way.

while (1)      
{
    GetMessage(&amp;msg, NULL, 0,  0);
    TranslateMessage(&amp;msg); 
    DispatchMessage(&amp;msg);
}
```



As written, of course, this loop would never end. That is where the return value for the [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) function comes in. Normally, **GetMessage** returns a nonzero value. When you want to exit the application and break out of the message loop, call the [**PostQuitMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644945) function.


```C++
        PostQuitMessage(0);
```



The [**PostQuitMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644945) function puts a [**WM\_QUIT**](https://msdn.microsoft.com/library/windows/desktop/ms632641) message on the message queue. **WM\_QUIT** is a special message: It causes [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) to return zero, signaling the end of the message loop. Here is the revised message loop.

``` syntax
// Correct.

MSG msg = { };
while (GetMessage(&msg, NULL, 0, 0))
{
    TranslateMessage(&msg);
    DispatchMessage(&msg);
}
```

As long as [**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) returns a nonzero value, the expression in the **while** loop evaluates to true. After you call [**PostQuitMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644945), the expression becomes false and the program breaks out of the loop. (One interesting result of this behavior is that your window procedure never receives a [**WM\_QUIT**](https://msdn.microsoft.com/library/windows/desktop/ms632641) message. Therefore, you do not have to have a case statement for this message in your window procedure.)

The next obvious question is when to call [**PostQuitMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644945). We'll return to this question in the topic [Closing the Window](closing-the-window.md), but first we have to write our window procedure.

## Posted Messages versus Sent Messages

The previous section talked about messages going onto a queue. Sometimes, the operating system will call a window procedure directly, bypassing the queue.

The terminology for this distinction can be confusing:

-   *Posting* a message means the message goes on the message queue, and is dispatched through the message loop ([**GetMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644936) and [**DispatchMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644934)).
-   *Sending* a message means the message skips the queue, and the operating system calls the window procedure directly.

For now, the difference is not very important. The window procedure handles all messages. However, some messages bypass the queue and go directly to your window procedure. However, it can make a difference if your application communicates between windows. You can find a more thorough discussion of this issue in the topic [About Messages and Message Queues](https://msdn.microsoft.com/library/windows/desktop/ms644927).

## Next

[Writing the Window Procedure](writing-the-window-procedure.md)

 

 




