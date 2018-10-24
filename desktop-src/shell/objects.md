---
Description: This section describes the Windows objects implemented by the Shell.
title: Shell Objects for Scripting and Microsoft Visual Basic
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
<td><a href="didiskquotauser-object"><strong>DIDiskQuotaUser</strong></a><br/></td>
<td>Allows a client to manage an NTFS volume's global disk quota settings. This object makes the essential functionality of the <a href="didiskquotauser-object"><strong>DIDiskQuotaUser</strong></a> interface available to scripting and Microsoft Visual Basic-based applications.<br/></td>
</tr>
<tr class="even">
<td><a href="diskquotacontrol-object"><strong>DiskQuotaControl</strong></a><br/></td>
<td>Allows an administrator to manage a volume's disk quota properties. The NTFS file system allows an administrator to manage disk usage on a shared volume by allocating a specified amount of disk space, or <em>quota limit</em>, to each user. You can use this object to set the default quota limit that will be automatically assigned to all new users.<br/></td>
</tr>
<tr class="odd">
<td><a href="dshellwindowsevents"><strong>DShellWindowsEvents</strong></a><br/></td>
<td>Receives <a href="/windows/desktop/api/Exdisp/nn-exdisp-ishellwindows"><strong>IShellWindows</strong></a> window registration events. <br/></td>
</tr>
<tr class="even">
<td><a href="folder"><strong>Folder</strong></a><br/></td>
<td>Represents a Shell folder. This object contains properties and methods that allow you to retrieve information about the folder.<br/></td>
</tr>
<tr class="odd">
<td><a href="folder2-object"><strong>Folder2</strong></a><br/></td>
<td>Extends the <a href="folder"><strong>Folder</strong></a> object to support offline folders.<br/></td>
</tr>
<tr class="even">
<td><a href="folderitem"><strong>FolderItem</strong></a><br/></td>
<td>Represents an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the item.<br/></td>
</tr>
<tr class="odd">
<td><a href="folderitems"><strong>FolderItems</strong></a><br/></td>
<td>Represents the collection of items in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.<br/></td>
</tr>
<tr class="even">
<td><a href="folderitems2-object"><strong>FolderItems2</strong></a><br/></td>
<td>Extends the <a href="folderitems"><strong>FolderItems</strong></a> object. It supports one additional method.<br/></td>
</tr>
<tr class="odd">
<td><a href="folderitems3-object"><strong>FolderItems3</strong></a><br/></td>
<td>Extends the <a href="folderitems2-object"><strong>FolderItems2</strong></a> object. This object supports an additional method and property.<br/></td>
</tr>
<tr class="even">
<td><a href="folderitemverb"><strong>FolderItemVerb</strong></a><br/></td>
<td>Represents a single verb available to an item. This object contains properties and methods that allow you to retrieve information about the verb.<br/></td>
</tr>
<tr class="odd">
<td><a href="folderitemverbs"><strong>FolderItemVerbs</strong></a><br/></td>
<td>Represents the collection of verbs for an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.<br/></td>
</tr>
<tr class="even">
<td><a href="ishelldispatch"><strong>IShellDispatch</strong></a><br/></td>
<td>Represents an object in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects. <br/>
<blockquote>
[!Note]<br />
<a href="ishelldispatch"><strong>IShellDispatch</strong></a> is implemented and accessed through the <a href="shell"><strong>Shell</strong></a> object.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="ishelldispatch2-object"><strong>IShellDispatch2</strong></a><br/></td>
<td>Extends the <a href="ishelldispatch"><strong>IShellDispatch</strong></a> object with a variety of new functionality. <br/>
<blockquote>
[!Note]<br />
<a href="ishelldispatch2-object"><strong>IShellDispatch2</strong></a> is implemented and accessed through the <a href="shell"><strong>Shell</strong></a> object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="ishelldispatch3"><strong>IShellDispatch3</strong></a><br/></td>
<td>Extends the <a href="ishelldispatch2-object"><strong>IShellDispatch2</strong></a> object. <a href="ishelldispatch3"><strong>IShellDispatch3</strong></a> supports one new method in addition to the properties and methods supported by <strong>IShellDispatch2</strong>. <br/>
<blockquote>
[!Note]<br />
<a href="ishelldispatch3"><strong>IShellDispatch3</strong></a> is implemented and accessed through the <a href="shell"><strong>Shell</strong></a> object.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="ishelldispatch4"><strong>IShellDispatch4</strong></a><br/></td>
<td>Extends the <a href="ishelldispatch3"><strong>IShellDispatch3</strong></a> object. In addition to the properties and methods supported by <strong>IShellDispatch3</strong>, <a href="ishelldispatch4"><strong>IShellDispatch4</strong></a> supports four additional methods. <br/>
<blockquote>
[!Note]<br />
<a href="ishelldispatch4"><strong>IShellDispatch4</strong></a> is implemented and accessed through the <a href="shell"><strong>Shell</strong></a> object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="ishelldispatch5"><strong>IShellDispatch5</strong></a><br/></td>
<td>Extends the <a href="ishelldispatch4"><strong>IShellDispatch4</strong></a> object. In addition to the properties and methods supported by <strong>IShellDispatch4</strong>, <a href="ishelldispatch5"><strong>IShellDispatch5</strong></a> adds a method that displays open windows in a 3D stack. <br/>
<blockquote>
[!Note]<br />
<a href="ishelldispatch5"><strong>IShellDispatch5</strong></a> is implemented and accessed through the <a href="shell"><strong>Shell</strong></a> object.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="ishelldispatch6"><strong>IShellDispatch6</strong></a><br/></td>
<td>Extends the <a href="ishelldispatch5"><strong>IShellDispatch5</strong></a> object. In addition to the properties and methods supported by <strong>IShellDispatch5</strong>, <a href="ishelldispatch6"><strong>IShellDispatch6</strong></a> adds a method that displays the Apps Search pane. <br/>
<blockquote>
[!Note]<br />
<a href="ishelldispatch6"><strong>IShellDispatch6</strong></a> is implemented and accessed through the <a href="shell"><strong>Shell</strong></a> object.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="ishelllinkdual2-object"><strong>IShellLinkDual2</strong></a><br/></td>
<td>Extends the <a href="shelllinkobject-object"><strong>ShellLinkObject</strong></a> object and supports one additional property.<br/></td>
</tr>
<tr class="odd">
<td><a href="newwdevents"><strong>NewWDEvents</strong></a><br/></td>
<td>Extends the <a href="webwizardhost"><strong>WebWizardHost</strong></a> object by enabling server-side pages hosted in a wizard to verify that the user has been authenticated through a Microsoft account.<br/></td>
</tr>
<tr class="even">
<td><a href="shell"><strong>Shell</strong></a><br/></td>
<td>Represents the objects in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.<br/></td>
</tr>
<tr class="odd">
<td><a href="shellfolderitem-object"><strong>ShellFolderItem</strong></a><br/></td>
<td>Extends the <a href="folderitem"><strong>FolderItem</strong></a> object. In addition to the properties and methods supported by <strong>FolderItem</strong>, <a href="shellfolderitem-object"><strong>ShellFolderItem</strong></a> has two additional methods.<br/></td>
</tr>
<tr class="even">
<td><a href="shellfolderview"><strong>ShellFolderView</strong></a><br/></td>
<td>Represents the objects in a view and provides properties and methods used to obtain information about the contents of the view.<br/></td>
</tr>
<tr class="odd">
<td><a href="shellfolderviewoc-object"><strong>ShellFolderViewOC</strong></a><br/></td>
<td>Forwards the events fired by a specified <a href="shellfolderview"><strong>ShellFolderView</strong></a> object to corresponding <a href="shellfolderviewoc-object"><strong>ShellFolderViewOC</strong></a> event handlers.<br/></td>
</tr>
<tr class="even">
<td><a href="shelllinkobject-object"><strong>ShellLinkObject</strong></a><br/></td>
<td>Manages Shell links. This object makes much of the functionality of the <a href="/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka"><strong>IShellLink</strong></a> interface available to scripting applications. <br/></td>
</tr>
<tr class="odd">
<td><a href="shelluihelper"><strong>ShellUIHelper</strong></a><br/></td>
<td>Implemented by the Shell to help script and Visual Basic developers use some of the features available in the Shell. The <a href="shelluihelper"><strong>ShellUIHelper</strong></a> object does not have any properties or events. Methods are provided to add items to the Shell.<br/></td>
</tr>
<tr class="even">
<td><a href="shellwindows"><strong>ShellWindows</strong></a><br/></td>
<td>Represents a collection of the open windows that belong to the Shell. Methods associated with this objects can control and execute commands within the Shell, and obtain other Shell-related objects.<br/></td>
</tr>
<tr class="odd">
<td><a href="webwizardhost"><strong>WebWizardHost</strong></a><br/></td>
<td>Exposes methods that enable HTML pages which are hosted in a wizard extension to communicate with the wizard.<br/></td>
</tr>
</tbody>
</table>



 

 

 




