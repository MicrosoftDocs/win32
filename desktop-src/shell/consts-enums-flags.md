---
Description: This section describes the Windows Shell constants, enumerations, and flags.
title: Shell Constants, Enumerations, and Flags
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<td>[<strong>_SVGIO</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_svgio)<br/></td>
<td>Used with the [<strong>IFolderView::Items</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ifolderview-items), [<strong>IFolderView::ItemCount</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ifolderview-itemcount), and [<strong>IShellView::GetItemObject</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-getitemobject) methods to restrict or control the items in their collections.<br/></td>
</tr>
<tr class="even">
<td>[<strong>_SVSIF</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_svsif)<br/></td>
<td>Indicates flags used by [<strong>IFolderView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifolderview), [<strong>IFolderView2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifolderview2), [<strong>IShellView</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) and [<strong>IShellView2</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview2) to specify a type of selection to apply.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPACTIONFLAGS</strong>](/windows/desktop/api/Shappmgr/ne-shappmgr-_tagappactionflags)<br/></td>
<td>Specifies application management actions supported by an application publisher. These flags are bitmasks passed to [<strong>IShellApp::GetPossibleActions</strong>](/windows/desktop/api/Shappmgr/nf-shappmgr-ishellapp-getpossibleactions).<br/></td>
</tr>
<tr class="even">
<td>[<strong>APPINFODATAFLAGS</strong>](/windows/desktop/api/Shappmgr/ne-shappmgr-_tagappinfoflags)<br/></td>
<td>Specifies application information to return from [<strong>IShellApp::GetAppInfo</strong>](/windows/desktop/api/Shappmgr/nf-shappmgr-ishellapp-getappinfo). These flags are bitmasks used in the [<strong>dwMask</strong>](/windows/desktop/api/Shappmgr/ns-shappmgr-_appinfodata) member of the <strong>APPINFODATA</strong> structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPLICATION_VIEW_ORIENTATION</strong>](/windows/desktop/api/Shobjidl_core/ne-shobjidl_core-application_view_orientation)<br/></td>
<td>Defines the set of display orientation modes for a window (app view). Used by [<strong>IApplicationDesignModeSettings2::GetApplicationViewOrientation</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings2-getapplicationvieworientation) and [<strong>IApplicationDesignModeSettings2::SetApplicationViewOrientation</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings2-setapplicationvieworientation).<br/></td>
</tr>
<tr class="even">
<td>[<strong>APPLICATION_VIEW_SIZE_PREFERENCE</strong>](/windows/desktop/api/Shobjidl_core/ne-shobjidl_core-application_view_size_preference)<br/></td>
<td>Defines the set of possible general window (app view) size preferences. Used by [<strong>ILaunchSourceViewSizePreference::GetSourceViewSizePreference</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ilaunchsourceviewsizepreference-getsourceviewsizepreference) and [<strong>ILaunchTargetViewSizePreference::GetTargetViewSizePreference</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ilaunchtargetviewsizepreference-gettargetviewsizepreference).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPLICATION_VIEW_STATE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-application_view_state)<br/></td>
<td>Indicates the current view state of a Windows Store app. Used by [<strong>IApplicationDesignModeSettings::SetApplicationViewState</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings-setapplicationviewstate) and [<strong>IApplicationDesignModeSettings::IsApplicationViewStateSupported</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings-isapplicationviewstatesupported).<br/></td>
</tr>
<tr class="even">
<td>[<strong>ASSOCDATA</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-assocdata)<br/></td>
<td>Used by [<strong>IQueryAssociations::GetData</strong>](/windows/desktop/api/Shlwapi/) to define the type of data that is to be returned.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCF</strong>](/windows/desktop/api/Shlwapi/)<br/></td>
<td>Provides information to the [<strong>IQueryAssociations</strong>](/windows/desktop/api/Shlwapi/) interface methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ASSOCIATIONLEVEL</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-associationlevel)<br/></td>
<td>Specifies the source of the default association for a file name extension. Used by methods of the [<strong>IApplicationAssociationRegistration</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationassociationregistration) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCIATIONTYPE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-associationtype)<br/></td>
<td>Specifies the type of association for an application. Used by methods of the [<strong>IApplicationAssociationRegistration</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationassociationregistration) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ASSOCKEY</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-assockey)<br/></td>
<td>Specifies the type of key to be returned by [<strong>IQueryAssociations::GetKey</strong>](/windows/desktop/api/Shlwapi/).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCSTR</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-assocstr)<br/></td>
<td>Used by [<strong>IQueryAssociations::GetString</strong>](/windows/desktop/api/Shlwapi/) to define the type of string that is to be returned.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ATTACHMENT_ACTION</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-attachment_action)<br/></td>
<td>Provides a set of flags to be used with [<strong>IAttachmentExecute::Prompt</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iattachmentexecute-prompt) to indicate the action to be performed upon user confirmation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ATTACHMENT_PROMPT</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-attachment_prompt)<br/></td>
<td>Provides a set of flags to be used with [<strong>IAttachmentExecute::Prompt</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iattachmentexecute-prompt) to indicate the type of prompt UI to display.<br/></td>
</tr>
<tr class="even">
<td>[<strong>AUTOCOMPLETELISTOPTIONS</strong>](/windows/desktop/api/shlobj_core/ne-shlobj_core-_tagautocompletelistoptions)<br/></td>
<td>Specifies which objects are enumerated for autocompletion lists.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>AUTOCOMPLETEOPTIONS</strong>](/windows/desktop/api/Shldisp/ne-shldisp-_tagautocompleteoptions)<br/></td>
<td>Specifies values used by [<strong>IAutoComplete2::GetOptions</strong>](/windows/desktop/api/Shldisp/nf-shldisp-iautocomplete2-getoptions) and [<strong>IAutoComplete2::SetOptions</strong>](/windows/desktop/api/Shldisp/nf-shldisp-iautocomplete2-setoptions) for options surrounding autocomplete.<br/></td>
</tr>
<tr class="even">
<td>[<strong>Bind Context String Keys</strong>](str-constants.md)<br/></td>
<td>A set of string keys that are used with the [<strong>IBindCtx::RegisterObjectParam</strong>](https://msdn.microsoft.com/windows/desktop/7ee2b5b2-9b9c-41f1-8e58-7432ebc0f9ed) method to specify a bind context.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BNSTATE</strong>](/windows/desktop/api/Shdeprecated/ne-shdeprecated-tagbnstate)<br/></td>
<td>Deprecated. Used by [<strong>IBrowserService::SetNavigateState</strong>](/windows/desktop/api/Shdeprecated/nf-shdeprecated-ibrowserservice-setnavigatestate) and [<strong>IBrowserService::GetNavigateState</strong>](/windows/desktop/api/Shdeprecated/nf-shdeprecated-ibrowserservice-getnavigatestate) to specify navigation states.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BROWSERFRAMEOPTIONS</strong>](/windows/desktop/api/Shobjidl_core/ne-shobjidl_core-_browserframeoptions)<br/></td>
<td>Used with method [<strong>IBrowserFrameOptions::GetFrameOptions</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ibrowserframeoptions-getframeoptions).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CATEGORYINFO_FLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-categoryinfo_flags)<br/></td>
<td>Provides a set of flags for use with the [<strong>CATEGORY_INFO</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-category_info) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CATSORT_FLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-catsort_flags)<br/></td>
<td>Specifies methods for sorting category data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CDCONTROLSTATE</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Specifies the values that indicate whether a control is visible and enabled. Used by members of the [<strong>IFileDialogCustomize</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifiledialogcustomize) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_ENUM_FLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-cm_enum_flags)<br/></td>
<td>Used by members of the [<strong>IColumnManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icolumnmanager) interface to specify which set of columns are being requested, either all or only those currently visible.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_MASK</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-cm_mask)<br/></td>
<td>Indicates which values in the [<strong>CM_COLUMNINFO</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-cm_columninfo) structure should be set during calls to [<strong>IColumnManager::SetColumnInfo</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icolumnmanager-setcolumninfo).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CM_SET_WIDTH_VALUE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-cm_set_width_value)<br/></td>
<td>Specifies width values in pixels and includes special support for default and autosize. Used by members of the [<strong>IColumnManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icolumnmanager) interface through the [<strong>CM_COLUMNINFO</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-cm_columninfo) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_STATE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-cm_state)<br/></td>
<td>Specifies column state values. Used by members of the [<strong>IColumnManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icolumnmanager) interface through the [<strong>CM_COLUMNINFO</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-cm_columninfo) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS</strong>](/windows/desktop/api/CredentialProvider/ne-credentialprovider-credential_provider_account_options)<br/></td>
<td>Indicates the type of credential that a credential provider should return to associate with the &quot;Other user&quot; tile. Used by [<strong>ICredentialProviderUserArray_GetAccountOptions</strong>](/windows/desktop/api/CredentialProvider/nf-credentialprovider-icredentialprovideruserarray-getaccountoptions).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS</strong>](/windows/desktop/api/CredentialProvider/ne-credentialprovider-credential_provider_credential_field_options)<br/></td>
<td>Provides customization options for a single field in a logon or credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE</strong>](/windows/desktop/api/Credentialprovider/ne-credentialprovider-_credential_provider_field_interactive_state)<br/></td>
<td>Describes the state of a field and how it a user can interact with it. Fields can be displayed by a credential provider in a variety of different interactive states.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_STATE</strong>](/windows/desktop/api/Credentialprovider/ne-credentialprovider-_credential_provider_field_state)<br/></td>
<td>Specifies the state of a single field in the Credential UI.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_TYPE</strong>](/windows/desktop/api/Credentialprovider/ne-credentialprovider-_credential_provider_field_type)<br/></td>
<td>Specifies a type of credential field. Used by [<strong>CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR</strong>](/windows/desktop/api/Credentialprovider/ns-credentialprovider-_credential_provider_field_descriptor).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE</strong>](/windows/desktop/api/Credentialprovider/ne-credentialprovider-_credential_provider_get_serialization_response)<br/></td>
<td>Describes the response when a credential provider attempts to serialize credentials.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_STATUS_ICON</strong>](/windows/desktop/api/Credentialprovider/ne-credentialprovider-_credential_provider_status_icon)<br/></td>
<td>Indicates which status icon should be displayed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_USAGE_SCENARIO</strong>](/windows/desktop/api/Credentialprovider/ne-credentialprovider-_credential_provider_usage_scenario)<br/></td>
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
<td>Flags that control the calling function's behavior. Used by [<strong>SHCreateThread</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethread) and [<strong>SHCreateThreadWithHandle</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-shcreatethreadwithhandle). In those functions, these values are defined as being of type SHCT_FLAGS.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DATAOBJ_GET_ITEM_FLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-dataobj_get_item_flags)<br/></td>
<td>Values used by the [<strong>SHGetItemFromDataObject</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shgetitemfromdataobject) function to specify options concerning the processing of the source object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DBID Command Flags</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-tagdeskbandcid)<br/></td>
<td>These command IDs can be sent to the band object's container with [<strong>IOleCommandTarget::Exec</strong>](https://msdn.microsoft.com/windows/desktop/a2071ca9-8675-4f53-b30e-8c7198c2acca).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEF_SHARE_ID</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-def_share_id)<br/></td>
<td>Values that specify the folder being acted on by methods of the [<strong>ISharingConfigurationManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-isharingconfigurationmanager) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DEFAULTSAVEFOLDERTYPE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-defaultsavefoldertype)<br/></td>
<td>Specifies the default save location.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEFAULT_FOLDER_MENU_RESTRICTIONS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-default_folder_menu_restrictions)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>DESKTOP_WALLPAPER_POSITION</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-desktop_wallpaper_position)<br/></td>
<td>Specifies how the desktop wallpaper should be displayed.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEVICE_SCALE_FACTOR</strong>](/windows/desktop/api/Shtypes/ne-shtypes-device_scale_factor)<br/></td>
<td>Indicates a spoofed device scale factor, as a percent. Used by [<strong>IApplicationDesignModeSettings::SetApplicationViewState</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings-setapplicationviewstate) and [<strong>IApplicationDesignModeSettings::IsApplicationViewStateSupported</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdesignmodesettings-isapplicationviewstatesupported)<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DISPLAY_DEVICE_TYPE</strong>](/windows/desktop/api/ShellScalingAPI/ne-shellscalingapi-display_device_type)<br/></td>
<td>Indicates whether the device is a primary or immersive type of display.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DROPIMAGETYPE</strong>](/windows/desktop/api/shlobj_core/ne-shlobj_core-dropimagetype)<br/></td>
<td>Values used with the [<strong>DROPDESCRIPTION</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-dropdescription) structure to specify the drop image.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXPCMDSTATE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_expcmdstate)<br/></td>
<td>[<strong>EXPCMDSTATE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_expcmdstate) values represent the command state of a Shell item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXPLORER_BROWSER_FILL_FLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-explorer_browser_fill_flags)<br/></td>
<td>These flags are used with [<strong>IExplorerBrowser::FillFromObject</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iexplorerbrowser-fillfromobject).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXPLORER_BROWSER_OPTIONS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-explorer_browser_options)<br/></td>
<td>These flags are used with [<strong>IExplorerBrowser::GetOptions</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iexplorerbrowser-getoptions) and [<strong>IExplorerBrowser::SetOptions</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iexplorerbrowser-setoptions).<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXPLORERPANESTATE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_explorerpanestate)<br/></td>
<td>Indicate flags used by [<strong>IExplorerPaneVisibility::GetPaneState</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iexplorerpanevisibility-getpanestate) to get the current state of the given Windows Explorer pane.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FDAP</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-fdap)<br/></td>
<td>Specifies list placement.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FDE_OVERWRITE_RESPONSE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-fde_overwrite_response)<br/></td>
<td>Specifies the values used by the [<strong>IFileDialogEvents::OnOverwrite</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ifiledialogevents-onoverwrite) method to indicate an application's response to an overwrite request during a save operation using the common file dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FDE_SHAREVIOLATION_RESPONSE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-fde_shareviolation_response)<br/></td>
<td>Specifies the values used by the [<strong>IFileDialogEvents::OnShareViolation</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ifiledialogevents-onshareviolation) method to indicate an application's response to a sharing violation that occurs when a file is opened or saved.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FFFP_MODE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-fffp_mode)<br/></td>
<td>Describes match criteria. Used by methods of the [<strong>IKnownFolderManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iknownfoldermanager) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FILE_USAGE_TYPE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-file_usage_type)<br/></td>
<td>Constants used by [<strong>IFileIsInUse::GetUsage</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ifileisinuse-getusage) to indicate how a file in use is being used.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FILEOPENDIALOGOPTIONS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_fileopendialogoptions)<br/></td>
<td>Defines the set of options available to an Open or Save dialog.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FILETYPEATTRIBUTEFLAGS</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-filetypeattributeflags)<br/></td>
<td>Indicates [<strong>FILETYPEATTRIBUTEFLAGS</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-filetypeattributeflags) constants that are used in the EditFlags value of a file association [PROGID](fa-progids.md) registry key.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDER_ENUM_MODE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-folder_enum_mode)<br/></td>
<td>Used by [<strong>IObjectWithFolderEnumMode::GetMode</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iobjectwithfolderenummode-getmode) and [<strong>IObjectWithFolderEnumMode::SetMode</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iobjectwithfolderenummode-setmode) methods to get and set the display modes for the folders.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FOLDERFLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-folderflags)<br/></td>
<td>A set of flags that specify folder view options. The flags are independent of each other and can be used in any combination.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDERLOGICALVIEWMODE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-folderlogicalviewmode)<br/></td>
<td>Used by [<strong>IFolderViewSettings::GetViewMode</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ifolderviewsettings-getviewmode) and [<strong>ISearchFolderItemFactory::SetFolderLogicalViewMode</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-isearchfolderitemfactory-setfolderlogicalviewmode) to describe the view mode.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FOLDERTYPEID</strong>](foldertypeid.md)<br/></td>
<td>The [<strong>FOLDERTYPEID</strong>](foldertypeid.md) values represent a view template applied to a folder, usually based on its intended use and contents.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDERVIEWMODE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-folderviewmode)<br/></td>
<td>Specifies the folder view type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FOLDERVIEWOPTIONS</strong>](/windows/desktop/api/Shobjidl/ne-shobjidl-folderviewoptions)<br/></td>
<td>Used by methods of the [<strong>IFolderViewOptions</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ifolderviewoptions) interface to activate Windows Vista options not supported by default in Windows 7 and later systems as well as deactivating new Windows 7 options.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IActiveDesktop Flags</strong>](iactivedesktop-flags.md)<br/></td>
<td>This section describes the flags used by [<strong>IActiveDesktop</strong>](https://msdn.microsoft.com/windows/desktop/4d572b86-36e8-417b-857c-eb477c04c691) interface methods.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IESHORTCUTFLAGS</strong>](/windows/desktop/api/shlobj_core/ne-shlobj_core-tagieshortcutflags)<br/></td>
<td>Specifies how a shortcut should be handled by the browser.<br/></td>
</tr>
<tr class="even">
<td>[<strong>KF_CATEGORY</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-kf_category)<br/></td>
<td>Value that represent a category by which a folder registered with the Known Folder system can be classified.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KF_DEFINITION_FLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_kf_definition_flags)<br/></td>
<td>Flags that specify certain known folder behaviors. Used with the [<strong>KNOWNFOLDER_DEFINITION</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-knownfolder_definition) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>KF_REDIRECT_FLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_kf_redirect_flags)<br/></td>
<td>Flags used by [<strong>IKnownFolderManager::Redirect</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iknownfoldermanager-redirect) to specify details of a known folder redirection such as permissions and ownership for the redirected folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KF_REDIRECTION_CAPABILITIES</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_kf_redirection_capabilities)<br/></td>
<td>Flags that specify the current redirection capabilities of a known folder. Used by [<strong>IKnownFolder::GetRedirectionCapabilities</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iknownfolder-getredirectioncapabilities).<br/></td>
</tr>
<tr class="even">
<td>[<strong>KNOWN_FOLDER_FLAG</strong>](/windows/desktop/api/shlobj_core/ne-shlobj_core-known_folder_flag)<br/></td>
<td>Specify special retrieval options for known folders. These values supersede [<strong>CSIDL</strong>](csidl.md) values, which have parallel meanings.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KNOWNFOLDERID</strong>](knownfolderid.md)<br/></td>
<td>The [<strong>KNOWNFOLDERID</strong>](knownfolderid.md) constants represent GUIDs that identify standard folders registered with the system as [Known Folders](known-folders.md). These folders are installed with Windows Vista and later operating systems, and a computer will have only folders appropriate to it installed. For descriptions of these folders, see [<strong>CSIDL</strong>](csidl.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>LIBRARYFOLDERFILTER</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-libraryfolderfilter)<br/></td>
<td>Defines options for filtering folder items. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>LIBRARYMANAGEDIALOGOPTIONS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-librarymanagedialogoptions)<br/></td>
<td>Used by [<strong>SHShowManageLibraryUI</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shshowmanagelibraryui) to define options for handling a name collision when saving a library.<br/></td>
</tr>
<tr class="even">
<td>[<strong>LIBRARYOPTIONFLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-libraryoptionflags)<br/></td>
<td>Specifies the library options.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>LIBRARYSAVEFLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-librarysaveflags)<br/></td>
<td>Specifies the options for handling a name collision when saving a library. <br/></td>
</tr>
<tr class="even">
<td>[<strong>MIMEASSOCIATIONDIALOG_IN_FLAGS</strong>](/windows/desktop/api/Intshcut/ne-intshcut-mimeassociationdialog_in_flags)<br/></td>
<td>Used with the [<strong>MIMEAssociationDialog</strong>](/windows/desktop/api/Intshcut/nf-intshcut-mimeassociationdialoga) function to determine how it executes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MONITOR_APP_VISIBILITY</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-monitor_app_visibility)<br/></td>
<td>Specifies whether a display is showing desktop windows instead of Windows Store apps.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MP_POPUPFLAGS constants</strong>](mp-popupflags.md)<br/></td>
<td>Represent options available when displaying a pop-up menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NET_STRING</strong>](net-string.md)<br/></td>
<td>Represent network address types. Use one or more (as a bitwise combination) of the following constants to create a network address mask to use with the macro [<strong>NetAddr_SetAllowType</strong>](/windows/desktop/api/Shellapi/nf-shellapi-netaddr_setallowtype).<br/></td>
</tr>
<tr class="even">
<td>[<strong>NSTCFOLDERCAPABILITIES</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-nstcfoldercapabilities)<br/></td>
<td>Specifies the state of a tree item. These values are used by methods of the [<strong>INameSpaceTreeControlFolderCapabilities</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacetreecontrolfoldercapabilities) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NSTCITEMSTATE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_nstcitemstate)<br/></td>
<td>Specifies the state of a tree item. These values are used by methods of the [<strong>INameSpaceTreeControl</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-inamespacetreecontrol) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NSTCSTYLE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_nstcstyle)<br/></td>
<td>Describes the characteristics of a given namespace tree control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NSTCSTYLE2</strong>](/windows/desktop/api/Shobjidl/ne-shobjidl-nstcstyle2)<br/></td>
<td>Used by methods of the [<strong>INameSpaceTreeControl2</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-inamespacetreecontrol2) to specify extended display styles in a Shell namespace treeview.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NWMF</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-nwmf)<br/></td>
<td>Flags used by [<strong>INewWindowManager::EvaluateNewWindow</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-inewwindowmanager-evaluatenewwindow). These values are factors in the decision of whether to display a pop-up window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PACKAGE_EXECUTION_STATE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-package_execution_state)<br/></td>

</tr>
<tr class="even">
<td>[<strong>PERCEIVED</strong>](/windows/desktop/api/Shtypes/ne-shtypes-tagperceived)<br/></td>
<td>Specifies a file's perceived type. This set of constants is used in the [<strong>AssocGetPerceivedType</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-assocgetperceivedtype) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PUBAPPINFOFLAGS</strong>](/windows/desktop/api/Shappmgr/ne-shappmgr-_tagpublishedappinfoflags)<br/></td>
<td>Specifies which members in the [<strong>PUBAPPINFO</strong>](/windows/desktop/api/Shappmgr/ns-shappmgr-_pubappinfo) structure are valid. These flags are bitmasks set in the <strong>dwMask</strong> member and passed to [<strong>IPublishedApp::GetPublishedAppInfo</strong>](/windows/desktop/api/Shappmgr/nf-shappmgr-ipublishedapp-getpublishedappinfo).<br/></td>
</tr>
<tr class="even">
<td>[<strong>QUERY_USER_NOTIFICATION_STATE</strong>](/windows/desktop/api/Shellapi/ne-shellapi-query_user_notification_state)<br/></td>
<td>Specifies the state of the machine for the current user in relation to the propriety of sending a notification. Used by [<strong>SHQueryUserNotificationState</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shqueryusernotificationstate).<br/></td>
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
<td>[<strong>RESTRICTIONS</strong>](/windows/desktop/api/shlobj_core/ne-shlobj_core-restrictions)<br/></td>
<td>These flags are used with the [<strong>SHRestricted</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shrestricted) function. <strong>SHRestricted</strong> is used to determine whether a specified administrator policy is in effect. In many cases, applications need to modify certain behaviors in order to comply with the policies enacted by system administrators.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCALE_CHANGE_FLAGS</strong>](/windows/desktop/api/ShellScalingAPI/ne-shellscalingapi-scale_change_flags)<br/></td>
<td>Flags that are used to indicate the scaling change that occured.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SCNRT_STATUS</strong>](/windows/desktop/api/shlobj_core/ne-shlobj_core-scnrt_status)<br/></td>
<td>Indicates whether to enable or disable Async Register and Deregister for [<strong>SHChangeNotifyRegisterThread</strong>](/windows/desktop/api/Shlobj/nf-shlobj-shchangenotifyregisterthread).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SFBS_FLAGS</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-tagsfbs_flags)<br/></td>
<td>Specifies how the [<strong>StrFormatByteSizeEx</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-strformatbytesizeex) function should handle rounding of undisplayed digits.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SFGAO</strong>](sfgao.md)<br/></td>
<td>Attributes that can be retrieved on an item (file or folder) or set of items.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHARD</strong>](/windows/desktop/api/shlobj_core/ne-shlobj_core-shard)<br/></td>
<td>Indicates the interpretation of the data passed by [<strong>SHAddToRecentDocs</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs) in its <em>pv</em> parameter to identify the item whose usage statistics are being tracked.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHARE_ROLE</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-share_role)<br/></td>
<td>Specifies the access permissions assigned to the <strong>Users</strong> or <strong>Public</strong> folder. Used in [<strong>CreateShare</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-isharingconfigurationmanager-createshare) and [<strong>GetSharePermissions</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-isharingconfigurationmanager-getsharepermissions).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCOLSTATE</strong>](/windows/desktop/api/Shtypes/ne-shtypes-tagshcolstate)<br/></td>
<td>Describes how a property should be treated. These values are defined in Shtypes.h.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCONTF</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_shcontf)<br/></td>
<td>Determines the types of items included in an enumeration. These values are used with the [<strong>IShellFolder::EnumObjects</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-enumobjects) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHELL_LINK_DATA_FLAGS</strong>](/windows/desktop/api/shlobj_core/ne-shlobj_core-shell_link_data_flags)<br/></td>
<td>Specifies option settings. Used with [<strong>IShellLinkDataList::GetFlags</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelllinkdatalist-getflags) and [<strong>IShellLinkDataList::SetFlags</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelllinkdatalist-setflags).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHELL_UI_COMPONENT</strong>](/windows/desktop/api/ShellScalingApi/ne-shellscalingapi-shell_ui_component)<br/></td>
<td>Identifies the type of UI component that is needed in the shell.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellFolderViewOptions</strong>](/windows/desktop/api/Shldisp/ne-shldisp-shellfolderviewoptions)<br/></td>
<td>Specifies the view options returned by the [<strong>ViewOptions</strong>](shellfolderview-viewoptions.md) property.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellSpecialFolderConstants</strong>](/windows/desktop/api/Shldisp/ne-shldisp-shellspecialfolderconstants)<br/></td>
<td>Specifies unique, system-independent values that identify special folders. These folders are frequently used by applications but which may not have the same name or location on any given system. For example, the system folder can be &quot;C:\Windows&quot; on one system and &quot;C:\Winnt&quot; on another.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellWindowFindWindowOptions</strong>](/windows/desktop/api/ExDisp/ne-exdisp-shellwindowfindwindowoptions)<br/></td>
<td>Specifies options for finding window in the Shell windows collection. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellWindowTypeConstants</strong>](/windows/desktop/api/Exdisp/ne-exdisp-shellwindowtypeconstants)<br/></td>
<td>Specifies types of Shell windows.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGDNF</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_shgdnf)<br/></td>
<td>Defines the values used with the [<strong>IShellFolder::GetDisplayNameOf</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof) and [<strong>IShellFolder::SetNameOf</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-setnameof) methods to specify the type of file or folder names used by those methods. <br/>
<blockquote>
[!Note]<br />
Prior to Windows 7, these values were packaged as the SHGNO enumeration.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGLOBALCOUNTER</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-shglobalcounter)<br/></td>
<td>Identifiers for various global counters, or shared variables. Each global counter can be incremented or decremented using [<strong>SHGlobalCounterIncrement</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-shglobalcounterincrement) and [<strong>SHGlobalCounterDecrement</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-shglobalcounterdecrement).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHREGDEL_FLAGS</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-shregdel_flags)<br/></td>
<td>Provides a set of values that indicate from which base key an item will be deleted.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHREGENUM_FLAGS</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-shregenum_flags)<br/></td>
<td>Provides a set of values that indicate the base key that will be used for an enumeration.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHSTOCKICONID</strong>](/windows/desktop/api/Shellapi/ne-shellapi-shstockiconid)<br/></td>
<td>Used by [<strong>SHGetStockIconInfo</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shgetstockiconinfo) to identify which stock system icon to retrieve.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SICHINTF</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_sichintf)<br/></td>
<td>Used to determine how to compare two Shell items. [<strong>IShellItem::Compare</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-compare) uses this enumerated type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SIGDN</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_sigdn)<br/></td>
<td>Requests the form of an item's display name to retrieve through [<strong>IShellItem::GetDisplayName</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-getdisplayname) and [<strong>SHGetNameFromIDList</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shgetnamefromidlist).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SPACTION</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_spaction)<br/></td>
<td>Describes an action being performed that requires progress to be shown to the user using an [<strong>IActionProgress</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iactionprogress) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SPBEGINF</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_spbeginf)<br/></td>
<td>Used by [<strong>IActionProgress::Begin</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iactionprogress-begin), these constants specify certain UI operations that are to be enabled or disabled.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SPTEXT</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_sptext)<br/></td>
<td>Specifies the type of descriptive text being provided to an [<strong>IActionProgress</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iactionprogress) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SRRF</strong>](srrf.md)<br/></td>
<td>Flags that restrict the data to be set or returned.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SSF Constants</strong>](ssf-constants.md)<br/></td>
<td>Used by the [<strong>SHGetSetSettings</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetsetsettings) function to specify which members of its [<strong>SHELLSTATE</strong>](/windows/desktop/api/Shlobj/ns-shlobj_core-shellstatea) structure should be set or retrived.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STPFLAG</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-stpflag)<br/></td>
<td>Used by the [<strong>ITaskbarList4::SetTabProperties</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist4-settabproperties) method to specify tab properties.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SVUIA_STATUS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-svuia_status)<br/></td>
<td>Used with the [<strong>IBrowserService2::_UIActivateView</strong>](/windows/desktop/api/Shdeprecated/nf-shdeprecated-ibrowserservice2-_uiactivateview) method to set the state of a browser view.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_CANCEL_REQUEST</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_cancel_request)<br/></td>
<td>Describes a request by the user to cancel a synchronization.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_CONFLICT_ITEM_TYPE</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_conflict_item_type)<br/></td>
<td>Describes conflict item type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_CONTROL_FLAGS</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_control_flags)<br/></td>
<td>Specifies how an operation requested on certain methods of [<strong>ISyncMgrControl</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrcontrol) should be performed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_EVENT_FLAGS</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_event_flags)<br/></td>
<td>Specifies flags for a synchronization event.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_EVENT_LEVEL</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_event_level)<br/></td>
<td>Specifies the type of event being reported to Sync Center.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_HANDLER_CAPABILITIES</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_handler_capabilities)<br/></td>
<td>Specifies the capabilities of a handler regarding the actions that can be performed against it.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_HANDLER_POLICIES</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_handler_policies)<br/></td>
<td>Enumerates policies specified by a sync handler that deviate from the default policy.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_HANDLER_TYPE</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_handler_type)<br/></td>
<td>Specifies the type of a handler. Used by [<strong>ISyncMgrHandlerInfo::GetType</strong>](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrhandlerinfo-gettype).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_ITEM_CAPABILITIES</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_item_capabilities)<br/></td>
<td>Specifies the actions that can be performed against an item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_ITEM_POLICIES</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_item_policies)<br/></td>
<td>Specifies an item's policies to control how they can be enabled or disabled by group policy.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_PRESENTER_CHOICE</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_presenter_choice)<br/></td>
<td>Describes what choice a user makes about a sync manager conflict resolution. Used by [<strong>ISyncMgrConflictPresenter</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrconflictpresenter).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_PRESENTER_NEXT_STEP</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_presenter_next_step)<br/></td>
<td>Describes the next step that is to occur in sync manager conflict resolution. Used by [<strong>ISyncMgrConflictPresenter</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrconflictpresenter).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_PROGRESS_STATUS</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_progress_status)<br/></td>
<td>Specifies the current progress status of a synchronization process. Used by [<strong>ISyncMgrSyncCallback::ReportProgress</strong>](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrsynccallback-reportprogress).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_RESOLUTION_ABILITIES</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_resolution_abilities)<br/></td>
<td>Indicates abilities and the conflict resolution activity to follow. Used with [<strong>ISyncMgrResolutionHandler::QueryAbilities</strong>](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrresolutionhandler-queryabilities).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_RESOLUTION_FEEDBACK</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_resolution_feedback)<br/></td>
<td>Describes Sync Manager resolution feedback. Used by [<strong>ISyncMgrResolutionHandler</strong>](/windows/desktop/api/Syncmgr/nn-syncmgr-isyncmgrresolutionhandler).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGR_SYNC_CONTROL_FLAGS</strong>](/windows/desktop/api/Syncmgr/ne-syncmgr-syncmgr_sync_control_flags)<br/></td>
<td>Indicates flags used by [<strong>ISyncMgrControl::StartHandlerSync</strong>](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrcontrol-starthandlersync) and [<strong>ISyncMgrControl::StartItemSync</strong>](/windows/desktop/api/Syncmgr/nf-syncmgr-isyncmgrcontrol-startitemsync).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRFLAG</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrflag)<br/></td>
<td>The [<strong>SYNCMGRFLAG</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrflag) enumeration values are used in the [<strong>ISyncMgrSynchronize::Initialize</strong>](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronize-initialize) method to indicate how the synchronization event was initiated.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRHANDLERFLAGS</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrhandlerflags)<br/></td>
<td>Used in the [<strong>SYNCMGRHANDLERINFO</strong>](/windows/desktop/api/Mobsync/ns-mobsync-_tagsyncmgrhandlerinfo) structure as flags that apply to the current handler.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRINVOKEFLAGS</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrinvokeflags)<br/></td>
<td>The [<strong>SYNCMGRINVOKEFLAGS</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrinvokeflags) enumeration value specifies how the Sync Manager is to be invoked in the [<strong>ISyncMgrSynchronizeInvoke::UpdateItems</strong>](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronizeinvoke-updateitems) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRITEMFLAGS</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgritemflags)<br/></td>
<td>Specifies information for the current item in the [<strong>SYNCMGRITEM</strong>](/windows/desktop/api/Mobsync/ns-mobsync-_tagsyncmgritem) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRLOGLEVEL</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrloglevel)<br/></td>
<td>The [<strong>SYNCMGRLOGLEVEL</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrloglevel) enumeration values specify an error level for use in the [<strong>ISyncMgrSynchronizeCallback::LogError</strong>](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-logerror) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRREGISTERFLAGS</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrregisterflags)<br/></td>
<td>The [<strong>SYNCMGRREGISTERFLAGS</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrregisterflags) enumeration values are used in methods of the [<strong>ISyncMgrRegister</strong>](/windows/desktop/api/Mobsync/nn-mobsync-isyncmgrregister) interface to identify events for which the handler is registered to be notified.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRSTATUS</strong>](/windows/desktop/api/Mobsync/ne-mobsync-_tagsyncmgrstatus)<br/></td>
<td>Used in the [<strong>ISyncMgrSynchronize::SetItemStatus</strong>](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronize-setitemstatus) method to specify the updated status for the item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>THUMBBUTTONFLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-thumbbuttonflags)<br/></td>
<td>Used by [<strong>THUMBBUTTON</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-thumbbutton) to control specific states and behaviors of the button.<br/></td>
</tr>
<tr class="even">
<td>[<strong>THUMBBUTTONMASK</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-thumbbuttonmask)<br/></td>
<td>Used by the [<strong>THUMBBUTTON</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-thumbbutton) structure to specify which members of that structure contain valid data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ThumbnailStreamCacheOptions</strong>](/windows/desktop/api/thumbnailstreamcache/ne-thumbnailstreamcache-thumbnailstreamcacheoptions)<br/></td>
<td>Defines the cache options used by the [<strong>IThumbnailStreamCache</strong>](/windows/desktop/api/thumbnailstreamcache/nn-thumbnailstreamcache-ithumbnailstreamcache) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>TRANSFER_SOURCE_FLAGS</strong>](/windows/desktop/api/shobjidl_core/ne-shobjidl_core-_transfer_source_flags)<br/></td>
<td>Used by methods of the [<strong>ITransferSource</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itransfersource) and [<strong>ITransferDestination</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itransferdestination) interfaces to control their file operations.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TRANSLATEURL_IN_FLAGS</strong>](/windows/desktop/api/Intshcut/ne-intshcut-translateurl_in_flags)<br/></td>
<td>The [<strong>TRANSLATEURL_IN_FLAGS</strong>](/windows/desktop/api/Intshcut/ne-intshcut-translateurl_in_flags) enumerated values are used with the [<strong>TranslateURL</strong>](/windows/desktop/api/Intshcut/nf-intshcut-translateurla) function to determine how it will execute.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UNDOCK_REASON</strong>](/windows/desktop/api/Shobjidl/ne-shobjidl-undock_reason)<br/></td>
<td>Values that indicate the reason that a docked accessibility app window has been undocked. Used by [<strong>IAccessibilityDockingServiceCallback::Undocked</strong>](/windows/desktop/api/Shobjidl/).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>URL_SCHEME</strong>](/windows/desktop/api/Shlwapi/ne-shlwapi-url_scheme)<br/></td>
<td>Used to specify URL schemes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>URLASSOCIATIONDIALOG_IN_FLAGS</strong>](/windows/desktop/api/Intshcut/ne-intshcut-urlassociationdialog_in_flags)<br/></td>
<td>The [<strong>URLASSOCIATIONDIALOG_IN_FLAGS</strong>](/windows/desktop/api/Intshcut/ne-intshcut-urlassociationdialog_in_flags) enumerated values are used with [<strong>URLAssociationDialog</strong>](/windows/desktop/api/Intshcut/nf-intshcut-urlassociationdialoga) to determine how it executes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>VPCOLORFLAGS</strong>](/windows/desktop/api/Shobjidl/ne-shobjidl-vpcolorflags)<br/></td>
<td>Specifies the use of a color. Used by [<strong>IVisualProperties</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-ivisualproperties) methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>VPWATERMARKFLAGS</strong>](/windows/desktop/api/Shobjidl/ne-shobjidl-vpwatermarkflags)<br/></td>
<td>Specifies watermark flags. Used by [<strong>IVisualProperties::SetWatermark</strong>](/windows/desktop/api/Shobjidl/nf-shobjidl-ivisualproperties-setwatermark).<br/></td>
</tr>
</tbody>
</table>



 

 

 




