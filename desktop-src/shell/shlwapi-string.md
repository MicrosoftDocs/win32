---
Description: 'This section describes the Windows Shell string handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.'
title: Shell String Handling Functions
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
<td>[<strong>ChrCmpI</strong>](chrcmpi.md)<br/></td>
<td>Performs a comparison between two characters. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetAcceptLanguages</strong>](getacceptlanguages.md)<br/></td>
<td>Retrieves a string used with websites when specifying language preferences.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IntlStrEqN</strong>](intlstreqn.md)<br/></td>
<td>Performs a case-sensitive comparison of a specified number of characters from the beginning of two localized strings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IntlStrEqNI</strong>](intlstreqni.md)<br/></td>
<td>Performs a case-insensitive comparison of a specified number of characters from the beginning of two localized strings.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IntlStrEqWorker</strong>](intlstreqworker.md)<br/></td>
<td>Compares a specified number of characters from the beginning of two localized strings.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IsCharSpace</strong>](ischarspace.md)<br/></td>
<td>Determines whether a character represents a space.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SHLoadIndirectString</strong>](shloadindirectstring.md)<br/></td>
<td>Extracts a specified text resource when given that resource in the form of an indirect string (a string that begins with the '@' symbol).<br/></td>
</tr>
<tr class="even">
<td>[<strong>SHStrDup</strong>](shstrdup.md)<br/></td>
<td>Makes a copy of a string in newly allocated memory.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCat</strong>](strcat.md)<br/></td>
<td>Appends one string to another. <br/>
<blockquote>
[!Note]<br />
Do not use. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCatBuff</strong>](strcatbuff.md)<br/></td>
<td>Copies and appends characters from one string to the end of another. <br/>
<blockquote>
[!Note]<br />
Do not use. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCatChainW</strong>](strcatchainw.md)<br/></td>
<td>Concatenates two Unicode strings. Used when repeated concatenations to the same buffer are required.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrChr</strong>](strchr.md)<br/></td>
<td>Searches a string for the first occurrence of a character that matches the specified character. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrChrI</strong>](strchri.md)<br/></td>
<td>Searches a string for the first occurrence of a character that matches the specified character. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrChrNIW</strong>](strchrniw.md)<br/></td>
<td>Searches a string for the first occurrence of a specified character. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrChrNW</strong>](strchrnw.md)<br/></td>
<td>Searches a string for the first occurrence of a specified character. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmp</strong>](strcmp.md)<br/></td>
<td>Compares two strings to determine if they are the same. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCmpC</strong>](strcmpc.md)<br/></td>
<td>Compares strings using C run-time (ASCII) collation rules. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmpI</strong>](strcmpi.md)<br/></td>
<td>Compares two strings to determine if they are the same. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCmpIC</strong>](strcmpic.md)<br/></td>
<td>Compares two strings using C run-time (ASCII) collation rules. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmpLogicalW</strong>](strcmplogicalw.md)<br/></td>
<td>Compares two Unicode strings. Digits in the strings are considered as numerical content rather than text. This test is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCmpN</strong>](strcmpn.md)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings to determine if they are the same. The comparison is case-sensitive. The <strong>StrNCmp</strong> macro differs from this function in name only.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmpNC</strong>](strcmpnc.md)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings using C run-time (ASCII) collation rules. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCmpNI</strong>](strcmpni.md)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings to determine if they are the same. The comparison is not case-sensitive. The <strong>StrNCmpI</strong> macro differs from this function in name only.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCmpNIC</strong>](strcmpnic.md)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings using C run-time (ASCII) collation rules. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCpy</strong>](strcpy.md)<br/></td>
<td>Copies one string to another. <br/>
<blockquote>
[!Note]<br />
Do not use. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCpyN</strong>](strcpyn.md)<br/></td>
<td>Copies a specified number of characters from the beginning of one string to another.<br/>
<blockquote>
[!Note]<br />
Do not use this function or the <strong>StrNCpy</strong> macro. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrCSpn</strong>](strcspn.md)<br/></td>
<td>Searches a string for the first occurrence of any of a group of characters. The search method is case-sensitive, and the terminating <strong>NULL</strong> character is included within the search pattern match.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrCSpnI</strong>](strcspni.md)<br/></td>
<td>Searches a string for the first occurrence of any of a group of characters. The search method is not case-sensitive, and the terminating <strong>NULL</strong> character is included within the search pattern match.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrDup</strong>](strdup.md)<br/></td>
<td>Duplicates a string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrFormatByteSize64</strong>](strformatbytesize64a.md)<br/></td>
<td>Converts a numeric value into a string that represents the number expressed as a size value in bytes, kilobytes, megabytes, or gigabytes, depending on the size.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrFormatByteSizeA</strong>](strformatbytesizea.md)<br/></td>
<td>Converts a numeric value into a string that represents the number expressed as a size value in bytes, kilobytes, megabytes, or gigabytes, depending on the size. Differs from [<strong>StrFormatByteSizeW</strong>](strformatbytesizew.md) in one parameter type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrFormatByteSizeEx</strong>](strformatbytesizeex.md)<br/></td>
<td>Converts a numeric value into a string that represents the number in bytes, kilobytes, megabytes, or gigabytes, depending on the size. Extends [<strong>StrFormatByteSizeW</strong>](strformatbytesizew.md) by offering the option to round to the nearest displayed digit or to discard undisplayed digits.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrFormatByteSizeW</strong>](strformatbytesizew.md)<br/></td>
<td>Converts a numeric value into a string that represents the number expressed as a size value in bytes, kilobytes, megabytes, or gigabytes, depending on the size. Differs from [<strong>StrFormatByteSizeA</strong>](strformatbytesizea.md) in one parameter type.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrFormatKBSize</strong>](strformatkbsize.md)<br/></td>
<td>Converts a numeric value into a string that represents the number expressed as a size value in kilobytes.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrFromTimeInterval</strong>](strfromtimeinterval.md)<br/></td>
<td>Converts a time interval, specified in milliseconds, to a string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrIsIntlEqual</strong>](strisintlequal.md)<br/></td>
<td>Compares a specified number of characters from the beginning of two strings to determine if they are equal.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrNCat</strong>](strncat.md)<br/></td>
<td>Appends a specified number of characters from the beginning of one string to the end of another. <br/>
<blockquote>
[!Note]<br />
Do not use this function or the <strong>StrCatN</strong> macro. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrPBrk</strong>](strpbrk.md)<br/></td>
<td>Searches a string for the first occurrence of a character contained in a specified buffer. This search does not include the terminating null character.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrRChr</strong>](strrchr.md)<br/></td>
<td>Searches a string for the last occurrence of a specified character. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrRChrI</strong>](strrchri.md)<br/></td>
<td>Searches a string for the last occurrence of a specified character. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrRetToBSTR</strong>](strrettobstr.md)<br/></td>
<td>Accepts a [<strong>STRRET</strong>](strret.md) structure returned by [<strong>IShellFolder::GetDisplayNameOf</strong>](ishellfolder-getdisplaynameof.md) that contains or points to a string, and returns that string as a [<strong>BSTR</strong>](1b2d7d2c-47af-4389-a6b6-b01b7e915228).<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrRetToBuf</strong>](strrettobuf.md)<br/></td>
<td>Converts an [<strong>STRRET</strong>](strret.md) structure returned by [<strong>IShellFolder::GetDisplayNameOf</strong>](ishellfolder-getdisplaynameof.md) to a string, and places the result in a buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrRetToStr</strong>](strrettostr.md)<br/></td>
<td>Takes an [<strong>STRRET</strong>](strret.md) structure returned by [<strong>IShellFolder::GetDisplayNameOf</strong>](ishellfolder-getdisplaynameof.md) and returns a pointer to an allocated string containing the display name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrRetToStrN</strong>](strrettostrn.md)<br/></td>
<td>Takes an [<strong>STRRET</strong>](strret.md) structure returned by [<strong>IShellFolder::GetDisplayNameOf</strong>](ishellfolder-getdisplaynameof.md), converts it to a string, and places the result in a buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrRStrI</strong>](strrstri.md)<br/></td>
<td>Searches for the last occurrence of a specified substring within a string. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrSpn</strong>](strspn.md)<br/></td>
<td>Obtains the length of a substring within a string that consists entirely of characters contained in a specified buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrStr</strong>](strstr.md)<br/></td>
<td>Finds the first occurrence of a substring within a string. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrStrI</strong>](strstri.md)<br/></td>
<td>Finds the first occurrence of a substring within a string. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrToInt</strong>](strtoint.md)<br/></td>
<td>Converts a string that represents a decimal value to an integer. The <strong>StrToLong</strong> macro is identical to this function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrToInt64Ex</strong>](strtoint64ex.md)<br/></td>
<td>Converts a string representing a decimal or hexadecimal value to a 64-bit integer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>StrToIntEx</strong>](strtointex.md)<br/></td>
<td>Converts a string representing a decimal or hexadecimal number to an integer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>StrTrim</strong>](strtrim.md)<br/></td>
<td>Removes specified leading and trailing characters from a string.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>wnsprintf</strong>](wnsprintf.md)<br/></td>
<td>Takes a variable-length argument list and returns the values of the arguments as a [<strong>printf</strong>](77a854ae-5b48-4865-89f4-f2dc5cf80f52)-style formatted string. <br/>
<blockquote>
[!Note]<br />
Do not use this function. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>wvnsprintf</strong>](wvnsprintf.md)<br/></td>
<td>Takes a list of arguments and returns the values of the arguments as a [<strong>printf</strong>](77a854ae-5b48-4865-89f4-f2dc5cf80f52)-style formatted string. <br/>
<blockquote>
[!Note]<br />
Do not use this function. See Remarks for alternative functions.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 




