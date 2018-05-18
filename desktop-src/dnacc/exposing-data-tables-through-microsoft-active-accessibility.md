---
Description: Microsoft Corporation
ms.assetid: '9c09fccf-c591-44f9-b6e5-408826a1d33c'
title: Exposing Data Tables through Microsoft Active Accessibility
---

# Exposing Data Tables through Microsoft Active Accessibility

Microsoft Corporation

April 2002

**Summary**: This article explains how to use the Microsoft Active Accessibility [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface to expose data table information to assistive technologies. This article assumes that you are familiar with the Active Accessibility 2.0 architecture. (19 printed pages)

-   [Introduction](#introduction)
-   [Exposing Data Table Information](#exposing-data-table-information)
    -   [IAccessible Object Roles for Data Tables](#iaccessible-object-roles-for-data-tables)
    -   [IAccessible Data Table Hierarchy Overview](#iaccessible-data-table-hierarchy-overview)
    -   [IAccessible Methods and Properties for Data Tables](#iaccessible-methods-and-properties-for-data-tables)
    -   [IAccessible::get\_accDescription Alternatives](#iaccessibleget-accdescription-alternatives)
    -   [IAccessible::acc\_Navigate Additional Information](#iaccessibleacc-navigate-additional-information)
    -   [Supporting Events](#supporting-events)
    -   [Implementing a Data Table](#implementing-a-data-table)
    -   [Data Table Example Overview](#data-table-example-overview)
    -   [Example of Event Support](#example-of-event-support)
-   [Additional References](#additional-references)

## Introduction

Microsoft Active Accessibility version 2.0 defines a consistent way to expose accessibility information about an application's user interface elements. Assistive technologies collect this information and present it to users as needed.

Because Active Accessibility does not currently support data tables, many assistive technology vendors (ATVs) extract data table information directly from the application's native object model. This technique is time consuming, requires the use of class name-based special casing for each application, and must be updated every time a new application is released.

Currently, Microsoft recommends that application developers use the MSHTML.dll or Microsoft Excel object models to expose data table information in server applications. Both technologies are proven and already supported by many ATVs. However, application developers who cannot support these models need an alternative solution. Microsoft recommends using the Active Accessibility [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface as an interim solution that will enable assistive technologies to collect data table information, navigate the table, and receive notification when information in the table changes. **IAccessible** provides the least complicated and most complete way to support data tables, until a permanent solution is developed.

## Exposing Data Table Information

Microsoft recommends that you use the existing MSHTML.dll or Excel object model to expose data table information to assistive technologies. However, for application developers who cannot support these models, an alternative solution is to use the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466)interface implementation described in this article.

The [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface provides a suitable alternative solution because it uses a well-known set of methods and properties to convey information about user interface elements to assistive technologies. The Active Accessibility [**ITextStore\***](https://msdn.microsoft.com/library/windows/desktop/ms629037) interfaces are designed to expose rich text information, such as documents. However, the **IAccessible** properties and methods are more appropriate for table-based data.

> [!Note]  
> [**ITextStore\***](https://msdn.microsoft.com/library/windows/desktop/ms629037) documents containing embedded data tables can support this [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) implementation.

 

The following sections discuss the implementation of Active Accessibility for data tables, describe the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object roles, present the **IAccessible** data table hierarchy, and define the **IAccessible** methods, properties, and events.

### IAccessible Object Roles for Data Tables

Use the following [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object role constants to define the data table hierarchy in server applications. Note that each constant is followed by its abbreviated convention, which is used throughout the remainder of the article:



| Term                                                                                                                                                                                                                                           | Description                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ROLE_SYSTEM_TABLE__or_Table_"></span><span id="role_system_table__or_table_"></span><span id="ROLE_SYSTEM_TABLE__OR_TABLE_"></span>ROLE\_SYSTEM\_TABLE (or Table)<br/>                                                         | An object that represents a table containing rows and columns of cells, and optionally, row headers and column headers.<br/>                                              |
| <span id="ROLE_SYSTEM_ROW__or_Row_"></span><span id="role_system_row__or_row_"></span><span id="ROLE_SYSTEM_ROW__OR_ROW_"></span>ROLE\_SYSTEM\_ROW (or Row)<br/>                                                                         | An object that represents a row of cells within a table.<br/>                                                                                                             |
| <span id="ROLE_SYSTEM_COLUMNHEADER__or_ColumnHeader_"></span><span id="role_system_columnheader__or_columnheader_"></span><span id="ROLE_SYSTEM_COLUMNHEADER__OR_COLUMNHEADER_"></span>ROLE\_SYSTEM\_COLUMNHEADER (or ColumnHeader)<br/> | An object that represents a column header that provides a visual label for a column in a table.<br/>                                                                      |
| <span id="ROLE_SYSTEM_ROWHEADER__or_RowHeader_"></span><span id="role_system_rowheader__or_rowheader_"></span><span id="ROLE_SYSTEM_ROWHEADER__OR_ROWHEADER_"></span>ROLE\_SYSTEM\_ROWHEADER (or RowHeader)<br/>                         | An object that represents a row header that provides a visual label for a row in a table.<br/>                                                                            |
| <span id="ROLE_SYSTEM_CELL__or_Cell_"></span><span id="role_system_cell__or_cell_"></span><span id="ROLE_SYSTEM_CELL__OR_CELL_"></span>ROLE\_SYSTEM\_CELL (or Cell)<br/>                                                                 | An object that represents a cell within a table.<br/>                                                                                                                     |
| <span id="ROLE_SYSTEM_COLUMN"></span><span id="role_system_column"></span>ROLE\_SYSTEM\_COLUMN<br/>                                                                                                                                      | An object that represents a column of cells within a table. The ROLE\_SYSTEM\_COLUMN role is not used because only a row-based table is presented for this solution.<br/> |



 

### IAccessible Data Table Hierarchy Overview

This article focuses on common row-based tables, and defines the data table structure as a grid of columns, rows, and cells. Cells are restricted to one column of one row. Summary text, if available, is exposed on the overall Table object.

The following tree represents an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) data table hierarchy.

``` syntax
ROLE_SYSTEM_TABLE
  |- ROLE_SYSTEM_ROW
  |  |- ROLE_SYSTEM_ROWHEADER
  |  |- ROLE_SYSTEM_COLUMNHEADER
  |  |- ROLE_SYSTEM_COLUMNHEADER
  |  |- ROLE_SYSTEM_COLUMNHEADER
  |     '- ..
  |- ROLE_SYSTEM_ROW
  |  |- ROLE_SYSTEM_ROWHEADER
  |  |- ROLE_SYSTEM_CELL
  |  |- ROLE_SYSTEM_CELL
  |  |- ROLE_SYSTEM_CELL
  |   '- ..
  |- ROLE_SYSTEM_ROW
  |  |- ROLE_SYSTEM_ROWHEADER
  |  |- ROLE_SYSTEM_CELL
  |  |- ROLE_SYSTEM_CELL
  |  |- ROLE_SYSTEM_CELL
  |   '- ..
   '- ..
```

As previously defined, a Table object is a collection of one or more Row objects, where each Row object is the parent of one or more children. A Row object can contain one or more Cell objects. However, all Row objects must have the same number of Cell objects. Although not shown in the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) data table hierarchy, a Cell object is also a container that can have an arbitrarily deep hierarchy of **IAccessible** objects with any valid role. For example, a nested or embedded table is represented by placing a Table object inside a Cell object.

> [!Note]  
> For improved performance, a server application can create an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object on demand, in response to the WM\_GETOBJECT windows message or the [**IAccessible::get\_accChild**](https://msdn.microsoft.com/library/windows/desktop/dd318475) method. After creating an **IAccessible** object, it is managed like any other standard COM object.

 

### IAccessible Methods and Properties for Data Tables

The following tables are organized by object role, and briefly describe the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) methods and properties required to support data tables. In-depth descriptions and implementations are available in the [Microsoft Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=208210). .

[**ROLE\_SYSTEM\_TABLE**](https://msdn.microsoft.com/library/windows/desktop/dd373608#role-system-table)



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IAccessible::accDoDefaultAction</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318470)</td>
<td>Returns DISP_E_MEMBERNOTFOUND; this property is not supported.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::accHitTest</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318471)</td>
<td>Returns the Table object or one of its children based on the screen coordinates.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::accLocation</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318472)</td>
<td>Returns the Table object's current screen location.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::accNavigate</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318473)</td>
<td>The [<strong>IAccessible</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318466) object returned is determined by the navigational constant passed to this method. <br/> Spatial navigation returns a sibling of the Table object. <br/> Logical navigation:<br/>
<ul>
<li>NAVDIR_NEXT or NAVDIR_PREV returns a sibling of the Table object.</li>
<li>NAVDIR_PARENT returns the Table object's parent.</li>
<li>NAVDIR_FIRSTCHILD or NAVDIR_LASTCHILD returns the appropriate Row object.</li>
</ul>
For more information, see [IAccessible::accNavigate Additional Information](#iaccessibleacc-navigate-additional-information).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::accSelect</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318474)</td>
<td>Adds or removes the selection for the entire Table object.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accChild</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318475)</td>
<td>Returns an [<strong>IDispatch</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318520) interface pointer of role type Row for the specified child.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accChildCount</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318476)</td>
<td>Returns the total number of rows.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accDefaultAction</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318477)</td>
<td>Returns DISP_E_MEMBERNOTFOUND; this property is not supported.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accDescription</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318478)</td>
<td>Returns DISP_E_MEMBERNOTFOUND, a string containing the table's summary text, or a string containing the number of rows and columns. <br/> For example, current status and owners of all active documents. Or 6 Rows, 3 Columns.<br/> For more information, see [IAccessible::get_accDescription Alternatives](#iaccessibleget-accdescription-alternatives).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accFocus</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318479)</td>
<td>Returns the descendant of the Table object that has the input focus.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accHelp</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318480)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or a localized string containing the table's Help property string.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accHelpTopic</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318481)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or the full path of the WinHelp file associated with the Table object and the identifier of the appropriate topic within that file.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accKeyboardShortcut</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318482)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or the Table object's shortcut key or access key.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accName</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318483)</td>
<td>Returns a localized string containing the Table object's name or summary text.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accParent</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318484)</td>
<td>Returns the [<strong>IDispatch</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318520) interface of the Table object.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accSelection</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318486)</td>
<td>Returns a collection of selected Cell objects.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accState</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318487)</td>
<td>Returns a bitmask representing the current state of the Table object.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accValue</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318488)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
</tbody>
</table>



 

[**ROLE\_SYSTEM\_ROW**](https://msdn.microsoft.com/library/windows/desktop/dd373608#role-system-row)



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IAccessible::accDoDefaultAction</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318470)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::accHitTest</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318471)</td>
<td>Returns the Row object or one of its children based on a given point on the screen.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::accLocation</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318472)</td>
<td>Returns the Row object's current screen location.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::accNavigate</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318473)</td>
<td>The [<strong>IAccessible</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318466) object returned is determined by the navigational constant passed to this method. <br/> Spatial navigation:<br/>
<ul>
<li>NAVDIR_UP or NAVDIR_DOWN returns another Row object or S_FALSE, if navigating from the top or bottom row, respectively.</li>
<li>NAVDIR_LEFT and NAVDIR_RIGHT always return S_FALSE.</li>
</ul>
Logical navigation:<br/>
<ul>
<li>NAVDIR_PARENT returns the Table object.</li>
<li>NAVDIR_PREV or NAVDIR_NEXT returns another Row object or S_FALSE, if navigating from the first or last Row object, respectively.</li>
<li>NAVDIR_FIRSTCHILD or NAVDIR_LASTCHILD returns a Cell, RowHeader, or ColumnHeader object.</li>
</ul>
For more information, see [IAccessible::accNavigate Additional Information](#iaccessibleacc-navigate-additional-information).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::accSelect</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318474)</td>
<td>Adds or removes a selection on a Row object.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accChild</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318475)</td>
<td>Returns an [<strong>IDispatch</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318520) interface pointer for the specified Cell, ColumnHeader, or RowHeader object.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accChildCount</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318476)</td>
<td>Returns the number of columns in the table.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accDefaultAction</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318477)</td>
<td>Returns DISP_E_MEMBERNOTFOUND; this property is not supported.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accDescription</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318478)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or a localized string containing the summary of a specific Row object's information.<br/> For example, Row3: Sales_Midwest_Q2.doc, Jill, Reviewed.<br/> For more information, see [IAccessible::get_accDescription Alternatives](#iaccessibleget-accdescription-alternatives).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accFocus</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318479)</td>
<td>Returns the descendant of the Row object that has the input focus.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accHelp</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318480)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or a localized string containing the Row object's Help property string.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accHelpTopic</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318481)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or the full path of the WinHelp file associated with the Row object and the identifier of the appropriate topic within that file.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accKeyboardShortcut</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318482)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or the Row object's shortcut key or access key.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accName</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318483)</td>
<td>Returns <strong>NULL</strong>, or a localized descriptive title, such as the &quot;Header Row&quot; or &quot;New Row&quot;.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accParent</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318484)</td>
<td>Returns the [<strong>IDispatch</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318520) interface of the Table object.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accSelection</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318486)</td>
<td>Returns a collection of Cell object's that are selected within the Row object.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accState</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318487)</td>
<td>Returns a bitmask representing the current state of the Row object.<br/> When exposing a large table with rows that may be scrolled out of view, it is important to mark the appropriate cells and rows as STATE_SYSTEM_INVISIBLE, and send the appropriate state change events.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accValue</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318488)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
</tbody>
</table>



 

[**ROLE\_SYSTEM\_COLUMNHEADER**](https://msdn.microsoft.com/library/windows/desktop/dd373608#role-system-columnheader) and [**ROLE\_SYSTEM\_ROWHEADER**](https://msdn.microsoft.com/library/windows/desktop/dd373608#role-system-rowheader)



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IAccessible::accDoDefaultAction</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318470)</td>
<td>Returns DISP_E_MEMBERNOTFOUND; this property is not supported.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::accHitTest</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318471)</td>
<td>Returns the ColumnHeader object, RowHeader object, or one of its children based on a given point on the screen.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::accLocation</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318472)</td>
<td>Returns the ColumnHeader or RowHeader object's current screen location.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::accNavigate</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318473)</td>
<td>The [<strong>IAccessible</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318466) object returned is determined by the navigational constant passed to this method. <br/> Spatial navigation returns a Cell, RowHeader, or ColumnHeader object, or S_FALSE, if no other cell exists in the specified direction.<br/> Logical navigation:<br/>
<ul>
<li>NAVDIR_PARENT returns the parent Row object.</li>
<li>NAVDIR_PREV or NAVDIR_NEXT returns a Cell, RowHeader, or ColumnHeader object, or S_FALSE, if navigating from the first or last cell, respectively, in a row.</li>
<li>NAVDIR_FIRSTCHILD or NAVDIR_LASTCHILD returns a valid child of the RowHeader, or ColumnHeader object, or S_FALSE, if it has no children.</li>
</ul>
For more information, see [IAccessible::accNavigate Additional Information](#iaccessibleacc-navigate-additional-information).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::accSelect</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318474)</td>
<td>Adds or removes the selection, or sets the focus.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accChild</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318475)</td>
<td>Returns an [<strong>IDispatch</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318520) interface pointer for the specified child, if one exists. Depending on the table's implementation, children are not limited to simple text.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accChildCount</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318476)</td>
<td>Returns the number of children that belong to the ColumnHeader or RowHeader object. The column or row header can have more than one child.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accDefaultAction</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318477)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accDescription</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318478)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accFocus</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318479)</td>
<td>Returns the descendant of the ColumnHeader or RowHeader object that has the input focus.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accHelp</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318480)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or a localized string containing the ColumnHeader or RowHeader object's HELP property string.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accHelpTopic</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318481)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or the full path of the WinHelp file associated with a ColumnHeader or RowHeader object and the identifier of the appropriate topic within that file.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accKeyboardShortcut</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318482)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or the ColumnHeader or RowHeader object's shortcut key or access key.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accName</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318483)</td>
<td>Returns a localized string that is visually displayed as the ColumnHeader or RowHeader object.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accParent</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318484)</td>
<td>Returns the [<strong>IDispatch</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318520) interface of the parent Row object.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accSelection</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318486)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accState</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318487)</td>
<td>Returns a bitmask representing the current state of the ColumnHeader or RowHeader object.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accValue</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318488)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
</tbody>
</table>



 

[**ROLE\_SYSTEM\_CELL**](https://msdn.microsoft.com/library/windows/desktop/dd373608#role-system-cell)



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IAccessible::accDoDefaultAction</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318470)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::accHitTest</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318471)</td>
<td>Returns the Cell object or one of its children based on a given point on the screen.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::accLocation</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318472)</td>
<td>Returns the Cell object's current screen location.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::accNavigate</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318473)</td>
<td>The [<strong>IAccessible</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318466) object returned is determined by the navigational constant passed to this method. Spatial navigation returns a Cell object, RowHeader object, ColumnHeader object or S_FALSE if no other cell exists in the specified direction. <br/> Logical navigation:<br/>
<ul>
<li>NAVDIR_PARENT returns the parent Row object.</li>
<li>NAVDIR_PREV or NAVDIR_NEXT returns a Cell, or RowHeader object, or S_FALSE if navigating from the first or last cell, respectively, in a row.</li>
<li>NAVDIR_FIRSTCHILD or NAVDIR_LASTCHILD returns a valid child of the Cell object, or S_FALSE if it has no children.</li>
</ul>
For more information, see [IAccessible::accNavigate Additional Information](#iaccessibleacc-navigate-additional-information).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::accSelect</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318474)</td>
<td>Adds or removes selection, or sets focus for a particular Cell object.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accChild</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318475)</td>
<td>Returns an [<strong>IDispatch</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318520) interface pointer for the specified child, if one exists. However, children are not limited to simple text.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accChildCount</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318476)</td>
<td>Returns the number of children that belong to the Cell object. A Cell object can have more than one child.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accDefaultAction</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318477)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accDescription</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318478)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or a localized string containing a summary of specific ColumnHeader and RowHeader object information.<br/> For example: 2, Status.<br/> For more information, see [IAccessible::get_accDescription Alternatives](#iaccessibleget-accdescription-alternatives). <br/></td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accFocus</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318479)</td>
<td>Returns the Cell object, or one of its descendants, that has the input focus.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accHelp</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318480)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or a localized string containing the Cell object's Help property string.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accHelpTopic</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318481)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or the full path of the WinHelp file related to the Cell, and the appropriate topic's identifier located within that file.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accKeyboardShortcut</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318482)</td>
<td>Returns DISP_E_MEMBERNOTFOUND or a Cell object's shortcut key or access key.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accName</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318483)</td>
<td>Returns a string that represents the Cell object's location within the data table.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accParent</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318484)</td>
<td>Returns the [<strong>IDispatch</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318520) interface for the parent Row object.</td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accSelection</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318486)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
<tr class="odd">
<td>[<strong>IAccessible::get_accState</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318487)</td>
<td>Returns STATE_SYSTEM_FOCUSED, STATE_SYSTEM_FOCUSABLE, STATE_SYSTEM_INVISIBLE, STATE_SYSTEM_OFFSCREEN, STATE_SYSTEM_SELECTABLE, STATE_SYSTEM_SELECTED, STATE_SYSTEM_MULTISELECTABLE, or according to your implementation, additional states as defined within the [Microsoft Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=208210).<br/> When exposing a large table with rows that may be scrolled out of view, it is important to mark the appropriate cells and rows as STATE_SYSTEM_INVISIBLE, and send the appropriate state change events.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAccessible::get_accValue</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318488)</td>
<td>Returns DISP_E_MEMBERNOTFOUND. This property is not supported.</td>
</tr>
</tbody>
</table>



 

### IAccessible::get\_accDescription Alternatives

Supporting the [**IAccessible::get\_accDescription**](https://msdn.microsoft.com/library/windows/desktop/dd318478) method for data table elements is optional. However, when compared to the alternatives listed below, supporting the **IAccessible::get\_accDescription** method involves less development work.

If you choose not to implement the [**IAccessible::get\_accDescription**](https://msdn.microsoft.com/library/windows/desktop/dd318478) method, then ATVs will have to use the following approaches to obtain the same information:

-   To find the number of rows in the data table, they will call [**IAccessible::get\_accChildCount**](https://msdn.microsoft.com/library/windows/desktop/dd318476) on the Table object.
-   To find the number of columns in the data table, they will call [**IAccessible::get\_accChildCount**](https://msdn.microsoft.com/library/windows/desktop/dd318476) on any of the Row objects.
-   To find individual row summary information, they will access each child object of that row.
-   To find row header information for a Cell object, they will locate the sibling RowHeader object and query its children for the desired information. In most cases the RowHeader object will be the first child of the Row object, and can be reached by calling the [**IAccessible::accNavigate**](https://msdn.microsoft.com/library/windows/desktop/dd318473) (the Cell object's Parent ID, NAVDIR\_FIRSTCHILD) method.
-   To find the column header information for a Cell object, they will locate the appropriate ColumnHeader object and query its children for the desired information. To locate a ColumnHeader object from a Cell object, they call [**IAccessible::accNavigate**](https://msdn.microsoft.com/library/windows/desktop/dd318473) (CHILDID\_SELF, NAVDIR\_UP) repeatedly until a ColumnHeader object is returned.

### IAccessible::acc\_Navigate Additional Information

Spatial navigation allows a client to traverse an object's [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) hierarchy using constants that represent direction: NAVDIR\_UP, NAVDIR\_DOWN, NAVDIR\_LEFT, and NAVDIR\_RIGHT. Typically, spatial navigation can be used only to move between siblings in the **IAccessible** hierarchy. In a dialog box, this means spatial navigation can be used to move from one control to another, but not from a control in the dialog box to another control in an adjacent dialog box. If this rule were applied to Table objects, spatial navigation would be restricted to movement within a single cell or row. The NAVDIR\_UP and NAVDIR\_DOWN navigation constants would be supported only on Rowobjects. Because spatial navigation between Cell objects is a common scenario, Table objects deviate from this convention and support spatial navigation between containers.

### Supporting Events

Active Accessibility relies on Window Events (WinEvents) to notify clients of changes in an application's user interface. The following table provides a brief overview of the WinEvents that are most relevant for data tables. For more information, see [WinEvents](https://msdn.microsoft.com/library/windows/desktop/dd373889).

**IAccessible Events for Data Tables**



| Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EVENT\_OBJECT\_CREATE          | Event is sent as [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466)objects are created, as a row or column is added to the table. Based on the previous data table definition, a cell will never be created without a Row object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| EVENT\_OBJECT\_DESTROY         | Event is sent as [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) objects are removed. If the parent Cell or Row object is destroyed, it does not need to be sent for the individual Cell objects or their child objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| EVENT\_OBJECT\_REORDER         | Event is sent for the Table object when its descendants (Row or Cell objects) are reorganized, due to sorting or moving of the table's rows or columns.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| EVENT\_OBJECT\_FOCUS           | Event is sent, for a Cell object or one of its children, if the user moves the input focus to a new Cell object. Assistive technologies can access information from the children of a Cell object in order to report the contents to the user. If the user moves focus into the contents of the Cell object, then EVENT\_OBJECT\_FOCUS is sent for the appropriate [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) child of that Cell object.                                                                                                                                                                                                                                                                                                     |
| EVENT\_OBJECT\_SELECTION       | Event is sent as a user moves from cell to cell. It also occurs if the selection is programmatically changed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| EVENT\_OBJECT\_SELECTIONADD    | Event is sent for tables that support multiselection, when the SHIFT + ARROW key combinations are used to increase the selection by Rows or by Cells. It also occurs if the selection is programmatically changed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| EVENT\_OBJECT\_SELECTIONREMOVE | Event is sent for tables that support multiselection, when the SHIFT + ARROW keys are used to decrease the selection by Rows or Cells. It also occurs if the selection is programmatically changed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| EVENT\_OBJECT\_SELECTIONWITHIN | Event is sent on the Table object, if the selected items within the table have significantly changed. It is used instead of sending several EVENT\_OBJECT\_SELECTIONADD, or EVENT\_OBJECT\_SELECTIONREMOVE events. It also occurs if the selection is programmatically changed.<br/> Microsoft Active Accessibility 2.0 servers can define a significant change as more than 20 cells.<br/> If a small number of cells are selected as a result of a column or row being selected, an EVENT\_OBJECT\_SELECTION event occurs on the first cell within that row or column, and the EVENT\_OBJECT\_SELECTIONADD event occurs on each additional cell. The reverse is true for EVENT\_OBJECT\_SELECTIONREMOVE events.<br/> |
| EVENT\_OBJECT\_STATECHANGE     | Event is sent as the [**IAccessible::get\_accState**](https://msdn.microsoft.com/library/windows/desktop/dd318487)method is changed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |



 

> [!Note]  
> The *hwnd* and *idObject* parameters of the [*WinEventProc*](https://msdn.microsoft.com/library/windows/desktop/dd373885) callback function describe the container, while the *idChild* parameter identifies the event-related object.

 

### Implementing a Data Table

Figure 1 illustrates a data table that tracks business documentation for customers and employees. It is a general solution that does not rely on a specific HWND or native object model support.

In this example, only the input cells have focusable, selectable, and multi-selectable states. The column headers — File Name, Owner and Status — and the row headers — 1, 2, 3, 4 and \* — are not focusable.

![figure 1. data table example](images/atg-msaasupportfortables-01.png)

### Data Table Example Overview

The following criteria are used to define the hierarchy in Figure 1. First, the role of an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466)object is defined. Second, the state of an **IAccessible** object appears in square brackets. Third, the name of an **IAccessible** object appears in bold italics. Finally, if needed, the value of an **IAccessible** object appears in double quotes.

The following is the tree view of the data table hierarchy associated with Figure 1.

``` syntax
ROLE_SYSTEM_TABLE <b><i>"Project Status"
</i></b> |- ROLE_SYSTEM_ROW [STATE_SYSTEM_SELECTABLE,
 |  |        STATE_SYSTEM_MULTISELECTABLE] <b><i>"Header Row"
</i></b> |  |- ROLE_SYSTEM_ROWHEADER <b><i>""
</i></b> |  |     '- ROLE_SYSTEM_PUSHBUTTON <b><i>"SelectThe Entire Table"
</i></b> |  |- ROLE_SYSTEM_COLUMNHEADER <b><i>"Column1"
</i></b> |  |     '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_READONLY] <b><i>"File Name"
</i></b> |  |- ROLE_SYSTEM_COLUMNHEADER <b><i>"Column 2"
</i></b> |  |     '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_READONLY] <b><i>"Owner"
</i></b> |     '- ROLE_SYSTEM_COLUMNHEADER <b><i>"Column 3"
</i></b> |          '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_READONLY] <b><i>"Status"
</i></b> |- ROLE_SYSTEM_ROW [STATE_SYSTEM_SELECTABLE,
 |  |        STATE_SYSTEM_MULTISELECTABLE] <b><i>""
</i></b> |  |- ROLE_SYSTEM_ROWHEADER <b><i>"1"
</i></b> |  |    '- ROLE_SYSTEM_PUSHBUTTON <b><i>"Select This Row"
</i></b> |  |- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE,
 |  |    |     STATE_SYSTEM_MULTISELECTABLE, STATE_SYSTEM_FOCUSABLE]   <b><i>"Row 1, Column 1"
</i></b> |  |    '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_FOCUSABLE] <b><i>"Midyear review.doc"
</i></b> |  |- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE,
 |  |   |      STATE_SYSTEM_MULTISELECTABLE, STATE_SYSTEM_FOCUSABLE] <b><i>"Row 1, Column 2"
</i></b> |  |    '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_FOCUSABLE] <b><i>"Jim"
</i></b> |  '- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE,
 |    |   STATE_SYSTEM_MULTISELECTABLE, STATE_SYSTEM_FOCUSABLE] <b><i>"Row 1, Column 3"
</i></b> |         |- ROLE_SYSTEM_STATICTEXT [STATE_SYSTEM_FOCUSABLE]<i> <b>"Completed"
</b></i> |          '- ROLE_SYSTEM_COMBOBOX [STATE_SYSTEM_INVISIBLE,
 |              |         STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"</i></b> "Completed"
 |              |- ROLE_SYSTEM_STATICTEXT [STATE_SYSTEM_INVISIBLE,
 |              |         STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"</i></b> "Completed"
 |              |- ROLE_SYSTEM_PUSHBUTTON [STATE_SYSTEM_INVISIBLE,
 |              |         STATE_SYSTEM_FOCUSABLE]<i> <b>"Open"
</b></i> |               '- ROLE_SYSTEM_LIST [STATE_SYSTEM_INVISIBLE,
 |                   |         STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"
</i></b> |                   |- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_INVISIBLE,
 |                   |         STATE_SYSTEM_FOCUSABLE] <b><i>"Draft"
</i></b> |                   |- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_INVISIBLE,
 |                   |         STATE_SYSTEM_FOCUSABLE] <b><i>"Reviewed"
</i></b> |                    '- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_INVISIBLE,
 |                              STATE_SYSTEM_FOCUSABLE] <b><i>"Completed"
</i></b> |- ROLE_SYSTEM_ROW [STATE_SYSTEM_SELECTABLE,
 |    |        STATE_SYSTEM_MULTISELECTABLE] <b>""
</b> |    |- ROLE_SYSTEM_ROWHEADER <b><i>"2"
</i></b> |    |    |    '- ROLE_SYSTEM_PUSHBUTTON <b><i>"Select This Row"
</i></b> |    |- ROLE_SYSTEM_CELL [STATE_SYSTEM_FOCUSABLE,
 |    |    |        STATE_SYSTEM_SELECTABLE, STATE_SYSTEM_MULTISELECTABLE]
 |    |    |         <b><i>"Row 2, Column 1"
</i></b> |    |     '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_FOCUSABLE] <b><i>"customer visit.doc"
</i></b> |    |- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE,
 |    |   |          STATE_SYSTEM_MULTISELECTABLE, STATE_SYSTEM_FOCUSABLE] <b><i>"Row 2, Column 2"
</i></b> |    |    '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_FOCUSABLE] <b><i>"Jim"
          </i></b> |  '- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE,
           STATE_SYSTEM_MULTISELECTABLE,       |
           STATE_SYSTEM_FOCUSABLE]     <b><i>"Row 2, Column 3"
</i></b> |         |- ROLE_SYSTEM_STATICTEXT [STATE_SYSTEM_INVISIBLE,
 |         |         STATE_SYSTEM_FOCUSABLE]<i> <b>"Draft"
</b></i> |          '- ROLE_SYSTEM_COMBOBOX [STATE_SYSTEM_FOCUSABLE] <b><i>"Status:" </i></b>"Draft"
 |              |- ROLE_SYSTEM_STATICTEXT [STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"</i></b> "Draft"
 |              |- ROLE_SYSTEM_PUSHBUTTON [STATE_SYSTEM_FOCUSABLE]<i><b>"Open"
</b></i> |               '- ROLE_SYSTEM_LIST [STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"
</i></b> |                   |- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_FOCUSABLE, STATE_SYSTEM_FOCUSED] <b><i>"Draft"
</i></b> |                   |- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_FOCUSABLE] <b><i>"Reviewed"
</i></b> |                    '- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_FOCUSABLE] <b><i>"Completed"
</i></b> |- ROLE_SYSTEM_ROW [STATE_SYSTEM_SELECTABLE, STATE_SYSTEM_MULTISELECTABLE] <b>""
</b> |    |              |   |- ROLE_SYSTEM_ROWHEADER <b><i>"3"
</i></b> |    |    '- ROLE_SYSTEM_PUSHBUTTON <b><i>"Select This Row"
</i></b> |    |- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE, STATE_SYSTEM_MULTISELECTABLE,
 |    |    |        STATE_SYSTEM_FOCUSABLE] <b><i>"Row 3, Column 1"
</i></b> |    |     '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_FOCUSABLE] <b><i>"Sales_Midwest_Q2.doc"
</i></b> |    |- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE,
 |    |    |        STATE_SYSTEM_MULTISELECTABLE, STATE_SYSTEM_FOCUSABLE] <b><i>"Row 3, Column 2"
</i></b> |    |     '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_FOCUSABLE] <b><i>"Jill"
</i></b> |     '- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE,
 |         |         STATE_SYSTEM_MULTISELECTABLE, STATE_SYSTEM_FOCUSABLE]
 |         |         <b><i>"Row 3, Column 3"
</i></b> |         |- ROLE_SYSTEM_STATICTEXT [STATE_SYSTEM_FOCUSABLE]<i><b>"Reviewed"
</b></i> |          '- ROLE_SYSTEM_COMBOBOX [STATE_SYSTEM_INVISIBLE,
 |              |         STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"</i></b> "Reviewed"
 |              |- ROLE_SYSTEM_STATICTEXT [STATE_SYSTEM_INVISIBLE,
 |              |         STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"</i></b> "Reviewed"
 |              |- ROLE_SYSTEM_PUSHBUTTON [STATE_SYSTEM_INVISIBLE,
 |              |         STATE_SYSTEM_FOCUSABLE]<i><b>"Open"
</b></i> |               '- ROLE_SYSTEM_LIST [STATE_SYSTEM_INVISIBLE,
 |                   |         STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"
</i></b> |                   |- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_INVISIBLE,
 |                   |         STATE_SYSTEM_FOCUSABLE] <b><i>"Draft"
</i></b> |                   |- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_INVISIBLE,
 |                   |         STATE_SYSTEM_FOCUSABLE] <b><i>"Reviewed"
</i></b> |                    '- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_INVISIBLE,
 |                             STATE_SYSTEM_FOCUSABLE] <b><i>"Completed"
</i></b>   '- ROLE_SYSTEM_ROW, STATE_SYSTEM_SELECTABLE,
          |         STATE_SYSTEM_MULTISELECTABLE] <b>""
</b>          |- ROWHEADER [ROLE_SYSTEM_ROWHEADER] <b>"*"
</b>          |     '- ROLE_SYSTEM_PUSHBUTTON <b><i>"Select This Row"</i></b>  
          |- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE,
          |    |         STATE_SYSTEM_MULTISELECTABLE, STATE_SYSTEM_FOCUSABLE] <b><i>"New Row, Column 1"
</i></b>          |     '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_FOCUSABLE] <b>""
</b>          |- ROLE_SYSTEM_CELL, [STATE_SYSTEM_SELECTABLE,
          |    |         STATE_SYSTEM_MULTISELECTABLE, STATE_SYSTEM_FOCUSABLE] <b><i>"New Row, Column 2"
</i></b>          |     '- ROLE_SYSTEM_TEXT [STATE_SYSTEM_FOCUSABLE] <b>""
</b>           '- ROLE_SYSTEM_CELL [STATE_SYSTEM_SELECTABLE,
               |          STATE_SYSTEM_MULTISELECTABLE, STATE_SYSTEM_FOCUSABLE] <b><i>"New Row, Column 3"
</i></b>               |- ROLE_SYSTEM_STATICTEXT [STATE_SYSTEM_FOCUSABLE]<b><i> ""
</i></b>                '- ROLE_SYSTEM_COMBOBOX [STATE_SYSTEM_INVISIBLE,
                    |         STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"</i></b> ""
                    |- ROLE_SYSTEM_STATICTEXT [STATE_SYSTEM_INVISIBLE,
                    |         STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"</i></b> ""
                    |- ROLE_SYSTEM_PUSHBUTTON [STATE_SYSTEM_INVISIBLE,
                    |         STATE_SYSTEM_FOCUSABLE]<i><b>"Open"
</b></i>                     '- ROLE_SYSTEM_LIST [STATE_SYSTEM_INVISIBLE,
                          |        STATE_SYSTEM_FOCUSABLE] <b><i>"Status:"</i></b>
                          |- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_INVISIBLE,
                          |        STATE_SYSTEM_FOCUSABLE] <b><i>"Draft"
</i></b>                          |- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_INVISIBLE,
                          |        STATE_SYSTEM_FOCUSABLE] <b><i>"Reviewed"
</i></b>                           '- ROLE_SYSTEM_LISTITEM [STATE_SYSTEM_INVISIBLE,
                                    STATE_SYSTEM_FOCUSABLE] <b><i>"Completed"</i></b>
```

### Example of Event Support

The following scenario relates to the data table example in Figure 1 and describes the events that occur within it.

1.  The input focus and selection is on the first child (Draft) of a drop-down list box located in the Status column of the second row.
2.  The user navigates in the drop-down list box by using the UP ARROW and DOWN ARROW keys, which changes the input focus and selection.
3.  The EVENT\_OBJECT\_FOCUS and the EVENT\_OBJECT\_SELECTION events are sent, as if the drop-down list box is contained within a traditional dialog box. After the user chooses a selection from the drop-down list box by pressing ENTER, the input focus and selection move back to the parent cell.
4.  As the user navigates in the data table with the LEFT ARROW, RIGHT ARROW, UP ARROW, and DOWN ARROW keys, the EVENT\_OBJECT\_FOCUS and EVENT\_OBJECT\_SELECTION events are sent for each Cell object. Assistive technologies rely on these events to track the input focus and determine which cell's information should be reported to the user.
5.  The user continues to navigate in the data table using the SHIFT+ARROW key combinations to increase or decrease the selection by a single cell or by a small group of cells. The EVENT\_OBJECT\_SELECTIONADD and EVENT\_OBJECT\_SELECTIONREMOVE events are sent along with the EVENT\_OBJECT\_FOCUS event, as the user continues to hold the SHIFT key down and change the input focus.
6.  If the user presses the CTRL+ARROW key combinations in the data table, then the input focus changes. However, the selection remains the same, so only the EVENT\_OBJECT\_FOCUS event is sent for the Cell object that takes focus.
7.  While the input focus is on an individual cell, the user can press a shortcut key to enter the cell and edit its contents. If this happens, the EVENT\_OBJECT\_FOCUS event is sent again for the correct [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) child of that cell.
8.  When the user creates a new row, by navigating to the (\*) Row or 'New Row', then the EVENT\_OBJECT\_CREATE event is sent for the new Row object.
9.  If the data table supports sorting, EVENT\_OBJECT\_REORDER is sent on the Table object when a sort order change has occurred.

## Additional References

See the following references for more information about specific topics discussed in this article:

-   For more information on Microsoft Active Accessibility, see [Microsoft Windows Software Development Kit (SDK)](https://msdn.microsoft.com/library/windows/desktop/dd373592).
-   For more information on the MSHTML Object Model, see [About MSHTML](http://go.microsoft.com/fwlink/p/?linkid=207066).
-   For more information on the Excel Object Model, see [Excel 2010 Developer Reference](http://go.microsoft.com/fwlink/p/?linkid=208265).
-   For more information on [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) creation, see [How to Handle WM\_GETOBJECT](https://msdn.microsoft.com/library/windows/desktop/dd318451).
-   For more information on Active Accessibility Events, see [WinEvents](https://msdn.microsoft.com/library/windows/desktop/dd373889).

 

 




