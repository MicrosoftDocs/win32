---
description: A set of string keys that are used with the IBindCtx::RegisterObjectParam method to specify a bind context.
title: Bind Context String Keys (Shobjidl.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: d89a0ee1-9a4b-48a4-8965-0d92f09743a6
api_name: 
 - STR_AVOID_DRIVE_RESTRICTION_POLICY
 - STR_BIND_DELEGATE_CREATE_OBJECT
 - STR_BIND_FOLDER_ENUM_MODE
 - STR_BIND_FOLDERS_READ_ONLY
 - STR_BIND_FORCE_FOLDER_SHORTCUT_RESOLVE
 - STR_DONT_PARSE_RELATIVE
 - STR_DONT_RESOLVE_LINK
 - STR_FILE_SYS_FIND_DATA
 - STR_FILE_SYS_BIND_DATA_WIN7_FORMAT
 - STR_GET_ASYNC_HANDLER
 - STR_GPS_BESTEFFORT
 - STR_GPS_DELAYCREATION
 - STR_GPS_FASTPROPERTIESONLY
 - STR_GPS_HANDLERPROPERTIESONLY
 - STR_GPS_NO_OPLOCK
 - STR_GPS_OPENSLOWITEM
 - STR_IFILTER_FORCE_TEXT_FILTER_FALLBACK
 - STR_IFILTER_LOAD_DEFINED_FILTER
 - STR_INTERNAL_NAVIGATE
 - STR_INTERNETFOLDER_PARSE_ONLY_URLMON_BINDABLE
 - STR_ITEM_CACHE_CONTEXT
 - STR_NO_VALIDATE_FILENAME_CHARS
 - STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS
 - STR_PARSE_AND_CREATE_ITEM
 - STR_PARSE_DONT_REQUIRE_VALIDATED_URLS
 - STR_PARSE_PARTIAL_IDLIST
 - STR_PARSE_PREFER_FOLDER_BROWSING
 - STR_PARSE_PREFER_WEB_BROWSING
 - STR_PARSE_PROPERTYSTORE
 - STR_PARSE_SHELL_PROTOCOL_TO_FILE_OBJECTS
 - STR_PARSE_SHOW_NET_DIAGNOSTICS_UI
 - STR_PARSE_SKIP_NET_CACHE
 - STR_PARSE_TRANSLATE_ALIASES
 - STR_PARSE_WITH_PROPERTIES
 - STR_PROPERTYBAG_PARAM
 - STR_SKIP_BINDING_CLSID
 - STR_TRACK_CLSID
api_type: 
 - HeaderDef
api_location: 
 - Shobjidl.h
topic_type: 
 - APIRef
 - kbSyntax

---

# Bind Context String Keys

A set of string keys that are used with the [**IBindCtx::RegisterObjectParam**](/windows/win32/api/objidl/nf-objidl-ibindctx-registerobjectparam) method to specify a bind context.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="STR_AVOID_DRIVE_RESTRICTION_POLICY"></span><span id="str_avoid_drive_restriction_policy"></span><dl> <dt><strong>STR_AVOID_DRIVE_RESTRICTION_POLICY</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows XP SP2</strong>. Specify this bind context to permit clients of the data source to override the hidden drive letter policy and enable access to the view objects for data sources on the drives that are blocked.<br/> Used with <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> or <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-bindtohandler"><strong>IShellItem::BindToHandler</strong></a>.<br/> The system supports administrator-controlled policies that hide specified drive letters to block users from accessing those drives through Windows Explorer. When this policy is active, the result is that view objects and other handlers created with the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-createviewobject"><strong>IShellFolder::CreateViewObject</strong></a> method will fail when called on drives that are blocked by policy.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_BIND_DELEGATE_CREATE_OBJECT"></span><span id="str_bind_delegate_create_object"></span><dl> <dt><strong>STR_BIND_DELEGATE_CREATE_OBJECT</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to cause the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> method to use the object specified by the <em>pbc</em> parameter to create the target object; in this case, the object specified by the <em>punk</em> parameter in the <a href="/windows/desktop/api/objidl/nf-objidl-ibindctx-registerobjectparam"><strong>IBindCtx::RegisterObjectParam</strong></a> call must implement the <a href="/windows/desktop/api/Propsys/nn-propsys-icreateobject"><strong>ICreateObject</strong></a> interface. <br/> Used with <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> or <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-bindtohandler"><strong>IShellItem::BindToHandler</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_BIND_FOLDER_ENUM_MODE"></span><span id="str_bind_folder_enum_mode"></span><dl> <dt><strong>STR_BIND_FOLDER_ENUM_MODE</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows 7</strong>. Passed to <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> with an <a href="/windows/desktop/api/shobjidl_core/ne-shobjidl_core-folder_enum_mode"><strong>FOLDER_ENUM_MODE</strong></a> value to control the enumeration mode of the parsed item. The <strong>FOLDER_ENUM_MODE</strong> value is passed in the bind context through an object that implements <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iobjectwithfolderenummode"><strong>IObjectWithFolderEnumMode</strong></a>. <br/> Items with different enumeration modes compare canonically (SHCIDS_CANONICALONLY) different because they enumerate different sets of items.<br/> If an item doesn't support the enumeration mode (because it isn't a folder or it doesn't provide the enumeration mode) then it is created in the default enumeration mode.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_BIND_FOLDERS_READ_ONLY"></span><span id="str_bind_folders_read_only"></span><dl> <dt><strong>STR_BIND_FOLDERS_READ_ONLY</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows 7</strong>. Passed to <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> along with <strong>STR_FILE_SYS_BIND_DATA</strong>. This forces simple parsing while also probing for Desktop.ini files along the path from which to get a localized name string. This avoids probing for folders along the path, which, in a case of a folder that represents a server or a share, could take extensive time and resources. Desktop.ini files are cached in some locations, so it will be at least as efficient as probing for folders attributes and then probing for the Desktop.ini if that folder should turn ou tot be read-only.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_BIND_FORCE_FOLDER_SHORTCUT_RESOLVE"></span><span id="str_bind_force_folder_shortcut_resolve"></span><dl> <dt><strong>STR_BIND_FORCE_FOLDER_SHORTCUT_RESOLVE</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows XP SP2</strong>. Specify this bind context to force a folder shortcut to resolve the link that points to its target. <br/> A folder shortcut is a folder item that points to another folder item in the same namespace, using a link (shortcut) to hold the IDList of the target. The link is resolved to track the target in case it is moved or renamed. For example, the Windows XP <strong>My Network Places</strong> folder and the Windows Vista <strong>Computer</strong> folder can contain folder shortcuts created with the <strong>Add Network Location</strong> wizard. To improve performance, the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> method does not resolve links to network folder by default.<br/> Used with <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> or <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-bindtohandler"><strong>IShellItem::BindToHandler</strong></a>. <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_DONT_PARSE_RELATIVE"></span><span id="str_dont_parse_relative"></span><dl> <dt><strong>STR_DONT_PARSE_RELATIVE</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows XP</strong>. Specify this bind context to prevent a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method on the <strong>Desktop</strong> folder from treating relative paths as relative to the desktop; in such a case, parsing fails when this bind context is specified.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_DONT_RESOLVE_LINK"></span><span id="str_dont_resolve_link"></span><dl> <dt><strong>STR_DONT_RESOLVE_LINK</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to instruct an <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem"><strong>IShellItem</strong></a> not to resolve the link target obtained when using the <strong>BHID_LinkTargetItem</strong> GUID in <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-bindtohandler"><strong>IShellItem::BindToHandler</strong></a>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_FILE_SYS_FIND_DATA"></span><span id="str_file_sys_find_data"></span><dl> <dt><strong>STR_FILE_SYS_FIND_DATA</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows XP</strong>. Specify this bind context to provide file metadata to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method, which is used instead of attempting to retrieve the actual file metadata. The associated object must implement <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifilesystembinddata"><strong>IFileSystemBindData</strong></a> and can optionally also implement <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifilesystembinddata2"><strong>IFileSystemBindData2</strong></a>. By default, the <strong>IShellFolder::ParseDisplayName</strong> method verifies that the file exists and uses the file's actual metadata to populate the ID list.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_FILE_SYS_BIND_DATA_WIN7_FORMAT"></span><span id="str_file_sys_bind_data_win7_format"></span><dl> <dt><strong>STR_FILE_SYS_BIND_DATA_WIN7_FORMAT</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows 8.1</strong>. Specify this bind context to indicate that the data provided in the <strong>STR_FILE_SYS_FIND_DATA</strong> bind context should be used to create an ItemID list in the Windows 7 format.&quot;<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GET_ASYNC_HANDLER"></span><span id="str_get_async_handler"></span><dl> <dt><strong>STR_GET_ASYNC_HANDLER</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows 7</strong>. Specify this bind context when the handler is being retrieved on the same thread as the UI. Any memory-intensive activities such as those that involve disk or network access should be avoided.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GPS_BESTEFFORT"></span><span id="str_gps_besteffort"></span><dl> <dt><strong>STR_GPS_BESTEFFORT</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context when requesting an <a href="/windows/desktop/api/propidl/nn-propidl-ipropertysetstorage"><strong>IPropertySetStorage</strong></a> or <a href="/windows/desktop/api/propsys/nn-propsys-ipropertystore"><strong>IPropertyStore</strong></a> handler. This value is used with <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a>. See the <a href="/windows/desktop/api/propsys/ne-propsys-getpropertystoreflags"><strong>GPS_BESTEFFORT</strong></a> flag for more information.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GPS_DELAYCREATION"></span><span id="str_gps_delaycreation"></span><dl> <dt><strong>STR_GPS_DELAYCREATION</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context when requesting an <a href="/windows/desktop/api/propidl/nn-propidl-ipropertysetstorage"><strong>IPropertySetStorage</strong></a> or <a href="/windows/desktop/api/propsys/nn-propsys-ipropertystore"><strong>IPropertyStore</strong></a> handler. This value is used with <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a>. See the <a href="/windows/desktop/api/propsys/ne-propsys-getpropertystoreflags"><strong>GPS_DELAYCREATION</strong></a> flag for more information.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GPS_FASTPROPERTIESONLY"></span><span id="str_gps_fastpropertiesonly"></span><dl> <dt><strong>STR_GPS_FASTPROPERTIESONLY</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context when requesting an <a href="/windows/desktop/api/propidl/nn-propidl-ipropertysetstorage"><strong>IPropertySetStorage</strong></a> or <a href="/windows/desktop/api/propsys/nn-propsys-ipropertystore"><strong>IPropertyStore</strong></a> handler. This value is used with <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a>. See the <a href="/windows/desktop/api/propsys/ne-propsys-getpropertystoreflags"><strong>GPS_FASTPROPERTIESONLY</strong></a> flag for more information.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GPS_HANDLERPROPERTIESONLY"></span><span id="str_gps_handlerpropertiesonly"></span><dl> <dt><strong>STR_GPS_HANDLERPROPERTIESONLY</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context when requesting an <a href="/windows/desktop/api/propidl/nn-propidl-ipropertysetstorage"><strong>IPropertySetStorage</strong></a> or <a href="/windows/desktop/api/propsys/nn-propsys-ipropertystore"><strong>IPropertyStore</strong></a> handler. This value is used with <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a>. See the <a href="/windows/desktop/api/propsys/ne-propsys-getpropertystoreflags"><strong>GPS_HANDLERPROPERTIESONLY</strong></a> flag for more information.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GPS_NO_OPLOCK"></span><span id="str_gps_no_oplock"></span><dl> <dt><strong>STR_GPS_NO_OPLOCK</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows 7</strong>. Specify this bind context when requesting an <a href="/windows/desktop/api/propidl/nn-propidl-ipropertysetstorage"><strong>IPropertySetStorage</strong></a> or <a href="/windows/desktop/api/propsys/nn-propsys-ipropertystore"><strong>IPropertyStore</strong></a> handler. This value is used with <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a>. See the <a href="/windows/desktop/api/propsys/ne-propsys-getpropertystoreflags"><strong>GPS_NO_OPLOCK</strong></a> flag for more information.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GPS_OPENSLOWITEM"></span><span id="str_gps_openslowitem"></span><dl> <dt><strong>STR_GPS_OPENSLOWITEM</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context when requesting an <a href="/windows/desktop/api/propidl/nn-propidl-ipropertysetstorage"><strong>IPropertySetStorage</strong></a> or <a href="/windows/desktop/api/propsys/nn-propsys-ipropertystore"><strong>IPropertyStore</strong></a> handler. This value is used with <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a>. See the <a href="/windows/desktop/api/propsys/ne-propsys-getpropertystoreflags"><strong>GPS_OPENSLOWITEM</strong></a> flag for more information.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_IFILTER_FORCE_TEXT_FILTER_FALLBACK"></span><span id="str_ifilter_force_text_filter_fallback"></span><dl> <dt><strong>STR_IFILTER_FORCE_TEXT_FILTER_FALLBACK</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Windows Vista only.</strong> Specify this bind context to cause a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> method that requests the <a href="/windows/desktop/api/filter/nn-filter-ifilter"><strong>IFilter</strong></a> interface for a file system object to return a text filter if no other filter is available. This value is not defined as of Windows 7.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_IFILTER_LOAD_DEFINED_FILTER"></span><span id="str_ifilter_load_defined_filter"></span><dl> <dt><strong>STR_IFILTER_LOAD_DEFINED_FILTER</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Windows Vista only.</strong> Specify this bind context to cause a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> method that requests the <a href="/windows/desktop/api/filter/nn-filter-ifilter"><strong>IFilter</strong></a> interface for a file system object to not return a fallback filter if no registered filter could be found.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_INTERNAL_NAVIGATE"></span><span id="str_internal_navigate"></span><dl> <dt><strong>STR_INTERNAL_NAVIGATE</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to enable loading of the history from a stream for an internal navigation when the <a href="/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768216(v=vs.85)"><strong>IPersistHistory::LoadHistory</strong></a> method is called. An internal navigation is a navigation within the same view.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_INTERNETFOLDER_PARSE_ONLY_URLMON_BINDABLE"></span><span id="str_internetfolder_parse_only_urlmon_bindable"></span><dl> <dt><strong>STR_INTERNETFOLDER_PARSE_ONLY_URLMON_BINDABLE</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows 7</strong>. Specify this bind context with STR_PARSE_PREFER_FOLDER_BROWSING when the client wants the Internet Shell folder handlers to generate an IDList for any valid URL if a DAV-type folder cannot be created for that URL. The URL is not verified to exist; only its syntax is checked and that it has a registered protocol handler.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_ITEM_CACHE_CONTEXT"></span><span id="str_item_cache_context"></span><dl> <dt><strong>STR_ITEM_CACHE_CONTEXT</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows 7</strong>. Specify this bind context to instruct implementations of <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> and <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipersistfolder3-initializeex"><strong>IPersistFolder3::InitializeEx</strong></a> to cache memory-intensive helper objects that can exist across instantiations of Shell items instead of recreating these objects each time that a Shell item is created. The associated object is another bind context object, initially empty. This should result in a separate bind context object, which is accessed through <a href="/windows/desktop/api/objidl/nf-objidl-ibindctx-getobjectparam"><strong>IBindCtx::GetObjectParam</strong></a> or <a href="/windows/desktop/api/objidl/nf-objidl-ibindctx-registerobjectparam"><strong>IBindCtx::Register.ObjectParam</strong></a>. <br/> A caller must opt into this behavior by providing this bind context parameter when calling <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname"><strong>SHCreateItemFromParsingName</strong></a>. By doing so, you optimize the behavior of binding to multiple parsing names in succession. The lifetime of the bind context object should span multiple instances of Shell items and their individual bind contexts.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_NO_VALIDATE_FILENAME_CHARS"></span><span id="str_no_validate_filename_chars"></span><dl> <dt><strong>STR_NO_VALIDATE_FILENAME_CHARS</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to allow invalid file name characters to appear in file names. By default, a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method rejects characters that are illegal in file names. This bind context is meaningful only in conjunction with the STR_FILE_SYS_FIND_DATA bind context.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS"></span><span id="str_parse_allow_internet_shell_folders"></span><dl> <dt><strong>STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to enable a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method on the <strong>Desktop</strong> folder to parse URLs. If this bind context is specified, it overrides <strong><strong>STR_PARSE_PREFER_WEB_BROWSING</strong></strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_PARSE_AND_CREATE_ITEM"></span><span id="str_parse_and_create_item"></span><dl> <dt><strong>STR_PARSE_AND_CREATE_ITEM</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows 7</strong>. Specify this bind context to instruct a data source's implementation of <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> to optimize the behavior of <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname"><strong>SHCreateItemFromParsingName</strong></a>. <br/> Normally, <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname"><strong>SHCreateItemFromParsingName</strong></a> performs two binding operations on the name to be parsed: one through and one to <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> and one to create the Shell item. When the <strong>STR_PARSE_AND_CREATE_ITEM</strong> bind context is supported, the second bind is avoided by creating the Shell item during the <strong>IShellFolder::ParseDisplayName</strong> bind and storing the Shell item through <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iparseandcreateitem-setitem"><strong>IParseAndCreateItem::SetItem</strong></a>. <strong>SHCreateItemFromParsingName</strong> then uses the stored Shell item rather than creating one.<br/> This parameter applies to the last element of the name that is parsed. For instance, in the name &quot;C:\Folder1\File.txt, the data applies to File.txt.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_PARSE_DONT_REQUIRE_VALIDATED_URLS"></span><span id="str_parse_dont_require_validated_urls"></span><dl> <dt><strong>STR_PARSE_DONT_REQUIRE_VALIDATED_URLS</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Windows Vista only.</strong> Specify that, when parsing a URL, this bind context should not require the URL to exist before generating an IDList for it. Specify this bind context along with <strong><strong>STR_PARSE_PREFER_FOLDER_BROWSING</strong></strong> when the client desires that the <strong>Internet Shell</strong> folder handlers generate an IDList for the URL if a DAV folder cannot be created for the given URL.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_PARSE_PARTIAL_IDLIST"></span><span id="str_parse_partial_idlist"></span><dl> <dt><strong>STR_PARSE_PARTIAL_IDLIST</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to pass the original item that is being re-parsed when that item is stored as a <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem"><strong>IShellItem</strong></a> object that also implements the <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iparentanditem"><strong>IParentAndItem</strong></a> interface. Before Windows 7 this value was not defined in a header file. It could be defined by the caller or passed as its string value of <strong>L&quot;ParseOriginalItem&quot;</strong>. As of Windows 7, the value is defined in Shlobj.h. Note that this is a different header than the other STR constants.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_PARSE_PREFER_FOLDER_BROWSING"></span><span id="str_parse_prefer_folder_browsing"></span><dl> <dt><strong>STR_PARSE_PREFER_FOLDER_BROWSING</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows XP</strong>. Specify this bind context to enable a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method on the <strong>Desktop</strong> folder to parse URLs as if they were folders. Use this bind context to bind to a WebDAV server.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_PARSE_PREFER_WEB_BROWSING"></span><span id="str_parse_prefer_web_browsing"></span><dl> <dt><strong>STR_PARSE_PREFER_WEB_BROWSING</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to prevent a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method on the <strong>Desktop</strong> folder form parsing URLs. This bind context can be overridden by <strong><strong>STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS</strong></strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_PARSE_PROPERTYSTORE"></span><span id="str_parse_propertystore"></span><dl> <dt><strong>STR_PARSE_PROPERTYSTORE</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to override the default property store used by the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method, and use the property store specified as the bind parameter instead. Applies to delegate folders.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_PARSE_SHELL_PROTOCOL_TO_FILE_OBJECTS"></span><span id="str_parse_shell_protocol_to_file_objects"></span><dl> <dt><strong>STR_PARSE_SHELL_PROTOCOL_TO_FILE_OBJECTS</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows XP SP2</strong>. Specify this bind context to enable a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method on the <strong>Desktop</strong> folder to use the &quot;shell:&quot; prefix notation to access files.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_PARSE_SHOW_NET_DIAGNOSTICS_UI"></span><span id="str_parse_show_net_diagnostics_ui"></span><dl> <dt><strong>STR_PARSE_SHOW_NET_DIAGNOSTICS_UI</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to cause a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method to display the network diagnostics dialog if the parsing of a network path fails.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_PARSE_SKIP_NET_CACHE"></span><span id="str_parse_skip_net_cache"></span><dl> <dt><strong>STR_PARSE_SKIP_NET_CACHE</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows Vista</strong>. Specify this bind context to cause a call to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method to skip checking the network shares cache and contact the network server directly. Information about network shares is cached to improve performance, and <strong>IShellFolder::ParseDisplayName</strong> checks this cache by default.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_PARSE_TRANSLATE_ALIASES"></span><span id="str_parse_translate_aliases"></span><dl> <dt><strong>STR_PARSE_TRANSLATE_ALIASES</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows XP</strong>. Specify this bind context to pass parsed properties to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> method for a delegate namespace. The namespace can use the passed properties instead of attempting to parse the name itself.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_PARSE_WITH_PROPERTIES"></span><span id="str_parse_with_properties"></span><dl> <dt><strong>STR_PARSE_WITH_PROPERTIES</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Windows Vista only.</strong> A parsing bind context that is used to pass a set of properties and the item's name when calling <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a>. The object in the bind context implements <a href="/windows/desktop/api/propsys/nn-propsys-ipropertystore"><strong>IPropertyStore</strong></a> and is retrieved by calling <a href="/windows/desktop/api/objidl/nf-objidl-ibindctx-getobjectparam"><strong>IBindCtx::GetObjectParam</strong></a>.<br/> DBFolder is a Shell data source that represents items in search results and query-based views. DBFolder retrieves these items by querying the Windows Search system. Items in the search results are identified through a protocol scheme, for example &quot;file:&quot; or &quot;mapi:&quot;. DBFolder provides the behavior for these items by delegating to Shell data sources that are created for these protocols. See <a href="/previous-versions/bb233544(v=msdn.10)">Developing Protocol Handler Add-ins</a> for more information.<br/> When DBFolder delegates its parsing operation to the Shell data sources that support Windows Search protocols, this bind context provides access to values that were returned in the query result for that item. This includes the following:<br/>
<ul>
<li><a href="/windows/desktop/properties/props-system-itemtype">System.ItemType</a> (PKEY_ItemType)</li>
<li><a href="/windows/desktop/properties/props-system-parsingpath">System.ParsingPath</a> (PKEY_ParsingPath)</li>
<li><a href="/windows/desktop/properties/props-system-itempathdisplay">System.ItemPathDisplay</a> (PKEY_ItemPathDisplay)</li>
<li><a href="/windows/desktop/properties/props-system-itemnamedisplay">System.ItemNameDisplay</a> (PKEY_ItemNameDisplay)</li>
</ul>
<br/> This bind context can also be used to parse a DBFolder item if a client has a set of properties that define the item. In this case an empty name should be passed to <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a>.<br/> Before Windows 7, this value was not defined in a header file. It could be defined by the caller or passed as its string value: <code>L&quot;ParseWithProperties&quot;</code>. As of Windows 7, the value is defined in Shlobj.h. Note that this is a different header than where the other STR constants are defined.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_PROPERTYBAG_PARAM"></span><span id="str_propertybag_param"></span><dl> <dt><strong>STR_PROPERTYBAG_PARAM</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows 8</strong>. Specify this bind context to indicate that the bind context parameter is a property bag (<a href="/windows/win32/api/oaidl/nn-oaidl-ipropertybag"><strong>IPropertyBag</strong></a>) used to pass VARIANT values in the bind context. See the Remarks section for further details.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_SKIP_BINDING_CLSID"></span><span id="str_skip_binding_clsid"></span><dl> <dt><strong>STR_SKIP_BINDING_CLSID</strong></dt> </dl></td>
<td style="text-align: left;"><strong>Introduced in Windows XP</strong>. Specify this bind context to cause calls to the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname"><strong>IShellFolder::ParseDisplayName</strong></a> or <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> methods to ignore a particular Shell namespace extension when parsing or binding. The CLSID of the namespace to ignore is provided by the <a href="/windows/desktop/api/objidl/nf-objidl-ipersist-getclassid"><strong>IPersist::GetClassID</strong></a> method of the bind parameter. <br/>
<blockquote>
[!Note]<br />
Introduced in Windows 2000 SP3, this value was defined in Shlobj.h until Windows XP, when it was moved to Shobjidl.h.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_TRACK_CLSID"></span><span id="str_track_clsid"></span><dl> <dt><strong>STR_TRACK_CLSID</strong></dt> </dl></td>
<td style="text-align: left;">Not used.<br/></td>
</tr>
</tbody>
</table>



## Remarks

Bind contexts are used to pass optional parameters to functions that have an IBindCtx\* parameter. Those parameters are expressed as COM objects and might implement interfaces that are used to model the parameter data. Some bind contexts represent a Boolean value, where **TRUE** indicates an object that implements only [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) and FALSE indicates no object is present.

[**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname), [**IShellFolder::BindToObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject) and [**IShellItem::BindToHandler**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-bindtohandler) take a bind context and you can pass them parameters through that bind context.

Some bind contexts are specific to a certain data source implementations or handler types.

Bind context parameters are defined for use with a specific function or method.

When requesting a property store through [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder), you can specify the equivalent of [**GPS\_DEFAULT**](/windows/win32/api/propsys/ne-propsys-getpropertystoreflags) by passing in a null [**IBindCtx**](/windows/win32/api/objidl/nn-objidl-ibindctx) parameter. You can also specify the equivalent of GPS\_READWRITE by passing a mode of STGM\_READWRITE \| STGM\_EXCLUSIVE in the bind context.

The property bag specified by the **STR\_PROPERTYBAG\_PARAM** bind context object contains additional values that you can access with the [**IPropertyBag::Read**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768197(v=vs.85)) and [**IPropertyBag::Write**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768198(v=vs.85)) methods.



| Property name                                 | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STR\_ENUM\_ITEMS\_FLAGS                       | VT\_UI4  | **Introduced in Windows 8**. Specifies a [**SHCONTF**](/windows/win32/api/shobjidl_core/ne-shobjidl_core-_shcontf) value to be passed to [**IShellFolder::EnumObjects**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-enumobjects) when you call [**IShellItem::BindToHandler**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-bindtohandler) with **BHID\_EnumItems**.                                                                                                                                                                                                                         |
| STR\_PARSE\_EXPLICIT\_ASSOCIATION\_SUCCESSFUL | VT\_BOOL | **Introduced in Windows 7**. The [**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname) method sets this property to tell the caller that the returned IDList was bound to the [ProgID](fa-progids.md) specified with **STR\_PARSE\_WITH\_EXPLICIT\_PROGID** or the application specified with **STR\_PARSE\_WITH\_EXPLICIT\_ASSOCAPP**. When **STR\_PARSE\_EXPLICIT\_ASSOCIATION\_SUCCESSFUL** is absent, the ProgID or application was not bound into the IDList. |
| STR\_PARSE\_WITH\_EXPLICIT\_ASSOCAPP          | VT\_BSTR | **Introduced in Windows 7**. Specify this property to cause a call to the [**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname) method to return an IDList bound to the file type association handler for the application.                                                                                                                                                                                                                                          |
| STR\_PARSE\_WITH\_EXPLICIT\_PROGID            | VT\_BSTR | **Introduced in Windows 7**. Specify this property to cause a call to the [**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname) method to return an IDList bound to the file association handler of the provided [ProgID](fa-progids.md).                                                                                                                                                                                                                          |



 

See the [Parsing With Parameters Sample](samples-parsingwithparameters.md) for an example of the use of bind context values.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 
