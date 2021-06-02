---
description: 'The system stores user profile information in a specific directory, which has different names in different versions of Windows: &\#0034;Documents and Settings&\#0034; in Windows XP and &\#0034;Users&\#0034; in Windows Vista and later.'
title: Profiles Directory
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 41056f40-fa1a-488a-b213-49cbdd8d4fdf
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Profiles Directory

The system stores user profile information in a specific directory, which has different names in different versions of Windows: "Documents and Settings" in Windows XP and "Users" in Windows Vista and later. To obtain the path of the profiles directory, use the [**GetProfilesDirectory**](/windows/desktop/api/Userenv/nf-userenv-getprofilesdirectorya) function.

The profiles directory contains the following subdirectories for user profiles.



| Directory                                      | Description                                                                                                                                |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ProgramData (Windows Vista or later)/All Users | Program information that applies to all users. The All Users directory still exists in Windows Vista or later, for backward compatibility. |
| Default                                        | Profile information that applies to the default user.                                                                                      |
| *User*                                         | Profile information that applies to the specified user. Each user has their own profile subdirectory.                                      |



 

To obtain the location of the ProgramData/All Users directory, call the [**GetAllUsersProfileDirectory**](/windows/desktop/api/Userenv/nf-userenv-getallusersprofiledirectorya) function. This directory contains the following subdirectories:



| Directory  | Description                          |
|------------|--------------------------------------|
| Desktop    | Shortcuts to display on the desktop. |
| Start Menu | Menu items for the **Start** menu.   |



 

To obtain the location of the default user's directory, call the [**GetDefaultUserProfileDirectory**](/windows/desktop/api/Userenv/nf-userenv-getdefaultuserprofiledirectorya) function. To obtain the location of a particular user's directory, call the [**GetUserProfileDirectory**](/windows/desktop/api/Userenv/nf-userenv-getuserprofiledirectorya) function. Both the default user and specific user directories contain the following subdirectories. Directories in italics indicate directories that are hidden by default. You can view these directories by selecting the **Show hidden files, folders, and drives** option in the **Folder Options** control panel item.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Directory</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Application Data</td>
<td>Application-specific data.</td>
</tr>
<tr class="even">
<td>Cookies</td>
<td>Windows Internet Explorer cookies.</td>
</tr>
<tr class="odd">
<td>Desktop</td>
<td>Shortcuts to display on the desktop.</td>
</tr>
<tr class="even">
<td>Favorites</td>
<td>Links to favorite websites.</td>
</tr>
<tr class="odd">
<td>Local Settings</td>
<td>Application settings and data that do not roam with the profile. Usually the settings or data in this directory are computer-specific, or they are too large to roam effectively. This directory contains the following subfolders:
<ul>
<li>Application Data</li>
<li>History</li>
<li>Temp</li>
<li>Temporary Internet Files</li>
</ul></td>
</tr>
<tr class="even">
<td>My Documents</td>
<td>The default location for documents that the user creates. Applications should save document files to this directory by default.</td>
</tr>
<tr class="odd">
<td><em>NetHood</em></td>
<td>Shortcuts to Network Neighborhood items.</td>
</tr>
<tr class="even">
<td><em>PrintHood</em></td>
<td>Shortcuts to printer folder items.</td>
</tr>
<tr class="odd">
<td><em>Recent</em></td>
<td>Shortcuts to the most recently used documents.</td>
</tr>
<tr class="even">
<td>SendTo</td>
<td>Shortcuts to locations to which the user often sends files.</td>
</tr>
<tr class="odd">
<td>Start Menu</td>
<td>Menu items for the <strong>Start</strong> menu.</td>
</tr>
<tr class="even">
<td><em>Templates</em></td>
<td>Shortcuts to template items.</td>
</tr>
</tbody>
</table>



 

To obtain the location of subdirectories of these directories, use the [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) or [**SHGetKnownFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath) functions.

 

 



