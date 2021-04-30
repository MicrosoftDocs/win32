---
description: Overview of the Managed Library and notes on using the Tablet PC platform Managed Library.
ms.assetid: d283ea1c-faf3-4222-a9a7-c67087636b86
title: Using the Managed Library
ms.topic: article
ms.date: 05/31/2018
---

# Using the Managed Library

The common language runtime is the foundation of the Microsoft .NET Framework. You can think of the common language runtime as an agent that manages code at execution time, providing core services such as memory management, thread management, and remoting, while also enforcing strict code safety. In fact, the concept of code management is a fundamental principle of the common language runtime. Code that targets the common language runtime is known as managed code. Code that does not target the common language runtime is known as native code.

The Framework class library is a comprehensive, object-oriented collection of reusable classes that you can use to develop applications ranging from traditional command-line or graphical user interface (GUI) applications to applications based on the latest innovations provided by ASP.NET and Web Services.

The Tablet PC Managed Library contains a set of managed objects that extends the Framework to provide support for input and output of handwriting on Tablet PC as well as data interchange with other computers.

## Exceptions

The managed library objects in the Tablet PC API wrap the COM library implementations. When the underlying COM library object or control returns an error, the managed API's will throw a Marshal.ThrowExceptionForHR exception that provides the details on the inner COM exception. You can refer to the HRESULT values in the COM Library Reference for details on the possible errors that may be returned.

## Object Comparison

For all objects in the Tablet PC Platform Managed library, [**Equals**](/previous-versions/windows/) is not overridden to correctly compare two objects that are the same. The managed application programming interface (API) does not support the comparison of objects for equality, either through the **Equals** function or through the equals (==) operator.

## Binding to the Latest Microsoft.Ink.dll

The latest Microsoft.Ink.dll assembly is a compatible replacement for Microsoft.Ink.dll version 1.0 and Microsoft.Ink.15.dll. In most cases, you do not need to make any changes to your applications that are distributed with the older assemblies. However, in some cases you need to instruct the common language runtime loader to use the newer dynamic-link library (DLL) wherever the older DLLs have been referenced.

The only time you need to explicitly bind to the new assembly by using the following technique is if your application uses a component that references the version 1.0 or 1.5 assembly in combination with a component that references a more recent version assembly,such as 1.7, and if those components may exchange data.

The best way to instruct the common language runtime loader to use the newer DLL is to redirect assembly versions at the application level. You can specify that your application use the newer version of the assembly by putting assembly binding information in your application's configuration file. For more information about redirecting assembly versions at the application level, see [Redirecting Assembly Versions](/documentation/?url=%2flibrary%2fcpguide%2fhtml%2fcpconassemblyversionredirection.asp%3fframe%3dtrue), specifically the section "Specifying Assembly Binding in Configuration Files."

You will need to create a configuration file in the same directory as your executable file. The configuration file must have the same name as your executable, followed by the .config file extension. For example, for an application, MyApp.exe, the configuration file must be the MyApp.exe.config file. The configuration file uses a [bindingRedirect](/previous-versions/dotnet/netframework-1.1/eftw1fys(v=vs.71)) element to force all prior versions to be mapped to the latest version, as shown in the following example:

`<bindingRedirect oldVersion="0.0.0.0-1.7.2600.xxxx" newVersion="1.7.2600.xxxx" />`

For more information about configuration files, including examples of how to construct the Extensible Markup Language (XML) for the configuration file, see both [bindingRedirect](/previous-versions/dotnet/netframework-1.1/eftw1fys(v=vs.71)) and [Redirecting Assembly Versions](/documentation/?url=%2flibrary%2fcpguide%2fhtml%2fcpconassemblyversionredirection.asp%3fframe%3dtrue).

Applications created with Microsoft Windows XP Tablet PC Edition Development Kit 1.7 and later versions are automatically bound to the new version of the Microsoft.Ink assembly. For more information about assembly binding see [How the Runtime Locates Assemblies](/documentation/?url=%2flibrary%2fcpguide%2fhtml%2fcpconHowRuntimeLocatesAssemblies.asp).

> [!Note]  
> Using application policy to bind to the updated assembly does not work for applications that use the [Divider](/previous-versions/ms583616(v=vs.100)) class or the [PenInputPanel](/previous-versions/aa514041(v=msdn.10)) class. Applications that use either of those classes must either continue to use Microsoft.Ink.15.dll or be recompiled after referencing the updated assembly.

 

## Working with Events

If the code within an event handler for any of the managed objects throws an exception, the exception is not delivered to the user. To ensure that exceptions are delivered, use try-catch blocks in your event handlers for managed events.

## Managing Forms

The [Form](/dotnet/api/system.windows.forms.form?view=netcore-3.1) class and its base classes do not define a finalizer. To clean up your resources on a form, write a subclass that provides a finalizer (for example, the C\# destructor using the ~) that calls [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1). To do the cleanup the finalizer overrides Dispose and then calls the base class Dispose. Do not refer to other objects that require the [Finalize](/previous-versions/windows/) method in the Dispose method when the Boolean parameter is **FALSE**, because those objects may already have been finalized. For more information about releasing resources see [Finalize Methods and Destructors](/documentation/?url=%2flibrary%2fcpguide%2fhtml%2fcpconfinalizemethodscdestructors.asp).

## Forms and the RecognizerContext

[RecognizerContext](/previous-versions/ms552546(v=vs.100)) events run in a different thread than the thread that the form is on. Controls in Windows Forms are bound to a specific thread and are not thread safe. Therefore, you must use one of the control's invoke methods to marshal the call to the proper thread. Four methods on a control are thread safe: the [Invoke](/dotnet/api/system.windows.forms.control.invoke?view=netcore-3.1), [BeginInvoke](/dotnet/api/system.windows.forms.control.begininvoke?view=netcore-3.1), [EndInvoke](/dotnet/api/system.windows.forms.control.endinvoke?view=netcore-3.1), and [CreateGraphics](/dotnet/api/system.windows.forms.control.creategraphics?view=netcore-3.1) methods. For all other method calls, use one of these invoke methods when calling from a different thread. For more information on using these methods, see [Manipulating Controls from Threads](/previous-versions/757y83z4(v=vs.140)).

## Waiting for Events

The Tablet PC environment is multithreaded. Use the [**CoWaitForMultipleHandles**](/windows/win32/api/combaseapi/nf-combaseapi-cowaitformultiplehandles) function instead of other wait methods to allow re-entrant Component Object Model (COM) calls to enter your multithreaded apartment (MTA) while your application is waiting on an event.

## Using Ink Strokes Collections

Instances of [Strokes](/previous-versions/ms552701(v=vs.100)) collections which are obtained from an [Ink](/previous-versions/aa515768(v=msdn.10)) object are not garbage collected. In order to avoid a memory leak, any time that you are working with one of these collections, make use of the "using" statement as shown below.


```C++
using (Strokes strokes = myInk.Strokes)
{
    int i = strokes.Count;
}
```



## Disposing Managed Objects and Controls

To avoid a memory leak you must explicitly call the [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1) method on any Tablet PC object or control to which an event handler has been attached before the object or control goes out of scope.

To improve the performance of your application, manually dispose of the following objects, controls, and collection when they are no longer needed.

-   [Divider](/previous-versions/ms583616(v=vs.100))
-   [Ink](/previous-versions/aa515768(v=msdn.10))
-   [InkCollector](/previous-versions/ms583683(v=vs.100))
-   [InkEdit](/previous-versions/ms552265(v=vs.100))
-   [InkOverlay](/previous-versions/ms552322(v=vs.100))
-   [InkPicture](/previous-versions/aa514604(v=msdn.10))
-   [PenInputPanel](/previous-versions/aa514041(v=msdn.10))
-   [RecognizerContext](/previous-versions/ms552546(v=vs.100))
-   [Strokes](/previous-versions/ms552701(v=vs.100))

The following C\# example demonstrates some scenarios in which the [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1) method is used.


```C++
// A field for a Divider object
private Microsoft.Ink.Divider theDivider;

// A method that creates a Divider object
public void CreateDivider()
{
    // Make sure any previous Divider object was disposed of.
    if (null != theDivider)
    {
        theDivider.Dispose();
        theDivider = null;
    }
    // Create the Divider object.
    theDivider = new Microsoft.Ink.Divider();

    // The remainder of the method
}

// A method that disposes of the Divider object
public void DisposeDivider()
{
    // The remainder of the method

    // Dispose of the Divider object.
    if (null != theDivider)
    {
        theDivider.Dispose();
        theDivider = null;
    }
}

// A method that uses a local PenInputPanel object.
public void UsePenInputPanel()
{
    // Create the PenInputPanel object.
    Microsoft.Ink.PenInputPanel thePenInputPanel =
        new Microsoft.Ink.PenInputPanel();

    // The remainder of the method

    // Dispose of the PenInputPanel object before exiting.
    thePenInputPanel.Dispose();
    thePenInputPanel = null;
}
```



 

 