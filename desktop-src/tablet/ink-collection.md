---
Description: Ink collection begins with the digitizer.
ms.assetid: 95e49f5b-d6f0-4a5a-868b-aa0caf87c39c
title: Ink Collection
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ink Collection

Ink collection begins with the digitizer. A user places a pen on the digitizer and starts to write. You can use the ink collection features of the API to manage the collection of ink data that "flows" from the pen. You have access to information about the available hardware on Tablet PC through the [**Tablets**](/windows/win32/msinkaut/?branch=master) collection and the [**Tablet**](/windows/win32/msinkaut/nn-msinkaut-iinktablet?branch=master) object. You then use the [**InkCollector**](/windows/win32/msinkaut/?branch=master) object to get the data that comes from the digitizer.

## Tablets and the Tablet Object

A [**Tablet**](/windows/win32/msinkaut/nn-msinkaut-iinktablet?branch=master) represents a digitizer device of Tablet PC. A Tablet PC may have more than one digitizer. Using the **Tablet** object, you can query for the available digitizer devices that are attached to Tablet PC and their respective hardware capabilities. For example, you can determine if the **Tablet** you are working with is integrated with the display or is a separate external device.

## InkCollector Object

The [**InkCollector**](/windows/win32/msinkaut/?branch=master) object captures ink input from available [**Tablet**](/windows/win32/msinkaut/nn-msinkaut-iinktablet?branch=master) devices. The **InkCollector** object only collects ink and gestures that are input into a specific window. A very efficient event sink renders this input in real time. The **InkCollector** object captures the input and directs it into an [**Ink**](/windows/win32/msinkaut/?branch=master) object.

> [!Note]  
> Simultaneously laying down ink with multiple pens may or may not work, depending on the hardware capabilities of the digitizer device.

 

### How the Ink Collector Works

The [**InkCollector**](/windows/win32/msinkaut/?branch=master) object attaches itself to a known application window. It then enables users to employ any available Tablet PC device (including the mouse) to lay down ink in real time on that window. The ink strokes that it collects are stored in an associated [**Ink**](/windows/win32/msinkaut/?branch=master) object. These strokes can then be manipulated or sent to a recognizer for recognition. The **InkCollector** object also notifies the application when a cursor comes into range of any of the Tablet PC devices that are being used.

For the [**InkCollector**](/windows/win32/msinkaut/?branch=master) object to accurately set the mouse cursor within an ink-enabled window, that window must be able to receive the **WM\_SETCURSOR** message. This is successful for all regular windows but, for a control within a dialog box, the dialog parent of the control filters this message. For the control to receive the message, set the **SS\_NOTIFY** style.

## InkOverlay Object

The [**InkCollector**](/windows/win32/msinkaut/?branch=master) object, discussed previously, is useful for applications to provide their own model for selecting, erasing, and other user interaction. The [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object is a superset of the **InkCollector** object that provides editing support. This is useful for applications to integrate ink drawing and editing into their own document canvas by using a set of standard ink selection models that the object provides.

Both the [**InkCollector**](/windows/win32/msinkaut/?branch=master) object and the [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object (as well as the [InkPicture](inkpicture-control.md) control) use common constructs, such as the [**Ink**](/windows/win32/msinkaut/?branch=master) object and the [**DrawingAttributes**](/windows/win32/msinkaut/?branch=master) collection, so that the basic way to change the color of ink is the same everywhere. This enables you to reuse code and to have common programmatic access, which can be particularly important if you offer scripting support in your application.

[**InkOverlay**](/windows/win32/msinkaut/?branch=master) is a COM object that is useful for annotation scenarios in which users are not concerned with performing recognition on ink but, instead, are interested in the size, shape, color, and position of the ink. It is well suited for taking notes and basic scribbling. The default user interface is a transparent rectangle with opaque ink.

[**InkOverlay**](/windows/win32/msinkaut/?branch=master) extends the [**InkCollector**](/windows/win32/msinkaut/?branch=master) class in three ways:

-   It raises events for begin-stroke, end-stroke, and ink attribute changes.
-   It enables users to select, erase, and resize ink.
-   It supports Cut, Copy, and Paste commands.

A typical scenario in which [**InkOverlay**](/windows/win32/msinkaut/?branch=master) is useful is in marking up a presentation slide or image. The **InkOverlay** object enables easy implementation of the ink and layout capabilities that this scenario requires.

To work with [**InkOverlay**](/windows/win32/msinkaut/?branch=master), you:

1.  Instantiate an [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object.
2.  Attach the hWnd (handle, in managed code) of a window to the [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object's [**hWnd**](/windows/win32/msinkaut/?branch=master) property ([Handle](P:Microsoft.Ink.InkOverlay.Handle) property, in managed code).
3.  Set the [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object's [**Enabled**](/windows/win32/msinkaut/?branch=master) property to **TRUE**.

The [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object includes basic printing support, but you must implement print preview or other advanced printing capabilities.

[**InkOverlay**](/windows/win32/msinkaut/?branch=master) persists ink in ink serialized format (ISF).

> [!Note]  
> If the [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object's [**EditingMode**](/windows/win32/msinkaut/?branch=master) is set to **Delete** or **Select**, other events (such as [**InkAdded**](inkdisp-inkadded.md), [**InkDeleted**](inkdisp-inkdeleted.md), and [**Stroke**](inkoverlay-stroke.md)) are triggered. These events are useful if you want to implement your own delete or select modes.

 

### Selecting Ink

The [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object enables users to use a lasso tool to select ink objects that are contained in a traced region. Users can also select ink by tapping any [**Ink**](/windows/win32/msinkaut/?branch=master) object.

Use the [**Selection**](/windows/win32/msinkaut/?branch=master) property to return a [**Strokes**](/windows/win32/msinkaut/?branch=master) collection that you can use to manipulate a user's selection.

When an [**Ink**](/windows/win32/msinkaut/?branch=master) object or a set of **Ink** objects is selected, sizing handles appear at the four corners of the ink's bounding box and at all midpoints between adjacent corners. If the user drags anywhere within the selected region, the ink becomes movable inside the control.

### Default Behavior

The [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object is set to collect ink by default. Ink is 53 ink space units wide (where 1 ink space unit = 1 HIMETRIC). Ink is black if the user is not running in high-contrast mode. Otherwise, ink is set to the **COLOR\_WINDOWTEXT** value (**WindowText** in managed code). [**FitToCurve**](/windows/win32/msinkaut/?branch=master) is **FALSE**.

### Cursor and Button Objects

A cursor corresponds to the tip of the pen that is used on Tablet PC. For instance, a pencil has two ends. Usually, one end is used for writing and the other is used for erasing. These two ends correspond to two cursors. The [**Cursor**](/windows/win32/msinkaut/nn-msinkaut-iinkcursor?branch=master) class is not be confused with [**System.Windows.Forms.Cursor**](T:System.Windows.Forms.Cursor).

On Tablet PC, a cursor is usually defined to be used either for writing or erasing. A cursor may potentially change roles if the application enables this functionality. Some Tablet PC devices allow multiple pens. Each cursor has an associated cursor ID that is unique on the system. A cursor can have zero or more associated buttons. These buttons are provided to the application as CursorButton objects. The application can provide a specific [**DrawingAttributes**](/windows/win32/msinkaut/?branch=master) object for any given cursor.

### Drawing Attributes Object

A [**DrawingAttributes**](/windows/win32/msinkaut/?branch=master) object describes how any known set of ink is to be drawn. A **DrawingAttributes** object includes basic properties such as [**Color**](/windows/win32/msinkaut/?branch=master), [**Width**](/windows/win32/msinkaut/?branch=master), and [**PenTip**](/windows/win32/msinkaut/?branch=master). It can also encompass advanced parameters, such as variable transparency and Bezier smoothing, that can provide interesting effects or improve ink readability.

### PenInputPanel Object

> [!Note]  
> The [**PenInputPanel**](/windows/win32/msinkaut/?branch=master) class has been deprecated. The **PenInputPanel** class has been replaced by the [**TextInputPanel**](/windows/win32/peninputpanel/nn-peninputpanel-itextinputpanel?branch=master) class.

 

The [**PenInputPanel**](/windows/win32/msinkaut/?branch=master) object allows you to easily add in-place pen input to your applications. The **PenInputPanel** is available as an attachable object that allows you to add Tablet PC Input Panel functionality to existing controls. The user interface is largely mandated by the current input language. You have the option of choosing the default input method for the **PenInputPanel**, either handwriting or keyboard. The end user can switch between input methods using buttons on the user interface.

## Related topics

<dl> <dt>

[**InkCollector Class (C++)**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[**InkOverlay Class (C++)**](/windows/win32/msinkaut/?branch=master)
</dt> <dt>

[**Microsoft.Ink Namespace**](N:Microsoft.Ink)
</dt> </dl>

 

 



