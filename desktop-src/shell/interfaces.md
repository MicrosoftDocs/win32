---
Description: 'This section describes the Windows Shell interfaces.'
title: Shell Interfaces
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
<td>[<strong>IAccessibleObject</strong>](iaccessibleobject.md)<br/></td>
<td>Exposes a method that can be used by an accessibility application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAccessibilityDockingService</strong>](iaccessibilitydockingservice.md)<br/></td>
<td>Docks a single accessibility app window to the bottom of a screen.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAccessibilityDockingServiceCallback</strong>](iaccessibilitydockingservicecallback.md)<br/></td>
<td>Informs an accessibility app that its window has been undocked.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IACLCustomMRU</strong>](iaclcustommru.md)<br/></td>
<td>Exposes methods that are used to initialize a most recently used (MRU) list for an autocompletion object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IACList</strong>](iaclist.md)<br/></td>
<td>Exposes a method that improves the efficiency of [<strong>autocompletion</strong>](iautocomplete.md) when the candidate strings are organized in a hierarchy.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IACList2</strong>](iaclist2.md)<br/></td>
<td>Extends the [<strong>IACList</strong>](iaclist.md) interface to enable clients of an autocomplete object to retrieve and set option flags.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IActionProgress</strong>](iactionprogress.md)<br/></td>
<td>Represents the abstract base class from which progress-driven operations can inherit.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IActionProgressDialog</strong>](iactionprogressdialog.md)<br/></td>
<td>Exposes methods that initialize and stop a progress dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationActivationManager</strong>](iapplicationactivationmanager.md)<br/></td>
<td>Provides methods which activate Windows Store apps for the Launch, File, and Protocol [extensions](m_ca_contracts.capabilities_and_contracts_portal). You will normally use this interface in debuggers and design tools.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IApplicationAssociationRegistration</strong>](iapplicationassociationregistration.md)<br/></td>
<td>Exposes methods that query and set default applications for specific file [<strong>Association Type</strong>](associationtype.md), and protocols at a specific [<strong>Association Level</strong>](associationlevel.md). <br/>
<blockquote>
[!Note]<br />
As of Windows 8, the only functionality of this interface that is supported is [<strong>QueryCurrentDefault</strong>](iapplicationassociationregistration-querycurrentdefault.md).
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationAssociationRegistrationUI</strong>](iapplicationassociationregistrationui.md)<br/></td>
<td>Exposes a method that launches an advanced association dialog box through which the user can customize their associations.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IApplicationDesignModeSettings</strong>](iapplicationdesignmodesettings.md)<br/></td>
<td>Enables development tool applications to dynamically spoof system and user states, such as native display resolution, device scale factor, and application view state, for the purpose of testing Windows Store apps running in design mode for a wide range of form factors without the need for the actual hardware. Also enables testing of changes in normally user-controlled state to test Windows Store apps under a variety of scenarios.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationDesignModeSettings2</strong>](iapplicationdesignmodesettings2.md)<br/></td>
<td>Enables development tool applications to dynamically control system and user states, such as native display resolution, device scale factor, and application view layout, reported to Windows Store apps for the purpose of testing Windows Store apps running in design mode for a wide range of form factors without the need for the actual hardware. Also enables testing of changes in normally user-controlled state to test Windows Store apps under a variety of scenarios.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IApplicationDestinations</strong>](iapplicationdestinations.md)<br/></td>
<td>Exposes methods that allow an application to remove one or all destinations from the <strong>Recent</strong> or <strong>Frequent</strong> categories in a Jump List.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IApplicationDocumentLists</strong>](iapplicationdocumentlists.md)<br/></td>
<td>Exposes methods that allow an application to retrieve the contents of the <strong>Recent</strong> or <strong>Frequent</strong> categories in a Jump List.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAppPublisher</strong>](iapppublisher.md)<br/></td>
<td>Exposes methods for publishing applications through <strong>Add/Remove Programs</strong> in Control Panel. This is the principal interface implemented for this purpose.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAppVisibility</strong>](iappvisibility.md)<br/></td>
<td>Provides functionality to determine whether the display is showing Windows Store apps.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAppVisibilityEvents</strong>](iappvisibilityevents.md)<br/></td>
<td>Enables applications to receive notifications of state changes in a display and of changes in Start screen visibility.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAssocHandler</strong>](iassochandler.md)<br/></td>
<td>Exposes methods for operations with a file association dialog box or menu.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAssocHandlerInvoker</strong>](iassochandlerinvoker.md)<br/></td>
<td>Exposes methods that invoke an associated application handler.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAttachmentExecute</strong>](iattachmentexecute.md)<br/></td>
<td>Exposes methods that work with client applications to present a user environment that provides safe download and exchange of files through email and messaging attachments.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAutoComplete</strong>](iautocomplete.md)<br/></td>
<td>Exposed by the autocomplete object (CLSID_AutoComplete). This interface allows applications to initialize, enable, and disable the object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAutoComplete2</strong>](iautocomplete2.md)<br/></td>
<td>Extends [<strong>IAutoComplete</strong>](iautocomplete.md). This interface enables clients of the autocomplete object to retrieve and set a number of options that control how autocompletion operates.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IAutoCompleteDropDown</strong>](iautocompletedropdown.md)<br/></td>
<td>Exposes methods that allow clients to reset or query the display state of the autocomplete drop-down list, which contains possible completions to a string entered by the user in an edit control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IBandHost</strong>](ibandhost.md)<br/></td>
<td>Exposes methods that create and destroy bands and specifiy their availability.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IBandSite</strong>](ibandsite.md)<br/></td>
<td>Exposes methods that control band objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IBrowserFrameOptions</strong>](ibrowserframeoptions.md)<br/></td>
<td>Allows a browser or host to ask [<strong>IShellView</strong>](ishellview.md) what kind of view behavior is supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICategorizer</strong>](icategorizer.md)<br/></td>
<td>Exposes methods that are used to obtain information about item identifier lists.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICategoryProvider</strong>](icategoryprovider.md)<br/></td>
<td>Exposes a list of categorizers registered on an [<strong>IShellFolder</strong>](ishellfolder.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICDBurn</strong>](icdburn.md)<br/></td>
<td>Exposes methods that determine whether a system has hardware for writing to CD, the drive letter of a CD writer device, and programmatically initiate a CD writing session. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IColumnManager</strong>](icolumnmanager.md)<br/></td>
<td>Exposes methods that enable inspection and manipulation of columns in the Windows Explorer Details view. Each column is referenced by a [<strong>PROPERTYKEY</strong>](properties.PROPERTYKEY) structure, which names a property.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICommDlgBrowser</strong>](icommdlgbrowser.md)<br/></td>
<td>Exposed by the common file dialog boxes to be used when they host a Shell browser. If supported, [<strong>ICommDlgBrowser</strong>](icommdlgbrowser.md) exposes methods that allow a Shell view to handle several cases that require different behavior in a dialog box than in a normal Shell view. You obtain an <strong>ICommDlgBrowser</strong> interface pointer by calling [<strong>QueryInterface</strong>](com.iunknown_queryinterface) on the [<strong>IShellBrowser</strong>](ishellbrowser.md) object. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICommDlgBrowser2</strong>](icommdlgbrowser2.md)<br/></td>
<td>Extends the capabilities of [<strong>ICommDlgBrowser</strong>](icommdlgbrowser.md). This interface is exposed by the common file dialog boxes when they host a Shell browser. A pointer to [<strong>ICommDlgBrowser2</strong>](icommdlgbrowser2.md) can be obtained by calling [<strong>QueryInterface</strong>](com.iunknown_queryinterface) on the [<strong>IShellBrowser</strong>](ishellbrowser.md) object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICommDlgBrowser3</strong>](icommdlgbrowser3.md)<br/></td>
<td>Extends the capabilities of [<strong>ICommDlgBrowser2</strong>](icommdlgbrowser2.md), and used by the common file dialog boxes when they host a Shell browser.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IComputerInfoChangeNotify</strong>](icomputerinfochangenotify.md)<br/></td>
<td>This interface may be absent in later versions of Windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IConnectableCredentialProviderCredential</strong>](iconnectablecredentialprovidercredential.md)<br/></td>
<td>Exposes methods for connecting and disconnecting [<strong>IConnectableCredentialProviderCredential</strong>](iconnectablecredentialprovidercredential.md) objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IContactManagerInterop</strong>](icontactmanagerinterop.md)<br/></td>
<td>Enables access to [<strong>ContactManager</strong>](icontactmanagerinterop.md) methods in an app that manages multiple windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IContextMenu</strong>](icontextmenu.md)<br/></td>
<td>Exposes methods that either create or merge a shortcut menu associated with a Shell object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IContextMenu2</strong>](icontextmenu2.md)<br/></td>
<td>Exposes methods that either create or merge a shortcut (context) menu associated with a Shell object. Extends [<strong>IContextMenu</strong>](icontextmenu.md) by adding a method that allows client objects to handle messages associated with owner-drawn menu items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IContextMenu3</strong>](icontextmenu3.md)<br/></td>
<td>Exposes methods that either create or merge a shortcut menu associated with a Shell object. Allows client objects to handle messages associated with owner-drawn menu items and extends [<strong>IContextMenu2</strong>](icontextmenu2.md) by accepting a return value from that message handling.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IContextMenuCB</strong>](icontextmenucb.md)<br/></td>
<td>Exposes a method that enables the callback of a context menu. For example, to add a shield icon to a <strong>menuItem</strong> that requires elevation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IControlMarkup</strong>](icontrolmarkup.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>ICopyHook</strong>](icopyhook.md)<br/></td>
<td>Exposes a method that creates a <em>copy hook handler</em>. A copy hook handler is a Shell extension that determines if a Shell folder or printer object can be moved, copied, renamed, or deleted. The Shell calls the [<strong>ICopyHook::CopyCallback</strong>](icopyhook-copycallback.md) method prior to performing one of these operations.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICreateObject</strong>](icreateobject.md)<br/></td>
<td>Exposes a method that creates an object of a specified class.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICreatingProcess</strong>](icreatingprocess.md)<br/></td>
<td>Used by [<strong>ShellExecuteEx</strong>](shellexecuteex.md) and [<strong>IContextMenu</strong>](icontextmenu.md) to allow the caller to alter some parameters of the process being created.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICreateProcessInputs</strong>](icreateprocessinputs.md)<br/></td>
<td>Used by the [<strong>ICreatingProcess</strong>](icreatingprocess.md) interface to alter some parameters of the process that is being created.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProvider</strong>](icredentialprovider.md)<br/></td>
<td>Exposes methods used in the setup and manipulation of a credential provider. All credential providers must implement this interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderCredential</strong>](icredentialprovidercredential.md)<br/></td>
<td>Exposes methods that enable the handling of a credential.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderCredential2</strong>](icredentialprovidercredential2.md)<br/></td>
<td>Extends the [<strong>ICredentialProviderCredential</strong>](icredentialprovidercredential.md) interface by adding a method that retrieves the security identifier (SID) of a user. The credential is associated with that user and can be grouped under the user's tile.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderCredentialEvents</strong>](icredentialprovidercredentialevents.md)<br/></td>
<td>Provides an asynchronous callback mechanism used by a credential to notify it of state or text change events in the Logon UI or Credential UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderCredentialEvents2</strong>](icredentialprovidercredentialevents2.md)<br/></td>
<td>Extends the [<strong>ICredentialProviderCredentialEvents</strong>](icredentialprovidercredentialevents.md) interface by adding methods that enable batch updating of fields in theLogon UI or Credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderCredentialWithFieldOptions</strong>](icredentialprovidercredentialwithfieldoptions.md)<br/></td>
<td>Provides a method that enables the credential provider framework to determine whether you've made a customization to a field's option in a logon or credential UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderEvents</strong>](icredentialproviderevents.md)<br/></td>
<td>Provides an asynchronous callback mechanism used by a credential provider to notify it of changes in the list of credentials or their fields.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderFilter</strong>](icredentialproviderfilter.md)<br/></td>
<td>Used to dynamically filter credential providers based on information available at runtime.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderSetUserArray</strong>](icredentialprovidersetuserarray.md)<br/></td>
<td>Provides a method that enables a credential provider to receive the set of users that will be shown in the logon or credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICredentialProviderUser</strong>](icredentialprovideruser.md)<br/></td>
<td>Provides methods used to retrieve certain properties of an individual user included in a logon or credential UI.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICredentialProviderUserArray</strong>](icredentialprovideruserarray.md)<br/></td>
<td>Represents the set of users that will appear in the logon or credential UI. This information enables the credential provider to enumerate the set to retrieve property information about each user to populate fields or filter the set.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICurrentItem</strong>](icurrentitem.md)<br/></td>
<td>Obtained by calling [<strong>IShellFolder::BindToObject</strong>](ishellfolder-bindtoobject.md) for an item. If the item represents a snapshot of an item at a previous time, this interface will obtain the current version of the item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ICurrentWorkingDirectory</strong>](icurrentworkingdirectory.md)<br/></td>
<td>Exposes methods that enable a client to retrieve or set an object's current working directory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ICustomDestinationList</strong>](icustomdestinationlist.md)<br/></td>
<td>Exposes methods that allow an application to provide a custom Jump List, including destinations and tasks, for display in the taskbar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDataObjectAsyncCapability</strong>](idataobjectasynccapability.md)<br/></td>
<td>Enables interfaces that are usually synchronous to function asynchronously. <br/>
<blockquote>
[!Note]<br />
This interface is the current, renamed version of [<strong>IAsyncOperation</strong>](shell.IAsyncOperation).
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDataObjectProvider</strong>](idataobjectprovider.md)<br/></td>
<td>Provides methods that enable you to set or retrieve a [DataPackage](http://go.microsoft.com/fwlink/p/?linkid=267543) object's [<strong>IDataObject interface</strong>](com.idataobject), which the DataPackage uses to support interoperability. The DataPackage object is used by an app to provide data to another app.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDataTransferManagerInterop</strong>](idatatransfermanagerinterop.md)<br/></td>
<td>Enables access to [<strong>DataTransferManager</strong>](w_appmod_dataxfer.datatransfermanager) methods in a Windows Store app that manages multiple windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDefaultExtractIconInit</strong>](idefaultextracticoninit.md)<br/></td>
<td>Exposes methods to set default icons associated with an object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDefaultFolderMenuInitialize</strong>](idefaultfoldermenuinitialize.md)<br/></td>
<td>Provides methods used to get and set shortcut menu information. This information is the same as that provided to [<strong>SHCreateDefaultContextMenu</strong>](shcreatedefaultcontextmenu.md) through the [<strong>DEFCONTEXTMENU</strong>](defcontextmenu.md) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDelayedPropertyStoreFactory</strong>](idelayedpropertystorefactory.md)<br/></td>
<td>Exposes a method to create a specified [<strong>IPropertyStore</strong>](properties.IPropertyStore) object in circumstances where property access is potentially slow.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDelegateFolder</strong>](idelegatefolder.md)<br/></td>
<td>Exposes a method through which a delegate folder is given the [<strong>IMalloc</strong>](com.imalloc) interface required to allocate and free item IDs.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDelegateItem</strong>](idelegateitem.md)<br/></td>
<td>Used to obtain the immediately underlying representation of an item's path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDesktopGadget</strong>](idesktopgadget.md)<br/></td>
<td>Exposes a method that allows the programmatic addition of an installed gadget to the user's desktop.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDesktopWallpaper</strong>](idesktopwallpaper.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IDestinationStreamFactory</strong>](idestinationstreamfactory.md)<br/></td>
<td>Exposes a method for manually copying a stream or file before applying changes to properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDisplayItem</strong>](idisplayitem.md)<br/></td>
<td>Exposes methods that find a version of the current item to be used to get display properties, such as the item name, that will be displayed in the UI. Used by the copy engine dialogs to provide the UI with an appropriate item to display. If no other version can be found, the current item is used.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDockingWindow</strong>](idockingwindow.md)<br/></td>
<td>Exposes methods that notify the docking window object of changes, including showing, hiding, and impending removal. This interface is implemented by window objects that can be docked within the border space of a Windows Explorer window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDockingWindowFrame</strong>](idockingwindowframe.md)<br/></td>
<td>Exposes methods that support the addition of [<strong>IDockingWindow</strong>](idockingwindow.md) objects to a frame. Implemented by the browser.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDockingWindowSite</strong>](idockingwindowsite.md)<br/></td>
<td>Exposes methods that manage the border space for one or more [<strong>IDockingWindow</strong>](idockingwindow.md) objects. This interface is implemented by the browser and is similar to the [<strong>IOleInPlaceUIWindow</strong>](com.ioleinplaceuiwindow) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDragSourceHelper</strong>](idragsourcehelper.md)<br/></td>
<td>Exposed by the Shell to allow an application to specify the image that will be displayed during a Shell drag-and-drop operation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDragSourceHelper2</strong>](idragsourcehelper2.md)<br/></td>
<td>Exposes a method that adds functionality to [<strong>IDragSourceHelper</strong>](idragsourcehelper.md). This method sets the characteristics of a drag-and-drop operation over an <strong>IDragSourceHelper</strong> object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDropTargetHelper</strong>](idroptargethelper.md)<br/></td>
<td>Exposes methods that allow drop targets to display a drag image while the image is over the target window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IDynamicHWHandler</strong>](idynamichwhandler.md)<br/></td>
<td>Called by AutoPlay. Exposes methods that get dynamic information regarding a registered handler prior to displaying it to the user.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumAssocHandlers</strong>](ienumassochandlers.md)<br/></td>
<td>Exposes a method that allows enumeration of a collection of handlers associated with particular file name extensions.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumerableView</strong>](ienumerableview.md)<br/></td>
<td>Exposes methods that enumerate the contents of a view and receive notification from callback upon enumeration completion. This interface enables clients of a view to attempt to share the view's list of folder contents.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumExplorerCommand</strong>](ienumexplorercommand.md)<br/></td>
<td>Provided by an [<strong>IExplorerCommandProvider</strong>](iexplorercommandprovider.md). This interface contains the enumeration of commands to be put into the command bar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumExtraSearch</strong>](ienumextrasearch.md)<br/></td>
<td>A standard OLE enumerator used by a client to determine the available search objects for a folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumFullIDList</strong>](ienumfullidlist.md)<br/></td>
<td>Exposes a standard set of methods that enumerate the pointers to item identifier lists (PIDLs) of the items in a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumIDList</strong>](ienumidlist.md)<br/></td>
<td>Exposes a standard set of methods used to enumerate the PIDLs of the items in a Shell folder. When a folder's [<strong>IShellFolder::EnumObjects</strong>](ishellfolder-enumobjects.md) method is called, it creates an enumeration object and passes a pointer to the object's [<strong>IEnumIDList</strong>](ienumidlist.md) interface back to the calling application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumObjects</strong>](ienumobjects.md)<br/></td>
<td>Exposes methods to enumerate unknown objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumPublishedApps</strong>](ienumpublishedapps.md)<br/></td>
<td>Exposes methods that enumerate published applications to Add/Remove Programs in the Control Panel. The object exposing this interface is requested through [<strong>IAppPublisher::EnumApps</strong>](iapppublisher-enumapps.md). <br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumReadyCallback</strong>](ienumreadycallback.md)<br/></td>
<td>Exposes methods that enable the view to notify the implementer when the enumeration has completed. The view calls this method to tell the implementer that the enumeration can be retrieved via [<strong>IEnumerableView::CreateEnumIDListFromContents</strong>](ienumerableview-createenumidlistfromcontents.md). The callback allows the implementer to share the views enumeration.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumResources</strong>](ienumresources.md)<br/></td>
<td>Exposes resource enumeration methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumShellItems</strong>](ienumshellitems.md)<br/></td>
<td>Exposes enumeration of [<strong>IShellItem</strong>](ishellitem.md) interfaces. This interface is typically obtained by calling the [<strong>IEnumShellItems</strong>](ienumshellitems.md) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumSyncMgrConflict</strong>](ienumsyncmgrconflict.md)<br/></td>
<td>Exposes conflict enumeration methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IEnumSyncMgrEvents</strong>](ienumsyncmgrevents.md)<br/></td>
<td>Exposes sync event enumeration methods.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IEnumSyncMgrSyncItems</strong>](ienumsyncmgrsyncitems.md)<br/></td>
<td>Exposes methods that enumerate the sync item objects managed by the handler.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExecuteCommand</strong>](iexecutecommand.md)<br/></td>
<td>Exposes methods that set a given state or parameter related to the command verb, as well as a method to invoke that verb.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExecuteCommandApplicationHostEnvironment</strong>](iexecutecommandapplicationhostenvironment.md)<br/></td>
<td>Provides a single method that enables an application to determine whether its host is in desktop or immersive mode.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExecuteCommandHost</strong>](iexecutecommandhost.md)<br/></td>
<td>Provides a method that enables an [<strong>IExplorerCommand</strong>](iexplorercommand.md)-based Shell verb handler to query the UI mode of the host component from which the application was invoked.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExplorerBrowser</strong>](iexplorerbrowser.md)<br/></td>
<td>[<strong>IExplorerBrowser</strong>](iexplorerbrowser.md) is a browser object that can be either navigated or that can host a view of a data object. As a full-featured browser object, it also supports an automatic travel log.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExplorerBrowserEvents</strong>](iexplorerbrowserevents.md)<br/></td>
<td>Exposes methods for notification of Explorer browser navigation and view creation events.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExplorerCommand</strong>](iexplorercommand.md)<br/></td>
<td>Exposes methods that get the command appearance, enumerate subcommands, or invoke the command.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExplorerCommandProvider</strong>](iexplorercommandprovider.md)<br/></td>
<td>Exposes methods to create Explorer commands and command enumerators.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExplorerCommandState</strong>](iexplorercommandstate.md)<br/></td>
<td>Exposes a single method that allows retrieval of the command state.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExplorerPaneVisibility</strong>](iexplorerpanevisibility.md)<br/></td>
<td>Used in Windows Explorer by an [<strong>IShellFolder</strong>](ishellfolder.md) implementation to give suggestions to the view about what panes are visible. Additionally, an [<strong>IExplorerBrowser</strong>](iexplorerbrowser.md) host can use this interface to provide information about pane visibility. The host should implement [<strong>QueryService</strong>](_inet_IServiceProvider_QueryService_Method) with <strong>SID_ExplorerPaneVisibility</strong> as the service ID. The host must be in the site chain. <br/> The [<strong>IExplorerPaneVisibility</strong>](iexplorerpanevisibility.md) implementation is retrieved from the Shell folder. The Shell folder, in turn, is retrieved from the view. A namespace extension can elect to provide a custom view ([<strong>IShellView</strong>](ishellview.md)) rather than using the system folder view object (DefView). In that case, the <strong>IShellView</strong> implementation must include an implementation of [<strong>IFolderView::GetFolder</strong>](ifolderview-getfolder.md) to return the <strong>IExplorerPaneVisibility</strong> object.<br/> A namespace extension can provide a custom view by implementing [<strong>IShellView</strong>](ishellview.md) itself rather than using the system folder view object (DefView). In that case, the <strong>IShellView</strong> implementation must include an implementation of [<strong>IFolderView::GetFolder</strong>](ifolderview-getfolder.md) to make use of [<strong>IExplorerPaneVisibility</strong>](iexplorerpanevisibility.md) .<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExtractIcon</strong>](iextracticon.md)<br/></td>
<td>Exposes methods that allow a client to retrieve the icon that is associated with one of the objects in a folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IExtractImage</strong>](iextractimage.md)<br/></td>
<td>Exposes methods that request a thumbnail image from a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IExtractImage2</strong>](iextractimage2.md)<br/></td>
<td>Extends the capabilities of [<strong>IExtractImage</strong>](iextractimage.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileDialog</strong>](ifiledialog.md)<br/></td>
<td>Exposes methods that initialize, show, and get results from the common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileDialog2</strong>](ifiledialog2.md)<br/></td>
<td>Extends the [<strong>IFileDialog</strong>](ifiledialog.md) interface by providing methods that allow the caller to name a specific, restricted location that can be browsed in the common file dialog as well as to specify alternate text to display as a label on the <strong>Cancel</strong> button.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileDialogControlEvents</strong>](ifiledialogcontrolevents.md)<br/></td>
<td>Exposes methods that allow an application to be notified of events that are related to controls that the application has added to a common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileDialogCustomize</strong>](ifiledialogcustomize.md)<br/></td>
<td>Exposes methods that allow an application to add controls to a common file dialog.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileDialogEvents</strong>](ifiledialogevents.md)<br/></td>
<td>Exposes methods that allow notification of events within a common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileIsInUse</strong>](ifileisinuse.md)<br/></td>
<td>Exposes methods that can be called to get information on or close a file that is in use by another application. When an application attempts to access a file and finds that file already in use, it can use the methods of this interface to gather information to present to the user in a dialog box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileOpenDialog</strong>](ifileopendialog.md)<br/></td>
<td>Extends the [<strong>IFileDialog</strong>](ifiledialog.md) interface by adding methods specific to the open dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileOperation</strong>](ifileoperation.md)<br/></td>
<td>Exposes methods to copy, move, rename, create, and delete Shell items as well as methods to provide progress and error dialogs. This interface replaces the [<strong>SHFileOperation</strong>](shfileoperation.md) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileOperationProgressSink</strong>](ifileoperationprogresssink.md)<br/></td>
<td>Exposes methods that provide a rich notification system used by callers of [<strong>IFileOperation</strong>](ifileoperation.md) to monitor the details of the operations they are performing through that interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileSaveDialog</strong>](ifilesavedialog.md)<br/></td>
<td>Extends the [<strong>IFileDialog</strong>](ifiledialog.md) interface by adding methods specific to the save dialog, which include those that provide support for the collection of metadata to be persisted with the file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileSyncMergeHandler</strong>](ifilesyncmergehandler.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IFileSystemBindData</strong>](shell.ifilesystembinddata)<br/></td>
<td>Exposes methods that store file system information for optimizing calls to [<strong>IShellFolder::ParseDisplayName</strong>](ishellfolder-parsedisplayname.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileSystemBindData2</strong>](ifilesystembinddata2.md)<br/></td>
<td>Extends [<strong>IFileSystemBindData</strong>](shell.ifilesystembinddata), which stores file system information for optimizing calls to [<strong>IShellFolder::ParseDisplayName</strong>](ishellfolder-parsedisplayname.md). This interface adds the ability set or get file ID or junction class identifier (CLSID).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFileViewer</strong>](ifileviewer.md)<br/></td>
<td>Exposes methods that designate an interface that allows a registered file viewer to be notified when it must show or print a file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFileViewerSite</strong>](ifileviewersite.md)<br/></td>
<td>Exposes methods that designate an interface that allows a file viewer to retrieve the handle to the current pinned window, or to set a new pinned window. The pinned window is the window in which the current file viewer displays a file. When the user selects a new file to view, the Shell directs the file viewer to display the new file in the pinned window rather than create a new window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderFilter</strong>](ifolderfilter.md)<br/></td>
<td>Exposed by a client to specify how to filter the enumeration of a Shell folder by a server application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFolderFilterSite</strong>](ifolderfiltersite.md)<br/></td>
<td>Exported by a host to allow clients to specify how to filter a Shell folder enumeration.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderView</strong>](ifolderview.md)<br/></td>
<td>Exposes methods that retrieve information about a folder's display options, select specified items in that folder, and set the folder's view mode.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFolderView2</strong>](ifolderview2.md)<br/></td>
<td>Exposes methods that retrieve information about a folder's display options, select specified items in that folder, and set the folder's view mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderViewHost</strong>](ifolderviewhost.md)<br/></td>
<td>Exposes a method that hosts an [<strong>IFolderView</strong>](ifolderview.md) object in a window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFolderViewOptions</strong>](ifolderviewoptions.md)<br/></td>
<td>Exposes methods that allow control of folder view options specific to the Windows 7 and later views.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFolderViewSettings</strong>](ifolderviewsettings.md)<br/></td>
<td>Exposes methods to obtain folder view settings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IFrameworkInputPane</strong>](iframeworkinputpane.md)<br/></td>
<td>Provides methods that enable apps to be informed of state changes and location for the input pane.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IFrameworkInputPaneHandler</strong>](iframeworkinputpanehandler.md)<br/></td>
<td>Enables an app to be notified when the input pane (the on-screen keyboard or handwriting panel) is being shown or hidden. This allows the app window to adjust its display so that no input areas (such as a text box) are obscured by the input pane.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IHandlerActivationHost</strong>](ihandleractivationhost.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IHandlerInfo</strong>](ihandlerinfo.md)<br/></td>
<td>Supplies methods that provide information about the handler to methods of the [<strong>IHandlerActivationHost</strong>](ihandleractivationhost.md) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IHomeGroup</strong>](ihomegroup.md)<br/></td>
<td>Exposes methods that determine a computer's HomeGroup membership status and display the sharing wizard.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IHWEventHandler</strong>](ihweventhandler.md)<br/></td>
<td>Called by AutoPlay to implement the handling of registered media types.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IHWEventHandler2</strong>](ihweventhandler2.md)<br/></td>
<td>Extends the [<strong>IHWEventHandler</strong>](ihweventhandler.md) interface to address User Account Control (UAC) elevation for device handlers.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IIdentityName</strong>](iidentityname.md)<br/></td>
<td>Exposes methods to compare two items to see if they are the same.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IImageRecompress</strong>](iimagerecompress.md)<br/></td>
<td>Exposes a method that recompress images.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeCommand</strong>](iinitializecommand.md)<br/></td>
<td>Exposes a single method used to initialize objects that implement [<strong>IExplorerCommandState</strong>](iexplorercommandstate.md), [<strong>IExecuteCommand</strong>](iexecutecommand.md) or [<strong>IDropTarget</strong>](com.idroptarget) with the application-specified command name and its registered properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeNetworkFolder</strong>](iinitializenetworkfolder.md)<br/></td>
<td>Exposes a method that initializes the network data source CLSID_NetworkPlaces as specified.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeWithBindCtx</strong>](iinitializewithbindctx.md)<br/></td>
<td>Exposes a method that initializes a handler, such as a property handler, thumbnail handler, or preview handler, with a bind context.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeWithFile</strong>](iinitializewithfile.md)<br/></td>
<td>Exposes a method to initialize a handler, such as a property handler, thumbnail handler, or preview handler, with a file path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeWithItem</strong>](iinitializewithitem.md)<br/></td>
<td>Exposes a method used to initialize a handler, such as a property handler, thumbnail handler, or preview handler, with an [<strong>IShellItem</strong>](ishellitem.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeWithPropertyStore</strong>](iinitializewithpropertystore.md)<br/></td>
<td>Exposes a method that initializes a handler, such as a property handler, thumbnail handler, or preview handler, with a property store.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInitializeWithStream</strong>](iinitializewithstream.md)<br/></td>
<td>Exposes a method that initializes a handler, such as a property handler, thumbnail handler, or preview handler, with a stream.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInitializeWithWindow</strong>](iinitializewithwindow.md)<br/></td>
<td>Exposes a method through which a client can provide an owner window to a Windows Runtime object used in a desktop application.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInputObject</strong>](iinputobject.md)<br/></td>
<td>Exposes methods that change UI activation and process accelerators for a user input object contained in the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInputObject2</strong>](iinputobject2.md)<br/></td>
<td>Exposes a method that extends [<strong>IInputObject</strong>](iinputobject.md) by handling global accelerators.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInputObjectSite</strong>](iinputobjectsite.md)<br/></td>
<td>Exposes a method that is used to communicate focus changes for a user input object contained in the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IInputPanelConfiguration</strong>](iinputpanelconfiguration.md)<br/></td>
<td>Provides functionality for desktop apps to opt in to the focus tracking mechanism used in Windows Store apps.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IInputPanelInvocationConfiguration</strong>](iinputpanelinvocationconfiguration.md)<br/></td>
<td>Enables Windows Store apps to opt out of the automatic invocation behavior.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IIOCancelInformation</strong>](iiocancelinformation.md)<br/></td>
<td>Exposes methods for posting a cancel window message to the process thread from the Progress Dialog. <br/> This interface enables the progress dialog to post a thread message through [<strong>PostThreadMessage</strong>](winmsg.postthreadmessage) to the worker thread to cancel its operations. The worker thread must periodically check the message queue through [<strong>GetMessage</strong>](winmsg.getmessage), [<strong>PeekMessage</strong>](winmsg.peekmessage) or [<strong>MsgWaitForMultipleObjectsEx</strong>](base.msgwaitformultipleobjectsex).<br/> The [<strong>IIOCancelInformation::SetCancelInformation</strong>](iiocancelinformation-setcancelinformation.md) method tells the progress dialog which thread ID and what message to [<strong>PostThreadMessage</strong>](winmsg.postthreadmessage) when the user clicks <strong>Cancel</strong>. A thread ID of &quot;zero&quot; disables the sending operation for the cancel message.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IItemNameLimits</strong>](iitemnamelimits.md)<br/></td>
<td>Retrieves a list of valid and invalid characters or the maximum length of a name in the namespace. Use this interface for validation parsing and translation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IKnownFolder</strong>](iknownfolder.md)<br/></td>
<td>Exposes methods that allow an application to retrieve information about a known folder's category, type, GUID, PIDL value, redirection capabilities, and definition. It provides a method for the retrival of a known folder's [<strong>IShellItem</strong>](ishellitem.md) object. It also provides methods to get or set the path of the known folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IKnownFolderManager</strong>](iknownfoldermanager.md)<br/></td>
<td>Exposes methods that create, enumerate or manage existing known folders.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILaunchSourceAppUserModelId</strong>](ilaunchsourceappusermodelid.md)<br/></td>
<td>Provides a method for retrieving an [AppUserModelId](appids.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILaunchSourceViewSizePreference</strong>](ilaunchsourceviewsizepreference.md)<br/></td>
<td>Provides methods for retrieving information about the source application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILaunchTargetMonitor</strong>](ilaunchtargetmonitor.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>ILaunchTargetViewSizePreference</strong>](ilaunchtargetviewsizepreference.md)<br/></td>
<td>Provides a method for retrieving the preferred view size for a new application window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMarkupCallback</strong>](imarkupcallback.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IMenuPopup</strong>](imenupopup.md)<br/></td>
<td>[<strong>IMenuPopup</strong>](imenupopup.md) may be altered or unavailable.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IModalWindow</strong>](imodalwindow.md)<br/></td>
<td>Exposes a method that represents a modal window. This interface is used in the Windows XP Passport Wizard.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMultiMonitorDockingSite</strong>](imultimonitordockingsite.md)<br/></td>
<td>Implemented by the browser. Exposes methods that manage which monitor contains the Windows taskbar on a multiple monitor system. <br/></td>
</tr>
<tr class="even">
<td>[<strong>INamedPropertyBag</strong>](inamedpropertybag.md)<br/></td>
<td>Exposes methods that provide an object with a specified property bag in which the object can save its properties.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INamedPropertyStore</strong>](inamedpropertystore.md)<br/></td>
<td>Exposes methods that get and set named properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeAccessible</strong>](inamespacetreeaccessible.md)<br/></td>
<td>Exposes methods that perform accessibility actions on a Shell item from a namespace tree control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INameSpaceTreeControl</strong>](inamespacetreecontrol.md)<br/></td>
<td>Exposes methods used to view and manipulate nodes in a tree of Shell items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeControl2</strong>](inamespacetreecontrol2.md)<br/></td>
<td>Extends the [<strong>INameSpaceTreeControl</strong>](inamespacetreecontrol.md) interface by providing methods that get and set the display styles of treeview controls for use with Shell namespace items.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INameSpaceTreeControlCustomDraw</strong>](inamespacetreecontrolcustomdraw.md)<br/></td>
<td>Exposes methods that enable the user to draw a custom namespace tree control and its items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeControlDropHandler</strong>](inamespacetreecontroldrophandler.md)<br/></td>
<td>Exposes handler methods for drag-and-drop. Used by the namespace tree control to notify the client of any drag-and-drop operation happening within the control. Provides a way for a client to intercept a drop operation and perform its own action, or to return the desired drop effect.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INameSpaceTreeControlEvents</strong>](inamespacetreecontrolevents.md)<br/></td>
<td>Exposes methods for handling [<strong>INameSpaceTreeControl</strong>](inamespacetreecontrol.md) events.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INameSpaceTreeControlFolderCapabilities</strong>](inamespacetreecontrolfoldercapabilities.md)<br/></td>
<td>Exposes a single method that retrieves the status of a folder's [System.IsPinnedToNameSpaceTree](properties.props_System_IsPinnedToNameSpaceTree) filtering support.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INamespaceWalk</strong>](inamespacewalk.md)<br/></td>
<td>Exposes methods that walk a namespace from a given root node. The depth of the walk is specified and an optional array is returned containing the IDs of all nodes walked.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INamespaceWalkCB</strong>](inamespacewalkcb.md)<br/></td>
<td>A callback interface exposing methods used with [<strong>INamespaceWalk</strong>](inamespacewalk.md). After performing a walk with <strong>INamespaceWalk</strong>, an [<strong>IShellFolder</strong>](ishellfolder.md) object representing the walked nodes is passed to the [<strong>INamespaceWalkCB</strong>](inamespacewalkcb.md) methods. What those methods do with the information depends on the object that is implementing them.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INamespaceWalkCB2</strong>](inamespacewalkcb2.md)<br/></td>
<td>Extends [<strong>INamespaceWalkCB</strong>](inamespacewalkcb.md) with a method that is required in order to complete a namespace walk. This method removes data collected during the walk. <br/></td>
</tr>
<tr class="even">
<td>[<strong>INewMenuClient</strong>](inewmenuclient.md)<br/></td>
<td>Exposes methods that allow manipulation of items in a Windows 7 menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INewShortcutHook</strong>](inewshortcuthook.md)<br/></td>
<td>Exposes methods to create a new Internet shortcut.<br/></td>
</tr>
<tr class="even">
<td>[<strong>INewWindowManager</strong>](inewwindowmanager.md)<br/></td>
<td>Exposes a method that determines whether a window that is launched by another window should be displayed or blocked, allowing control of pop-up windows.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INotifyReplica</strong>](inotifyreplica.md)<br/></td>
<td>Exposes a method that provides an object's creator with the means to notify the object that it may be subject to subsequent reconciliation. The briefcase reconciler is responsible for implementing this interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectArray</strong>](iobjectarray.md)<br/></td>
<td>Exposes methods that enable clients to access items in a collection of objects that support [<strong>IUnknown</strong>](com.iunknown).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectCollection</strong>](iobjectcollection.md)<br/></td>
<td>Extends the [<strong>IObjectArray</strong>](iobjectarray.md) interface by providing methods that enable clients to add and remove objects that support [<strong>IUnknown</strong>](com.iunknown) in a collection.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectProvider</strong>](iobjectprovider.md)<br/></td>
<td>Exposes a method to discover objects that are named with a <strong>GUID</strong> from another object. Unlike [<strong>QueryService</strong>](_inet_IServiceProvider_QueryService_Method) this interface will not delegate its functionality on to other objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithAppUserModelID</strong>](iobjectwithappusermodelid.md)<br/></td>
<td>Exposes methods that allow implementers of a custom [<strong>IAssocHandler</strong>](iassochandler.md) object to provide access to its explicit Application User Model ID (AppUserModelID). This information is used to determine whether a particular file type can be added to an application's Jump List.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectWithBackReferences</strong>](iobjectwithbackreferences.md)<br/></td>
<td>Provides a method for interacting with back references held by an object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithCancelEvent</strong>](iobjectwithcancelevent.md)<br/></td>
<td>Supplies a caller with an event that will be signaled by the called object to denote cancellation of a task.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectWithFolderEnumMode</strong>](iobjectwithfolderenummode.md)<br/></td>
<td>Exposes methods that get and set enumeration modes of a parsed item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithProgID</strong>](iobjectwithprogid.md)<br/></td>
<td>Exposes methods that provide access to the ProgID associated with an object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjectWithPropertyKey</strong>](iobjectwithpropertykey.md)<br/></td>
<td>Exposes methods for getting and setting the property key.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IObjectWithSelection</strong>](iobjectwithselection.md)<br/></td>
<td>Exposes methods that get or set selected items represented by a Shell item array.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IObjMgr</strong>](iobjmgr.md)<br/></td>
<td>Exposes methods that allow a client to append or remove an object from a collection of objects managed by a server object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOpenControlPanel</strong>](iopencontrolpanel.md)<br/></td>
<td>Exposes methods that retrieve the view state of the Control Panel, the path of individual Control Panel items, and that open either the Control Panel itself or an individual Control Panel item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOpenSearchSource</strong>](iopensearchsource.md)<br/></td>
<td>Exposes a method to get search results from a custom client-side OpenSearch data source.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOperationsProgressDialog</strong>](ioperationsprogressdialog.md)<br/></td>
<td>Exposes methods to get, set, and query a progress dialog.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPackageDebugSettings</strong>](ipackagedebugsettings.md)<br/></td>
<td>Enables debugger developers to control the life cycle of a Windows Store app, such as suspending or resuming.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPackageExecutionStateChangeNotification</strong>](ipackageexecutionstatechangenotification.md)<br/></td>
<td>Enables receiving package state-change notifications during Windows Store app debugging.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IParentAndItem</strong>](iparentanditem.md)<br/></td>
<td>Exposes methods that get and set the parent and the parent's child ID. While [<strong>IParentAndItem</strong>](iparentanditem.md) is typically implemented on IShellItems, it is not specific to [<strong>IShellItem</strong>](ishellitem.md). <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IParseAndCreateItem</strong>](iparseandcreateitem.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IPersistFolder</strong>](ipersistfolder.md)<br/></td>
<td>Exposes a method that initializes Shell folder objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPersistFolder2</strong>](ipersistfolder2.md)<br/></td>
<td>Exposes methods that obtain information from Shell folder objects.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPersistFolder3</strong>](ipersistfolder3.md)<br/></td>
<td>Extends the [<strong>IPersistFolder</strong>](ipersistfolder.md) and [<strong>IPersistFolder2</strong>](ipersistfolder2.md) interfaces by allowing a folder object to implement nondefault handling of folder shortcuts.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPersistIDList</strong>](ipersistidlist.md)<br/></td>
<td>Exposes methods that are used to persist item identifier lists.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPersistSerializedPropStorage</strong>](ipersistserializedpropstorage.md)<br/></td>
<td>Exposes methods to persist serialized property storage data for later use and to restore persisted data to a new property store instance.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPersistSerializedPropStorage2</strong>](ipersistserializedpropstorage2.md)<br/></td>
<td>Exposes methods to persist serialized property storage data for later use and to restore persisted data to a new property store instance.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPlaybackManager</strong>](iplaybackmanager.md)<br/></td>
<td>Provides methods that allow media applications to communicate with the Windows playback manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPlaybackManagerEvents</strong>](iplaybackmanagerevents.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IPreviewHandler</strong>](ipreviewhandler.md)<br/></td>
<td>Exposes methods for the display of rich previews.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPreviewHandlerFrame</strong>](ipreviewhandlerframe.md)<br/></td>
<td>Enables preview handlers to pass keyboard shortcuts to the host. This interface retrieves a list of keyboard shortcuts and directs the host to handle a keyboard shortcut.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPreviewHandlerVisuals</strong>](ipreviewhandlervisuals.md)<br/></td>
<td>Exposes methods for applying color and font information to preview handlers.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPreviewItem</strong>](ipreviewitem.md)<br/></td>
<td>Identifies an item that will be shown in the preview pane.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IPreviousVersionsInfo</strong>](ipreviousversionsinfo.md)<br/></td>
<td>Exposes a method that checks for previous versions of server files or folders, stored for the purpose of reversion by the <em>shadow copies</em> technology provided with Windows Server 2003.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPrivateIdentityManager</strong>](iprivateidentitymanager.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IPrivateIdentityManager2</strong>](iprivateidentitymanager2.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>IProfferService</strong>](iprofferservice.md)<br/></td>
<td>Exposes a general mechanism for objects to offer services to other objects on the same host.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IProgressDialog</strong>](iprogressdialog.md)<br/></td>
<td>Exposes methods that provide options for an application to display a progress dialog box. This interface is exported by the progress dialog box object (CLSID_ProgressDialog). This object is a generic way to show a user how an operation is progressing. It is typically used when deleting, uploading, copying, moving, or downloading large numbers of files.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPublishedApp</strong>](ipublishedapp.md)<br/></td>
<td>Exposes methods that represent applications to Add/Remove Programs in Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IPublishedApp2</strong>](ipublishedapp2.md)<br/></td>
<td>Extends the [<strong>IPublishedApp</strong>](ipublishedapp.md) interface by providing an additional installation method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IPublishingWizard</strong>](ipublishingwizard.md)<br/></td>
<td>Exposes methods for working with the Online Print Wizard, the Web Publishing Wizard, and the Add Network Place Wizard. In Windows Vista, [<strong>IPublishingWizard</strong>](ipublishingwizard.md) no longer supports the Web Publishing Wizard or Online Print Wizard.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IQueryAssociations</strong>](iqueryassociations.md)<br/></td>
<td>Exposes methods that simplify the process of retrieving information stored in the registry in association with defining a file type or protocol and associating it with an application.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IQueryCancelAutoPlay</strong>](iquerycancelautoplay.md)<br/></td>
<td>Exposes a method that programmatically overrides [AutoPlay](autorun2k-intro.md) or [AutoRun](autoplay.md). This allows you to customize the location and type of content that is launched when media is inserted.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IQueryCodePage</strong>](iquerycodepage.md)<br/></td>
<td>Gets and sets the numeric value (Code Page identifier) of the ANSI code page.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IQueryContinue</strong>](iquerycontinue.md)<br/></td>
<td>Exposes a method that provides a simple, standard mechanism for objects to query a client for permission to continue an operation. Clients of [<strong>IUserNotification</strong>](iusernotification.md), for example, must pass an implementation of [<strong>IQueryContinue</strong>](iquerycontinue.md) to the [<strong>IUserNotification::Show</strong>](iusernotification-show.md) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IQueryContinueWithStatus</strong>](iquerycontinuewithstatus.md)<br/></td>
<td>Exposes methods that provide a standard mechanism for credential providers to call [<strong>QueryContinue</strong>](iquerycontinue-querycontinue.md) while attempting to connect to the network to determine if they should continue these attempts. Credential providers can also use this interface to display messages to the user while attempting to establish a network connection.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IQueryInfo</strong>](iqueryinfo.md)<br/></td>
<td>Exposes methods that the Shell uses to retrieve flags and info tip information for an item that resides in an [<strong>IShellFolder</strong>](ishellfolder.md) implementation. Info tips are usually displayed inside a [tooltip](_win32_Tooltip_Controls) control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IRelatedItem</strong>](irelateditem.md)<br/></td>
<td>Exposes methods that derive related items with specific relationships.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IRemoteComputer</strong>](iremotecomputer.md)<br/></td>
<td>Exposes a method that enumerates or initializes a namespace extension when it is invoked on a remote object. This interface is used, for example, to initialize the remote printers virtual folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IResolveShellLink</strong>](iresolveshelllink.md)<br/></td>
<td>Exposes a method that enables an application to request that a Shell folder object resolve a link for one of its items.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IResultsFolder</strong>](iresultsfolder.md)<br/></td>
<td>Exposes methods that hold items from a data object.<br/> An [<strong>IResultsFolder</strong>](iresultsfolder.md) is a folder that can hold items from all over the namespace and represent them to the user in a single folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IRunnableTask</strong>](irunnabletask.md)<br/></td>
<td>A free-threaded interface that can be exposed by an object to allow operations to be performed on a background thread. For example, if the [<strong>IExtractImage::GetLocation</strong>](iextractimage-getlocation.md) method returns E_PENDING, the calling application is permitted to extract the image on a background thread.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISearchBoxInfo</strong>](isearchboxinfo.md)<br/></td>
<td>Exposes methods that allow the caller to retrieve information entered into a search box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISearchContext</strong>](isearchcontext.md)<br/></td>
<td>Exposes methods that channel customization information to the search hooks.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISearchFolderItemFactory</strong>](isearchfolderitemfactory.md)<br/></td>
<td>Exposes methods that create and modify search folders. The Set methods are called first to set up the parameters of the search. When not called, default values will be used instead. [<strong>ISearchFolderItemFactory::GetIDList</strong>](isearchfolderitemfactory-getidlist.md) and [<strong>ISearchFolderItemFactory::GetShellItem</strong>](isearchfolderitemfactory-getshellitem.md) return the two forms of the search specified by these parameters. <br/></td>
</tr>
<tr class="even">
<td>[<strong>ISharedBitmap</strong>](isharedbitmap.md)<br/></td>
<td>Exposes memory-efficient methods for accessing bitmaps. This interface is used as a thin wrapper around HBITMAP objects, allowing those objects to be reference counted and protected from having their underlying data changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISharingConfigurationManager</strong>](isharingconfigurationmanager.md)<br/></td>
<td>Exposes methods that set and retrieve information about a computer's default sharing settings for the <strong>Users</strong> (<code>C:\Users</code>) or <strong>Public</strong> (<code>C:\Users\Public</code>) folder. Also exposes a set of methods that allow control of printer sharing.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellApp</strong>](ishellapp.md)<br/></td>
<td>Exposes methods that provide general information about an application to the Add/Remove Programs Application. You cannot use it outside the Add/Remove Programs application. The information given by this interface includes a list of supported management actions and whether the application is currently installed. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellBrowser</strong>](ishellbrowser.md)<br/></td>
<td>Implemented by hosts of Shell views (objects that implement [<strong>IShellView</strong>](ishellview.md)). Exposes methods that provide services for the view it is hosting and other objects that run in the context of the Explorer window. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellChangeNotify</strong>](ishellchangenotify.md)<br/></td>
<td>Exposes a method that notifies a Shell namespace extension when the ID of an item has changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellDetails</strong>](ishelldetails.md)<br/></td>
<td>Exposed by Shell folders to provide detailed information about the items in a folder. This is the same information that is displayed by the Windows Explorer when the view of the folder is set to Details. For Windows 2000 and later systems, [<strong>IShellDetails</strong>](ishelldetails.md) is superseded by [<strong>IShellFolder2</strong>](ishellfolder2.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellExtInit</strong>](ishellextinit.md)<br/></td>
<td>Exposes a method that initializes Shell extensions for property sheets, shortcut menus, and drag-and-drop handlers (extensions that add items to shortcut menus during nondefault drag-and-drop operations).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolder</strong>](ishellfolder.md)<br/></td>
<td>Exposed by all Shell namespace folder objects, its methods are used to manage folders.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolder2</strong>](ishellfolder2.md)<br/></td>
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
<td>[<strong>IShellFolderViewCB</strong>](ishellfolderviewcb.md)<br/></td>
<td>Exposes a method that allows communication between Windows Explorer and a folder view implemented using the system folder view object (the [<strong>IShellView</strong>](ishellview.md) object returned through [<strong>SHCreateShellFolderView</strong>](shcreateshellfolderview.md)) so that the folder view can be notified of events and modify its view accordingly.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolderViewDual</strong>](ishellfolderviewdual.md)<br/></td>
<td>Exposes methods that modify the view and select items in the current folder. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolderViewDual2</strong>](ishellfolderviewdual2.md)<br/></td>
<td>Exposes methods that modify the view and select items in the current folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellFolderViewDual3</strong>](ishellfolderviewdual3.md)<br/></td>
<td>Exposes methods that modify the current folder view.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellFolderViewType</strong>](ishellfolderviewtype.md)<br/></td>
<td>Exposes methods that enable a Shell folder to support different views on its content (different hierarchical layouts of its data).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellIcon</strong>](ishellicon.md)<br/></td>
<td>Exposes a method that obtains an icon index for an [<strong>IShellFolder</strong>](ishellfolder.md) object. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellIconOverlay</strong>](ishelliconoverlay.md)<br/></td>
<td>Exposes methods that are used by a namespace extension to specify icon overlays for the objects it contains.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellIconOverlayIdentifier</strong>](ishelliconoverlayidentifier.md)<br/></td>
<td>Exposes methods that handle all communication between icon overlay handlers and the Shell.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellImageDataAbort</strong>](ishellimagedataabort.md)<br/></td>
<td>Exposes a single method used to abort [<strong>IShellImageData</strong>](ishellimagedata.md) processes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellImageDataFactory</strong>](ishellimagedatafactory.md)<br/></td>
<td>Exposes methods that create [<strong>IShellImageData</strong>](ishellimagedata.md) instances based on various image sources.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellItem</strong>](ishellitem.md)<br/></td>
<td>Exposes methods that retrieve information about a Shell item. [<strong>IShellItem</strong>](ishellitem.md) and [<strong>IShellItem2</strong>](ishellitem2.md) are the preferred representations of items in any new code.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellItem2</strong>](ishellitem2.md)<br/></td>
<td>Extends [<strong>IShellItem</strong>](ishellitem.md) with methods that retrieve various property values of the item. <strong>IShellItem</strong> and [<strong>IShellItem2</strong>](ishellitem2.md) are the preferred representations of items in any new code.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellItemArray</strong>](ishellitemarray.md)<br/></td>
<td>Exposes methods that create and manipulate [<strong>Shell item</strong>](ishellitem.md) arrays.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellItemFilter</strong>](ishellitemfilter.md)<br/></td>
<td>Exposed by a client to specify how to filter the enumeration of a [<strong>Shell item</strong>](ishellitem.md) by a server application.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellItemImageFactory</strong>](ishellitemimagefactory.md)<br/></td>
<td>Exposes a method to return either icons or thumbnails for Shell items. If no thumbnail or icon is available for the requested item, a per-class icon may be provided from the Shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellItemResources</strong>](ishellitemresources.md)<br/></td>
<td>Exposes methods to manipulate and query Shell item resources.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellLibrary</strong>](ishelllibrary.md)<br/></td>
<td>Exposes methods for creating and managing libraries.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellLink</strong>](ishelllink.md)<br/></td>
<td>Exposes methods that create, modify, and resolve Shell links.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellLinkDataList</strong>](ishelllinkdatalist.md)<br/></td>
<td>Exposes methods that allow an application to attach extra data blocks to a [Shell link](shell.Links). These methods add, copy, or remove data blocks.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellMenu</strong>](ishellmenu.md)<br/></td>
<td>Exposes methods that interact with Shell menus such as the <strong>Start</strong> menu, and the <strong>Favorites</strong> menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellMenuCallback</strong>](ishellmenucallback.md)<br/></td>
<td>A callback interface that exposes a method that receives messages from a menu band.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellPropSheetExt</strong>](ishellpropsheetext.md)<br/></td>
<td>Exposes methods that allow a property sheet handler to add or replace pages in the property sheet displayed for a file object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellRunDll</strong>](ishellrundll.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IShellView</strong>](ishellview.md)<br/></td>
<td>Exposes methods that present a view in the Windows Explorer or folder windows.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellView2</strong>](ishellview2.md)<br/></td>
<td>Extends the capabilities of [<strong>IShellView</strong>](ishellview.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IShellView3</strong>](ishellview3.md)<br/></td>
<td>Extends the capabilities of [<strong>IShellView2</strong>](ishellview2.md) by providing a method to replace [<strong>IShellView2::CreateViewWindow2</strong>](ishellview2-createviewwindow2.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IShellWindows</strong>](ishellwindows.md)<br/></td>
<td>Provides access to the collection of open Shell windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IStartMenuPinnedList</strong>](istartmenupinnedlist.md)<br/></td>
<td>Exposes a method that unpins an application shortcut from the <strong>Start</strong> menu or the taskbar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IStorageProviderHandler</strong>](istorageproviderhandler.md)<br/></td>
<td>Retrieves the [<strong>IStorageProviderPropertyHandler</strong>](istorageproviderpropertyhandler.md) associated with a specific file or folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IStorageProviderPropertyHandler</strong>](istorageproviderpropertyhandler.md)<br/></td>
<td>Provides a collection of properties associated with a file or folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IStreamAsync</strong>](istreamasync.md)<br/></td>
<td>Exposes methods to manage input/outpout (I/O) to an asynchronous stream. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IStreamUnbufferedInfo</strong>](istreamunbufferedinfo.md)<br/></td>
<td>Exposes a method that determines the sector size as an aid to byte alignment.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISuspensionDependencyManager</strong>](isuspensiondependencymanager.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflict</strong>](isyncmgrconflict.md)<br/></td>
<td>Exposes methods that provide information about a conflict retrieved from a conflict store, and allows the conflict to be resolved.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrConflictFolder</strong>](isyncmgrconflictfolder.md)<br/></td>
<td>Exposes a method that gets the conflict ID list for a conflict object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflictItems</strong>](isyncmgrconflictitems.md)<br/></td>
<td>Exposes methods that get conflict item data and item count.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrConflictPresenter</strong>](isyncmgrconflictpresenter.md)<br/></td>
<td>Exposes a method that presents a conflict to the user.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflictResolutionItems</strong>](isyncmgrconflictresolutionitems.md)<br/></td>
<td>Exposes methods that get item info and item count.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrConflictResolveInfo</strong>](isyncmgrconflictresolveinfo.md)<br/></td>
<td>Exposes methods that get and set information about sync manager conflict resolution.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrConflictStore</strong>](isyncmgrconflictstore.md)<br/></td>
<td>Exposes methods that allow a handler to provide conflicts that appear in the Conflicts folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrControl</strong>](isyncmgrcontrol.md)<br/></td>
<td>Exposes methods that allow an application or handler to start or stop a synchronization, notify Sync Center of changes to the set of handlers or items, or notify of changes to property values.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrEnumItems</strong>](syncmgr-isyncmgrenumitems.md)<br/></td>
<td>Exposes methods that enumerate through an array of [<strong>SYNCMGRITEM</strong>](syncmgr-syncmgritem.md) structures. Each of these structures provides information about an item that can be synchronized. [<strong>ISyncMgrEnumItems</strong>](syncmgr-isyncmgrenumitems.md) has the same methods as all standard enumerator interfaces: Next, Skip, Reset, and Clone.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrEvent</strong>](isyncmgrevent.md)<br/></td>
<td>Exposes methods that retrieve data from an event store. An event store allows Sync Center to get an enumerator of all events in the store, as well as to retrieve individual events.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrEventLinkUIOperation</strong>](isyncmgreventlinkuioperation.md)<br/></td>
<td>Provides a method that is called when event links are clicked in the sync results folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrEventStore</strong>](isyncmgreventstore.md)<br/></td>
<td>Exposes methods that allow a handler to provide its own event store and manage its own sync events, instead of using the default Sync Center event store. These events are displayed in the Sync Results folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrHandler</strong>](isyncmgrhandler.md)<br/></td>
<td>Exposes methods that make up the primary interface implemented by a sync handler. Sync Center creates one instance of the handler through this interface to get properties, enumerate sync items, and modify state. Sync Center creates a separate instance of the handler on a separate thread to perform a synchronization or a UI operation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrHandlerCollection</strong>](isyncmgrhandlercollection.md)<br/></td>
<td>Exposes methods that provide an enumerator of sync handler IDs and instantiate those sync handlers.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrHandlerInfo</strong>](isyncmgrhandlerinfo.md)<br/></td>
<td>Exposes methods that allow a handler to provide property and state information to Sync Center.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrRegister</strong>](syncmgr-isyncmgrregister.md)<br/></td>
<td>Exposes methods so that an application can register with the synchronization manager. This can be achieved either through the [<strong>ISyncMgrRegister</strong>](syncmgr-isyncmgrregister.md) interface or by registering directly in the registry.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrResolutionHandler</strong>](isyncmgrresolutionhandler.md)<br/></td>
<td>Exposes methods that manage synchronizing conflicts. Implement this interface to construct a sync conflict handler. The conflict resolution user interface (UI) will call this interface to resolve the conflict presented to the user. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrScheduleWizardUIOperation</strong>](isyncmgrschedulewizarduioperation.md)<br/></td>
<td>Exposes a method that allows a handler to display the sync schedule wizard for the handler.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSessionCreator</strong>](isyncmgrsessioncreator.md)<br/></td>
<td>Exposes a single method through which a handler or external application can notify Sync Center that synchronization has begun, as well as report progress and events.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSyncCallback</strong>](isyncmgrsynccallback.md)<br/></td>
<td>Exposes methods that allow a synchronization process to report progress and events to Sync Center, or to query whether the process has been canceled.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSynchronize</strong>](syncmgr-isyncmgrsynchronize.md)<br/></td>
<td>Exposes methods that enable the registered application or service to receive notifications from the synchronization manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSynchronizeCallback</strong>](syncmgr-isyncmgrsynchronizecallback.md)<br/></td>
<td>Exposes methods that manage the synchronization process.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSynchronizeInvoke</strong>](syncmgr-isyncmgrsynchronizeinvoke.md)<br/></td>
<td>Exposes methods that enable a registered application to invoke the synchronization manager to update items.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSyncItem</strong>](isyncmgrsyncitem.md)<br/></td>
<td>Exposes methods that act on and retrieve information from a single sync item, allowing handlers to manage sync items as independent objects.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSyncItemContainer</strong>](isyncmgrsyncitemcontainer.md)<br/></td>
<td>Exposes methods that provide information to handlers about the items they contain.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrSyncItemInfo</strong>](isyncmgrsynciteminfo.md)<br/></td>
<td>Exposes methods that provide property and state information for a single sync item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ISyncMgrSyncResult</strong>](isyncmgrsyncresult.md)<br/></td>
<td>Exposes a method that applications calling [<strong>ISyncMgrControl</strong>](isyncmgrcontrol.md) can use to get the result of a [<strong>ISyncMgrControl::StartHandlerSync</strong>](isyncmgrcontrol-starthandlersync.md) or [<strong>ISyncMgrControl::StartItemSync</strong>](isyncmgrcontrol-startitemsync.md) call.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ISyncMgrUIOperation</strong>](isyncmgruioperation.md)<br/></td>
<td>Exposes a method through which a sync handler or sync item can display a UI object when requested to do so by Sync Center.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITaskbarList</strong>](itaskbarlist.md)<br/></td>
<td>Exposes methods that control the taskbar. It allows you to dynamically add, remove, and activate items on the taskbar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITaskbarList2</strong>](itaskbarlist2.md)<br/></td>
<td>Extends the [<strong>ITaskbarList</strong>](itaskbarlist.md) interface by exposing a method to mark a window as a full-screen display.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITaskbarList3</strong>](itaskbarlist3.md)<br/></td>
<td>Extends [<strong>ITaskbarList2</strong>](itaskbarlist2.md) by exposing methods that support the unified launching and switching taskbar button functionality added in Windows 7. This functionality includes thumbnail representations and switch targets based on individual tabs in a tabbed application, thumbnail toolbars, notification and status overlays, and progress indicators.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITaskbarList4</strong>](itaskbarlist4.md)<br/></td>
<td>Extends [<strong>ITaskbarList3</strong>](itaskbarlist3.md) by providing a method that allows the caller to control two property values for the tab thumbnail and peek feature.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IThumbnailCache</strong>](ithumbnailcache.md)<br/></td>
<td>Exposes methods for a system thumbnail cache that is shared across applications.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IThumbnailCachePrimer</strong>](ithumbnailcacheprimer.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>IThumbnailHandlerFactory</strong>](ithumbnailhandlerfactory.md)<br/></td>
<td>Exposes a method for retrieving the thumbnail handler of an item. Implement this interface if you want to specify what extractor is used for a child IDList.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IThumbnailProvider</strong>](ithumbnailprovider.md)<br/></td>
<td>Exposes a method for getting a thumbnail image and is intended to be implemented for thumbnail handlers. The object that implements this interface must also implement [<strong>IInitializeWithStream</strong>](iinitializewithstream.md). <br/></td>
</tr>
<tr class="even">
<td>[<strong>IThumbnailSettings</strong>](ithumbnailsettings.md)<br/></td>
<td>Provides a method that enables a thumbnail provider to determine the user context of a thumbnail request.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IThumbnailStreamCache</strong>](ithumbnailstreamcache.md)<br/></td>
<td>Gets or sets the thumbnail stream. This interface is for internal use only and can only be called by the photos application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITrackShellMenu</strong>](itrackshellmenu.md)<br/></td>
<td>Exposes methods that extend the [<strong>IShellMenu</strong>](ishellmenu.md) interface by providing the ability to coordinate toolbar buttons with a menu as well as display a pop-up menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITranscodeImage</strong>](itranscodeimage.md)<br/></td>
<td>Exposes a method that allows conversion to JPEG or bitmap (BMP) image formats from any image type supported by Windows. <br/></td>
</tr>
<tr class="even">
<td>[<strong>ITransferAdviseSink</strong>](itransferadvisesink.md)<br/></td>
<td>Exposes methods supporting status collection and failure information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITransferDestination</strong>](itransferdestination.md)<br/></td>
<td>Exposes methods that create a destination Shell item for a copy or move operation. This interface is provided to allow more control over file operations by providing an [<strong>ITransferDestination::Advise</strong>](itransferdestination-advise.md) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITransferMediumItem</strong>](itransfermediumitem.md)<br/></td>
<td>Used by a copy engine to get the item on which to call [<strong>QueryInterface</strong>](com.iunknown_queryinterface) to return a pointer to interface [<strong>ITransferDestination</strong>](itransferdestination.md) or interface [<strong>ITransferSource</strong>](itransfersource.md). These interfaces can be queried and enumerated for copy, move, or delete operations.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITransferSource</strong>](itransfersource.md)<br/></td>
<td>Exposes methods to manipulate [<strong>IShellItem</strong>](ishellitem.md), including copy, move, recycle, and others. This interface is offered to provide more control over file operations by providing an [<strong>ITransferSource::Advise</strong>](itransfersource-advise.md) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITrayDeskBand</strong>](itraydeskband.md)<br/></td>
<td>Exposes methods that show, hide, and query deskbands.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IUpdateIDList</strong>](iupdateidlist.md)<br/></td>
<td>Provides a method to update the [<strong>ITEMIDLIST</strong>](itemidlist.md) of the child of an folder object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IURLSearchHook</strong>](iurlsearchhook.md)<br/></td>
<td>Exposes a method that is used by the browser to translate the address of an unknown URL protocol.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IURLSearchHook2</strong>](iurlsearchhook2.md)<br/></td>
<td>Exposes a method that is used by the browser to translate the address of an unknown URL protocol by using a search context object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IUserAccountChangeCallback</strong>](iuseraccountchangecallback.md)<br/></td>
<td>Exposes a method which is called when the picture that represents a user account is changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IUserNotification</strong>](iusernotification.md)<br/></td>
<td>Exposes methods that set notification information and then display that notification to the user in a balloon that appears in conjunction with the notification area of the taskbar. <br/>
<blockquote>
[!Note]<br />
[<strong>IUserNotification2</strong>](iusernotification2.md) differs from [<strong>IUserNotification</strong>](iusernotification.md) only in its [<strong>Show</strong>](iusernotification2-show.md) method, which adds an additional parameter for a callback interface to communicate with the notification. Otherwise the two interfaces are identical in form and function. CLSID_UserNotification implements both versions of <strong>Show</strong> as an overload.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>IUserNotification2</strong>](iusernotification2.md)<br/></td>
<td>Exposes methods that set notification information and then display that notification to the user in a balloon that appears in conjunction with the notification area of the taskbar. <br/>
<blockquote>
[!Note]<br />
[<strong>IUserNotification2</strong>](iusernotification2.md) does not inherit from [<strong>IUserNotification</strong>](iusernotification.md). <strong>IUserNotification2</strong> differs from <strong>IUserNotification</strong> only in its [<strong>Show</strong>](iusernotification2-show.md) method, which adds an additional parameter for a callback interface to communicate with the notification. Otherwise the two interfaces are identical in form and function. CLSID_UserNotification implements both versions of <strong>Show</strong> as an overload.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IUserNotificationCallback</strong>](iusernotificationcallback.md)<br/></td>
<td>Exposes a method for the handling of a mouse click or shortcut menu access in a notification balloon. Used with [<strong>IUserNotification2::Show</strong>](iusernotification2-show.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>IUseToBrowseItem</strong>](iusetobrowseitem.md)<br/></td>
<td>Finds the item that should be used when browsing to this item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IViewStateIdentityItem</strong>](iviewstateidentityitem.md)<br/></td>
<td>Provides a canonical persistence item, an item for which view customizations will be remembered.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IVirtualDesktopManager</strong>](ivirtualdesktopmanager.md)<br/></td>
<td>Exposes methods that enable an application to interact with groups of windows that form virtual workspaces.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IVisualProperties</strong>](ivisualproperties.md)<br/></td>
<td>Exposes methods that set and get visual properties.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IWebWizardExtension</strong>](iwebwizardextension.md)<br/></td>
<td>Extends the [<strong>IWizardExtension</strong>](iwizardextension.md) interface by exposing methods to set the wizard extension's initial URL, and a specific URL in case of an error.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IWizardExtension</strong>](iwizardextension.md)<br/></td>
<td>Used by wizards such as the Web Publishing Wizard and Online Print Ordering Wizard which host server-side content pages. This interface exposes methods to specify supported extension pages and to navigate into and out of those pages.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IWizardSite</strong>](iwizardsite.md)<br/></td>
<td>Exposes methods used by a wizard extension to navigate the borders between itself and the rest of the wizard.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TaskCompletionClient</strong>](taskcompletionclient.md)<br/></td>
<td>Enables task completion. <br/></td>
</tr>
</tbody>
</table>



 

 

 




