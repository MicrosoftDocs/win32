---
description: This section describes the Windows objects implemented by the Shell.
title: Shell Objects for Scripting and Microsoft Visual Basic
ms.topic: article
ms.date: 05/31/2018
ms.assetid: eee58404-808b-451c-8325-8dcd9537fd11
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Shell Objects for Scripting and Microsoft Visual Basic

This section describes the Windows objects implemented by the Shell.

## In this section




| Topic | Description | 
|-------|-------------|
| <a href="didiskquotauser-object.md"><strong>DIDiskQuotaUser</strong></a><br /> | Allows a client to manage an NTFS volume's global disk quota settings. This object makes the essential functionality of the <a href="didiskquotauser-object.md"><strong>DIDiskQuotaUser</strong></a> interface available to scripting and Microsoft Visual Basic-based applications.<br /> | 
| <a href="diskquotacontrol-object.md"><strong>DiskQuotaControl</strong></a><br /> | Allows an administrator to manage a volume's disk quota properties. The NTFS file system allows an administrator to manage disk usage on a shared volume by allocating a specified amount of disk space, or <em>quota limit</em>, to each user. You can use this object to set the default quota limit that will be automatically assigned to all new users.<br /> | 
| <a href="dshellwindowsevents.md"><strong>DShellWindowsEvents</strong></a><br /> | Receives <a href="/windows/desktop/api/Exdisp/nn-exdisp-ishellwindows"><strong>IShellWindows</strong></a> window registration events. <br /> | 
| <a href="folder.md"><strong>Folder</strong></a><br /> | Represents a Shell folder. This object contains properties and methods that allow you to retrieve information about the folder.<br /> | 
| <a href="folder2-object.md"><strong>Folder2</strong></a><br /> | Extends the <a href="folder.md"><strong>Folder</strong></a> object to support offline folders.<br /> | 
| <a href="folderitem.md"><strong>FolderItem</strong></a><br /> | Represents an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the item.<br /> | 
| <a href="folderitems.md"><strong>FolderItems</strong></a><br /> | Represents the collection of items in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.<br /> | 
| <a href="folderitems2-object.md"><strong>FolderItems2</strong></a><br /> | Extends the <a href="folderitems.md"><strong>FolderItems</strong></a> object. It supports one additional method.<br /> | 
| <a href="folderitems3-object.md"><strong>FolderItems3</strong></a><br /> | Extends the <a href="folderitems2-object.md"><strong>FolderItems2</strong></a> object. This object supports an additional method and property.<br /> | 
| <a href="folderitemverb.md"><strong>FolderItemVerb</strong></a><br /> | Represents a single verb available to an item. This object contains properties and methods that allow you to retrieve information about the verb.<br /> | 
| <a href="folderitemverbs.md"><strong>FolderItemVerbs</strong></a><br /> | Represents the collection of verbs for an item in a Shell folder. This object contains properties and methods that allow you to retrieve information about the collection.<br /> | 
| <a href="ishelldispatch.md"><strong>IShellDispatch</strong></a><br /> | Represents an object in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects. <br /><blockquote>[!Note]<br /><a href="ishelldispatch.md"><strong>IShellDispatch</strong></a> is implemented and accessed through the <a href="shell.md"><strong>Shell</strong></a> object.</blockquote><br /> | 
| <a href="ishelldispatch2-object.md"><strong>IShellDispatch2</strong></a><br /> | Extends the <a href="ishelldispatch.md"><strong>IShellDispatch</strong></a> object with a variety of new functionality. <br /><blockquote>[!Note]<br /><a href="ishelldispatch2-object.md"><strong>IShellDispatch2</strong></a> is implemented and accessed through the <a href="shell.md"><strong>Shell</strong></a> object.</blockquote><br /> | 
| <a href="ishelldispatch3.md"><strong>IShellDispatch3</strong></a><br /> | Extends the <a href="ishelldispatch2-object.md"><strong>IShellDispatch2</strong></a> object. <a href="ishelldispatch3.md"><strong>IShellDispatch3</strong></a> supports one new method in addition to the properties and methods supported by <strong>IShellDispatch2</strong>. <br /><blockquote>[!Note]<br /><a href="ishelldispatch3.md"><strong>IShellDispatch3</strong></a> is implemented and accessed through the <a href="shell.md"><strong>Shell</strong></a> object.</blockquote><br /> | 
| <a href="ishelldispatch4.md"><strong>IShellDispatch4</strong></a><br /> | Extends the <a href="ishelldispatch3.md"><strong>IShellDispatch3</strong></a> object. In addition to the properties and methods supported by <strong>IShellDispatch3</strong>, <a href="ishelldispatch4.md"><strong>IShellDispatch4</strong></a> supports four additional methods. <br /><blockquote>[!Note]<br /><a href="ishelldispatch4.md"><strong>IShellDispatch4</strong></a> is implemented and accessed through the <a href="shell.md"><strong>Shell</strong></a> object.</blockquote><br /> | 
| <a href="ishelldispatch5.md"><strong>IShellDispatch5</strong></a><br /> | Extends the <a href="ishelldispatch4.md"><strong>IShellDispatch4</strong></a> object. In addition to the properties and methods supported by <strong>IShellDispatch4</strong>, <a href="ishelldispatch5.md"><strong>IShellDispatch5</strong></a> adds a method that displays open windows in a 3D stack. <br /><blockquote>[!Note]<br /><a href="ishelldispatch5.md"><strong>IShellDispatch5</strong></a> is implemented and accessed through the <a href="shell.md"><strong>Shell</strong></a> object.</blockquote><br /> | 
| <a href="ishelldispatch6.md"><strong>IShellDispatch6</strong></a><br /> | Extends the <a href="ishelldispatch5.md"><strong>IShellDispatch5</strong></a> object. In addition to the properties and methods supported by <strong>IShellDispatch5</strong>, <a href="ishelldispatch6.md"><strong>IShellDispatch6</strong></a> adds a method that displays the Apps Search pane. <br /><blockquote>[!Note]<br /><a href="ishelldispatch6.md"><strong>IShellDispatch6</strong></a> is implemented and accessed through the <a href="shell.md"><strong>Shell</strong></a> object.</blockquote><br /> | 
| <a href="ishelllinkdual2-object.md"><strong>IShellLinkDual2</strong></a><br /> | Extends the <a href="shelllinkobject-object.md"><strong>ShellLinkObject</strong></a> object and supports one additional property.<br /> | 
| <a href="newwdevents.md"><strong>NewWDEvents</strong></a><br /> | Extends the <a href="webwizardhost.md"><strong>WebWizardHost</strong></a> object by enabling server-side pages hosted in a wizard to verify that the user has been authenticated through a Microsoft account.<br /> | 
| <a href="shell.md"><strong>Shell</strong></a><br /> | Represents the objects in the Shell. Methods are provided to control the Shell and to execute commands within the Shell. There are also methods to obtain other Shell-related objects.<br /> | 
| <a href="shellfolderitem-object.md"><strong>ShellFolderItem</strong></a><br /> | Extends the <a href="folderitem.md"><strong>FolderItem</strong></a> object. In addition to the properties and methods supported by <strong>FolderItem</strong>, <a href="shellfolderitem-object.md"><strong>ShellFolderItem</strong></a> has two additional methods.<br /> | 
| <a href="shellfolderview.md"><strong>ShellFolderView</strong></a><br /> | Represents the objects in a view and provides properties and methods used to obtain information about the contents of the view.<br /> | 
| <a href="shellfolderviewoc-object.md"><strong>ShellFolderViewOC</strong></a><br /> | Forwards the events fired by a specified <a href="shellfolderview.md"><strong>ShellFolderView</strong></a> object to corresponding <a href="shellfolderviewoc-object.md"><strong>ShellFolderViewOC</strong></a> event handlers.<br /> | 
| <a href="shelllinkobject-object.md"><strong>ShellLinkObject</strong></a><br /> | Manages Shell links. This object makes much of the functionality of the <a href="/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka"><strong>IShellLink</strong></a> interface available to scripting applications. <br /> | 
| <a href="shelluihelper.md"><strong>ShellUIHelper</strong></a><br /> | Implemented by the Shell to help script and Visual Basic developers use some of the features available in the Shell. The <a href="shelluihelper.md"><strong>ShellUIHelper</strong></a> object does not have any properties or events. Methods are provided to add items to the Shell.<br /> | 
| <a href="shellwindows.md"><strong>ShellWindows</strong></a><br /> | Represents a collection of the open windows that belong to the Shell. Methods associated with this objects can control and execute commands within the Shell, and obtain other Shell-related objects.<br /> | 
| <a href="webwizardhost.md"><strong>WebWizardHost</strong></a><br /> | Exposes methods that enable HTML pages which are hosted in a wizard extension to communicate with the wizard.<br /> | 




 

 

 




