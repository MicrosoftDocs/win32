---
Description: This section describes the Windows Shell string handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.
title: Shell String Handling Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shell String Handling Functions

This section describes the Windows Shell string handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.

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
<td>[<strong>ChrCmpI</strong>](/windows/win32/Shlwapi/nf-shlwapi-chrcmpia?branch=master)<br/></td>
<td>Performs a comparison between two characters. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetAcceptLanguages</strong>](/windows/win32/Shlwapi/nf-shlwapi-getacceptlanguagesa?branch=master)<br/></td>
<td>Retrieves a string used with websites when specifying language preferences.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IntlStrEqN</strong>](/windows/win32/Shlwapi/nf-shlwapi-intlstreqna?branch=master)<br/></td>
<td>Performs a case-sensitive comparison of a specified number of characters from the beginning of two localized strings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IntlStrEqNI</strong>](/windows/win32/Shlwapi/nf-shlwapi-intlstreqnia?branch=master)<br/></td>
<td>Performs a case-insensitive comparison of a specified number of characters from the beginning of two localized strings.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IntlStrEqWorker</strong>](/windows/win32/Shlwapi/nf-shlwapi-intlstreqworkera?branch=master)<br/></td>
<td>Compares a specified number of characters from the beginning of two localized strings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IsCharSpace</strong>](/windows/win32/Shlwapi/nf-shlwapi-ischarspacea?branch=master)<br/></td>
<td>Determines whether a character represents a space.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHLoadIndirectString</strong>](/windows/win32/Shlwapi/nf-shlwapi-shloadindirectstring?branch=master)<br/></td>
<td>Extracts a specified text resource when given that resource in the form of an indirect string (a string that begins with the '@' symbol).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHStrDup</strong>](/windows/win32/Shlwapi/nf-shlwapi-shstrdupa?branch=master)<br/></td>
<td>Makes a copy of a string in newly allocated memory.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCat</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcatw?branch=master)<br/></td>
<td>Appends one string to another. <br/>
<blockquote>
[!Note]<br />
Do not use. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCatBuff</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcatbuffa?branch=master)<br/></td>
<td>Copies and appends characters from one string to the end of another. <br/>
<blockquote>
[!Note]<br />
Do not use. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCatChainW</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcatchainw?branch=master)<br/></td>
<td>Concatenates two Unicode strings. Used when repeated concatenations to the same buffer are required.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrChr</strong>](/windows/win32/Shlwapi/nf-shlwapi-strchra?branch=master)<br/></td>
<td>Searches a string for the first occurrence of a character that matches the specified character. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrChrI</strong>](/windows/win32/Shlwapi/nf-shlwapi-strchria?branch=master)<br/></td>
<td>Searches a string for the first occurrence of a character that matches the specified character. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrChrNIW</strong>](/windows/win32/Shlwapi/nf-shlwapi-strchrniw?branch=master)<br/></td>
<td>Searches a string for the first occurrence of a specified character. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrChrNW</strong>](/windows/win32/Shlwapi/nf-shlwapi-strchrnw?branch=master)<br/></td>
<td>Searches a string for the first occurrence of a specified character. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmp</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcmpw?branch=master)<br/></td>
<td>Compares two strings to determine if they are the same. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCmpC</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcmpca?branch=master)<br/></td>
<td>Compares strings using C run-time (ASCII) collation rules. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmpI</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcmpiw?branch=master)<br/></td>
<td>Compares two strings to determine if they are the same. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCmpIC</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcmpica?branch=master)<br/></td>
<td>Compares two strings using C run-time (ASCII) collation rules. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmpLogicalW</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcmplogicalw?branch=master)<br/></td>
<td>Compares two Unicode strings. Digits in the strings are considered as numerical content rather than text. This test is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCmpN</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcmpna?branch=master)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings to determine if they are the same. The comparison is case-sensitive. The <strong>StrNCmp</strong> macro differs from this function in name only.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmpNC</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcmpnca?branch=master)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings using C run-time (ASCII) collation rules. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCmpNI</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcmpnia?branch=master)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings to determine if they are the same. The comparison is not case-sensitive. The <strong>StrNCmpI</strong> macro differs from this function in name only.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmpNIC</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcmpnica?branch=master)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings using C run-time (ASCII) collation rules. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCpy</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcpyw?branch=master)<br/></td>
<td>Copies one string to another. <br/>
<blockquote>
[!Note]<br />
Do not use. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCpyN</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcpynw?branch=master)<br/></td>
<td>Copies a specified number of characters from the beginning of one string to another.<br/>
<blockquote>
[!Note]<br />
Do not use this function or the <strong>StrNCpy</strong> macro. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCSpn</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcspna?branch=master)<br/></td>
<td>Searches a string for the first occurrence of any of a group of characters. The search method is case-sensitive, and the terminating <strong>NULL</strong> character is included within the search pattern match.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCSpnI</strong>](/windows/win32/Shlwapi/nf-shlwapi-strcspnia?branch=master)<br/></td>
<td>Searches a string for the first occurrence of any of a group of characters. The search method is not case-sensitive, and the terminating <strong>NULL</strong> character is included within the search pattern match.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrDup</strong>](/windows/win32/Shlwapi/nf-shlwapi-strdupa?branch=master)<br/></td>
<td>Duplicates a string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrFormatByteSize64</strong>](/windows/win32/Shlwapi/nf-shlwapi-strformatbytesize64a?branch=master)<br/></td>
<td>Converts a numeric value into a string that represents the number expressed as a size value in bytes, kilobytes, megabytes, or gigabytes, depending on the size.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrFormatByteSizeA</strong>](/windows/win32/Shlwapi/nf-shlwapi-strformatbytesizea?branch=master)<br/></td>
<td>Converts a numeric value into a string that represents the number expressed as a size value in bytes, kilobytes, megabytes, or gigabytes, depending on the size. Differs from [<strong>StrFormatByteSizeW</strong>](/windows/win32/Shlwapi/nf-shlwapi-strformatbytesizew?branch=master) in one parameter type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrFormatByteSizeEx</strong>](/windows/win32/Shlwapi/nf-shlwapi-strformatbytesizeex?branch=master)<br/></td>
<td>Converts a numeric value into a string that represents the number in bytes, kilobytes, megabytes, or gigabytes, depending on the size. Extends [<strong>StrFormatByteSizeW</strong>](/windows/win32/Shlwapi/nf-shlwapi-strformatbytesizew?branch=master) by offering the option to round to the nearest displayed digit or to discard undisplayed digits.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrFormatByteSizeW</strong>](/windows/win32/Shlwapi/nf-shlwapi-strformatbytesizew?branch=master)<br/></td>
<td>Converts a numeric value into a string that represents the number expressed as a size value in bytes, kilobytes, megabytes, or gigabytes, depending on the size. Differs from [<strong>StrFormatByteSizeA</strong>](/windows/win32/Shlwapi/nf-shlwapi-strformatbytesizea?branch=master) in one parameter type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrFormatKBSize</strong>](/windows/win32/Shlwapi/nf-shlwapi-strformatkbsizea?branch=master)<br/></td>
<td>Converts a numeric value into a string that represents the number expressed as a size value in kilobytes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrFromTimeInterval</strong>](/windows/win32/Shlwapi/nf-shlwapi-strfromtimeintervala?branch=master)<br/></td>
<td>Converts a time interval, specified in milliseconds, to a string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrIsIntlEqual</strong>](/windows/win32/Shlwapi/nf-shlwapi-strisintlequala?branch=master)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings to determine if they are equal.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrNCat</strong>](/windows/win32/Shlwapi/nf-shlwapi-strncata?branch=master)<br/></td>
<td>Appends a specified number of characters from the beginning of one string to the end of another. <br/>
<blockquote>
[!Note]<br />
Do not use this function or the <strong>StrCatN</strong> macro. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrPBrk</strong>](/windows/win32/Shlwapi/nf-shlwapi-strpbrka?branch=master)<br/></td>
<td>Searches a string for the first occurrence of a character contained in a specified buffer. This search does not include the terminating null character.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrRChr</strong>](/windows/win32/Shlwapi/nf-shlwapi-strrchra?branch=master)<br/></td>
<td>Searches a string for the last occurrence of a specified character. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrRChrI</strong>](/windows/win32/Shlwapi/nf-shlwapi-strrchria?branch=master)<br/></td>
<td>Searches a string for the last occurrence of a specified character. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrRetToBSTR</strong>](/windows/win32/Shlwapi/nf-shlwapi-strrettobstr?branch=master)<br/></td>
<td>Accepts a [<strong>STRRET</strong>](/windows/win32/Shtypes/ns-shtypes-_strret?branch=master) structure returned by [<strong>IShellFolder::GetDisplayNameOf</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof?branch=master) that contains or points to a string, and returns that string as a [<strong>BSTR</strong>](1b2d7d2c-47af-4389-a6b6-b01b7e915228).<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrRetToBuf</strong>](/windows/win32/Shlwapi/nf-shlwapi-strrettobufa?branch=master)<br/></td>
<td>Converts an [<strong>STRRET</strong>](/windows/win32/Shtypes/ns-shtypes-_strret?branch=master) structure returned by [<strong>IShellFolder::GetDisplayNameOf</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof?branch=master) to a string, and places the result in a buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrRetToStr</strong>](/windows/win32/Shlwapi/nf-shlwapi-strrettostra?branch=master)<br/></td>
<td>Takes an [<strong>STRRET</strong>](/windows/win32/Shtypes/ns-shtypes-_strret?branch=master) structure returned by [<strong>IShellFolder::GetDisplayNameOf</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof?branch=master) and returns a pointer to an allocated string containing the display name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrRetToStrN</strong>](strrettostrn.md)<br/></td>
<td>Takes an [<strong>STRRET</strong>](/windows/win32/Shtypes/ns-shtypes-_strret?branch=master) structure returned by [<strong>IShellFolder::GetDisplayNameOf</strong>](/windows/win32/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof?branch=master), converts it to a string, and places the result in a buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrRStrI</strong>](/windows/win32/Shlwapi/nf-shlwapi-strrstria?branch=master)<br/></td>
<td>Searches for the last occurrence of a specified substring within a string. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrSpn</strong>](/windows/win32/Shlwapi/nf-shlwapi-strspna?branch=master)<br/></td>
<td>Obtains the length of a substring within a string that consists entirely of characters contained in a specified buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrStr</strong>](/windows/win32/Shlwapi/nf-shlwapi-strstra?branch=master)<br/></td>
<td>Finds the first occurrence of a substring within a string. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrStrI</strong>](/windows/win32/Shlwapi/nf-shlwapi-strstria?branch=master)<br/></td>
<td>Finds the first occurrence of a substring within a string. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrToInt</strong>](/windows/win32/Shlwapi/nf-shlwapi-strtointa?branch=master)<br/></td>
<td>Converts a string that represents a decimal value to an integer. The <strong>StrToLong</strong> macro is identical to this function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrToInt64Ex</strong>](/windows/win32/Shlwapi/nf-shlwapi-strtoint64exa?branch=master)<br/></td>
<td>Converts a string representing a decimal or hexadecimal value to a 64-bit integer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrToIntEx</strong>](/windows/win32/Shlwapi/nf-shlwapi-strtointexa?branch=master)<br/></td>
<td>Converts a string representing a decimal or hexadecimal number to an integer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrTrim</strong>](/windows/win32/Shlwapi/nf-shlwapi-strtrima?branch=master)<br/></td>
<td>Removes specified leading and trailing characters from a string.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>wnsprintf</strong>](/windows/win32/Shlwapi/nf-shlwapi-wnsprintfa?branch=master)<br/></td>
<td>Takes a variable-length argument list and returns the values of the arguments as a [<strong>printf</strong>](77a854ae-5b48-4865-89f4-f2dc5cf80f52)-style formatted string. <br/>
<blockquote>
[!Note]<br />
Do not use this function. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>wvnsprintf</strong>](/windows/win32/Shlwapi/nf-shlwapi-wvnsprintfa?branch=master)<br/></td>
<td>Takes a list of arguments and returns the values of the arguments as a [<strong>printf</strong>](77a854ae-5b48-4865-89f4-f2dc5cf80f52)-style formatted string. <br/>
<blockquote>
[!Note]<br />
Do not use this function. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 




