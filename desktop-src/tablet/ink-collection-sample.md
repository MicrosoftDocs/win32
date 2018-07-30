---
Description: This application is based on the InkCollector object and demonstrates the collection of ink.
ms.assetid: e799fb16-5a1e-4d57-a033-554f72e2e685
title: Ink Collection Sample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ink Collection Sample

This application is based on the [InkCollector](https://msdn.microsoft.com/library/ms836493(v=MSDN.10).aspx) object and demonstrates the collection of ink. The application creates a window, attaches an InkCollector object to it, and provides the user with menu choices that can be used to change the ink color, the ink width, and enable and disable ink collection.

> [!Note]  
> The version discussed in this section is Visual Basic .NET. The concepts are the same between other language versions in the samples library.

 

## Declaring the InkCollector

The application first imports the [Microsoft.Ink](https://msdn.microsoft.com/library/ms826516(v=MSDN.10).aspx) namespace. Then, the application declares `myInkCollector`, which holds the [InkCollector](https://msdn.microsoft.com/library/ms836493(v=MSDN.10).aspx) object for the form.


```C++
' The Ink namespace, which contains the Tablet PC Platform APIImports Microsoft.Ink
...
Public Class InkCollection
   Inherits Form
    ' Declare the Ink Collector object
    Private myInkCollector
```



## Setting Things Up

The form's `InkCollection_Load` method handles the form's [Load](https://msdn.microsoft.com/library/4w303742(v=VS.90).aspx) event. It creates a [InkCollector](https://msdn.microsoft.com/library/ms836493(v=MSDN.10).aspx) object assigned to the form modifies the [DefaultDrawingAttributes](https://msdn.microsoft.com/library/ms836500(v=MSDN.10).aspx) property of the InkCollector object and enables the InkCollector object.


```C++
Private Sub InkCollection_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    ' Create an ink collector and assign it to this form's window
    myInkCollector = New InkCollector(Me.Handle)

    ' Set the pen width to be a medium width
    myInkCollector.DefaultDrawingAttributes.Width = MediumInkWidth

    ' If you do not modify the default drawing attributes, the default 
    ' drawing attributes will use the following properties and values:
    ' ...

    ' Turn the ink collector on
    myInkCollector.Enabled = True
End Sub
```



The [InkCollector](https://msdn.microsoft.com/library/ms836493(v=MSDN.10).aspx) is assigned to the form's window by assigning the form's window handle to the InkCollector object's [Handle](https://msdn.microsoft.com/library/ms836504(v=MSDN.10).aspx) property. Ink collection is turned on by setting the InkCollector object's [Enabled](https://msdn.microsoft.com/library/ms836503(v=MSDN.10).aspx) property to **TRUE**.

The [InkCollector](https://msdn.microsoft.com/library/ms836493(v=MSDN.10).aspx) object's [DefaultDrawingAttributes](https://msdn.microsoft.com/library/ms836500(v=MSDN.10).aspx) property sets the default attributes that are assigned to a new cursor. To set different attributes on a new cursor, use the [DrawingAttributes](https://msdn.microsoft.com/library/ms839523(v=MSDN.10).aspx) property of the [Cursor](https://msdn.microsoft.com/library/ms839521(v=MSDN.10).aspx) object. To change the drawing attributes of a single stroke, use the [DrawingAttributes](https://msdn.microsoft.com/library/ms827846(v=MSDN.10).aspx) property of the [Stroke](https://msdn.microsoft.com/library/ms827842(v=MSDN.10).aspx) object.

## Changing the Properties

The rest of this simple application consists of handlers for the various menu selections the user can make. For example, when the user chooses to change the ink color to red by selecting Red from the Ink menu, the color is changed using the [Color](https://msdn.microsoft.com/library/ms837933(v=MSDN.10).aspx) property on [InkCollector](https://msdn.microsoft.com/library/ms836493(v=MSDN.10).aspx) object's [DefaultDrawingAttributes](https://msdn.microsoft.com/library/ms836500(v=MSDN.10).aspx) property in the event handler for the menu.


```C++
Private Sub miRed_Click(ByVal sender As System.Object, 
                        ByVal e As System.EventArgs) Handles miRed.Click
    myInkCollector.DefaultDrawingAttributes.Color = Color.Red
End Sub
```



## Closing the Form

The form's [Dispose](https://msdn.microsoft.com/library/d305e9bx(v=VS.90).aspx) method disposes the [InkCollector](https://msdn.microsoft.com/library/ms836493(v=MSDN.10).aspx) object, `myInkCollector`.

 

 



