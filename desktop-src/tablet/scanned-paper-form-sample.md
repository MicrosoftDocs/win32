---
description: In this C\# sample, a paper form has been scanned as a Portable Network Graphics (PNG) file and specified as the background image at run time for a InkPicture control. The sample uses a message box to display handwriting recognition results.
ms.assetid: fc9a39c2-9e4b-4d22-a118-3d24544897dd
title: Scanned Paper Form Sample
ms.topic: article
ms.date: 05/31/2018
---

# Scanned Paper Form Sample

In this C\# sample, a paper form has been scanned as a Portable Network Graphics (PNG) file and specified as the background image at run time for a [InkPicture](/previous-versions/aa514604(v=msdn.10)) control. The sample uses a message box to display handwriting recognition results.

The sample includes an Extensible Markup Language (XML) file, Formdata.xml. The XML file contains the name of the PNG file. It also contains `FieldInfo` elements that define rectangular regions on the form where a user can enter ink. The information in the `FieldInfo` element is shown in the following example:


```C++
    <FieldInfo>
        <Name>first name</Name>
        <Left>88</Left>
        <Top>65</Top>
        <Right>332</Right>
        <Bottom>94</Bottom>
    </FieldInfo>
```



The Left, Top, Right, and Bottom elements are definitions of pixel coordinates for each field.

The sample initializes a new [DataSet](/dotnet/api/system.data.dataset?view=netcore-3.1&preserve-view=true) with the data contained in Formdata.xml:


```C++
    formData = new DataSet("FormData");
    formData.ReadXml("formdata.xml"); 
```



The form image specified in Formdata.xml is loaded as the background of the [InkPicture](/previous-versions/aa514604(v=msdn.10)) control:


```C++
    inkPicture1.BackgroundImage = 
        System.Drawing.Image.FromFile(
        (string) formData.Tables["FormData"].Rows[0]["Image"]);
```



Ink collection is then enabled for the [InkPicture](/previous-versions/aa514604(v=msdn.10)) control:


```C++
    inkPicture1.InkEnabled = true;
```



## Menu Event Handlers

The application includes click event handlers for all of the menus displayed along the top of the form.

### Recognize Menu Item

The Recognize menu click event handler disables ink collection for the control and checks for a handwriting recognizer. If no recognizer is installed, a dialog box is displayed. A user must then click the Ink or Pen menu option to re-enable the control for ink input.

If a recognizer is installed, the `Recognize` function retrieves the XML data that specifies pixel coordinates for each form field. The coordinates are converted to ink space coordinates, and a rectangle is defined for each form field. After rectangles are defined, the function finds the strokes that intersect and lie within each rectangle. Finally, it performs recognition on the ink and displays the results in a message box.

### Ink Menu Item

The Ink menu click event handler enables the [InkPicture](/previous-versions/aa514604(v=msdn.10)) control.

### Pen Menu Item

The Pen menu click event handler performs the following tasks:

-   Disables ink collection for the [InkPicture](/previous-versions/aa514604(v=msdn.10)) control (which is necessary before changing the [EditingMode](/previous-versions/ms582189(v=vs.100)) property).
-   Sets the [EditingMode](/previous-versions/ms582189(v=vs.100)) property to collect ink.
-   Re-enables ink collection for the [InkPicture](/previous-versions/aa514604(v=msdn.10)) control and toggles the Pen, Select, and Eraser menus to indicate the active mode.

### Edit Menu Item

The Edit menu click event handler is similar to the Pen menu event handler. It performs the following tasks:

-   Disables ink collection.
-   Sets the [EditingMode](/previous-versions/ms582189(v=vs.100)) property to **Select**, which enables the user to perform ink selection.
-   Re-enables ink collection and toggles the Pen, Edit, and Eraser menus to indicate the active mode.

### Eraser Menu Item

The Eraser menu click event handler sets the [InkPicture](/previous-versions/aa514604(v=msdn.10)) control [EditingMode](/previous-versions/ms582189(v=vs.100)) to **Delete**, which enables a user to erase ink. It also toggles the Pen, Edit, and Eraser menu items.

### Clear Menu Item

The Clear menu click event handler deletes the current [Strokes](/previous-versions/ms552701(v=vs.100)) collection for the [InkPicture](/previous-versions/aa514604(v=msdn.10)) control, thereby erasing all of the ink on the form.

## Closing the Form

In the Windows Form Designer generated code, the [InkPicture](/previous-versions/aa514604(v=msdn.10)) control is added to the form's component list when the form is initialized. When the form closes, the InkPicture control is disposed, as well as the other components of the form, by the form's [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1&preserve-view=true) method.

## Related topics

<dl> <dt>

[InkEdit Control](inkedit-control.md)
</dt> <dt>

[InkPicture Control](inkpicture-control.md)
</dt> </dl>

 

 
