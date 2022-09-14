---
title: Verification Routines
description: This section describes the verification routines that UI Accessibility Checker can run to test an application's accessibility implementation.
ms.assetid: '0ff38f83-5741-4c0e-a070-a8385f95eba3'
ms.topic: article
ms.date: 05/31/2018
---

# Verification Routines

This section describes the verification routines that UI Accessibility Checker can run to test an application's accessibility implementation.



<table>
<thead>
<tr class="header">
<th>Category</th>
<th>Routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><strong>Consistency</strong>${REMOVE}$<br />
</td>
<td><strong>ScreenReader</strong></td>
<td>Compiles all visible elements in the verification target and displays them in a ListView control in the order that a standard screen reader announces them to a user.</td>
</tr>
<tr class="even">
<td><strong>UiaScreenReader</strong></td>
<td>Same as <strong>ScreenReader</strong>, but for UIA implementations.</td>

</tr>
<tr class="odd">
<td rowspan="2"><strong>Navigation</strong>${REMOVE}$<br />
</td>
<td><strong>CheckTreeDepth</strong></td>
<td>Sends Tab (or Shift+Tab) characters as input to the verification target to confirm that the target's UI isn't overly complex or inaccessible using standard keyboard navigation.</td>
</tr>
<tr class="even">
<td><strong>CheckTabbingUia</strong></td>
<td>Sends Tab (or Shift+Tab) characters as input to the verification target to confirm that all focusable elements in the UI are reachable in an orderly, logical fashion using standard keyboard navigation.</td>

</tr>
<tr class="odd">
<td rowspan="5"><strong>Properties</strong>${REMOVE}$<br />
</td>
<td><strong>CheckRole</strong></td>
<td>Confirms that each focusable element in the UI reports a valid, logical MSAA role, and that the control has a value as required by that role.</td>
</tr>
<tr class="even">
<td><strong>CheckState</strong></td>
<td>Confirms that each focusable element in the UI reports a valid, logical MSAA state.</td>

</tr>
<tr class="odd">
<td><strong>CheckName</strong></td>
<td>Confirms that each focusable element in the UI reports a valid, logical MSAA name.</td>

</tr>
<tr class="even">
<td><strong>CheckAccessKeys</strong></td>
<td>Confirms that access keys that are assigned to elements in the verification target are unique within the verification target.</td>

</tr>
<tr class="odd">
<td><strong>CheckBoundingRect</strong></td>
<td>Confirms that each focusable element in the UI has a bounding rectangle that can be used as a target for hit testing.</td>

</tr>
<tr class="even">
<td rowspan="2"><strong>Tree</strong>${REMOVE}$<br />
</td>
<td><strong>CheckParentChild</strong></td>
<td>Parent and child relationships in the element tree are consistent and predictable.</td>
</tr>
<tr class="odd">
<td><strong>CheckOrphanChildren</strong></td>
<td>Confirms that each focusable element in the UI reports a valid MSAA parent.</td>

</tr>
<tr class="even">
<td rowspan="6"><strong>UIA Properties</strong>${REMOVE}$<br />
</td>
<td><strong>CheckNameUIA</strong></td>
<td>Confirms that each focusable element in the UI reports a valid, logical UIA name.</td>
</tr>
<tr class="odd">
<td><strong>CheckTreeDepthUIA</strong></td>
<td>Sends Tab (or Shift+Tab) characters as input to the verification target to confirm that to UIA elements in the target's UI aren't overly complex or inaccessible using standard keyboard navigation.</td>

</tr>
<tr class="even">
<td><strong>CheckStateUIA</strong></td>
<td>Confirms that each focusable element in the UI reports a valid, logical UIA state.</td>

</tr>
<tr class="odd">
<td><strong>CheckAccessKeysUIA</strong></td>
<td>Confirms that sibling elements do not have the same access and/or accelerator key.</td>

</tr>
<tr class="even">
<td><strong>CheckBoundingRectUIA</strong></td>
<td>Confirms that each focusable UIA element in the UI has a bounding rectangle that can be used as a target for hit testing.</td>

</tr>
<tr class="odd">
<td><strong>CheckControlTypeUIA</strong></td>
<td>Confirms that each focusable element in the UI reports a valid, logical UIA control type.</td>

</tr>
<tr class="even">
<td rowspan="3"><strong>UIA Tree</strong>${REMOVE}$<br />
</td>
<td><strong>CheckNavigateUia</strong></td>
<td>Confirms that the UIA TreeWalker can navigate through an element's children.</td>
</tr>
<tr class="odd">
<td><strong>CheckOrphanChildrenUia</strong></td>
<td>Confirms that each focusable element in the UI reports a valid UIA parent.</td>

</tr>
<tr class="even">
<td><strong>CheckSiblingsUia</strong></td>
<td>Confirms that sibling elements do not have the same Name:ControlType pairs, nor the same AutomationId's.</td>

</tr>
<tr class="odd">
<td>${ROWSPAN9}$<strong>ARIA Web Verifications</strong>${REMOVE}$<br />
</td>
<td><strong>CheckARIARole</strong></td>
<td>Confirms that all elements have a valid ARIA role. The associated HTML tag and ARIA role are information elements with invalid roles flagged as errors.</td>
</tr>
<tr class="even">
<td><strong>CheckLabel</strong></td>
<td>Confirms each element with input, button, image-button, or landmark role has a label.</td>

</tr>
<tr class="odd">
<td><strong>CheckRangeControls</strong></td>
<td>Confirms range controls with slider or progress bar role have proper ARIA attributes defined.</td>

</tr>
<tr class="even">
<td><strong>CheckContainerRole</strong></td>
<td>Confirms an element, or at least one of its children, has onkeydown/onkeypress defined.</td>

</tr>
<tr class="odd">
<td><strong>CheckLayoutTable</strong></td>
<td>Confirms a table layout has a summary/th/aria-describedby included.</td>

</tr>
<tr class="even">
<td><strong>CheckGridStructure</strong></td>
<td>Confirms a non-table element with grid role has a structure of grid>row>gridcell with associated attributes.</td>

</tr>
<tr class="odd">
<td><strong>CheckDataTable</strong></td>
<td>Confirms the properties of data tables.</td>

</tr>
<tr class="even">
<td><strong>CheckActiveDescendants</strong></td>
<td>Confirms the properties of elements with an active descendant defined.</td>

</tr>
<tr class="odd">
<td><strong>CheckElementsWithClickHandler</strong></td>
<td>Confirms the tab index of elements with click handlers.</td>

</tr>
<tr class="even">
<td rowspan="3"><strong>Web Verifications</strong>${REMOVE}$<br />
</td>
<td><strong>CheckHtml (Web)</strong></td>
<td>Confirms various HTML characteristics such as headers, name, frames, and titles.</td>
</tr>
<tr class="odd">
<td><strong>CheckName (Web)</strong></td>
<td>Confirms name characteristics such as length, invalid characters, and role inclusion.</td>

</tr>
<tr class="even">
<td><strong>CheckRole (Web)</strong></td>
<td>Confirms invalid roles, roles that should have values, and/or roles not implemented.</td>

</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[UI Accessibility Checker](ui-accessibility-checker.md)
</dt> </dl>

 

 




