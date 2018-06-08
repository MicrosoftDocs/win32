---
Description: This section describes the Windows Shell interfaces.
title: Shell Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell Interfaces

This section describes the Windows Shell interfaces.

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
<td>[<strong>IAccessibleObject</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iaccessibleobject)<br/></td>
<td>Exposes a method that can be used by an accessibility application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAccessibilityDockingService</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Docks a single accessibility app window to the bottom of a screen.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAccessibilityDockingServiceCallback</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Informs an accessibility app that its window has been undocked.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IACLCustomMRU</strong>](iaclcustommru.md)<br/></td>
<td>Exposes methods that are used to initialize a most recently used (MRU) list for an autocompletion object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IACList</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes a method that improves the efficiency of [<strong>autocompletion</strong>](/windows/desktop/api/Shldisp/nn-shldisp-iautocomplete) when the candidate strings are organized in a hierarchy.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IACList2</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Extends the [<strong>IACList</strong>](/windows/desktop/api/Shlobj_core/) interface to enable clients of an autocomplete object to retrieve and set option flags.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IActionProgress</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iactionprogress)<br/></td>
<td>Represents the abstract base class from which progress-driven operations can inherit.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IActionProgressDialog</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iactionprogressdialog)<br/></td>
<td>Exposes methods that initialize and stop a progress dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationActivationManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationactivationmanager)<br/></td>
<td>Provides methods which activate Windows Store apps for the Launch, File, and Protocol [extensions](https://msdn.microsoft.com/08800074-78ba-410a-962f-876da3463629). You will normally use this interface in debuggers and design tools.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IApplicationAssociationRegistration</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationassociationregistration)<br/></td>
<td>Exposes methods that query and set default applications for specific file [<strong>Association Type</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-associationtype), and protocols at a specific [<strong>Association Level</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-associationlevel). <br/>
<blockquote>
[!Note]<br />
As of Windows 8, the only functionality of this interface that is supported is [<strong>QueryCurrentDefault</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationassociationregistration-querycurrentdefault).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationAssociationRegistrationUI</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iapplicationassociationregistrationui)<br/></td>
<td>Exposes a method that launches an advanced association dialog box through which the user can customize their associations.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IApplicationDesignModeSettings</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdesignmodesettings)<br/></td>
<td>Enables development tool applications to dynamically spoof system and user states, such as native display resolution, device scale factor, and application view state, for the purpose of testing Windows Store apps running in design mode for a wide range of form factors without the need for the actual hardware. Also enables testing of changes in normally user-controlled state to test Windows Store apps under a variety of scenarios.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationDesignModeSettings2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdesignmodesettings2)<br/></td>
<td>Enables development tool applications to dynamically control system and user states, such as native display resolution, device scale factor, and application view layout, reported to Windows Store apps for the purpose of testing Windows Store apps running in design mode for a wide range of form factors without the need for the actual hardware. Also enables testing of changes in normally user-controlled state to test Windows Store apps under a variety of scenarios.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IApplicationDestinations</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdestinations)<br/></td>
<td>Exposes methods that allow an application to remove one or all destinations from the <strong>Recent</strong> or <strong>Frequent</strong> categories in a Jump List.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationDocumentLists</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdocumentlists)<br/></td>
<td>Exposes methods that allow an application to retrieve the contents of the <strong>Recent</strong> or <strong>Frequent</strong> categories in a Jump List.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAppPublisher</strong>](/windows/desktop/api/Shappmgr/nn-shappmgr-iapppublisher)<br/></td>
<td>Exposes methods for publishing applications through <strong>Add/Remove Programs</strong> in Control Panel. This is the principal interface implemented for this purpose.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAppVisibility</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iappvisibility)<br/></td>
<td>Provides functionality to determine whether the display is showing Windows Store apps.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAppVisibilityEvents</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iappvisibilityevents)<br/></td>
<td>Enables applications to receive notifications of state changes in a display and of changes in Start screen visibility.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAssocHandler</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iassochandler)<br/></td>
<td>Exposes methods for operations with a file association dialog box or menu.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAssocHandlerInvoker</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iassochandlerinvoker)<br/></td>
<td>Exposes methods that invoke an associated application handler.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAttachmentExecute</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iattachmentexecute)<br/></td>
<td>Exposes methods that work with client applications to present a user environment that provides safe download and exchange of files through email and messaging attachments.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAutoComplete</strong>](/windows/desktop/api/Shldisp/nn-shldisp-iautocomplete)<br/></td>
<td>Exposed by the autocomplete object (CLSID_AutoComplete). This interface allows applications to initialize, enable, and disable the object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAutoComplete2</strong>](/windows/desktop/api/Shldisp/nn-shldisp-iautocomplete2)<br/></td>
<td>Extends [<strong>IAutoComplete</strong>](/windows/desktop/api/Shldisp/nn-shldisp-iautocomplete). This interface enables clients of the autocomplete object to retrieve and set a number of options that control how autocompletion operates.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAutoCompleteDropDown</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iautocompletedropdown)<br/></td>
<td>Exposes methods that allow clients to reset or query the display state of the autocomplete drop-down list, which contains possible completions to a string entered by the user in an edit control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IBandHost</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ibandhost)<br/></td>
<td>Exposes methods that create and destroy bands and specifiy their availability.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IBandSite</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ibandsite)<br/></td>
<td>Exposes methods that control band objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IBrowserFrameOptions</strong>](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ibrowserframeoptions)<br/></td>
<td>Allows a browser or host to ask [<strong>IShellView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) what kind of view behavior is supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICategorizer</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icategorizer)<br/></td>
<td>Exposes methods that are used to obtain information about item identifier lists.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICategoryProvider</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icategoryprovider)<br/></td>
<td>Exposes a list of categorizers registered on an [<strong>IShellFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder).<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICDBurn</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-icdburn)<br/></td>
<td>Exposes methods that determine whether a system has hardware for writing to CD, the drive letter of a CD writer device, and programmatically initiate a CD writing session. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IColumnManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icolumnmanager)<br/></td>
<td>Exposes methods that enable inspection and manipulation of columns in the Windows Explorer Details view. Each column is referenced by a [<strong>PROPERTYKEY</strong>](https://msdn.microsoft.com/3f5f31af-f040-443b-9045-9761055381ea) structure, which names a property.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICommDlgBrowser</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icommdlgbrowser)<br/></td>
<td>Exposed by the common file dialog boxes to be used when they host a Shell browser. If supported, [<strong>ICommDlgBrowser</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icommdlgbrowser) exposes methods that allow a Shell view to handle several cases that require different behavior in a dialog box than in a normal Shell view. You obtain an <strong>ICommDlgBrowser</strong> interface pointer by calling [<strong>QueryInterface</strong>](https://msdn.microsoft.com/54d5ff80-18db-43f2-b636-f93ac053146d) on the [<strong>IShellBrowser</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellbrowser) object. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICommDlgBrowser2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icommdlgbrowser2)<br/></td>
<td>Extends the capabilities of [<strong>ICommDlgBrowser</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icommdlgbrowser). This interface is exposed by the common file dialog boxes when they host a Shell browser. A pointer to [<strong>ICommDlgBrowser2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icommdlgbrowser2) can be obtained by calling [<strong>QueryInterface</strong>](https://msdn.microsoft.com/54d5ff80-18db-43f2-b636-f93ac053146d) on the [<strong>IShellBrowser</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellbrowser) object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICommDlgBrowser3</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-icommdlgbrowser3)<br/></td>
<td>Extends the capabilities of [<strong>ICommDlgBrowser2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icommdlgbrowser2), and used by the common file dialog boxes when they host a Shell browser.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IComputerInfoChangeNotify</strong>](/windows/desktop/api/shobjidl/nn-shobjidl-icomputerinfochangenotify)<br/></td>
<td>This interface may be absent in later versions of Windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IConnectableCredentialProviderCredential</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-iconnectablecredentialprovidercredential)<br/></td>
<td>Exposes methods for connecting and disconnecting [<strong>IConnectableCredentialProviderCredential</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-iconnectablecredentialprovidercredential) objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IContactManagerInterop</strong>](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-icontactmanagerinterop)<br/></td>
<td>Enables access to [<strong>ContactManager</strong>](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-icontactmanagerinterop) methods in an app that manages multiple windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IContextMenu</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-icontextmenu)<br/></td>
<td>Exposes methods that either create or merge a shortcut menu associated with a Shell object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IContextMenu2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icontextmenu2)<br/></td>
<td>Exposes methods that either create or merge a shortcut (context) menu associated with a Shell object. Extends [<strong>IContextMenu</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-icontextmenu) by adding a method that allows client objects to handle messages associated with owner-drawn menu items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IContextMenu3</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icontextmenu3)<br/></td>
<td>Exposes methods that either create or merge a shortcut menu associated with a Shell object. Allows client objects to handle messages associated with owner-drawn menu items and extends [<strong>IContextMenu2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icontextmenu2) by accepting a return value from that message handling.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IContextMenuCB</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icontextmenucb)<br/></td>
<td>Exposes a method that enables the callback of a context menu. For example, to add a shield icon to a <strong>menuItem</strong> that requires elevation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IControlMarkup</strong>](/windows/desktop/api/Shobjidl/)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>ICopyHook</strong>](/windows/desktop/api/Shlobj/)<br/></td>
<td>Exposes a method that creates a <em>copy hook handler</em>. A copy hook handler is a Shell extension that determines if a Shell folder or printer object can be moved, copied, renamed, or deleted. The Shell calls the [<strong>ICopyHook::CopyCallback</strong>](/windows/desktop/api/Shlobj/) method prior to performing one of these operations.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICreateObject</strong>](/windows/desktop/api/Propsys/nn-propsys-icreateobject)<br/></td>
<td>Exposes a method that creates an object of a specified class.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICreatingProcess</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icreatingprocess)<br/></td>
<td>Used by [<strong>ShellExecuteEx</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) and [<strong>IContextMenu</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-icontextmenu) to allow the caller to alter some parameters of the process being created.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICreateProcessInputs</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icreateprocessinputs)<br/></td>
<td>Used by the [<strong>ICreatingProcess</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icreatingprocess) interface to alter some parameters of the process that is being created.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProvider</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-icredentialprovider)<br/></td>
<td>Exposes methods used in the setup and manipulation of a credential provider. All credential providers must implement this interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderCredential</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-icredentialprovidercredential)<br/></td>
<td>Exposes methods that enable the handling of a credential.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderCredential2</strong>](/windows/desktop/api/CredentialProvider/nn-credentialprovider-icredentialprovidercredential2)<br/></td>
<td>Extends the [<strong>ICredentialProviderCredential</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-icredentialprovidercredential) interface by adding a method that retrieves the security identifier (SID) of a user. The credential is associated with that user and can be grouped under the user's tile.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderCredentialEvents</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-icredentialprovidercredentialevents)<br/></td>
<td>Provides an asynchronous callback mechanism used by a credential to notify it of state or text change events in the Logon UI or Credential UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderCredentialEvents2</strong>](/windows/desktop/api/CredentialProvider/nn-credentialprovider-icredentialprovidercredentialevents2)<br/></td>
<td>Extends the [<strong>ICredentialProviderCredentialEvents</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-icredentialprovidercredentialevents) interface by adding methods that enable batch updating of fields in theLogon UI or Credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderCredentialWithFieldOptions</strong>](/windows/desktop/api/CredentialProvider/nn-credentialprovider-icredentialprovidercredentialwithfieldoptions)<br/></td>
<td>Provides a method that enables the credential provider framework to determine whether you've made a customization to a field's option in a logon or credential UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderEvents</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-icredentialproviderevents)<br/></td>
<td>Provides an asynchronous callback mechanism used by a credential provider to notify it of changes in the list of credentials or their fields.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderFilter</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-icredentialproviderfilter)<br/></td>
<td>Used to dynamically filter credential providers based on information available at runtime.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderSetUserArray</strong>](/windows/desktop/api/CredentialProvider/nn-credentialprovider-icredentialprovidersetuserarray)<br/></td>
<td>Provides a method that enables a credential provider to receive the set of users that will be shown in the logon or credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderUser</strong>](/windows/desktop/api/CredentialProvider/nn-credentialprovider-icredentialprovideruser)<br/></td>
<td>Provides methods used to retrieve certain properties of an individual user included in a logon or credential UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderUserArray</strong>](/windows/desktop/api/CredentialProvider/nn-credentialprovider-icredentialprovideruserarray)<br/></td>
<td>Represents the set of users that will appear in the logon or credential UI. This information enables the credential provider to enumerate the set to retrieve property information about each user to populate fields or filter the set.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICurrentItem</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Obtained by calling [<strong>IShellFolder::BindToObject</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject) for an item. If the item represents a snapshot of an item at a previous time, this interface will obtain the current version of the item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICurrentWorkingDirectory</strong>](/windows/desktop/api/Shlobj/)<br/></td>
<td>Exposes methods that enable a client to retrieve or set an object's current working directory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICustomDestinationList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icustomdestinationlist)<br/></td>
<td>Exposes methods that allow an application to provide a custom Jump List, including destinations and tasks, for display in the taskbar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDataObjectAsyncCapability</strong>](/windows/desktop/api/Shldisp/nn-shldisp-idataobjectasynccapability)<br/></td>
<td>Enables interfaces that are usually synchronous to function asynchronously. <br/>
<blockquote>
[!Note]<br />
This interface is the current, renamed version of [<strong>IAsyncOperation</strong>](https://www.bing.com/search?q=<strong>IAsyncOperation</strong>).
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDataObjectProvider</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idataobjectprovider)<br/></td>
<td>Provides methods that enable you to set or retrieve a [DataPackage](http://go.microsoft.com/fwlink/p/?linkid=267543) object's [<strong>IDataObject interface</strong>](https://msdn.microsoft.com/8a002deb-2727-456c-8078-a9b0d5893ed4), which the DataPackage uses to support interoperability. The DataPackage object is used by an app to provide data to another app.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDataTransferManagerInterop</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idatatransfermanagerinterop)<br/></td>
<td>Enables access to [<strong>DataTransferManager</strong>](https://msdn.microsoft.com/Windows.ApplicationModel.DataTransfer.DataTransferManager) methods in a Windows Store app that manages multiple windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDefaultExtractIconInit</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idefaultextracticoninit)<br/></td>
<td>Exposes methods to set default icons associated with an object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDefaultFolderMenuInitialize</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idefaultfoldermenuinitialize)<br/></td>
<td>Provides methods used to get and set shortcut menu information. This information is the same as that provided to [<strong>SHCreateDefaultContextMenu</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu) through the [<strong>DEFCONTEXTMENU</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-defcontextmenu) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDelayedPropertyStoreFactory</strong>](/windows/desktop/api/Propsys/nn-propsys-idelayedpropertystorefactory)<br/></td>
<td>Exposes a method to create a specified [<strong>IPropertyStore</strong>](https://msdn.microsoft.com/e995aaa1-d4c9-475f-b1fa-b9123cd5b653) object in circumstances where property access is potentially slow.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDelegateFolder</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idelegatefolder)<br/></td>
<td>Exposes a method through which a delegate folder is given the [<strong>IMalloc</strong>](https://msdn.microsoft.com/047f281e-2665-4d6d-9a0b-918cd3339447) interface required to allocate and free item IDs.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDelegateItem</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Used to obtain the immediately underlying representation of an item's path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDesktopGadget</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-idesktopgadget)<br/></td>
<td>Exposes a method that allows the programmatic addition of an installed gadget to the user's desktop.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDesktopWallpaper</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idesktopwallpaper)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IDestinationStreamFactory</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idestinationstreamfactory)<br/></td>
<td>Exposes a method for manually copying a stream or file before applying changes to properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDisplayItem</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Exposes methods that find a version of the current item to be used to get display properties, such as the item name, that will be displayed in the UI. Used by the copy engine dialogs to provide the UI with an appropriate item to display. If no other version can be found, the current item is used.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDockingWindow</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idockingwindow)<br/></td>
<td>Exposes methods that notify the docking window object of changes, including showing, hiding, and impending removal. This interface is implemented by window objects that can be docked within the border space of a Windows Explorer window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDockingWindowFrame</strong>](/windows/desktop/api/Shlobj/)<br/></td>
<td>Exposes methods that support the addition of [<strong>IDockingWindow</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idockingwindow) objects to a frame. Implemented by the browser.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDockingWindowSite</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes methods that manage the border space for one or more [<strong>IDockingWindow</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idockingwindow) objects. This interface is implemented by the browser and is similar to the [<strong>IOleInPlaceUIWindow</strong>](https://msdn.microsoft.com/3cfb31aa-9746-438c-af64-8236c170fe88) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDragSourceHelper</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idragsourcehelper)<br/></td>
<td>Exposed by the Shell to allow an application to specify the image that will be displayed during a Shell drag-and-drop operation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDragSourceHelper2</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-idragsourcehelper2)<br/></td>
<td>Exposes a method that adds functionality to [<strong>IDragSourceHelper</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idragsourcehelper). This method sets the characteristics of a drag-and-drop operation over an <strong>IDragSourceHelper</strong> object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDropTargetHelper</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idroptargethelper)<br/></td>
<td>Exposes methods that allow drop targets to display a drag image while the image is over the target window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDynamicHWHandler</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-idynamichwhandler)<br/></td>
<td>Called by AutoPlay. Exposes methods that get dynamic information regarding a registered handler prior to displaying it to the user.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumAssocHandlers</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumassochandlers)<br/></td>
<td>Exposes a method that allows enumeration of a collection of handlers associated with particular file name extensions.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumerableView</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ienumerableview)<br/></td>
<td>Exposes methods that enumerate the contents of a view and receive notification from callback upon enumeration completion. This interface enables clients of a view to attempt to share the view's list of folder contents.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumExplorerCommand</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumexplorercommand)<br/></td>
<td>Provided by an [<strong>IExplorerCommandProvider</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandprovider). This interface contains the enumeration of commands to be put into the command bar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumExtraSearch</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumextrasearch)<br/></td>
<td>A standard OLE enumerator used by a client to determine the available search objects for a folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumFullIDList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumfullidlist)<br/></td>
<td>Exposes a standard set of methods that enumerate the pointers to item identifier lists (PIDLs) of the items in a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumIDList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumidlist)<br/></td>
<td>Exposes a standard set of methods used to enumerate the PIDLs of the items in a Shell folder. When a folder's [<strong>IShellFolder::EnumObjects</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-enumobjects) method is called, it creates an enumeration object and passes a pointer to the object's [<strong>IEnumIDList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumidlist) interface back to the calling application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumObjects</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumobjects)<br/></td>
<td>Exposes methods to enumerate unknown objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumPublishedApps</strong>](/windows/desktop/api/Shappmgr/nn-shappmgr-ienumpublishedapps)<br/></td>
<td>Exposes methods that enumerate published applications to Add/Remove Programs in the Control Panel. The object exposing this interface is requested through [<strong>IAppPublisher::EnumApps</strong>](/windows/desktop/api/Shappmgr/nf-shappmgr-iapppublisher-enumapps). <br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumReadyCallback</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ienumreadycallback)<br/></td>
<td>Exposes methods that enable the view to notify the implementer when the enumeration has completed. The view calls this method to tell the implementer that the enumeration can be retrieved via [<strong>IEnumerableView::CreateEnumIDListFromContents</strong>](/windows/desktop/api/Shobjidl/nf-shobjidl-ienumerableview-createenumidlistfromcontents). The callback allows the implementer to share the views enumeration.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumResources</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumresources)<br/></td>
<td>Exposes resource enumeration methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumShellItems</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumshellitems)<br/></td>
<td>Exposes enumeration of [<strong>IShellItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) interfaces. This interface is typically obtained by calling the [<strong>IEnumShellItems</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumshellitems) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumSyncMgrConflict</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-ienumsyncmgrconflict)<br/></td>
<td>Exposes conflict enumeration methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumSyncMgrEvents</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-ienumsyncmgrevents)<br/></td>
<td>Exposes sync event enumeration methods.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumSyncMgrSyncItems</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-ienumsyncmgrsyncitems)<br/></td>
<td>Exposes methods that enumerate the sync item objects managed by the handler.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExecuteCommand</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexecutecommand)<br/></td>
<td>Exposes methods that set a given state or parameter related to the command verb, as well as a method to invoke that verb.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExecuteCommandApplicationHostEnvironment</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexecutecommandapplicationhostenvironment)<br/></td>
<td>Provides a single method that enables an application to determine whether its host is in desktop or immersive mode.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExecuteCommandHost</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexecutecommandhost)<br/></td>
<td>Provides a method that enables an [<strong>IExplorerCommand</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand)-based Shell verb handler to query the UI mode of the host component from which the application was invoked.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExplorerBrowser</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorerbrowser)<br/></td>
<td>[<strong>IExplorerBrowser</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorerbrowser) is a browser object that can be either navigated or that can host a view of a data object. As a full-featured browser object, it also supports an automatic travel log.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExplorerBrowserEvents</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorerbrowserevents)<br/></td>
<td>Exposes methods for notification of Explorer browser navigation and view creation events.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExplorerCommand</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand)<br/></td>
<td>Exposes methods that get the command appearance, enumerate subcommands, or invoke the command.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExplorerCommandProvider</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandprovider)<br/></td>
<td>Exposes methods to create Explorer commands and command enumerators.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExplorerCommandState</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandstate)<br/></td>
<td>Exposes a single method that allows retrieval of the command state.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExplorerPaneVisibility</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorerpanevisibility)<br/></td>
<td>Used in Windows Explorer by an [<strong>IShellFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder) implementation to give suggestions to the view about what panes are visible. Additionally, an [<strong>IExplorerBrowser</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorerbrowser) host can use this interface to provide information about pane visibility. The host should implement [<strong>QueryService</strong>](https://msdn.microsoft.com/windows/desktop/42026089-3e71-4483-ab35-1a6f305547fe) with <strong>SID_ExplorerPaneVisibility</strong> as the service ID. The host must be in the site chain. <br/> The [<strong>IExplorerPaneVisibility</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorerpanevisibility) implementation is retrieved from the Shell folder. The Shell folder, in turn, is retrieved from the view. A namespace extension can elect to provide a custom view ([<strong>IShellView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview)) rather than using the system folder view object (DefView). In that case, the <strong>IShellView</strong> implementation must include an implementation of [<strong>IFolderView::GetFolder</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ifolderview-getfolder) to return the <strong>IExplorerPaneVisibility</strong> object.<br/> A namespace extension can provide a custom view by implementing [<strong>IShellView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) itself rather than using the system folder view object (DefView). In that case, the <strong>IShellView</strong> implementation must include an implementation of [<strong>IFolderView::GetFolder</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ifolderview-getfolder) to make use of [<strong>IExplorerPaneVisibility</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorerpanevisibility) .<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExtractIcon</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes methods that allow a client to retrieve the icon that is associated with one of the objects in a folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExtractImage</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iextractimage)<br/></td>
<td>Exposes methods that request a thumbnail image from a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExtractImage2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iextractimage2)<br/></td>
<td>Extends the capabilities of [<strong>IExtractImage</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iextractimage).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileDialog</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ifiledialog)<br/></td>
<td>Exposes methods that initialize, show, and get results from the common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileDialog2</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ifiledialog2)<br/></td>
<td>Extends the [<strong>IFileDialog</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ifiledialog) interface by providing methods that allow the caller to name a specific, restricted location that can be browsed in the common file dialog as well as to specify alternate text to display as a label on the <strong>Cancel</strong> button.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileDialogControlEvents</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ifiledialogcontrolevents)<br/></td>
<td>Exposes methods that allow an application to be notified of events that are related to controls that the application has added to a common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileDialogCustomize</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifiledialogcustomize)<br/></td>
<td>Exposes methods that allow an application to add controls to a common file dialog.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileDialogEvents</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifiledialogevents)<br/></td>
<td>Exposes methods that allow notification of events within a common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileIsInUse</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileisinuse)<br/></td>
<td>Exposes methods that can be called to get information on or close a file that is in use by another application. When an application attempts to access a file and finds that file already in use, it can use the methods of this interface to gather information to present to the user in a dialog box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileOpenDialog</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ifileopendialog)<br/></td>
<td>Extends the [<strong>IFileDialog</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ifiledialog) interface by adding methods specific to the open dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileOperation</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperation)<br/></td>
<td>Exposes methods to copy, move, rename, create, and delete Shell items as well as methods to provide progress and error dialogs. This interface replaces the [<strong>SHFileOperation</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileOperationProgressSink</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperationprogresssink)<br/></td>
<td>Exposes methods that provide a rich notification system used by callers of [<strong>IFileOperation</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperation) to monitor the details of the operations they are performing through that interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileSaveDialog</strong>](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ifilesavedialog)<br/></td>
<td>Extends the [<strong>IFileDialog</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ifiledialog) interface by adding methods specific to the save dialog, which include those that provide support for the collection of metadata to be persisted with the file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileSyncMergeHandler</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifilesyncmergehandler)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IFileSystemBindData</strong>](https://msdn.microsoft.com/f5099bb3-21a7-4708-ac48-d32a14646614)<br/></td>
<td>Exposes methods that store file system information for optimizing calls to [<strong>IShellFolder::ParseDisplayName</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileSystemBindData2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifilesystembinddata2)<br/></td>
<td>Extends [<strong>IFileSystemBindData</strong>](https://msdn.microsoft.com/f5099bb3-21a7-4708-ac48-d32a14646614), which stores file system information for optimizing calls to [<strong>IShellFolder::ParseDisplayName</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname). This interface adds the ability set or get file ID or junction class identifier (CLSID).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileViewer</strong>](/windows/desktop/api/Shlobj/)<br/></td>
<td>Exposes methods that designate an interface that allows a registered file viewer to be notified when it must show or print a file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileViewerSite</strong>](/windows/desktop/api/Shlobj/)<br/></td>
<td>Exposes methods that designate an interface that allows a file viewer to retrieve the handle to the current pinned window, or to set a new pinned window. The pinned window is the window in which the current file viewer displays a file. When the user selects a new file to view, the Shell directs the file viewer to display the new file in the pinned window rather than create a new window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderFilter</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifolderfilter)<br/></td>
<td>Exposed by a client to specify how to filter the enumeration of a Shell folder by a server application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFolderFilterSite</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifolderfiltersite)<br/></td>
<td>Exported by a host to allow clients to specify how to filter a Shell folder enumeration.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifolderview)<br/></td>
<td>Exposes methods that retrieve information about a folder's display options, select specified items in that folder, and set the folder's view mode.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFolderView2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifolderview2)<br/></td>
<td>Exposes methods that retrieve information about a folder's display options, select specified items in that folder, and set the folder's view mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderViewHost</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ifolderviewhost)<br/></td>
<td>Exposes a method that hosts an [<strong>IFolderView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifolderview) object in a window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFolderViewOptions</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ifolderviewoptions)<br/></td>
<td>Exposes methods that allow control of folder view options specific to the Windows 7 and later views.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderViewSettings</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifolderviewsettings)<br/></td>
<td>Exposes methods to obtain folder view settings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFrameworkInputPane</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iframeworkinputpane)<br/></td>
<td>Provides methods that enable apps to be informed of state changes and location for the input pane.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFrameworkInputPaneHandler</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iframeworkinputpanehandler)<br/></td>
<td>Enables an app to be notified when the input pane (the on-screen keyboard or handwriting panel) is being shown or hidden. This allows the app window to adjust its display so that no input areas (such as a text box) are obscured by the input pane.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IHandlerActivationHost</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ihandleractivationhost)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IHandlerInfo</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ihandlerinfo)<br/></td>
<td>Supplies methods that provide information about the handler to methods of the [<strong>IHandlerActivationHost</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ihandleractivationhost) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IHomeGroup</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ihomegroup)<br/></td>
<td>Exposes methods that determine a computer's HomeGroup membership status and display the sharing wizard.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IHWEventHandler</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ihweventhandler)<br/></td>
<td>Called by AutoPlay to implement the handling of registered media types.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IHWEventHandler2</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ihweventhandler2)<br/></td>
<td>Extends the [<strong>IHWEventHandler</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ihweventhandler) interface to address User Account Control (UAC) elevation for device handlers.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IIdentityName</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Exposes methods to compare two items to see if they are the same.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IImageRecompress</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iimagerecompress)<br/></td>
<td>Exposes a method that recompress images.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeCommand</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iinitializecommand)<br/></td>
<td>Exposes a single method used to initialize objects that implement [<strong>IExplorerCommandState</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandstate), [<strong>IExecuteCommand</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexecutecommand) or [<strong>IDropTarget</strong>](https://msdn.microsoft.com/13fbe834-1ef8-4944-b2e4-9f5c413c65c8) with the application-specified command name and its registered properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeNetworkFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iinitializenetworkfolder)<br/></td>
<td>Exposes a method that initializes the network data source CLSID_NetworkPlaces as specified.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeWithBindCtx</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iinitializewithbindctx)<br/></td>
<td>Exposes a method that initializes a handler, such as a property handler, thumbnail handler, or preview handler, with a bind context.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeWithFile</strong>](/windows/desktop/api/Propsys/nn-propsys-iinitializewithfile)<br/></td>
<td>Exposes a method to initialize a handler, such as a property handler, thumbnail handler, or preview handler, with a file path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeWithItem</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-iinitializewithitem)<br/></td>
<td>Exposes a method used to initialize a handler, such as a property handler, thumbnail handler, or preview handler, with an [<strong>IShellItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeWithPropertyStore</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iinitializewithpropertystore)<br/></td>
<td>Exposes a method that initializes a handler, such as a property handler, thumbnail handler, or preview handler, with a property store.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeWithStream</strong>](/windows/desktop/api/Propsys/nn-propsys-iinitializewithstream)<br/></td>
<td>Exposes a method that initializes a handler, such as a property handler, thumbnail handler, or preview handler, with a stream.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeWithWindow</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iinitializewithwindow)<br/></td>
<td>Exposes a method through which a client can provide an owner window to a Windows Runtime object used in a desktop application.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInputObject</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-iinputobject)<br/></td>
<td>Exposes methods that change UI activation and process accelerators for a user input object contained in the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInputObject2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iinputobject2)<br/></td>
<td>Exposes a method that extends [<strong>IInputObject</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-iinputobject) by handling global accelerators.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInputObjectSite</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iinputobjectsite)<br/></td>
<td>Exposes a method that is used to communicate focus changes for a user input object contained in the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInputPanelConfiguration</strong>](/windows/desktop/api/inputpanelconfiguration/nn-inputpanelconfiguration-iinputpanelconfiguration)<br/></td>
<td>Provides functionality for desktop apps to opt in to the focus tracking mechanism used in Windows Store apps.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInputPanelInvocationConfiguration</strong>](/windows/desktop/api/inputpanelconfiguration/nn-inputpanelconfiguration-iinputpanelinvocationconfiguration)<br/></td>
<td>Enables Windows Store apps to opt out of the automatic invocation behavior.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IIOCancelInformation</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iiocancelinformation)<br/></td>
<td>Exposes methods for posting a cancel window message to the process thread from the Progress Dialog. <br/> This interface enables the progress dialog to post a thread message through [<strong>PostThreadMessage</strong>](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\windowing\messagesandmessagequeues\messagesandmessagequeuesreference\messagesandmessagequeuesfunctions\postthreadmessage.htm) to the worker thread to cancel its operations. The worker thread must periodically check the message queue through [<strong>GetMessage</strong>](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\windowing\messagesandmessagequeues\messagesandmessagequeuesreference\messagesandmessagequeuesfunctions\getmessage.htm), [<strong>PeekMessage</strong>](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\windowing\messagesandmessagequeues\messagesandmessagequeuesreference\messagesandmessagequeuesfunctions\peekmessage.htm) or [<strong>MsgWaitForMultipleObjectsEx</strong>](https://msdn.microsoft.com/1774b721-3ad4-492e-96af-b71de9066f0c).<br/> The [<strong>IIOCancelInformation::SetCancelInformation</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iiocancelinformation-setcancelinformation) method tells the progress dialog which thread ID and what message to [<strong>PostThreadMessage</strong>](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\windowing\messagesandmessagequeues\messagesandmessagequeuesreference\messagesandmessagequeuesfunctions\postthreadmessage.htm) when the user clicks <strong>Cancel</strong>. A thread ID of &quot;zero&quot; disables the sending operation for the cancel message.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IItemNameLimits</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iitemnamelimits)<br/></td>
<td>Retrieves a list of valid and invalid characters or the maximum length of a name in the namespace. Use this interface for validation parsing and translation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IKnownFolder</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfolder)<br/></td>
<td>Exposes methods that allow an application to retrieve information about a known folder's category, type, GUID, PIDL value, redirection capabilities, and definition. It provides a method for the retrival of a known folder's [<strong>IShellItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) object. It also provides methods to get or set the path of the known folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IKnownFolderManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfoldermanager)<br/></td>
<td>Exposes methods that create, enumerate or manage existing known folders.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILaunchSourceAppUserModelId</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ilaunchsourceappusermodelid)<br/></td>
<td>Provides a method for retrieving an [AppUserModelId](appids.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILaunchSourceViewSizePreference</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ilaunchsourceviewsizepreference)<br/></td>
<td>Provides methods for retrieving information about the source application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILaunchTargetMonitor</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ilaunchtargetmonitor)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>ILaunchTargetViewSizePreference</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ilaunchtargetviewsizepreference)<br/></td>
<td>Provides a method for retrieving the preferred view size for a new application window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMarkupCallback</strong>](/windows/desktop/api/Shobjidl/)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IMenuPopup</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-imenupopup)<br/></td>
<td>[<strong>IMenuPopup</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-imenupopup) may be altered or unavailable.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IModalWindow</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-imodalwindow)<br/></td>
<td>Exposes a method that represents a modal window. This interface is used in the Windows XP Passport Wizard.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMultiMonitorDockingSite</strong>](imultimonitordockingsite.md)<br/></td>
<td>Implemented by the browser. Exposes methods that manage which monitor contains the Windows taskbar on a multiple monitor system. <br/></td>
</tr>
<tr class="even">
<td>[<strong>INamedPropertyBag</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes methods that provide an object with a specified property bag in which the object can save its properties.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INamedPropertyStore</strong>](/windows/desktop/api/Propsys/nn-propsys-inamedpropertystore)<br/></td>
<td>Exposes methods that get and set named properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeAccessible</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-inamespacetreeaccessible)<br/></td>
<td>Exposes methods that perform accessibility actions on a Shell item from a namespace tree control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INameSpaceTreeControl</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacetreecontrol)<br/></td>
<td>Exposes methods used to view and manipulate nodes in a tree of Shell items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeControl2</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-inamespacetreecontrol2)<br/></td>
<td>Extends the [<strong>INameSpaceTreeControl</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacetreecontrol) interface by providing methods that get and set the display styles of treeview controls for use with Shell namespace items.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INameSpaceTreeControlCustomDraw</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-inamespacetreecontrolcustomdraw)<br/></td>
<td>Exposes methods that enable the user to draw a custom namespace tree control and its items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeControlDropHandler</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-inamespacetreecontroldrophandler)<br/></td>
<td>Exposes handler methods for drag-and-drop. Used by the namespace tree control to notify the client of any drag-and-drop operation happening within the control. Provides a way for a client to intercept a drop operation and perform its own action, or to return the desired drop effect.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INameSpaceTreeControlEvents</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-inamespacetreecontrolevents)<br/></td>
<td>Exposes methods for handling [<strong>INameSpaceTreeControl</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacetreecontrol) events.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeControlFolderCapabilities</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacetreecontrolfoldercapabilities)<br/></td>
<td>Exposes a single method that retrieves the status of a folder's [System.IsPinnedToNameSpaceTree](https://msdn.microsoft.com/00937acb-1ce2-44f6-96a1-69e5dbb665f6) filtering support.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INamespaceWalk</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacewalk)<br/></td>
<td>Exposes methods that walk a namespace from a given root node. The depth of the walk is specified and an optional array is returned containing the IDs of all nodes walked.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INamespaceWalkCB</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacewalkcb)<br/></td>
<td>A callback interface exposing methods used with [<strong>INamespaceWalk</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacewalk). After performing a walk with <strong>INamespaceWalk</strong>, an [<strong>IShellFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder) object representing the walked nodes is passed to the [<strong>INamespaceWalkCB</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacewalkcb) methods. What those methods do with the information depends on the object that is implementing them.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INamespaceWalkCB2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacewalkcb2)<br/></td>
<td>Extends [<strong>INamespaceWalkCB</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacewalkcb) with a method that is required in order to complete a namespace walk. This method removes data collected during the walk. <br/></td>
</tr>
<tr class="even">
<td>[<strong>INewMenuClient</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inewmenuclient)<br/></td>
<td>Exposes methods that allow manipulation of items in a Windows 7 menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INewShortcutHook</strong>](/windows/desktop/api/Shlobj/)<br/></td>
<td>Exposes methods to create a new Internet shortcut.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INewWindowManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inewwindowmanager)<br/></td>
<td>Exposes a method that determines whether a window that is launched by another window should be displayed or blocked, allowing control of pop-up windows.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INotifyReplica</strong>](/windows/desktop/api/Reconcil/)<br/></td>
<td>Exposes a method that provides an object's creator with the means to notify the object that it may be subject to subsequent reconciliation. The briefcase reconciler is responsible for implementing this interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectArray</strong>](/windows/desktop/api/Objectarray/nn-objectarray-iobjectarray)<br/></td>
<td>Exposes methods that enable clients to access items in a collection of objects that support [<strong>IUnknown</strong>](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectCollection</strong>](/windows/desktop/api/objectarray/nn-objectarray-iobjectcollection)<br/></td>
<td>Extends the [<strong>IObjectArray</strong>](/windows/desktop/api/Objectarray/nn-objectarray-iobjectarray) interface by providing methods that enable clients to add and remove objects that support [<strong>IUnknown</strong>](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) in a collection.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectProvider</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iobjectprovider)<br/></td>
<td>Exposes a method to discover objects that are named with a <strong>GUID</strong> from another object. Unlike [<strong>QueryService</strong>](https://msdn.microsoft.com/windows/desktop/42026089-3e71-4483-ab35-1a6f305547fe) this interface will not delegate its functionality on to other objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithAppUserModelID</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iobjectwithappusermodelid)<br/></td>
<td>Exposes methods that allow implementers of a custom [<strong>IAssocHandler</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iassochandler) object to provide access to its explicit Application User Model ID (AppUserModelID). This information is used to determine whether a particular file type can be added to an application's Jump List.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectWithBackReferences</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iobjectwithbackreferences)<br/></td>
<td>Provides a method for interacting with back references held by an object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithCancelEvent</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iobjectwithcancelevent)<br/></td>
<td>Supplies a caller with an event that will be signaled by the called object to denote cancellation of a task.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectWithFolderEnumMode</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iobjectwithfolderenummode)<br/></td>
<td>Exposes methods that get and set enumeration modes of a parsed item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithProgID</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iobjectwithprogid)<br/></td>
<td>Exposes methods that provide access to the ProgID associated with an object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectWithPropertyKey</strong>](/windows/desktop/api/Propsys/nn-propsys-iobjectwithpropertykey)<br/></td>
<td>Exposes methods for getting and setting the property key.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithSelection</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iobjectwithselection)<br/></td>
<td>Exposes methods that get or set selected items represented by a Shell item array.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjMgr</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes methods that allow a client to append or remove an object from a collection of objects managed by a server object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOpenControlPanel</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iopencontrolpanel)<br/></td>
<td>Exposes methods that retrieve the view state of the Control Panel, the path of individual Control Panel items, and that open either the Control Panel itself or an individual Control Panel item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOpenSearchSource</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iopensearchsource)<br/></td>
<td>Exposes a method to get search results from a custom client-side OpenSearch data source.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOperationsProgressDialog</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ioperationsprogressdialog)<br/></td>
<td>Exposes methods to get, set, and query a progress dialog.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPackageDebugSettings</strong>](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ipackagedebugsettings)<br/></td>
<td>Enables debugger developers to control the life cycle of a Windows Store app, such as suspending or resuming.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPackageExecutionStateChangeNotification</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipackageexecutionstatechangenotification)<br/></td>
<td>Enables receiving package state-change notifications during Windows Store app debugging.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IParentAndItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iparentanditem)<br/></td>
<td>Exposes methods that get and set the parent and the parent's child ID. While [<strong>IParentAndItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iparentanditem) is typically implemented on IShellItems, it is not specific to [<strong>IShellItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem). <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IParseAndCreateItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iparseandcreateitem)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IPersistFolder</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder)<br/></td>
<td>Exposes a method that initializes Shell folder objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPersistFolder2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder2)<br/></td>
<td>Exposes methods that obtain information from Shell folder objects.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPersistFolder3</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder3)<br/></td>
<td>Extends the [<strong>IPersistFolder</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder) and [<strong>IPersistFolder2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder2) interfaces by allowing a folder object to implement nondefault handling of folder shortcuts.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPersistIDList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistidlist)<br/></td>
<td>Exposes methods that are used to persist item identifier lists.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPersistSerializedPropStorage</strong>](/windows/desktop/api/Propsys/nn-propsys-ipersistserializedpropstorage)<br/></td>
<td>Exposes methods to persist serialized property storage data for later use and to restore persisted data to a new property store instance.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPersistSerializedPropStorage2</strong>](/windows/desktop/api/Propsys/nn-propsys-ipersistserializedpropstorage2)<br/></td>
<td>Exposes methods to persist serialized property storage data for later use and to restore persisted data to a new property store instance.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPlaybackManager</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Provides methods that allow media applications to communicate with the Windows playback manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPlaybackManagerEvents</strong>](/windows/desktop/api/Shobjidl/)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IPreviewHandler</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ipreviewhandler)<br/></td>
<td>Exposes methods for the display of rich previews.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPreviewHandlerFrame</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ipreviewhandlerframe)<br/></td>
<td>Enables preview handlers to pass keyboard shortcuts to the host. This interface retrieves a list of keyboard shortcuts and directs the host to handle a keyboard shortcut.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPreviewHandlerVisuals</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ipreviewhandlervisuals)<br/></td>
<td>Exposes methods for applying color and font information to preview handlers.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPreviewItem</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Identifies an item that will be shown in the preview pane.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPreviousVersionsInfo</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ipreviousversionsinfo)<br/></td>
<td>Exposes a method that checks for previous versions of server files or folders, stored for the purpose of reversion by the <em>shadow copies</em> technology provided with Windows Server 2003.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPrivateIdentityManager</strong>](iprivateidentitymanager.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IPrivateIdentityManager2</strong>](iprivateidentitymanager2.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IProfferService</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iprofferservice)<br/></td>
<td>Exposes a general mechanism for objects to offer services to other objects on the same host.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IProgressDialog</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes methods that provide options for an application to display a progress dialog box. This interface is exported by the progress dialog box object (CLSID_ProgressDialog). This object is a generic way to show a user how an operation is progressing. It is typically used when deleting, uploading, copying, moving, or downloading large numbers of files.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPublishedApp</strong>](/windows/desktop/api/Shappmgr/nn-shappmgr-ipublishedapp)<br/></td>
<td>Exposes methods that represent applications to Add/Remove Programs in Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IPublishedApp2</strong>](/windows/desktop/api/Shappmgr/nn-shappmgr-ipublishedapp2)<br/></td>
<td>Extends the [<strong>IPublishedApp</strong>](/windows/desktop/api/Shappmgr/nn-shappmgr-ipublishedapp) interface by providing an additional installation method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPublishingWizard</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ipublishingwizard)<br/></td>
<td>Exposes methods for working with the Online Print Wizard, the Web Publishing Wizard, and the Add Network Place Wizard. In Windows Vista, [<strong>IPublishingWizard</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ipublishingwizard) no longer supports the Web Publishing Wizard or Online Print Wizard.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IQueryAssociations</strong>](/windows/desktop/api/Shlwapi/)<br/></td>
<td>Exposes methods that simplify the process of retrieving information stored in the registry in association with defining a file type or protocol and associating it with an application.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IQueryCancelAutoPlay</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iquerycancelautoplay)<br/></td>
<td>Exposes a method that programmatically overrides [AutoPlay](autorun2k-intro.md) or [AutoRun](autoplay.md). This allows you to customize the location and type of content that is launched when media is inserted.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IQueryCodePage</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iquerycodepage)<br/></td>
<td>Gets and sets the numeric value (Code Page identifier) of the ANSI code page.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IQueryContinue</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iquerycontinue)<br/></td>
<td>Exposes a method that provides a simple, standard mechanism for objects to query a client for permission to continue an operation. Clients of [<strong>IUserNotification</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iusernotification), for example, must pass an implementation of [<strong>IQueryContinue</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iquerycontinue) to the [<strong>IUserNotification::Show</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iusernotification-show) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IQueryContinueWithStatus</strong>](/windows/desktop/api/Credentialprovider/nn-credentialprovider-iquerycontinuewithstatus)<br/></td>
<td>Exposes methods that provide a standard mechanism for credential providers to call [<strong>QueryContinue</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iquerycontinue-querycontinue) while attempting to connect to the network to determine if they should continue these attempts. Credential providers can also use this interface to display messages to the user while attempting to establish a network connection.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IQueryInfo</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes methods that the Shell uses to retrieve flags and info tip information for an item that resides in an [<strong>IShellFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder) implementation. Info tips are usually displayed inside a [tooltip](https://msdn.microsoft.com/windows/desktop/1020cec7-57b4-4463-9419-f80fd14fa12c) control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IRelatedItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-irelateditem)<br/></td>
<td>Exposes methods that derive related items with specific relationships.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IRemoteComputer</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iremotecomputer)<br/></td>
<td>Exposes a method that enumerates or initializes a namespace extension when it is invoked on a remote object. This interface is used, for example, to initialize the remote printers virtual folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IResolveShellLink</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iresolveshelllink)<br/></td>
<td>Exposes a method that enables an application to request that a Shell folder object resolve a link for one of its items.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IResultsFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iresultsfolder)<br/></td>
<td>Exposes methods that hold items from a data object.<br/> An [<strong>IResultsFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iresultsfolder) is a folder that can hold items from all over the namespace and represent them to the user in a single folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IRunnableTask</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-irunnabletask)<br/></td>
<td>A free-threaded interface that can be exposed by an object to allow operations to be performed on a background thread. For example, if the [<strong>IExtractImage::GetLocation</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iextractimage-getlocation) method returns E_PENDING, the calling application is permitted to extract the image on a background thread.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISearchBoxInfo</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-isearchboxinfo)<br/></td>
<td>Exposes methods that allow the caller to retrieve information entered into a search box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISearchContext</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes methods that channel customization information to the search hooks.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISearchFolderItemFactory</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-isearchfolderitemfactory)<br/></td>
<td>Exposes methods that create and modify search folders. The Set methods are called first to set up the parameters of the search. When not called, default values will be used instead. [<strong>ISearchFolderItemFactory::GetIDList</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-isearchfolderitemfactory-getidlist) and [<strong>ISearchFolderItemFactory::GetShellItem</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-isearchfolderitemfactory-getshellitem) return the two forms of the search specified by these parameters. <br/></td>
</tr>
<tr class="even">
<td>[<strong>ISharedBitmap</strong>](/windows/desktop/api/Thumbcache/nn-thumbcache-isharedbitmap)<br/></td>
<td>Exposes memory-efficient methods for accessing bitmaps. This interface is used as a thin wrapper around HBITMAP objects, allowing those objects to be reference counted and protected from having their underlying data changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISharingConfigurationManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-isharingconfigurationmanager)<br/></td>
<td>Exposes methods that set and retrieve information about a computer's default sharing settings for the <strong>Users</strong> (<code>C:\Users</code>) or <strong>Public</strong> (<code>C:\Users\Public</code>) folder. Also exposes a set of methods that allow control of printer sharing.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellApp</strong>](/windows/desktop/api/Shappmgr/nn-shappmgr-ishellapp)<br/></td>
<td>Exposes methods that provide general information about an application to the Add/Remove Programs Application. You cannot use it outside the Add/Remove Programs application. The information given by this interface includes a list of supported management actions and whether the application is currently installed. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellBrowser</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellbrowser)<br/></td>
<td>Implemented by hosts of Shell views (objects that implement [<strong>IShellView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview)). Exposes methods that provide services for the view it is hosting and other objects that run in the context of the Explorer window. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellChangeNotify</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes a method that notifies a Shell namespace extension when the ID of an item has changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellDetails</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposed by Shell folders to provide detailed information about the items in a folder. This is the same information that is displayed by the Windows Explorer when the view of the folder is set to Details. For Windows 2000 and later systems, [<strong>IShellDetails</strong>](/windows/desktop/api/Shlobj_core/) is superseded by [<strong>IShellFolder2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellfolder2).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellExtInit</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellextinit)<br/></td>
<td>Exposes a method that initializes Shell extensions for property sheets, shortcut menus, and drag-and-drop handlers (extensions that add items to shortcut menus during nondefault drag-and-drop operations).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder)<br/></td>
<td>Exposed by all Shell namespace folder objects, its methods are used to manage folders.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolder2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellfolder2)<br/></td>
<td>Extends the capabilities of [<strong>IShellFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder). Its methods provide a variety of information about the contents of a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolderSearchable</strong>](ishellfoldersearchable.md)<br/></td>
<td>Exposes methods that allow a Shell extension to provide a searchable namespace.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolderSearchableCallback</strong>](ishellfoldersearchablecallback.md)<br/></td>
<td>Exposes callback routines to monitor the search process.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolderViewCB</strong>](/windows/desktop/api/Shlobj/)<br/></td>
<td>Exposes a method that allows communication between Windows Explorer and a folder view implemented using the system folder view object (the [<strong>IShellView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) object returned through [<strong>SHCreateShellFolderView</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreateshellfolderview)) so that the folder view can be notified of events and modify its view accordingly.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolderViewDual</strong>](/windows/desktop/api/Shldisp/nn-shldisp-ishellfolderviewdual)<br/></td>
<td>Exposes methods that modify the view and select items in the current folder. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolderViewDual2</strong>](/windows/desktop/api/Shldisp/nn-shldisp-ishellfolderviewdual2)<br/></td>
<td>Exposes methods that modify the view and select items in the current folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolderViewDual3</strong>](/windows/desktop/api/Shldisp/nn-shldisp-ishellfolderviewdual3)<br/></td>
<td>Exposes methods that modify the current folder view.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolderViewType</strong>](ishellfolderviewtype.md)<br/></td>
<td>Exposes methods that enable a Shell folder to support different views on its content (different hierarchical layouts of its data).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellIcon</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellicon)<br/></td>
<td>Exposes a method that obtains an icon index for an [<strong>IShellFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder) object. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellIconOverlay</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes methods that are used by a namespace extension to specify icon overlays for the objects it contains.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellIconOverlayIdentifier</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelliconoverlayidentifier)<br/></td>
<td>Exposes methods that handle all communication between icon overlay handlers and the Shell.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellImageDataAbort</strong>](/windows/desktop/api/Shimgdata/nn-shimgdata-ishellimagedataabort)<br/></td>
<td>Exposes a single method used to abort [<strong>IShellImageData</strong>](/windows/desktop/api/Shimgdata/nn-shimgdata-ishellimagedata) processes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellImageDataFactory</strong>](/windows/desktop/api/Shimgdata/nn-shimgdata-ishellimagedatafactory)<br/></td>
<td>Exposes methods that create [<strong>IShellImageData</strong>](/windows/desktop/api/Shimgdata/nn-shimgdata-ishellimagedata) instances based on various image sources.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem)<br/></td>
<td>Exposes methods that retrieve information about a Shell item. [<strong>IShellItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) and [<strong>IShellItem2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem2) are the preferred representations of items in any new code.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellItem2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem2)<br/></td>
<td>Extends [<strong>IShellItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) with methods that retrieve various property values of the item. <strong>IShellItem</strong> and [<strong>IShellItem2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem2) are the preferred representations of items in any new code.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellItemArray</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitemarray)<br/></td>
<td>Exposes methods that create and manipulate [<strong>Shell item</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) arrays.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellItemFilter</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitemfilter)<br/></td>
<td>Exposed by a client to specify how to filter the enumeration of a [<strong>Shell item</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) by a server application.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellItemImageFactory</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory)<br/></td>
<td>Exposes a method to return either icons or thumbnails for Shell items. If no thumbnail or icon is available for the requested item, a per-class icon may be provided from the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellItemResources</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitemresources)<br/></td>
<td>Exposes methods to manipulate and query Shell item resources.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellLibrary</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllibrary)<br/></td>
<td>Exposes methods for creating and managing libraries.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellLink</strong>](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka)<br/></td>
<td>Exposes methods that create, modify, and resolve Shell links.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellLinkDataList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinkdatalist)<br/></td>
<td>Exposes methods that allow an application to attach extra data blocks to a [Shell link](https://msdn.microsoft.com/32ad306d-54bd-4130-ad30-08db50ef106e). These methods add, copy, or remove data blocks.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellMenu</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellmenu)<br/></td>
<td>Exposes methods that interact with Shell menus such as the <strong>Start</strong> menu, and the <strong>Favorites</strong> menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellMenuCallback</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellmenucallback)<br/></td>
<td>A callback interface that exposes a method that receives messages from a menu band.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellPropSheetExt</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellpropsheetext)<br/></td>
<td>Exposes methods that allow a property sheet handler to add or replace pages in the property sheet displayed for a file object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellRunDll</strong>](/windows/desktop/api/shobjidl/nn-shobjidl-ishellrundll)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IShellView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview)<br/></td>
<td>Exposes methods that present a view in the Windows Explorer or folder windows.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellView2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview2)<br/></td>
<td>Extends the capabilities of [<strong>IShellView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellView3</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ishellview3)<br/></td>
<td>Extends the capabilities of [<strong>IShellView2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview2) by providing a method to replace [<strong>IShellView2::CreateViewWindow2</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview2-createviewwindow2).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellWindows</strong>](/windows/desktop/api/Exdisp/nn-exdisp-ishellwindows)<br/></td>
<td>Provides access to the collection of open Shell windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IStartMenuPinnedList</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-istartmenupinnedlist)<br/></td>
<td>Exposes a method that unpins an application shortcut from the <strong>Start</strong> menu or the taskbar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IStorageProviderHandler</strong>](/windows/desktop/api/storageprovider/nn-storageprovider-istorageproviderhandler)<br/></td>
<td>Retrieves the [<strong>IStorageProviderPropertyHandler</strong>](/windows/desktop/api/storageprovider/nn-storageprovider-istorageproviderpropertyhandler) associated with a specific file or folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IStorageProviderPropertyHandler</strong>](/windows/desktop/api/storageprovider/nn-storageprovider-istorageproviderpropertyhandler)<br/></td>
<td>Provides a collection of properties associated with a file or folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IStreamAsync</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-istreamasync)<br/></td>
<td>Exposes methods to manage input/outpout (I/O) to an asynchronous stream. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IStreamUnbufferedInfo</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-istreamunbufferedinfo)<br/></td>
<td>Exposes a method that determines the sector size as an aid to byte alignment.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISuspensionDependencyManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-isuspensiondependencymanager)<br/></td>

</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflict</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrconflict)<br/></td>
<td>Exposes methods that provide information about a conflict retrieved from a conflict store, and allows the conflict to be resolved.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrConflictFolder</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrconflictfolder)<br/></td>
<td>Exposes a method that gets the conflict ID list for a conflict object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflictItems</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrconflictitems)<br/></td>
<td>Exposes methods that get conflict item data and item count.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrConflictPresenter</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrconflictpresenter)<br/></td>
<td>Exposes a method that presents a conflict to the user.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflictResolutionItems</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrconflictresolutionitems)<br/></td>
<td>Exposes methods that get item info and item count.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrConflictResolveInfo</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrconflictresolveinfo)<br/></td>
<td>Exposes methods that get and set information about sync manager conflict resolution.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflictStore</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrconflictstore)<br/></td>
<td>Exposes methods that allow a handler to provide conflicts that appear in the Conflicts folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrControl</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrcontrol)<br/></td>
<td>Exposes methods that allow an application or handler to start or stop a synchronization, notify Sync Center of changes to the set of handlers or items, or notify of changes to property values.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrEnumItems</strong>](/windows/desktop/api/mobsync/nn-mobsync-isyncmgrenumitems)<br/></td>
<td>Exposes methods that enumerate through an array of [<strong>SYNCMGRITEM</strong>](/windows/desktop/api/Mobsync/ns-mobsync-_tagsyncmgritem) structures. Each of these structures provides information about an item that can be synchronized. [<strong>ISyncMgrEnumItems</strong>](/windows/desktop/api/mobsync/nn-mobsync-isyncmgrenumitems) has the same methods as all standard enumerator interfaces: Next, Skip, Reset, and Clone.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrEvent</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrevent)<br/></td>
<td>Exposes methods that retrieve data from an event store. An event store allows Sync Center to get an enumerator of all events in the store, as well as to retrieve individual events.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrEventLinkUIOperation</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgreventlinkuioperation)<br/></td>
<td>Provides a method that is called when event links are clicked in the sync results folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrEventStore</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgreventstore)<br/></td>
<td>Exposes methods that allow a handler to provide its own event store and manage its own sync events, instead of using the default Sync Center event store. These events are displayed in the Sync Results folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrHandler</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrhandler)<br/></td>
<td>Exposes methods that make up the primary interface implemented by a sync handler. Sync Center creates one instance of the handler through this interface to get properties, enumerate sync items, and modify state. Sync Center creates a separate instance of the handler on a separate thread to perform a synchronization or a UI operation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrHandlerCollection</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrhandlercollection)<br/></td>
<td>Exposes methods that provide an enumerator of sync handler IDs and instantiate those sync handlers.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrHandlerInfo</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrhandlerinfo)<br/></td>
<td>Exposes methods that allow a handler to provide property and state information to Sync Center.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrRegister</strong>](/windows/desktop/api/Mobsync/nn-mobsync-isyncmgrregister)<br/></td>
<td>Exposes methods so that an application can register with the synchronization manager. This can be achieved either through the [<strong>ISyncMgrRegister</strong>](/windows/desktop/api/Mobsync/nn-mobsync-isyncmgrregister) interface or by registering directly in the registry.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrResolutionHandler</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrresolutionhandler)<br/></td>
<td>Exposes methods that manage synchronizing conflicts. Implement this interface to construct a sync conflict handler. The conflict resolution user interface (UI) will call this interface to resolve the conflict presented to the user. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrScheduleWizardUIOperation</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrschedulewizarduioperation)<br/></td>
<td>Exposes a method that allows a handler to display the sync schedule wizard for the handler.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSessionCreator</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsessioncreator)<br/></td>
<td>Exposes a single method through which a handler or external application can notify Sync Center that synchronization has begun, as well as report progress and events.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSyncCallback</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsynccallback)<br/></td>
<td>Exposes methods that allow a synchronization process to report progress and events to Sync Center, or to query whether the process has been canceled.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSynchronize</strong>](/windows/desktop/api/Mobsync/nn-mobsync-isyncmgrsynchronize)<br/></td>
<td>Exposes methods that enable the registered application or service to receive notifications from the synchronization manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSynchronizeCallback</strong>](/windows/desktop/api/mobsync/nn-mobsync-isyncmgrsynchronizecallback)<br/></td>
<td>Exposes methods that manage the synchronization process.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSynchronizeInvoke</strong>](/windows/desktop/api/Mobsync/nn-mobsync-isyncmgrsynchronizeinvoke)<br/></td>
<td>Exposes methods that enable a registered application to invoke the synchronization manager to update items.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSyncItem</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsyncitem)<br/></td>
<td>Exposes methods that act on and retrieve information from a single sync item, allowing handlers to manage sync items as independent objects.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSyncItemContainer</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsyncitemcontainer)<br/></td>
<td>Exposes methods that provide information to handlers about the items they contain.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSyncItemInfo</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsynciteminfo)<br/></td>
<td>Exposes methods that provide property and state information for a single sync item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSyncResult</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrsyncresult)<br/></td>
<td>Exposes a method that applications calling [<strong>ISyncMgrControl</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrcontrol) can use to get the result of a [<strong>ISyncMgrControl::StartHandlerSync</strong>](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrcontrol-starthandlersync) or [<strong>ISyncMgrControl::StartItemSync</strong>](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrcontrol-startitemsync) call.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrUIOperation</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgruioperation)<br/></td>
<td>Exposes a method through which a sync handler or sync item can display a UI object when requested to do so by Sync Center.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITaskbarList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist)<br/></td>
<td>Exposes methods that control the taskbar. It allows you to dynamically add, remove, and activate items on the taskbar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITaskbarList2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist2)<br/></td>
<td>Extends the [<strong>ITaskbarList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist) interface by exposing a method to mark a window as a full-screen display.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITaskbarList3</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist3)<br/></td>
<td>Extends [<strong>ITaskbarList2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist2) by exposing methods that support the unified launching and switching taskbar button functionality added in Windows 7. This functionality includes thumbnail representations and switch targets based on individual tabs in a tabbed application, thumbnail toolbars, notification and status overlays, and progress indicators.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITaskbarList4</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist4)<br/></td>
<td>Extends [<strong>ITaskbarList3</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist3) by providing a method that allows the caller to control two property values for the tab thumbnail and peek feature.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IThumbnailCache</strong>](/windows/desktop/api/Thumbcache/nn-thumbcache-ithumbnailcache)<br/></td>
<td>Exposes methods for a system thumbnail cache that is shared across applications.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IThumbnailCachePrimer</strong>](/windows/desktop/api/thumbcache/nn-thumbcache-ithumbnailcacheprimer)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IThumbnailHandlerFactory</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ithumbnailhandlerfactory)<br/></td>
<td>Exposes a method for retrieving the thumbnail handler of an item. Implement this interface if you want to specify what extractor is used for a child IDList.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IThumbnailProvider</strong>](/windows/desktop/api/Thumbcache/nn-thumbcache-ithumbnailprovider)<br/></td>
<td>Exposes a method for getting a thumbnail image and is intended to be implemented for thumbnail handlers. The object that implements this interface must also implement [<strong>IInitializeWithStream</strong>](/windows/desktop/api/Propsys/nn-propsys-iinitializewithstream). <br/></td>
</tr>
<tr class="even">
<td>[<strong>IThumbnailSettings</strong>](/windows/desktop/api/Thumbcache/nn-thumbcache-ithumbnailsettings)<br/></td>
<td>Provides a method that enables a thumbnail provider to determine the user context of a thumbnail request.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IThumbnailStreamCache</strong>](/windows/desktop/api/thumbnailstreamcache/nn-thumbnailstreamcache-ithumbnailstreamcache)<br/></td>
<td>Gets or sets the thumbnail stream. This interface is for internal use only and can only be called by the photos application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITrackShellMenu</strong>](/windows/desktop/api/Shdeprecated/nn-shdeprecated-itrackshellmenu)<br/></td>
<td>Exposes methods that extend the [<strong>IShellMenu</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellmenu) interface by providing the ability to coordinate toolbar buttons with a menu as well as display a pop-up menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITranscodeImage</strong>](/windows/desktop/api/Imagetranscode/nn-imagetranscode-itranscodeimage)<br/></td>
<td>Exposes a method that allows conversion to JPEG or bitmap (BMP) image formats from any image type supported by Windows. <br/></td>
</tr>
<tr class="even">
<td>[<strong>ITransferAdviseSink</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itransferadvisesink)<br/></td>
<td>Exposes methods supporting status collection and failure information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITransferDestination</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itransferdestination)<br/></td>
<td>Exposes methods that create a destination Shell item for a copy or move operation. This interface is provided to allow more control over file operations by providing an [<strong>ITransferDestination::Advise</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itransferdestination-advise) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITransferMediumItem</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Used by a copy engine to get the item on which to call [<strong>QueryInterface</strong>](https://msdn.microsoft.com/54d5ff80-18db-43f2-b636-f93ac053146d) to return a pointer to interface [<strong>ITransferDestination</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itransferdestination) or interface [<strong>ITransferSource</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itransfersource). These interfaces can be queried and enumerated for copy, move, or delete operations.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITransferSource</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itransfersource)<br/></td>
<td>Exposes methods to manipulate [<strong>IShellItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem), including copy, move, recycle, and others. This interface is offered to provide more control over file operations by providing an [<strong>ITransferSource::Advise</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itransfersource-advise) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITrayDeskBand</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-itraydeskband)<br/></td>
<td>Exposes methods that show, hide, and query deskbands.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IUpdateIDList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iupdateidlist)<br/></td>
<td>Provides a method to update the [<strong>ITEMIDLIST</strong>](/windows/desktop/api/Shtypes/ns-shtypes-_itemidlist) of the child of an folder object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IURLSearchHook</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes a method that is used by the browser to translate the address of an unknown URL protocol.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IURLSearchHook2</strong>](/windows/desktop/api/Shlobj_core/)<br/></td>
<td>Exposes a method that is used by the browser to translate the address of an unknown URL protocol by using a search context object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IUserAccountChangeCallback</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iuseraccountchangecallback)<br/></td>
<td>Exposes a method which is called when the picture that represents a user account is changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IUserNotification</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iusernotification)<br/></td>
<td>Exposes methods that set notification information and then display that notification to the user in a balloon that appears in conjunction with the notification area of the taskbar. <br/>
<blockquote>
[!Note]<br />
[<strong>IUserNotification2</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iusernotification2) differs from [<strong>IUserNotification</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iusernotification) only in its [<strong>Show</strong>](/windows/desktop/api/Shobjidl/nf-shobjidl-iusernotification2-show) method, which adds an additional parameter for a callback interface to communicate with the notification. Otherwise the two interfaces are identical in form and function. CLSID_UserNotification implements both versions of <strong>Show</strong> as an overload.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IUserNotification2</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iusernotification2)<br/></td>
<td>Exposes methods that set notification information and then display that notification to the user in a balloon that appears in conjunction with the notification area of the taskbar. <br/>
<blockquote>
[!Note]<br />
[<strong>IUserNotification2</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iusernotification2) does not inherit from [<strong>IUserNotification</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iusernotification). <strong>IUserNotification2</strong> differs from <strong>IUserNotification</strong> only in its [<strong>Show</strong>](/windows/desktop/api/Shobjidl/nf-shobjidl-iusernotification2-show) method, which adds an additional parameter for a callback interface to communicate with the notification. Otherwise the two interfaces are identical in form and function. CLSID_UserNotification implements both versions of <strong>Show</strong> as an overload.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IUserNotificationCallback</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iusernotificationcallback)<br/></td>
<td>Exposes a method for the handling of a mouse click or shortcut menu access in a notification balloon. Used with [<strong>IUserNotification2::Show</strong>](/windows/desktop/api/Shobjidl/nf-shobjidl-iusernotification2-show).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IUseToBrowseItem</strong>](/windows/desktop/api/shobjidl/)<br/></td>
<td>Finds the item that should be used when browsing to this item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IViewStateIdentityItem</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Provides a canonical persistence item, an item for which view customizations will be remembered.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IVirtualDesktopManager</strong>](/windows/desktop/api/shobjidl/nn-shobjidl-ivirtualdesktopmanager)<br/></td>
<td>Exposes methods that enable an application to interact with groups of windows that form virtual workspaces.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IVisualProperties</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ivisualproperties)<br/></td>
<td>Exposes methods that set and get visual properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IWebWizardExtension</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iwebwizardextension)<br/></td>
<td>Extends the [<strong>IWizardExtension</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iwizardextension) interface by exposing methods to set the wizard extension's initial URL, and a specific URL in case of an error.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IWizardExtension</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iwizardextension)<br/></td>
<td>Used by wizards such as the Web Publishing Wizard and Online Print Ordering Wizard which host server-side content pages. This interface exposes methods to specify supported extension pages and to navigate into and out of those pages.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IWizardSite</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-iwizardsite)<br/></td>
<td>Exposes methods used by a wizard extension to navigate the borders between itself and the rest of the wizard.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TaskCompletionClient</strong>](taskcompletionclient.md)<br/></td>
<td>Enables task completion. <br/></td>
</tr>
</tbody>
</table>



 

 

 




