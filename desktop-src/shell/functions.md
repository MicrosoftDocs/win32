---
Description: This section describes the Windows Shell functions.
title: Shell Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shell Functions

\[This function is no longer implemented.\]

This section describes the Windows Shell functions.

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
<td>[Intsafe.h Functions](intsafe-h-functions-bumper.md)<br/></td>

</tr>
<tr class="even">
<td>[Library Functions](library-functions-bumper.md)<br/></td>

</tr>
<tr class="odd">
<td>[Path Functions](path-functions.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>AssocCreateForClasses</strong>](/windows/win32/Shellapi/nf-shellapi-assoccreateforclasses?branch=master)<br/></td>
<td>Retrieves an object that implements an [<strong>IQueryAssociations</strong>](/windows/win32/Shlwapi/?branch=master) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>AssocGetDetailsOfPropKey</strong>](/windows/win32/shlobj_core/nf-shlobj_core-assocgetdetailsofpropkey?branch=master)<br/></td>
<td>Retrieves the value for a given property key using the file association information provided by the [Namespace Extensions](nse-works.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>CDefFolderMenu_Create2</strong>](/windows/win32/shlobj_core/nf-shlobj_core-cdeffoldermenu_create2?branch=master)<br/></td>
<td>Creates a context menu for a selected group of file folder objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CIShutdown</strong>](/windows/win32/Ntquery/nf-ntquery-cishutdown?branch=master)<br/></td>
<td>Shuts down the content indexer and closes all open catalogs. <br/>
<blockquote>
[!Note]<br />
This function is not supported as of Windows 8.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>CommandLineToArgvW</strong>](/windows/win32/Shellapi/nf-shellapi-commandlinetoargvw?branch=master)<br/></td>
<td>Parses a Unicode command line string and returns an array of pointers to the command line arguments, along with a count of such arguments, in a way that is similar to the standard C run-time <em>argv</em> and <em>argc</em> values.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APPLET_PROC</strong>](/windows/win32/Cpl/nc-cpl-applet_proc?branch=master)<br/></td>
<td>Serves as the entry point for a Control Panel application. This is a library-defined callback function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CreateAppContainerProfile</strong>](/windows/win32/Userenv/nf-userenv-createappcontainerprofile?branch=master)<br/></td>
<td>Creates a per-user, per-app profile for Windows Store apps.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CreateEnvironmentBlock</strong>](/windows/win32/Userenv/nf-userenv-createenvironmentblock?branch=master)<br/></td>
<td>Retrieves the environment variables for the specified user. This block can then be passed to the [<strong>CreateProcessAsUser</strong>](base.createprocessasuser) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CreateMRUListW</strong>](createmrulist.md)<br/></td>
<td>Creates a new most recently used (MRU) list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CreateProfile</strong>](/windows/win32/Userenv/nf-userenv-createprofile?branch=master)<br/></td>
<td>Creates a new user profile.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DefScreenSaverProc</strong>](/windows/win32/Scrnsave/nf-scrnsave-defscreensaverproc?branch=master)<br/></td>
<td>Provides default processing for any messages that a screen saver application does not process.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DefSubclassProc</strong>](/windows/win32/Commctrl/nf-commctrl-defsubclassproc?branch=master)<br/></td>
<td>Calls the next handler in a window's subclass chain. The last handler in the subclass chain calls the original window procedure for the window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DeleteAppContainerProfile</strong>](/windows/win32/Userenv/nf-userenv-deleteappcontainerprofile?branch=master)<br/></td>
<td>Deletes the specified per-user, per-app profile.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DeleteProfile</strong>](/windows/win32/Userenv/nf-userenv-deleteprofilea?branch=master)<br/></td>
<td>Deletes the user profile and all user-related settings from the specified computer. The caller must have administrative privileges to delete a user's profile.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DestroyEnvironmentBlock</strong>](/windows/win32/Userenv/nf-userenv-destroyenvironmentblock?branch=master)<br/></td>
<td>Frees environment variables created by the [<strong>CreateEnvironmentBlock</strong>](/windows/win32/Userenv/nf-userenv-createenvironmentblock?branch=master) function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DeriveAppContainerSidFromAppContainerName</strong>](/windows/win32/Userenv/nf-userenv-deriveappcontainersidfromappcontainername?branch=master)<br/></td>
<td>Gets the SID of the specified profile.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName</strong>](/windows/win32/userenv/nf-userenv-deriverestrictedappcontainersidfromappcontainersidandrestrictedname?branch=master)<br/></td>
<td>DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName is reserved for future use.<br/></td>
</tr>
<tr class="odd">
<td>[<em>DLLGETVERSIONPROC</em>](/windows/win32/Shlwapi/nc-shlwapi-dllgetversionproc?branch=master)<br/></td>
<td>Implemented by many of the Windows Shell DLLs to allow applications to obtain DLL-specific version information.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DragAcceptFiles</strong>](/windows/win32/Shellapi/nf-shellapi-dragacceptfiles?branch=master)<br/></td>
<td>Registers whether a window accepts dropped files.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DragFinish</strong>](/windows/win32/Shellapi/nf-shellapi-dragfinish?branch=master)<br/></td>
<td>Releases memory that the system allocated for use in transferring file names to the application.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DragQueryFile</strong>](/windows/win32/Shellapi/nf-shellapi-dragqueryfilea?branch=master)<br/></td>
<td>Retrieves the names of dropped files that result from a successful drag-and-drop operation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DragQueryPoint</strong>](/windows/win32/Shellapi/nf-shellapi-dragquerypoint?branch=master)<br/></td>
<td>Retrieves the position of the mouse pointer at the time a file was dropped during a drag-and-drop operation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DuplicateIcon</strong>](/windows/win32/Shellapi/?branch=master)<br/></td>
<td>Creates a duplicate of a specified icon.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ExpandEnvironmentStringsForUser</strong>](/windows/win32/Userenv/nf-userenv-expandenvironmentstringsforusera?branch=master)<br/></td>
<td>Expands the source string by using the environment block established for the specified user.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ExtractAssociatedIcon</strong>](/windows/win32/Shellapi/?branch=master)<br/></td>
<td>Gets a handle to an icon stored as a resource in a file or an icon stored in a file's associated executable file.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ExtractIcon</strong>](/windows/win32/Shellapi/?branch=master)<br/></td>
<td>Gets a handle to an icon from the specified executable file, DLL, or icon file. <br/> To retrieve an array of handles to large or small icons, use the [<strong>ExtractIconEx</strong>](/windows/win32/Shellapi/?branch=master) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ExtractIconEx</strong>](/windows/win32/Shellapi/?branch=master)<br/></td>
<td>The [<strong>ExtractIconEx</strong>](/windows/win32/Shellapi/?branch=master) function creates an array of handles to large or small icons extracted from the specified executable file, DLL, or icon file.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FileIconInit</strong>](fileiconinit.md)<br/></td>
<td>Initializes or reinitializes the system image list.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FindExecutable</strong>](/windows/win32/Shellapi/nf-shellapi-findexecutablea?branch=master)<br/></td>
<td>Retrieves the name of and handle to the executable (.exe) file associated with a specific document file.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FreeConfirmConflictItem</strong>](/windows/win32/syncmgr/nf-syncmgr-freeconfirmconflictitem?branch=master)<br/></td>
<td>Frees the resources that have been allocated for a [<strong>CONFIRM_CONFLICT_ITEM</strong>](/windows/win32/Syncmgr/ns-syncmgr-confirm_conflict_item?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FreeIDListArray</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-freeidlistarray?branch=master)<br/></td>
<td>Frees the memory used by an pointer to an item identifier list (PIDL) list array.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FreeIDListArrayChild</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-freeidlistarraychild?branch=master)<br/></td>
<td>Releases the memory space for the array of pointers to child item IDs. This releases both the PITEMID_CHILDs within the array and the array itself.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FreeIDListArrayFull</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-freeidlistarrayfull?branch=master)<br/></td>
<td>Releases the memory space for the PIDL array. This releases both the PIDLIST_ABSOLUTEs within the array and the array itself.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FreeKnownFolderDefinitionFields</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-freeknownfolderdefinitionfields?branch=master)<br/></td>
<td>Frees the allocated fields in the result from [<strong>IKnownFolder::GetFolderDefinition</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-iknownfolder-getfolderdefinition?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>FreeMRUList</strong>](freemrulist.md)<br/></td>
<td>Frees the handle associated with the MRU list and writes cached data to the registry.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetAllUsersProfileDirectory</strong>](/windows/win32/Userenv/nf-userenv-getallusersprofiledirectorya?branch=master)<br/></td>
<td>Retrieves the path to the root of the directory that contains program data shared by all users.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetAppContainerFolderPath</strong>](/windows/win32/Userenv/nf-userenv-getappcontainerfolderpath?branch=master)<br/></td>
<td>Gets the path of the local app data folder for the specified app container.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetAppContainerRegistryLocation</strong>](/windows/win32/Userenv/nf-userenv-getappcontainerregistrylocation?branch=master)<br/></td>
<td>Gets the location of the registry storage associated with an app container.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetContractDelegateWindow</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Retrieves a window that has been set as a delegate for an app's primary foreground window for the purpose of associating the delegate window with the app's contracts. Use this function if you are a developer writing a Windows Store app in native C++.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetCurrentProcessExplicitAppUserModelID</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-getcurrentprocessexplicitappusermodelid?branch=master)<br/></td>
<td>Retrieves the application-defined, explicit Application User Model ID (AppUserModelID) for the current process.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetDefaultUserProfileDirectory</strong>](/windows/win32/Userenv/nf-userenv-getdefaultuserprofiledirectorya?branch=master)<br/></td>
<td>Retrieves the path to the root of the default user's profile.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetDpiForShellUiComponent</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-getdpiforshelluicomponent?branch=master)<br/></td>
<td>Retrieves the dots per inch (dpi) occupied by a [<strong>SHELL_UI_COMPONENT</strong>](/windows/win32/ShellScalingApi/ne-shellscalingapi-shell_ui_component?branch=master) based on the current scale factor and [<strong>PROCESS_DPI_AWARENESS</strong>](hidpi.process_dpi_awareness).<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetMenuContextHelpId</strong>](/windows/win32/Winuser/nf-winuser-getmenucontexthelpid?branch=master)<br/></td>
<td>Retrieves the Help context identifier associated with the specified menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetProfilesDirectory</strong>](/windows/win32/Userenv/nf-userenv-getprofilesdirectorya?branch=master)<br/></td>
<td>Retrieves the path to the root directory where user profiles are stored.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetProfileType</strong>](/windows/win32/Userenv/nf-userenv-getprofiletype?branch=master)<br/></td>
<td>Retrieves the type of profile loaded for the current user.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetScaleFactorForDevice</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-getscalefactorfordevice?branch=master)<br/></td>
<td>Gets the preferred scale factor for a display device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetScaleFactorForMonitor</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-getscalefactorformonitor?branch=master)<br/></td>
<td>Gets the scale factor of a specific monitor. This function replaces [<strong>GetScaleFactorForDevice</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-getscalefactorfordevice?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetUserProfileDirectory</strong>](/windows/win32/Userenv/nf-userenv-getuserprofiledirectorya?branch=master)<br/></td>
<td>Retrieves the path to the root directory of the specified user's profile.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetWindowContextHelpId</strong>](/windows/win32/Winuser/nf-winuser-getwindowcontexthelpid?branch=master)<br/></td>
<td>Retrieves the Help context identifier, if any, associated with the specified window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetWindowSubclass</strong>](/windows/win32/Commctrl/nf-commctrl-getwindowsubclass?branch=master)<br/></td>
<td>Retrieves the reference data for the specified window subclass callback.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IDListContainerIsConsistent</strong>](/windows/win32/shlobj_core/nf-shlobj_core-idlistcontainerisconsistent?branch=master)<br/></td>
<td>Verifies that the container structure of an IDList is valid.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILAppendID</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilappendid?branch=master)<br/></td>
<td>Appends or prepends an [<strong>SHITEMID</strong>](/windows/win32/Shtypes/ns-shtypes-_shitemid?branch=master) structure to an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILClone</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilclone?branch=master)<br/></td>
<td>Clones an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILCloneChild</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilclonechild?branch=master)<br/></td>
<td>Clones a child [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILCloneFirst</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilclonefirst?branch=master)<br/></td>
<td>Clones the first [<strong>SHITEMID</strong>](/windows/win32/Shtypes/ns-shtypes-_shitemid?branch=master) structure in an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILCloneFull</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilclonefull?branch=master)<br/></td>
<td>Clones a full, or absolute, [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILCombine</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilcombine?branch=master)<br/></td>
<td>Combines two [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structures.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILCreateFromPath</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilcreatefrompath?branch=master)<br/></td>
<td>Returns the [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure associated with a specified file path.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILFindChild</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilfindchild?branch=master)<br/></td>
<td>Determines whether a specified [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure is the child of another <strong>ITEMIDLIST</strong> structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILFindLastID</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilfindlastid?branch=master)<br/></td>
<td>Returns a pointer to the last [<strong>SHITEMID</strong>](/windows/win32/Shtypes/ns-shtypes-_shitemid?branch=master) structure in an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILFree</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilfree?branch=master)<br/></td>
<td>Frees an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure allocated by the Shell.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILGetNext</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilgetnext?branch=master)<br/></td>
<td>Retrieves the next [<strong>SHITEMID</strong>](/windows/win32/Shtypes/ns-shtypes-_shitemid?branch=master) structure in an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILGetSize</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilgetsize?branch=master)<br/></td>
<td>Returns the size, in bytes, of an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILIsAligned</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilisaligned?branch=master)<br/></td>
<td>Verifies whether a constant [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) is aligned on a pointer boundary, which is a <strong>DWORD</strong> on 32-bit architectures and a <strong>QWORD</strong> on 64-bit architectures.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILIsChild</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilischild?branch=master)<br/></td>
<td>Verifies whether a PIDL is a child PIDL, which is a PIDL with exactly one [<strong>SHITEMID</strong>](/windows/win32/Shtypes/ns-shtypes-_shitemid?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILIsEmpty</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilisempty?branch=master)<br/></td>
<td>Verifies whether an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure is empty.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILIsEqual</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilisequal?branch=master)<br/></td>
<td>Tests whether two [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structures are equal in a binary comparison.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILIsParent</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilisparent?branch=master)<br/></td>
<td>Tests whether an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure is the parent of another <strong>ITEMIDLIST</strong> structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILNext(PCUIDLIST_RELATIVE)</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilnext?branch=master)<br/></td>
<td>Retrieves the next [<strong>SHITEMID</strong>](/windows/win32/Shtypes/ns-shtypes-_shitemid?branch=master) structure in an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILNext(PUIDLIST_RELATIVE)</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Retrieves the next [<strong>SHITEMID</strong>](/windows/win32/Shtypes/ns-shtypes-_shitemid?branch=master) structure in an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILRemoveLastID</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilremovelastid?branch=master)<br/></td>
<td>Removes the last [<strong>SHITEMID</strong>](/windows/win32/Shtypes/ns-shtypes-_shitemid?branch=master) structure from an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILSaveToStream</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilsavetostream?branch=master)<br/></td>
<td>Saves an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure to a stream.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ILSkip(PCUIDLIST_RELATIVE, UINT)</strong>](/windows/win32/shlobj_core/nf-shlobj_core-ilskip?branch=master)<br/></td>
<td>Skips a given number of bytes in a constant, unaligned, relative [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ILSkip(PUIDLIST_RELATIVE, UINT)</strong>](/windows/win32/Shlobj_core/?branch=master)<br/></td>
<td>Skips a given number of bytes in an unaligned, relative [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>InetIsOffline</strong>](/windows/win32/Intshcut/nf-intshcut-inetisoffline?branch=master)<br/></td>
<td>Determines whether the system is connected to the Internet.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>InitNetworkAddressControl</strong>](/windows/win32/Shellapi/nf-shellapi-initnetworkaddresscontrol?branch=master)<br/></td>
<td>Initializes the network address control window class.<br/></td>
</tr>
<tr class="even">
<td>[<strong>LoadUserProfile</strong>](/windows/win32/Userenv/nf-userenv-loaduserprofilea?branch=master)<br/></td>
<td>Loads the specified user's profile. The profile can be a [local user profile](local-user-profiles.md) or a [roaming user profile](roaming-user-profiles.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIMEAssociationDialog</strong>](/windows/win32/Intshcut/nf-intshcut-mimeassociationdialoga?branch=master)<br/></td>
<td>Runs the unregistered MIME content type dialog box.<br/>
<blockquote>
[!Note]<br />
Windows XP Service Pack 2 (SP2) or later: This function is no longer supported.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathMakeUniqueName</strong>](/windows/win32/shlobj_core/nf-shlobj_core-pathmakeuniquename?branch=master)<br/></td>
<td>Creates a unique path name from a template.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathYetAnotherMakeUniqueName</strong>](/windows/win32/shlobj_core/nf-shlobj_core-pathyetanothermakeuniquename?branch=master)<br/></td>
<td>Creates a unique filename based on an existing filename.<br/></td>
</tr>
<tr class="even">
<td>[<strong>RegisterAppStateChangeNotification</strong>](/windows/win32/appnotify/nf-appnotify-registerappstatechangenotification?branch=master)<br/></td>
<td>Enables an app to register a callback function through which it can be notified that its library is going into or coming out of a suspended state. The app can use this information to perform any necessary operations, such as preserving state, that should be performed at that point.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RegisterDialogClasses</strong>](/windows/win32/Scrnsave/nf-scrnsave-registerdialogclasses?branch=master)<br/></td>
<td>Registers any nonstandard window classes required by a screen saver's configuration dialog box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>RegisterScaleChangeEvent</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-registerscalechangeevent?branch=master)<br/></td>
<td>Registers for an event that is triggered when the scale has possibly changed. This function replaces [<strong>RegisterScaleChangeNotifications</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-registerscalechangenotifications?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RegisterScaleChangeNotifications</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-registerscalechangenotifications?branch=master)<br/></td>
<td>Registers a window to receive callbacks when scaling information changes.<br/>
<blockquote>
[!Note]<br />
This function is not supported as of Windows 8.1. Use [<strong>RegisterScaleChangeEvent</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-registerscalechangeevent?branch=master) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>RemoveWindowSubclass</strong>](/windows/win32/Commctrl/nf-commctrl-removewindowsubclass?branch=master)<br/></td>
<td>Removes a subclass callback from a window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RevokeScaleChangeNotifications</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-revokescalechangenotifications?branch=master)<br/></td>
<td>Revokes the registration of a window, preventing it from receiving callbacks when scaling information changes.<br/>
<blockquote>
[!Note]<br />
This function is not supported as of Windows 8.1. Use [<strong>UnregisterScaleChangeEvent</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-unregisterscalechangeevent?branch=master) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ScreenSaverConfigureDialog</strong>](/windows/win32/Scrnsave/nf-scrnsave-screensaverconfiguredialog?branch=master)<br/></td>
<td>Receives messages sent to a screen saver's configuration dialog box. A screen saver that allows user configuration must define this function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ScreenSaverProc</strong>](/windows/win32/Scrnsave/nf-scrnsave-screensaverproc?branch=master)<br/></td>
<td>Receives messages sent to the specified screen saver window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SetContractDelegateWindow</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-setcontractdelegatewindow?branch=master)<br/></td>
<td>Associates an app window other than the primary foreground window with an app's contracts. Use this function if you are a developer writing a Windows Store app in native C++.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SetCurrentProcessExplicitAppUserModelID</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-setcurrentprocessexplicitappusermodelid?branch=master)<br/></td>
<td>Specifies a unique application-defined AppUserModelID that identifies the current process to the taskbar. This identifier allows an application to group its associated processes and windows under a single taskbar button.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SetMenuContextHelpId</strong>](/windows/win32/Winuser/nf-winuser-setmenucontexthelpid?branch=master)<br/></td>
<td>Associates a Help context identifier with a menu.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SetWindowContextHelpId</strong>](/windows/win32/Winuser/nf-winuser-setwindowcontexthelpid?branch=master)<br/></td>
<td>Associates a Help context identifier with the specified window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SetWindowSubclass</strong>](/windows/win32/Commctrl/nf-commctrl-setwindowsubclass?branch=master)<br/></td>
<td>Installs or updates a window subclass callback.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHAddToRecentDocs</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shaddtorecentdocs?branch=master)<br/></td>
<td>Notifies the system that an item has been accessed, for the purposes of tracking those items used most recently and most frequently. This function can also be used to clear all usage data.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHAppBarMessage</strong>](/windows/win32/Shellapi/nf-shellapi-shappbarmessage?branch=master)<br/></td>
<td>Sends an appbar message to the system.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHAssocEnumHandlers</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shassocenumhandlers?branch=master)<br/></td>
<td>Returns an enumeration object for a specified set of file name extension handlers.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHAssocEnumHandlersForProtocolByApplication</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shassocenumhandlersforprotocolbyapplication?branch=master)<br/></td>
<td>Gets an enumeration interface that provides access to handlers associated with a given protocol.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHBindToFolderIDListParent</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shbindtofolderidlistparent?branch=master)<br/></td>
<td>Given a Shell namespace item specified in the form of a folder, and an item identifier list relative to that folder, this function binds to the parent of the namespace item and optionally returns a pointer to the final component of the item identifier list.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHBindToFolderIDListParentEx</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shbindtofolderidlistparentex?branch=master)<br/></td>
<td>Extends the [<strong>SHBindToFolderIDListParent</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shbindtofolderidlistparent?branch=master) function by allowing the caller to specify a bind context.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHBindToObject</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shbindtoobject?branch=master)<br/></td>
<td>Retrieves and binds to a specified object by using the Shell namespace [<strong>IShellFolder::BindToObject</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject?branch=master) method.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHBindToParent</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shbindtoparent?branch=master)<br/></td>
<td>Takes a pointer to a fully qualified item identifier list (PIDL), and returns a specified interface pointer on the parent object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHBrowseForFolder</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shbrowseforfoldera?branch=master)<br/></td>
<td>Displays a dialog box that enables the user to select a Shell folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHChangeNotification_Lock</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shchangenotification_lock?branch=master)<br/></td>
<td>Locks the shared memory associated with a Shell change notification event.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHChangeNotification_Unlock</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shchangenotification_unlock?branch=master)<br/></td>
<td>Unlocks shared memory for a change notification.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHChangeNotify</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shchangenotify?branch=master)<br/></td>
<td>Notifies the system of an event that an application has performed. An application should use this function if it performs an action that may affect the Shell.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHChangeNotifyDeregister</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shchangenotifyderegister?branch=master)<br/></td>
<td>Unregisters the client's window process from receiving [<strong>SHChangeNotify</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shchangenotify?branch=master) messages.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHChangeNotifyRegister</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shchangenotifyregister?branch=master)<br/></td>
<td>Registers a window to receive notifications from the file system or Shell, if the file system supports notifications.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHChangeNotifyRegisterThread</strong>](/windows/win32/Shlobj/nf-shlobj-shchangenotifyregisterthread?branch=master)<br/></td>
<td>Enables asynchronous register and deregister of a thread.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCreateAssociationRegistration</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateassociationregistration?branch=master)<br/></td>
<td>Creates an [<strong>IApplicationAssociationRegistration</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-iapplicationassociationregistration?branch=master) object based on the stock implementation of the interface provided by Windows.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCreateDataObject</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shcreatedataobject?branch=master)<br/></td>
<td>Creates a data object in a parent folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCreateDefaultContextMenu</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu?branch=master)<br/></td>
<td>Creates an object that represents the Shell's default context menu implementation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCreateDefaultExtractIcon</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreatedefaultextracticon?branch=master)<br/></td>
<td>Creates a standard icon extractor, whose defaults can be further configured via the [<strong>IDefaultExtractIconInit</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-idefaultextracticoninit?branch=master) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCreateDefaultPropertiesOp</strong>](/windows/win32/Shobjidl/nf-shobjidl-shcreatedefaultpropertiesop?branch=master)<br/></td>
<td>Creates a file operation that sets the default properties on the Shell item that have not already been set.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCreateItemFromIDList</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateitemfromidlist?branch=master)<br/></td>
<td>Creates and initializes a Shell item object from a PIDL. The resulting shell item object supports the [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCreateItemFromParsingName</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname?branch=master)<br/></td>
<td>Creates and initializes a Shell item object from a parsing name.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCreateItemFromRelativeName</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateitemfromrelativename?branch=master)<br/></td>
<td>Creates and initializes a Shell item object from a relative parsing name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCreateItemInKnownFolder</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateiteminknownfolder?branch=master)<br/></td>
<td>Creates a Shell item object for a single file that exists inside a known folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCreateItemWithParent</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateitemwithparent?branch=master)<br/></td>
<td>Create a Shell item, given a parent folder and a child item ID.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCreateShellFolderView</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shcreateshellfolderview?branch=master)<br/></td>
<td>Creates a new instance of the default Shell folder view object (DefView).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCreateShellFolderViewEx</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shcreateshellfolderviewex?branch=master)<br/></td>
<td>Creates a new instance of the default Shell folder view object. It is recommended that you use [<strong>SHCreateShellFolderView</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shcreateshellfolderview?branch=master) rather than this function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCreateShellItem</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shcreateshellitem?branch=master)<br/></td>
<td>Creates an [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) object. <br/>
<blockquote>
[!Note]<br />
It is recommended that you use [<strong>SHCreateItemWithParent</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateitemwithparent?branch=master) or [<strong>SHCreateItemFromIDList</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateitemfromidlist?branch=master) instead of this function.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCreateShellItemArray</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateshellitemarray?branch=master)<br/></td>
<td>Creates a Shell item array object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCreateShellItemArrayFromDataObject</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateshellitemarrayfromdataobject?branch=master)<br/></td>
<td>Creates a Shell item array object from a data object. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHCreateShellItemArrayFromIDLists</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateshellitemarrayfromidlists?branch=master)<br/></td>
<td>Creates a Shell item array object from a list of [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structures.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHCreateShellItemArrayFromShellItem</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shcreateshellitemarrayfromshellitem?branch=master)<br/></td>
<td>Creates an array of one element from a single Shell item.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHDefExtractIcon</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shdefextracticona?branch=master)<br/></td>
<td>Provides a default handler to extract an icon from a file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHDoDragDrop</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shdodragdrop?branch=master)<br/></td>
<td>Executes a drag-and-drop operation. Supports drag source creation on demand, as well as drag images.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>Shell_NotifyIcon</strong>](/windows/win32/Shellapi/nf-shellapi-shell_notifyicona?branch=master)<br/></td>
<td>Sends a message to the taskbar's status area.<br/></td>
</tr>
<tr class="even">
<td>[<strong>Shell_NotifyIconGetRect</strong>](/windows/win32/Shellapi/nf-shellapi-shell_notifyicongetrect?branch=master)<br/></td>
<td>Gets the screen coordinates of the bounding rectangle of a notification icon.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellAbout</strong>](/windows/win32/Shellapi/nf-shellapi-shellabouta?branch=master)<br/></td>
<td>Displays a <strong>ShellAbout</strong> dialog box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellDDEInit</strong>](shellddeinit.md)<br/></td>
<td>Registers the Shell Dynamic Data Exchange (DDE) services in the current process, notifying the system that the current process wishes to host DDE objects.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ShellExecute</strong>](/windows/win32/Shellapi/nf-shellapi-shellexecutea?branch=master)<br/></td>
<td>Performs an operation on a specified file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShellExecuteEx</strong>](/windows/win32/Shellapi/nf-shellapi-shellexecuteexa?branch=master)<br/></td>
<td>Performs an operation on a specified file.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHEmptyRecycleBin</strong>](/windows/win32/Shellapi/nf-shellapi-shemptyrecyclebina?branch=master)<br/></td>
<td>Empties the Recycle Bin on the specified drive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHEnumerateUnreadMailAccounts</strong>](/windows/win32/Shellapi/nf-shellapi-shenumerateunreadmailaccountsa?branch=master)<br/></td>
<td>Enumerates the user accounts that have unread email.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHEvaluateSystemCommandTemplate</strong>](/windows/win32/Shellapi/nf-shellapi-shevaluatesystemcommandtemplate?branch=master)<br/></td>
<td>Enforces strict validation of parameters used in a call to [<strong>CreateProcess</strong>](base.createprocess) or [<strong>ShellExecute</strong>](/windows/win32/Shellapi/nf-shellapi-shellexecutea?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHFileOperation</strong>](/windows/win32/Shellapi/nf-shellapi-shfileoperationa?branch=master)<br/></td>
<td>Copies, moves, renames, or deletes a file system object. This function has been replaced in Windows Vista by [<strong>IFileOperation</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ifileoperation?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHFreeNameMappings</strong>](/windows/win32/Shellapi/nf-shellapi-shfreenamemappings?branch=master)<br/></td>
<td>Frees a file name mapping object that was retrieved by the [<strong>SHFileOperation</strong>](/windows/win32/Shellapi/nf-shellapi-shfileoperationa?branch=master) function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetDataFromIDList</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetdatafromidlista?branch=master)<br/></td>
<td>Retrieves extended property data from a relative identifier list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetDesktopFolder</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetdesktopfolder?branch=master)<br/></td>
<td>Retrieves the [<strong>IShellFolder</strong>](ishellfolder.md) interface for the desktop folder, which is the root of the Shell's namespace.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetDiskFreeSpaceEx</strong>](/windows/win32/Shellapi/nf-shellapi-shgetdiskfreespaceexa?branch=master)<br/></td>
<td>Retrieves disk space information for a disk volume.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetDriveMedia</strong>](/windows/win32/Shellapi/nf-shellapi-shgetdrivemedia?branch=master)<br/></td>
<td>Returns the type of media that is in the given drive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetFileInfo</strong>](/windows/win32/Shellapi/nf-shellapi-shgetfileinfoa?branch=master)<br/></td>
<td>Retrieves information about an object in the file system, such as a file, folder, directory, or drive root.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetFolderPathEx</strong>](/windows/win32/Shlobj/?branch=master)<br/></td>
<td>Retrieves the full path of a known folder identified by the folder's [<strong>KNOWNFOLDERID</strong>](knownfolderid.md). This extends [<strong>SHGetKnownFolderPath</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetknownfolderpath?branch=master) by allowing you to set the initial size of the string buffer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetIconOverlayIndex</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgeticonoverlayindexa?branch=master)<br/></td>
<td>Returns the index of the overlay icon in the system image list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetIDListFromObject</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shgetidlistfromobject?branch=master)<br/></td>
<td>Retrieves the PIDL of an object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetImageList</strong>](/windows/win32/Shellapi/nf-shellapi-shgetimagelist?branch=master)<br/></td>
<td>Retrieves an image list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetInstanceExplorer</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetinstanceexplorer?branch=master)<br/></td>
<td>Retrieves an interface that allows hosted Shell extensions and other components to prevent their host process from closing prematurely. The host process is typically Windows Explorer or Windows Internet Explorer, but this function can also be used by other applications.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetItemFromDataObject</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shgetitemfromdataobject?branch=master)<br/></td>
<td>Creates an [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) or related object based on an item specified by an [<strong>IDataObject</strong>](com.idataobject).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetItemFromObject</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shgetitemfromobject?branch=master)<br/></td>
<td>Retrieves an [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) for an object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetKnownFolderIDList</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetknownfolderidlist?branch=master)<br/></td>
<td>Retrieves the path of a known folder as an [<strong>ITEMIDLIST</strong>](/windows/win32/Shtypes/ns-shtypes-_itemidlist?branch=master) structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetKnownFolderItem</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetknownfolderitem?branch=master)<br/></td>
<td>Retrieves an [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) object that represents a known folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetKnownFolderPath</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetknownfolderpath?branch=master)<br/></td>
<td>Retrieves the full path of a known folder identified by the folder's [<strong>KNOWNFOLDERID</strong>](knownfolderid.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetLocalizedName</strong>](/windows/win32/Shellapi/nf-shellapi-shgetlocalizedname?branch=master)<br/></td>
<td>Retrieves the localized name of a file in a Shell folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetNameFromIDList</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shgetnamefromidlist?branch=master)<br/></td>
<td>Retrieves the display name of an item identified by its IDList.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetNameFromPropertyKey</strong>](/windows/win32/Shobjidl/?branch=master)<br/></td>
<td>Retrieves the property's canonical name given its [<strong>PROPERTYKEY</strong>](properties.PROPERTYKEY).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetNewLinkInfo</strong>](/windows/win32/Shellapi/nf-shellapi-shgetnewlinkinfoa?branch=master)<br/></td>
<td>Creates a name for a new shortcut based on the shortcut's proposed target. This function does not create the shortcut, just the name.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetPathFromIDList</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetpathfromidlista?branch=master)<br/></td>
<td>Converts an item identifier list to a file system path.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetPathFromIDListEx</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetpathfromidlistex?branch=master)<br/></td>
<td>Converts an item identifier list to a file system path. This function extends [<strong>SHGetPathFromIDList</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetpathfromidlista?branch=master) by allowing you to set the initial size of the string buffer and declare the options below.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetSettings</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shgetsettings?branch=master)<br/></td>
<td>Retrieves the current Shell option settings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetStockIconInfo</strong>](/windows/win32/Shellapi/nf-shellapi-shgetstockiconinfo?branch=master)<br/></td>
<td>Retrieves information about system-defined Shell icons.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHGetTemporaryPropertyForItem</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shgettemporarypropertyforitem?branch=master)<br/></td>
<td>Retrieves the temporary property for the given item. A temporary property is a read/write store that holds properties only for the lifetime of the [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) object, rather than being persisted back into the item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHGetUnreadMailCount</strong>](/windows/win32/Shellapi/nf-shellapi-shgetunreadmailcountw?branch=master)<br/></td>
<td>Retrieves a specified user's unread message count for any or all email accounts.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHIsFileAvailableOffline</strong>](shell.shisfileavailableoffline)<br/></td>
<td>Determines whether a file or folder is available for offline use. This function also determines whether the file would be opened from the network, from the local Offline Files cache, or from both locations.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHLoadInProc</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shloadinproc?branch=master)<br/></td>
<td>Creates an instance of the specified object class from within the context of the Shell's process. <br/> <strong>Windows Vista</strong> and later: This function has been disabled and returns E_NOTIMPL.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHLoadNonloadedIconOverlayIdentifiers</strong>](shell.shloadnonloadediconoverlayidentifiers)<br/></td>
<td>Signals the Shell that during the next operation requiring overlay information, it should load icon overlay identifiers that either failed creation or were not present for creation at startup. Identifiers that have already been loaded are not affected.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHLocalStrDup</strong>](/windows/win32/Shlwapi/nf-shlwapi-shlocalstrdupa?branch=master)<br/></td>
<td>Makes a copy of a string in newly allocated memory.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHMultiFileProperties</strong>](/windows/win32/Shlobj/nf-shlobj-shmultifileproperties?branch=master)<br/></td>
<td>Displays a merged property sheet for a set of files. Property values common to all the files are shown while those that differ display the string <strong>(multiple values)</strong>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHOpenFolderAndSelectItems</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shopenfolderandselectitems?branch=master)<br/></td>
<td>Opens a Windows Explorer window with specified items in a particular folder selected.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHOpenWithDialog</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shopenwithdialog?branch=master)<br/></td>
<td>Displays the <strong>Open With</strong> dialog box.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ShowShareFolderUI</strong>](shell.showsharefolderui)<br/></td>
<td>Displays the <strong>Folder Sharing</strong> tab on the properties sheet for the specified folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHParseDisplayName</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shparsedisplayname?branch=master)<br/></td>
<td>Translates a Shell namespace object's display name into an item identifier list and returns the attributes of the object. This function is the preferred method to convert a string to a PIDL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHPathPrepareForWrite</strong>](shell.shpathprepareforwrite)<br/></td>
<td>Checks to see if the path exists. This includes remounting mapped network drives, prompting for ejectable media to be reinserted, creating the paths, prompting for the media to be formatted, and providing the appropriate user interfaces, if necessary. Read/write permissions for the medium are not checked.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHQueryRecycleBin</strong>](/windows/win32/Shellapi/nf-shellapi-shqueryrecyclebina?branch=master)<br/></td>
<td>Retrieves the size of the Recycle Bin and the number of items in it, for a specified drive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHQueryUserNotificationState</strong>](/windows/win32/Shellapi/nf-shellapi-shqueryusernotificationstate?branch=master)<br/></td>
<td>Checks the state of the computer for the current user to determine whether sending a notification is appropriate.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHRemoveLocalizedName</strong>](/windows/win32/Shellapi/nf-shellapi-shremovelocalizedname?branch=master)<br/></td>
<td>Removes the localized name of a file in a Shell folder.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHRunControlPanel</strong>](/windows/win32/Shlobj/nf-shlobj-shruncontrolpanel?branch=master)<br/></td>
<td>Opens a Control Panel item. <br/>
<blockquote>
[!Note]<br />
This function is not supported as of Windows Vista
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHSetDefaultProperties</strong>](/windows/win32/Shobjidl/nf-shobjidl-shsetdefaultproperties?branch=master)<br/></td>
<td>Applies the default set of properties on a Shell item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHSetInstanceExplorer</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shsetinstanceexplorer?branch=master)<br/></td>
<td>Provides an interface that allows hosted Shell extensions and other components to prevent their host process from closing prematurely. The host process is typically Windows Explorer or Internet Explorer, but this function can also be used by other applications.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHSetKnownFolderPath</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shsetknownfolderpath?branch=master)<br/></td>
<td>Redirects a known folder to a new location.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHSetLocalizedName</strong>](/windows/win32/Shellapi/nf-shellapi-shsetlocalizedname?branch=master)<br/></td>
<td>Sets the localized name of a file in a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHSetTemporaryPropertyForItem</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-shsettemporarypropertyforitem?branch=master)<br/></td>
<td>Sets a temporary property for the specified item. A temporary property is kept in a read/write store that holds properties only for the lifetime of the [<strong>IShellItem</strong>](/windows/win32/shobjidl_core/nn-shobjidl_core-ishellitem?branch=master) object, instead of writing them back into the item.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHSetUnreadMailCount</strong>](/windows/win32/Shellapi/nf-shellapi-shsetunreadmailcountw?branch=master)<br/></td>
<td>Stores the current user's unread message count for a specified email account in the registry.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHTestTokenMembership</strong>](/windows/win32/Shellapi/nf-shellapi-shtesttokenmembership?branch=master)<br/></td>
<td>Uses [<strong>CheckTokenMembership</strong>](security.checktokenmembership) to test whether the given token is a member of the local group with the specified RID.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHUpdateImage</strong>](/windows/win32/shlobj_core/nf-shlobj_core-shupdateimagea?branch=master)<br/></td>
<td>Notifies the Shell that an image in the system image list has changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SoftwareUpdateMessageBox</strong>](/windows/win32/Shlobj/nf-shlobj-softwareupdatemessagebox?branch=master)<br/></td>
<td>Displays a standard message box that can be used to notify a user that an application has been updated.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StgMakeUniqueName</strong>](/windows/win32/shlobj_core/nf-shlobj_core-stgmakeuniquename?branch=master)<br/></td>
<td>Creates a unique name for a stream or storage object from a template.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrStrNIW</strong>](/windows/win32/Shlwapi/nf-shlwapi-strstrniw?branch=master)<br/></td>
<td>Finds the first occurrence of a substring within a string. The comparison is case-insensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrStrNW</strong>](/windows/win32/Shlwapi/nf-shlwapi-strstrnw?branch=master)<br/></td>
<td>Finds the first occurrence of a substring within a string. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TranslateURL</strong>](/windows/win32/Intshcut/nf-intshcut-translateurla?branch=master)<br/></td>
<td>Applies common translations to a given URL string, creating a new URL string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UnloadUserProfile</strong>](/windows/win32/Userenv/nf-userenv-unloaduserprofile?branch=master)<br/></td>
<td>Unloads a user's profile that was loaded by the [<strong>LoadUserProfile</strong>](/windows/win32/Userenv/nf-userenv-loaduserprofilea?branch=master) function. The caller must have administrative privileges on the computer. For more information, see the Remarks section of the <strong>LoadUserProfile</strong> function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UnregisterAppStateChangeNotification</strong>](/windows/win32/appnotify/nf-appnotify-unregisterappstatechangenotification?branch=master)<br/></td>
<td>Cancels a change notification registered through [<strong>RegisterAppStateChangeNotification</strong>](/windows/win32/appnotify/nf-appnotify-registerappstatechangenotification?branch=master).<br/></td>
</tr>
<tr class="even">
<td>[<strong>UnregisterScaleChangeEvent</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-unregisterscalechangeevent?branch=master)<br/></td>
<td>Unregisters for the scale change event registered through [<strong>RegisterScaleChangeEvent</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-registerscalechangeevent?branch=master). This function replaces [<strong>RevokeScaleChangeNotifications</strong>](/windows/win32/ShellScalingAPI/nf-shellscalingapi-revokescalechangenotifications?branch=master).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>URLAssociationDialog</strong>](/windows/win32/Intshcut/nf-intshcut-urlassociationdialoga?branch=master)<br/></td>
<td>Invokes the unregistered URL protocol dialog box. This dialog box allows the user to select an application to associate with a previously unknown protocol.<br/>
<blockquote>
[!Note]<br />
Windows XP SP2 or later: This function is no longer supported.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>WinExecError</strong>](/windows/win32/Shellapi/?branch=master)<br/></td>
<td>Retrieves the error value generated if the [WinExec](http://go.microsoft.com/fwlink/p/?linkid=238266) function cannot run a specified application. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>WinHelp</strong>](/windows/win32/Winuser/nf-winuser-winhelpa?branch=master)<br/></td>
<td>Launches Windows Help (Winhelp.exe) and passes additional data that indicates the nature of the help requested by the application.<br/></td>
</tr>
</tbody>
</table>



 

 

 




