---
title: Deprecated Control Pattern Functions
description: Deprecated Control Pattern Functions
ms.assetid: 06434b07-7592-4909-8c4e-064382bdbf98
ms.topic: reference
ms.date: 05/31/2018
---

# Deprecated Control Pattern Functions

> [!Note]  
> The control pattern functions described in this section are deprecated. Client applications should use the Component Object Model (COM) interfaces described in the following sections:
>
> -   [UI Automation Element Interfaces for Clients](uiauto-entry-uiautoclientinterfaces.md)
> -   [Property Condition Interface for Clients](uiauto-client-propconditioninterfaces.md)
> -   [Control Pattern Interfaces for Clients](uiauto-client-controlpatterninterfaces.md)
> -   [Event Handling Interfaces for Clients](uiauto-client-eventhandlinginterfaces.md)
> -   [Proxy Factory Interfaces for Clients](uiauto-client-proxyfactoryinterfaces.md)

 

## In this section




| Function | Description | 
|----------|-------------|
| [**DockPattern_SetDockPosition**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-dockpattern_setdockposition)<br> |  **Note:** This function is deprecated. Client applications should use the Microsoft UI Automation COM interfaces instead.<br> Docks the UI Automation element at the requested **dockPosition** within a docking container.<br> | 
| [**ExpandCollapsePattern_Collapse**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-expandcollapsepattern_collapse)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Hides all descendant nodes, controls, or content of the UI Automation element.<br> | 
| [**ExpandCollapsePattern_Expand**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-expandcollapsepattern_expand)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Expands a control on the screen so that it shows more information.<br> | 
| [**GridPattern_GetItem**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-gridpattern_getitem)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets the node for an item in a grid.<br> | 
| [**InvokePattern_Invoke**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-invokepattern_invoke)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Sends a request to activate a control and initiate its single, unambiguous action.<br> | 
| [**ItemContainerPattern_FindItemByProperty**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-itemcontainerpattern_finditembyproperty)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves a node within a containing node, based on a specified property value.<br> | 
| [**LegacyIAccessiblePattern_DoDefaultAction**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-legacyiaccessiblepattern_dodefaultaction)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Performs the Microsoft Active Accessibility default action for the element.<br> | 
| [**LegacyIAccessiblePattern_GetIAccessible**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-legacyiaccessiblepattern_getiaccessible)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object that corresponds to the UI Automation element.<br> | 
| [**LegacyIAccessiblePattern_Select**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-legacyiaccessiblepattern_select)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Performs a Microsoft Active Accessibility selection.<br> | 
| [**LegacyIAccessiblePattern_SetValue**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-legacyiaccessiblepattern_setvalue)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Sets the Microsoft Active Accessibility value property for the node.<br> | 
| [**MultipleViewPattern_GetViewName**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-multipleviewpattern_getviewname)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the name of a control-specific view.<br> | 
| [**MultipleViewPattern_SetCurrentView**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-multipleviewpattern_setcurrentview)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Sets a control to a different layout.<br> | 
| [**RangeValuePattern_SetValue**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-rangevaluepattern_setvalue)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Sets the value of a control that has a numerical range.<br> | 
| [**ScrollItemPattern_ScrollIntoView**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-scrollitempattern_scrollintoview)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Scrolls the content area of a container object in order to display the UI Automation element within the visible region (viewport) of the container.<br> | 
| [**ScrollPattern_Scroll**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-scrollpattern_scroll)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Scrolls the currently visible region of the content area the specified [**ScrollAmount**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-scrollamount), horizontally, vertically, or both.<br> | 
| [**ScrollPattern_SetScrollPercent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-scrollpattern_setscrollpercent)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Scrolls a container to a specific position horizontally, vertically, or both.<br> | 
| [**SelectionItemPattern_AddToSelection**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-selectionitempattern_addtoselection)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Adds an unselected element to a selection in a control.<br> | 
| [**SelectionItemPattern_RemoveFromSelection**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-selectionitempattern_removefromselection)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Removes an element from the selection in a selection container.<br> | 
| [**SelectionItemPattern_Select**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-selectionitempattern_select)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Selects an element in a selection container.<br> | 
| [**SynchronizedInputPattern_Cancel**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-synchronizedinputpattern_cancel)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Causes the UI Automation provider to stop listening for mouse or keyboard input.<br> | 
| [**SynchronizedInputPattern_StartListening**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-synchronizedinputpattern_startlistening)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Causes the UI Automation provider to start listening for mouse or keyboard input.<br> | 
| [**TextPattern_get_DocumentRange**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textpattern_get_documentrange)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets the text range for the entire document.<br> | 
| [**TextPattern_get_SupportedTextSelection**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textpattern_get_supportedtextselection)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Ascertains whether the text container's contents can be selected and deselected.<br> | 
| [**TextPattern_GetSelection**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textpattern_getselection)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets the current range of selected text from a text container supporting the text pattern.<br> | 
| [**TextPattern_GetVisibleRanges**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textpattern_getvisibleranges)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves an array of disjoint text ranges from a text container where each text range begins with the first partially visible line through to the end of the last partially visible line. For example, a multi-column layout where the columns are partially scrolled out of the visible area of the viewport and the content flows from the bottom of one column to the top of the next.<br> | 
| [**TextPattern_RangeFromChild**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textpattern_rangefromchild)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets the text range that a given node spans.<br> | 
| [**TextPattern_RangeFromPoint**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textpattern_rangefrompoint)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the degenerate (empty) text range nearest to the specified screen coordinates.<br> | 
| [**TextRange_AddToSelection**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_addtoselection)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Adds to the existing collection of highlighted text in a text container that supports multiple, disjoint selections by highlighting supplementary text corresponding to the calling text range **Start** and **End** endpoints.<br> | 
| [**TextRange_Clone**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_clone)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Copies a text range.<br> | 
| [**TextRange_Compare**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_compare)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Compares two text ranges.<br> | 
| [**TextRange_CompareEndpoints**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_compareendpoints)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Returns a value indicating whether two text ranges have identical endpoints.<br> | 
| [**TextRange_ExpandToEnclosingUnit**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_expandtoenclosingunit)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Expands the text range to a larger or smaller unit such as Character, Word, Line, or Page.<br> | 
| [**TextRange_FindAttribute**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_findattribute)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Searches in a specified direction for the first piece of text supporting a specified text attribute.<br> | 
| [**TextRange_FindText**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_findtext)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Returns the first text range in the specified direction that contains the text the client is searching for.<br> | 
| [**TextRange_GetAttributeValue**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_getattributevalue)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Gets the value of an text attribute for a text range.<br> | 
| [**TextRange_GetBoundingRectangles**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_getboundingrectangles)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Retrieves the minimum number of bounding rectangles that can enclose the range, one rectangle per line.<br> | 
| [**TextRange_GetChildren**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_getchildren)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Returns all UI Automation elements contained within the specified text range.<br> | 
| [**TextRange_GetEnclosingElement**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_getenclosingelement)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Returns the node for the next smallest provider that covers the range.<br> | 
| [**TextRange_GetText**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_gettext)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Returns the text in a text range, up to a specified number of characters.<br> | 
| [**TextRange_Move**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_move)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Moves the text range the specified number of units requested by the client.<br> | 
| [**TextRange_MoveEndpointByRange**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_moveendpointbyrange)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Moves an endpoint of one range to the endpoint of another range.<br> | 
| [**TextRange_MoveEndpointByUnit**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_moveendpointbyunit)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Moves an endpoint of the range the specified number of units.<br> | 
| [**TextRange_RemoveFromSelection**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_removefromselection)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Removes the selected text, corresponding to the calling text range **TextPatternRangeEndpoint_Start** and **TextPatternRangeEndpoint_End** endpoints, from an existing collection of selected text in a text container that supports multiple, disjoint selections.<br> | 
| [**TextRange_ScrollIntoView**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_scrollintoview)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Scrolls the text so the specified range is visible in the viewport.<br> | 
| [**TextRange_Select**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-textrange_select)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Selects a text range.<br> | 
| [**TogglePattern_Toggle**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-togglepattern_toggle)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Toggles a control to its next supported state.<br> | 
| [**TransformPattern_Move**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-transformpattern_move)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Moves an element to a specified location on the screen.<br> | 
| [**TransformPattern_Resize**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-transformpattern_resize)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Resizes an element on the screen.<br> | 
| [**TransformPattern_Rotate**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-transformpattern_rotate)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Rotates an element on the screen.<br> | 
| [**ValuePattern_SetValue**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-valuepattern_setvalue)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Sets the text value of an element.<br> | 
| [**VirtualizedItemPattern_Realize**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-virtualizeditempattern_realize)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Makes the virtual item fully accessible as a UI Automation element.<br> | 
| [**WindowPattern_Close**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-windowpattern_close)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Closes an open window.<br> | 
| [**WindowPattern_SetWindowVisualState**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-windowpattern_setwindowvisualstate)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Sets the visual state of a window; for example, to maximize a window.<br> | 
| [**WindowPattern_WaitForInputIdle**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-windowpattern_waitforinputidle)<br> |  **Note:** This function is deprecated. Client applications should use the UI Automation COM interfaces instead.<br> Causes the calling code to block for the specified time or until the associated process enters an idle state, whichever completes first.<br> | 




 

## Related topics

<dl> <dt>

[UI Automation Clients](uiauto-entry-uiautoclientsforwin32apps.md)
</dt> </dl>

 

 





