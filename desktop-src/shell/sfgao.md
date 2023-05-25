---
description: Attributes that can be retrieved on an item (file or folder) or set of items.
ms.assetid: 4cb85995-cdc8-4474-8c4d-c783ac91c759
title: SFGAO (Shobjidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SFGAO

`SFGAO` bitfield values represent attributes that can be retrieved on an item (file or folder) or set of items. They are used with the IShellFolder and IShellItem APIs, most notably <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getattributesof"><strong>IShellFolder::GetAttributesOf</strong></a> and <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-getattributes"><strong>IShellItem::GetAttributes</strong></a>.

| Constant/value | Description | 
|----------------|-------------|
| <span id="SFGAO_CANCOPY"></span><span id="sfgao_cancopy"></span><dl><dt><strong>SFGAO_CANCOPY</strong></dt><dt>0x00000001</dt></dl> | The specified items can be copied.<br /> | 
| <span id="SFGAO_CANMOVE"></span><span id="sfgao_canmove"></span><dl><dt><strong>SFGAO_CANMOVE</strong></dt><dt>0x00000002</dt></dl> | The specified items can be moved.<br /> | 
| <span id="SFGAO_CANLINK"></span><span id="sfgao_canlink"></span><dl><dt><strong>SFGAO_CANLINK</strong></dt><dt>0x00000004</dt></dl> | Shortcuts can be created for the specified items. This attribute has the same value as <a href="/windows/desktop/com/dropeffect-constants"><strong>DROPEFFECT_LINK</strong></a>. <br /> If a namespace extension returns this attribute, a <strong>Create Shortcut</strong> entry with a default handler is added to the shortcut menu that is displayed during drag-and-drop operations. The extension can also implement its own handler for the <em>link</em> verb in place of the default. If the extension does so, it is responsible for creating the shortcut.<br /> A <strong>Create Shortcut</strong> item is also added to the Windows Explorer <strong>File</strong> menu and to normal shortcut menus.<br /> If the item is selected, your application's <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand"><strong>IContextMenu::InvokeCommand</strong></a> method is invoked with the <strong>lpVerb</strong> member of the <a href="/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-cminvokecommandinfo"><strong>CMINVOKECOMMANDINFO</strong></a> structure set to <em>link</em>. Your application is responsible for creating the link.<br /> | 
| <span id="SFGAO_STORAGE"></span><span id="sfgao_storage"></span><dl><dt><strong>SFGAO_STORAGE</strong></dt><dt>0x00000008</dt></dl> | The specified items can be bound to an <a href="/windows/desktop/api/objidl/nn-objidl-istorage"><strong>IStorage</strong></a> object through <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a>. For more information about namespace manipulation capabilities, see <strong>IStorage</strong>.<br /> | 
| <span id="SFGAO_CANRENAME"></span><span id="sfgao_canrename"></span><dl><dt><strong>SFGAO_CANRENAME</strong></dt><dt>0x00000010</dt></dl> | The specified items can be renamed. Note that this value is essentially a suggestion; not all namespace clients allow items to be renamed. However, those that do must have this attribute set.<br /> | 
| <span id="SFGAO_CANDELETE"></span><span id="sfgao_candelete"></span><dl><dt><strong>SFGAO_CANDELETE</strong></dt><dt>0x00000020</dt></dl> | The specified items can be deleted.<br /> | 
| <span id="SFGAO_HASPROPSHEET"></span><span id="sfgao_haspropsheet"></span><dl><dt><strong>SFGAO_HASPROPSHEET</strong></dt><dt>0x00000040</dt></dl> | The specified items have property sheets.<br /> | 
| <span id="SFGAO_DROPTARGET"></span><span id="sfgao_droptarget"></span><dl><dt><strong>SFGAO_DROPTARGET</strong></dt><dt>0x00000100</dt></dl> | The specified items are drop targets.<br /> | 
| <span id="SFGAO_CAPABILITYMASK"></span><span id="sfgao_capabilitymask"></span><dl><dt><strong>SFGAO_CAPABILITYMASK</strong></dt><dt>0x00000177</dt></dl> | This flag is a mask for the capability attributes: SFGAO_CANCOPY, SFGAO_CANMOVE, SFGAO_CANLINK, SFGAO_CANRENAME, SFGAO_CANDELETE, SFGAO_HASPROPSHEET, and SFGAO_DROPTARGET. Callers normally do not use this value.<br /> | 
| <span id="SFGAO_SYSTEM"></span><span id="sfgao_system"></span><dl><dt><strong>SFGAO_SYSTEM</strong></dt><dt>0x00001000</dt></dl> | <strong>Windows 7 and later</strong>. The specified items are system items.<br /> | 
| <span id="SFGAO_ENCRYPTED"></span><span id="sfgao_encrypted"></span><dl><dt><strong>SFGAO_ENCRYPTED</strong></dt><dt>0x00002000</dt></dl> | The specified items are encrypted and might require special presentation.<br /> | 
| <span id="SFGAO_ISSLOW"></span><span id="sfgao_isslow"></span><dl><dt><strong>SFGAO_ISSLOW</strong></dt><dt>0x00004000</dt></dl> | Accessing the item (through <a href="/windows/desktop/api/objidl/nn-objidl-istream"><strong>IStream</strong></a> or other storage interfaces) is expected to be a slow operation. Applications should avoid accessing items flagged with SFGAO_ISSLOW. <br /><blockquote>[!Note]<br />Opening a stream for an item is generally a slow operation at all times. SFGAO_ISSLOW indicates that it is expected to be especially slow, for example in the case of slow network connections or offline (FILE_ATTRIBUTE_OFFLINE) files. However, querying SFGAO_ISSLOW is itself a slow operation. Applications should query SFGAO_ISSLOW only on a background thread. An alternate method, such as retrieving the <a href="/windows/desktop/properties/props-system-fileattributes"><strong>PKEY_FileAttributes</strong></a> property and testing for FILE_ATTRIBUTE_OFFLINE, could be used in place of a method call that involves SFGAO_ISSLOW.</blockquote><br /> | 
| <span id="SFGAO_GHOSTED"></span><span id="sfgao_ghosted"></span><dl><dt><strong>SFGAO_GHOSTED</strong></dt><dt>0x00008000</dt></dl> | The specified items are shown as dimmed and unavailable to the user.<br /> | 
| <span id="SFGAO_LINK"></span><span id="sfgao_link"></span><dl><dt><strong>SFGAO_LINK</strong></dt><dt>0x00010000</dt></dl> | The specified items are shortcuts.<br /> | 
| <span id="SFGAO_SHARE"></span><span id="sfgao_share"></span><dl><dt><strong>SFGAO_SHARE</strong></dt><dt>0x00020000</dt></dl> | The specified objects are shared.<br /> | 
| <span id="SFGAO_READONLY"></span><span id="sfgao_readonly"></span><dl><dt><strong>SFGAO_READONLY</strong></dt><dt>0x00040000</dt></dl> | The specified items are read-only. In the case of folders, this means that new items cannot be created in those folders. This should not be confused with the behavior specified by the FILE_ATTRIBUTE_READONLY flag retrieved by <a href="/windows/desktop/api/shlobj/nf-shlobj-icolumnprovider-getitemdata"><strong>IColumnProvider::GetItemData</strong></a> in a <a href="/windows/desktop/api/Shlobj/ns-shlobj-shcolumndata"><strong>SHCOLUMNDATA</strong></a> structure. FILE_ATTRIBUTE_READONLY has no meaning for Win32 file system folders.<br /> | 
| <span id="SFGAO_HIDDEN"></span><span id="sfgao_hidden"></span><dl><dt><strong>SFGAO_HIDDEN</strong></dt><dt>0x00080000</dt></dl> | The item is hidden and should not be displayed unless the <strong>Show hidden files and folders</strong> option is enabled in <strong>Folder Settings</strong>.<br /> | 
| <span id="SFGAO_DISPLAYATTRMASK"></span><span id="sfgao_displayattrmask"></span><dl><dt><strong>SFGAO_DISPLAYATTRMASK</strong></dt><dt>0x000FC000</dt></dl> | Do not use.<br /> | 
| <span id="SFGAO_NONENUMERATED"></span><span id="sfgao_nonenumerated"></span><dl><dt><strong>SFGAO_NONENUMERATED</strong></dt><dt>0x00100000</dt></dl> | The items are nonenumerated items and should be hidden. They are not returned through an enumerator such as that created by the <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-enumobjects"><strong>IShellFolder::EnumObjects</strong></a> method.<br /> | 
| <span id="SFGAO_NEWCONTENT"></span><span id="sfgao_newcontent"></span><dl><dt><strong>SFGAO_NEWCONTENT</strong></dt><dt>0x00200000</dt></dl> | The items contain new content, as defined by the particular application.<br /> | 
| <span id="SFGAO_CANMONIKER"></span><span id="sfgao_canmoniker"></span><dl><dt><strong>SFGAO_CANMONIKER</strong></dt></dl> | Not supported.<br /> | 
| <span id="SFGAO_HASSTORAGE"></span><span id="sfgao_hasstorage"></span><dl><dt><strong>SFGAO_HASSTORAGE</strong></dt></dl> | Not supported.<br /> | 
| <span id="SFGAO_STREAM"></span><span id="sfgao_stream"></span><dl><dt><strong>SFGAO_STREAM</strong></dt><dt>0x00400000</dt></dl> | Indicates that the item has a stream associated with it. That stream can be accessed through a call to <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> or <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-bindtohandler"><strong>IShellItem::BindToHandler</strong></a> with IID_IStream in the <em>riid</em> parameter.<br /> | 
| <span id="SFGAO_STORAGEANCESTOR"></span><span id="sfgao_storageancestor"></span><dl><dt><strong>SFGAO_STORAGEANCESTOR</strong></dt><dt>0x00800000</dt></dl> | Children of this item are accessible through <a href="/windows/desktop/api/objidl/nn-objidl-istream"><strong>IStream</strong></a> or <a href="/windows/desktop/api/objidl/nn-objidl-istorage"><strong>IStorage</strong></a>. Those children are flagged with SFGAO_STORAGE or SFGAO_STREAM.<br /> | 
| <span id="SFGAO_VALIDATE"></span><span id="sfgao_validate"></span><dl><dt><strong>SFGAO_VALIDATE</strong></dt><dt>0x01000000</dt></dl> | When specified as input, SFGAO_VALIDATE instructs the folder to validate that the items contained in a folder or Shell item array exist. If one or more of those items do not exist, <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getattributesof"><strong>IShellFolder::GetAttributesOf</strong></a> and <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitemarray-getattributes"><strong>IShellItemArray::GetAttributes</strong></a> return a failure code. This flag is never returned as an [out] value.<br /> When used with the file system folder, SFGAO_VALIDATE instructs the folder to discard cached properties retrieved by clients of <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder2-getdetailsex"><strong>IShellFolder2::GetDetailsEx</strong></a> that might have accumulated for the specified items.<br /> | 
| <span id="SFGAO_REMOVABLE"></span><span id="sfgao_removable"></span><dl><dt><strong>SFGAO_REMOVABLE</strong></dt><dt>0x02000000</dt></dl> | The specified items are on removable media or are themselves removable devices.<br /> | 
| <span id="SFGAO_COMPRESSED"></span><span id="sfgao_compressed"></span><dl><dt><strong>SFGAO_COMPRESSED</strong></dt><dt>0x04000000</dt></dl> | The specified items are compressed.<br /> | 
| <span id="SFGAO_BROWSABLE"></span><span id="sfgao_browsable"></span><dl><dt><strong>SFGAO_BROWSABLE</strong></dt><dt>0x08000000</dt></dl> | The specified items can be hosted inside a web browser or Windows Explorer frame.<br /> | 
| <span id="SFGAO_FILESYSANCESTOR"></span><span id="sfgao_filesysancestor"></span><dl><dt><strong>SFGAO_FILESYSANCESTOR</strong></dt><dt>0x10000000</dt></dl> | The specified folders are either file system folders or contain at least one descendant (child, grandchild, or later) that is a file system (SFGAO_FILESYSTEM) folder.<br /> | 
| <span id="SFGAO_FOLDER"></span><span id="sfgao_folder"></span><dl><dt><strong>SFGAO_FOLDER</strong></dt><dt>0x20000000</dt></dl> | The specified items are folders. Some items can be flagged with both SFGAO_STREAM and SFGAO_FOLDER, such as a compressed file with a .zip file name extension. Some applications might include this flag when testing for items that are both files and containers.<br /> | 
| <span id="SFGAO_FILESYSTEM"></span><span id="sfgao_filesystem"></span><dl><dt><strong>SFGAO_FILESYSTEM</strong></dt><dt>0x40000000</dt></dl> | The specified folders or files are part of the file system (that is, they are files, directories, or root directories). The parsed names of the items can be assumed to be valid Win32 file system paths. These paths can be either UNC or drive-letter based.<br /> | 
| <span id="SFGAO_STORAGECAPMASK"></span><span id="sfgao_storagecapmask"></span><dl><dt><strong>SFGAO_STORAGECAPMASK</strong></dt><dt>0x70C50008</dt></dl> | This flag is a mask for the storage capability attributes: SFGAO_STORAGE, SFGAO_LINK, SFGAO_READONLY, SFGAO_STREAM, SFGAO_STORAGEANCESTOR, SFGAO_FILESYSANCESTOR, SFGAO_FOLDER, and SFGAO_FILESYSTEM. Callers normally do not use this value.<br /> | 
| <span id="SFGAO_HASSUBFOLDER"></span><span id="sfgao_hassubfolder"></span><dl><dt><strong>SFGAO_HASSUBFOLDER</strong></dt><dt>0x80000000</dt></dl> | The specified folders have subfolders. The SFGAO_HASSUBFOLDER attribute is only advisory and might be returned by Shell folder implementations even if they do not contain subfolders. Note, however, that the converse—failing to return SFGAO_HASSUBFOLDER—definitively states that the folder objects do not have subfolders.<br /> Returning SFGAO_HASSUBFOLDER is recommended whenever a significant amount of time is required to determine whether any subfolders exist. For example, the Shell always returns SFGAO_HASSUBFOLDER when a folder is located on a network drive.<br /> | 
| <span id="SFGAO_CONTENTSMASK"></span><span id="sfgao_contentsmask"></span><dl><dt><strong>SFGAO_CONTENTSMASK</strong></dt><dt>0x80000000</dt></dl> | This flag is a mask for content attributes, at present only SFGAO_HASSUBFOLDER. Callers normally do not use this value.<br /> | 
| <span id="SFGAO_PKEYSFGAOMASK"></span><span id="sfgao_pkeysfgaomask"></span><dl><dt><strong>SFGAO_PKEYSFGAOMASK</strong></dt><dt>0x81044000</dt></dl> | Mask used by the <a href="/windows/desktop/properties/props-system-sfgaoflags">PKEY_SFGAOFlags</a> property to determine attributes that are considered to cause slow calculations or lack context: SFGAO_ISSLOW, SFGAO_READONLY, SFGAO_HASSUBFOLDER, and SFGAO_VALIDATE. Callers normally do not use this value.<br /> | 




## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



## See also

<dl> <dt>

[**IShellFolder::GetAttributesOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getattributesof)
</dt> <dt>

[**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname)
</dt> <dt>

[**IShellItem::GetAttributes**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-getattributes)
</dt> <dt>

[**IShellItemArray::GetAttributes**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitemarray-getattributes)
</dt> </dl>

 

 
