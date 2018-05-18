---
Description: 'This section describes the Windows Shell constants, enumerations, and flags.'
title: 'Shell Constants, Enumerations, and Flags'
---

# Shell Constants, Enumerations, and Flags

This section describes the Windows Shell constants, enumerations, and flags.

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
<td>[<strong>_SVGIO</strong>](svgio.md)<br/></td>
<td>Used with the [<strong>IFolderView::Items</strong>](ifolderview-items.md), [<strong>IFolderView::ItemCount</strong>](ifolderview-itemcount.md), and [<strong>IShellView::GetItemObject</strong>](ishellview-getitemobject.md) methods to restrict or control the items in their collections.<br/></td>
</tr>
<tr class="even">
<td>[<strong>_SVSIF</strong>](svsif.md)<br/></td>
<td>Indicates flags used by [<strong>IFolderView</strong>](ifolderview.md), [<strong>IFolderView2</strong>](ifolderview2.md), [<strong>IShellView</strong>](ishellview.md) and [<strong>IShellView2</strong>](ishellview2.md) to specify a type of selection to apply.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPACTIONFLAGS</strong>](appactionflags.md)<br/></td>
<td>Specifies application management actions supported by an application publisher. These flags are bitmasks passed to [<strong>IShellApp::GetPossibleActions</strong>](ishellapp-getpossibleactions.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>APPINFODATAFLAGS</strong>](appinfodataflags.md)<br/></td>
<td>Specifies application information to return from [<strong>IShellApp::GetAppInfo</strong>](ishellapp-getappinfo.md). These flags are bitmasks used in the [<strong>dwMask</strong>](appinfodata.md) member of the <strong>APPINFODATA</strong> structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPLICATION_VIEW_ORIENTATION</strong>](application-view-orientation.md)<br/></td>
<td>Defines the set of display orientation modes for a window (app view). Used by [<strong>IApplicationDesignModeSettings2::GetApplicationViewOrientation</strong>](iapplicationdesignmodesettings2-getapplicationvieworientation.md) and [<strong>IApplicationDesignModeSettings2::SetApplicationViewOrientation</strong>](iapplicationdesignmodesettings2-setapplicationvieworientation.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>APPLICATION_VIEW_SIZE_PREFERENCE</strong>](application-view-size-preference.md)<br/></td>
<td>Defines the set of possible general window (app view) size preferences. Used by [<strong>ILaunchSourceViewSizePreference::GetSourceViewSizePreference</strong>](ilaunchsourceviewsizepreference-getsourceviewsizepreference.md) and [<strong>ILaunchTargetViewSizePreference::GetTargetViewSizePreference</strong>](ilaunchtargetviewsizepreference-gettargetviewsizepreference.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPLICATION_VIEW_STATE</strong>](application-view-state.md)<br/></td>
<td>Indicates the current view state of a Windows Store app. Used by [<strong>IApplicationDesignModeSettings::SetApplicationViewState</strong>](iapplicationdesignmodesettings-setapplicationviewstate.md) and [<strong>IApplicationDesignModeSettings::IsApplicationViewStateSupported</strong>](iapplicationdesignmodesettings-isapplicationviewstatesupported.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>ASSOCDATA</strong>](assocdata-str.md)<br/></td>
<td>Used by [<strong>IQueryAssociations::GetData</strong>](iqueryassociations-getdata.md) to define the type of data that is to be returned.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCF</strong>](assocf-str.md)<br/></td>
<td>Provides information to the [<strong>IQueryAssociations</strong>](iqueryassociations.md) interface methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ASSOCIATIONLEVEL</strong>](associationlevel.md)<br/></td>
<td>Specifies the source of the default association for a file name extension. Used by methods of the [<strong>IApplicationAssociationRegistration</strong>](iapplicationassociationregistration.md) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCIATIONTYPE</strong>](associationtype.md)<br/></td>
<td>Specifies the type of association for an application. Used by methods of the [<strong>IApplicationAssociationRegistration</strong>](iapplicationassociationregistration.md) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ASSOCKEY</strong>](assockey-str.md)<br/></td>
<td>Specifies the type of key to be returned by [<strong>IQueryAssociations::GetKey</strong>](iqueryassociations-getkey.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCSTR</strong>](assocstr-str.md)<br/></td>
<td>Used by [<strong>IQueryAssociations::GetString</strong>](iqueryassociations-getstring.md) to define the type of string that is to be returned.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ATTACHMENT_ACTION</strong>](attachment-action.md)<br/></td>
<td>Provides a set of flags to be used with [<strong>IAttachmentExecute::Prompt</strong>](iattachmentexecute-prompt.md) to indicate the action to be performed upon user confirmation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ATTACHMENT_PROMPT</strong>](attachment-prompt.md)<br/></td>
<td>Provides a set of flags to be used with [<strong>IAttachmentExecute::Prompt</strong>](iattachmentexecute-prompt.md) to indicate the type of prompt UI to display.<br/></td>
</tr>
<tr class="even">
<td>[<strong>AUTOCOMPLETELISTOPTIONS</strong>](autocompletelistoptions.md)<br/></td>
<td>Specifies which objects are enumerated for autocompletion lists.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>AUTOCOMPLETEOPTIONS</strong>](autocompleteoptions.md)<br/></td>
<td>Specifies values used by [<strong>IAutoComplete2::GetOptions</strong>](iautocomplete2-getoptions.md) and [<strong>IAutoComplete2::SetOptions</strong>](iautocomplete2-setoptions.md) for options surrounding autocomplete.<br/></td>
</tr>
<tr class="even">
<td>[<strong>Bind Context String Keys</strong>](str-constants.md)<br/></td>
<td>A set of string keys that are used with the [<strong>IBindCtx::RegisterObjectParam</strong>](com.ibindctx_registerobjectparam) method to specify a bind context.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BNSTATE</strong>](bnstate.md)<br/></td>
<td>Deprecated. Used by [<strong>IBrowserService::SetNavigateState</strong>](ibrowserservice-setnavigatestate.md) and [<strong>IBrowserService::GetNavigateState</strong>](ibrowserservice-getnavigatestate.md) to specify navigation states.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BROWSERFRAMEOPTIONS</strong>](browserframeoptions.md)<br/></td>
<td>Used with method [<strong>IBrowserFrameOptions::GetFrameOptions</strong>](ibrowserframeoptions-getframeoptions.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CATEGORYINFO_FLAGS</strong>](categoryinfo-flags.md)<br/></td>
<td>Provides a set of flags for use with the [<strong>CATEGORY_INFO</strong>](category-info.md) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CATSORT_FLAGS</strong>](catsort-flags.md)<br/></td>
<td>Specifies methods for sorting category data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CDCONTROLSTATE</strong>](cdcontrolstate.md)<br/></td>
<td>Specifies the values that indicate whether a control is visible and enabled. Used by members of the [<strong>IFileDialogCustomize</strong>](ifiledialogcustomize.md) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_ENUM_FLAGS</strong>](cm-enum-flags.md)<br/></td>
<td>Used by members of the [<strong>IColumnManager</strong>](icolumnmanager.md) interface to specify which set of columns are being requested, either all or only those currently visible.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_MASK</strong>](cm-mask.md)<br/></td>
<td>Indicates which values in the [<strong>CM_COLUMNINFO</strong>](cm-columninfo.md) structure should be set during calls to [<strong>IColumnManager::SetColumnInfo</strong>](icolumnmanager-setcolumninfo.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_SET_WIDTH_VALUE</strong>](cm-set-width-value.md)<br/></td>
<td>Specifies width values in pixels and includes special support for default and autosize. Used by members of the [<strong>IColumnManager</strong>](icolumnmanager.md) interface through the [<strong>CM_COLUMNINFO</strong>](cm-columninfo.md) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_STATE</strong>](cm-state.md)<br/></td>
<td>Specifies column state values. Used by members of the [<strong>IColumnManager</strong>](icolumnmanager.md) interface through the [<strong>CM_COLUMNINFO</strong>](cm-columninfo.md) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS</strong>](credential-provider-account-options.md)<br/></td>
<td>Indicates the type of credential that a credential provider should return to associate with the &quot;Other user&quot; tile. Used by [<strong>ICredentialProviderUserArray_GetAccountOptions</strong>](icredentialprovideruserarray-getaccountoptions.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS</strong>](credential-provider-credential-field-options.md)<br/></td>
<td>Provides customization options for a single field in a logon or credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE</strong>](credential-provider-field-interactive-state.md)<br/></td>
<td>Describes the state of a field and how it a user can interact with it. Fields can be displayed by a credential provider in a variety of different interactive states.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_STATE</strong>](credential-provider-field-state.md)<br/></td>
<td>Specifies the state of a single field in the Credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_TYPE</strong>](credential-provider-field-type.md)<br/></td>
<td>Specifies a type of credential field. Used by [<strong>CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR</strong>](credential-provider-field-descriptor.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE</strong>](credential-provider-get-serialization-response.md)<br/></td>
<td>Describes the response when a credential provider attempts to serialize credentials.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_STATUS_ICON</strong>](credential-provider-status-icon.md)<br/></td>
<td>Indicates which status icon should be displayed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_USAGE_SCENARIO</strong>](credential-provider-usage-scenario.md)<br/></td>
<td>Declares the scenarios in which a credential provider is supported. A credential provider usage scenario (CPUS) enables the credential provider to provide distinct enumeration behavior and UI field setup across scenarios.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CSIDL</strong>](csidl.md)<br/></td>
<td><blockquote>
<p>[!Note]As of Windows Vista, these values have been replaced by [<strong>KNOWNFOLDERID</strong>](knownfolderid.md) values. See that topic for a list of the new constants and their corresponding CSIDL values. For convenience, corresponding <strong>KNOWNFOLDERID</strong> values are also noted here for each CSIDL value.</p>
<p>The CSIDL system is supported under Windows Vista for compatibility reasons. However, new development should use [<strong>KNOWNFOLDERID</strong>](knownfolderid.md) values rather than CSIDL values.<br/></p>
</blockquote>
<br/> CSIDL (constant special item ID list) values provide a unique system-independent way to identify special folders used frequently by applications, but which may not have the same name or location on any given system. For example, the system folder may be &quot;C:\Windows&quot; on one system and &quot;C:\Winnt&quot; on another. These constants are defined in Shlobj.h.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CTF Flags</strong>](ctf.md)<br/></td>
<td>Flags that control the calling function's behavior. Used by [<strong>SHCreateThread</strong>](shcreatethread.md) and [<strong>SHCreateThreadWithHandle</strong>](shcreatethreadwithhandle.md). In those functions, these values are defined as being of type SHCT_FLAGS.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DATAOBJ_GET_ITEM_FLAGS</strong>](dataobj-get-item-flags.md)<br/></td>
<td>Values used by the [<strong>SHGetItemFromDataObject</strong>](shgetitemfromdataobject.md) function to specify options concerning the processing of the source object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DBID Command Flags</strong>](dbid-command-flags.md)<br/></td>
<td>These command IDs can be sent to the band object's container with [<strong>IOleCommandTarget::Exec</strong>](com.iolecommandtarget_exec).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEF_SHARE_ID</strong>](def-share-id.md)<br/></td>
<td>Values that specify the folder being acted on by methods of the [<strong>ISharingConfigurationManager</strong>](isharingconfigurationmanager.md) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DEFAULTSAVEFOLDERTYPE</strong>](defaultsavefoldertype.md)<br/></td>
<td>Specifies the default save location.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEFAULT_FOLDER_MENU_RESTRICTIONS</strong>](default-folder-menu-restrictions.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>DESKTOP_WALLPAPER_POSITION</strong>](desktop-wallpaper-position.md)<br/></td>
<td>Specifies how the desktop wallpaper should be displayed.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEVICE_SCALE_FACTOR</strong>](device-scale-factor.md)<br/></td>
<td>Indicates a spoofed device scale factor, as a percent. Used by [<strong>IApplicationDesignModeSettings::SetApplicationViewState</strong>](iapplicationdesignmodesettings-setapplicationviewstate.md) and [<strong>IApplicationDesignModeSettings::IsApplicationViewStateSupported</strong>](iapplicationdesignmodesettings-isapplicationviewstatesupported.md)<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DISPLAY_DEVICE_TYPE</strong>](display-device-type.md)<br/></td>
<td>Indicates whether the device is a primary or immersive type of display.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DROPIMAGETYPE</strong>](dropimagetype.md)<br/></td>
<td>Values used with the [<strong>DROPDESCRIPTION</strong>](dropdescription.md) structure to specify the drop image.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXPCMDSTATE</strong>](expcmdstate.md)<br/></td>
<td>[<strong>EXPCMDSTATE</strong>](expcmdstate.md) values represent the command state of a Shell item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXPLORER_BROWSER_FILL_FLAGS</strong>](explorer-browser-fill-flags.md)<br/></td>
<td>These flags are used with [<strong>IExplorerBrowser::FillFromObject</strong>](iexplorerbrowser-fillfromobject.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXPLORER_BROWSER_OPTIONS</strong>](explorer-browser-options.md)<br/></td>
<td>These flags are used with [<strong>IExplorerBrowser::GetOptions</strong>](iexplorerbrowser-getoptions.md) and [<strong>IExplorerBrowser::SetOptions</strong>](iexplorerbrowser-setoptions.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXPLORERPANESTATE</strong>](explorerpanestate.md)<br/></td>
<td>Indicate flags used by [<strong>IExplorerPaneVisibility::GetPaneState</strong>](iexplorerpanevisibility-getpanestate.md) to get the current state of the given Windows Explorer pane.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FDAP</strong>](fdap.md)<br/></td>
<td>Specifies list placement.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FDE_OVERWRITE_RESPONSE</strong>](fde-overwrite-response.md)<br/></td>
<td>Specifies the values used by the [<strong>IFileDialogEvents::OnOverwrite</strong>](ifiledialogevents-onoverwrite.md) method to indicate an application's response to an overwrite request during a save operation using the common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FDE_SHAREVIOLATION_RESPONSE</strong>](fde-shareviolation-response.md)<br/></td>
<td>Specifies the values used by the [<strong>IFileDialogEvents::OnShareViolation</strong>](ifiledialogevents-onshareviolation.md) method to indicate an application's response to a sharing violation that occurs when a file is opened or saved.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FFFP_MODE</strong>](fffp-mode.md)<br/></td>
<td>Describes match criteria. Used by methods of the [<strong>IKnownFolderManager</strong>](iknownfoldermanager.md) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FILE_USAGE_TYPE</strong>](file-usage-type.md)<br/></td>
<td>Constants used by [<strong>IFileIsInUse::GetUsage</strong>](ifileisinuse-getusage.md) to indicate how a file in use is being used.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FILEOPENDIALOGOPTIONS</strong>](fileopendialogoptions.md)<br/></td>
<td>Defines the set of options available to an Open or Save dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FILETYPEATTRIBUTEFLAGS</strong>](filetypeattributeflags.md)<br/></td>
<td>Indicates [<strong>FILETYPEATTRIBUTEFLAGS</strong>](filetypeattributeflags.md) constants that are used in the EditFlags value of a file association [PROGID](fa-progids.md) registry key.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDER_ENUM_MODE</strong>](folder-enum-mode.md)<br/></td>
<td>Used by [<strong>IObjectWithFolderEnumMode::GetMode</strong>](iobjectwithfolderenummode-getmode.md) and [<strong>IObjectWithFolderEnumMode::SetMode</strong>](iobjectwithfolderenummode-setmode.md) methods to get and set the display modes for the folders.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FOLDERFLAGS</strong>](folderflags.md)<br/></td>
<td>A set of flags that specify folder view options. The flags are independent of each other and can be used in any combination.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDERLOGICALVIEWMODE</strong>](folderlogicalviewmode.md)<br/></td>
<td>Used by [<strong>IFolderViewSettings::GetViewMode</strong>](ifolderviewsettings-getviewmode.md) and [<strong>ISearchFolderItemFactory::SetFolderLogicalViewMode</strong>](isearchfolderitemfactory-setfolderlogicalviewmode.md) to describe the view mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FOLDERTYPEID</strong>](foldertypeid.md)<br/></td>
<td>The [<strong>FOLDERTYPEID</strong>](foldertypeid.md) values represent a view template applied to a folder, usually based on its intended use and contents.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDERVIEWMODE</strong>](folderviewmode.md)<br/></td>
<td>Specifies the folder view type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FOLDERVIEWOPTIONS</strong>](folderviewoptions.md)<br/></td>
<td>Used by methods of the [<strong>IFolderViewOptions</strong>](ifolderviewoptions.md) interface to activate Windows Vista options not supported by default in Windows 7 and later systems as well as deactivating new Windows 7 options.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IActiveDesktop Flags</strong>](iactivedesktop-flags.md)<br/></td>
<td>This section describes the flags used by [<strong>IActiveDesktop</strong>](lwef.iactivedesktop_interface) interface methods.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IESHORTCUTFLAGS</strong>](ieshortcutflags.md)<br/></td>
<td>Specifies how a shortcut should be handled by the browser.<br/></td>
</tr>
<tr class="even">
<td>[<strong>KF_CATEGORY</strong>](kf-category.md)<br/></td>
<td>Value that represent a category by which a folder registered with the Known Folder system can be classified.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KF_DEFINITION_FLAGS</strong>](kf-definition-flags.md)<br/></td>
<td>Flags that specify certain known folder behaviors. Used with the [<strong>KNOWNFOLDER_DEFINITION</strong>](knownfolder-definition.md) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>KF_REDIRECT_FLAGS</strong>](kf-redirect-flags.md)<br/></td>
<td>Flags used by [<strong>IKnownFolderManager::Redirect</strong>](iknownfoldermanager-redirect.md) to specify details of a known folder redirection such as permissions and ownership for the redirected folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KF_REDIRECTION_CAPABILITIES</strong>](kf-redirection-capabilities.md)<br/></td>
<td>Flags that specify the current redirection capabilities of a known folder. Used by [<strong>IKnownFolder::GetRedirectionCapabilities</strong>](iknownfolder-getredirectioncapabilities.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>KNOWN_FOLDER_FLAG</strong>](known-folder-flag.md)<br/></td>
<td>Specify special retrieval options for known folders. These values supersede [<strong>CSIDL</strong>](csidl.md) values, which have parallel meanings.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KNOWNFOLDERID</strong>](knownfolderid.md)<br/></td>
<td>The [<strong>KNOWNFOLDERID</strong>](knownfolderid.md) constants represent GUIDs that identify standard folders registered with the system as [Known Folders](known-folders.md). These folders are installed with Windows Vista and later operating systems, and a computer will have only folders appropriate to it installed. For descriptions of these folders, see [<strong>CSIDL</strong>](csidl.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>LIBRARYFOLDERFILTER</strong>](libraryfolderfilter.md)<br/></td>
<td>Defines options for filtering folder items. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>LIBRARYMANAGEDIALOGOPTIONS</strong>](librarymanagedialogoptions.md)<br/></td>
<td>Used by [<strong>SHShowManageLibraryUI</strong>](shshowmanagelibraryui.md) to define options for handling a name collision when saving a library.<br/></td>
</tr>
<tr class="even">
<td>[<strong>LIBRARYOPTIONFLAGS</strong>](libraryoptionflags.md)<br/></td>
<td>Specifies the library options.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>LIBRARYSAVEFLAGS</strong>](librarysaveflags.md)<br/></td>
<td>Specifies the options for handling a name collision when saving a library. <br/></td>
</tr>
<tr class="even">
<td>[<strong>MIMEASSOCIATIONDIALOG_IN_FLAGS</strong>](mimeassociationdialog-in-flags.md)<br/></td>
<td>Used with the [<strong>MIMEAssociationDialog</strong>](mimeassociationdialog.md) function to determine how it executes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MONITOR_APP_VISIBILITY</strong>](monitor-app-visibility.md)<br/></td>
<td>Specifies whether a display is showing desktop windows instead of Windows Store apps.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MP_POPUPFLAGS constants</strong>](mp-popupflags.md)<br/></td>
<td>Represent options available when displaying a pop-up menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NET_STRING</strong>](net-string.md)<br/></td>
<td>Represent network address types. Use one or more (as a bitwise combination) of the following constants to create a network address mask to use with the macro [<strong>NetAddr_SetAllowType</strong>](netaddr-setallowtype.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>NSTCFOLDERCAPABILITIES</strong>](nstcfoldercapabilities.md)<br/></td>
<td>Specifies the state of a tree item. These values are used by methods of the [<strong>INameSpaceTreeControlFolderCapabilities</strong>](inamespacetreecontrolfoldercapabilities.md) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NSTCITEMSTATE</strong>](nstcitemstate.md)<br/></td>
<td>Specifies the state of a tree item. These values are used by methods of the [<strong>INameSpaceTreeControl</strong>](inamespacetreecontrol.md) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NSTCSTYLE</strong>](nstcstyle.md)<br/></td>
<td>Describes the characteristics of a given namespace tree control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NSTCSTYLE2</strong>](nstcstyle2.md)<br/></td>
<td>Used by methods of the [<strong>INameSpaceTreeControl2</strong>](inamespacetreecontrol2.md) to specify extended display styles in a Shell namespace treeview.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NWMF</strong>](nwmf.md)<br/></td>
<td>Flags used by [<strong>INewWindowManager::EvaluateNewWindow</strong>](inewwindowmanager-evaluatenewwindow.md). These values are factors in the decision of whether to display a pop-up window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PACKAGE_EXECUTION_STATE</strong>](package-execution-state.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>PERCEIVED</strong>](perceived.md)<br/></td>
<td>Specifies a file's perceived type. This set of constants is used in the [<strong>AssocGetPerceivedType</strong>](assocgetperceivedtype.md) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PUBAPPINFOFLAGS</strong>](pubappinfoflags.md)<br/></td>
<td>Specifies which members in the [<strong>PUBAPPINFO</strong>](pubappinfo.md) structure are valid. These flags are bitmasks set in the <strong>dwMask</strong> member and passed to [<strong>IPublishedApp::GetPublishedAppInfo</strong>](ipublishedapp-getpublishedappinfo.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>QUERY_USER_NOTIFICATION_STATE</strong>](query-user-notification-state.md)<br/></td>
<td>Specifies the state of the machine for the current user in relation to the propriety of sending a notification. Used by [<strong>SHQueryUserNotificationState</strong>](shqueryusernotificationstate.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Registry Data Types</strong>](hkey-type.md)<br/></td>
<td>These data types can be used to specify the type of a registry value.<br/></td>
</tr>
<tr class="even">
<td>[<strong>REGSAM</strong>](regsam.md)<br/></td>
<td>A data type used for specifying the security access attributes in the registry.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RESTRICTIONS</strong>](restrictions.md)<br/></td>
<td>These flags are used with the [<strong>SHRestricted</strong>](shrestricted.md) function. <strong>SHRestricted</strong> is used to determine whether a specified administrator policy is in effect. In many cases, applications need to modify certain behaviors in order to comply with the policies enacted by system administrators.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCALE_CHANGE_FLAGS</strong>](scale-change-flags.md)<br/></td>
<td>Flags that are used to indicate the scaling change that occured.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SCNRT_STATUS</strong>](scnrt-status.md)<br/></td>
<td>Indicates whether to enable or disable Async Register and Deregister for [<strong>SHChangeNotifyRegisterThread</strong>](shchangenotifyregisterthread.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SFBS_FLAGS</strong>](sfbs-flags.md)<br/></td>
<td>Specifies how the [<strong>StrFormatByteSizeEx</strong>](strformatbytesizeex.md) function should handle rounding of undisplayed digits.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SFGAO</strong>](sfgao.md)<br/></td>
<td>Attributes that can be retrieved on an item (file or folder) or set of items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHARD</strong>](shard.md)<br/></td>
<td>Indicates the interpretation of the data passed by [<strong>SHAddToRecentDocs</strong>](shaddtorecentdocs.md) in its <em>pv</em> parameter to identify the item whose usage statistics are being tracked.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHARE_ROLE</strong>](share-role.md)<br/></td>
<td>Specifies the access permissions assigned to the <strong>Users</strong> or <strong>Public</strong> folder. Used in [<strong>CreateShare</strong>](isharingconfigurationmanager-createshare.md) and [<strong>GetSharePermissions</strong>](isharingconfigurationmanager-getsharepermissions.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCOLSTATE</strong>](shcolstate.md)<br/></td>
<td>Describes how a property should be treated. These values are defined in Shtypes.h.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCONTF</strong>](shcontf.md)<br/></td>
<td>Determines the types of items included in an enumeration. These values are used with the [<strong>IShellFolder::EnumObjects</strong>](ishellfolder-enumobjects.md) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHELL_LINK_DATA_FLAGS</strong>](shell-link-data-flags.md)<br/></td>
<td>Specifies option settings. Used with [<strong>IShellLinkDataList::GetFlags</strong>](ishelllinkdatalist-getflags.md) and [<strong>IShellLinkDataList::SetFlags</strong>](ishelllinkdatalist-setflags.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHELL_UI_COMPONENT</strong>](shell-ui-component.md)<br/></td>
<td>Identifies the type of UI component that is needed in the shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellFolderViewOptions</strong>](shellfolderviewoptions.md)<br/></td>
<td>Specifies the view options returned by the [<strong>ViewOptions</strong>](shellfolderview-viewoptions.md) property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellSpecialFolderConstants</strong>](shellspecialfolderconstants.md)<br/></td>
<td>Specifies unique, system-independent values that identify special folders. These folders are frequently used by applications but which may not have the same name or location on any given system. For example, the system folder can be &quot;C:\Windows&quot; on one system and &quot;C:\Winnt&quot; on another.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellWindowFindWindowOptions</strong>](shellwindowfindwindowoptions.md)<br/></td>
<td>Specifies options for finding window in the Shell windows collection. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellWindowTypeConstants</strong>](shellwindowtypeconstants.md)<br/></td>
<td>Specifies types of Shell windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGDNF</strong>](shgno.md)<br/></td>
<td>Defines the values used with the [<strong>IShellFolder::GetDisplayNameOf</strong>](ishellfolder-getdisplaynameof.md) and [<strong>IShellFolder::SetNameOf</strong>](ishellfolder-setnameof.md) methods to specify the type of file or folder names used by those methods. <br/>
<blockquote>
[!Note]<br />
Prior to Windows 7, these values were packaged as the SHGNO enumeration.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGLOBALCOUNTER</strong>](shglobalcounter.md)<br/></td>
<td>Identifiers for various global counters, or shared variables. Each global counter can be incremented or decremented using [<strong>SHGlobalCounterIncrement</strong>](shglobalcounterincrement.md) and [<strong>SHGlobalCounterDecrement</strong>](shglobalcounterdecrement.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHREGDEL_FLAGS</strong>](shregdel-flags.md)<br/></td>
<td>Provides a set of values that indicate from which base key an item will be deleted.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHREGENUM_FLAGS</strong>](shregenum-flags.md)<br/></td>
<td>Provides a set of values that indicate the base key that will be used for an enumeration.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHSTOCKICONID</strong>](shstockiconid.md)<br/></td>
<td>Used by [<strong>SHGetStockIconInfo</strong>](shgetstockiconinfo.md) to identify which stock system icon to retrieve.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SICHINTF</strong>](sichint.md)<br/></td>
<td>Used to determine how to compare two Shell items. [<strong>IShellItem::Compare</strong>](ishellitem-compare.md) uses this enumerated type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SIGDN</strong>](sigdn.md)<br/></td>
<td>Requests the form of an item's display name to retrieve through [<strong>IShellItem::GetDisplayName</strong>](ishellitem-getdisplayname.md) and [<strong>SHGetNameFromIDList</strong>](shgetnamefromidlist.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SPACTION</strong>](spaction.md)<br/></td>
<td>Describes an action being performed that requires progress to be shown to the user using an [<strong>IActionProgress</strong>](iactionprogress.md) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SPBEGINF</strong>](spbeginf-constants.md)<br/></td>
<td>Used by [<strong>IActionProgress::Begin</strong>](iactionprogress-begin.md), these constants specify certain UI operations that are to be enabled or disabled.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SPTEXT</strong>](sptext.md)<br/></td>
<td>Specifies the type of descriptive text being provided to an [<strong>IActionProgress</strong>](iactionprogress.md) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SRRF</strong>](srrf.md)<br/></td>
<td>Flags that restrict the data to be set or returned.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SSF Constants</strong>](ssf-constants.md)<br/></td>
<td>Used by the [<strong>SHGetSetSettings</strong>](shgetsetsettings.md) function to specify which members of its [<strong>SHELLSTATE</strong>](shellstate.md) structure should be set or retrived.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STPFLAG</strong>](stpflag.md)<br/></td>
<td>Used by the [<strong>ITaskbarList4::SetTabProperties</strong>](itaskbarlist4-settabproperties.md) method to specify tab properties.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SVUIA_STATUS</strong>](svuia-status.md)<br/></td>
<td>Used with the [<strong>IBrowserService2::_UIActivateView</strong>](ibrowserservice2--uiactivateview.md) method to set the state of a browser view.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_CANCEL_REQUEST</strong>](syncmgr-cancel-request.md)<br/></td>
<td>Describes a request by the user to cancel a synchronization.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_CONFLICT_ITEM_TYPE</strong>](syncmgr-conflict-item-type.md)<br/></td>
<td>Describes conflict item type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_CONTROL_FLAGS</strong>](syncmgr-control-flags.md)<br/></td>
<td>Specifies how an operation requested on certain methods of [<strong>ISyncMgrControl</strong>](isyncmgrcontrol.md) should be performed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_EVENT_FLAGS</strong>](syncmgr-event-flags.md)<br/></td>
<td>Specifies flags for a synchronization event.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_EVENT_LEVEL</strong>](syncmgr-event-level.md)<br/></td>
<td>Specifies the type of event being reported to Sync Center.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_HANDLER_CAPABILITIES</strong>](syncmgr-handler-capabilities.md)<br/></td>
<td>Specifies the capabilities of a handler regarding the actions that can be performed against it.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_HANDLER_POLICIES</strong>](syncmgr-handler-policies.md)<br/></td>
<td>Enumerates policies specified by a sync handler that deviate from the default policy.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_HANDLER_TYPE</strong>](syncmgr-handler-type.md)<br/></td>
<td>Specifies the type of a handler. Used by [<strong>ISyncMgrHandlerInfo::GetType</strong>](isyncmgrhandlerinfo-gettype.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_ITEM_CAPABILITIES</strong>](syncmgr-item-capabilities.md)<br/></td>
<td>Specifies the actions that can be performed against an item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_ITEM_POLICIES</strong>](syncmgr-item-policies.md)<br/></td>
<td>Specifies an item's policies to control how they can be enabled or disabled by group policy.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_PRESENTER_CHOICE</strong>](syncmgr-presenter-choice.md)<br/></td>
<td>Describes what choice a user makes about a sync manager conflict resolution. Used by [<strong>ISyncMgrConflictPresenter</strong>](isyncmgrconflictpresenter.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_PRESENTER_NEXT_STEP</strong>](syncmgr-presenter-next-step.md)<br/></td>
<td>Describes the next step that is to occur in sync manager conflict resolution. Used by [<strong>ISyncMgrConflictPresenter</strong>](isyncmgrconflictpresenter.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_PROGRESS_STATUS</strong>](syncmgr-progress-status.md)<br/></td>
<td>Specifies the current progress status of a synchronization process. Used by [<strong>ISyncMgrSyncCallback::ReportProgress</strong>](isyncmgrsynccallback-reportprogress.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_RESOLUTION_ABILITIES</strong>](syncmgr-resolution-abilities.md)<br/></td>
<td>Indicates abilities and the conflict resolution activity to follow. Used with [<strong>ISyncMgrResolutionHandler::QueryAbilities</strong>](isyncmgrresolutionhandler-queryabilities.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_RESOLUTION_FEEDBACK</strong>](syncmgr-resolution-feedback.md)<br/></td>
<td>Describes Sync Manager resolution feedback. Used by [<strong>ISyncMgrResolutionHandler</strong>](isyncmgrresolutionhandler.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_SYNC_CONTROL_FLAGS</strong>](syncmgr-sync-control-flags.md)<br/></td>
<td>Indicates flags used by [<strong>ISyncMgrControl::StartHandlerSync</strong>](isyncmgrcontrol-starthandlersync.md) and [<strong>ISyncMgrControl::StartItemSync</strong>](isyncmgrcontrol-startitemsync.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRFLAG</strong>](syncmgr-syncmgrflag.md)<br/></td>
<td>The [<strong>SYNCMGRFLAG</strong>](syncmgr-syncmgrflag.md) enumeration values are used in the [<strong>ISyncMgrSynchronize::Initialize</strong>](syncmgr-isyncmgrsynchronize-initialize.md) method to indicate how the synchronization event was initiated.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRHANDLERFLAGS</strong>](syncmgr-syncmgrhandlerflags.md)<br/></td>
<td>Used in the [<strong>SYNCMGRHANDLERINFO</strong>](syncmgr-syncmgrhandlerinfo.md) structure as flags that apply to the current handler.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRINVOKEFLAGS</strong>](syncmgr-syncmgrinvokeflags.md)<br/></td>
<td>The [<strong>SYNCMGRINVOKEFLAGS</strong>](syncmgr-syncmgrinvokeflags.md) enumeration value specifies how the Sync Manager is to be invoked in the [<strong>ISyncMgrSynchronizeInvoke::UpdateItems</strong>](syncmgr-isyncmgrsynchronizeinvoke-updateitems.md) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRITEMFLAGS</strong>](syncmgr-syncmgritemflags.md)<br/></td>
<td>Specifies information for the current item in the [<strong>SYNCMGRITEM</strong>](syncmgr-syncmgritem.md) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRLOGLEVEL</strong>](syncmgr-syncmgrloglevel.md)<br/></td>
<td>The [<strong>SYNCMGRLOGLEVEL</strong>](syncmgr-syncmgrloglevel.md) enumeration values specify an error level for use in the [<strong>ISyncMgrSynchronizeCallback::LogError</strong>](syncmgr-isyncmgrsynchronizecallback-logerror.md) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRREGISTERFLAGS</strong>](syncmgr-syncmgrregisterflags.md)<br/></td>
<td>The [<strong>SYNCMGRREGISTERFLAGS</strong>](syncmgr-syncmgrregisterflags.md) enumeration values are used in methods of the [<strong>ISyncMgrRegister</strong>](syncmgr-isyncmgrregister.md) interface to identify events for which the handler is registered to be notified.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRSTATUS</strong>](syncmgr-syncmgrstatus.md)<br/></td>
<td>Used in the [<strong>ISyncMgrSynchronize::SetItemStatus</strong>](syncmgr-isyncmgrsynchronize-setitemstatus.md) method to specify the updated status for the item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>THUMBBUTTONFLAGS</strong>](thumbbuttonflags.md)<br/></td>
<td>Used by [<strong>THUMBBUTTON</strong>](thumbbutton.md) to control specific states and behaviors of the button.<br/></td>
</tr>
<tr class="even">
<td>[<strong>THUMBBUTTONMASK</strong>](thumbbuttonmask.md)<br/></td>
<td>Used by the [<strong>THUMBBUTTON</strong>](thumbbutton.md) structure to specify which members of that structure contain valid data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ThumbnailStreamCacheOptions</strong>](thumbnailstreamcacheoptions.md)<br/></td>
<td>Defines the cache options used by the [<strong>IThumbnailStreamCache</strong>](ithumbnailstreamcache.md) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>TRANSFER_SOURCE_FLAGS</strong>](tsf-constants.md)<br/></td>
<td>Used by methods of the [<strong>ITransferSource</strong>](itransfersource.md) and [<strong>ITransferDestination</strong>](itransferdestination.md) interfaces to control their file operations.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TRANSLATEURL_IN_FLAGS</strong>](translateurl-in-flags.md)<br/></td>
<td>The [<strong>TRANSLATEURL_IN_FLAGS</strong>](translateurl-in-flags.md) enumerated values are used with the [<strong>TranslateURL</strong>](translateurl.md) function to determine how it will execute.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UNDOCK_REASON</strong>](undock-reason.md)<br/></td>
<td>Values that indicate the reason that a docked accessibility app window has been undocked. Used by [<strong>IAccessibilityDockingServiceCallback::Undocked</strong>](iaccessibilitydockingservicecallback-undocked.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>URL_SCHEME</strong>](url-scheme.md)<br/></td>
<td>Used to specify URL schemes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>URLASSOCIATIONDIALOG_IN_FLAGS</strong>](urlassociationdialog-in-flags.md)<br/></td>
<td>The [<strong>URLASSOCIATIONDIALOG_IN_FLAGS</strong>](urlassociationdialog-in-flags.md) enumerated values are used with [<strong>URLAssociationDialog</strong>](urlassociationdialog.md) to determine how it executes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>VPCOLORFLAGS</strong>](vpcolorflags.md)<br/></td>
<td>Specifies the use of a color. Used by [<strong>IVisualProperties</strong>](ivisualproperties.md) methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>VPWATERMARKFLAGS</strong>](vpwatermarkflags.md)<br/></td>
<td>Specifies watermark flags. Used by [<strong>IVisualProperties::SetWatermark</strong>](ivisualproperties-setwatermark.md).<br/></td>
</tr>
</tbody>
</table>



 

 

 




