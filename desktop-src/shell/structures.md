---
Description: 'This section describes the Windows Shell Structures.'
title: Shell Structures
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
<td>[<strong>AASHELLMENUFILENAME</strong>](aashellmenufilename-str.md)<br/></td>
<td>A variable-size structure that contains information about a menu file name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>AASHELLMENUITEM</strong>](aashellmenuitem-str.md)<br/></td>
<td>Contains information about a menu item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPBARDATA</strong>](appbardata.md)<br/></td>
<td>Contains information about a system appbar message.<br/></td>
</tr>
<tr class="even">
<td>[<strong>APPCATEGORYINFO</strong>](appcategoryinfo.md)<br/></td>
<td>Provides application category information to Add/Remove Programs in Control Panel. The [<strong>APPCATEGORYINFOLIST</strong>](appcategoryinfolist.md) structure is used create a complete list of categories for an application publisher.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPCATEGORYINFOLIST</strong>](appcategoryinfolist.md)<br/></td>
<td>Provides a list of supported application categories from an application publisher to Add/Remove Programs in Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>APPINFODATA</strong>](appinfodata.md)<br/></td>
<td>Provides information about a published application to the Add/Remove Programs Control Panel utility.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ASSOCIATIONELEMENT</strong>](associationelement.md)<br/></td>
<td>Defines information used by [<strong>AssocCreateForClasses</strong>](assoccreateforclasses.md) to retrieve an [<strong>IQueryAssociations</strong>](iqueryassociations.md) interface for a given file association.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BANDINFOSFB</strong>](bandinfosfb.md)<br/></td>
<td>Contains information about a folder band. This structure is used with the [<strong>IShellFolderBand::GetBandInfoSFB</strong>](ishellfolderband-getbandinfosfb.md) and [<strong>IShellFolderBand::SetBandInfoSFB</strong>](ishellfolderband-setbandinfosfb.md) methods.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BANDSITEINFO</strong>](bandsiteinfo.md)<br/></td>
<td>Contains information about a band site. This structure is used with the [<strong>IBandSite::GetBandSiteInfo</strong>](ibandsite-getbandsiteinfo.md) and [<strong>IBandSite::SetBandSiteInfo</strong>](ibandsite-setbandsiteinfo.md) methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BASEBROWSERDATA</strong>](basebrowserdata.md)<br/></td>
<td>Contains protected members of the base class. [<strong>BASEBROWSERDATA</strong>](basebrowserdata.md) defines the browser state and is used with [<strong>IBrowserService2::GetBaseBrowserData</strong>](ibrowserservice2-getbasebrowserdata.md) and [<strong>IBrowserService2::PutBaseBrowserData</strong>](ibrowserservice2-putbasebrowserdata.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BORDERWIDTHS</strong>](borderwidths.md)<br/></td>
<td>Defines the coordinates of the upper-left and lower-right corners of a border rectangle.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BROWSEINFO</strong>](browseinfo.md)<br/></td>
<td>Contains parameters for the [<strong>SHBrowseForFolder</strong>](shbrowseforfolder.md) function and receives information about the folder selected by the user.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CATEGORY_INFO</strong>](category-info.md)<br/></td>
<td>Contains category information. A component category is a group of logically-related Component Object Model (COM) classes that share a common category identifier (CATID).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CIDA</strong>](cida.md)<br/></td>
<td>Used with the [CFSTR_SHELLIDLIST](clipboard.md) clipboard format to transfer the pointer to an item identifier list (PIDL) of one or more Shell namespace objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CM_COLUMNINFO</strong>](cm-columninfo.md)<br/></td>
<td>Defines column information. Used by members of the [<strong>IColumnManager</strong>](icolumnmanager.md) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CMINVOKECOMMANDINFO</strong>](cminvokecommandinfo.md)<br/></td>
<td>Contains information needed by [<strong>IContextMenu::InvokeCommand</strong>](icontextmenu-invokecommand.md) to invoke a shortcut menu command.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CMINVOKECOMMANDINFOEX</strong>](cminvokecommandinfoex.md)<br/></td>
<td>Contains extended information about a shortcut menu command. This structure is an extended version of [<strong>CMINVOKECOMMANDINFO</strong>](cminvokecommandinfo.md) that allows the use of Unicode values.<br/></td>
</tr>
<tr class="even">
<td>[<strong>COMDLG_FILTERSPEC</strong>](comdlg-filterspec.md)<br/></td>
<td>Used generically to filter elements.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>COMPONENT</strong>](component.md)<br/></td>
<td>Used by Windows 2000 to hold information about a component. This structure replaces the [<strong>IE4COMPONENT</strong>](ie4component.md) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>COMPONENTSOPT</strong>](componentsopt.md)<br/></td>
<td>Contains the desktop item options.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>COMPPOS</strong>](comppos.md)<br/></td>
<td>Holds information about a component's position and size.<br/></td>
</tr>
<tr class="even">
<td>[<strong>COMPSTATEINFO</strong>](compstateinfo.md)<br/></td>
<td>Used by Windows 2000 to hold information about a component's state.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CONFIRM_CONFLICT_ITEM</strong>](confirm-conflict-item.md)<br/></td>
<td>Defines conflict item structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CONFIRM_CONFLICT_RESULT_INFO</strong>](confirm-conflict-result-info.md)<br/></td>
<td>Defines conflict result information structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CPLINFO</strong>](cplinfo.md)<br/></td>
<td>Contains resource information and an application-defined value for a dialog box supported by a Control Panel application. The [<strong>CPlApplet</strong>](cplapplet.md) function of the Control Panel application returns this information to the Control Panel in response to a [<strong>CPL_INQUIRE</strong>](cpl-inquire.md) message.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION</strong>](credential-provider-credential-serialization.md)<br/></td>
<td>Contains details about a credential.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR</strong>](credential-provider-field-descriptor.md)<br/></td>
<td>Describes a single field in a credential. For example, a string or a user image.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CSFV</strong>](csfv.md)<br/></td>
<td>Used with the [<strong>SHCreateShellFolderViewEx</strong>](shcreateshellfolderviewex.md) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DATABLOCK_HEADER</strong>](datablock-header-str.md)<br/></td>
<td>Serves as the header for some of the extra data structures used by [<strong>IShellLinkDataList</strong>](ishelllinkdatalist.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEFCONTEXTMENU</strong>](defcontextmenu.md)<br/></td>
<td>Contains context menu information used by [<strong>SHCreateDefaultContextMenu</strong>](shcreatedefaultcontextmenu.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DELEGATEITEMID</strong>](delegateitemid.md)<br/></td>
<td>Used by delegate folders in place of a standard [<strong>ITEMIDLIST</strong>](itemidlist.md) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DETAILSINFO</strong>](detailsinfo.md)<br/></td>
<td>Contains detail information for a Shell folder item. Used with the [<strong>SFVM_GETDETAILSOF</strong>](sfvm-getdetailsof.md) notification.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DFMICS</strong>](dfmics.md)<br/></td>
<td>Contains additional arguments used by [<strong>DFM_INVOKECOMMANDEX</strong>](dfm-invokecommandex.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>DLLVERSIONINFO</strong>](dllversioninfo-0rjh.md)<br/></td>
<td>Receives DLL-specific version information. It is used with the [<strong>DllGetVersion</strong>](dllgetversion.md) function. <br/>
<blockquote>
[!Note]<br />
In place of this structure, you can use the [<strong>DLLVERSIONINFO2</strong>](dllversioninfo2-0rjh.md) structure.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DLLVERSIONINFO2</strong>](dllversioninfo2-0rjh.md)<br/></td>
<td>Receives DLL-specific version information. It is used with the [<strong>DllGetVersion</strong>](dllgetversion.md) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DROPDESCRIPTION</strong>](dropdescription.md)<br/></td>
<td>Describes the image and accompanying text for a drop object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DROPFILES</strong>](dropfiles.md)<br/></td>
<td>Defines the [CF_HDROP](clipboard.md) clipboard format. The data that follows is a double null-terminated list of file names.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXP_DARWIN_LINK</strong>](exp-darwin-link-str.md)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](ishelllinkdatalist.md). It holds the link's Windows Installer ID.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXP_PROPERTYSTORAGE</strong>](exp-propertystorage.md)<br/></td>
<td>Stores information about the Shell link state. This structure is used for extra data sections that are tagged with EXP_PROPERTYSTORAGE_SIG.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXP_SPECIAL_FOLDER</strong>](exp-special-folder-str.md)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](ishelllinkdatalist.md). It holds special folder information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXP_SZ_LINK</strong>](exp-sz-link-str.md)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](ishelllinkdatalist.md). It holds expandable environment strings for the icon or target.<br/></td>
</tr>
<tr class="even">
<td>[<strong>EXT_BUTTON</strong>](ext-button.md)<br/></td>
<td>Contains information about a button that a File Manager extension DLL is adding to the toolbar of File Manager.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>EXTRASEARCH</strong>](extrasearch.md)<br/></td>
<td>Used by an [<strong>IEnumExtraSearch</strong>](ienumextrasearch.md) enumerator object to return information on the search objects supported by a Shell Folder object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FILE_ATTRIBUTES_ARRAY</strong>](file-attributes-array.md)<br/></td>
<td>Contains the clipboard format definition for CFSTR_FILE_ATTRIBUTES_ARRAY.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FILEDESCRIPTOR</strong>](filedescriptor.md)<br/></td>
<td>Describes the properties of a file that is being copied by means of the clipboard during a Microsoft ActiveX [drag-and-drop](dragdrop.md) operation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FILEGROUPDESCRIPTOR</strong>](filegroupdescriptor.md)<br/></td>
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
<td>[<strong>FOLDERSETTINGS</strong>](foldersettings.md)<br/></td>
<td>Contains folder view information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FVSHOWINFO</strong>](fvshowinfo.md)<br/></td>
<td>Contains information that the file viewer uses to display a file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>HELPINFO</strong>](helpinfo-str.md)<br/></td>
<td>Contains information about an item for which context-sensitive Help has been requested.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HELPWININFO</strong>](helpwininfo-str.md)<br/></td>
<td>Contains the size and position of either a primary or secondary Help window. An application can set this information by calling the [<strong>WinHelp</strong>](winhelp.md) function with the HELP_SETWINPOS value.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IE4COMPONENT</strong>](ie4component.md)<br/></td>
<td>Used by Microsoft Internet Explorer 4.0 and Microsoft Internet Explorer 4.01 to hold information about a component. With Windows 2000, it is replaced by the [<strong>COMPONENT</strong>](component.md) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ITEMIDLIST</strong>](itemidlist.md)<br/></td>
<td>Contains a list of item identifiers.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ITEMSPACING</strong>](itemspacing.md)<br/></td>
<td>Stores the dimensions of the two possible sizes of icon spacing that are available for display: small and large. Used by [<strong>IShellFolderView::GetItemSpacing</strong>](ishellfolderview-getitemspacing.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>KNOWNFOLDER_DEFINITION</strong>](knownfolder-definition.md)<br/></td>
<td>Defines the specifics of a known folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>LOGFONT</strong>](logfont.md)<br/></td>
<td>Defines the attributes of a font.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MRUINFO</strong>](mruinfo.md)<br/></td>
<td>Contains information that defines a new most recently used (MRU) list. Used by [<strong>CreateMRUListW</strong>](createmrulist.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>MULTIKEYHELP</strong>](multikeyhelp-str.md)<br/></td>
<td>Specifies a keyword to search for and the keyword table to be searched by Windows Help.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NC_ADDRESS</strong>](nc-address.md)<br/></td>
<td>Contains information that describes a network address.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NET_ADDRESS_INFO</strong>](net-address-info.md)<br/></td>
<td>Describes a network address.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NEWCPLINFO</strong>](newcplinfo.md)<br/></td>
<td>Contains resource information and an application-defined value for a dialog box supported by a Control Panel application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NOTIFYICONDATA</strong>](notifyicondata.md)<br/></td>
<td>Contains information that the system needs to display notifications in the notification area. Used by [<strong>Shell_NotifyIcon</strong>](shell-notifyicon.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NOTIFYICONIDENTIFIER</strong>](notifyiconidentifier.md)<br/></td>
<td>Contains information used by [<strong>Shell_NotifyIconGetRect</strong>](shell-notifyicongetrect.md) to identify the icon for which to retrieve the bounding rectangle.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NRESARRAY</strong>](nresarray.md)<br/></td>
<td>Defines the CF_NETRESOURCE clipboard format.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NSTCCUSTOMDRAW</strong>](nstccustomdraw.md)<br/></td>
<td>Custom draw structure used by [<strong>INameSpaceTreeControlCustomDraw</strong>](inamespacetreecontrolcustomdraw.md) methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NT_CONSOLE_PROPS</strong>](nt-console-props-str.md)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](ishelllinkdatalist.md). It holds console properties.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NT_FE_CONSOLE_PROPS</strong>](nt-fe-console-props-str.md)<br/></td>
<td>Holds an extra data block used by [<strong>IShellLinkDataList</strong>](ishelllinkdatalist.md). It holds the console's code page.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OPEN_PRINTER_PROPS_INFO</strong>](open-printer-props-info.md)<br/></td>
<td>Identifies a particular property sheet in a printer's property pages and whether that property sheet should be modal. Optionally used with the [<strong>SHInvokePrinterCommand</strong>](shinvokeprintercommand.md) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OPENASINFO</strong>](openasinfo.md)<br/></td>
<td>Stores information for the [<strong>SHOpenWithDialog</strong>](shopenwithdialog.md) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OVERLAPPED</strong>](overlapped.md)<br/></td>
<td>Contains information used in asynchronous (overlapped) input/output (I/O).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PARSEDURL</strong>](parsedurl.md)<br/></td>
<td>Used by the [<strong>ParseURL</strong>](parseurl.md) function to return the parsed URL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PERSIST_FOLDER_TARGET_INFO</strong>](persist-folder-target-info-str.md)<br/></td>
<td>Specifies a folder shortcut's target folder and its attributes. This structure is used by [<strong>IPersistFolder3::GetFolderTargetInfo</strong>](ipersistfolder3-getfoldertargetinfo.md) and [<strong>IPersistFolder3::InitializeEx</strong>](ipersistfolder3-initializeex.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PREVIEWHANDLERFRAMEINFO</strong>](previewhandlerframeinfo.md)<br/></td>
<td>Accelerator table structure. Used by [<strong>IPreviewHandlerFrame::GetWindowContext</strong>](ipreviewhandlerframe-getwindowcontext.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>PROFILEINFO</strong>](profileinfo.md)<br/></td>
<td>Contains information used when loading or unloading a user profile.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PUBAPPINFO</strong>](pubappinfo.md)<br/></td>
<td>Provides information about a published application from an application publisher to <strong>Add/Remove Programs</strong> in Control Panel.<br/></td>
</tr>
<tr class="even">
<td>[<strong>QCMINFO</strong>](qcminfo-str.md)<br/></td>
<td>Contains information for merging menu items into Windows Explorer menus.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>QITAB</strong>](qitab.md)<br/></td>
<td>Used by the [<strong>QISearch</strong>](qisearch.md) function to describe a single interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SERIALIZEDPROPERTYVALUE</strong>](serializedpropertyvalue.md)<br/></td>
<td>A range of memory of arbitrary type that represents a serialized [<strong>PROPVARIANT</strong>](stg.propvariant) structure. Programs should not inspect the contents of a [<strong>SERIALIZEDPROPERTYVALUE</strong>](serializedpropertyvalue.md); instead, they should manipulate it with the [<strong>StgSerializePropVariant</strong>](properties.StgSerializePropVariant) and [<strong>StgDeserializePropVariant</strong>](properties.StgDeserializePropVariant) functions.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SFV_CREATE</strong>](sfv-create.md)<br/></td>
<td>This structure is used with the [<strong>SHCreateShellFolderView</strong>](shcreateshellfolderview.md) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SFV_SETITEMPOS</strong>](sfv-setitempos.md)<br/></td>
<td>Stores position information for an item. Used with message [<strong>SFVM_SETITEMPOS</strong>](sfvm-setitempos.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SFVM_HELPTOPIC_DATA</strong>](sfvm-helptopic-data-str.md)<br/></td>
<td>Contains the name of an HTML Help file and a topic in that file. Used with the [<strong>SFVM_GETHELPTOPIC</strong>](sfvm-gethelptopic.md) notification. This structure requires Unicode strings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SFVM_PROPPAGE_DATA</strong>](sfvm-proppage-data.md)<br/></td>
<td>Contains the details of a page to be added to an object's <strong>Properties</strong> sheet.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHARDAPPIDINFO</strong>](shardappidinfo.md)<br/></td>
<td>Contains data used by [<strong>SHAddToRecentDocs</strong>](shaddtorecentdocs.md) to identify both an item—in this case as an [<strong>IShellItem</strong>](ishellitem.md)—and the process that it is associated with.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHARDAPPIDINFOIDLIST</strong>](shardappidinfoidlist.md)<br/></td>
<td>Contains data used by [<strong>SHAddToRecentDocs</strong>](shaddtorecentdocs.md) to identify both an item—in this case by an absolute PIDL—and the process that it is associated with.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHARDAPPIDINFOLINK</strong>](shardappidinfolink.md)<br/></td>
<td>Contains data used by [<strong>SHAddToRecentDocs</strong>](shaddtorecentdocs.md) to identify both an item, in this case through an [<strong>IShellLink</strong>](ishelllink.md), and the process that it is associated with.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHChangeNotifyEntry</strong>](shchangenotifyentry.md)<br/></td>
<td>Contains and receives information for change notifications. This structure is used with the [<strong>SHChangeNotifyRegister</strong>](shchangenotifyregister.md) function and the [<strong>SFVM_QUERYFSNOTIFY</strong>](sfvm-queryfsnotify.md) notification.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCOLUMNDATA</strong>](shcolumndata-str.md)<br/></td>
<td>Contains information that identifies a particular file. It is used by [<strong>IColumnProvider::GetItemData</strong>](icolumnprovider-getitemdata.md) when requesting data for a particular file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCOLUMNID</strong>](shcolumnid-str.md)<br/></td>
<td>Specifies the FMTID/PID identifier of a column that will be displayed by the Windows Explorer Details view. <br/>
<blockquote>
[!Note]<br />
As of Windows Vista, [<strong>SHCOLUMNID</strong>](shcolumnid-str.md) is considered a legacy form and should not be used. In its place, use the [<strong>PROPERTYKEY</strong>](properties.PROPERTYKEY) structure.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCOLUMNINFO</strong>](shcolumninfo-str.md)<br/></td>
<td>Contains information about the properties of a column. It is used by [<strong>IColumnProvider::GetColumnInfo</strong>](icolumnprovider-getcolumninfo.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCOLUMNINIT</strong>](shcolumninit-str.md)<br/></td>
<td>Passes initialization information to [<strong>IColumnProvider::Initialize</strong>](icolumnprovider-initialize.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHDESCRIPTIONID</strong>](shdescriptionid-str.md)<br/></td>
<td>Receives item data in response to a call to [<strong>SHGetDataFromIDList</strong>](shgetdatafromidlist.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHDRAGIMAGE</strong>](shdragimage-str.md)<br/></td>
<td>Contains the information needed to create a drag image.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHELL_ITEM_RESOURCE</strong>](shell-item-resource.md)<br/></td>
<td>Defines Shell item resource.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHELLDETAILS</strong>](shelldetails-str.md)<br/></td>
<td>Reports detailed information on an item in a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHELLEXECUTEINFO</strong>](shellexecuteinfo.md)<br/></td>
<td>Contains information used by [<strong>ShellExecuteEx</strong>](shellexecuteex.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHELLFLAGSTATE</strong>](shellflagstate.md)<br/></td>
<td>Contains a set of flags that indicate the current Shell settings. This structure is used with the [<strong>SHGetSettings</strong>](shgetsettings.md) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHELLSTATE</strong>](shellstate.md)<br/></td>
<td>Contains settings for the Shell's state. This structure is used with the [<strong>SHGetSetSettings</strong>](shgetsetsettings.md) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHFILEINFO</strong>](shfileinfo.md)<br/></td>
<td>Contains information about a file object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHFILEOPSTRUCT</strong>](shfileopstruct.md)<br/></td>
<td>Contains information that the [<strong>SHFileOperation</strong>](shfileoperation.md) function uses to perform file operations. <br/>
<blockquote>
[!Note]<br />
As of Windows Vista, the use of the [<strong>IFileOperation</strong>](ifileoperation.md) interface is recommended over this function.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHFOLDERCUSTOMSETTINGS</strong>](shfoldercustomsettings.md)<br/></td>
<td>Holds custom folder settings. This structure is used with the [<strong>SHGetSetFolderCustomSettings</strong>](shgetsetfoldercustomsettings.md) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHITEMID</strong>](shitemid.md)<br/></td>
<td>Defines an item identifier.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHNAMEMAPPING</strong>](shnamemapping.md)<br/></td>
<td>Contains the old and new path names for each file that was moved, copied, or renamed by the [<strong>SHFileOperation</strong>](shfileoperation.md) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHQUERYRBINFO</strong>](shqueryrbinfo.md)<br/></td>
<td>Contains the size and item count information retrieved by the [<strong>SHQueryRecycleBin</strong>](shqueryrecyclebin.md) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHSTOCKICONINFO</strong>](shstockiconinfo.md)<br/></td>
<td>Receives information used to retrieve a stock Shell icon. This structure is used in a call [<strong>SHGetStockIconInfo</strong>](shgetstockiconinfo.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SLOWAPPINFO</strong>](slowappinfo.md)<br/></td>
<td>Provides specialized application information to <strong>Add/Remove Programs</strong> in Control Panel. This structure is not applicable to published applications.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SMCSHCHANGENOTIFYSTRUCT</strong>](smcshchangenotifystruct.md)<br/></td>
<td>Contains information about change notification. It is used by [<strong>IShellMenuCallback::CallbackSM</strong>](ishellmenucallback-callbacksm.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SMDATA</strong>](smdata.md)<br/></td>
<td>Contains information from a menu band.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SMINFO</strong>](sminfo.md)<br/></td>
<td>Contains information about an item from a menu band.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SOFTDISTINFO</strong>](softdistinfo.md)<br/></td>
<td>Contains information about a software update.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SORTCOLUMN</strong>](sortcolumn.md)<br/></td>
<td>Stores information about how to sort a column that is displayed in the folder view.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STRRET</strong>](strret.md)<br/></td>
<td>Contains strings returned from the [<strong>IShellFolder</strong>](ishellfolder.md) interface methods.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SV2CVW2_PARAMS</strong>](sv2cvw2-params.md)<br/></td>
<td>Holds the parameters for the [<strong>IShellView2::CreateViewWindow2</strong>](ishellview2-createviewwindow2.md) method.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNC_HANDLER_ITEM_INFO</strong>](sync-handler-item-info.md)<br/></td>
<td>Defines a handler for a scheduled synchronization. Used with [<strong>ISyncSchedule::AddItem</strong>](isyncschedule-additem.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGR_CONFLICT_ID_INFO</strong>](syncmgr-conflict-id-info.md)<br/></td>
<td>Describes conflict ID information structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRHANDLERINFO</strong>](syncmgr-syncmgrhandlerinfo.md)<br/></td>
<td>Provides information about the handler for use in the [<strong>ISyncMgrSynchronize::GetHandlerInfo</strong>](syncmgr-isyncmgrsynchronize-gethandlerinfo.md) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRITEM</strong>](syncmgr-syncmgritem.md)<br/></td>
<td>Provides information about items being enumerated by the [<strong>ISyncMgrEnumItems</strong>](syncmgr-isyncmgrenumitems.md) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SYNCMGRLOGERRORINFO</strong>](syncmgr-syncmgrlogerrorinfo.md)<br/></td>
<td>Provides error information for use in the [<strong>ISyncMgrSynchronizeCallback::LogError</strong>](syncmgr-isyncmgrsynchronizecallback-logerror.md) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SYNCMGRPROGRESSITEM</strong>](syncmgr-syncmgrprogressitem.md)<br/></td>
<td>Provides status information while a synchronization is in progress. This structure is used with the [<strong>ISyncMgrSynchronizeCallback::Progress</strong>](syncmgr-isyncmgrsynchronizecallback-progress.md) method and corresponds to a single synchronization item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TBINFO</strong>](tbinfo-str.md)<br/></td>
<td>Used with the [<strong>SFVM_GETBUTTONINFO</strong>](sfvm-getbuttoninfo.md) notification to specify the number of buttons to add to the toolbar, as well as how they're added.<br/></td>
</tr>
<tr class="even">
<td>[<strong>THUMBBUTTON</strong>](thumbbutton.md)<br/></td>
<td>Used by methods of the [<strong>ITaskbarList3</strong>](itaskbarlist3.md) interface to define buttons used in a toolbar embedded in a window's thumbnail representation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WALLPAPEROPT</strong>](wallpaperopt.md)<br/></td>
<td>Contains the wallpaper display options. Used with members of the [<strong>IActiveDesktop</strong>](lwef.iactivedesktop_interface) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>WINDOWDATA</strong>](windowdata.md)<br/></td>
<td>Stores window data.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WTS_CONTEXTFLAGS</strong>](wts-contextflags.md)<br/></td>
<td>Specifies the context of a thumbnail extraction. Used by [<strong>IThumbnailSettings::SetContext</strong>](ithumbnailsettings-setcontext.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>WTS_FLAGS</strong>](wts-flags.md)<br/></td>
<td>Values used by [<strong>IThumbnailCache::GetThumbnail</strong>](ithumbnailcache-getthumbnail.md) to specify options for the extraction and display of the thumbnail image.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WTS_THUMBNAILID</strong>](wts-thumbnailid.md)<br/></td>
<td>Contains a unique identifier for a thumbnail in the system thumbnail cache.<br/></td>
</tr>
</tbody>
</table>



 

 

 




