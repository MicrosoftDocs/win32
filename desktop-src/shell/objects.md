---
Description: This section describes the Windows objects implemented by the Shell.
title: Shell Objects for Scripting and Microsoft Visual Basic
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell Objects for Scripting and Microsoft Visual Basic

This section describes the Windows objects implemented by the Shell.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>DIDiskQuotaUser</strong>](didiskquotauser-object.md)<br/></td>
<td>Allows a client to manage an NTFS volume's global disk quota settings. This object makes the essential functionality of the [<strong>DIDiskQuotaUser</strong>](didiskquotauser-object.md) interface available to scripting and Microsoft Visual Basic-based applications.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DiskQuotaControl</strong>](diskquotacontrol-object.md)<br/></td>
<td>Allows an administrator to manage a volume's disk quota properties. The NTFS file system allows an administrator to manage disk usage on a shared volume by allocating a specified amount of disk space, or <em>quota limit</em>, to each user. You can use this object to set the default quota limit that will be automatically assigned to all new users.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DShellWindowsEvents</strong>](dshellwindowsevents.md)<br/></td>
<td>Receives [<strong>IShellWindows</strong>](/windows/desktop/api/Exdisp/nn-exdisp-ishellwindows) window registration events. <br/></td>
</tr>
<tr class="even">
<td>[<strong>Folder</strong>](folder.md)<br/></td>
<td>Represents a Shell folder. This object contains properties and methods that allow you to retrieve information about the folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Folder2</strong>](folder2-object.md)<br/></td>
<td>Extends the [<strong>Folder</strong>](folder.md) object to support offline folders.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FolderItem</strong>](folderitem.md)<br/></td>
<td>Represents an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FolderItems</strong>](folderitems.md)<br/></td>
<td>Represents the collection of items in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FolderItems2</strong>](folderitems2-object.md)<br/></td>
<td>Extends the [<strong>FolderItems</strong>](folderitems.md) object. It supports one additional method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FolderItems3</strong>](folderitems3-object.md)<br/></td>
<td>Extends the [<strong>FolderItems2</strong>](folderitems2-object.md) object. This object supports an additional method and property.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FolderItemVerb</strong>](folderitemverb.md)<br/></td>
<td>Represents a single verb available to an item. This object contains properties and methods that allow you to retrieve information about the verb.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FolderItemVerbs</strong>](folderitemverbs.md)<br/></td>
<td>Represents the collection of verbs for an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellDispatch</strong>](ishelldispatch.md)<br/></td>
<td>Represents an object in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects. <br/>
<blockquote>
[!Note]<br />
[<strong>IShellDispatch</strong>](ishelldispatch.md) is implemented and accessed through the [<strong>Shell</strong>](shell.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellDispatch2</strong>](ishelldispatch2-object.md)<br/></td>
<td>Extends the [<strong>IShellDispatch</strong>](ishelldispatch.md) object with a variety of new functionality. <br/>
<blockquote>
[!Note]<br />
[<strong>IShellDispatch2</strong>](ishelldispatch2-object.md) is implemented and accessed through the [<strong>Shell</strong>](shell.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellDispatch3</strong>](ishelldispatch3.md)<br/></td>
<td>Extends the [<strong>IShellDispatch2</strong>](ishelldispatch2-object.md) object. [<strong>IShellDispatch3</strong>](ishelldispatch3.md) supports one new method in addition to the properties and methods supported by <strong>IShellDispatch2</strong>. <br/>
<blockquote>
[!Note]<br />
[<strong>IShellDispatch3</strong>](ishelldispatch3.md) is implemented and accessed through the [<strong>Shell</strong>](shell.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellDispatch4</strong>](ishelldispatch4.md)<br/></td>
<td>Extends the [<strong>IShellDispatch3</strong>](ishelldispatch3.md) object. In addition to the properties and methods supported by <strong>IShellDispatch3</strong>, [<strong>IShellDispatch4</strong>](ishelldispatch4.md) supports four additional methods. <br/>
<blockquote>
[!Note]<br />
[<strong>IShellDispatch4</strong>](ishelldispatch4.md) is implemented and accessed through the [<strong>Shell</strong>](shell.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellDispatch5</strong>](ishelldispatch5.md)<br/></td>
<td>Extends the [<strong>IShellDispatch4</strong>](ishelldispatch4.md) object. In addition to the properties and methods supported by <strong>IShellDispatch4</strong>, [<strong>IShellDispatch5</strong>](ishelldispatch5.md) adds a method that displays open windows in a 3D stack. <br/>
<blockquote>
[!Note]<br />
[<strong>IShellDispatch5</strong>](ishelldispatch5.md) is implemented and accessed through the [<strong>Shell</strong>](shell.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellDispatch6</strong>](ishelldispatch6.md)<br/></td>
<td>Extends the [<strong>IShellDispatch5</strong>](ishelldispatch5.md) object. In addition to the properties and methods supported by <strong>IShellDispatch5</strong>, [<strong>IShellDispatch6</strong>](ishelldispatch6.md) adds a method that displays the Apps Search pane. <br/>
<blockquote>
[!Note]<br />
[<strong>IShellDispatch6</strong>](ishelldispatch6.md) is implemented and accessed through the [<strong>Shell</strong>](shell.md) object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellLinkDual2</strong>](ishelllinkdual2-object.md)<br/></td>
<td>Extends the [<strong>ShellLinkObject</strong>](shelllinkobject-object.md) object and supports one additional property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NewWDEvents</strong>](newwdevents.md)<br/></td>
<td>Extends the [<strong>WebWizardHost</strong>](webwizardhost.md) object by enabling server-side pages hosted in a wizard to verify that the user has been authenticated through a Microsoft account.<br/></td>
</tr>
<tr class="even">
<td>[<strong>Shell</strong>](shell.md)<br/></td>
<td>Represents the objects in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellFolderItem</strong>](shellfolderitem-object.md)<br/></td>
<td>Extends the [<strong>FolderItem</strong>](folderitem.md) object. In addition to the properties and methods supported by <strong>FolderItem</strong>, [<strong>ShellFolderItem</strong>](shellfolderitem-object.md) has two additional methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellFolderView</strong>](shellfolderview.md)<br/></td>
<td>Represents the objects in a view and provides properties and methods used to obtain information about the contents of the view.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellFolderViewOC</strong>](shellfolderviewoc-object.md)<br/></td>
<td>Forwards the events fired by a specified [<strong>ShellFolderView</strong>](shellfolderview.md) object to corresponding [<strong>ShellFolderViewOC</strong>](shellfolderviewoc-object.md) event handlers.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellLinkObject</strong>](shelllinkobject-object.md)<br/></td>
<td>Manages Shell links. This object makes much of the functionality of the [<strong>IShellLink</strong>](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka) interface available to scripting applications. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellUIHelper</strong>](shelluihelper.md)<br/></td>
<td>Implemented by the Shell to help script and Visual Basic developers use some of the features available in the Shell. The [<strong>ShellUIHelper</strong>](shelluihelper.md) object does not have any properties or events. Methods are provided to add items to the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellWindows</strong>](shellwindows.md)<br/></td>
<td>Represents a collection of the open windows that belong to the Shell. Methods associated with this objects can control and execute commands within the Shell, and obtain other Shell-related objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WebWizardHost</strong>](webwizardhost.md)<br/></td>
<td>Exposes methods that enable HTML pages which are hosted in a wizard extension to communicate with the wizard.<br/></td>
</tr>
</tbody>
</table>



 

 

 




