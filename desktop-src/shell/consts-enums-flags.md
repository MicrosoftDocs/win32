---
Description: This section describes the Windows Shell constants, enumerations, and flags.
title: Shell Constants, Enumerations, and Flags
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<td>[<strong>_SVGIO</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_svgio?branch=master)<br/></td>
<td>Used with the [<strong>IFolderView::Items</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ifolderview-items?branch=master), [<strong>IFolderView::ItemCount</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ifolderview-itemcount?branch=master), and [<strong>IShellView::GetItemObject</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellview-getitemobject?branch=master) methods to restrict or control the items in their collections.<br/></td>
</tr>
<tr class="even">
<td>[<strong>_SVSIF</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_svsif?branch=master)<br/></td>
<td>Indicates flags used by [<strong>IFolderView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifolderview?branch=master), [<strong>IFolderView2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifolderview2?branch=master), [<strong>IShellView</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview?branch=master) and [<strong>IShellView2</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellview2?branch=master) to specify a type of selection to apply.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPACTIONFLAGS</strong>](/windows/win32/Shappmgr/ne-shappmgr-_tagappactionflags?branch=master)<br/></td>
<td>Specifies application management actions supported by an application publisher. These flags are bitmasks passed to [<strong>IShellApp::GetPossibleActions</strong>](/windows/win32/Shappmgr/nf-shappmgr-ishellapp-getpossibleactions?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>APPINFODATAFLAGS</strong>](/windows/win32/Shappmgr/ne-shappmgr-_tagappinfoflags?branch=master)<br/></td>
<td>Specifies application information to return from [<strong>IShellApp::GetAppInfo</strong>](/windows/win32/Shappmgr/nf-shappmgr-ishellapp-getappinfo?branch=master). These flags are bitmasks used in the [<strong>dwMask</strong>](/windows/win32/Shappmgr/ns-shappmgr-_appinfodata?branch=master) member of the <strong>APPINFODATA</strong> structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPLICATION_VIEW_ORIENTATION</strong>](/windows/win32/Shobjidl_core/ne-shobjidl_core-application_view_orientation?branch=master)<br/></td>
<td>Defines the set of display orientation modes for a window (app view). Used by [<strong>IApplicationDesignModeSettings2::GetApplicationViewOrientation</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings2-getapplicationvieworientation?branch=master) and [<strong>IApplicationDesignModeSettings2::SetApplicationViewOrientation</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings2-setapplicationvieworientation?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>APPLICATION_VIEW_SIZE_PREFERENCE</strong>](/windows/win32/Shobjidl_core/ne-shobjidl_core-application_view_size_preference?branch=master)<br/></td>
<td>Defines the set of possible general window (app view) size preferences. Used by [<strong>ILaunchSourceViewSizePreference::GetSourceViewSizePreference</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ilaunchsourceviewsizepreference-getsourceviewsizepreference?branch=master) and [<strong>ILaunchTargetViewSizePreference::GetTargetViewSizePreference</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ilaunchtargetviewsizepreference-gettargetviewsizepreference?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPLICATION_VIEW_STATE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-application_view_state?branch=master)<br/></td>
<td>Indicates the current view state of a Windows Store app. Used by [<strong>IApplicationDesignModeSettings::SetApplicationViewState</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings-setapplicationviewstate?branch=master) and [<strong>IApplicationDesignModeSettings::IsApplicationViewStateSupported</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings-isapplicationviewstatesupported?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>ASSOCDATA</strong>](/windows/win32/Shlwapi/ne-shlwapi-assocdata?branch=master)<br/></td>
<td>Used by [<strong>IQueryAssociations::GetData</strong>](/windows/win32/Shlwapi/?branch=master) to define the type of data that is to be returned.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCF</strong>](/windows/win32/Shlwapi/?branch=master)<br/></td>
<td>Provides information to the [<strong>IQueryAssociations</strong>](/windows/win32/Shlwapi/?branch=master) interface methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ASSOCIATIONLEVEL</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-associationlevel?branch=master)<br/></td>
<td>Specifies the source of the default association for a file name extension. Used by methods of the [<strong>IApplicationAssociationRegistration</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iapplicationassociationregistration?branch=master) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCIATIONTYPE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-associationtype?branch=master)<br/></td>
<td>Specifies the type of association for an application. Used by methods of the [<strong>IApplicationAssociationRegistration</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iapplicationassociationregistration?branch=master) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ASSOCKEY</strong>](/windows/win32/Shlwapi/ne-shlwapi-assockey?branch=master)<br/></td>
<td>Specifies the type of key to be returned by [<strong>IQueryAssociations::GetKey</strong>](/windows/win32/Shlwapi/?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCSTR</strong>](/windows/win32/Shlwapi/ne-shlwapi-assocstr?branch=master)<br/></td>
<td>Used by [<strong>IQueryAssociations::GetString</strong>](/windows/win32/Shlwapi/?branch=master) to define the type of string that is to be returned.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ATTACHMENT_ACTION</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-attachment_action?branch=master)<br/></td>
<td>Provides a set of flags to be used with [<strong>IAttachmentExecute::Prompt</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iattachmentexecute-prompt?branch=master) to indicate the action to be performed upon user confirmation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ATTACHMENT_PROMPT</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-attachment_prompt?branch=master)<br/></td>
<td>Provides a set of flags to be used with [<strong>IAttachmentExecute::Prompt</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iattachmentexecute-prompt?branch=master) to indicate the type of prompt UI to display.<br/></td>
</tr>
<tr class="even">
<td>[<strong>AUTOCOMPLETELISTOPTIONS</strong>](/windows/win32/shlobj_core/ne-shlobj_core-_tagautocompletelistoptions?branch=master)<br/></td>
<td>Specifies which objects are enumerated for autocompletion lists.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>AUTOCOMPLETEOPTIONS</strong>](/windows/win32/Shldisp/ne-shldisp-_tagautocompleteoptions?branch=master)<br/></td>
<td>Specifies values used by [<strong>IAutoComplete2::GetOptions</strong>](/windows/win32/Shldisp/nf-shldisp-iautocomplete2-getoptions?branch=master) and [<strong>IAutoComplete2::SetOptions</strong>](/windows/win32/Shldisp/nf-shldisp-iautocomplete2-setoptions?branch=master) for options surrounding autocomplete.<br/></td>
</tr>
<tr class="even">
<td>[<strong>Bind Context String Keys</strong>](str-constants.md)<br/></td>
<td>A set of string keys that are used with the [<strong>IBindCtx::RegisterObjectParam</strong>](com.ibindctx_registerobjectparam) method to specify a bind context.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BNSTATE</strong>](/windows/win32/Shdeprecated/ne-shdeprecated-tagbnstate?branch=master)<br/></td>
<td>Deprecated. Used by [<strong>IBrowserService::SetNavigateState</strong>](/windows/win32/Shdeprecated/nf-shdeprecated-ibrowserservice-setnavigatestate?branch=master) and [<strong>IBrowserService::GetNavigateState</strong>](/windows/win32/Shdeprecated/nf-shdeprecated-ibrowserservice-getnavigatestate?branch=master) to specify navigation states.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BROWSERFRAMEOPTIONS</strong>](/windows/win32/Shobjidl_core/ne-shobjidl_core-_browserframeoptions?branch=master)<br/></td>
<td>Used with method [<strong>IBrowserFrameOptions::GetFrameOptions</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ibrowserframeoptions-getframeoptions?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CATEGORYINFO_FLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-categoryinfo_flags?branch=master)<br/></td>
<td>Provides a set of flags for use with the [<strong>CATEGORY_INFO</strong>](/windows/win32/shobjidl_core/ns-shobjidl_core-category_info?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CATSORT_FLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-catsort_flags?branch=master)<br/></td>
<td>Specifies methods for sorting category data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CDCONTROLSTATE</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Specifies the values that indicate whether a control is visible and enabled. Used by members of the [<strong>IFileDialogCustomize</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifiledialogcustomize?branch=master) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_ENUM_FLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-cm_enum_flags?branch=master)<br/></td>
<td>Used by members of the [<strong>IColumnManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icolumnmanager?branch=master) interface to specify which set of columns are being requested, either all or only those currently visible.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_MASK</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-cm_mask?branch=master)<br/></td>
<td>Indicates which values in the [<strong>CM_COLUMNINFO</strong>](/windows/win32/shobjidl_core/ns-shobjidl_core-cm_columninfo?branch=master) structure should be set during calls to [<strong>IColumnManager::SetColumnInfo</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-icolumnmanager-setcolumninfo?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_SET_WIDTH_VALUE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-cm_set_width_value?branch=master)<br/></td>
<td>Specifies width values in pixels and includes special support for default and autosize. Used by members of the [<strong>IColumnManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icolumnmanager?branch=master) interface through the [<strong>CM_COLUMNINFO</strong>](/windows/win32/shobjidl_core/ns-shobjidl_core-cm_columninfo?branch=master) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_STATE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-cm_state?branch=master)<br/></td>
<td>Specifies column state values. Used by members of the [<strong>IColumnManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-icolumnmanager?branch=master) interface through the [<strong>CM_COLUMNINFO</strong>](/windows/win32/shobjidl_core/ns-shobjidl_core-cm_columninfo?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS</strong>](/windows/win32/CredentialProvider/ne-credentialprovider-credential_provider_account_options?branch=master)<br/></td>
<td>Indicates the type of credential that a credential provider should return to associate with the &quot;Other user&quot; tile. Used by [<strong>ICredentialProviderUserArray_GetAccountOptions</strong>](/windows/win32/CredentialProvider/nf-credentialprovider-icredentialprovideruserarray-getaccountoptions?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS</strong>](/windows/win32/CredentialProvider/ne-credentialprovider-credential_provider_credential_field_options?branch=master)<br/></td>
<td>Provides customization options for a single field in a logon or credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE</strong>](/windows/win32/Credentialprovider/ne-credentialprovider-_credential_provider_field_interactive_state?branch=master)<br/></td>
<td>Describes the state of a field and how it a user can interact with it. Fields can be displayed by a credential provider in a variety of different interactive states.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_STATE</strong>](/windows/win32/Credentialprovider/ne-credentialprovider-_credential_provider_field_state?branch=master)<br/></td>
<td>Specifies the state of a single field in the Credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_TYPE</strong>](/windows/win32/Credentialprovider/ne-credentialprovider-_credential_provider_field_type?branch=master)<br/></td>
<td>Specifies a type of credential field. Used by [<strong>CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR</strong>](/windows/win32/Credentialprovider/ns-credentialprovider-_credential_provider_field_descriptor?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE</strong>](/windows/win32/Credentialprovider/ne-credentialprovider-_credential_provider_get_serialization_response?branch=master)<br/></td>
<td>Describes the response when a credential provider attempts to serialize credentials.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_STATUS_ICON</strong>](/windows/win32/Credentialprovider/ne-credentialprovider-_credential_provider_status_icon?branch=master)<br/></td>
<td>Indicates which status icon should be displayed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_USAGE_SCENARIO</strong>](/windows/win32/Credentialprovider/ne-credentialprovider-_credential_provider_usage_scenario?branch=master)<br/></td>
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
<td>Flags that control the calling function's behavior. Used by [<strong>SHCreateThread</strong>](/windows/win32/Shlwapi/nf-shlwapi-shcreatethread?branch=master) and [<strong>SHCreateThreadWithHandle</strong>](/windows/win32/Shlwapi/nf-shlwapi-shcreatethreadwithhandle?branch=master). In those functions, these values are defined as being of type SHCT_FLAGS.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DATAOBJ_GET_ITEM_FLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-dataobj_get_item_flags?branch=master)<br/></td>
<td>Values used by the [<strong>SHGetItemFromDataObject</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shgetitemfromdataobject?branch=master) function to specify options concerning the processing of the source object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DBID Command Flags</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-tagdeskbandcid?branch=master)<br/></td>
<td>These command IDs can be sent to the band object's container with [<strong>IOleCommandTarget::Exec</strong>](com.iolecommandtarget_exec).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEF_SHARE_ID</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-def_share_id?branch=master)<br/></td>
<td>Values that specify the folder being acted on by methods of the [<strong>ISharingConfigurationManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-isharingconfigurationmanager?branch=master) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DEFAULTSAVEFOLDERTYPE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-defaultsavefoldertype?branch=master)<br/></td>
<td>Specifies the default save location.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEFAULT_FOLDER_MENU_RESTRICTIONS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-default_folder_menu_restrictions?branch=master)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>DESKTOP_WALLPAPER_POSITION</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-desktop_wallpaper_position?branch=master)<br/></td>
<td>Specifies how the desktop wallpaper should be displayed.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEVICE_SCALE_FACTOR</strong>](/windows/win32/Shtypes/ne-shtypes-device_scale_factor?branch=master)<br/></td>
<td>Indicates a spoofed device scale factor, as a percent. Used by [<strong>IApplicationDesignModeSettings::SetApplicationViewState</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings-setapplicationviewstate?branch=master) and [<strong>IApplicationDesignModeSettings::IsApplicationViewStateSupported</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings-isapplicationviewstatesupported?branch=master)<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DISPLAY_DEVICE_TYPE</strong>](/windows/win32/ShellScalingAPI/ne-shellscalingapi-display_device_type?branch=master)<br/></td>
<td>Indicates whether the device is a primary or immersive type of display.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DROPIMAGETYPE</strong>](/windows/win32/shlobj_core/ne-shlobj_core-dropimagetype?branch=master)<br/></td>
<td>Values used with the [<strong>DROPDESCRIPTION</strong>](/windows/win32/shlobj_core/ns-shlobj_core-dropdescription?branch=master) structure to specify the drop image.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXPCMDSTATE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_expcmdstate?branch=master)<br/></td>
<td>[<strong>EXPCMDSTATE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_expcmdstate?branch=master) values represent the command state of a Shell item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXPLORER_BROWSER_FILL_FLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-explorer_browser_fill_flags?branch=master)<br/></td>
<td>These flags are used with [<strong>IExplorerBrowser::FillFromObject</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iexplorerbrowser-fillfromobject?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXPLORER_BROWSER_OPTIONS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-explorer_browser_options?branch=master)<br/></td>
<td>These flags are used with [<strong>IExplorerBrowser::GetOptions</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iexplorerbrowser-getoptions?branch=master) and [<strong>IExplorerBrowser::SetOptions</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iexplorerbrowser-setoptions?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXPLORERPANESTATE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_explorerpanestate?branch=master)<br/></td>
<td>Indicate flags used by [<strong>IExplorerPaneVisibility::GetPaneState</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iexplorerpanevisibility-getpanestate?branch=master) to get the current state of the given Windows Explorer pane.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FDAP</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-fdap?branch=master)<br/></td>
<td>Specifies list placement.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FDE_OVERWRITE_RESPONSE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-fde_overwrite_response?branch=master)<br/></td>
<td>Specifies the values used by the [<strong>IFileDialogEvents::OnOverwrite</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ifiledialogevents-onoverwrite?branch=master) method to indicate an application's response to an overwrite request during a save operation using the common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FDE_SHAREVIOLATION_RESPONSE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-fde_shareviolation_response?branch=master)<br/></td>
<td>Specifies the values used by the [<strong>IFileDialogEvents::OnShareViolation</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ifiledialogevents-onshareviolation?branch=master) method to indicate an application's response to a sharing violation that occurs when a file is opened or saved.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FFFP_MODE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-fffp_mode?branch=master)<br/></td>
<td>Describes match criteria. Used by methods of the [<strong>IKnownFolderManager</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iknownfoldermanager?branch=master) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FILE_USAGE_TYPE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-file_usage_type?branch=master)<br/></td>
<td>Constants used by [<strong>IFileIsInUse::GetUsage</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ifileisinuse-getusage?branch=master) to indicate how a file in use is being used.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FILEOPENDIALOGOPTIONS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_fileopendialogoptions?branch=master)<br/></td>
<td>Defines the set of options available to an Open or Save dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FILETYPEATTRIBUTEFLAGS</strong>](/windows/win32/Shlwapi/ne-shlwapi-filetypeattributeflags?branch=master)<br/></td>
<td>Indicates [<strong>FILETYPEATTRIBUTEFLAGS</strong>](/windows/win32/Shlwapi/ne-shlwapi-filetypeattributeflags?branch=master) constants that are used in the EditFlags value of a file association [PROGID](fa-progids.md) registry key.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDER_ENUM_MODE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-folder_enum_mode?branch=master)<br/></td>
<td>Used by [<strong>IObjectWithFolderEnumMode::GetMode</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iobjectwithfolderenummode-getmode?branch=master) and [<strong>IObjectWithFolderEnumMode::SetMode</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iobjectwithfolderenummode-setmode?branch=master) methods to get and set the display modes for the folders.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FOLDERFLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-folderflags?branch=master)<br/></td>
<td>A set of flags that specify folder view options. The flags are independent of each other and can be used in any combination.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDERLOGICALVIEWMODE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-folderlogicalviewmode?branch=master)<br/></td>
<td>Used by [<strong>IFolderViewSettings::GetViewMode</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ifolderviewsettings-getviewmode?branch=master) and [<strong>ISearchFolderItemFactory::SetFolderLogicalViewMode</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-isearchfolderitemfactory-setfolderlogicalviewmode?branch=master) to describe the view mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FOLDERTYPEID</strong>](foldertypeid.md)<br/></td>
<td>The [<strong>FOLDERTYPEID</strong>](foldertypeid.md) values represent a view template applied to a folder, usually based on its intended use and contents.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDERVIEWMODE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-folderviewmode?branch=master)<br/></td>
<td>Specifies the folder view type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FOLDERVIEWOPTIONS</strong>](/windows/win32/Shobjidl/ne-shobjidl-folderviewoptions?branch=master)<br/></td>
<td>Used by methods of the [<strong>IFolderViewOptions</strong>](/windows/win32/Shobjidl/nn-shobjidl-ifolderviewoptions?branch=master) interface to activate Windows Vista options not supported by default in Windows 7 and later systems as well as deactivating new Windows 7 options.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IActiveDesktop Flags</strong>](iactivedesktop-flags.md)<br/></td>
<td>This section describes the flags used by [<strong>IActiveDesktop</strong>](lwef.iactivedesktop_interface) interface methods.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IESHORTCUTFLAGS</strong>](/windows/win32/shlobj_core/ne-shlobj_core-tagieshortcutflags?branch=master)<br/></td>
<td>Specifies how a shortcut should be handled by the browser.<br/></td>
</tr>
<tr class="even">
<td>[<strong>KF_CATEGORY</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-kf_category?branch=master)<br/></td>
<td>Value that represent a category by which a folder registered with the Known Folder system can be classified.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KF_DEFINITION_FLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_kf_definition_flags?branch=master)<br/></td>
<td>Flags that specify certain known folder behaviors. Used with the [<strong>KNOWNFOLDER_DEFINITION</strong>](/windows/win32/Shobjidl_core/ns-shobjidl_core-knownfolder_definition?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>KF_REDIRECT_FLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_kf_redirect_flags?branch=master)<br/></td>
<td>Flags used by [<strong>IKnownFolderManager::Redirect</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iknownfoldermanager-redirect?branch=master) to specify details of a known folder redirection such as permissions and ownership for the redirected folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KF_REDIRECTION_CAPABILITIES</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_kf_redirection_capabilities?branch=master)<br/></td>
<td>Flags that specify the current redirection capabilities of a known folder. Used by [<strong>IKnownFolder::GetRedirectionCapabilities</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iknownfolder-getredirectioncapabilities?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>KNOWN_FOLDER_FLAG</strong>](/windows/win32/shlobj_core/ne-shlobj_core-known_folder_flag?branch=master)<br/></td>
<td>Specify special retrieval options for known folders. These values supersede [<strong>CSIDL</strong>](csidl.md) values, which have parallel meanings.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KNOWNFOLDERID</strong>](knownfolderid.md)<br/></td>
<td>The [<strong>KNOWNFOLDERID</strong>](knownfolderid.md) constants represent GUIDs that identify standard folders registered with the system as [Known Folders](known-folders.md). These folders are installed with Windows Vista and later operating systems, and a computer will have only folders appropriate to it installed. For descriptions of these folders, see [<strong>CSIDL</strong>](csidl.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>LIBRARYFOLDERFILTER</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-libraryfolderfilter?branch=master)<br/></td>
<td>Defines options for filtering folder items. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>LIBRARYMANAGEDIALOGOPTIONS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-librarymanagedialogoptions?branch=master)<br/></td>
<td>Used by [<strong>SHShowManageLibraryUI</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shshowmanagelibraryui?branch=master) to define options for handling a name collision when saving a library.<br/></td>
</tr>
<tr class="even">
<td>[<strong>LIBRARYOPTIONFLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-libraryoptionflags?branch=master)<br/></td>
<td>Specifies the library options.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>LIBRARYSAVEFLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-librarysaveflags?branch=master)<br/></td>
<td>Specifies the options for handling a name collision when saving a library. <br/></td>
</tr>
<tr class="even">
<td>[<strong>MIMEASSOCIATIONDIALOG_IN_FLAGS</strong>](/windows/win32/Intshcut/ne-intshcut-mimeassociationdialog_in_flags?branch=master)<br/></td>
<td>Used with the [<strong>MIMEAssociationDialog</strong>](/windows/win32/Intshcut/nf-intshcut-mimeassociationdialoga?branch=master) function to determine how it executes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MONITOR_APP_VISIBILITY</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-monitor_app_visibility?branch=master)<br/></td>
<td>Specifies whether a display is showing desktop windows instead of Windows Store apps.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MP_POPUPFLAGS constants</strong>](mp-popupflags.md)<br/></td>
<td>Represent options available when displaying a pop-up menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NET_STRING</strong>](net-string.md)<br/></td>
<td>Represent network address types. Use one or more (as a bitwise combination) of the following constants to create a network address mask to use with the macro [<strong>NetAddr_SetAllowType</strong>](/windows/win32/Shellapi/nf-shellapi-netaddr_setallowtype?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>NSTCFOLDERCAPABILITIES</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-nstcfoldercapabilities?branch=master)<br/></td>
<td>Specifies the state of a tree item. These values are used by methods of the [<strong>INameSpaceTreeControlFolderCapabilities</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacetreecontrolfoldercapabilities?branch=master) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NSTCITEMSTATE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_nstcitemstate?branch=master)<br/></td>
<td>Specifies the state of a tree item. These values are used by methods of the [<strong>INameSpaceTreeControl</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-inamespacetreecontrol?branch=master) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NSTCSTYLE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_nstcstyle?branch=master)<br/></td>
<td>Describes the characteristics of a given namespace tree control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NSTCSTYLE2</strong>](/windows/win32/Shobjidl/ne-shobjidl-nstcstyle2?branch=master)<br/></td>
<td>Used by methods of the [<strong>INameSpaceTreeControl2</strong>](/windows/win32/Shobjidl/nn-shobjidl-inamespacetreecontrol2?branch=master) to specify extended display styles in a Shell namespace treeview.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NWMF</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-nwmf?branch=master)<br/></td>
<td>Flags used by [<strong>INewWindowManager::EvaluateNewWindow</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-inewwindowmanager-evaluatenewwindow?branch=master). These values are factors in the decision of whether to display a pop-up window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PACKAGE_EXECUTION_STATE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-package_execution_state?branch=master)<br/></td>

</tr>
<tr class="even">
<td>[<strong>PERCEIVED</strong>](/windows/win32/Shtypes/ne-shtypes-tagperceived?branch=master)<br/></td>
<td>Specifies a file's perceived type. This set of constants is used in the [<strong>AssocGetPerceivedType</strong>](/windows/win32/Shlwapi/nf-shlwapi-assocgetperceivedtype?branch=master) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PUBAPPINFOFLAGS</strong>](/windows/win32/Shappmgr/ne-shappmgr-_tagpublishedappinfoflags?branch=master)<br/></td>
<td>Specifies which members in the [<strong>PUBAPPINFO</strong>](/windows/win32/Shappmgr/ns-shappmgr-_pubappinfo?branch=master) structure are valid. These flags are bitmasks set in the <strong>dwMask</strong> member and passed to [<strong>IPublishedApp::GetPublishedAppInfo</strong>](/windows/win32/Shappmgr/nf-shappmgr-ipublishedapp-getpublishedappinfo?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>QUERY_USER_NOTIFICATION_STATE</strong>](/windows/win32/Shellapi/ne-shellapi-query_user_notification_state?branch=master)<br/></td>
<td>Specifies the state of the machine for the current user in relation to the propriety of sending a notification. Used by [<strong>SHQueryUserNotificationState</strong>](/windows/win32/Shellapi/nf-shellapi-shqueryusernotificationstate?branch=master).<br/></td>
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
<td>[<strong>RESTRICTIONS</strong>](/windows/win32/shlobj_core/ne-shlobj_core-restrictions?branch=master)<br/></td>
<td>These flags are used with the [<strong>SHRestricted</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shrestricted?branch=master) function. <strong>SHRestricted</strong> is used to determine whether a specified administrator policy is in effect. In many cases, applications need to modify certain behaviors in order to comply with the policies enacted by system administrators.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCALE_CHANGE_FLAGS</strong>](/windows/win32/ShellScalingAPI/ne-shellscalingapi-scale_change_flags?branch=master)<br/></td>
<td>Flags that are used to indicate the scaling change that occured.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SCNRT_STATUS</strong>](/windows/win32/shlobj_core/ne-shlobj_core-scnrt_status?branch=master)<br/></td>
<td>Indicates whether to enable or disable Async Register and Deregister for [<strong>SHChangeNotifyRegisterThread</strong>](/windows/win32/Shlobj/nf-shlobj-shchangenotifyregisterthread?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SFBS_FLAGS</strong>](/windows/win32/Shlwapi/ne-shlwapi-tagsfbs_flags?branch=master)<br/></td>
<td>Specifies how the [<strong>StrFormatByteSizeEx</strong>](/windows/win32/Shlwapi/nf-shlwapi-strformatbytesizeex?branch=master) function should handle rounding of undisplayed digits.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SFGAO</strong>](sfgao.md)<br/></td>
<td>Attributes that can be retrieved on an item (file or folder) or set of items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHARD</strong>](/windows/win32/shlobj_core/ne-shlobj_core-shard?branch=master)<br/></td>
<td>Indicates the interpretation of the data passed by [<strong>SHAddToRecentDocs</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shaddtorecentdocs?branch=master) in its <em>pv</em> parameter to identify the item whose usage statistics are being tracked.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHARE_ROLE</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-share_role?branch=master)<br/></td>
<td>Specifies the access permissions assigned to the <strong>Users</strong> or <strong>Public</strong> folder. Used in [<strong>CreateShare</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-isharingconfigurationmanager-createshare?branch=master) and [<strong>GetSharePermissions</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-isharingconfigurationmanager-getsharepermissions?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCOLSTATE</strong>](/windows/win32/Shtypes/ne-shtypes-tagshcolstate?branch=master)<br/></td>
<td>Describes how a property should be treated. These values are defined in Shtypes.h.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCONTF</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_shcontf?branch=master)<br/></td>
<td>Determines the types of items included in an enumeration. These values are used with the [<strong>IShellFolder::EnumObjects</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-enumobjects?branch=master) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHELL_LINK_DATA_FLAGS</strong>](/windows/win32/shlobj_core/ne-shlobj_core-shell_link_data_flags?branch=master)<br/></td>
<td>Specifies option settings. Used with [<strong>IShellLinkDataList::GetFlags</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishelllinkdatalist-getflags?branch=master) and [<strong>IShellLinkDataList::SetFlags</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishelllinkdatalist-setflags?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHELL_UI_COMPONENT</strong>](/windows/win32/ShellScalingApi/ne-shellscalingapi-shell_ui_component?branch=master)<br/></td>
<td>Identifies the type of UI component that is needed in the shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellFolderViewOptions</strong>](/windows/win32/Shldisp/ne-shldisp-shellfolderviewoptions?branch=master)<br/></td>
<td>Specifies the view options returned by the [<strong>ViewOptions</strong>](shellfolderview-viewoptions.md) property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellSpecialFolderConstants</strong>](/windows/win32/Shldisp/ne-shldisp-shellspecialfolderconstants?branch=master)<br/></td>
<td>Specifies unique, system-independent values that identify special folders. These folders are frequently used by applications but which may not have the same name or location on any given system. For example, the system folder can be &quot;C:\Windows&quot; on one system and &quot;C:\Winnt&quot; on another.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellWindowFindWindowOptions</strong>](/windows/win32/ExDisp/ne-exdisp-shellwindowfindwindowoptions?branch=master)<br/></td>
<td>Specifies options for finding window in the Shell windows collection. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellWindowTypeConstants</strong>](/windows/win32/Exdisp/ne-exdisp-shellwindowtypeconstants?branch=master)<br/></td>
<td>Specifies types of Shell windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGDNF</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_shgdnf?branch=master)<br/></td>
<td>Defines the values used with the [<strong>IShellFolder::GetDisplayNameOf</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof?branch=master) and [<strong>IShellFolder::SetNameOf</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-setnameof?branch=master) methods to specify the type of file or folder names used by those methods. <br/>
<blockquote>
[!Note]<br />
Prior to Windows 7, these values were packaged as the SHGNO enumeration.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGLOBALCOUNTER</strong>](/windows/win32/Shlwapi/ne-shlwapi-shglobalcounter?branch=master)<br/></td>
<td>Identifiers for various global counters, or shared variables. Each global counter can be incremented or decremented using [<strong>SHGlobalCounterIncrement</strong>](/windows/win32/Shlwapi/nf-shlwapi-shglobalcounterincrement?branch=master) and [<strong>SHGlobalCounterDecrement</strong>](/windows/win32/Shlwapi/nf-shlwapi-shglobalcounterdecrement?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHREGDEL_FLAGS</strong>](/windows/win32/Shlwapi/ne-shlwapi-shregdel_flags?branch=master)<br/></td>
<td>Provides a set of values that indicate from which base key an item will be deleted.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHREGENUM_FLAGS</strong>](/windows/win32/Shlwapi/ne-shlwapi-shregenum_flags?branch=master)<br/></td>
<td>Provides a set of values that indicate the base key that will be used for an enumeration.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHSTOCKICONID</strong>](/windows/win32/Shellapi/ne-shellapi-shstockiconid?branch=master)<br/></td>
<td>Used by [<strong>SHGetStockIconInfo</strong>](/windows/win32/Shellapi/nf-shellapi-shgetstockiconinfo?branch=master) to identify which stock system icon to retrieve.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SICHINTF</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_sichintf?branch=master)<br/></td>
<td>Used to determine how to compare two Shell items. [<strong>IShellItem::Compare</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellitem-compare?branch=master) uses this enumerated type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SIGDN</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_sigdn?branch=master)<br/></td>
<td>Requests the form of an item's display name to retrieve through [<strong>IShellItem::GetDisplayName</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellitem-getdisplayname?branch=master) and [<strong>SHGetNameFromIDList</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shgetnamefromidlist?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SPACTION</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_spaction?branch=master)<br/></td>
<td>Describes an action being performed that requires progress to be shown to the user using an [<strong>IActionProgress</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iactionprogress?branch=master) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SPBEGINF</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_spbeginf?branch=master)<br/></td>
<td>Used by [<strong>IActionProgress::Begin</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iactionprogress-begin?branch=master), these constants specify certain UI operations that are to be enabled or disabled.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SPTEXT</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_sptext?branch=master)<br/></td>
<td>Specifies the type of descriptive text being provided to an [<strong>IActionProgress</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iactionprogress?branch=master) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SRRF</strong>](srrf.md)<br/></td>
<td>Flags that restrict the data to be set or returned.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SSF Constants</strong>](ssf-constants.md)<br/></td>
<td>Used by the [<strong>SHGetSetSettings</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetsetsettings?branch=master) function to specify which members of its [<strong>SHELLSTATE</strong>](/windows/win32/Shlobj/ns-shlobj_core-shellstatea?branch=master) structure should be set or retrived.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STPFLAG</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-stpflag?branch=master)<br/></td>
<td>Used by the [<strong>ITaskbarList4::SetTabProperties</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-itaskbarlist4-settabproperties?branch=master) method to specify tab properties.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SVUIA_STATUS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-svuia_status?branch=master)<br/></td>
<td>Used with the [<strong>IBrowserService2::_UIActivateView</strong>](/windows/win32/Shdeprecated/nf-shdeprecated-ibrowserservice2-_uiactivateview?branch=master) method to set the state of a browser view.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_CANCEL_REQUEST</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_cancel_request?branch=master)<br/></td>
<td>Describes a request by the user to cancel a synchronization.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_CONFLICT_ITEM_TYPE</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_conflict_item_type?branch=master)<br/></td>
<td>Describes conflict item type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_CONTROL_FLAGS</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_control_flags?branch=master)<br/></td>
<td>Specifies how an operation requested on certain methods of [<strong>ISyncMgrControl</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrcontrol?branch=master) should be performed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_EVENT_FLAGS</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_event_flags?branch=master)<br/></td>
<td>Specifies flags for a synchronization event.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_EVENT_LEVEL</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_event_level?branch=master)<br/></td>
<td>Specifies the type of event being reported to Sync Center.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_HANDLER_CAPABILITIES</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_handler_capabilities?branch=master)<br/></td>
<td>Specifies the capabilities of a handler regarding the actions that can be performed against it.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_HANDLER_POLICIES</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_handler_policies?branch=master)<br/></td>
<td>Enumerates policies specified by a sync handler that deviate from the default policy.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_HANDLER_TYPE</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_handler_type?branch=master)<br/></td>
<td>Specifies the type of a handler. Used by [<strong>ISyncMgrHandlerInfo::GetType</strong>](/windows/win32/Syncmgr/nf-syncmgr-isyncmgrhandlerinfo-gettype?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_ITEM_CAPABILITIES</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_item_capabilities?branch=master)<br/></td>
<td>Specifies the actions that can be performed against an item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_ITEM_POLICIES</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_item_policies?branch=master)<br/></td>
<td>Specifies an item's policies to control how they can be enabled or disabled by group policy.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_PRESENTER_CHOICE</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_presenter_choice?branch=master)<br/></td>
<td>Describes what choice a user makes about a sync manager conflict resolution. Used by [<strong>ISyncMgrConflictPresenter</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrconflictpresenter?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_PRESENTER_NEXT_STEP</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_presenter_next_step?branch=master)<br/></td>
<td>Describes the next step that is to occur in sync manager conflict resolution. Used by [<strong>ISyncMgrConflictPresenter</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrconflictpresenter?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_PROGRESS_STATUS</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_progress_status?branch=master)<br/></td>
<td>Specifies the current progress status of a synchronization process. Used by [<strong>ISyncMgrSyncCallback::ReportProgress</strong>](/windows/win32/Syncmgr/nf-syncmgr-isyncmgrsynccallback-reportprogress?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_RESOLUTION_ABILITIES</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_resolution_abilities?branch=master)<br/></td>
<td>Indicates abilities and the conflict resolution activity to follow. Used with [<strong>ISyncMgrResolutionHandler::QueryAbilities</strong>](/windows/win32/Syncmgr/nf-syncmgr-isyncmgrresolutionhandler-queryabilities?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_RESOLUTION_FEEDBACK</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_resolution_feedback?branch=master)<br/></td>
<td>Describes Sync Manager resolution feedback. Used by [<strong>ISyncMgrResolutionHandler</strong>](/windows/win32/Syncmgr/nn-syncmgr-isyncmgrresolutionhandler?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_SYNC_CONTROL_FLAGS</strong>](/windows/win32/Syncmgr/ne-syncmgr-syncmgr_sync_control_flags?branch=master)<br/></td>
<td>Indicates flags used by [<strong>ISyncMgrControl::StartHandlerSync</strong>](/windows/win32/Syncmgr/nf-syncmgr-isyncmgrcontrol-starthandlersync?branch=master) and [<strong>ISyncMgrControl::StartItemSync</strong>](/windows/win32/Syncmgr/nf-syncmgr-isyncmgrcontrol-startitemsync?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRFLAG</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrflag?branch=master)<br/></td>
<td>The [<strong>SYNCMGRFLAG</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrflag?branch=master) enumeration values are used in the [<strong>ISyncMgrSynchronize::Initialize</strong>](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronize-initialize?branch=master) method to indicate how the synchronization event was initiated.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRHANDLERFLAGS</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrhandlerflags?branch=master)<br/></td>
<td>Used in the [<strong>SYNCMGRHANDLERINFO</strong>](/windows/win32/Mobsync/ns-mobsync-_tagsyncmgrhandlerinfo?branch=master) structure as flags that apply to the current handler.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRINVOKEFLAGS</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrinvokeflags?branch=master)<br/></td>
<td>The [<strong>SYNCMGRINVOKEFLAGS</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrinvokeflags?branch=master) enumeration value specifies how the Sync Manager is to be invoked in the [<strong>ISyncMgrSynchronizeInvoke::UpdateItems</strong>](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronizeinvoke-updateitems?branch=master) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRITEMFLAGS</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgritemflags?branch=master)<br/></td>
<td>Specifies information for the current item in the [<strong>SYNCMGRITEM</strong>](/windows/win32/Mobsync/ns-mobsync-_tagsyncmgritem?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRLOGLEVEL</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrloglevel?branch=master)<br/></td>
<td>The [<strong>SYNCMGRLOGLEVEL</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrloglevel?branch=master) enumeration values specify an error level for use in the [<strong>ISyncMgrSynchronizeCallback::LogError</strong>](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-logerror?branch=master) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRREGISTERFLAGS</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrregisterflags?branch=master)<br/></td>
<td>The [<strong>SYNCMGRREGISTERFLAGS</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrregisterflags?branch=master) enumeration values are used in methods of the [<strong>ISyncMgrRegister</strong>](/windows/win32/Mobsync/nn-mobsync-isyncmgrregister?branch=master) interface to identify events for which the handler is registered to be notified.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRSTATUS</strong>](/windows/win32/Mobsync/ne-mobsync-_tagsyncmgrstatus?branch=master)<br/></td>
<td>Used in the [<strong>ISyncMgrSynchronize::SetItemStatus</strong>](/windows/win32/Mobsync/nf-mobsync-isyncmgrsynchronize-setitemstatus?branch=master) method to specify the updated status for the item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>THUMBBUTTONFLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-thumbbuttonflags?branch=master)<br/></td>
<td>Used by [<strong>THUMBBUTTON</strong>](/windows/win32/Shobjidl_core/ns-shobjidl_core-thumbbutton?branch=master) to control specific states and behaviors of the button.<br/></td>
</tr>
<tr class="even">
<td>[<strong>THUMBBUTTONMASK</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-thumbbuttonmask?branch=master)<br/></td>
<td>Used by the [<strong>THUMBBUTTON</strong>](/windows/win32/Shobjidl_core/ns-shobjidl_core-thumbbutton?branch=master) structure to specify which members of that structure contain valid data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ThumbnailStreamCacheOptions</strong>](/windows/win32/thumbnailstreamcache/ne-thumbnailstreamcache-thumbnailstreamcacheoptions?branch=master)<br/></td>
<td>Defines the cache options used by the [<strong>IThumbnailStreamCache</strong>](/windows/win32/thumbnailstreamcache/nn-thumbnailstreamcache-ithumbnailstreamcache?branch=master) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>TRANSFER_SOURCE_FLAGS</strong>](/windows/win32/shobjidl_core/ne-shobjidl_core-_transfer_source_flags?branch=master)<br/></td>
<td>Used by methods of the [<strong>ITransferSource</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itransfersource?branch=master) and [<strong>ITransferDestination</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-itransferdestination?branch=master) interfaces to control their file operations.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TRANSLATEURL_IN_FLAGS</strong>](/windows/win32/Intshcut/ne-intshcut-translateurl_in_flags?branch=master)<br/></td>
<td>The [<strong>TRANSLATEURL_IN_FLAGS</strong>](/windows/win32/Intshcut/ne-intshcut-translateurl_in_flags?branch=master) enumerated values are used with the [<strong>TranslateURL</strong>](/windows/win32/Intshcut/nf-intshcut-translateurla?branch=master) function to determine how it will execute.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UNDOCK_REASON</strong>](/windows/win32/Shobjidl/ne-shobjidl-undock_reason?branch=master)<br/></td>
<td>Values that indicate the reason that a docked accessibility app window has been undocked. Used by [<strong>IAccessibilityDockingServiceCallback::Undocked</strong>](/windows/win32/Shobjidl/?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>URL_SCHEME</strong>](/windows/win32/Shlwapi/ne-shlwapi-url_scheme?branch=master)<br/></td>
<td>Used to specify URL schemes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>URLASSOCIATIONDIALOG_IN_FLAGS</strong>](/windows/win32/Intshcut/ne-intshcut-urlassociationdialog_in_flags?branch=master)<br/></td>
<td>The [<strong>URLASSOCIATIONDIALOG_IN_FLAGS</strong>](/windows/win32/Intshcut/ne-intshcut-urlassociationdialog_in_flags?branch=master) enumerated values are used with [<strong>URLAssociationDialog</strong>](/windows/win32/Intshcut/nf-intshcut-urlassociationdialoga?branch=master) to determine how it executes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>VPCOLORFLAGS</strong>](/windows/win32/Shobjidl/ne-shobjidl-vpcolorflags?branch=master)<br/></td>
<td>Specifies the use of a color. Used by [<strong>IVisualProperties</strong>](/windows/win32/Shobjidl/nn-shobjidl-ivisualproperties?branch=master) methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>VPWATERMARKFLAGS</strong>](/windows/win32/Shobjidl/ne-shobjidl-vpwatermarkflags?branch=master)<br/></td>
<td>Specifies watermark flags. Used by [<strong>IVisualProperties::SetWatermark</strong>](/windows/win32/Shobjidl/nf-shobjidl-ivisualproperties-setwatermark?branch=master).<br/></td>
</tr>
</tbody>
</table>



 

 

 




