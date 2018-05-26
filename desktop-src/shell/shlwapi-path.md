---
Description: This section describes the Windows Shell path handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.
title: Shell Path Handling Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<td>[<strong>PathAddBackslash</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathaddbackslasha?branch=master)<br/></td>
<td>Adds a backslash to the end of a string to create the correct syntax for a path. If the source path already has a trailing backslash, no backslash will be added. <br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchAddBackslash</strong>](/windows/win32/pathcch/nf-pathcch-pathcchaddbackslash?branch=master) or [<strong>PathCchAddBackslashEx</strong>](/windows/win32/pathcch/nf-pathcch-pathcchaddbackslashex?branch=master) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathAddExtension</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathaddextensiona?branch=master)<br/></td>
<td>Adds a file name extension to a path string.<br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchAddExtension</strong>](/windows/win32/pathcch/nf-pathcch-pathcchaddextension?branch=master) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathAppend</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathappenda?branch=master)<br/></td>
<td>Appends one path to the end of another. <br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchAppend</strong>](/windows/win32/pathcch/nf-pathcch-pathcchappend?branch=master) or [<strong>PathCchAppendEx</strong>](/windows/win32/pathcch/nf-pathcch-pathcchappendex?branch=master) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathBuildRoot</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathbuildroota?branch=master)<br/></td>
<td>Creates a root path from a given drive number.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathCanonicalize</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathcanonicalizea?branch=master)<br/></td>
<td>Simplifies a path by removing navigation elements such as &quot;.&quot; and &quot;..&quot; to produce a direct, well-formed path.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathCombine</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathcombinea?branch=master)<br/></td>
<td>Concatenates two strings that represent properly formed paths into one path; also concatenates any relative path elements. <br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchCombine</strong>](/windows/win32/pathcch/nf-pathcch-pathcchcombine?branch=master) or [<strong>PathCchCombineEx</strong>](/windows/win32/pathcch/nf-pathcch-pathcchcombineex?branch=master) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathCommonPrefix</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathcommonprefixa?branch=master)<br/></td>
<td>Compares two paths to determine if they share a common prefix. A prefix is one of these types: &quot;C:\\&quot;, &quot;.&quot;, &quot;..&quot;, &quot;..\\&quot;.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathCompactPath</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathcompactpatha?branch=master)<br/></td>
<td>Truncates a file path to fit within a given pixel width by replacing path components with ellipses.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathCompactPathEx</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathcompactpathexa?branch=master)<br/></td>
<td>Truncates a path to fit within a certain number of characters by replacing path components with ellipses.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathCreateFromUrl</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathcreatefromurla?branch=master)<br/></td>
<td>Converts a file URL to a Microsoft MS-DOS path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathCreateFromUrlAlloc</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathcreatefromurlalloc?branch=master)<br/></td>
<td>Creates a path from a file URL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathFileExists</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathfileexistsa?branch=master)<br/></td>
<td>Determines whether a path to a file system object such as a file or folder is valid.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathFindExtension</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathfindextensiona?branch=master)<br/></td>
<td>Searches a path for an extension.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathFindFileName</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathfindfilenamea?branch=master)<br/></td>
<td>Searches a path for a file name.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathFindNextComponent</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathfindnextcomponenta?branch=master)<br/></td>
<td>Parses a path and returns the portion of that path that follows the first backslash.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathFindOnPath</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathfindonpatha?branch=master)<br/></td>
<td>Searches for a file.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathFindSuffixArray</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathfindsuffixarraya?branch=master)<br/></td>
<td>Determines whether a given file name has one of a list of suffixes.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathGetArgs</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathgetargsa?branch=master)<br/></td>
<td>Finds the command line arguments within a given path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathGetCharType</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathgetchartypea?branch=master)<br/></td>
<td>Determines the type of character in relation to a path.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathGetDriveNumber</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathgetdrivenumbera?branch=master)<br/></td>
<td>Searches a path for a drive letter within the range of 'A' to 'Z' and returns the corresponding drive number.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsContentType</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathiscontenttypea?branch=master)<br/></td>
<td>Determines if a file's registered content type matches the specified content type. This function obtains the content type for the specified file type and compares that string with the <em>pszContentType</em>. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsDirectory</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisdirectorya?branch=master)<br/></td>
<td>Verifies that a path is a valid directory.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsDirectoryEmpty</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisdirectoryemptya?branch=master)<br/></td>
<td>Determines whether a specified path is an empty directory.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsFileSpec</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisfilespeca?branch=master)<br/></td>
<td>Searches a path for any path-delimiting characters (for example, ':' or '\' ). If there are no path-delimiting characters present, the path is considered to be a File Spec path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsHTMLFile</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathishtmlfilea?branch=master)<br/></td>
<td>Determines if a file is an HTML file. The determination is made based on the content type that is registered for the file's extension.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsLFNFileSpec</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathislfnfilespeca?branch=master)<br/></td>
<td>Determines whether a file name is in long format.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsNetworkPath</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisnetworkpatha?branch=master)<br/></td>
<td>Determines whether a path string represents a network resource.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsPrefix</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisprefixa?branch=master)<br/></td>
<td>Searches a path to determine if it contains a valid prefix of the type passed by <em>pszPrefix</em>. A prefix is one of these types: &quot;C:\\&quot;, &quot;.&quot;, &quot;..&quot;, &quot;..\\&quot;.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsRelative</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisrelativea?branch=master)<br/></td>
<td>Searches a path and determines if it is relative.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsRoot</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisroota?branch=master)<br/></td>
<td>Determines whether a path string refers to the root of a volume.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsSameRoot</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathissameroota?branch=master)<br/></td>
<td>Compares two paths to determine if they have a common root component.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsSystemFolder</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathissystemfoldera?branch=master)<br/></td>
<td>Determines if an existing folder contains the attributes that make it a system folder. Alternately, this function indicates if certain attributes qualify a folder to be a system folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsUNC</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisunca?branch=master)<br/></td>
<td>Determines if a path string is a valid Universal Naming Convention (UNC) path, as opposed to a path based on a drive letter.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsUNCServer</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisuncservera?branch=master)<br/></td>
<td>Determines if a string is a valid UNC for a server path only.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathIsUNCServerShare</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisuncserversharea?branch=master)<br/></td>
<td>Determines if a string is a valid UNC share path, \\<em>server</em>\<em>share</em>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathIsURL</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathisurla?branch=master)<br/></td>
<td>Tests a given string to determine if it conforms to a valid URL format.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathMakePretty</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathmakeprettya?branch=master)<br/></td>
<td>Converts an all-uppercase path to all lowercase characters to give the path a consistent appearance.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathMakeSystemFolder</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathmakesystemfoldera?branch=master)<br/></td>
<td>Gives an existing folder the proper attributes to become a system folder.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathMatchSpec</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathmatchspeca?branch=master)<br/></td>
<td>Searches a string using a MS-DOS wildcard match type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathMatchSpecEx</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathmatchspecexa?branch=master)<br/></td>
<td>Matches a file name from a path against one or more file name patterns.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathParseIconLocation</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathparseiconlocationa?branch=master)<br/></td>
<td>Parses a file location string that contains a file location and icon index, and returns separate values.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathQuoteSpaces</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathquotespacesa?branch=master)<br/></td>
<td>Searches a path for spaces. If spaces are found, the entire path is enclosed in quotation marks.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathRelativePathTo</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathrelativepathtoa?branch=master)<br/></td>
<td>Creates a relative path from one file or folder to another.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathRemoveArgs</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathremoveargsa?branch=master)<br/></td>
<td>Removes any arguments from a given path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathRemoveBackslash</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathremovebackslasha?branch=master)<br/></td>
<td>Removes the trailing backslash from a given path.<br/>
<blockquote>
[!Note]<br />
This function is deprecated. We recommend the use of the [<strong>PathCchRemoveBackslash</strong>](/windows/win32/pathcch/nf-pathcch-pathcchremovebackslash?branch=master) or [<strong>PathCchRemoveBackslashEx</strong>](/windows/win32/pathcch/nf-pathcch-pathcchremovebackslashex?branch=master) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathRemoveBlanks</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathremoveblanksa?branch=master)<br/></td>
<td>Removes all leading and trailing spaces from a string.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathRemoveExtension</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathremoveextensiona?branch=master)<br/></td>
<td>Removes the file name extension from a path, if one is present. <br/>
<blockquote>
[!Note]<br />
This function is deprecated. We recommend the use of the [<strong>PathCchRemoveExtension</strong>](/windows/win32/pathcch/nf-pathcch-pathcchremoveextension?branch=master) in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathRemoveFileSpec</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathremovefilespeca?branch=master)<br/></td>
<td>Removes the trailing file name and backslash from a path, if they are present.<br/>
<blockquote>
[!Note]<br />
This function is deprecated. We recommend the use of the [<strong>PathCchRemoveFileSpec</strong>](/windows/win32/pathcch/nf-pathcch-pathcchremovefilespec?branch=master) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathRenameExtension</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathrenameextensiona?branch=master)<br/></td>
<td>Replaces the extension of a file name with a new extension. If the file name does not contain an extension, the extension will be attached to the end of the string.<br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchRenameExtension</strong>](/windows/win32/pathcch/nf-pathcch-pathcchrenameextension?branch=master) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathSearchAndQualify</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathsearchandqualifya?branch=master)<br/></td>
<td>Determines if a given path is correctly formatted and fully qualified.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathSetDlgItemPath</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathsetdlgitempatha?branch=master)<br/></td>
<td>Sets the text of a child control in a window or dialog box, using [<strong>PathCompactPath</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathcompactpatha?branch=master) to ensure the path fits in the control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathSkipRoot</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathskiproota?branch=master)<br/></td>
<td>Retrieves a pointer to the first character in a path following the drive letter or UNC server/share path elements.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathStripPath</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathstrippatha?branch=master)<br/></td>
<td>Removes the path portion of a fully qualified path and file.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathStripToRoot</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathstriptoroota?branch=master)<br/></td>
<td>Removes all file and directory elements in a path except for the root information.<br/>
<blockquote>
[!Note]<br />
Misuse of this function can lead to a buffer overrun. We recommend the use of the safer [<strong>PathCchStripToRoot</strong>](/windows/win32/pathcch/nf-pathcch-pathcchstriptoroot?branch=master) function in its place.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathUndecorate</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathundecoratea?branch=master)<br/></td>
<td>Removes the decoration from a path string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathUnExpandEnvStrings</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathunexpandenvstringsa?branch=master)<br/></td>
<td>Replaces certain folder names in a fully qualified path with their associated environment string.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PathUnmakeSystemFolder</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathunmakesystemfoldera?branch=master)<br/></td>
<td>Removes the attributes from a folder that make it a system folder. This folder must actually exist in the file system.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PathUnquoteSpaces</strong>](/windows/win32/Shlwapi/nf-shlwapi-pathunquotespacesa?branch=master)<br/></td>
<td>Removes quotes from the beginning and end of a path.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHSkipJunction</strong>](/windows/win32/Shlwapi/nf-shlwapi-shskipjunction?branch=master)<br/></td>
<td>Checks a bind context to see if it is safe to bind to a particular component object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlApplyScheme</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlapplyschemea?branch=master)<br/></td>
<td>Determines a scheme for a specified URL string, and returns a string with an appropriate prefix.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlCanonicalize</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlcanonicalizea?branch=master)<br/></td>
<td>Converts a URL string into canonical form.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlCombine</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlcombinea?branch=master)<br/></td>
<td>When provided with a relative URL and its base, returns a URL in canonical form.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlCompare</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlcomparea?branch=master)<br/></td>
<td>Makes a case-sensitive comparison of two URL strings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlCreateFromPath</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlcreatefrompatha?branch=master)<br/></td>
<td>Converts a MS-DOS path to a canonicalized URL.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlEscape</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlescapea?branch=master)<br/></td>
<td>Converts characters or surrogate pairs in a URL that might be altered during transport across the Internet (&quot;unsafe&quot; characters) into their corresponding escape sequences. Surrogate pairs are characters between U+10000 to U+10FFFF (in UTF-32) or between DC00 to DFFF (in UTF-16). <br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlEscapeSpaces</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlescapespaces?branch=master)<br/></td>
<td>A macro that converts space characters into their corresponding escape sequence.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlGetLocation</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlgetlocationa?branch=master)<br/></td>
<td>Retrieves the location from a URL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlGetPart</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlgetparta?branch=master)<br/></td>
<td>Accepts a URL string and returns a specified part of that URL.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlHash</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlhasha?branch=master)<br/></td>
<td>Hashes a URL string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlIs</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlisa?branch=master)<br/></td>
<td>Tests whether a URL is a specified type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlIsFileUrl</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlisfileurla?branch=master)<br/></td>
<td>Tests a URL to determine if it is a file URL.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlIsNoHistory</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlisnohistorya?branch=master)<br/></td>
<td>Returns whether a URL is a URL that browsers typically do not include in navigation history.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlIsOpaque</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlisopaquea?branch=master)<br/></td>
<td>Returns whether a URL is opaque.<br/></td>
</tr>
<tr class="even">
<td>[<strong>UrlUnescape</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlunescapea?branch=master)<br/></td>
<td>Converts escape sequences back into ordinary characters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>UrlUnescapeInPlace</strong>](/windows/win32/Shlwapi/nf-shlwapi-urlunescapeinplace?branch=master)<br/></td>
<td>Converts escape sequences back into ordinary characters and overwrites the original string.<br/></td>
</tr>
</tbody>
</table>



 

 

 




