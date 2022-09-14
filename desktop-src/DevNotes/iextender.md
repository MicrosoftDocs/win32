---
description: The IExtender interface provides a set of basic properties that are added to the interface of a control. Programmers can use these properties as if they were part of the control.
ms.assetid: 901873bd-af6a-415e-865f-21769367c99f
title: IExtender interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IExtender
- IExtender.Align
- IExtender.get_Align
- IExtender.put_Align
- IExtender.Enabled
- IExtender.get_Enabled
- IExtender.put_Enabled
- IExtender.Height
- IExtender.get_Height
- IExtender.put_Height
- IExtender.Left
- IExtender.get_Left
- IExtender.put_Left
- IExtender.TabStop
- IExtender.get_TabStop
- IExtender.put_TabStop
- IExtender.Top
- IExtender.get_Top
- IExtender.put_Top
- IExtender.Visible
- IExtender.get_Visible
- IExtender.put_Visible
- IExtender.Width
- IExtender.get_Width
- IExtender.put_Width
- IExtender.Name
- IExtender.get_Name
- IExtender.Parent
- IExtender.get_Parent
- IExtender.Hwnd
- IExtender.get_Hwnd
- IExtender.Container
- IExtender.get_Container
api_type: 
- COM
api_location: 
- Ole2disp.dll
- Oleaut32.dll
---

# IExtender interface

The **IExtender** interface provides a set of basic properties that are added to the interface of a control. Programmers can use these properties as if they were part of the control.

## Members

The **IExtender** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IExtender** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IExtender** interface has these methods.



| Method                         | Description                                    |
|:-------------------------------|:-----------------------------------------------|
| [**Move**](iextender-move.md) | Moves an MDIForm, form, or control.<br/> |



 

### Properties

The **IExtender** interface has these properties.



<table>
<colgroup>
<col  />
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th >Property</th>
<th >Access type</th>
<th >Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td >Align<br/></td>
<td >Read/write<br/></td>
<td >Returns or sets a value that determines whether an object is displayed in any size anywhere on a form or whether it is displayed at the top, bottom, left, or right of the form and is automatically sized to fit the width of the form.<br/> 
<table>
<thead>
<tr class="header">
<th>Constant</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>vbAlignNone 0</td>
<td>(Default in a non-MDI form) None—size and location can be set at design time or in code. The setting is ignored if the object is on an MDI form.</td>
</tr>
<tr class="even">
<td>vbAlignTop 1</td>
<td>(Default in an MDI form) Top—the object is at the top of the form, and its width is equal to the ScaleWidth property setting of the form.</td>
</tr>
<tr class="odd">
<td>vbAlignBottom 2</td>
<td>Bottom—the object is at the bottom of the form, and its width is equal to the ScaleWidth property setting of the form.</td>
</tr>
<tr class="even">
<td>vbAlignLeft 3</td>
<td>Left—the object is at the left of the form, and its width is equal to the ScaleWidth property setting of the form.</td>
</tr>
<tr class="odd">
<td>vbAlignRight 4</td>
<td>Right—the object is at the right of the form, and its width is equal to the ScaleWidth property setting of the form.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td ><p>Container</p></td>
<td ><p>Read-only</p></td>
<td ><p>Returns the container of a control on a form.</p></td>
</tr>
<tr class="odd">
<td ><p>Enabled</p></td>
<td ><p>Read/write</p></td>
<td ><p>Returns or sets a value that determines whether a form or control can respond to user-generated events.</p></td>
</tr>
<tr class="even">
<td ><p>Height</p></td>
<td ><p>Read/write</p></td>
<td ><p>Returns or sets the height of an object.</p></td>
</tr>
<tr class="odd">
<td ><p>Hwnd</p></td>
<td ><p>Read-only</p></td>
<td ><p>Returns a handle to a form or control.</p></td>
</tr>
<tr class="even">
<td ><p>Left</p></td>
<td ><p>Read/write</p></td>
<td ><p>Returns or sets the distance between the internal left edge of an object and the left edge of its container.</p></td>
</tr>
<tr class="odd">
<td ><p>Name</p></td>
<td ><p>Read-only</p></td>
<td ><p>Returns the name used in code to identify a form, control, or data access object.</p></td>
</tr>
<tr class="even">
<td ><p>Parent</p></td>
<td ><p>Read-only</p></td>
<td ><p>Returns the form, object, or collection that contains a control or another object or collection.</p></td>
</tr>
<tr class="odd">
<td ><p>TabStop</p></td>
<td ><p>Read/write</p></td>
<td ><p>Returns or sets a value that indicates whether a user can use the <strong>Tab</strong> key to give the focus to an object.</p></td>
</tr>
<tr class="even">
<td ><p>Top</p></td>
<td ><p>Read/write</p></td>
<td ><p>Returns or sets the distance between the internal top edge of an object and the top edge of its container.</p></td>
</tr>
<tr class="odd">
<td ><p>Visible</p></td>
<td ><p>Read/write</p></td>
<td ><p>Returns or sets a value that indicates whether an object is visible or hidden.</p></td>
</tr>
<tr class="even">
<td ><p>Width</p></td>
<td ><p>Read/write</p></td>
<td ><p>Returns or sets the width of an object.</p></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ole2disp.dll; </dt> <dt>Oleaut32.dll</dt> </dl> |



 

 
