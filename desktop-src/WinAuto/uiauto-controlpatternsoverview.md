---
title: UI Automation Control Patterns Overview
description: A control pattern is an interface implementation that exposes a particular aspect of a controls functionality to Microsoft UI Automation client applications.
ms.assetid: fdac2b9f-916a-495a-b187-c4d8086319ff
keywords:
- UI Automation,control patterns overview
- UI Automation,dynamic control patterns
- control patterns,about
- control patterns,components
- control patterns,clients
- control patterns,providers
- control patterns,dynamic
- control patterns,interfaces
- interfaces,control patterns
- clients,control patterns
- dynamic control patterns
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UI Automation Control Patterns Overview

A *control pattern* is an interface implementation that exposes a particular aspect of a control's functionality to Microsoft UI Automation client applications. Clients use the properties and methods exposed through a control pattern to retrieve information about a particular capability of the control, or to manipulate a particular aspect of the control's behavior. For example, a control that presents a tabular interface uses the [Grid](uiauto-implementinggrid.md) control pattern to expose the number of rows and columns in the table, and to enable a client to retrieve items from the table.

UI Automation uses control patterns to represent common control behaviors. For example, you use the [Invoke](uiauto-implementinginvoke.md) control pattern for controls that can be invoked, such as buttons, and the [Scroll](uiauto-implementingscroll.md) control pattern for controls that have scroll bars, such as list boxes, list views, or combo boxes. Because each control pattern represents a separate functionality, control patterns can be combined to describe the full set of functionality supported by a particular control.

> [!Note]  
> An aggregate control is built with child controls that provide the user interface for functionality that is exposed by the parent, and the parent should implement all control patterns that are typically associated with its child controls. In turn, those same control patterns are not required to be implemented by the child controls.

 

This topic contains the following sections:

-   [UI Automation Control Pattern Components](#ui-automation-control-pattern-components)
-   [Control Patterns in Providers and Clients](#control-patterns-in-providers-and-clients)
-   [Dynamic Control Patterns](#dynamic-control-patterns)
-   [Control Patterns and Related Interfaces](#control-patterns-and-related-interfaces)
-   [Related topics](#related-topics)

## UI Automation Control Pattern Components

Control patterns support methods, properties, events, and relationships that are required to define a discrete piece of functionality available in a control.

-   The methods allow UI Automation clients to manipulate the control.
-   The properties and events provide information about the functionality and state of the control.
-   The relationship between a UI Automation element and its parent, children, and siblings describes the element structure in the UI Automation tree.

Control patterns relate to controls similar to the way interfaces relate to Component Object Model (COM) objects. In COM, you can query an object to ask what interfaces it supports, and then use those interfaces to access functionality. In UI Automation, clients can ask a control which control patterns it supports, and then interact with the control through the properties, methods, events, and structures exposed by the supported control patterns.

## Control Patterns in Providers and Clients

UI Automation providers implement control pattern interfaces to expose the appropriate behavior for a specific piece of functionality that is supported by the control. These interfaces are not directly exposed to clients, but are used by the UI Automation core to implement another set of client interfaces. For example, a provider exposes scrolling functionality to UI Automation through [**IScrollProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iscrollprovider?branch=master), and UI Automation exposes the functionality to clients through [**IUIAutomationScrollPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationscrollpattern?branch=master).

## Dynamic Control Patterns

Some controls do not always support the same set of control patterns. For example, a multiline edit control enables vertical scrolling only when it contains more lines of text than can be displayed in its viewable area. Scrolling is disabled when enough text is removed so that scrolling is no longer required. For this example, [**IUIAutomationScrollPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationscrollpattern?branch=master) is supported dynamically, depending on the how much text is in the edit box.

## Control Patterns and Related Interfaces

The following table describes the UI Automation control patterns. The table also lists the provider interfaces used to implement the control patterns, and the client interfaces used to access them.



| Name                                                          | Provider interface                                                      | Client interface                                                                              | Description                                                                                                                                                                                                                     |
|---------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Annotation](uiauto-implementingannotation.md)               | [**IAnnotationProvider**](https://msdn.microsoft.com/library/windows/desktop/hh448757)           | [**IUIAutomationAnnotationPattern**](https://msdn.microsoft.com/library/windows/desktop/hh437209)           | Used to expose the properties of an annotation in a document, for example comments in the margin that are connected to document text.                                                                                           |
| [Dock](uiauto-implementingdock.md)                           | [**IDockProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-idockprovider?branch=master)                           | [**IUIAutomationDockPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationdockpattern?branch=master)                           | Used for controls that can be docked in a docking container, for example, toolbars or tool palettes.                                                                                                                            |
| [Drag](https://msdn.microsoft.com/library/windows/desktop/hh707348)                       | [**IDragProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-idragprovider?branch=master)                           | [**IUIAutomationDragPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationdragpattern?branch=master)                           | Used to support draggable controls, or controls with draggable items.                                                                                                                                                           |
| [DropTarget](https://msdn.microsoft.com/library/windows/desktop/hh707349)           | [**IDropTargetProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-idroptargetprovider?branch=master)               | [**IUIAutomationDropTargetPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationdroptargetpattern?branch=master)               | Used to support controls that can be the target of a drag-and-drop operation.                                                                                                                                                   |
| [ExpandCollapse](uiauto-implementingexpandcollapse.md)       | [**IExpandCollapseProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider?branch=master)       | [**IUIAutomationExpandCollapsePattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationexpandcollapsepattern?branch=master)       | Used for controls that can be expanded or collapsed, for example, menu items in an application, such as the File menu.                                                                                                          |
| [Grid](uiauto-implementinggrid.md)                           | [**IGridProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-igridprovider?branch=master)                           | [**IUIAutomationGridPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationgridpattern?branch=master)                           | Used for controls that support grid functionality, such as sizing and moving to a specified cell, for example, the large icon view in Windows Explorer or simple tables in Microsoft Office Word.                               |
| [GridItem](uiauto-implementinggriditem.md)                   | [**IGridItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-igriditemprovider?branch=master)                   | [**IUIAutomationGridItemPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationgriditempattern?branch=master)                   | Used for controls that have cells in grids. The individual cells should support the GridItem pattern, for example, each cell in Windows Explorer detail view.                                                                   |
| [Invoke](uiauto-implementinginvoke.md)                       | [**IInvokeProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iinvokeprovider?branch=master)                       | [**IUIAutomationInvokePattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationinvokepattern?branch=master)                       | Used for controls that can be invoked, such as buttons.                                                                                                                                                                         |
| [ItemContainer](uiauto-implementingitemcontainer.md)         | [**IItemContainerProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iitemcontainerprovider?branch=master)         | [**IUIAutomationItemContainerPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationitemcontainerpattern?branch=master)         | Used for controls that can contain other items.                                                                                                                                                                                 |
| [LegacyIAccessible](uiauto-implementinglegacyiaccessible.md) | [**ILegacyIAccessibleProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ilegacyiaccessibleprovider?branch=master) | [**IUIAutomationLegacyIAccessiblePattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern?branch=master) | Used to expose Microsoft Active Accessibility properties and methods to UI Automation clients.                                                                                                                                  |
| [MultipleView](uiauto-implementingmultipleview.md)           | [**IMultipleViewProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-imultipleviewprovider?branch=master)           | [**IUIAutomationMultipleViewPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationmultipleviewpattern?branch=master)           | Used for controls that can switch between multiple representations of the same set of information, data, or children, for example, a list-view control where data is available in thumbnail, tile, icon, list, or detail views. |
| [ObjectModel](uiauto-implementingobjectmodel.md)             | [**IObjectModelProvider**](https://msdn.microsoft.com/library/windows/desktop/hh448776)         | [**IUIAutomationObjectModelPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationobjectmodelpattern?branch=master)             | Used to expose a pointer to the underlying object model of a document. This control pattern allows a client to navigate from a UI Automation element into the underlying object model.                                          |
| [RangeValue](uiauto-implementingrangevalue.md)               | [**IRangeValueProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irangevalueprovider?branch=master)               | [**IUIAutomationRangeValuePattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationrangevaluepattern?branch=master)               | Used for controls that have a range of values. For example, a spinner control that displays years might have a range of 1900—2010, while a spinner control that displays months would have a range of 1—12.                     |
| [Scroll](uiauto-implementingscroll.md)                       | [**IScrollProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iscrollprovider?branch=master)                       | [**IUIAutomationScrollPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationscrollpattern?branch=master)                       | Used for controls that can scroll when there is more information than can be displayed in the viewable area of the control.                                                                                                     |
| [ScrollItem](uiauto-implementingscrollitem.md)               | [**IScrollItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iscrollitemprovider?branch=master)               | [**IUIAutomationScrollItemPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationscrollitempattern?branch=master)               | Used for controls that have individual items in a list that scrolls, for example, a list control in a combo box control.                                                                                                        |
| [Selection](uiauto-implementingselection.md)                 | [**ISelectionProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionprovider?branch=master)                 | [**IUIAutomationSelectionPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationselectionpattern?branch=master)                 | Used for selection container controls, for example, list boxes and combo boxes.                                                                                                                                                 |
| [SelectionItem](uiauto-implementingselectionitem.md)         | [**ISelectionItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider?branch=master)         | [**IUIAutomationSelectionItemPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationselectionitempattern?branch=master)         | Used for individual items in selection container controls, such as list boxes and combo boxes.                                                                                                                                  |
| [Spreadsheet](uiauto-implementingspreadsheet.md)             | [**ISpreadsheetProvider**](https://msdn.microsoft.com/library/windows/desktop/hh448796)         | [**IUIAutomationSpreadsheetPattern**](https://msdn.microsoft.com/library/windows/desktop/hh437280)         | Used to expose the contents of a spreadsheet or other grid-based document. Controls that implement the Spreadsheet control pattern should also implement the Grid control pattern.                                              |
| [SpreadsheetItem](uiauto-implementingspreadsheetitem.md)     | [**ISpreadsheetItemProvider**](https://msdn.microsoft.com/library/windows/desktop/hh448790) | [**IUIAutomationSpreadsheetItemPattern**](https://msdn.microsoft.com/library/windows/desktop/hh437267) | Used to expose the properties of a cell in a spreadsheet or other grid-based document. Controls that implement the SpreadsheetItem control pattern should also implement the GridItem control pattern.                          |
| [Styles](https://msdn.microsoft.com/library/windows/desktop/hh448775)                   | [**IStylesProvider**](https://msdn.microsoft.com/library/windows/desktop/hh448800)                   | [**IUIAutomationStylesPattern**](https://msdn.microsoft.com/library/windows/desktop/hh437282)                   | Used to describe a UI element that has a specific style, fill color, fill pattern, or shape.                                                                                                                                    |
| [SynchronizedInput](uiauto-implementingsynchronizedinput.md) | [**ISynchronizedInputProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-isynchronizedinputprovider?branch=master) | [**IUIAutomationSynchronizedInputPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationsynchronizedinputpattern?branch=master) | Used for controls that accept keyboard or mouse input.                                                                                                                                                                          |
| [Table](uiauto-implementingtable.md)                         | [**ITableProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-itableprovider?branch=master)                         | [**IUIAutomationTablePattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtablepattern?branch=master)                         | Used for controls that have a grid and header information.                                                                                                                                                                      |
| [TableItem](uiauto-implementingtableitem.md)                 | [**ITableItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-itableitemprovider?branch=master)                 | [**IUIAutomationTableItemPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtableitempattern?branch=master)                 | Used for items in a table.                                                                                                                                                                                                      |
| [Text](uiauto-implementingtextandtextrange.md)               | [**ITextProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-itextprovider?branch=master)                           | [**IUIAutomationTextPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtextpattern?branch=master)                           | Used for edit controls and documents that expose textual information.                                                                                                                                                           |
| TextEdit                                                      | [**ITextEditProvider**](https://msdn.microsoft.com/library/windows/desktop/dn302166)               | [**IUIAutomationTextEditPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtexteditpattern?branch=master)                   | Used for edit controls that modify text programmatically, for example a control that performs auto-correction or enables input composition.                                                                                     |
| [TextChild](textchild-control-pattern.md)                    | [**ITextChildProvider**](https://msdn.microsoft.com/library/windows/desktop/hh437317)            | [**IUIAutomationTextChildPattern**](https://msdn.microsoft.com/library/windows/desktop/hh437296)             | Used to access an element’s nearest ancestor that supports the Text control pattern.                                                                                                                                            |
| [TextRange](uiauto-implementingtextandtextrange.md)          | [**ITextRangeProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-itextrangeprovider?branch=master)                 | [**IUIAutomationTextRange**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtextrange?branch=master)                               | Used for retrieving textual content, text attributes, and embedded objects from text-based controls such as edit controls and documents.                                                                                        |
| [Toggle](uiauto-implementingtoggle.md)                       | [**IToggleProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-itoggleprovider?branch=master)                       | [**IUIAutomationTogglePattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtogglepattern?branch=master)                       | Used for controls where the state can be toggled, for example, check boxes and checkable menu items.                                                                                                                            |
| [Transform](uiauto-implementingtransform.md)                 | [**ITransformProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-itransformprovider?branch=master)                 | [**IUIAutomationTransformPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtransformpattern?branch=master)                 | Used for controls that can be resized, moved, and rotated. Typical uses for the Transform control pattern are in designers, forms, graphical editors, and drawing applications.                                                 |
| [Value](uiauto-implementingvalue.md)                         | [**IValueProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ivalueprovider?branch=master)                         | [**IUIAutomationValuePattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationvaluepattern?branch=master)                         | Used for controls that have a value that does not lie within a specified range, for example, a date-time picker.                                                                                                                |
| [VirtualizedItem](uiauto-implementingvirtualizeditem.md)     | [**IVirtualizedItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ivirtualizeditemprovider?branch=master)     | [**IUIAutomationVirtualizedItemPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationvirtualizeditempattern?branch=master)     | Used for controls that work with items in a virtual list.                                                                                                                                                                       |
| [Window](uiauto-implementingwindow.md)                       | [**IWindowProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iwindowprovider?branch=master)                       | [**IUIAutomationWindowPattern**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationwindowpattern?branch=master)                       | Used for windows. Examples are top-level application windows, multiple-document interface (MDI) child windows, and dialog boxes.                                                                                                |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Implementing UI Automation Control Patterns](uiauto-implementinguiautocontrolpatterns.md)
</dt> <dt>

[Control Pattern Mapping for UI Automation Clients](uiauto-controlpatternmapping.md)
</dt> </dl>

 

 




