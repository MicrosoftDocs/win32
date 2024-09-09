---
description: Ink collection begins with the digitizer.
ms.assetid: 95e49f5b-d6f0-4a5a-868b-aa0caf87c39c
title: Ink Collection
ms.topic: article
ms.date: 05/31/2018
---

# Ink Collection

Ink collection begins with the digitizer. A user places a pen on the digitizer and starts to write. You can use the ink collection features of the API to manage the collection of ink data that "flows" from the pen. You have access to information about the available hardware on Tablet PC through the [**Tablets**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktablets-item) collection and the [**Tablet**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) object. You then use the [**InkCollector**](inkcollector-class.md) object to get the data that comes from the digitizer.

## Tablets and the Tablet Object

A [**Tablet**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) represents a digitizer device of Tablet PC. A Tablet PC may have more than one digitizer. Using the **Tablet** object, you can query for the available digitizer devices that are attached to Tablet PC and their respective hardware capabilities. For example, you can determine if the **Tablet** you are working with is integrated with the display or is a separate external device.

## InkCollector Object

The [**InkCollector**](inkcollector-class.md) object captures ink input from available [**Tablet**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) devices. The **InkCollector** object only collects ink and gestures that are input into a specific window. A very efficient event sink renders this input in real time. The **InkCollector** object captures the input and directs it into an [**Ink**](inkdisp-class.md) object.

> [!Note]  
> Simultaneously laying down ink with multiple pens may or may not work, depending on the hardware capabilities of the digitizer device.

 

### How the Ink Collector Works

The [**InkCollector**](inkcollector-class.md) object attaches itself to a known application window. It then enables users to employ any available Tablet PC device (including the mouse) to lay down ink in real time on that window. The ink strokes that it collects are stored in an associated [**Ink**](inkdisp-class.md) object. These strokes can then be manipulated or sent to a recognizer for recognition. The **InkCollector** object also notifies the application when a cursor comes into range of any of the Tablet PC devices that are being used.

For the [**InkCollector**](inkcollector-class.md) object to accurately set the mouse cursor within an ink-enabled window, that window must be able to receive the **WM\_SETCURSOR** message. This is successful for all regular windows but, for a control within a dialog box, the dialog parent of the control filters this message. For the control to receive the message, set the **SS\_NOTIFY** style.

## InkOverlay Object

The [**InkCollector**](inkcollector-class.md) object, discussed previously, is useful for applications to provide their own model for selecting, erasing, and other user interaction. The [**InkOverlay**](inkoverlay-class.md) object is a superset of the **InkCollector** object that provides editing support. This is useful for applications to integrate ink drawing and editing into their own document canvas by using a set of standard ink selection models that the object provides.

Both the [**InkCollector**](inkcollector-class.md) object and the [**InkOverlay**](inkoverlay-class.md) object (as well as the [InkPicture](inkpicture-control.md) control) use common constructs, such as the [**Ink**](inkdisp-class.md) object and the [**DrawingAttributes**](inkdrawingattributes-class.md) collection, so that the basic way to change the color of ink is the same everywhere. This enables you to reuse code and to have common programmatic access, which can be particularly important if you offer scripting support in your application.

[**InkOverlay**](inkoverlay-class.md) is a COM object that is useful for annotation scenarios in which users are not concerned with performing recognition on ink but, instead, are interested in the size, shape, color, and position of the ink. It is well suited for taking notes and basic scribbling. The default user interface is a transparent rectangle with opaque ink.

[**InkOverlay**](inkoverlay-class.md) extends the [**InkCollector**](inkcollector-class.md) class in three ways:

-   It raises events for begin-stroke, end-stroke, and ink attribute changes.
-   It enables users to select, erase, and resize ink.
-   It supports Cut, Copy, and Paste commands.

A typical scenario in which [**InkOverlay**](inkoverlay-class.md) is useful is in marking up a presentation slide or image. The **InkOverlay** object enables easy implementation of the ink and layout capabilities that this scenario requires.

To work with [**InkOverlay**](inkoverlay-class.md), you:

1.  Instantiate an [**InkOverlay**](inkoverlay-class.md) object.
2.  Attach the hWnd (handle, in managed code) of a window to the [**InkOverlay**](inkoverlay-class.md) object's [**hWnd**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_hwnd) property ([Handle](/previous-versions/ms582171(v=vs.100)) property, in managed code).
3.  Set the [**InkOverlay**](inkoverlay-class.md) object's [**Enabled**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_enabled) property to **TRUE**.

The [**InkOverlay**](inkoverlay-class.md) object includes basic printing support, but you must implement print preview or other advanced printing capabilities.

[**InkOverlay**](inkoverlay-class.md) persists ink in ink serialized format (ISF).

> [!Note]  
> If the [**InkOverlay**](inkoverlay-class.md) object's [**EditingMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_editingmode) is set to **Delete** or **Select**, other events (such as [**InkAdded**](inkdisp-inkadded.md), [**InkDeleted**](inkdisp-inkdeleted.md), and [**Stroke**](inkoverlay-stroke.md)) are triggered. These events are useful if you want to implement your own delete or select modes.

 

### Selecting Ink

The [**InkOverlay**](inkoverlay-class.md) object enables users to use a lasso tool to select ink objects that are contained in a traced region. Users can also select ink by tapping any [**Ink**](inkdisp-class.md) object.

Use the [**Selection**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_selection) property to return a [**Strokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection that you can use to manipulate a user's selection.

When an [**Ink**](inkdisp-class.md) object or a set of **Ink** objects is selected, sizing handles appear at the four corners of the ink's bounding box and at all midpoints between adjacent corners. If the user drags anywhere within the selected region, the ink becomes movable inside the control.

### Default Behavior

The [**InkOverlay**](inkoverlay-class.md) object is set to collect ink by default. Ink is 53 ink space units wide (where 1 ink space unit = 1 HIMETRIC). Ink is black if the user is not running in high-contrast mode. Otherwise, ink is set to the **COLOR\_WINDOWTEXT** value (**WindowText** in managed code). [**FitToCurve**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_fittocurve) is **FALSE**.

### Cursor and Button Objects

A cursor corresponds to the tip of the pen that is used on Tablet PC. For instance, a pencil has two ends. Usually, one end is used for writing and the other is used for erasing. These two ends correspond to two cursors. The [**Cursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) class is not be confused with [**System.Windows.Forms.Cursor**](/dotnet/api/system.windows.forms.cursor?view=netcore-3.1&preserve-view=true).

On Tablet PC, a cursor is usually defined to be used either for writing or erasing. A cursor may potentially change roles if the application enables this functionality. Some Tablet PC devices allow multiple pens. Each cursor has an associated cursor ID that is unique on the system. A cursor can have zero or more associated buttons. These buttons are provided to the application as CursorButton objects. The application can provide a specific [**DrawingAttributes**](inkdrawingattributes-class.md) object for any given cursor.

### Drawing Attributes Object

A [**DrawingAttributes**](inkdrawingattributes-class.md) object describes how any known set of ink is to be drawn. A **DrawingAttributes** object includes basic properties such as [**Color**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_color), [**Width**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_width), and [**PenTip**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_pentip). It can also encompass advanced parameters, such as variable transparency and Bezier smoothing, that can provide interesting effects or improve ink readability.

### PenInputPanel Object

> [!Note]  
> The [**PenInputPanel**](peninputpanel-class.md) class has been deprecated. The **PenInputPanel** class has been replaced by the [**TextInputPanel**](/windows/desktop/api/peninputpanel/nn-peninputpanel-itextinputpanel) class.

 

The [**PenInputPanel**](peninputpanel-class.md) object allows you to easily add in-place pen input to your applications. The **PenInputPanel** is available as an attachable object that allows you to add Tablet PC Input Panel functionality to existing controls. The user interface is largely mandated by the current input language. You have the option of choosing the default input method for the **PenInputPanel**, either handwriting or keyboard. The end user can switch between input methods using buttons on the user interface.

## Related topics

<dl> <dt>

[**InkCollector Class (C++)**](inkcollector-class.md)
</dt> <dt>

[**InkOverlay Class (C++)**](inkoverlay-class.md)
</dt> <dt>

[**Microsoft.Ink Namespace**](/previous-versions/dotnet/netframework-3.5/ms581553(v=vs.90))
</dt> </dl>

 

 
