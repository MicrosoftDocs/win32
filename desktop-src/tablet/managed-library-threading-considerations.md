---
Description: The following Tablet PC threading considerations are specific to the Managed Library.
ms.assetid: bcc398d3-22ea-466c-9206-92b0ac208def
title: Managed Library Threading Considerations
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managed Library Threading Considerations

The following Tablet PC threading considerations are specific to the Managed Library.

-   [Thread-Safety](#thread-safety)
-   [STA and MTA Applications](#sta-and-mta-applications)
-   [Windows Forms Threading Considerations](#windows-forms-threading-considerations)
-   [Clipboard Considerations](#clipboard-considerations)
-   [Exceptions within Event Handlers](#exceptions-within-event-handlers)
-   [Disposing Objects and Controls](#disposing-objects-and-controls)
-   [StylusInput APIs](#stylusinput-apis)

## Thread-Safety

The Tablet PC Platform's Managed Library classes are not generally thread-safe. The following collections are thread-safe at the member level; however, these collections do not guarantee that an enumerator is protected if another thread operates on the collection simultaneously:

-   [CursorButtons](https://msdn.microsoft.com/library/ms839506(v=MSDN.10).aspx)
-   [Cursors](https://msdn.microsoft.com/library/ms839493(v=MSDN.10).aspx)
-   [DivisionUnits](https://msdn.microsoft.com/library/ms837954(v=MSDN.10).aspx)
-   [RecognitionAlternates](https://msdn.microsoft.com/library/ms830115(v=MSDN.10).aspx)
-   [Recognizers](https://msdn.microsoft.com/library/ms828520(v=MSDN.10).aspx)
-   [Tablets](https://msdn.microsoft.com/library/ms827599(v=MSDN.10).aspx)

## STA and MTA Applications

Managed applications created by using the wizards contained in Microsoft Visual Studio .NET are single-threaded apartment (STA) by default. You can change the apartment for your application by setting the STA thread or multithreaded apartment (MTA) thread attribute on the entry point of your application.

If your application runs in an MTA, you must write thread-safe code; however, by doing so you can improve certain event handling performance issues.

For more information about the STA thread and MTA thread attributes, see [STAThreadAttribute](https://msdn.microsoft.com/library/71tx0eb5(v=VS.100).aspx) class and [MTAThreadAttribute](https://msdn.microsoft.com/library/77y997f0(v=VS.100).aspx) Class.

## Windows Forms Threading Considerations

The [InkPicture](https://msdn.microsoft.com/library/Aa514604(v=MSDN.10).aspx) and [InkEdit](https://msdn.microsoft.com/library/ms552265(v=VS.100).aspx) controls extend Windows Forms controls. Windows Forms controls use the single-threaded apartment (STA) model because Windows Forms are based on native Win32 windows that are inherently single threaded. In managed code, ink controls should be created in the same thread as the main thread for the form.

In an STA application, certain events happen on a thread other than the application's user interface (UI) thread. When calling any Windows Forms object or control, including the [InkPicture](https://msdn.microsoft.com/library/Aa514604(v=MSDN.10).aspx) and [InkEdit](https://msdn.microsoft.com/library/ms552265(v=VS.100).aspx) controls, from within a Tablet PC event handler, use the object or control's inherited [Control.Invoke](https://msdn.microsoft.com/library/30s4t80c(v=VS.90).aspx) method. The [InvokeRequired](https://msdn.microsoft.com/library/a82t6122(v=VS.90).aspx) property, inherited from the Control class, can be used to determine if this is necessary.

For example, in the following event handler for the [Recognition](https://msdn.microsoft.com/library/ms829424(v=MSDN.10).aspx) event, the [InvokeRequired](https://msdn.microsoft.com/library/a82t6122(v=VS.90).aspx) property is tested and if **TRUE**, the event handler is re-invoked from the user interface thread.


```C++
void recoContext_Recognition(object sender, 
        RecognizerContextRecognitionEventArgs e)
{
    if (InvokeRequired)
    {
        Invoke( new RecognizerContextRecognitionEventHandler(  
                     recoContext_Recognition ),
                    new object[] { sender, e } );
        return;
    }
     // Use the recognition result here.
}
```



If you put a [UserControl](https://msdn.microsoft.com/library/cdhdhykx(v=VS.90).aspx) onto awebpagein a browser (see [Web Controls](web-controls.md)), then it runs as an STA application. For smart client applications (see [No Touch Deployment](no-touch-deployment.md)), the developer has full control over the [ApartmentState](https://msdn.microsoft.com/library/5575keyf(v=VS.90).aspx). (The default is generally STA, but may be MTA, depending on your version of CLR.) For threading issues involving the [**RealTimeStylus**](realtimestylus-class.md), see [Threading Considerations for the StylusInput APIs](threading-considerations-for-the-stylusinput-apis.md).

For more information about calling Windows Forms from an MTA application, see [Multithreaded Windows Forms Control Sample](https://msdn.microsoft.com/en-us/library/3s8xdz5c(v=VS.71).aspx).

## Clipboard Considerations

The [Clipboard](https://msdn.microsoft.com/library/ms648709(v=VS.85).aspx) object works only from an STA thread. When trying to copy to or paste from the Clipboard from a thread that is not STA, you get a [ThreadStateException](https://msdn.microsoft.com/library/fe9t88b7(v=VS.96).aspx). If your application is MTA, create an STA thread to handle the Clipboard's method calls and some of the other UI aspects of your application.

## Exceptions within Event Handlers

Exceptions cannot be thrown from within Tablet PC event handlers. For example, if an event handler delegate for a Tablet PC object or collection has three registered handlers and the first one throws an exception, then the following sequence occurs:

1.  The first handler exits.
2.  The exception is lost.
3.  The remaining handlers are not invoked.

## Disposing Objects and Controls

To avoid a memory leak you must explicitly call the [Dispose](https://msdn.microsoft.com/library/d305e9bx(v=VS.100).aspx) method on any Tablet PC object or control to which an event handler has been attached before the object or control goes out of scope.

To improve performance in your application, manually dispose of any Tablet PC object or control that implements the [Dispose](https://msdn.microsoft.com/library/d305e9bx(v=VS.100).aspx) method when the object or control is no longer needed.

## StylusInput APIs

For information about threading considerations for the [**RealTimeStylus**](realtimestylus-class.md) object and the StylusInput application programming interfaces (APIs) see [Threading Considerations for the StylusInput APIs](threading-considerations-for-the-stylusinput-apis.md).

 

 



