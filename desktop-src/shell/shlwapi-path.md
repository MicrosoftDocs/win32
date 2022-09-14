---
description: This section describes the Windows Shell path handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.
title: Shell Path Handling Functions
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 31c4afa9-2030-4714-a98b-ed895c9c28a0
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Shell Path Handling Functions

This section describes the Windows Shell path handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.

## In this section




| Topic | Description | 
|-------|-------------|
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathaddbackslasha"><strong>PathAddBackslash</strong></a><br /> | Adds a backslash to the end of a string to create the correct syntax for a path. If the source path already has a trailing backslash, no backslash will be added. <br /><blockquote>[!Note]<br />Misuse of this function can lead to a buffer overrun. We recommend the use of the safer <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchaddbackslash"><strong>PathCchAddBackslash</strong></a> or <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchaddbackslashex"><strong>PathCchAddBackslashEx</strong></a> function in its place.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathaddextensiona"><strong>PathAddExtension</strong></a><br /> | Adds a file name extension to a path string.<br /><blockquote>[!Note]<br />Misuse of this function can lead to a buffer overrun. We recommend the use of the safer <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchaddextension"><strong>PathCchAddExtension</strong></a> function in its place.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathappenda"><strong>PathAppend</strong></a><br /> | Appends one path to the end of another. <br /><blockquote>[!Note]<br />Misuse of this function can lead to a buffer overrun. We recommend the use of the safer <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchappend"><strong>PathCchAppend</strong></a> or <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchappendex"><strong>PathCchAppendEx</strong></a> function in its place.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathbuildroota"><strong>PathBuildRoot</strong></a><br /> | Creates a root path from a given drive number.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathcanonicalizea"><strong>PathCanonicalize</strong></a><br /> | Simplifies a path by removing navigation elements such as "." and ".." to produce a direct, well-formed path.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathcombinea"><strong>PathCombine</strong></a><br /> | Concatenates two strings that represent properly formed paths into one path; also concatenates any relative path elements. <br /><blockquote>[!Note]<br />Misuse of this function can lead to a buffer overrun. We recommend the use of the safer <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchcombine"><strong>PathCchCombine</strong></a> or <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchcombineex"><strong>PathCchCombineEx</strong></a> function in its place.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathcommonprefixa"><strong>PathCommonPrefix</strong></a><br /> | Compares two paths to determine if they share a common prefix. A prefix is one of these types: "C:\\", ".", "..", "..\\".<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathcompactpatha"><strong>PathCompactPath</strong></a><br /> | Truncates a file path to fit within a given pixel width by replacing path components with ellipses.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathcompactpathexa"><strong>PathCompactPathEx</strong></a><br /> | Truncates a path to fit within a certain number of characters by replacing path components with ellipses.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathcreatefromurla"><strong>PathCreateFromUrl</strong></a><br /> | Converts a file URL to a Microsoft MS-DOS path.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathcreatefromurlalloc"><strong>PathCreateFromUrlAlloc</strong></a><br /> | Creates a path from a file URL.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathfileexistsa"><strong>PathFileExists</strong></a><br /> | Determines whether a path to a file system object such as a file or folder is valid.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindextensiona"><strong>PathFindExtension</strong></a><br /> | Searches a path for an extension.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindfilenamea"><strong>PathFindFileName</strong></a><br /> | Searches a path for a file name.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindnextcomponenta"><strong>PathFindNextComponent</strong></a><br /> | Parses a path and returns the portion of that path that follows the first backslash.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindonpatha"><strong>PathFindOnPath</strong></a><br /> | Searches for a file.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathfindsuffixarraya"><strong>PathFindSuffixArray</strong></a><br /> | Determines whether a given file name has one of a list of suffixes.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathgetargsa"><strong>PathGetArgs</strong></a><br /> | Finds the command line arguments within a given path.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathgetchartypea"><strong>PathGetCharType</strong></a><br /> | Determines the type of character in relation to a path.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathgetdrivenumbera"><strong>PathGetDriveNumber</strong></a><br /> | Searches a path for a drive letter within the range of 'A' to 'Z' and returns the corresponding drive number.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathiscontenttypea"><strong>PathIsContentType</strong></a><br /> | Determines if a file's registered content type matches the specified content type. This function obtains the content type for the specified file type and compares that string with the <em>pszContentType</em>. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisdirectorya"><strong>PathIsDirectory</strong></a><br /> | Verifies that a path is a valid directory.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisdirectoryemptya"><strong>PathIsDirectoryEmpty</strong></a><br /> | Determines whether a specified path is an empty directory.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisfilespeca"><strong>PathIsFileSpec</strong></a><br /> | Searches a path for any path-delimiting characters (for example, ':' or '\' ). If there are no path-delimiting characters present, the path is considered to be a File Spec path.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathishtmlfilea"><strong>PathIsHTMLFile</strong></a><br /> | Determines if a file is an HTML file. The determination is made based on the content type that is registered for the file's extension.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathislfnfilespeca"><strong>PathIsLFNFileSpec</strong></a><br /> | Determines whether a file name is in long format.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisnetworkpatha"><strong>PathIsNetworkPath</strong></a><br /> | Determines whether a path string represents a network resource.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisprefixa"><strong>PathIsPrefix</strong></a><br /> | Searches a path to determine if it contains a valid prefix of the type passed by <em>pszPrefix</em>. A prefix is one of these types: "C:\\", ".", "..", "..\\".<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisrelativea"><strong>PathIsRelative</strong></a><br /> | Searches a path and determines if it is relative.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisroota"><strong>PathIsRoot</strong></a><br /> | Determines whether a path string refers to the root of a volume.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathissameroota"><strong>PathIsSameRoot</strong></a><br /> | Compares two paths to determine if they have a common root component.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathissystemfoldera"><strong>PathIsSystemFolder</strong></a><br /> | Determines if an existing folder contains the attributes that make it a system folder. Alternately, this function indicates if certain attributes qualify a folder to be a system folder.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisunca"><strong>PathIsUNC</strong></a><br /> | Determines if a path string is a valid Universal Naming Convention (UNC) path, as opposed to a path based on a drive letter.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisuncservera"><strong>PathIsUNCServer</strong></a><br /> | Determines if a string is a valid UNC for a server path only.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisuncserversharea"><strong>PathIsUNCServerShare</strong></a><br /> | Determines if a string is a valid UNC share path, \\<em>server</em>\<em>share</em>.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathisurla"><strong>PathIsURL</strong></a><br /> | Tests a given string to determine if it conforms to a valid URL format.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathmakeprettya"><strong>PathMakePretty</strong></a><br /> | Converts an all-uppercase path to all lowercase characters to give the path a consistent appearance.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathmakesystemfoldera"><strong>PathMakeSystemFolder</strong></a><br /> | Gives an existing folder the proper attributes to become a system folder.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathmatchspeca"><strong>PathMatchSpec</strong></a><br /> | Searches a string using a MS-DOS wildcard match type.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathmatchspecexa"><strong>PathMatchSpecEx</strong></a><br /> | Matches a file name from a path against one or more file name patterns.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathparseiconlocationa"><strong>PathParseIconLocation</strong></a><br /> | Parses a file location string that contains a file location and icon index, and returns separate values.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathquotespacesa"><strong>PathQuoteSpaces</strong></a><br /> | Searches a path for spaces. If spaces are found, the entire path is enclosed in quotation marks.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathrelativepathtoa"><strong>PathRelativePathTo</strong></a><br /> | Creates a relative path from one file or folder to another.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathremoveargsa"><strong>PathRemoveArgs</strong></a><br /> | Removes any arguments from a given path.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathremovebackslasha"><strong>PathRemoveBackslash</strong></a><br /> | Removes the trailing backslash from a given path.<br /><blockquote>[!Note]<br />This function is deprecated. We recommend the use of the <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchremovebackslash"><strong>PathCchRemoveBackslash</strong></a> or <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchremovebackslashex"><strong>PathCchRemoveBackslashEx</strong></a> function in its place.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathremoveblanksa"><strong>PathRemoveBlanks</strong></a><br /> | Removes all leading and trailing spaces from a string.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathremoveextensiona"><strong>PathRemoveExtension</strong></a><br /> | Removes the file name extension from a path, if one is present. <br /><blockquote>[!Note]<br />This function is deprecated. We recommend the use of the <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchremoveextension"><strong>PathCchRemoveExtension</strong></a> in its place.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathremovefilespeca"><strong>PathRemoveFileSpec</strong></a><br /> | Removes the trailing file name and backslash from a path, if they are present.<br /><blockquote>[!Note]<br />This function is deprecated. We recommend the use of the <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchremovefilespec"><strong>PathCchRemoveFileSpec</strong></a> function in its place.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathrenameextensiona"><strong>PathRenameExtension</strong></a><br /> | Replaces the extension of a file name with a new extension. If the file name does not contain an extension, the extension will be attached to the end of the string.<br /><blockquote>[!Note]<br />Misuse of this function can lead to a buffer overrun. We recommend the use of the safer <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchrenameextension"><strong>PathCchRenameExtension</strong></a> function in its place.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathsearchandqualifya"><strong>PathSearchAndQualify</strong></a><br /> | Determines if a given path is correctly formatted and fully qualified.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathsetdlgitempatha"><strong>PathSetDlgItemPath</strong></a><br /> | Sets the text of a child control in a window or dialog box, using <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathcompactpatha"><strong>PathCompactPath</strong></a> to ensure the path fits in the control.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathskiproota"><strong>PathSkipRoot</strong></a><br /> | Retrieves a pointer to the first character in a path following the drive letter or UNC server/share path elements.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathstrippatha"><strong>PathStripPath</strong></a><br /> | Removes the path portion of a fully qualified path and file.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathstriptoroota"><strong>PathStripToRoot</strong></a><br /> | Removes all file and directory elements in a path except for the root information.<br /><blockquote>[!Note]<br />Misuse of this function can lead to a buffer overrun. We recommend the use of the safer <a href="/windows/desktop/api/pathcch/nf-pathcch-pathcchstriptoroot"><strong>PathCchStripToRoot</strong></a> function in its place.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathundecoratea"><strong>PathUndecorate</strong></a><br /> | Removes the decoration from a path string.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathunexpandenvstringsa"><strong>PathUnExpandEnvStrings</strong></a><br /> | Replaces certain folder names in a fully qualified path with their associated environment string.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathunmakesystemfoldera"><strong>PathUnmakeSystemFolder</strong></a><br /> | Removes the attributes from a folder that make it a system folder. This folder must actually exist in the file system.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-pathunquotespacesa"><strong>PathUnquoteSpaces</strong></a><br /> | Removes quotes from the beginning and end of a path.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-shskipjunction"><strong>SHSkipJunction</strong></a><br /> | Checks a bind context to see if it is safe to bind to a particular component object.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlapplyschemea"><strong>UrlApplyScheme</strong></a><br /> | Determines a scheme for a specified URL string, and returns a string with an appropriate prefix.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlcanonicalizea"><strong>UrlCanonicalize</strong></a><br /> | Converts a URL string into canonical form.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlcombinea"><strong>UrlCombine</strong></a><br /> | When provided with a relative URL and its base, returns a URL in canonical form.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlcomparea"><strong>UrlCompare</strong></a><br /> | Makes a case-sensitive comparison of two URL strings.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlcreatefrompatha"><strong>UrlCreateFromPath</strong></a><br /> | Converts a MS-DOS path to a canonicalized URL.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlescapea"><strong>UrlEscape</strong></a><br /> | Converts characters or surrogate pairs in a URL that might be altered during transport across the Internet ("unsafe" characters) into their corresponding escape sequences. Surrogate pairs are characters between U+10000 to U+10FFFF (in UTF-32) or between DC00 to DFFF (in UTF-16). <br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlescapespaces"><strong>UrlEscapeSpaces</strong></a><br /> | A macro that converts space characters into their corresponding escape sequence.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlgetlocationa"><strong>UrlGetLocation</strong></a><br /> | Retrieves the location from a URL.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlgetparta"><strong>UrlGetPart</strong></a><br /> | Accepts a URL string and returns a specified part of that URL.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlhasha"><strong>UrlHash</strong></a><br /> | Hashes a URL string.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlisa"><strong>UrlIs</strong></a><br /> | Tests whether a URL is a specified type.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlisfileurla"><strong>UrlIsFileUrl</strong></a><br /> | Tests a URL to determine if it is a file URL.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlisnohistorya"><strong>UrlIsNoHistory</strong></a><br /> | Returns whether a URL is a URL that browsers typically do not include in navigation history.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlisopaquea"><strong>UrlIsOpaque</strong></a><br /> | Returns whether a URL is opaque.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlunescapea"><strong>UrlUnescape</strong></a><br /> | Converts escape sequences back into ordinary characters.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-urlunescapeinplace"><strong>UrlUnescapeInPlace</strong></a><br /> | Converts escape sequences back into ordinary characters and overwrites the original string.<br /> | 




 

 

 




