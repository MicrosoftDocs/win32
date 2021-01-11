---
description: The following Tablet PC threading considerations are specific to the Managed Library.
ms.assetid: bcc398d3-22ea-466c-9206-92b0ac208def
title: Managed Library Threading Considerations
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

-   [CursorButtons](/previous-versions/ms839506(v=msdn.10))
-   [Cursors](/previous-versions/ms839493(v=msdn.10))
-   [DivisionUnits](/previous-versions/ms837954(v=msdn.10))
-   [RecognitionAlternates](/previous-versions/ms830115(v=msdn.10))
-   [Recognizers](/previous-versions/ms828520(v=msdn.10))
-   [Tablets](/previous-versions/ms827599(v=msdn.10))

## STA and MTA Applications

Managed applications created by using the wizards contained in Microsoft Visual Studio .NET are single-threaded apartment (STA) by default. You can change the apartment for your application by setting the STA thread or multithreaded apartment (MTA) thread attribute on the entry point of your application.

If your application runs in an MTA, you must write thread-safe code; however, by doing so you can improve certain event handling performance issues.

For more information about the STA thread and MTA thread attributes, see [STAThreadAttribute](/dotnet/api/system.stathreadattribute?view=netcore-3.1) class and [MTAThreadAttribute](/dotnet/api/system.mtathreadattribute?view=netcore-3.1) Class.

## Windows Forms Threading Considerations

The [InkPicture](/previous-versions/aa514604(v=msdn.10)) and [InkEdit](/previous-versions/ms552265(v=vs.100)) controls extend Windows Forms controls. Windows Forms controls use the single-threaded apartment (STA) model because Windows Forms are based on native Win32 windows that are inherently single threaded. In managed code, ink controls should be created in the same thread as the main thread for the form.

In an STA application, certain events happen on a thread other than the application's user interface (UI) thread. When calling any Windows Forms object or control, including the [InkPicture](/previous-versions/aa514604(v=msdn.10)) and [InkEdit](/previous-versions/ms552265(v=vs.100)) controls, from within a Tablet PC event handler, use the object or control's inherited [Control.Invoke](/dotnet/api/system.windows.forms.control.invoke?view=netcore-3.1) method. The [InvokeRequired](/dotnet/api/system.windows.forms.control.invokerequired?view=netcore-3.1) property, inherited from the Control class, can be used to determine if this is necessary.

For example, in the following event handler for the [Recognition](/previous-versions/ms829424(v=msdn.10)) event, the [InvokeRequired](/dotnet/api/system.windows.forms.control.invokerequired?view=netcore-3.1) property is tested and if **TRUE**, the event handler is re-invoked from the user interface thread.


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



If you put a [UserControl](/dotnet/api/system.web.ui.usercontrol?view=netframework-4.8) onto awebpagein a browser (see [Web Controls](web-controls.md)), then it runs as an STA application. For smart client applications (see [No Touch Deployment](no-touch-deployment.md)), the developer has full control over the [ApartmentState](/dotnet/api/system.threading.apartmentstate?view=netcore-3.1). (The default is generally STA, but may be MTA, depending on your version of CLR.) For threading issues involving the [**RealTimeStylus**](realtimestylus-class.md), see [Threading Considerations for the StylusInput APIs](threading-considerations-for-the-stylusinput-apis.md).

For more information about calling Windows Forms from an MTA application, see [Multithreaded Windows Forms Control Sample](/previous-versions/dotnet/netframework-1.1/3s8xdz5c(v=vs.71)).

## Clipboard Considerations

The [Clipboard](../dataxchg/clipboard.md) object works only from an STA thread. When trying to copy to or paste from the Clipboard from a thread that is not STA, you get a [ThreadStateException](/previous-versions/windows/). If your application is MTA, create an STA thread to handle the Clipboard's method calls and some of the other UI aspects of your application.

## Exceptions within Event Handlers

Exceptions cannot be thrown from within Tablet PC event handlers. For example, if an event handler delegate for a Tablet PC object or collection has three registered handlers and the first one throws an exception, then the following sequence occurs:

1.  The first handler exits.
2.  The exception is lost.
3.  The remaining handlers are not invoked.

## Disposing Objects and Controls

To avoid a memory leak you must explicitly call the [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1) method on any Tablet PC object or control to which an event handler has been attached before the object or control goes out of scope.

To improve performance in your application, manually dispose of any Tablet PC object or control that implements the [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1) method when the object or control is no longer needed.

## StylusInput APIs

For information about threading considerations for the [**RealTimeStylus**](realtimestylus-class.md) object and the StylusInput application programming interfaces (APIs) see [Threading Considerations for the StylusInput APIs](threading-considerations-for-the-stylusinput-apis.md).

 

 
