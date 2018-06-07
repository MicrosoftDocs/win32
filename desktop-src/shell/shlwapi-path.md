---
Description: This section describes the Windows Shell path handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.
title: Shell Path Handling Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell Path Handling Functions

This section describes the Windows Shell path handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.

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
<td>[<strong>PathAddBackslash</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathaddbackslasha)<br/></td>
<td>Adds a backslash to the end of a string to create the correct syntax for a path. If the source path already has a trailing backslash, no backslash will be added. <br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchAddBackslash</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchaddbackslash) or [<strong>PathCchAddBackslashEx</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchaddbackslashex) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathAddExtension</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathaddextensiona)<br/></td>
<td>Adds a file name extension to a path string.<br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchAddExtension</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchaddextension) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathAppend</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathappenda)<br/></td>
<td>Appends one path to the end of another. <br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchAppend</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchappend) or [<strong>PathCchAppendEx</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchappendex) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathBuildRoot</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathbuildroota)<br/></td>
<td>Creates a root path from a given drive number.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathCanonicalize</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathcanonicalizea)<br/></td>
<td>Simplifies a path by removing navigation elements such as &quot;.&quot; and &quot;..&quot; to produce a direct, well-formed path.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathCombine</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathcombinea)<br/></td>
<td>Concatenates two strings that represent properly formed paths into one path; also concatenates any relative path elements. <br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchCombine</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchcombine) or [<strong>PathCchCombineEx</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchcombineex) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathCommonPrefix</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathcommonprefixa)<br/></td>
<td>Compares two paths to determine if they share a common prefix. A prefix is one of these types: &quot;C:\\&quot;, &quot;.&quot;, &quot;..&quot;, &quot;..\\&quot;.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathCompactPath</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathcompactpatha)<br/></td>
<td>Truncates a file path to fit within a given pixel width by replacing path components with ellipses.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathCompactPathEx</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathcompactpathexa)<br/></td>
<td>Truncates a path to fit within a certain number of characters by replacing path components with ellipses.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathCreateFromUrl</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathcreatefromurla)<br/></td>
<td>Converts a file URL to a Microsoft MS-DOS path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathCreateFromUrlAlloc</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathcreatefromurlalloc)<br/></td>
<td>Creates a path from a file URL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathFileExists</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathfileexistsa)<br/></td>
<td>Determines whether a path to a file system object such as a file or folder is valid.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathFindExtension</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindextensiona)<br/></td>
<td>Searches a path for an extension.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathFindFileName</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindfilenamea)<br/></td>
<td>Searches a path for a file name.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathFindNextComponent</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindnextcomponenta)<br/></td>
<td>Parses a path and returns the portion of that path that follows the first backslash.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathFindOnPath</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindonpatha)<br/></td>
<td>Searches for a file.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathFindSuffixArray</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindsuffixarraya)<br/></td>
<td>Determines whether a given file name has one of a list of suffixes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathGetArgs</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathgetargsa)<br/></td>
<td>Finds the command line arguments within a given path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathGetCharType</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathgetchartypea)<br/></td>
<td>Determines the type of character in relation to a path.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathGetDriveNumber</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathgetdrivenumbera)<br/></td>
<td>Searches a path for a drive letter within the range of 'A' to 'Z' and returns the corresponding drive number.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsContentType</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathiscontenttypea)<br/></td>
<td>Determines if a file's registered content type matches the specified content type. This function obtains the content type for the specified file type and compares that string with the <em>pszContentType</em>. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsDirectory</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisdirectorya)<br/></td>
<td>Verifies that a path is a valid directory.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsDirectoryEmpty</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisdirectoryemptya)<br/></td>
<td>Determines whether a specified path is an empty directory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsFileSpec</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisfilespeca)<br/></td>
<td>Searches a path for any path-delimiting characters (for example, ':' or '\' ). If there are no path-delimiting characters present, the path is considered to be a File Spec path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsHTMLFile</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathishtmlfilea)<br/></td>
<td>Determines if a file is an HTML file. The determination is made based on the content type that is registered for the file's extension.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsLFNFileSpec</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathislfnfilespeca)<br/></td>
<td>Determines whether a file name is in long format.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsNetworkPath</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisnetworkpatha)<br/></td>
<td>Determines whether a path string represents a network resource.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsPrefix</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisprefixa)<br/></td>
<td>Searches a path to determine if it contains a valid prefix of the type passed by <em>pszPrefix</em>. A prefix is one of these types: &quot;C:\\&quot;, &quot;.&quot;, &quot;..&quot;, &quot;..\\&quot;.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsRelative</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisrelativea)<br/></td>
<td>Searches a path and determines if it is relative.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsRoot</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisroota)<br/></td>
<td>Determines whether a path string refers to the root of a volume.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsSameRoot</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathissameroota)<br/></td>
<td>Compares two paths to determine if they have a common root component.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsSystemFolder</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathissystemfoldera)<br/></td>
<td>Determines if an existing folder contains the attributes that make it a system folder. Alternately, this function indicates if certain attributes qualify a folder to be a system folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsUNC</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisunca)<br/></td>
<td>Determines if a path string is a valid Universal Naming Convention (UNC) path, as opposed to a path based on a drive letter.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsUNCServer</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisuncservera)<br/></td>
<td>Determines if a string is a valid UNC for a server path only.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsUNCServerShare</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisuncserversharea)<br/></td>
<td>Determines if a string is a valid UNC share path, \\<em>server</em>\<em>share</em>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsURL</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathisurla)<br/></td>
<td>Tests a given string to determine if it conforms to a valid URL format.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathMakePretty</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathmakeprettya)<br/></td>
<td>Converts an all-uppercase path to all lowercase characters to give the path a consistent appearance.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathMakeSystemFolder</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathmakesystemfoldera)<br/></td>
<td>Gives an existing folder the proper attributes to become a system folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathMatchSpec</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathmatchspeca)<br/></td>
<td>Searches a string using a MS-DOS wildcard match type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathMatchSpecEx</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathmatchspecexa)<br/></td>
<td>Matches a file name from a path against one or more file name patterns.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathParseIconLocation</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathparseiconlocationa)<br/></td>
<td>Parses a file location string that contains a file location and icon index, and returns separate values.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathQuoteSpaces</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathquotespacesa)<br/></td>
<td>Searches a path for spaces. If spaces are found, the entire path is enclosed in quotation marks.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathRelativePathTo</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathrelativepathtoa)<br/></td>
<td>Creates a relative path from one file or folder to another.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathRemoveArgs</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathremoveargsa)<br/></td>
<td>Removes any arguments from a given path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathRemoveBackslash</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathremovebackslasha)<br/></td>
<td>Removes the trailing backslash from a given path.<br/>
<blockquote>
[!Note]<br />
This function is deprecated. We recommend the use of the [<strong>PathCchRemoveBackslash</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchremovebackslash) or [<strong>PathCchRemoveBackslashEx</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchremovebackslashex) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathRemoveBlanks</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathremoveblanksa)<br/></td>
<td>Removes all leading and trailing spaces from a string.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathRemoveExtension</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathremoveextensiona)<br/></td>
<td>Removes the file name extension from a path, if one is present. <br/>
<blockquote>
[!Note]<br />
This function is deprecated. We recommend the use of the [<strong>PathCchRemoveExtension</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchremoveextension) in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathRemoveFileSpec</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathremovefilespeca)<br/></td>
<td>Removes the trailing file name and backslash from a path, if they are present.<br/>
<blockquote>
[!Note]<br />
This function is deprecated. We recommend the use of the [<strong>PathCchRemoveFileSpec</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchremovefilespec) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathRenameExtension</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathrenameextensiona)<br/></td>
<td>Replaces the extension of a file name with a new extension. If the file name does not contain an extension, the extension will be attached to the end of the string.<br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchRenameExtension</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchrenameextension) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathSearchAndQualify</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathsearchandqualifya)<br/></td>
<td>Determines if a given path is correctly formatted and fully qualified.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathSetDlgItemPath</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathsetdlgitempatha)<br/></td>
<td>Sets the text of a child control in a window or dialog box, using [<strong>PathCompactPath</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathcompactpatha) to ensure the path fits in the control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathSkipRoot</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathskiproota)<br/></td>
<td>Retrieves a pointer to the first character in a path following the drive letter or UNC server/share path elements.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathStripPath</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathstrippatha)<br/></td>
<td>Removes the path portion of a fully qualified path and file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathStripToRoot</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathstriptoroota)<br/></td>
<td>Removes all file and directory elements in a path except for the root information.<br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchStripToRoot</strong>](/windows/desktop/api/pathcch/nf-pathcch-pathcchstriptoroot) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathUndecorate</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathundecoratea)<br/></td>
<td>Removes the decoration from a path string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathUnExpandEnvStrings</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathunexpandenvstringsa)<br/></td>
<td>Replaces certain folder names in a fully qualified path with their associated environment string.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathUnmakeSystemFolder</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathunmakesystemfoldera)<br/></td>
<td>Removes the attributes from a folder that make it a system folder. This folder must actually exist in the file system.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathUnquoteSpaces</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-pathunquotespacesa)<br/></td>
<td>Removes quotes from the beginning and end of a path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHSkipJunction</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-shskipjunction)<br/></td>
<td>Checks a bind context to see if it is safe to bind to a particular component object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlApplyScheme</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlapplyschemea)<br/></td>
<td>Determines a scheme for a specified URL string, and returns a string with an appropriate prefix.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlCanonicalize</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlcanonicalizea)<br/></td>
<td>Converts a URL string into canonical form.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlCombine</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlcombinea)<br/></td>
<td>When provided with a relative URL and its base, returns a URL in canonical form.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlCompare</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlcomparea)<br/></td>
<td>Makes a case-sensitive comparison of two URL strings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlCreateFromPath</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlcreatefrompatha)<br/></td>
<td>Converts a MS-DOS path to a canonicalized URL.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlEscape</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlescapea)<br/></td>
<td>Converts characters or surrogate pairs in a URL that might be altered during transport across the Internet (&quot;unsafe&quot; characters) into their corresponding escape sequences. Surrogate pairs are characters between U+10000 to U+10FFFF (in UTF-32) or between DC00 to DFFF (in UTF-16). <br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlEscapeSpaces</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlescapespaces)<br/></td>
<td>A macro that converts space characters into their corresponding escape sequence.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlGetLocation</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlgetlocationa)<br/></td>
<td>Retrieves the location from a URL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlGetPart</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlgetparta)<br/></td>
<td>Accepts a URL string and returns a specified part of that URL.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlHash</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlhasha)<br/></td>
<td>Hashes a URL string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlIs</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlisa)<br/></td>
<td>Tests whether a URL is a specified type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlIsFileUrl</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlisfileurla)<br/></td>
<td>Tests a URL to determine if it is a file URL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlIsNoHistory</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlisnohistorya)<br/></td>
<td>Returns whether a URL is a URL that browsers typically do not include in navigation history.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlIsOpaque</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlisopaquea)<br/></td>
<td>Returns whether a URL is opaque.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlUnescape</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlunescapea)<br/></td>
<td>Converts escape sequences back into ordinary characters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlUnescapeInPlace</strong>](/windows/desktop/api/Shlwapi/nf-shlwapi-urlunescapeinplace)<br/></td>
<td>Converts escape sequences back into ordinary characters and overwrites the original string.<br/></td>
</tr>
</tbody>
</table>



 

 

 




