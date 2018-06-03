---
Description: This section describes the Windows Shell Structures.
title: Shell Structures
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell Structures

This section describes the Windows Shell Structures.

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
<td>[<strong>AASHELLMENUFILENAME</strong>](/windows/desktop/api/Shlobj/ns-shlobj-tagaamenufilename)<br/></td>
<td>A variable-size structure that contains information about a menu file name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>AASHELLMENUITEM</strong>](/windows/desktop/api/Shlobj/ns-shlobj-tagaashellmenuitem)<br/></td>
<td>Contains information about a menu item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPBARDATA</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_appbardata)<br/></td>
<td>Contains information about a system appbar message.<br/></td>
</tr>
<tr class="even">
<td>[<strong>APPCATEGORYINFO</strong>](/windows/desktop/api/Appmgmt/ns-appmgmt-_appcategoryinfo)<br/></td>
<td>Provides application category information to Add/Remove Programs in Control Panel. The [<strong>APPCATEGORYINFOLIST</strong>](/windows/desktop/api/Appmgmt/ns-appmgmt-_appcategoryinfolist) structure is used create a complete list of categories for an application publisher.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPCATEGORYINFOLIST</strong>](/windows/desktop/api/Appmgmt/ns-appmgmt-_appcategoryinfolist)<br/></td>
<td>Provides a list of supported application categories from an application publisher to Add/Remove Programs in Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>APPINFODATA</strong>](/windows/desktop/api/Shappmgr/ns-shappmgr-_appinfodata)<br/></td>
<td>Provides information about a published application to the Add/Remove Programs Control Panel utility.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCIATIONELEMENT</strong>](/windows/desktop/api/Shellapi/ns-shellapi-associationelement)<br/></td>
<td>Defines information used by [<strong>AssocCreateForClasses</strong>](/windows/desktop/api/Shellapi/nf-shellapi-assoccreateforclasses) to retrieve an [<strong>IQueryAssociations</strong>](/windows/desktop/api/Shlwapi/) interface for a given file association.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BANDINFOSFB</strong>](/windows/desktop/api/Shlobj/ns-shlobj-bandinfosfb)<br/></td>
<td>Contains information about a folder band. This structure is used with the [<strong>IShellFolderBand::GetBandInfoSFB</strong>](/windows/desktop/api/Shlobj/) and [<strong>IShellFolderBand::SetBandInfoSFB</strong>](/windows/desktop/api/Shlobj/) methods.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BANDSITEINFO</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-tagbandsiteinfo)<br/></td>
<td>Contains information about a band site. This structure is used with the [<strong>IBandSite::GetBandSiteInfo</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ibandsite-getbandsiteinfo) and [<strong>IBandSite::SetBandSiteInfo</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ibandsite-setbandsiteinfo) methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BASEBROWSERDATA</strong>](/windows/desktop/api/Shdeprecated/ns-shdeprecated-basebrowserdatalh)<br/></td>
<td>Contains protected members of the base class. [<strong>BASEBROWSERDATA</strong>](/windows/desktop/api/Shdeprecated/ns-shdeprecated-basebrowserdatalh) defines the browser state and is used with [<strong>IBrowserService2::GetBaseBrowserData</strong>](/windows/desktop/api/Shdeprecated/nf-shdeprecated-ibrowserservice2-getbasebrowserdata) and [<strong>IBrowserService2::PutBaseBrowserData</strong>](/windows/desktop/api/Shdeprecated/nf-shdeprecated-ibrowserservice2-putbasebrowserdata).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BORDERWIDTHS</strong>](/windows/desktop/api/Oleidl/)<br/></td>
<td>Defines the coordinates of the upper-left and lower-right corners of a border rectangle.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BROWSEINFO</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_browseinfoa)<br/></td>
<td>Contains parameters for the [<strong>SHBrowseForFolder</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shbrowseforfoldera) function and receives information about the folder selected by the user.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CATEGORY_INFO</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-category_info)<br/></td>
<td>Contains category information. A component category is a group of logically-related Component Object Model (COM) classes that share a common category identifier (CATID).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CIDA</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_ida)<br/></td>
<td>Used with the [CFSTR_SHELLIDLIST](clipboard.md) clipboard format to transfer the pointer to an item identifier list (PIDL) of one or more Shell namespace objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_COLUMNINFO</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-cm_columninfo)<br/></td>
<td>Defines column information. Used by members of the [<strong>IColumnManager</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icolumnmanager) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CMINVOKECOMMANDINFO</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-_cminvokecommandinfo)<br/></td>
<td>Contains information needed by [<strong>IContextMenu::InvokeCommand</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand) to invoke a shortcut menu command.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CMINVOKECOMMANDINFOEX</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-_cminvokecommandinfoex)<br/></td>
<td>Contains extended information about a shortcut menu command. This structure is an extended version of [<strong>CMINVOKECOMMANDINFO</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-_cminvokecommandinfo) that allows the use of Unicode values.<br/></td>
</tr>
<tr class="even">
<td>[<strong>COMDLG_FILTERSPEC</strong>](/windows/desktop/api/Shtypes/ns-shtypes-_comdlg_filterspec)<br/></td>
<td>Used generically to filter elements.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>COMPONENT</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_tagcomponent)<br/></td>
<td>Used by Windows 2000 to hold information about a component. This structure replaces the [<strong>IE4COMPONENT</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_tagie4component) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>COMPONENTSOPT</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_tagcomponentsopt)<br/></td>
<td>Contains the desktop item options.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>COMPPOS</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_tagcomppos)<br/></td>
<td>Holds information about a component's position and size.<br/></td>
</tr>
<tr class="even">
<td>[<strong>COMPSTATEINFO</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_tagcompstateinfo)<br/></td>
<td>Used by Windows 2000 to hold information about a component's state.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CONFIRM_CONFLICT_ITEM</strong>](/windows/desktop/api/Syncmgr/ns-syncmgr-confirm_conflict_item)<br/></td>
<td>Defines conflict item structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CONFIRM_CONFLICT_RESULT_INFO</strong>](/windows/desktop/api/Syncmgr/ns-syncmgr-confirm_conflict_result_info)<br/></td>
<td>Defines conflict result information structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CPLINFO</strong>](/windows/desktop/api/Cpl/ns-cpl-tagcplinfo)<br/></td>
<td>Contains resource information and an application-defined value for a dialog box supported by a Control Panel application. The [<strong>CPlApplet</strong>](/windows/desktop/api/Cpl/nc-cpl-applet_proc) function of the Control Panel application returns this information to the Control Panel in response to a [<strong>CPL_INQUIRE</strong>](cpl-inquire.md) message.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION</strong>](/windows/desktop/api/Credentialprovider/ns-credentialprovider-_credential_provider_credential_serialization)<br/></td>
<td>Contains details about a credential.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR</strong>](/windows/desktop/api/Credentialprovider/ns-credentialprovider-_credential_provider_field_descriptor)<br/></td>
<td>Describes a single field in a credential. For example, a string or a user image.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CSFV</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_csfv)<br/></td>
<td>Used with the [<strong>SHCreateShellFolderViewEx</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreateshellfolderviewex) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DATABLOCK_HEADER</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-tagdatablockheader)<br/></td>
<td>Serves as the header for some of the extra data structures used by [<strong>IShellLinkDataList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinkdatalist).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEFCONTEXTMENU</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-defcontextmenu)<br/></td>
<td>Contains context menu information used by [<strong>SHCreateDefaultContextMenu</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DELEGATEITEMID</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-delegateitemid)<br/></td>
<td>Used by delegate folders in place of a standard [<strong>ITEMIDLIST</strong>](/windows/desktop/api/Shtypes/ns-shtypes-_itemidlist) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DETAILSINFO</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_detailsinfo)<br/></td>
<td>Contains detail information for a Shell folder item. Used with the [<strong>SFVM_GETDETAILSOF</strong>](sfvm-getdetailsof.md) notification.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DFMICS</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-dfmics)<br/></td>
<td>Contains additional arguments used by [<strong>DFM_INVOKECOMMANDEX</strong>](dfm-invokecommandex.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DLLVERSIONINFO</strong>](/windows/desktop/api/Shlwapi/ns-shlwapi-_dllversioninfo)<br/></td>
<td>Receives DLL-specific version information. It is used with the [<strong>DllGetVersion</strong>](/windows/desktop/api/Shlwapi/nc-shlwapi-dllgetversionproc) function. <br/>
<blockquote>
[!Note]<br />
In place of this structure, you can use the [<strong>DLLVERSIONINFO2</strong>](/windows/desktop/api/Shlwapi/ns-shlwapi-_dllversioninfo2) structure.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DLLVERSIONINFO2</strong>](/windows/desktop/api/Shlwapi/ns-shlwapi-_dllversioninfo2)<br/></td>
<td>Receives DLL-specific version information. It is used with the [<strong>DllGetVersion</strong>](/windows/desktop/api/Shlwapi/nc-shlwapi-dllgetversionproc) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DROPDESCRIPTION</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-dropdescription)<br/></td>
<td>Describes the image and accompanying text for a drop object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DROPFILES</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_dropfiles)<br/></td>
<td>Defines the [CF_HDROP](clipboard.md) clipboard format. The data that follows is a double null-terminated list of file names.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXP_DARWIN_LINK</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-exp_darwin_link)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinkdatalist). It holds the link's Windows Installer ID.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXP_PROPERTYSTORAGE</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-exp_propertystorage)<br/></td>
<td>Stores information about the Shell link state. This structure is used for extra data sections that are tagged with EXP_PROPERTYSTORAGE_SIG.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXP_SPECIAL_FOLDER</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-exp_special_folder)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinkdatalist). It holds special folder information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXP_SZ_LINK</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-exp_sz_link)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinkdatalist). It holds expandable environment strings for the icon or target.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXT_BUTTON</strong>](ext-button.md)<br/></td>
<td>Contains information about a button that a File Manager extension DLL is adding to the toolbar of File Manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXTRASEARCH</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-extrasearch)<br/></td>
<td>Used by an [<strong>IEnumExtraSearch</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumextrasearch) enumerator object to return information on the search objects supported by a Shell Folder object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FILE_ATTRIBUTES_ARRAY</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-file_attributes_array)<br/></td>
<td>Contains the clipboard format definition for CFSTR_FILE_ATTRIBUTES_ARRAY.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FILEDESCRIPTOR</strong>](/windows/desktop/api/Shlobj/ns-shlobj_core-_filedescriptora)<br/></td>
<td>Describes the properties of a file that is being copied by means of the clipboard during a Microsoft ActiveX [drag-and-drop](dragdrop.md) operation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FILEGROUPDESCRIPTOR</strong>](/windows/desktop/api/Shlobj/ns-shlobj_core-_filegroupdescriptora)<br/></td>
<td>Defines the CF_FILEGROUPDESCRIPTOR clipboard format.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FMS_GETDRIVEINFO</strong>](fms-getdriveinfo.md)<br/></td>
<td>Contains information about the drive selected in the active File Manager window (the directory window or the Search Results window).<br/></td>
</tr>
<tr class="even">
<td>[<strong>FMS_GETFILESEL</strong>](fms-getfilesel.md)<br/></td>
<td>Contains information about a selected file in the active File Manager window (the directory window or the Search Results window).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FMS_HELPSTRING</strong>](fms-helpstring.md)<br/></td>
<td>Contains information that File Manager uses to add a Help string for a menu or toolbar command item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FMS_LOAD</strong>](fms-load.md)<br/></td>
<td>Contains information that File Manager uses to add a custom menu provided by a File Manager extension DLL. The structure also provides a delta value that the extension DLL can use to manipulate the custom menu after File Manager has loaded the menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FMS_TOOLBARLOAD</strong>](fms-toolbarload.md)<br/></td>
<td>Contains information about custom buttons to be added to the File Manager toolbar. The buttons are provided by a File Manager extension DLL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FOLDERSETTINGS</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-foldersettings)<br/></td>
<td>Contains folder view information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FVSHOWINFO</strong>](/windows/desktop/api/Shlobj/ns-shlobj-fvshowinfo)<br/></td>
<td>Contains information that the file viewer uses to display a file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>HELPINFO</strong>](/windows/desktop/api/Winuser/ns-winuser-taghelpinfo)<br/></td>
<td>Contains information about an item for which context-sensitive Help has been requested.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HELPWININFO</strong>](/windows/desktop/api/Winuser/ns-winuser-taghelpwininfoa)<br/></td>
<td>Contains the size and position of either a primary or secondary Help window. An application can set this information by calling the [<strong>WinHelp</strong>](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function with the HELP_SETWINPOS value.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IE4COMPONENT</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_tagie4component)<br/></td>
<td>Used by Microsoft Internet Explorer 4.0 and Microsoft Internet Explorer 4.01 to hold information about a component. With Windows 2000, it is replaced by the [<strong>COMPONENT</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_tagcomponent) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITEMIDLIST</strong>](/windows/desktop/api/Shtypes/ns-shtypes-_itemidlist)<br/></td>
<td>Contains a list of item identifiers.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITEMSPACING</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_itemspacing)<br/></td>
<td>Stores the dimensions of the two possible sizes of icon spacing that are available for display: small and large. Used by [<strong>IShellFolderView::GetItemSpacing</strong>](/windows/desktop/api/shlobj_core/).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KNOWNFOLDER_DEFINITION</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-knownfolder_definition)<br/></td>
<td>Defines the specifics of a known folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>LOGFONT</strong>](/windows/desktop/api/dimm/ns-dimm-__midl___midl_itf_dimm_0000_0000_0003)<br/></td>
<td>Defines the attributes of a font.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MRUINFO</strong>](mruinfo.md)<br/></td>
<td>Contains information that defines a new most recently used (MRU) list. Used by [<strong>CreateMRUListW</strong>](createmrulist.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MULTIKEYHELP</strong>](/windows/desktop/api/Winuser/ns-winuser-tagmultikeyhelpa)<br/></td>
<td>Specifies a keyword to search for and the keyword table to be searched by Windows Help.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NC_ADDRESS</strong>](/windows/desktop/api/Shellapi/ns-shellapi-tagnc_address)<br/></td>
<td>Contains information that describes a network address.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NET_ADDRESS_INFO</strong>](/windows/desktop/api/Iphlpapi/)<br/></td>
<td>Describes a network address.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NEWCPLINFO</strong>](/windows/desktop/api/Cpl/ns-cpl-tagnewcplinfoa)<br/></td>
<td>Contains resource information and an application-defined value for a dialog box supported by a Control Panel application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NOTIFYICONDATA</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_notifyicondataa)<br/></td>
<td>Contains information that the system needs to display notifications in the notification area. Used by [<strong>Shell_NotifyIcon</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NOTIFYICONIDENTIFIER</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_notifyiconidentifier)<br/></td>
<td>Contains information used by [<strong>Shell_NotifyIconGetRect</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicongetrect) to identify the icon for which to retrieve the bounding rectangle.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NRESARRAY</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_nresarray)<br/></td>
<td>Defines the CF_NETRESOURCE clipboard format.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NSTCCUSTOMDRAW</strong>](/windows/desktop/api/Shobjidl/ns-shobjidl-nstccustomdraw)<br/></td>
<td>Custom draw structure used by [<strong>INameSpaceTreeControlCustomDraw</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl-inamespacetreecontrolcustomdraw) methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NT_CONSOLE_PROPS</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-nt_console_props)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinkdatalist). It holds console properties.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NT_FE_CONSOLE_PROPS</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-nt_fe_console_props)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinkdatalist). It holds the console's code page.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OPEN_PRINTER_PROPS_INFO</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_open_printer_props_infoa)<br/></td>
<td>Identifies a particular property sheet in a printer's property pages and whether that property sheet should be modal. Optionally used with the [<strong>SHInvokePrinterCommand</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shinvokeprintercommanda) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OPENASINFO</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_openasinfo)<br/></td>
<td>Stores information for the [<strong>SHOpenWithDialog</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shopenwithdialog) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OVERLAPPED</strong>](/windows/desktop/api/Shobjidl/ns-shobjidl-_overlapped)<br/></td>
<td>Contains information used in asynchronous (overlapped) input/output (I/O).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PARSEDURL</strong>](/windows/desktop/api/Shlwapi/ns-shlwapi-tagparsedurla)<br/></td>
<td>Used by the [<strong>ParseURL</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-parseurla) function to return the parsed URL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PERSIST_FOLDER_TARGET_INFO</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-_persist_folder_target_info)<br/></td>
<td>Specifies a folder shortcut's target folder and its attributes. This structure is used by [<strong>IPersistFolder3::GetFolderTargetInfo</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipersistfolder3-getfoldertargetinfo) and [<strong>IPersistFolder3::InitializeEx</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipersistfolder3-initializeex).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PREVIEWHANDLERFRAMEINFO</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-previewhandlerframeinfo)<br/></td>
<td>Accelerator table structure. Used by [<strong>IPreviewHandlerFrame::GetWindowContext</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipreviewhandlerframe-getwindowcontext).<br/></td>
</tr>
<tr class="even">
<td>[<strong>PROFILEINFO</strong>](/windows/desktop/api/Profinfo/ns-profinfo-_profileinfoa)<br/></td>
<td>Contains information used when loading or unloading a user profile.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PUBAPPINFO</strong>](/windows/desktop/api/Shappmgr/ns-shappmgr-_pubappinfo)<br/></td>
<td>Provides information about a published application from an application publisher to <strong>Add/Remove Programs</strong> in Control Panel.<br/></td>
</tr>
<tr class="even">
<td>[<strong>QCMINFO</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_qcminfo)<br/></td>
<td>Contains information for merging menu items into Windows Explorer menus.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>QITAB</strong>](/windows/desktop/api/Shlwapi/ns-shlwapi-qitab)<br/></td>
<td>Used by the [<strong>QISearch</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-qisearch) function to describe a single interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SERIALIZEDPROPERTYVALUE</strong>](/windows/desktop/api/Propidl/ns-propidl-tagserializedpropertyvalue)<br/></td>
<td>A range of memory of arbitrary type that represents a serialized [<strong>PROPVARIANT</strong>](https://msdn.microsoft.com/windows/desktop/e86cc279-826d-4767-8d96-fc8280060ea1) structure. Programs should not inspect the contents of a [<strong>SERIALIZEDPROPERTYVALUE</strong>](/windows/desktop/api/Propidl/ns-propidl-tagserializedpropertyvalue); instead, they should manipulate it with the [<strong>StgSerializePropVariant</strong>](https://msdn.microsoft.com/windows/desktop/c588e239-616f-4569-88b5-6bfb504cefa1) and [<strong>StgDeserializePropVariant</strong>](https://msdn.microsoft.com/windows/desktop/0517ef4d-e57c-4613-8d11-5e1eb14eb9fa) functions.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SFV_CREATE</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_sfv_create)<br/></td>
<td>This structure is used with the [<strong>SHCreateShellFolderView</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreateshellfolderview) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SFV_SETITEMPOS</strong>](/windows/desktop/api/Shlobj/ns-shlobj-_sfv_setitempos)<br/></td>
<td>Stores position information for an item. Used with message [<strong>SFVM_SETITEMPOS</strong>](sfvm-setitempos.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SFVM_HELPTOPIC_DATA</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_sfvm_helptopic_data)<br/></td>
<td>Contains the name of an HTML Help file and a topic in that file. Used with the [<strong>SFVM_GETHELPTOPIC</strong>](sfvm-gethelptopic.md) notification. This structure requires Unicode strings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SFVM_PROPPAGE_DATA</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_sfvm_proppage_data)<br/></td>
<td>Contains the details of a page to be added to an object's <strong>Properties</strong> sheet.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHARDAPPIDINFO</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-shardappidinfo)<br/></td>
<td>Contains data used by [<strong>SHAddToRecentDocs</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs) to identify both an item—in this case as an [<strong>IShellItem</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem)—and the process that it is associated with.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHARDAPPIDINFOIDLIST</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-shardappidinfoidlist)<br/></td>
<td>Contains data used by [<strong>SHAddToRecentDocs</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs) to identify both an item—in this case by an absolute PIDL—and the process that it is associated with.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHARDAPPIDINFOLINK</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-shardappidinfolink)<br/></td>
<td>Contains data used by [<strong>SHAddToRecentDocs</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs) to identify both an item, in this case through an [<strong>IShellLink</strong>](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka), and the process that it is associated with.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHChangeNotifyEntry</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_shchangenotifyentry)<br/></td>
<td>Contains and receives information for change notifications. This structure is used with the [<strong>SHChangeNotifyRegister</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotifyregister) function and the [<strong>SFVM_QUERYFSNOTIFY</strong>](sfvm-queryfsnotify.md) notification.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCOLUMNDATA</strong>](/windows/desktop/api/Shlobj/ns-shlobj-shcolumndata)<br/></td>
<td>Contains information that identifies a particular file. It is used by [<strong>IColumnProvider::GetItemData</strong>](/windows/desktop/api/Shlobj/) when requesting data for a particular file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCOLUMNID</strong>](/windows/desktop/api/Shobjidl/)<br/></td>
<td>Specifies the FMTID/PID identifier of a column that will be displayed by the Windows Explorer Details view. <br/>
<blockquote>
[!Note]<br />
As of Windows Vista, [<strong>SHCOLUMNID</strong>](/windows/desktop/api/Shobjidl/) is considered a legacy form and should not be used. In its place, use the [<strong>PROPERTYKEY</strong>](https://msdn.microsoft.com/windows/desktop/3f5f31af-f040-443b-9045-9761055381ea) structure.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCOLUMNINFO</strong>](/windows/desktop/api/Shlobj/ns-shlobj-shcolumninfo)<br/></td>
<td>Contains information about the properties of a column. It is used by [<strong>IColumnProvider::GetColumnInfo</strong>](/windows/desktop/api/Shlobj/).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCOLUMNINIT</strong>](/windows/desktop/api/Shlobj/ns-shlobj-shcolumninit)<br/></td>
<td>Passes initialization information to [<strong>IColumnProvider::Initialize</strong>](/windows/desktop/api/Shlobj/).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHDESCRIPTIONID</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_shdescriptionid)<br/></td>
<td>Receives item data in response to a call to [<strong>SHGetDataFromIDList</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetdatafromidlista).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHDRAGIMAGE</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-shdragimage)<br/></td>
<td>Contains the information needed to create a drag image.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHELL_ITEM_RESOURCE</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-shell_item_resource)<br/></td>
<td>Defines Shell item resource.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHELLDETAILS</strong>](/windows/desktop/api/Shtypes/ns-shtypes-_shelldetails)<br/></td>
<td>Reports detailed information on an item in a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHELLEXECUTEINFO</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_shellexecuteinfoa)<br/></td>
<td>Contains information used by [<strong>ShellExecuteEx</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHELLFLAGSTATE</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-shellflagstate)<br/></td>
<td>Contains a set of flags that indicate the current Shell settings. This structure is used with the [<strong>SHGetSettings</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetsettings) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHELLSTATE</strong>](/windows/desktop/api/Shlobj/ns-shlobj_core-shellstatea)<br/></td>
<td>Contains settings for the Shell's state. This structure is used with the [<strong>SHGetSetSettings</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetsetsettings) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHFILEINFO</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_shfileinfoa)<br/></td>
<td>Contains information about a file object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHFILEOPSTRUCT</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_shfileopstructa)<br/></td>
<td>Contains information that the [<strong>SHFileOperation</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa) function uses to perform file operations. <br/>
<blockquote>
[!Note]<br />
As of Windows Vista, the use of the [<strong>IFileOperation</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperation) interface is recommended over this function.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHFOLDERCUSTOMSETTINGS</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-shfoldercustomsettings)<br/></td>
<td>Holds custom folder settings. This structure is used with the [<strong>SHGetSetFolderCustomSettings</strong>](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetsetfoldercustomsettings) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHITEMID</strong>](/windows/desktop/api/Shtypes/ns-shtypes-_shitemid)<br/></td>
<td>Defines an item identifier.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHNAMEMAPPING</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_shnamemappinga)<br/></td>
<td>Contains the old and new path names for each file that was moved, copied, or renamed by the [<strong>SHFileOperation</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHQUERYRBINFO</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_shqueryrbinfo)<br/></td>
<td>Contains the size and item count information retrieved by the [<strong>SHQueryRecycleBin</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shqueryrecyclebina) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHSTOCKICONINFO</strong>](/windows/desktop/api/Shellapi/ns-shellapi-_shstockiconinfo)<br/></td>
<td>Receives information used to retrieve a stock Shell icon. This structure is used in a call [<strong>SHGetStockIconInfo</strong>](/windows/desktop/api/Shellapi/nf-shellapi-shgetstockiconinfo).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SLOWAPPINFO</strong>](/windows/desktop/api/Shappmgr/ns-shappmgr-_tagslowappinfo)<br/></td>
<td>Provides specialized application information to <strong>Add/Remove Programs</strong> in Control Panel. This structure is not applicable to published applications.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SMCSHCHANGENOTIFYSTRUCT</strong>](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-shcschangenotifystruct)<br/></td>
<td>Contains information about change notification. It is used by [<strong>IShellMenuCallback::CallbackSM</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SMDATA</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-tagsmdata)<br/></td>
<td>Contains information from a menu band.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SMINFO</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-tagsminfo)<br/></td>
<td>Contains information about an item from a menu band.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SOFTDISTINFO</strong>](/windows/desktop/api/Urlmon/ns-urlmon-_tagsoftdistinfo)<br/></td>
<td>Contains information about a software update.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SORTCOLUMN</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-sortcolumn)<br/></td>
<td>Stores information about how to sort a column that is displayed in the folder view.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STRRET</strong>](/windows/desktop/api/Shtypes/ns-shtypes-_strret)<br/></td>
<td>Contains strings returned from the [<strong>IShellFolder</strong>](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder) interface methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SV2CVW2_PARAMS</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-_sv2cvw2_params)<br/></td>
<td>Holds the parameters for the [<strong>IShellView2::CreateViewWindow2</strong>](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview2-createviewwindow2) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNC_HANDLER_ITEM_INFO</strong>](/windows/desktop/api/Syncmgr/)<br/></td>
<td>Defines a handler for a scheduled synchronization. Used with [<strong>ISyncSchedule::AddItem</strong>](/windows/desktop/api/Syncmgr/).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_CONFLICT_ID_INFO</strong>](/windows/desktop/api/Syncmgr/ns-syncmgr-syncmgr_conflict_id_info)<br/></td>
<td>Describes conflict ID information structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRHANDLERINFO</strong>](/windows/desktop/api/Mobsync/ns-mobsync-_tagsyncmgrhandlerinfo)<br/></td>
<td>Provides information about the handler for use in the [<strong>ISyncMgrSynchronize::GetHandlerInfo</strong>](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronize-gethandlerinfo) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRITEM</strong>](/windows/desktop/api/Mobsync/ns-mobsync-_tagsyncmgritem)<br/></td>
<td>Provides information about items being enumerated by the [<strong>ISyncMgrEnumItems</strong>](/windows/desktop/api/mobsync/nn-mobsync-isyncmgrenumitems) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRLOGERRORINFO</strong>](/windows/desktop/api/Mobsync/ns-mobsync-_tagsyncmgrlogerrorinfo)<br/></td>
<td>Provides error information for use in the [<strong>ISyncMgrSynchronizeCallback::LogError</strong>](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-logerror) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRPROGRESSITEM</strong>](/windows/desktop/api/Mobsync/ns-mobsync-_tagsyncmgrprogressitem)<br/></td>
<td>Provides status information while a synchronization is in progress. This structure is used with the [<strong>ISyncMgrSynchronizeCallback::Progress</strong>](/windows/desktop/api/Mobsync/nf-mobsync-isyncmgrsynchronizecallback-progress) method and corresponds to a single synchronization item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TBINFO</strong>](/windows/desktop/api/Shlobj/ns-shlobj-_tbinfo)<br/></td>
<td>Used with the [<strong>SFVM_GETBUTTONINFO</strong>](sfvm-getbuttoninfo.md) notification to specify the number of buttons to add to the toolbar, as well as how they're added.<br/></td>
</tr>
<tr class="even">
<td>[<strong>THUMBBUTTON</strong>](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-thumbbutton)<br/></td>
<td>Used by methods of the [<strong>ITaskbarList3</strong>](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist3) interface to define buttons used in a toolbar embedded in a window's thumbnail representation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WALLPAPEROPT</strong>](/windows/desktop/api/shlobj_core/ns-shlobj_core-_tagwallpaperopt)<br/></td>
<td>Contains the wallpaper display options. Used with members of the [<strong>IActiveDesktop</strong>](https://msdn.microsoft.com/windows/desktop/4d572b86-36e8-417b-857c-eb477c04c691) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>WINDOWDATA</strong>](/windows/desktop/api/Tlogstg/ns-tlogstg-_windowdata)<br/></td>
<td>Stores window data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WTS_CONTEXTFLAGS</strong>](/windows/desktop/api/Thumbcache/ne-thumbcache-wts_contextflags)<br/></td>
<td>Specifies the context of a thumbnail extraction. Used by [<strong>IThumbnailSettings::SetContext</strong>](/windows/desktop/api/Thumbcache/nf-thumbcache-ithumbnailsettings-setcontext).<br/></td>
</tr>
<tr class="even">
<td>[<strong>WTS_FLAGS</strong>](/windows/desktop/api/Thumbcache/ne-thumbcache-wts_flags)<br/></td>
<td>Values used by [<strong>IThumbnailCache::GetThumbnail</strong>](/windows/desktop/api/Thumbcache/nf-thumbcache-ithumbnailcache-getthumbnail) to specify options for the extraction and display of the thumbnail image.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WTS_THUMBNAILID</strong>](/windows/desktop/api/Thumbcache/ns-thumbcache-wts_thumbnailid)<br/></td>
<td>Contains a unique identifier for a thumbnail in the system thumbnail cache.<br/></td>
</tr>
</tbody>
</table>



 

 

 




