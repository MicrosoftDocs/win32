---
description: This section describes the Windows Shell functions.
title: Shell Functions
ms.topic: article
ms.date: 05/31/2018
ms.assetid: f4d6c0c4-8db3-4721-80f5-2a73bb57cd99
api_name: 
api_type: 
api_location: 
topic_type:
- kbArticle
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
<td><a href="intsafe-h-functions-bumper.md">Intsafe.h Functions</a><br/></td>

</tr>
<tr class="even">
<td><a href="library-functions-bumper.md">Library Functions</a><br/></td>

</tr>
<tr class="odd">
<td><a href="path-functions.md">Path Functions</a><br/></td>

</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-assoccreateforclasses"><strong>AssocCreateForClasses</strong></a><br/></td>
<td>Retrieves an object that implements an <a href="/windows/desktop/api/shlwapi/nn-shlwapi-iqueryassociations"><strong>IQueryAssociations</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-assocgetdetailsofpropkey"><strong>AssocGetDetailsOfPropKey</strong></a><br/></td>
<td>Retrieves the value for a given property key using the file association information provided by the <a href="nse-works.md">Namespace Extensions</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-cdeffoldermenu_create2"><strong>CDefFolderMenu_Create2</strong></a><br/></td>
<td>Creates a context menu for a selected group of file folder objects.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/win32/api/ntquery/nf-ntquery-cishutdown"><strong>CIShutdown</strong></a><br/></td>
<td>Shuts down the content indexer and closes all open catalogs. <br/>
<blockquote>
[!Note]<br />
This function is not supported as of Windows 8.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-commandlinetoargvw"><strong>CommandLineToArgvW</strong></a><br/></td>
<td>Parses a Unicode command line string and returns an array of pointers to the command line arguments, along with a count of such arguments, in a way that is similar to the standard C run-time <em>argv</em> and <em>argc</em> values.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/cpl/nc-cpl-applet_proc"><strong>APPLET_PROC</strong></a><br/></td>
<td>Serves as the entry point for a Control Panel application. This is a library-defined callback function.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-createappcontainerprofile"><strong>CreateAppContainerProfile</strong></a><br/></td>
<td>Creates a per-user, per-app profile for Windows Store apps.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-createenvironmentblock"><strong>CreateEnvironmentBlock</strong></a><br/></td>
<td>Retrieves the environment variables for the specified user. This block can then be passed to the <a href="/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessasusera"><strong>CreateProcessAsUser</strong></a> function.<br/></td>
</tr>
<tr class="even">
<td><a href="createmrulist.md"><strong>CreateMRUListW</strong></a><br/></td>
<td>Creates a new most recently used (MRU) list.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-createprofile"><strong>CreateProfile</strong></a><br/></td>
<td>Creates a new user profile.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Scrnsave/nf-scrnsave-defscreensaverproc"><strong>DefScreenSaverProc</strong></a><br/></td>
<td>Provides default processing for any messages that a screen saver application does not process.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-defsubclassproc"><strong>DefSubclassProc</strong></a><br/></td>
<td>Calls the next handler in a window's subclass chain. The last handler in the subclass chain calls the original window procedure for the window.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-deleteappcontainerprofile"><strong>DeleteAppContainerProfile</strong></a><br/></td>
<td>Deletes the specified per-user, per-app profile.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-deleteprofilea"><strong>DeleteProfile</strong></a><br/></td>
<td>Deletes the user profile and all user-related settings from the specified computer. The caller must have administrative privileges to delete a user's profile.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-destroyenvironmentblock"><strong>DestroyEnvironmentBlock</strong></a><br/></td>
<td>Frees environment variables created by the <a href="/windows/desktop/api/Userenv/nf-userenv-createenvironmentblock"><strong>CreateEnvironmentBlock</strong></a> function.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-deriveappcontainersidfromappcontainername"><strong>DeriveAppContainerSidFromAppContainerName</strong></a><br/></td>
<td>Gets the SID of the specified profile.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/userenv/nf-userenv-deriverestrictedappcontainersidfromappcontainersidandrestrictedname"><strong>DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName</strong></a><br/></td>
<td>DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName is reserved for future use.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shlwapi/nc-shlwapi-dllgetversionproc"><em>DLLGETVERSIONPROC</em></a><br/></td>
<td>Implemented by many of the Windows Shell DLLs to allow applications to obtain DLL-specific version information.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-dragacceptfiles"><strong>DragAcceptFiles</strong></a><br/></td>
<td>Registers whether a window accepts dropped files.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-dragfinish"><strong>DragFinish</strong></a><br/></td>
<td>Releases memory that the system allocated for use in transferring file names to the application.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-dragqueryfilea"><strong>DragQueryFile</strong></a><br/></td>
<td>Retrieves the names of dropped files that result from a successful drag-and-drop operation.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-dragquerypoint"><strong>DragQueryPoint</strong></a><br/></td>
<td>Retrieves the position of the mouse pointer at the time a file was dropped during a drag-and-drop operation.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shellapi/nf-shellapi-duplicateicon"><strong>DuplicateIcon</strong></a><br/></td>
<td>Creates a duplicate of a specified icon.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-expandenvironmentstringsforusera"><strong>ExpandEnvironmentStringsForUser</strong></a><br/></td>
<td>Expands the source string by using the environment block established for the specified user.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shellapi/nf-shellapi-extractassociatedicona"><strong>ExtractAssociatedIcon</strong></a><br/></td>
<td>Gets a handle to an icon stored as a resource in a file or an icon stored in a file's associated executable file.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shellapi/nf-shellapi-extracticona"><strong>ExtractIcon</strong></a><br/></td>
<td>Gets a handle to an icon from the specified executable file, DLL, or icon file. <br/> To retrieve an array of handles to large or small icons, use the <a href="/windows/desktop/api/shellapi/nf-shellapi-extracticonexa"><strong>ExtractIconEx</strong></a> function.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shellapi/nf-shellapi-extracticonexa"><strong>ExtractIconEx</strong></a><br/></td>
<td>The <a href="/windows/desktop/api/shellapi/nf-shellapi-extracticonexa"><strong>ExtractIconEx</strong></a> function creates an array of handles to large or small icons extracted from the specified executable file, DLL, or icon file.<br/></td>
</tr>
<tr class="odd">
<td><a href="fileiconinit.md"><strong>FileIconInit</strong></a><br/></td>
<td>Initializes or reinitializes the system image list.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-findexecutablea"><strong>FindExecutable</strong></a><br/></td>
<td>Retrieves the name of and handle to the executable (.exe) file associated with a specific document file.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/syncmgr/nf-syncmgr-freeconfirmconflictitem"><strong>FreeConfirmConflictItem</strong></a><br/></td>
<td>Frees the resources that have been allocated for a <a href="/windows/desktop/api/Syncmgr/ns-syncmgr-confirm_conflict_item"><strong>CONFIRM_CONFLICT_ITEM</strong></a> structure.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-freeidlistarray"><strong>FreeIDListArray</strong></a><br/></td>
<td>Frees the memory used by an pointer to an item identifier list (PIDL) list array.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-freeidlistarraychild"><strong>FreeIDListArrayChild</strong></a><br/></td>
<td>Releases the memory space for the array of pointers to child item IDs. This releases both the PITEMID_CHILDs within the array and the array itself.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-freeidlistarrayfull"><strong>FreeIDListArrayFull</strong></a><br/></td>
<td>Releases the memory space for the PIDL array. This releases both the PIDLIST_ABSOLUTEs within the array and the array itself.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-freeknownfolderdefinitionfields"><strong>FreeKnownFolderDefinitionFields</strong></a><br/></td>
<td>Frees the allocated fields in the result from <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iknownfolder-getfolderdefinition"><strong>IKnownFolder::GetFolderDefinition</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="freemrulist.md"><strong>FreeMRUList</strong></a><br/></td>
<td>Frees the handle associated with the MRU list and writes cached data to the registry.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-getallusersprofiledirectorya"><strong>GetAllUsersProfileDirectory</strong></a><br/></td>
<td>Retrieves the path to the root of the directory that contains program data shared by all users.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-getappcontainerfolderpath"><strong>GetAppContainerFolderPath</strong></a><br/></td>
<td>Gets the path of the local app data folder for the specified app container.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-getappcontainerregistrylocation"><strong>GetAppContainerRegistryLocation</strong></a><br/></td>
<td>Gets the location of the registry storage associated with an app container.<br/></td>
</tr>
<tr class="even">
<td><a href="/previous-versions/windows/desktop/legacy/jj152005(v=vs.85)"><strong>GetContractDelegateWindow</strong></a><br/></td>
<td>Retrieves a window that has been set as a delegate for an app's primary foreground window for the purpose of associating the delegate window with the app's contracts. Use this function if you are a developer writing a Windows Store app in native C++.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-getcurrentprocessexplicitappusermodelid"><strong>GetCurrentProcessExplicitAppUserModelID</strong></a><br/></td>
<td>Retrieves the application-defined, explicit Application User Model ID (AppUserModelID) for the current process.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-getdefaultuserprofiledirectorya"><strong>GetDefaultUserProfileDirectory</strong></a><br/></td>
<td>Retrieves the path to the root of the default user's profile.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-getdpiforshelluicomponent"><strong>GetDpiForShellUiComponent</strong></a><br/></td>
<td>Retrieves the dots per inch (dpi) occupied by a <a href="/windows/desktop/api/ShellScalingApi/ne-shellscalingapi-shell_ui_component"><strong>SHELL_UI_COMPONENT</strong></a> based on the current scale factor and <a href="/windows/desktop/api/shellscalingapi/ne-shellscalingapi-process_dpi_awareness"><strong>PROCESS_DPI_AWARENESS</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-getmenucontexthelpid"><strong>GetMenuContextHelpId</strong></a><br/></td>
<td>Retrieves the Help context identifier associated with the specified menu.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-getprofilesdirectorya"><strong>GetProfilesDirectory</strong></a><br/></td>
<td>Retrieves the path to the root directory where user profiles are stored.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-getprofiletype"><strong>GetProfileType</strong></a><br/></td>
<td>Retrieves the type of profile loaded for the current user.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-getscalefactorfordevice"><strong>GetScaleFactorForDevice</strong></a><br/></td>
<td>Gets the preferred scale factor for a display device.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-getscalefactorformonitor"><strong>GetScaleFactorForMonitor</strong></a><br/></td>
<td>Gets the scale factor of a specific monitor. This function replaces <a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-getscalefactorfordevice"><strong>GetScaleFactorForDevice</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-getuserprofiledirectorya"><strong>GetUserProfileDirectory</strong></a><br/></td>
<td>Retrieves the path to the root directory of the specified user's profile.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-getwindowcontexthelpid"><strong>GetWindowContextHelpId</strong></a><br/></td>
<td>Retrieves the Help context identifier, if any, associated with the specified window.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-getwindowsubclass"><strong>GetWindowSubclass</strong></a><br/></td>
<td>Retrieves the reference data for the specified window subclass callback.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-idlistcontainerisconsistent"><strong>IDListContainerIsConsistent</strong></a><br/></td>
<td>Verifies that the container structure of an IDList is valid.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilappendid"><strong>ILAppendID</strong></a><br/></td>
<td>Appends or prepends an <a href="/windows/desktop/api/Shtypes/ns-shtypes-shitemid"><strong>SHITEMID</strong></a> structure to an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilclone"><strong>ILClone</strong></a><br/></td>
<td>Clones an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilclonechild"><strong>ILCloneChild</strong></a><br/></td>
<td>Clones a child <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilclonefirst"><strong>ILCloneFirst</strong></a><br/></td>
<td>Clones the first <a href="/windows/desktop/api/Shtypes/ns-shtypes-shitemid"><strong>SHITEMID</strong></a> structure in an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilclonefull"><strong>ILCloneFull</strong></a><br/></td>
<td>Clones a full, or absolute, <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilcombine"><strong>ILCombine</strong></a><br/></td>
<td>Combines two <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structures.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilcreatefrompath"><strong>ILCreateFromPath</strong></a><br/></td>
<td>Returns the <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure associated with a specified file path.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilfindchild"><strong>ILFindChild</strong></a><br/></td>
<td>Determines whether a specified <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure is the child of another <strong>ITEMIDLIST</strong> structure.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilfindlastid"><strong>ILFindLastID</strong></a><br/></td>
<td>Returns a pointer to the last <a href="/windows/desktop/api/Shtypes/ns-shtypes-shitemid"><strong>SHITEMID</strong></a> structure in an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilfree"><strong>ILFree</strong></a><br/></td>
<td>Frees an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure allocated by the Shell.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilgetnext"><strong>ILGetNext</strong></a><br/></td>
<td>Retrieves the next <a href="/windows/desktop/api/Shtypes/ns-shtypes-shitemid"><strong>SHITEMID</strong></a> structure in an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilgetsize"><strong>ILGetSize</strong></a><br/></td>
<td>Returns the size, in bytes, of an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilisaligned"><strong>ILIsAligned</strong></a><br/></td>
<td>Verifies whether a constant <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> is aligned on a pointer boundary, which is a <strong>DWORD</strong> on 32-bit architectures and a <strong>QWORD</strong> on 64-bit architectures.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilischild"><strong>ILIsChild</strong></a><br/></td>
<td>Verifies whether a PIDL is a child PIDL, which is a PIDL with exactly one <a href="/windows/desktop/api/Shtypes/ns-shtypes-shitemid"><strong>SHITEMID</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilisempty"><strong>ILIsEmpty</strong></a><br/></td>
<td>Verifies whether an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure is empty.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilisequal"><strong>ILIsEqual</strong></a><br/></td>
<td>Tests whether two <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structures are equal in a binary comparison.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilisparent"><strong>ILIsParent</strong></a><br/></td>
<td>Tests whether an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure is the parent of another <strong>ITEMIDLIST</strong> structure.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilnext"><strong>ILNext(PCUIDLIST_RELATIVE)</strong></a><br/></td>
<td>Retrieves the next <a href="/windows/desktop/api/Shtypes/ns-shtypes-shitemid"><strong>SHITEMID</strong></a> structure in an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="odd">
<td><a href="/previous-versions/windows/desktop/legacy/bb776455(v=vs.85)"><strong>ILNext(PUIDLIST_RELATIVE)</strong></a><br/></td>
<td>Retrieves the next <a href="/windows/desktop/api/Shtypes/ns-shtypes-shitemid"><strong>SHITEMID</strong></a> structure in an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilremovelastid"><strong>ILRemoveLastID</strong></a><br/></td>
<td>Removes the last <a href="/windows/desktop/api/Shtypes/ns-shtypes-shitemid"><strong>SHITEMID</strong></a> structure from an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilsavetostream"><strong>ILSaveToStream</strong></a><br/></td>
<td>Saves an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure to a stream.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-ilskip"><strong>ILSkip(PCUIDLIST_RELATIVE, UINT)</strong></a><br/></td>
<td>Skips a given number of bytes in a constant, unaligned, relative <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="odd">
<td><a href="/previous-versions/windows/desktop/legacy/bb776459(v=vs.85)"><strong>ILSkip(PUIDLIST_RELATIVE, UINT)</strong></a><br/></td>
<td>Skips a given number of bytes in an unaligned, relative <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Intshcut/nf-intshcut-inetisoffline"><strong>InetIsOffline</strong></a><br/></td>
<td>Determines whether the system is connected to the Internet.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-initnetworkaddresscontrol"><strong>InitNetworkAddressControl</strong></a><br/></td>
<td>Initializes the network address control window class.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-loaduserprofilea"><strong>LoadUserProfile</strong></a><br/></td>
<td>Loads the specified user's profile. The profile can be a <a href="local-user-profiles.md">local user profile</a> or a <a href="roaming-user-profiles.md">roaming user profile</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Intshcut/nf-intshcut-mimeassociationdialoga"><strong>MIMEAssociationDialog</strong></a><br/></td>
<td>Runs the unregistered MIME content type dialog box.<br/>
<blockquote>
[!Note]<br />
Windows XP Service Pack 2 (SP2) or later: This function is no longer supported.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-pathmakeuniquename"><strong>PathMakeUniqueName</strong></a><br/></td>
<td>Creates a unique path name from a template.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-pathyetanothermakeuniquename"><strong>PathYetAnotherMakeUniqueName</strong></a><br/></td>
<td>Creates a unique filename based on an existing filename.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/appnotify/nf-appnotify-registerappstatechangenotification"><strong>RegisterAppStateChangeNotification</strong></a><br/></td>
<td>Enables an app to register a callback function through which it can be notified that its library is going into or coming out of a suspended state. The app can use this information to perform any necessary operations, such as preserving state, that should be performed at that point.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Scrnsave/nf-scrnsave-registerdialogclasses"><strong>RegisterDialogClasses</strong></a><br/></td>
<td>Registers any nonstandard window classes required by a screen saver's configuration dialog box.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-registerscalechangeevent"><strong>RegisterScaleChangeEvent</strong></a><br/></td>
<td>Registers for an event that is triggered when the scale has possibly changed. This function replaces <a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-registerscalechangenotifications"><strong>RegisterScaleChangeNotifications</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-registerscalechangenotifications"><strong>RegisterScaleChangeNotifications</strong></a><br/></td>
<td>Registers a window to receive callbacks when scaling information changes.<br/>
<blockquote>
[!Note]<br />
This function is not supported as of Windows 8.1. Use <a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-registerscalechangeevent"><strong>RegisterScaleChangeEvent</strong></a> instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-removewindowsubclass"><strong>RemoveWindowSubclass</strong></a><br/></td>
<td>Removes a subclass callback from a window.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-revokescalechangenotifications"><strong>RevokeScaleChangeNotifications</strong></a><br/></td>
<td>Revokes the registration of a window, preventing it from receiving callbacks when scaling information changes.<br/>
<blockquote>
[!Note]<br />
This function is not supported as of Windows 8.1. Use <a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-unregisterscalechangeevent"><strong>UnregisterScaleChangeEvent</strong></a> instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Scrnsave/nf-scrnsave-screensaverconfiguredialog"><strong>ScreenSaverConfigureDialog</strong></a><br/></td>
<td>Receives messages sent to a screen saver's configuration dialog box. A screen saver that allows user configuration must define this function.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Scrnsave/nf-scrnsave-screensaverproc"><strong>ScreenSaverProc</strong></a><br/></td>
<td>Receives messages sent to the specified screen saver window.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-setcontractdelegatewindow"><strong>SetContractDelegateWindow</strong></a><br/></td>
<td>Associates an app window other than the primary foreground window with an app's contracts. Use this function if you are a developer writing a Windows Store app in native C++.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-setcurrentprocessexplicitappusermodelid"><strong>SetCurrentProcessExplicitAppUserModelID</strong></a><br/></td>
<td>Specifies a unique application-defined AppUserModelID that identifies the current process to the taskbar. This identifier allows an application to group its associated processes and windows under a single taskbar button.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-setmenucontexthelpid"><strong>SetMenuContextHelpId</strong></a><br/></td>
<td>Associates a Help context identifier with a menu.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-setwindowcontexthelpid"><strong>SetWindowContextHelpId</strong></a><br/></td>
<td>Associates a Help context identifier with the specified window.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-setwindowsubclass"><strong>SetWindowSubclass</strong></a><br/></td>
<td>Installs or updates a window subclass callback.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs"><strong>SHAddToRecentDocs</strong></a><br/></td>
<td>Notifies the system that an item has been accessed, for the purposes of tracking those items used most recently and most frequently. This function can also be used to clear all usage data.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shappbarmessage"><strong>SHAppBarMessage</strong></a><br/></td>
<td>Sends an appbar message to the system.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shassocenumhandlers"><strong>SHAssocEnumHandlers</strong></a><br/></td>
<td>Returns an enumeration object for a specified set of file name extension handlers.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shassocenumhandlersforprotocolbyapplication"><strong>SHAssocEnumHandlersForProtocolByApplication</strong></a><br/></td>
<td>Gets an enumeration interface that provides access to handlers associated with a given protocol.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shbindtofolderidlistparent"><strong>SHBindToFolderIDListParent</strong></a><br/></td>
<td>Given a Shell namespace item specified in the form of a folder, and an item identifier list relative to that folder, this function binds to the parent of the namespace item and optionally returns a pointer to the final component of the item identifier list.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shbindtofolderidlistparentex"><strong>SHBindToFolderIDListParentEx</strong></a><br/></td>
<td>Extends the <a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shbindtofolderidlistparent"><strong>SHBindToFolderIDListParent</strong></a> function by allowing the caller to specify a bind context.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shbindtoobject"><strong>SHBindToObject</strong></a><br/></td>
<td>Retrieves and binds to a specified object by using the Shell namespace <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject"><strong>IShellFolder::BindToObject</strong></a> method.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shbindtoparent"><strong>SHBindToParent</strong></a><br/></td>
<td>Takes a pointer to a fully qualified item identifier list (PIDL), and returns a specified interface pointer on the parent object.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shbrowseforfoldera"><strong>SHBrowseForFolder</strong></a><br/></td>
<td>Displays a dialog box that enables the user to select a Shell folder.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotification_lock"><strong>SHChangeNotification_Lock</strong></a><br/></td>
<td>Locks the shared memory associated with a Shell change notification event.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotification_unlock"><strong>SHChangeNotification_Unlock</strong></a><br/></td>
<td>Unlocks shared memory for a change notification.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotify"><strong>SHChangeNotify</strong></a><br/></td>
<td>Notifies the system of an event that an application has performed. An application should use this function if it performs an action that may affect the Shell.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotifyderegister"><strong>SHChangeNotifyDeregister</strong></a><br/></td>
<td>Unregisters the client's window process from receiving <a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotify"><strong>SHChangeNotify</strong></a> messages.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotifyregister"><strong>SHChangeNotifyRegister</strong></a><br/></td>
<td>Registers a window to receive notifications from the file system or Shell, if the file system supports notifications.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shlobj/nf-shlobj-shchangenotifyregisterthread"><strong>SHChangeNotifyRegisterThread</strong></a><br/></td>
<td>Enables asynchronous register and deregister of a thread.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateassociationregistration"><strong>SHCreateAssociationRegistration</strong></a><br/></td>
<td>Creates an <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationassociationregistration"><strong>IApplicationAssociationRegistration</strong></a> object based on the stock implementation of the interface provided by Windows.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreatedataobject"><strong>SHCreateDataObject</strong></a><br/></td>
<td>Creates a data object in a parent folder.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu"><strong>SHCreateDefaultContextMenu</strong></a><br/></td>
<td>Creates an object that represents the Shell's default context menu implementation.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreatedefaultextracticon"><strong>SHCreateDefaultExtractIcon</strong></a><br/></td>
<td>Creates a standard icon extractor, whose defaults can be further configured via the <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idefaultextracticoninit"><strong>IDefaultExtractIconInit</strong></a> interface.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shobjidl/nf-shobjidl-shcreatedefaultpropertiesop"><strong>SHCreateDefaultPropertiesOp</strong></a><br/></td>
<td>Creates a file operation that sets the default properties on the Shell item that have not already been set.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromidlist"><strong>SHCreateItemFromIDList</strong></a><br/></td>
<td>Creates and initializes a Shell item object from a PIDL. The resulting shell item object supports the <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem"><strong>IShellItem</strong></a> interface.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromparsingname"><strong>SHCreateItemFromParsingName</strong></a><br/></td>
<td>Creates and initializes a Shell item object from a parsing name.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromrelativename"><strong>SHCreateItemFromRelativeName</strong></a><br/></td>
<td>Creates and initializes a Shell item object from a relative parsing name.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateiteminknownfolder"><strong>SHCreateItemInKnownFolder</strong></a><br/></td>
<td>Creates a Shell item object for a single file that exists inside a known folder.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemwithparent"><strong>SHCreateItemWithParent</strong></a><br/></td>
<td>Create a Shell item, given a parent folder and a child item ID.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreateshellfolderview"><strong>SHCreateShellFolderView</strong></a><br/></td>
<td>Creates a new instance of the default Shell folder view object (DefView).<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreateshellfolderviewex"><strong>SHCreateShellFolderViewEx</strong></a><br/></td>
<td>Creates a new instance of the default Shell folder view object. It is recommended that you use <a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreateshellfolderview"><strong>SHCreateShellFolderView</strong></a> rather than this function.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreateshellitem"><strong>SHCreateShellItem</strong></a><br/></td>
<td>Creates an <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem"><strong>IShellItem</strong></a> object. <br/>
<blockquote>
[!Note]<br />
It is recommended that you use <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemwithparent"><strong>SHCreateItemWithParent</strong></a> or <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateitemfromidlist"><strong>SHCreateItemFromIDList</strong></a> instead of this function.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateshellitemarray"><strong>SHCreateShellItemArray</strong></a><br/></td>
<td>Creates a Shell item array object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateshellitemarrayfromdataobject"><strong>SHCreateShellItemArrayFromDataObject</strong></a><br/></td>
<td>Creates a Shell item array object from a data object. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateshellitemarrayfromidlists"><strong>SHCreateShellItemArrayFromIDLists</strong></a><br/></td>
<td>Creates a Shell item array object from a list of <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structures.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateshellitemarrayfromshellitem"><strong>SHCreateShellItemArrayFromShellItem</strong></a><br/></td>
<td>Creates an array of one element from a single Shell item.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shdefextracticona"><strong>SHDefExtractIcon</strong></a><br/></td>
<td>Provides a default handler to extract an icon from a file.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shdodragdrop"><strong>SHDoDragDrop</strong></a><br/></td>
<td>Executes a drag-and-drop operation. Supports drag source creation on demand, as well as drag images.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona"><strong>Shell_NotifyIcon</strong></a><br/></td>
<td>Sends a message to the taskbar's status area.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicongetrect"><strong>Shell_NotifyIconGetRect</strong></a><br/></td>
<td>Gets the screen coordinates of the bounding rectangle of a notification icon.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shellabouta"><strong>ShellAbout</strong></a><br/></td>
<td>Displays a <strong>ShellAbout</strong> dialog box.<br/></td>
</tr>
<tr class="even">
<td><a href="shellddeinit.md"><strong>ShellDDEInit</strong></a><br/></td>
<td>Registers the Shell Dynamic Data Exchange (DDE) services in the current process, notifying the system that the current process wishes to host DDE objects.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea"><strong>ShellExecute</strong></a><br/></td>
<td>Performs an operation on a specified file.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa"><strong>ShellExecuteEx</strong></a><br/></td>
<td>Performs an operation on a specified file.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shemptyrecyclebina"><strong>SHEmptyRecycleBin</strong></a><br/></td>
<td>Empties the Recycle Bin on the specified drive.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shenumerateunreadmailaccountsa"><strong>SHEnumerateUnreadMailAccounts</strong></a><br/></td>
<td>Enumerates the user accounts that have unread email.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shevaluatesystemcommandtemplate"><strong>SHEvaluateSystemCommandTemplate</strong></a><br/></td>
<td>Enforces strict validation of parameters used in a call to <a href="/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa"><strong>CreateProcess</strong></a> or <a href="/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea"><strong>ShellExecute</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa"><strong>SHFileOperation</strong></a><br/></td>
<td>Copies, moves, renames, or deletes a file system object. This function has been replaced in Windows Vista by <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperation"><strong>IFileOperation</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shfreenamemappings"><strong>SHFreeNameMappings</strong></a><br/></td>
<td>Frees a file name mapping object that was retrieved by the <a href="/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa"><strong>SHFileOperation</strong></a> function.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetdatafromidlista"><strong>SHGetDataFromIDList</strong></a><br/></td>
<td>Retrieves extended property data from a relative identifier list.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetdesktopfolder"><strong>SHGetDesktopFolder</strong></a><br/></td>
<td>Retrieves the <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellfolder"><strong>IShellFolder</strong></a> interface for the desktop folder, which is the root of the Shell's namespace.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shgetdiskfreespaceexa"><strong>SHGetDiskFreeSpaceEx</strong></a><br/></td>
<td>Retrieves disk space information for a disk volume.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shgetdrivemedia"><strong>SHGetDriveMedia</strong></a><br/></td>
<td>Returns the type of media that is in the given drive.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shgetfileinfoa"><strong>SHGetFileInfo</strong></a><br/></td>
<td>Retrieves information about an object in the file system, such as a file, folder, directory, or drive root.<br/></td>
</tr>
<tr class="odd">
<td><a href="/previous-versions/windows/desktop/legacy/mt757093(v=vs.85)"><strong>SHGetFolderPathEx</strong></a><br/></td>
<td>Retrieves the full path of a known folder identified by the folder's <a href="knownfolderid.md"><strong>KNOWNFOLDERID</strong></a>. This extends <a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath"><strong>SHGetKnownFolderPath</strong></a> by allowing you to set the initial size of the string buffer.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgeticonoverlayindexa"><strong>SHGetIconOverlayIndex</strong></a><br/></td>
<td>Returns the index of the overlay icon in the system image list.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shgetidlistfromobject"><strong>SHGetIDListFromObject</strong></a><br/></td>
<td>Retrieves the PIDL of an object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shgetimagelist"><strong>SHGetImageList</strong></a><br/></td>
<td>Retrieves an image list.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetinstanceexplorer"><strong>SHGetInstanceExplorer</strong></a><br/></td>
<td>Retrieves an interface that allows hosted Shell extensions and other components to prevent their host process from closing prematurely. The host process is typically Windows Explorer or Windows Internet Explorer, but this function can also be used by other applications.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shgetitemfromdataobject"><strong>SHGetItemFromDataObject</strong></a><br/></td>
<td>Creates an <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem"><strong>IShellItem</strong></a> or related object based on an item specified by an <a href="/windows/desktop/api/objidl/nn-objidl-idataobject"><strong>IDataObject</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shgetitemfromobject"><strong>SHGetItemFromObject</strong></a><br/></td>
<td>Retrieves an <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem"><strong>IShellItem</strong></a> for an object.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderidlist"><strong>SHGetKnownFolderIDList</strong></a><br/></td>
<td>Retrieves the path of a known folder as an <a href="/windows/desktop/api/Shtypes/ns-shtypes-itemidlist"><strong>ITEMIDLIST</strong></a> structure.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderitem"><strong>SHGetKnownFolderItem</strong></a><br/></td>
<td>Retrieves an <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem"><strong>IShellItem</strong></a> object that represents a known folder.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath"><strong>SHGetKnownFolderPath</strong></a><br/></td>
<td>Retrieves the full path of a known folder identified by the folder's <a href="knownfolderid.md"><strong>KNOWNFOLDERID</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shgetlocalizedname"><strong>SHGetLocalizedName</strong></a><br/></td>
<td>Retrieves the localized name of a file in a Shell folder.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shgetnamefromidlist"><strong>SHGetNameFromIDList</strong></a><br/></td>
<td>Retrieves the display name of an item identified by its IDList.<br/></td>
</tr>
<tr class="odd">
<td><a href="/previous-versions/windows/desktop/legacy/bb762192(v=vs.85)"><strong>SHGetNameFromPropertyKey</strong></a><br/></td>
<td>Retrieves the property's canonical name given its <a href="/windows/desktop/api/wtypes/ns-wtypes-propertykey"><strong>PROPERTYKEY</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shgetnewlinkinfoa"><strong>SHGetNewLinkInfo</strong></a><br/></td>
<td>Creates a name for a new shortcut based on the shortcut's proposed target. This function does not create the shortcut, just the name.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetpathfromidlista"><strong>SHGetPathFromIDList</strong></a><br/></td>
<td>Converts an item identifier list to a file system path.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetpathfromidlistex"><strong>SHGetPathFromIDListEx</strong></a><br/></td>
<td>Converts an item identifier list to a file system path. This function extends <a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetpathfromidlista"><strong>SHGetPathFromIDList</strong></a> by allowing you to set the initial size of the string buffer and declare the options below.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetsettings"><strong>SHGetSettings</strong></a><br/></td>
<td>Retrieves the current Shell option settings.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shgetstockiconinfo"><strong>SHGetStockIconInfo</strong></a><br/></td>
<td>Retrieves information about system-defined Shell icons.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shgettemporarypropertyforitem"><strong>SHGetTemporaryPropertyForItem</strong></a><br/></td>
<td>Retrieves the temporary property for the given item. A temporary property is a read/write store that holds properties only for the lifetime of the <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem"><strong>IShellItem</strong></a> object, rather than being persisted back into the item.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shgetunreadmailcountw"><strong>SHGetUnreadMailCount</strong></a><br/></td>
<td>Retrieves a specified user's unread message count for any or all email accounts.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shellapi/nf-shellapi-shisfileavailableoffline"><strong>SHIsFileAvailableOffline</strong></a><br/></td>
<td>Determines whether a file or folder is available for offline use. This function also determines whether the file would be opened from the network, from the local Offline Files cache, or from both locations.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shloadinproc"><strong>SHLoadInProc</strong></a><br/></td>
<td>Creates an instance of the specified object class from within the context of the Shell's process. <br/> <strong>Windows Vista</strong> and later: This function has been disabled and returns E_NOTIMPL.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shellapi/nf-shellapi-shloadnonloadediconoverlayidentifiers"><strong>SHLoadNonloadedIconOverlayIdentifiers</strong></a><br/></td>
<td>Signals the Shell that during the next operation requiring overlay information, it should load icon overlay identifiers that either failed creation or were not present for creation at startup. Identifiers that have already been loaded are not affected.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shlwapi/nf-shlwapi-shlocalstrdupa"><strong>SHLocalStrDup</strong></a><br/></td>
<td>Makes a copy of a string in newly allocated memory.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shlobj/nf-shlobj-shmultifileproperties"><strong>SHMultiFileProperties</strong></a><br/></td>
<td>Displays a merged property sheet for a set of files. Property values common to all the files are shown while those that differ display the string <strong>(multiple values)</strong>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shopenfolderandselectitems"><strong>SHOpenFolderAndSelectItems</strong></a><br/></td>
<td>Opens a Windows Explorer window with specified items in a particular folder selected.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shopenwithdialog"><strong>SHOpenWithDialog</strong></a><br/></td>
<td>Displays the <strong>Open With</strong> dialog box.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/shell/showsharefolderui"><strong>ShowShareFolderUI</strong></a><br/></td>
<td>Displays the <strong>Folder Sharing</strong> tab on the properties sheet for the specified folder.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shparsedisplayname"><strong>SHParseDisplayName</strong></a><br/></td>
<td>Translates a Shell namespace object's display name into an item identifier list and returns the attributes of the object. This function is the preferred method to convert a string to a PIDL.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shpathprepareforwritea"><strong>SHPathPrepareForWrite</strong></a><br/></td>
<td>Checks to see if the path exists. This includes remounting mapped network drives, prompting for ejectable media to be reinserted, creating the paths, prompting for the media to be formatted, and providing the appropriate user interfaces, if necessary. Read/write permissions for the medium are not checked.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shqueryrecyclebina"><strong>SHQueryRecycleBin</strong></a><br/></td>
<td>Retrieves the size of the Recycle Bin and the number of items in it, for a specified drive.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shqueryusernotificationstate"><strong>SHQueryUserNotificationState</strong></a><br/></td>
<td>Checks the state of the computer for the current user to determine whether sending a notification is appropriate.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shremovelocalizedname"><strong>SHRemoveLocalizedName</strong></a><br/></td>
<td>Removes the localized name of a file in a Shell folder.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shlobj/nf-shlobj-shruncontrolpanel"><strong>SHRunControlPanel</strong></a><br/></td>
<td>Opens a Control Panel item. <br/>
<blockquote>
[!Note]<br />
This function is not supported as of Windows Vista
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shobjidl/nf-shobjidl-shsetdefaultproperties"><strong>SHSetDefaultProperties</strong></a><br/></td>
<td>Applies the default set of properties on a Shell item.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shsetinstanceexplorer"><strong>SHSetInstanceExplorer</strong></a><br/></td>
<td>Provides an interface that allows hosted Shell extensions and other components to prevent their host process from closing prematurely. The host process is typically Windows Explorer or Internet Explorer, but this function can also be used by other applications.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shsetknownfolderpath"><strong>SHSetKnownFolderPath</strong></a><br/></td>
<td>Redirects a known folder to a new location.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shsetlocalizedname"><strong>SHSetLocalizedName</strong></a><br/></td>
<td>Sets the localized name of a file in a Shell folder.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shsettemporarypropertyforitem"><strong>SHSetTemporaryPropertyForItem</strong></a><br/></td>
<td>Sets a temporary property for the specified item. A temporary property is kept in a read/write store that holds properties only for the lifetime of the <a href="/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem"><strong>IShellItem</strong></a> object, instead of writing them back into the item.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shsetunreadmailcountw"><strong>SHSetUnreadMailCount</strong></a><br/></td>
<td>Stores the current user's unread message count for a specified email account in the registry.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shellapi/nf-shellapi-shtesttokenmembership"><strong>SHTestTokenMembership</strong></a><br/></td>
<td>Uses <a href="/windows/desktop/api/securitybaseapi/nf-securitybaseapi-checktokenmembership"><strong>CheckTokenMembership</strong></a> to test whether the given token is a member of the local group with the specified RID.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-shupdateimagea"><strong>SHUpdateImage</strong></a><br/></td>
<td>Notifies the Shell that an image in the system image list has changed.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shlobj/nf-shlobj-softwareupdatemessagebox"><strong>SoftwareUpdateMessageBox</strong></a><br/></td>
<td>Displays a standard message box that can be used to notify a user that an application has been updated.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/shlobj_core/nf-shlobj_core-stgmakeuniquename"><strong>StgMakeUniqueName</strong></a><br/></td>
<td>Creates a unique name for a stream or storage object from a template.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strstrniw"><strong>StrStrNIW</strong></a><br/></td>
<td>Finds the first occurrence of a substring within a string. The comparison is case-insensitive.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strstrnw"><strong>StrStrNW</strong></a><br/></td>
<td>Finds the first occurrence of a substring within a string. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Intshcut/nf-intshcut-translateurla"><strong>TranslateURL</strong></a><br/></td>
<td>Applies common translations to a given URL string, creating a new URL string.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Userenv/nf-userenv-unloaduserprofile"><strong>UnloadUserProfile</strong></a><br/></td>
<td>Unloads a user's profile that was loaded by the <a href="/windows/desktop/api/Userenv/nf-userenv-loaduserprofilea"><strong>LoadUserProfile</strong></a> function. The caller must have administrative privileges on the computer. For more information, see the Remarks section of the <strong>LoadUserProfile</strong> function.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/appnotify/nf-appnotify-unregisterappstatechangenotification"><strong>UnregisterAppStateChangeNotification</strong></a><br/></td>
<td>Cancels a change notification registered through <a href="/windows/desktop/api/appnotify/nf-appnotify-registerappstatechangenotification"><strong>RegisterAppStateChangeNotification</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-unregisterscalechangeevent"><strong>UnregisterScaleChangeEvent</strong></a><br/></td>
<td>Unregisters for the scale change event registered through <a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-registerscalechangeevent"><strong>RegisterScaleChangeEvent</strong></a>. This function replaces <a href="/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-revokescalechangenotifications"><strong>RevokeScaleChangeNotifications</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Intshcut/nf-intshcut-urlassociationdialoga"><strong>URLAssociationDialog</strong></a><br/></td>
<td>Invokes the unregistered URL protocol dialog box. This dialog box allows the user to select an application to associate with a previously unknown protocol.<br/>
<blockquote>
[!Note]<br />
Windows XP SP2 or later: This function is no longer supported.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="/previous-versions/windows/desktop/legacy/bb762266(v=vs.85)"><strong>WinExecError</strong></a><br/></td>
<td>Retrieves the error value generated if the <a href="/windows/win32/api/winbase/nf-winbase-winexec">WinExec</a> function cannot run a specified application. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-winhelpa"><strong>WinHelp</strong></a><br/></td>
<td>Launches Windows Help (Winhelp.exe) and passes additional data that indicates the nature of the help requested by the application.<br/></td>
</tr>
</tbody>
</table>



 

 

 
