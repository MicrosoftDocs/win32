---
description: Overview of ink controls for the Tablet PC.
ms.assetid: 03229b86-f59b-4946-8816-fa153af57630
title: Ink Controls
ms.topic: article
ms.date: 05/31/2018
---

# Ink Controls

The Tablet PC platform provides two controls, [InkEdit](inkedit-control.md) and [InkPicture](inkpicture-control.md), which enable you to easily add ink and handwriting recognition to Tablet PC applications. The InkEdit control has [managed](/previous-versions/ms835842(v=msdn.10)), [ActiveX](inkedit-control-reference.md) , and Win32 versions, while InkPicture has only the managed [InkPicture](/previous-versions/ms583740(v=vs.100)) and [ActiveX](inkpicture-control-reference.md) versions.

The key difference between the controls is in how data is saved. The [InkEdit](inkedit-control.md) control saves ink as text by default, while [InkPicture](inkpicture-control.md) saves ink as ink.

The [InkEdit](inkedit-control.md) control is intended for text entry through handwriting recognition. [InkPicture](inkpicture-control.md) is intended for annotation (for example, marking up a presentation slide or other picture).

In managed code, create ink controls in the same thread as the main thread for the form. If an [InkEdit](inkedit-control.md) or [InkPicture](inkpicture-control.md) control is created in a different thread, then your application may not respond properly.

You should explicitly change the threading model to single-thread apartment (STA) before creating an ink control. This causes the control to be created on the main thread. You can use the following Managed C++ code to explicitly set the threading model.


```C++
Thread::get_CurrentThread()->set_ApartmentState(ApartmentState::STA);
```



You can use the following code to do the same thing in C\#.


```C++
System.Threading.Thread.CurrentThread.ApartmentState = System.Threading.ApartmentState.STA;
```



In managed code, to avoid a memory leak you must explicitly call the [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1) method on any Tablet PC control to which an event handler has been attached before the control goes out of scope.

The following sections describe ink controls and the use of ink controls in applications:

-   [Adding Ink Controls to a Project](adding-ink-controls-to-a-project.md)
-   [InkEdit Control](inkedit-control.md)
-   [InkPicture Control](inkpicture-control.md)

 

 
