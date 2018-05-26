---
Description: This section describes the Windows Shell interfaces.
title: Shell Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<td>[<strong>IAccessibleObject</strong>](/windows/win32/Shobjidl/nn-shobjidl-iaccessibleobject?branch=master)<br/></td>
<td>Exposes a method that can be used by an accessibility application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAccessibilityDockingService</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Docks a single accessibility app window to the bottom of a screen.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAccessibilityDockingServiceCallback</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Informs an accessibility app that its window has been undocked.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IACLCustomMRU</strong>](iaclcustommru.md)<br/></td>
<td>Exposes methods that are used to initialize a most recently used (MRU) list for an autocompletion object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IACList</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes a method that improves the efficiency of [<strong>autocompletion</strong>](/windows/win32/Shldisp/nn-shldisp-iautocomplete?branch=master) when the candidate strings are organized in a hierarchy.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IACList2</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Extends the [<strong>IACList</strong>](/windows/win32/Shlobj_core/?branch=master) interface to enable clients of an autocomplete object to retrieve and set option flags.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IActionProgress</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iactionprogress?branch=master)<br/></td>
<td>Represents the abstract base class from which progress-driven operations can inherit.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IActionProgressDialog</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iactionprogressdialog?branch=master)<br/></td>
<td>Exposes methods that initialize and stop a progress dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationActivationManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iapplicationactivationmanager?branch=master)<br/></td>
<td>Provides methods which activate Windows Store apps for the Launch, File, and Protocol [extensions](m_ca_contracts.capabilities_and_contracts_portal). You will normally use this interface in debuggers and design tools.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IApplicationAssociationRegistration</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iapplicationassociationregistration?branch=master)<br/></td>
<td>Exposes methods that query and set default applications for specific file [<strong>Association Type</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-associationtype?branch=master), and protocols at a specific [<strong>Association Level</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-associationlevel?branch=master). <br/>
<blockquote>
[!Note]<br />
As of Windows 8, the only functionality of this interface that is supported is [<strong>QueryCurrentDefault</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iapplicationassociationregistration-querycurrentdefault?branch=master).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationAssociationRegistrationUI</strong>](/windows/win32/Shobjidl/nn-shobjidl-iapplicationassociationregistrationui?branch=master)<br/></td>
<td>Exposes a method that launches an advanced association dialog box through which the user can customize their associations.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IApplicationDesignModeSettings</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iapplicationdesignmodesettings?branch=master)<br/></td>
<td>Enables development tool applications to dynamically spoof system and user states, such as native display resolution, device scale factor, and application view state, for the purpose of testing Windows Store apps running in design mode for a wide range of form factors without the need for the actual hardware. Also enables testing of changes in normally user-controlled state to test Windows Store apps under a variety of scenarios.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationDesignModeSettings2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iapplicationdesignmodesettings2?branch=master)<br/></td>
<td>Enables development tool applications to dynamically control system and user states, such as native display resolution, device scale factor, and application view layout, reported to Windows Store apps for the purpose of testing Windows Store apps running in design mode for a wide range of form factors without the need for the actual hardware. Also enables testing of changes in normally user-controlled state to test Windows Store apps under a variety of scenarios.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IApplicationDestinations</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iapplicationdestinations?branch=master)<br/></td>
<td>Exposes methods that allow an application to remove one or all destinations from the <strong>Recent</strong> or <strong>Frequent</strong> categories in a Jump List.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationDocumentLists</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iapplicationdocumentlists?branch=master)<br/></td>
<td>Exposes methods that allow an application to retrieve the contents of the <strong>Recent</strong> or <strong>Frequent</strong> categories in a Jump List.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAppPublisher</strong>](/windows/win32/Shappmgr/nn-shappmgr-iapppublisher?branch=master)<br/></td>
<td>Exposes methods for publishing applications through <strong>Add/Remove Programs</strong> in Control Panel. This is the principal interface implemented for this purpose.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAppVisibility</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iappvisibility?branch=master)<br/></td>
<td>Provides functionality to determine whether the display is showing Windows Store apps.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAppVisibilityEvents</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iappvisibilityevents?branch=master)<br/></td>
<td>Enables applications to receive notifications of state changes in a display and of changes in Start screen visibility.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAssocHandler</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iassochandler?branch=master)<br/></td>
<td>Exposes methods for operations with a file association dialog box or menu.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAssocHandlerInvoker</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iassochandlerinvoker?branch=master)<br/></td>
<td>Exposes methods that invoke an associated application handler.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAttachmentExecute</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iattachmentexecute?branch=master)<br/></td>
<td>Exposes methods that work with client applications to present a user environment that provides safe download and exchange of files through email and messaging attachments.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAutoComplete</strong>](/windows/win32/Shldisp/nn-shldisp-iautocomplete?branch=master)<br/></td>
<td>Exposed by the autocomplete object (CLSID_AutoComplete). This interface allows applications to initialize, enable, and disable the object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAutoComplete2</strong>](/windows/win32/Shldisp/nn-shldisp-iautocomplete2?branch=master)<br/></td>
<td>Extends [<strong>IAutoComplete</strong>](/windows/win32/Shldisp/nn-shldisp-iautocomplete?branch=master). This interface enables clients of the autocomplete object to retrieve and set a number of options that control how autocompletion operates.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAutoCompleteDropDown</strong>](/windows/win32/Shobjidl/nn-shobjidl-iautocompletedropdown?branch=master)<br/></td>
<td>Exposes methods that allow clients to reset or query the display state of the autocomplete drop-down list, which contains possible completions to a string entered by the user in an edit control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IBandHost</strong>](/windows/win32/Shobjidl/nn-shobjidl-ibandhost?branch=master)<br/></td>
<td>Exposes methods that create and destroy bands and specifiy their availability.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IBandSite</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ibandsite?branch=master)<br/></td>
<td>Exposes methods that control band objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IBrowserFrameOptions</strong>](/windows/win32/Shobjidl_core/nn-shobjidl_core-ibrowserframeoptions?branch=master)<br/></td>
<td>Allows a browser or host to ask [<strong>IShellView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview?branch=master) what kind of view behavior is supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICategorizer</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icategorizer?branch=master)<br/></td>
<td>Exposes methods that are used to obtain information about item identifier lists.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICategoryProvider</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icategoryprovider?branch=master)<br/></td>
<td>Exposes a list of categorizers registered on an [<strong>IShellFolder</strong>](ishellfolder.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICDBurn</strong>](/windows/win32/Shobjidl/nn-shobjidl-icdburn?branch=master)<br/></td>
<td>Exposes methods that determine whether a system has hardware for writing to CD, the drive letter of a CD writer device, and programmatically initiate a CD writing session. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IColumnManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icolumnmanager?branch=master)<br/></td>
<td>Exposes methods that enable inspection and manipulation of columns in the Windows Explorer Details view. Each column is referenced by a [<strong>PROPERTYKEY</strong>](properties.PROPERTYKEY) structure, which names a property.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICommDlgBrowser</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icommdlgbrowser?branch=master)<br/></td>
<td>Exposed by the common file dialog boxes to be used when they host a Shell browser. If supported, [<strong>ICommDlgBrowser</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icommdlgbrowser?branch=master) exposes methods that allow a Shell view to handle several cases that require different behavior in a dialog box than in a normal Shell view. You obtain an <strong>ICommDlgBrowser</strong> interface pointer by calling [<strong>QueryInterface</strong>](com.iunknown_queryinterface) on the [<strong>IShellBrowser</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ishellbrowser?branch=master) object. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICommDlgBrowser2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icommdlgbrowser2?branch=master)<br/></td>
<td>Extends the capabilities of [<strong>ICommDlgBrowser</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icommdlgbrowser?branch=master). This interface is exposed by the common file dialog boxes when they host a Shell browser. A pointer to [<strong>ICommDlgBrowser2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icommdlgbrowser2?branch=master) can be obtained by calling [<strong>QueryInterface</strong>](com.iunknown_queryinterface) on the [<strong>IShellBrowser</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ishellbrowser?branch=master) object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICommDlgBrowser3</strong>](/windows/win32/Shobjidl/nn-shobjidl-icommdlgbrowser3?branch=master)<br/></td>
<td>Extends the capabilities of [<strong>ICommDlgBrowser2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icommdlgbrowser2?branch=master), and used by the common file dialog boxes when they host a Shell browser.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IComputerInfoChangeNotify</strong>](/windows/win32/shobjidl/nn-shobjidl-icomputerinfochangenotify?branch=master)<br/></td>
<td>This interface may be absent in later versions of Windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IConnectableCredentialProviderCredential</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-iconnectablecredentialprovidercredential?branch=master)<br/></td>
<td>Exposes methods for connecting and disconnecting [<strong>IConnectableCredentialProviderCredential</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-iconnectablecredentialprovidercredential?branch=master) objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IContactManagerInterop</strong>](/windows/win32/Shobjidl_core/nn-shobjidl_core-icontactmanagerinterop?branch=master)<br/></td>
<td>Enables access to [<strong>ContactManager</strong>](/windows/win32/Shobjidl_core/nn-shobjidl_core-icontactmanagerinterop?branch=master) methods in an app that manages multiple windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IContextMenu</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-icontextmenu?branch=master)<br/></td>
<td>Exposes methods that either create or merge a shortcut menu associated with a Shell object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IContextMenu2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenu2?branch=master)<br/></td>
<td>Exposes methods that either create or merge a shortcut (context) menu associated with a Shell object. Extends [<strong>IContextMenu</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-icontextmenu?branch=master) by adding a method that allows client objects to handle messages associated with owner-drawn menu items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IContextMenu3</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenu3?branch=master)<br/></td>
<td>Exposes methods that either create or merge a shortcut menu associated with a Shell object. Allows client objects to handle messages associated with owner-drawn menu items and extends [<strong>IContextMenu2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenu2?branch=master) by accepting a return value from that message handling.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IContextMenuCB</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icontextmenucb?branch=master)<br/></td>
<td>Exposes a method that enables the callback of a context menu. For example, to add a shield icon to a <strong>menuItem</strong> that requires elevation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IControlMarkup</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>ICopyHook</strong>](/windows/win32/Shlobj/?branch=master)<br/></td>
<td>Exposes a method that creates a <em>copy hook handler</em>. A copy hook handler is a Shell extension that determines if a Shell folder or printer object can be moved, copied, renamed, or deleted. The Shell calls the [<strong>ICopyHook::CopyCallback</strong>](/windows/win32/Shlobj/?branch=master) method prior to performing one of these operations.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICreateObject</strong>](/windows/win32/Propsys/nn-propsys-icreateobject?branch=master)<br/></td>
<td>Exposes a method that creates an object of a specified class.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICreatingProcess</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icreatingprocess?branch=master)<br/></td>
<td>Used by [<strong>ShellExecuteEx</strong>](/windows/win32/Shellapi/nf-shellapi-shellexecuteexa?branch=master) and [<strong>IContextMenu</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-icontextmenu?branch=master) to allow the caller to alter some parameters of the process being created.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICreateProcessInputs</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icreateprocessinputs?branch=master)<br/></td>
<td>Used by the [<strong>ICreatingProcess</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icreatingprocess?branch=master) interface to alter some parameters of the process that is being created.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProvider</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-icredentialprovider?branch=master)<br/></td>
<td>Exposes methods used in the setup and manipulation of a credential provider. All credential providers must implement this interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderCredential</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-icredentialprovidercredential?branch=master)<br/></td>
<td>Exposes methods that enable the handling of a credential.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderCredential2</strong>](/windows/win32/CredentialProvider/nn-credentialprovider-icredentialprovidercredential2?branch=master)<br/></td>
<td>Extends the [<strong>ICredentialProviderCredential</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-icredentialprovidercredential?branch=master) interface by adding a method that retrieves the security identifier (SID) of a user. The credential is associated with that user and can be grouped under the user's tile.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderCredentialEvents</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-icredentialprovidercredentialevents?branch=master)<br/></td>
<td>Provides an asynchronous callback mechanism used by a credential to notify it of state or text change events in the Logon UI or Credential UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderCredentialEvents2</strong>](/windows/win32/CredentialProvider/nn-credentialprovider-icredentialprovidercredentialevents2?branch=master)<br/></td>
<td>Extends the [<strong>ICredentialProviderCredentialEvents</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-icredentialprovidercredentialevents?branch=master) interface by adding methods that enable batch updating of fields in theLogon UI or Credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderCredentialWithFieldOptions</strong>](/windows/win32/CredentialProvider/nn-credentialprovider-icredentialprovidercredentialwithfieldoptions?branch=master)<br/></td>
<td>Provides a method that enables the credential provider framework to determine whether you've made a customization to a field's option in a logon or credential UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderEvents</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-icredentialproviderevents?branch=master)<br/></td>
<td>Provides an asynchronous callback mechanism used by a credential provider to notify it of changes in the list of credentials or their fields.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderFilter</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-icredentialproviderfilter?branch=master)<br/></td>
<td>Used to dynamically filter credential providers based on information available at runtime.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderSetUserArray</strong>](/windows/win32/CredentialProvider/nn-credentialprovider-icredentialprovidersetuserarray?branch=master)<br/></td>
<td>Provides a method that enables a credential provider to receive the set of users that will be shown in the logon or credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderUser</strong>](/windows/win32/CredentialProvider/nn-credentialprovider-icredentialprovideruser?branch=master)<br/></td>
<td>Provides methods used to retrieve certain properties of an individual user included in a logon or credential UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderUserArray</strong>](/windows/win32/CredentialProvider/nn-credentialprovider-icredentialprovideruserarray?branch=master)<br/></td>
<td>Represents the set of users that will appear in the logon or credential UI. This information enables the credential provider to enumerate the set to retrieve property information about each user to populate fields or filter the set.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICurrentItem</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Obtained by calling [<strong>IShellFolder::BindToObject</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject?branch=master) for an item. If the item represents a snapshot of an item at a previous time, this interface will obtain the current version of the item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICurrentWorkingDirectory</strong>](/windows/win32/Shlobj/?branch=master)<br/></td>
<td>Exposes methods that enable a client to retrieve or set an object's current working directory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICustomDestinationList</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icustomdestinationlist?branch=master)<br/></td>
<td>Exposes methods that allow an application to provide a custom Jump List, including destinations and tasks, for display in the taskbar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDataObjectAsyncCapability</strong>](/windows/win32/Shldisp/nn-shldisp-idataobjectasynccapability?branch=master)<br/></td>
<td>Enables interfaces that are usually synchronous to function asynchronously. <br/>
<blockquote>
[!Note]<br />
This interface is the current, renamed version of [<strong>IAsyncOperation</strong>](shell.IAsyncOperation).
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDataObjectProvider</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idataobjectprovider?branch=master)<br/></td>
<td>Provides methods that enable you to set or retrieve a [DataPackage](http://go.microsoft.com/fwlink/p/?linkid=267543) object's [<strong>IDataObject interface</strong>](com.idataobject), which the DataPackage uses to support interoperability. The DataPackage object is used by an app to provide data to another app.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDataTransferManagerInterop</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idatatransfermanagerinterop?branch=master)<br/></td>
<td>Enables access to [<strong>DataTransferManager</strong>](w_appmod_dataxfer.datatransfermanager) methods in a Windows Store app that manages multiple windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDefaultExtractIconInit</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idefaultextracticoninit?branch=master)<br/></td>
<td>Exposes methods to set default icons associated with an object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDefaultFolderMenuInitialize</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idefaultfoldermenuinitialize?branch=master)<br/></td>
<td>Provides methods used to get and set shortcut menu information. This information is the same as that provided to [<strong>SHCreateDefaultContextMenu</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu?branch=master) through the [<strong>DEFCONTEXTMENU</strong>](/windows/win32/shlobj_core/ns-shlobj_core-defcontextmenu?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDelayedPropertyStoreFactory</strong>](/windows/win32/Propsys/nn-propsys-idelayedpropertystorefactory?branch=master)<br/></td>
<td>Exposes a method to create a specified [<strong>IPropertyStore</strong>](properties.IPropertyStore) object in circumstances where property access is potentially slow.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDelegateFolder</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idelegatefolder?branch=master)<br/></td>
<td>Exposes a method through which a delegate folder is given the [<strong>IMalloc</strong>](com.imalloc) interface required to allocate and free item IDs.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDelegateItem</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Used to obtain the immediately underlying representation of an item's path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDesktopGadget</strong>](/windows/win32/Shobjidl/nn-shobjidl-idesktopgadget?branch=master)<br/></td>
<td>Exposes a method that allows the programmatic addition of an installed gadget to the user's desktop.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDesktopWallpaper</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idesktopwallpaper?branch=master)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IDestinationStreamFactory</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idestinationstreamfactory?branch=master)<br/></td>
<td>Exposes a method for manually copying a stream or file before applying changes to properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDisplayItem</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Exposes methods that find a version of the current item to be used to get display properties, such as the item name, that will be displayed in the UI. Used by the copy engine dialogs to provide the UI with an appropriate item to display. If no other version can be found, the current item is used.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDockingWindow</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idockingwindow?branch=master)<br/></td>
<td>Exposes methods that notify the docking window object of changes, including showing, hiding, and impending removal. This interface is implemented by window objects that can be docked within the border space of a Windows Explorer window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDockingWindowFrame</strong>](/windows/win32/Shlobj/?branch=master)<br/></td>
<td>Exposes methods that support the addition of [<strong>IDockingWindow</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idockingwindow?branch=master) objects to a frame. Implemented by the browser.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDockingWindowSite</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes methods that manage the border space for one or more [<strong>IDockingWindow</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idockingwindow?branch=master) objects. This interface is implemented by the browser and is similar to the [<strong>IOleInPlaceUIWindow</strong>](com.ioleinplaceuiwindow) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDragSourceHelper</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idragsourcehelper?branch=master)<br/></td>
<td>Exposed by the Shell to allow an application to specify the image that will be displayed during a Shell drag-and-drop operation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDragSourceHelper2</strong>](/windows/win32/Shobjidl/nn-shobjidl-idragsourcehelper2?branch=master)<br/></td>
<td>Exposes a method that adds functionality to [<strong>IDragSourceHelper</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idragsourcehelper?branch=master). This method sets the characteristics of a drag-and-drop operation over an <strong>IDragSourceHelper</strong> object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDropTargetHelper</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idroptargethelper?branch=master)<br/></td>
<td>Exposes methods that allow drop targets to display a drag image while the image is over the target window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDynamicHWHandler</strong>](/windows/win32/Shobjidl/nn-shobjidl-idynamichwhandler?branch=master)<br/></td>
<td>Called by AutoPlay. Exposes methods that get dynamic information regarding a registered handler prior to displaying it to the user.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumAssocHandlers</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumassochandlers?branch=master)<br/></td>
<td>Exposes a method that allows enumeration of a collection of handlers associated with particular file name extensions.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumerableView</strong>](/windows/win32/Shobjidl/nn-shobjidl-ienumerableview?branch=master)<br/></td>
<td>Exposes methods that enumerate the contents of a view and receive notification from callback upon enumeration completion. This interface enables clients of a view to attempt to share the view's list of folder contents.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumExplorerCommand</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumexplorercommand?branch=master)<br/></td>
<td>Provided by an [<strong>IExplorerCommandProvider</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommandprovider?branch=master). This interface contains the enumeration of commands to be put into the command bar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumExtraSearch</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumextrasearch?branch=master)<br/></td>
<td>A standard OLE enumerator used by a client to determine the available search objects for a folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumFullIDList</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumfullidlist?branch=master)<br/></td>
<td>Exposes a standard set of methods that enumerate the pointers to item identifier lists (PIDLs) of the items in a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumIDList</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumidlist?branch=master)<br/></td>
<td>Exposes a standard set of methods used to enumerate the PIDLs of the items in a Shell folder. When a folder's [<strong>IShellFolder::EnumObjects</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-enumobjects?branch=master) method is called, it creates an enumeration object and passes a pointer to the object's [<strong>IEnumIDList</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumidlist?branch=master) interface back to the calling application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumObjects</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumobjects?branch=master)<br/></td>
<td>Exposes methods to enumerate unknown objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumPublishedApps</strong>](/windows/win32/Shappmgr/nn-shappmgr-ienumpublishedapps?branch=master)<br/></td>
<td>Exposes methods that enumerate published applications to Add/Remove Programs in the Control Panel. The object exposing this interface is requested through [<strong>IAppPublisher::EnumApps</strong>](/windows/win32/Shappmgr/nf-shappmgr-iapppublisher-enumapps?branch=master). <br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumReadyCallback</strong>](/windows/win32/Shobjidl/nn-shobjidl-ienumreadycallback?branch=master)<br/></td>
<td>Exposes methods that enable the view to notify the implementer when the enumeration has completed. The view calls this method to tell the implementer that the enumeration can be retrieved via [<strong>IEnumerableView::CreateEnumIDListFromContents</strong>](/windows/win32/Shobjidl/nf-shobjidl-ienumerableview-createenumidlistfromcontents?branch=master). The callback allows the implementer to share the views enumeration.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumResources</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumresources?branch=master)<br/></td>
<td>Exposes resource enumeration methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumShellItems</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumshellitems?branch=master)<br/></td>
<td>Exposes enumeration of [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) interfaces. This interface is typically obtained by calling the [<strong>IEnumShellItems</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ienumshellitems?branch=master) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumSyncMgrConflict</strong>](/windows/win32/Syncmgr/nn-syncmgr-ienumsyncmgrconflict?branch=master)<br/></td>
<td>Exposes conflict enumeration methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumSyncMgrEvents</strong>](/windows/win32/Syncmgr/nn-syncmgr-ienumsyncmgrevents?branch=master)<br/></td>
<td>Exposes sync event enumeration methods.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumSyncMgrSyncItems</strong>](/windows/win32/Syncmgr/nn-syncmgr-ienumsyncmgrsyncitems?branch=master)<br/></td>
<td>Exposes methods that enumerate the sync item objects managed by the handler.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExecuteCommand</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexecutecommand?branch=master)<br/></td>
<td>Exposes methods that set a given state or parameter related to the command verb, as well as a method to invoke that verb.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExecuteCommandApplicationHostEnvironment</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexecutecommandapplicationhostenvironment?branch=master)<br/></td>
<td>Provides a single method that enables an application to determine whether its host is in desktop or immersive mode.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExecuteCommandHost</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexecutecommandhost?branch=master)<br/></td>
<td>Provides a method that enables an [<strong>IExplorerCommand</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommand?branch=master)-based Shell verb handler to query the UI mode of the host component from which the application was invoked.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExplorerBrowser</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorerbrowser?branch=master)<br/></td>
<td>[<strong>IExplorerBrowser</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorerbrowser?branch=master) is a browser object that can be either navigated or that can host a view of a data object. As a full-featured browser object, it also supports an automatic travel log.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExplorerBrowserEvents</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorerbrowserevents?branch=master)<br/></td>
<td>Exposes methods for notification of Explorer browser navigation and view creation events.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExplorerCommand</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommand?branch=master)<br/></td>
<td>Exposes methods that get the command appearance, enumerate subcommands, or invoke the command.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExplorerCommandProvider</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommandprovider?branch=master)<br/></td>
<td>Exposes methods to create Explorer commands and command enumerators.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExplorerCommandState</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommandstate?branch=master)<br/></td>
<td>Exposes a single method that allows retrieval of the command state.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExplorerPaneVisibility</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorerpanevisibility?branch=master)<br/></td>
<td>Used in Windows Explorer by an [<strong>IShellFolder</strong>](ishellfolder.md) implementation to give suggestions to the view about what panes are visible. Additionally, an [<strong>IExplorerBrowser</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorerbrowser?branch=master) host can use this interface to provide information about pane visibility. The host should implement [<strong>QueryService</strong>](_inet_IServiceProvider_QueryService_Method) with <strong>SID_ExplorerPaneVisibility</strong> as the service ID. The host must be in the site chain. <br/> The [<strong>IExplorerPaneVisibility</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorerpanevisibility?branch=master) implementation is retrieved from the Shell folder. The Shell folder, in turn, is retrieved from the view. A namespace extension can elect to provide a custom view ([<strong>IShellView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview?branch=master)) rather than using the system folder view object (DefView). In that case, the <strong>IShellView</strong> implementation must include an implementation of [<strong>IFolderView::GetFolder</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ifolderview-getfolder?branch=master) to return the <strong>IExplorerPaneVisibility</strong> object.<br/> A namespace extension can provide a custom view by implementing [<strong>IShellView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview?branch=master) itself rather than using the system folder view object (DefView). In that case, the <strong>IShellView</strong> implementation must include an implementation of [<strong>IFolderView::GetFolder</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ifolderview-getfolder?branch=master) to make use of [<strong>IExplorerPaneVisibility</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorerpanevisibility?branch=master) .<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExtractIcon</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes methods that allow a client to retrieve the icon that is associated with one of the objects in a folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExtractImage</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iextractimage?branch=master)<br/></td>
<td>Exposes methods that request a thumbnail image from a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExtractImage2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iextractimage2?branch=master)<br/></td>
<td>Extends the capabilities of [<strong>IExtractImage</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iextractimage?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileDialog</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ifiledialog?branch=master)<br/></td>
<td>Exposes methods that initialize, show, and get results from the common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileDialog2</strong>](/windows/win32/Shobjidl/nn-shobjidl-ifiledialog2?branch=master)<br/></td>
<td>Extends the [<strong>IFileDialog</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ifiledialog?branch=master) interface by providing methods that allow the caller to name a specific, restricted location that can be browsed in the common file dialog as well as to specify alternate text to display as a label on the <strong>Cancel</strong> button.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileDialogControlEvents</strong>](/windows/win32/Shobjidl/nn-shobjidl-ifiledialogcontrolevents?branch=master)<br/></td>
<td>Exposes methods that allow an application to be notified of events that are related to controls that the application has added to a common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileDialogCustomize</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifiledialogcustomize?branch=master)<br/></td>
<td>Exposes methods that allow an application to add controls to a common file dialog.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileDialogEvents</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifiledialogevents?branch=master)<br/></td>
<td>Exposes methods that allow notification of events within a common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileIsInUse</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifileisinuse?branch=master)<br/></td>
<td>Exposes methods that can be called to get information on or close a file that is in use by another application. When an application attempts to access a file and finds that file already in use, it can use the methods of this interface to gather information to present to the user in a dialog box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileOpenDialog</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ifileopendialog?branch=master)<br/></td>
<td>Extends the [<strong>IFileDialog</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ifiledialog?branch=master) interface by adding methods specific to the open dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileOperation</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifileoperation?branch=master)<br/></td>
<td>Exposes methods to copy, move, rename, create, and delete Shell items as well as methods to provide progress and error dialogs. This interface replaces the [<strong>SHFileOperation</strong>](/windows/win32/Shellapi/nf-shellapi-shfileoperationa?branch=master) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileOperationProgressSink</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifileoperationprogresssink?branch=master)<br/></td>
<td>Exposes methods that provide a rich notification system used by callers of [<strong>IFileOperation</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifileoperation?branch=master) to monitor the details of the operations they are performing through that interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileSaveDialog</strong>](/windows/win32/Shobjidl_core/nn-shobjidl_core-ifilesavedialog?branch=master)<br/></td>
<td>Extends the [<strong>IFileDialog</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ifiledialog?branch=master) interface by adding methods specific to the save dialog, which include those that provide support for the collection of metadata to be persisted with the file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileSyncMergeHandler</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifilesyncmergehandler?branch=master)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IFileSystemBindData</strong>](shell.ifilesystembinddata)<br/></td>
<td>Exposes methods that store file system information for optimizing calls to [<strong>IShellFolder::ParseDisplayName</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileSystemBindData2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifilesystembinddata2?branch=master)<br/></td>
<td>Extends [<strong>IFileSystemBindData</strong>](shell.ifilesystembinddata), which stores file system information for optimizing calls to [<strong>IShellFolder::ParseDisplayName</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname?branch=master). This interface adds the ability set or get file ID or junction class identifier (CLSID).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileViewer</strong>](/windows/win32/Shlobj/?branch=master)<br/></td>
<td>Exposes methods that designate an interface that allows a registered file viewer to be notified when it must show or print a file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileViewerSite</strong>](/windows/win32/Shlobj/?branch=master)<br/></td>
<td>Exposes methods that designate an interface that allows a file viewer to retrieve the handle to the current pinned window, or to set a new pinned window. The pinned window is the window in which the current file viewer displays a file. When the user selects a new file to view, the Shell directs the file viewer to display the new file in the pinned window rather than create a new window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderFilter</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifolderfilter?branch=master)<br/></td>
<td>Exposed by a client to specify how to filter the enumeration of a Shell folder by a server application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFolderFilterSite</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifolderfiltersite?branch=master)<br/></td>
<td>Exported by a host to allow clients to specify how to filter a Shell folder enumeration.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifolderview?branch=master)<br/></td>
<td>Exposes methods that retrieve information about a folder's display options, select specified items in that folder, and set the folder's view mode.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFolderView2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifolderview2?branch=master)<br/></td>
<td>Exposes methods that retrieve information about a folder's display options, select specified items in that folder, and set the folder's view mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderViewHost</strong>](/windows/win32/Shobjidl/nn-shobjidl-ifolderviewhost?branch=master)<br/></td>
<td>Exposes a method that hosts an [<strong>IFolderView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifolderview?branch=master) object in a window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFolderViewOptions</strong>](/windows/win32/Shobjidl/nn-shobjidl-ifolderviewoptions?branch=master)<br/></td>
<td>Exposes methods that allow control of folder view options specific to the Windows 7 and later views.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderViewSettings</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifolderviewsettings?branch=master)<br/></td>
<td>Exposes methods to obtain folder view settings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFrameworkInputPane</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iframeworkinputpane?branch=master)<br/></td>
<td>Provides methods that enable apps to be informed of state changes and location for the input pane.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFrameworkInputPaneHandler</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iframeworkinputpanehandler?branch=master)<br/></td>
<td>Enables an app to be notified when the input pane (the on-screen keyboard or handwriting panel) is being shown or hidden. This allows the app window to adjust its display so that no input areas (such as a text box) are obscured by the input pane.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IHandlerActivationHost</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ihandleractivationhost?branch=master)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IHandlerInfo</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ihandlerinfo?branch=master)<br/></td>
<td>Supplies methods that provide information about the handler to methods of the [<strong>IHandlerActivationHost</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ihandleractivationhost?branch=master) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IHomeGroup</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ihomegroup?branch=master)<br/></td>
<td>Exposes methods that determine a computer's HomeGroup membership status and display the sharing wizard.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IHWEventHandler</strong>](/windows/win32/Shobjidl/nn-shobjidl-ihweventhandler?branch=master)<br/></td>
<td>Called by AutoPlay to implement the handling of registered media types.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IHWEventHandler2</strong>](/windows/win32/Shobjidl/nn-shobjidl-ihweventhandler2?branch=master)<br/></td>
<td>Extends the [<strong>IHWEventHandler</strong>](/windows/win32/Shobjidl/nn-shobjidl-ihweventhandler?branch=master) interface to address User Account Control (UAC) elevation for device handlers.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IIdentityName</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Exposes methods to compare two items to see if they are the same.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IImageRecompress</strong>](/windows/win32/Shobjidl/nn-shobjidl-iimagerecompress?branch=master)<br/></td>
<td>Exposes a method that recompress images.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeCommand</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iinitializecommand?branch=master)<br/></td>
<td>Exposes a single method used to initialize objects that implement [<strong>IExplorerCommandState</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommandstate?branch=master), [<strong>IExecuteCommand</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iexecutecommand?branch=master) or [<strong>IDropTarget</strong>](com.idroptarget) with the application-specified command name and its registered properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeNetworkFolder</strong>](/windows/win32/Shobjidl/nn-shobjidl-iinitializenetworkfolder?branch=master)<br/></td>
<td>Exposes a method that initializes the network data source CLSID_NetworkPlaces as specified.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeWithBindCtx</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iinitializewithbindctx?branch=master)<br/></td>
<td>Exposes a method that initializes a handler, such as a property handler, thumbnail handler, or preview handler, with a bind context.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeWithFile</strong>](/windows/win32/Propsys/nn-propsys-iinitializewithfile?branch=master)<br/></td>
<td>Exposes a method to initialize a handler, such as a property handler, thumbnail handler, or preview handler, with a file path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeWithItem</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-iinitializewithitem?branch=master)<br/></td>
<td>Exposes a method used to initialize a handler, such as a property handler, thumbnail handler, or preview handler, with an [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeWithPropertyStore</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iinitializewithpropertystore?branch=master)<br/></td>
<td>Exposes a method that initializes a handler, such as a property handler, thumbnail handler, or preview handler, with a property store.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeWithStream</strong>](/windows/win32/Propsys/nn-propsys-iinitializewithstream?branch=master)<br/></td>
<td>Exposes a method that initializes a handler, such as a property handler, thumbnail handler, or preview handler, with a stream.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeWithWindow</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iinitializewithwindow?branch=master)<br/></td>
<td>Exposes a method through which a client can provide an owner window to a Windows Runtime object used in a desktop application.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInputObject</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-iinputobject?branch=master)<br/></td>
<td>Exposes methods that change UI activation and process accelerators for a user input object contained in the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInputObject2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iinputobject2?branch=master)<br/></td>
<td>Exposes a method that extends [<strong>IInputObject</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-iinputobject?branch=master) by handling global accelerators.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInputObjectSite</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iinputobjectsite?branch=master)<br/></td>
<td>Exposes a method that is used to communicate focus changes for a user input object contained in the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInputPanelConfiguration</strong>](/windows/win32/inputpanelconfiguration/nn-inputpanelconfiguration-iinputpanelconfiguration?branch=master)<br/></td>
<td>Provides functionality for desktop apps to opt in to the focus tracking mechanism used in Windows Store apps.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInputPanelInvocationConfiguration</strong>](/windows/win32/inputpanelconfiguration/nn-inputpanelconfiguration-iinputpanelinvocationconfiguration?branch=master)<br/></td>
<td>Enables Windows Store apps to opt out of the automatic invocation behavior.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IIOCancelInformation</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iiocancelinformation?branch=master)<br/></td>
<td>Exposes methods for posting a cancel window message to the process thread from the Progress Dialog. <br/> This interface enables the progress dialog to post a thread message through [<strong>PostThreadMessage</strong>](winmsg.postthreadmessage) to the worker thread to cancel its operations. The worker thread must periodically check the message queue through [<strong>GetMessage</strong>](winmsg.getmessage), [<strong>PeekMessage</strong>](winmsg.peekmessage) or [<strong>MsgWaitForMultipleObjectsEx</strong>](base.msgwaitformultipleobjectsex).<br/> The [<strong>IIOCancelInformation::SetCancelInformation</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iiocancelinformation-setcancelinformation?branch=master) method tells the progress dialog which thread ID and what message to [<strong>PostThreadMessage</strong>](winmsg.postthreadmessage) when the user clicks <strong>Cancel</strong>. A thread ID of &quot;zero&quot; disables the sending operation for the cancel message.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IItemNameLimits</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iitemnamelimits?branch=master)<br/></td>
<td>Retrieves a list of valid and invalid characters or the maximum length of a name in the namespace. Use this interface for validation parsing and translation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IKnownFolder</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iknownfolder?branch=master)<br/></td>
<td>Exposes methods that allow an application to retrieve information about a known folder's category, type, GUID, PIDL value, redirection capabilities, and definition. It provides a method for the retrival of a known folder's [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) object. It also provides methods to get or set the path of the known folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IKnownFolderManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iknownfoldermanager?branch=master)<br/></td>
<td>Exposes methods that create, enumerate or manage existing known folders.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILaunchSourceAppUserModelId</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ilaunchsourceappusermodelid?branch=master)<br/></td>
<td>Provides a method for retrieving an [AppUserModelId](appids.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILaunchSourceViewSizePreference</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ilaunchsourceviewsizepreference?branch=master)<br/></td>
<td>Provides methods for retrieving information about the source application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILaunchTargetMonitor</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ilaunchtargetmonitor?branch=master)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>ILaunchTargetViewSizePreference</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ilaunchtargetviewsizepreference?branch=master)<br/></td>
<td>Provides a method for retrieving the preferred view size for a new application window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMarkupCallback</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IMenuPopup</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-imenupopup?branch=master)<br/></td>
<td>[<strong>IMenuPopup</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-imenupopup?branch=master) may be altered or unavailable.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IModalWindow</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-imodalwindow?branch=master)<br/></td>
<td>Exposes a method that represents a modal window. This interface is used in the Windows XP Passport Wizard.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMultiMonitorDockingSite</strong>](imultimonitordockingsite.md)<br/></td>
<td>Implemented by the browser. Exposes methods that manage which monitor contains the Windows taskbar on a multiple monitor system. <br/></td>
</tr>
<tr class="even">
<td>[<strong>INamedPropertyBag</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes methods that provide an object with a specified property bag in which the object can save its properties.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INamedPropertyStore</strong>](/windows/win32/Propsys/nn-propsys-inamedpropertystore?branch=master)<br/></td>
<td>Exposes methods that get and set named properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeAccessible</strong>](/windows/win32/Shobjidl/nn-shobjidl-inamespacetreeaccessible?branch=master)<br/></td>
<td>Exposes methods that perform accessibility actions on a Shell item from a namespace tree control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INameSpaceTreeControl</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacetreecontrol?branch=master)<br/></td>
<td>Exposes methods used to view and manipulate nodes in a tree of Shell items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeControl2</strong>](/windows/win32/Shobjidl/nn-shobjidl-inamespacetreecontrol2?branch=master)<br/></td>
<td>Extends the [<strong>INameSpaceTreeControl</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacetreecontrol?branch=master) interface by providing methods that get and set the display styles of treeview controls for use with Shell namespace items.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INameSpaceTreeControlCustomDraw</strong>](/windows/win32/Shobjidl/nn-shobjidl-inamespacetreecontrolcustomdraw?branch=master)<br/></td>
<td>Exposes methods that enable the user to draw a custom namespace tree control and its items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeControlDropHandler</strong>](/windows/win32/Shobjidl/nn-shobjidl-inamespacetreecontroldrophandler?branch=master)<br/></td>
<td>Exposes handler methods for drag-and-drop. Used by the namespace tree control to notify the client of any drag-and-drop operation happening within the control. Provides a way for a client to intercept a drop operation and perform its own action, or to return the desired drop effect.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INameSpaceTreeControlEvents</strong>](/windows/win32/Shobjidl/nn-shobjidl-inamespacetreecontrolevents?branch=master)<br/></td>
<td>Exposes methods for handling [<strong>INameSpaceTreeControl</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacetreecontrol?branch=master) events.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeControlFolderCapabilities</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacetreecontrolfoldercapabilities?branch=master)<br/></td>
<td>Exposes a single method that retrieves the status of a folder's [System.IsPinnedToNameSpaceTree](properties.props_System_IsPinnedToNameSpaceTree) filtering support.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INamespaceWalk</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacewalk?branch=master)<br/></td>
<td>Exposes methods that walk a namespace from a given root node. The depth of the walk is specified and an optional array is returned containing the IDs of all nodes walked.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INamespaceWalkCB</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacewalkcb?branch=master)<br/></td>
<td>A callback interface exposing methods used with [<strong>INamespaceWalk</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacewalk?branch=master). After performing a walk with <strong>INamespaceWalk</strong>, an [<strong>IShellFolder</strong>](ishellfolder.md) object representing the walked nodes is passed to the [<strong>INamespaceWalkCB</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacewalkcb?branch=master) methods. What those methods do with the information depends on the object that is implementing them.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INamespaceWalkCB2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacewalkcb2?branch=master)<br/></td>
<td>Extends [<strong>INamespaceWalkCB</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacewalkcb?branch=master) with a method that is required in order to complete a namespace walk. This method removes data collected during the walk. <br/></td>
</tr>
<tr class="even">
<td>[<strong>INewMenuClient</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inewmenuclient?branch=master)<br/></td>
<td>Exposes methods that allow manipulation of items in a Windows 7 menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INewShortcutHook</strong>](/windows/win32/Shlobj/?branch=master)<br/></td>
<td>Exposes methods to create a new Internet shortcut.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INewWindowManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inewwindowmanager?branch=master)<br/></td>
<td>Exposes a method that determines whether a window that is launched by another window should be displayed or blocked, allowing control of pop-up windows.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INotifyReplica</strong>](/windows/win32/Reconcil/?branch=master)<br/></td>
<td>Exposes a method that provides an object's creator with the means to notify the object that it may be subject to subsequent reconciliation. The briefcase reconciler is responsible for implementing this interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectArray</strong>](/windows/win32/Objectarray/nn-objectarray-iobjectarray?branch=master)<br/></td>
<td>Exposes methods that enable clients to access items in a collection of objects that support [<strong>IUnknown</strong>](com.iunknown).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectCollection</strong>](/windows/win32/objectarray/nn-objectarray-iobjectcollection?branch=master)<br/></td>
<td>Extends the [<strong>IObjectArray</strong>](/windows/win32/Objectarray/nn-objectarray-iobjectarray?branch=master) interface by providing methods that enable clients to add and remove objects that support [<strong>IUnknown</strong>](com.iunknown) in a collection.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectProvider</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iobjectprovider?branch=master)<br/></td>
<td>Exposes a method to discover objects that are named with a <strong>GUID</strong> from another object. Unlike [<strong>QueryService</strong>](_inet_IServiceProvider_QueryService_Method) this interface will not delegate its functionality on to other objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithAppUserModelID</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iobjectwithappusermodelid?branch=master)<br/></td>
<td>Exposes methods that allow implementers of a custom [<strong>IAssocHandler</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iassochandler?branch=master) object to provide access to its explicit Application User Model ID (AppUserModelID). This information is used to determine whether a particular file type can be added to an application's Jump List.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectWithBackReferences</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iobjectwithbackreferences?branch=master)<br/></td>
<td>Provides a method for interacting with back references held by an object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithCancelEvent</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iobjectwithcancelevent?branch=master)<br/></td>
<td>Supplies a caller with an event that will be signaled by the called object to denote cancellation of a task.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectWithFolderEnumMode</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iobjectwithfolderenummode?branch=master)<br/></td>
<td>Exposes methods that get and set enumeration modes of a parsed item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithProgID</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iobjectwithprogid?branch=master)<br/></td>
<td>Exposes methods that provide access to the ProgID associated with an object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectWithPropertyKey</strong>](/windows/win32/Propsys/nn-propsys-iobjectwithpropertykey?branch=master)<br/></td>
<td>Exposes methods for getting and setting the property key.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithSelection</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iobjectwithselection?branch=master)<br/></td>
<td>Exposes methods that get or set selected items represented by a Shell item array.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjMgr</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes methods that allow a client to append or remove an object from a collection of objects managed by a server object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOpenControlPanel</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iopencontrolpanel?branch=master)<br/></td>
<td>Exposes methods that retrieve the view state of the Control Panel, the path of individual Control Panel items, and that open either the Control Panel itself or an individual Control Panel item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOpenSearchSource</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iopensearchsource?branch=master)<br/></td>
<td>Exposes a method to get search results from a custom client-side OpenSearch data source.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOperationsProgressDialog</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ioperationsprogressdialog?branch=master)<br/></td>
<td>Exposes methods to get, set, and query a progress dialog.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPackageDebugSettings</strong>](/windows/win32/Shobjidl_core/nn-shobjidl_core-ipackagedebugsettings?branch=master)<br/></td>
<td>Enables debugger developers to control the life cycle of a Windows Store app, such as suspending or resuming.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPackageExecutionStateChangeNotification</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ipackageexecutionstatechangenotification?branch=master)<br/></td>
<td>Enables receiving package state-change notifications during Windows Store app debugging.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IParentAndItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iparentanditem?branch=master)<br/></td>
<td>Exposes methods that get and set the parent and the parent's child ID. While [<strong>IParentAndItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iparentanditem?branch=master) is typically implemented on IShellItems, it is not specific to [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master). <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IParseAndCreateItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iparseandcreateitem?branch=master)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IPersistFolder</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ipersistfolder?branch=master)<br/></td>
<td>Exposes a method that initializes Shell folder objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPersistFolder2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ipersistfolder2?branch=master)<br/></td>
<td>Exposes methods that obtain information from Shell folder objects.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPersistFolder3</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ipersistfolder3?branch=master)<br/></td>
<td>Extends the [<strong>IPersistFolder</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ipersistfolder?branch=master) and [<strong>IPersistFolder2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ipersistfolder2?branch=master) interfaces by allowing a folder object to implement nondefault handling of folder shortcuts.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPersistIDList</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ipersistidlist?branch=master)<br/></td>
<td>Exposes methods that are used to persist item identifier lists.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPersistSerializedPropStorage</strong>](/windows/win32/Propsys/nn-propsys-ipersistserializedpropstorage?branch=master)<br/></td>
<td>Exposes methods to persist serialized property storage data for later use and to restore persisted data to a new property store instance.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPersistSerializedPropStorage2</strong>](/windows/win32/Propsys/nn-propsys-ipersistserializedpropstorage2?branch=master)<br/></td>
<td>Exposes methods to persist serialized property storage data for later use and to restore persisted data to a new property store instance.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPlaybackManager</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Provides methods that allow media applications to communicate with the Windows playback manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPlaybackManagerEvents</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IPreviewHandler</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ipreviewhandler?branch=master)<br/></td>
<td>Exposes methods for the display of rich previews.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPreviewHandlerFrame</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ipreviewhandlerframe?branch=master)<br/></td>
<td>Enables preview handlers to pass keyboard shortcuts to the host. This interface retrieves a list of keyboard shortcuts and directs the host to handle a keyboard shortcut.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPreviewHandlerVisuals</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ipreviewhandlervisuals?branch=master)<br/></td>
<td>Exposes methods for applying color and font information to preview handlers.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPreviewItem</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Identifies an item that will be shown in the preview pane.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPreviousVersionsInfo</strong>](/windows/win32/Shobjidl/nn-shobjidl-ipreviousversionsinfo?branch=master)<br/></td>
<td>Exposes a method that checks for previous versions of server files or folders, stored for the purpose of reversion by the <em>shadow copies</em> technology provided with Windows Server 2003.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPrivateIdentityManager</strong>](iprivateidentitymanager.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IPrivateIdentityManager2</strong>](iprivateidentitymanager2.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IProfferService</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iprofferservice?branch=master)<br/></td>
<td>Exposes a general mechanism for objects to offer services to other objects on the same host.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IProgressDialog</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes methods that provide options for an application to display a progress dialog box. This interface is exported by the progress dialog box object (CLSID_ProgressDialog). This object is a generic way to show a user how an operation is progressing. It is typically used when deleting, uploading, copying, moving, or downloading large numbers of files.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPublishedApp</strong>](/windows/win32/Shappmgr/nn-shappmgr-ipublishedapp?branch=master)<br/></td>
<td>Exposes methods that represent applications to Add/Remove Programs in Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IPublishedApp2</strong>](/windows/win32/Shappmgr/nn-shappmgr-ipublishedapp2?branch=master)<br/></td>
<td>Extends the [<strong>IPublishedApp</strong>](/windows/win32/Shappmgr/nn-shappmgr-ipublishedapp?branch=master) interface by providing an additional installation method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPublishingWizard</strong>](/windows/win32/Shobjidl/nn-shobjidl-ipublishingwizard?branch=master)<br/></td>
<td>Exposes methods for working with the Online Print Wizard, the Web Publishing Wizard, and the Add Network Place Wizard. In Windows Vista, [<strong>IPublishingWizard</strong>](/windows/win32/Shobjidl/nn-shobjidl-ipublishingwizard?branch=master) no longer supports the Web Publishing Wizard or Online Print Wizard.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IQueryAssociations</strong>](/windows/win32/Shlwapi/?branch=master)<br/></td>
<td>Exposes methods that simplify the process of retrieving information stored in the registry in association with defining a file type or protocol and associating it with an application.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IQueryCancelAutoPlay</strong>](/windows/win32/Shobjidl/nn-shobjidl-iquerycancelautoplay?branch=master)<br/></td>
<td>Exposes a method that programmatically overrides [AutoPlay](autorun2k-intro.md) or [AutoRun](autoplay.md). This allows you to customize the location and type of content that is launched when media is inserted.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IQueryCodePage</strong>](/windows/win32/Shobjidl/nn-shobjidl-iquerycodepage?branch=master)<br/></td>
<td>Gets and sets the numeric value (Code Page identifier) of the ANSI code page.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IQueryContinue</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iquerycontinue?branch=master)<br/></td>
<td>Exposes a method that provides a simple, standard mechanism for objects to query a client for permission to continue an operation. Clients of [<strong>IUserNotification</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iusernotification?branch=master), for example, must pass an implementation of [<strong>IQueryContinue</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iquerycontinue?branch=master) to the [<strong>IUserNotification::Show</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iusernotification-show?branch=master) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IQueryContinueWithStatus</strong>](/windows/win32/Credentialprovider/nn-credentialprovider-iquerycontinuewithstatus?branch=master)<br/></td>
<td>Exposes methods that provide a standard mechanism for credential providers to call [<strong>QueryContinue</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iquerycontinue-querycontinue?branch=master) while attempting to connect to the network to determine if they should continue these attempts. Credential providers can also use this interface to display messages to the user while attempting to establish a network connection.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IQueryInfo</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes methods that the Shell uses to retrieve flags and info tip information for an item that resides in an [<strong>IShellFolder</strong>](ishellfolder.md) implementation. Info tips are usually displayed inside a [tooltip](_win32_Tooltip_Controls) control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IRelatedItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-irelateditem?branch=master)<br/></td>
<td>Exposes methods that derive related items with specific relationships.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IRemoteComputer</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iremotecomputer?branch=master)<br/></td>
<td>Exposes a method that enumerates or initializes a namespace extension when it is invoked on a remote object. This interface is used, for example, to initialize the remote printers virtual folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IResolveShellLink</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iresolveshelllink?branch=master)<br/></td>
<td>Exposes a method that enables an application to request that a Shell folder object resolve a link for one of its items.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IResultsFolder</strong>](/windows/win32/Shobjidl/nn-shobjidl-iresultsfolder?branch=master)<br/></td>
<td>Exposes methods that hold items from a data object.<br/> An [<strong>IResultsFolder</strong>](/windows/win32/Shobjidl/nn-shobjidl-iresultsfolder?branch=master) is a folder that can hold items from all over the namespace and represent them to the user in a single folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IRunnableTask</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-irunnabletask?branch=master)<br/></td>
<td>A free-threaded interface that can be exposed by an object to allow operations to be performed on a background thread. For example, if the [<strong>IExtractImage::GetLocation</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iextractimage-getlocation?branch=master) method returns E_PENDING, the calling application is permitted to extract the image on a background thread.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISearchBoxInfo</strong>](/windows/win32/Shobjidl/nn-shobjidl-isearchboxinfo?branch=master)<br/></td>
<td>Exposes methods that allow the caller to retrieve information entered into a search box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISearchContext</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes methods that channel customization information to the search hooks.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISearchFolderItemFactory</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-isearchfolderitemfactory?branch=master)<br/></td>
<td>Exposes methods that create and modify search folders. The Set methods are called first to set up the parameters of the search. When not called, default values will be used instead. [<strong>ISearchFolderItemFactory::GetIDList</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-isearchfolderitemfactory-getidlist?branch=master) and [<strong>ISearchFolderItemFactory::GetShellItem</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-isearchfolderitemfactory-getshellitem?branch=master) return the two forms of the search specified by these parameters. <br/></td>
</tr>
<tr class="even">
<td>[<strong>ISharedBitmap</strong>](/windows/win32/Thumbcache/nn-thumbcache-isharedbitmap?branch=master)<br/></td>
<td>Exposes memory-efficient methods for accessing bitmaps. This interface is used as a thin wrapper around HBITMAP objects, allowing those objects to be reference counted and protected from having their underlying data changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISharingConfigurationManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-isharingconfigurationmanager?branch=master)<br/></td>
<td>Exposes methods that set and retrieve information about a computer's default sharing settings for the <strong>Users</strong> (<code>C:\Users</code>) or <strong>Public</strong> (<code>C:\Users\Public</code>) folder. Also exposes a set of methods that allow control of printer sharing.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellApp</strong>](/windows/win32/Shappmgr/nn-shappmgr-ishellapp?branch=master)<br/></td>
<td>Exposes methods that provide general information about an application to the Add/Remove Programs Application. You cannot use it outside the Add/Remove Programs application. The information given by this interface includes a list of supported management actions and whether the application is currently installed. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellBrowser</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ishellbrowser?branch=master)<br/></td>
<td>Implemented by hosts of Shell views (objects that implement [<strong>IShellView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview?branch=master)). Exposes methods that provide services for the view it is hosting and other objects that run in the context of the Explorer window. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellChangeNotify</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes a method that notifies a Shell namespace extension when the ID of an item has changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellDetails</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposed by Shell folders to provide detailed information about the items in a folder. This is the same information that is displayed by the Windows Explorer when the view of the folder is set to Details. For Windows 2000 and later systems, [<strong>IShellDetails</strong>](/windows/win32/Shlobj_core/?branch=master) is superseded by [<strong>IShellFolder2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellfolder2?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellExtInit</strong>](/windows/win32/Shobjidl/nn-shobjidl_core-ishellextinit?branch=master)<br/></td>
<td>Exposes a method that initializes Shell extensions for property sheets, shortcut menus, and drag-and-drop handlers (extensions that add items to shortcut menus during nondefault drag-and-drop operations).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolder</strong>](ishellfolder.md)<br/></td>
<td>Exposed by all Shell namespace folder objects, its methods are used to manage folders.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolder2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellfolder2?branch=master)<br/></td>
<td>Extends the capabilities of [<strong>IShellFolder</strong>](ishellfolder.md). Its methods provide a variety of information about the contents of a Shell folder.<br/></td>
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
<td>[<strong>IShellFolderViewCB</strong>](/windows/win32/Shlobj/?branch=master)<br/></td>
<td>Exposes a method that allows communication between Windows Explorer and a folder view implemented using the system folder view object (the [<strong>IShellView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview?branch=master) object returned through [<strong>SHCreateShellFolderView</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shcreateshellfolderview?branch=master)) so that the folder view can be notified of events and modify its view accordingly.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolderViewDual</strong>](/windows/win32/Shldisp/nn-shldisp-ishellfolderviewdual?branch=master)<br/></td>
<td>Exposes methods that modify the view and select items in the current folder. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolderViewDual2</strong>](/windows/win32/Shldisp/nn-shldisp-ishellfolderviewdual2?branch=master)<br/></td>
<td>Exposes methods that modify the view and select items in the current folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolderViewDual3</strong>](/windows/win32/Shldisp/nn-shldisp-ishellfolderviewdual3?branch=master)<br/></td>
<td>Exposes methods that modify the current folder view.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolderViewType</strong>](ishellfolderviewtype.md)<br/></td>
<td>Exposes methods that enable a Shell folder to support different views on its content (different hierarchical layouts of its data).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellIcon</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellicon?branch=master)<br/></td>
<td>Exposes a method that obtains an icon index for an [<strong>IShellFolder</strong>](ishellfolder.md) object. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellIconOverlay</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes methods that are used by a namespace extension to specify icon overlays for the objects it contains.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellIconOverlayIdentifier</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishelliconoverlayidentifier?branch=master)<br/></td>
<td>Exposes methods that handle all communication between icon overlay handlers and the Shell.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellImageDataAbort</strong>](/windows/win32/Shimgdata/nn-shimgdata-ishellimagedataabort?branch=master)<br/></td>
<td>Exposes a single method used to abort [<strong>IShellImageData</strong>](/windows/win32/Shimgdata/nn-shimgdata-ishellimagedata?branch=master) processes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellImageDataFactory</strong>](/windows/win32/Shimgdata/nn-shimgdata-ishellimagedatafactory?branch=master)<br/></td>
<td>Exposes methods that create [<strong>IShellImageData</strong>](/windows/win32/Shimgdata/nn-shimgdata-ishellimagedata?branch=master) instances based on various image sources.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master)<br/></td>
<td>Exposes methods that retrieve information about a Shell item. [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) and [<strong>IShellItem2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem2?branch=master) are the preferred representations of items in any new code.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellItem2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem2?branch=master)<br/></td>
<td>Extends [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) with methods that retrieve various property values of the item. <strong>IShellItem</strong> and [<strong>IShellItem2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem2?branch=master) are the preferred representations of items in any new code.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellItemArray</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitemarray?branch=master)<br/></td>
<td>Exposes methods that create and manipulate [<strong>Shell item</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) arrays.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellItemFilter</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitemfilter?branch=master)<br/></td>
<td>Exposed by a client to specify how to filter the enumeration of a [<strong>Shell item</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) by a server application.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellItemImageFactory</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory?branch=master)<br/></td>
<td>Exposes a method to return either icons or thumbnails for Shell items. If no thumbnail or icon is available for the requested item, a per-class icon may be provided from the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellItemResources</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitemresources?branch=master)<br/></td>
<td>Exposes methods to manipulate and query Shell item resources.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellLibrary</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishelllibrary?branch=master)<br/></td>
<td>Exposes methods for creating and managing libraries.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellLink</strong>](/windows/win32/Shobjidl_core/nn-shobjidl_core-ishelllinka?branch=master)<br/></td>
<td>Exposes methods that create, modify, and resolve Shell links.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellLinkDataList</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishelllinkdatalist?branch=master)<br/></td>
<td>Exposes methods that allow an application to attach extra data blocks to a [Shell link](shell.Links). These methods add, copy, or remove data blocks.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellMenu</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellmenu?branch=master)<br/></td>
<td>Exposes methods that interact with Shell menus such as the <strong>Start</strong> menu, and the <strong>Favorites</strong> menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellMenuCallback</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellmenucallback?branch=master)<br/></td>
<td>A callback interface that exposes a method that receives messages from a menu band.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellPropSheetExt</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellpropsheetext?branch=master)<br/></td>
<td>Exposes methods that allow a property sheet handler to add or replace pages in the property sheet displayed for a file object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellRunDll</strong>](/windows/win32/shobjidl/nn-shobjidl-ishellrundll?branch=master)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IShellView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview?branch=master)<br/></td>
<td>Exposes methods that present a view in the Windows Explorer or folder windows.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellView2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview2?branch=master)<br/></td>
<td>Extends the capabilities of [<strong>IShellView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellView3</strong>](/windows/win32/Shobjidl/nn-shobjidl-ishellview3?branch=master)<br/></td>
<td>Extends the capabilities of [<strong>IShellView2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview2?branch=master) by providing a method to replace [<strong>IShellView2::CreateViewWindow2</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellview2-createviewwindow2?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellWindows</strong>](/windows/win32/Exdisp/nn-exdisp-ishellwindows?branch=master)<br/></td>
<td>Provides access to the collection of open Shell windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IStartMenuPinnedList</strong>](/windows/win32/Shobjidl/nn-shobjidl-istartmenupinnedlist?branch=master)<br/></td>
<td>Exposes a method that unpins an application shortcut from the <strong>Start</strong> menu or the taskbar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IStorageProviderHandler</strong>](/windows/win32/storageprovider/nn-storageprovider-istorageproviderhandler?branch=master)<br/></td>
<td>Retrieves the [<strong>IStorageProviderPropertyHandler</strong>](/windows/win32/storageprovider/nn-storageprovider-istorageproviderpropertyhandler?branch=master) associated with a specific file or folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IStorageProviderPropertyHandler</strong>](/windows/win32/storageprovider/nn-storageprovider-istorageproviderpropertyhandler?branch=master)<br/></td>
<td>Provides a collection of properties associated with a file or folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IStreamAsync</strong>](/windows/win32/Shobjidl/nn-shobjidl-istreamasync?branch=master)<br/></td>
<td>Exposes methods to manage input/outpout (I/O) to an asynchronous stream. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IStreamUnbufferedInfo</strong>](/windows/win32/Shobjidl/nn-shobjidl-istreamunbufferedinfo?branch=master)<br/></td>
<td>Exposes a method that determines the sector size as an aid to byte alignment.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISuspensionDependencyManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-isuspensiondependencymanager?branch=master)<br/></td>

</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflict</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrconflict?branch=master)<br/></td>
<td>Exposes methods that provide information about a conflict retrieved from a conflict store, and allows the conflict to be resolved.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrConflictFolder</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrconflictfolder?branch=master)<br/></td>
<td>Exposes a method that gets the conflict ID list for a conflict object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflictItems</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrconflictitems?branch=master)<br/></td>
<td>Exposes methods that get conflict item data and item count.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrConflictPresenter</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrconflictpresenter?branch=master)<br/></td>
<td>Exposes a method that presents a conflict to the user.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflictResolutionItems</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrconflictresolutionitems?branch=master)<br/></td>
<td>Exposes methods that get item info and item count.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrConflictResolveInfo</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrconflictresolveinfo?branch=master)<br/></td>
<td>Exposes methods that get and set information about sync manager conflict resolution.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflictStore</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrconflictstore?branch=master)<br/></td>
<td>Exposes methods that allow a handler to provide conflicts that appear in the Conflicts folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrControl</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrcontrol?branch=master)<br/></td>
<td>Exposes methods that allow an application or handler to start or stop a synchronization, notify Sync Center of changes to the set of handlers or items, or notify of changes to property values.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrEnumItems</strong>](/windows/win32/mobsync/nn-mobsync-isyncmgrenumitems?branch=master)<br/></td>
<td>Exposes methods that enumerate through an array of [<strong>SYNCMGRITEM</strong>](/windows/win32/Mobsync/ns-mobsync-_tagsyncmgritem?branch=master) structures. Each of these structures provides information about an item that can be synchronized. [<strong>ISyncMgrEnumItems</strong>](/windows/win32/mobsync/nn-mobsync-isyncmgrenumitems?branch=master) has the same methods as all standard enumerator interfaces: Next, Skip, Reset, and Clone.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrEvent</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrevent?branch=master)<br/></td>
<td>Exposes methods that retrieve data from an event store. An event store allows Sync Center to get an enumerator of all events in the store, as well as to retrieve individual events.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrEventLinkUIOperation</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgreventlinkuioperation?branch=master)<br/></td>
<td>Provides a method that is called when event links are clicked in the sync results folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrEventStore</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgreventstore?branch=master)<br/></td>
<td>Exposes methods that allow a handler to provide its own event store and manage its own sync events, instead of using the default Sync Center event store. These events are displayed in the Sync Results folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrHandler</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrhandler?branch=master)<br/></td>
<td>Exposes methods that make up the primary interface implemented by a sync handler. Sync Center creates one instance of the handler through this interface to get properties, enumerate sync items, and modify state. Sync Center creates a separate instance of the handler on a separate thread to perform a synchronization or a UI operation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrHandlerCollection</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrhandlercollection?branch=master)<br/></td>
<td>Exposes methods that provide an enumerator of sync handler IDs and instantiate those sync handlers.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrHandlerInfo</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrhandlerinfo?branch=master)<br/></td>
<td>Exposes methods that allow a handler to provide property and state information to Sync Center.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrRegister</strong>](/windows/win32/Mobsync/nn-mobsync-isyncmgrregister?branch=master)<br/></td>
<td>Exposes methods so that an application can register with the synchronization manager. This can be achieved either through the [<strong>ISyncMgrRegister</strong>](/windows/win32/Mobsync/nn-mobsync-isyncmgrregister?branch=master) interface or by registering directly in the registry.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrResolutionHandler</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrresolutionhandler?branch=master)<br/></td>
<td>Exposes methods that manage synchronizing conflicts. Implement this interface to construct a sync conflict handler. The conflict resolution user interface (UI) will call this interface to resolve the conflict presented to the user. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrScheduleWizardUIOperation</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrschedulewizarduioperation?branch=master)<br/></td>
<td>Exposes a method that allows a handler to display the sync schedule wizard for the handler.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSessionCreator</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrsessioncreator?branch=master)<br/></td>
<td>Exposes a single method through which a handler or external application can notify Sync Center that synchronization has begun, as well as report progress and events.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSyncCallback</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrsynccallback?branch=master)<br/></td>
<td>Exposes methods that allow a synchronization process to report progress and events to Sync Center, or to query whether the process has been canceled.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSynchronize</strong>](/windows/win32/Mobsync/nn-mobsync-isyncmgrsynchronize?branch=master)<br/></td>
<td>Exposes methods that enable the registered application or service to receive notifications from the synchronization manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSynchronizeCallback</strong>](/windows/win32/mobsync/nn-mobsync-isyncmgrsynchronizecallback?branch=master)<br/></td>
<td>Exposes methods that manage the synchronization process.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSynchronizeInvoke</strong>](/windows/win32/Mobsync/nn-mobsync-isyncmgrsynchronizeinvoke?branch=master)<br/></td>
<td>Exposes methods that enable a registered application to invoke the synchronization manager to update items.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSyncItem</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrsyncitem?branch=master)<br/></td>
<td>Exposes methods that act on and retrieve information from a single sync item, allowing handlers to manage sync items as independent objects.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSyncItemContainer</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrsyncitemcontainer?branch=master)<br/></td>
<td>Exposes methods that provide information to handlers about the items they contain.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSyncItemInfo</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrsynciteminfo?branch=master)<br/></td>
<td>Exposes methods that provide property and state information for a single sync item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSyncResult</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrsyncresult?branch=master)<br/></td>
<td>Exposes a method that applications calling [<strong>ISyncMgrControl</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrcontrol?branch=master) can use to get the result of a [<strong>ISyncMgrControl::StartHandlerSync</strong>](/windows/win32/Syncmgr/nf-syncmgr-isyncmgrcontrol-starthandlersync?branch=master) or [<strong>ISyncMgrControl::StartItemSync</strong>](/windows/win32/Syncmgr/nf-syncmgr-isyncmgrcontrol-startitemsync?branch=master) call.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrUIOperation</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgruioperation?branch=master)<br/></td>
<td>Exposes a method through which a sync handler or sync item can display a UI object when requested to do so by Sync Center.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITaskbarList</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itaskbarlist?branch=master)<br/></td>
<td>Exposes methods that control the taskbar. It allows you to dynamically add, remove, and activate items on the taskbar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITaskbarList2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itaskbarlist2?branch=master)<br/></td>
<td>Extends the [<strong>ITaskbarList</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itaskbarlist?branch=master) interface by exposing a method to mark a window as a full-screen display.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITaskbarList3</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itaskbarlist3?branch=master)<br/></td>
<td>Extends [<strong>ITaskbarList2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itaskbarlist2?branch=master) by exposing methods that support the unified launching and switching taskbar button functionality added in Windows 7. This functionality includes thumbnail representations and switch targets based on individual tabs in a tabbed application, thumbnail toolbars, notification and status overlays, and progress indicators.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITaskbarList4</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itaskbarlist4?branch=master)<br/></td>
<td>Extends [<strong>ITaskbarList3</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itaskbarlist3?branch=master) by providing a method that allows the caller to control two property values for the tab thumbnail and peek feature.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IThumbnailCache</strong>](/windows/win32/Thumbcache/nn-thumbcache-ithumbnailcache?branch=master)<br/></td>
<td>Exposes methods for a system thumbnail cache that is shared across applications.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IThumbnailCachePrimer</strong>](/windows/win32/thumbcache/nn-thumbcache-ithumbnailcacheprimer?branch=master)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IThumbnailHandlerFactory</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ithumbnailhandlerfactory?branch=master)<br/></td>
<td>Exposes a method for retrieving the thumbnail handler of an item. Implement this interface if you want to specify what extractor is used for a child IDList.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IThumbnailProvider</strong>](/windows/win32/Thumbcache/nn-thumbcache-ithumbnailprovider?branch=master)<br/></td>
<td>Exposes a method for getting a thumbnail image and is intended to be implemented for thumbnail handlers. The object that implements this interface must also implement [<strong>IInitializeWithStream</strong>](/windows/win32/Propsys/nn-propsys-iinitializewithstream?branch=master). <br/></td>
</tr>
<tr class="even">
<td>[<strong>IThumbnailSettings</strong>](/windows/win32/Thumbcache/nn-thumbcache-ithumbnailsettings?branch=master)<br/></td>
<td>Provides a method that enables a thumbnail provider to determine the user context of a thumbnail request.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IThumbnailStreamCache</strong>](/windows/win32/thumbnailstreamcache/nn-thumbnailstreamcache-ithumbnailstreamcache?branch=master)<br/></td>
<td>Gets or sets the thumbnail stream. This interface is for internal use only and can only be called by the photos application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITrackShellMenu</strong>](/windows/win32/Shdeprecated/nn-shdeprecated-itrackshellmenu?branch=master)<br/></td>
<td>Exposes methods that extend the [<strong>IShellMenu</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellmenu?branch=master) interface by providing the ability to coordinate toolbar buttons with a menu as well as display a pop-up menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITranscodeImage</strong>](/windows/win32/Imagetranscode/nn-imagetranscode-itranscodeimage?branch=master)<br/></td>
<td>Exposes a method that allows conversion to JPEG or bitmap (BMP) image formats from any image type supported by Windows. <br/></td>
</tr>
<tr class="even">
<td>[<strong>ITransferAdviseSink</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itransferadvisesink?branch=master)<br/></td>
<td>Exposes methods supporting status collection and failure information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITransferDestination</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itransferdestination?branch=master)<br/></td>
<td>Exposes methods that create a destination Shell item for a copy or move operation. This interface is provided to allow more control over file operations by providing an [<strong>ITransferDestination::Advise</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-itransferdestination-advise?branch=master) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITransferMediumItem</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Used by a copy engine to get the item on which to call [<strong>QueryInterface</strong>](com.iunknown_queryinterface) to return a pointer to interface [<strong>ITransferDestination</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itransferdestination?branch=master) or interface [<strong>ITransferSource</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itransfersource?branch=master). These interfaces can be queried and enumerated for copy, move, or delete operations.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITransferSource</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itransfersource?branch=master)<br/></td>
<td>Exposes methods to manipulate [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master), including copy, move, recycle, and others. This interface is offered to provide more control over file operations by providing an [<strong>ITransferSource::Advise</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-itransfersource-advise?branch=master) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITrayDeskBand</strong>](/windows/win32/Shobjidl/nn-shobjidl-itraydeskband?branch=master)<br/></td>
<td>Exposes methods that show, hide, and query deskbands.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IUpdateIDList</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iupdateidlist?branch=master)<br/></td>
<td>Provides a method to update the [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) of the child of an folder object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IURLSearchHook</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes a method that is used by the browser to translate the address of an unknown URL protocol.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IURLSearchHook2</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Exposes a method that is used by the browser to translate the address of an unknown URL protocol by using a search context object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IUserAccountChangeCallback</strong>](/windows/win32/Shobjidl/nn-shobjidl-iuseraccountchangecallback?branch=master)<br/></td>
<td>Exposes a method which is called when the picture that represents a user account is changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IUserNotification</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iusernotification?branch=master)<br/></td>
<td>Exposes methods that set notification information and then display that notification to the user in a balloon that appears in conjunction with the notification area of the taskbar. <br/>
<blockquote>
[!Note]<br />
[<strong>IUserNotification2</strong>](/windows/win32/Shobjidl/nn-shobjidl-iusernotification2?branch=master) differs from [<strong>IUserNotification</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iusernotification?branch=master) only in its [<strong>Show</strong>](/windows/win32/Shobjidl/nf-shobjidl-iusernotification2-show?branch=master) method, which adds an additional parameter for a callback interface to communicate with the notification. Otherwise the two interfaces are identical in form and function. CLSID_UserNotification implements both versions of <strong>Show</strong> as an overload.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IUserNotification2</strong>](/windows/win32/Shobjidl/nn-shobjidl-iusernotification2?branch=master)<br/></td>
<td>Exposes methods that set notification information and then display that notification to the user in a balloon that appears in conjunction with the notification area of the taskbar. <br/>
<blockquote>
[!Note]<br />
[<strong>IUserNotification2</strong>](/windows/win32/Shobjidl/nn-shobjidl-iusernotification2?branch=master) does not inherit from [<strong>IUserNotification</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iusernotification?branch=master). <strong>IUserNotification2</strong> differs from <strong>IUserNotification</strong> only in its [<strong>Show</strong>](/windows/win32/Shobjidl/nf-shobjidl-iusernotification2-show?branch=master) method, which adds an additional parameter for a callback interface to communicate with the notification. Otherwise the two interfaces are identical in form and function. CLSID_UserNotification implements both versions of <strong>Show</strong> as an overload.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IUserNotificationCallback</strong>](/windows/win32/Shobjidl/nn-shobjidl-iusernotificationcallback?branch=master)<br/></td>
<td>Exposes a method for the handling of a mouse click or shortcut menu access in a notification balloon. Used with [<strong>IUserNotification2::Show</strong>](/windows/win32/Shobjidl/nf-shobjidl-iusernotification2-show?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IUseToBrowseItem</strong>](/windows/win32/shobjidl/?branch=master)<br/></td>
<td>Finds the item that should be used when browsing to this item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IViewStateIdentityItem</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Provides a canonical persistence item, an item for which view customizations will be remembered.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IVirtualDesktopManager</strong>](/windows/win32/shobjidl/nn-shobjidl-ivirtualdesktopmanager?branch=master)<br/></td>
<td>Exposes methods that enable an application to interact with groups of windows that form virtual workspaces.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IVisualProperties</strong>](/windows/win32/Shobjidl/nn-shobjidl-ivisualproperties?branch=master)<br/></td>
<td>Exposes methods that set and get visual properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IWebWizardExtension</strong>](/windows/win32/Shobjidl/nn-shobjidl-iwebwizardextension?branch=master)<br/></td>
<td>Extends the [<strong>IWizardExtension</strong>](/windows/win32/Shobjidl/nn-shobjidl-iwizardextension?branch=master) interface by exposing methods to set the wizard extension's initial URL, and a specific URL in case of an error.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IWizardExtension</strong>](/windows/win32/Shobjidl/nn-shobjidl-iwizardextension?branch=master)<br/></td>
<td>Used by wizards such as the Web Publishing Wizard and Online Print Ordering Wizard which host server-side content pages. This interface exposes methods to specify supported extension pages and to navigate into and out of those pages.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IWizardSite</strong>](/windows/win32/Shobjidl/nn-shobjidl-iwizardsite?branch=master)<br/></td>
<td>Exposes methods used by a wizard extension to navigate the borders between itself and the rest of the wizard.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TaskCompletionClient</strong>](taskcompletionclient.md)<br/></td>
<td>Enables task completion. <br/></td>
</tr>
</tbody>
</table>



 

 

 




