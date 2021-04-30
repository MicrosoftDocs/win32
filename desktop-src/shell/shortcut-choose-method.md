---
description: 'This topic is organized as follows:'
title: Choosing a Static or Dynamic Shortcut Menu Method
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 44227BCF-D35E-4a9e-B4E6-D50E6AFBAEDF
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Choosing a Static or Dynamic Shortcut Menu Method

This topic is organized as follows:

-   [Choose a Verb Method](#choose-a-verb-method)
    -   [Static Verb Methods](#static-verb-methods)
    -   [Preferred Dynamic Verb Methods](#preferred-dynamic-verb-methods)
    -   [Discouraged Dynamic Verb Methods](#discouraged-dynamic-verb-methods)
-   [Extend a Shortcut Menu](#extend-a-shortcut-menu)
-   [Support for Verb Methods by Operating System](#support-for-verb-methods-by-operating-system)
-   [Related topics](#related-topics)

## Choose a Verb Method

It is strongly encouraged that you implement a shortcut menu using one of the static verb methods.

### Static Verb Methods

Static verbs are the simplest verbs to implement, but they still provide rich functionality. Always chose the simplest shortcut menu method that meets your needs.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Static Verb</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa"><strong>CreateProcess</strong></a> with command line parameters</td>
<td>This is the simplest and most familiar means of implementing a static verb. A process is invoked through a call to the <a href="/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa"><strong>CreateProcess</strong></a> function with the selected files and any optional parameters passed as the command line. This opens the file or folder.<br/> This method has the following limitations:
<ul>
<li>The command-line length is limited to 2000 characters, which limits the number of items that the verb can handle.</li>
<li>Can only be used with file system items.</li>
<li>Does not enable re-use of an already running process.</li>
<li>Requires that an executable be installed to handle the verb.</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td><strong>DropTarget</strong>/<a href="/windows/desktop/api/oleidl/nn-oleidl-idroptarget"><strong>IDropTarget</strong></a></td>
<td>A COM-based verb activation means that supports in-proc or out-of-proc activation. <strong>DropTarget</strong>/<a href="/windows/desktop/api/oleidl/nn-oleidl-idroptarget"><strong>IDropTarget</strong></a> also supports re-use of an already running handler when the <strong>IDropTarget</strong> interface is implemented by a local server. It also perfectly expresses the items via the marshaled data object and provides a reference to the invoking site chain so that you can interact with the invoker through the <a href="/previous-versions/windows/internet-explorer/ie-developer/platform-apis/cc678966(v=vs.85)"><strong>QueryService</strong></a>.</td>
</tr>
<tr class="odd">
<td>Windows 7 and later: <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexecutecommand"><strong>IExecuteCommand</strong></a></td>
<td>The most direct implementation method. Because this is a COM-based invoke method (like DropTarget) this interface supports in-proc and out-of-proc activation. The verb implements <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexecutecommand"><strong>IExecuteCommand</strong></a> and <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iobjectwithselection"><strong>IObjectWithSelection</strong></a>, and optionally <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iinitializecommand"><strong>IInitializeCommand</strong></a>. The items are passed directly as a Shell item array and more of the parameters from the invoker are available to the verb implementation, including the invoke point, keyboard state, and so forth.</td>
</tr>
<tr class="even">
<td>Windows 7 and later:<strong>ExplorerCommand</strong>/ <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand"><strong>IExplorerCommand</strong></a></td>
<td>Enables data sources that provide their command module commands through <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandprovider"><strong>IExplorerCommandProvider</strong></a> to use those commands as verbs on a shortcut menu. Because this interface supports in-process activation only, it is recommended for use by Shell data sources that need to share the implementation between commands and shortcut menus.</td>
</tr>
</tbody>
</table>



 

> [!Note]  
> [**IExplorerCommand**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand) is a hybrid between a static and dynamic verb. **IExplorerCommand** was declared in Windows Vista, but its ability to implement a verb in a shortcut menu is new to Windows 7.

 

For more information about [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) and Shell queries for file association attributes, see [Perceived Types and Application Registration](fa-perceivedtypes.md).

### Preferred Dynamic Verb Methods

The following dynamic verb methods are preferred:



| Verb Type                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Static verb (listed in the previous table) + Advanced Query Syntax (AQS)                  | This choice gets dynamic verb visibility.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Windows 7 and later: [**IExplorerCommand**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand)                         | This choice enables a common implementation of verbs and explorer commands that are displayed in the command module in Windows Explorer.                                                                                                                                                                                                                                                                                                                                                                                               |
| Windows 7 and later: [**IExplorerCommandState**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandstate) + static verb | This choice also gets dynamic verb visibility. It is a hybrid model where a simple in-process handler is used to compute if a given static verb should be displyed. This can be applied to all of the static verb implementation methods to achieve dynamic behavior and minimize the exposure of the in-process logic. [**IExplorerCommandState**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandstate) has the advantage of running on a background thread, and thereby avoids UI hangs. It is considerably simpler than [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu). |



 

### Discouraged Dynamic Verb Methods

[**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) is the most powerful but also the most complicated method to implement. It is based on in-process COM objects that run on the thread of the caller, which usually Windows Explorer but can be any application hosting the items. **IContextMenu** supports verb visibility, ordering, and custom drawing. Some of these features have been added to the static verb features, such as an icon to be associated with a command, and [**IExplorerCommand**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand) to deal with visibility.

If you must extend the shortcut menu for a file type by registering a dynamic verb for the file type, then follow the instructions provided in [Customizing a Shortcut Menu Using Dynamic Verbs](shortcut-menu-using-dynamic-verbs.md).

## Extend a Shortcut Menu

After you choose a verb method you can extend a shortcut menu for a file type by registering a static verb for the file type. For more information, see [Creating Context Menu Handlers](context-menu-handlers.md).

## Support for Verb Methods by Operating System

Support for verb invocation methods by operating system are listed in the following table.



|                      |            |               |                      |
|----------------------|------------|---------------|----------------------|
|                      | Windows XP | Windows Vista | Windows 7 and beyond |
| CreateProcess        | X          | X             | X                    |
| DDE                  | X          | X             | X                    |
| DropTarget           | X          | X             | X                    |
| ExecuteCommand       |            | X             | X                    |
| ExplorerCommand      |            |               | X                    |
| ExplorerCommandState |            |               | X                    |



 

## Related topics

<dl> <dt>

[Best Practices for Shortcut Menu Handlers and Multiple Selection Verbs](verbs-best-practices.md)
</dt> <dt>

[Creating Shortcut Menu Handlers](context-menu-handlers.md)
</dt> <dt>

[Customizing a Shortcut Menu Using Dynamic Verbs](shortcut-menu-using-dynamic-verbs.md)
</dt> <dt>

[Shortcut (Context) Menus and Shortcut Menu Handlers](context-menu.md)
</dt> <dt>

[Shortcut Menu Reference](context-menu-reference.md)
</dt> <dt>

[Verbs and File Associations](fa-verbs.md)
</dt> </dl>

 

 
