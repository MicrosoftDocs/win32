---
description: This section describes the Windows Shell string handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.
title: Shell String Handling Functions
ms.topic: article
ms.date: 05/31/2018
ms.assetid: c7329e22-c9bf-4845-bc0a-a155d1bd2005
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Shell String Handling Functions

This section describes the Windows Shell string handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.

## In this section




| Topic | Description | 
|-------|-------------|
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-chrcmpia"><strong>ChrCmpI</strong></a><br /> | Performs a comparison between two characters. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-getacceptlanguagesa"><strong>GetAcceptLanguages</strong></a><br /> | Retrieves a string used with websites when specifying language preferences.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-intlstreqna"><strong>IntlStrEqN</strong></a><br /> | Performs a case-sensitive comparison of a specified number of characters from the beginning of two localized strings.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-intlstreqnia"><strong>IntlStrEqNI</strong></a><br /> | Performs a case-insensitive comparison of a specified number of characters from the beginning of two localized strings.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-intlstreqworkera"><strong>IntlStrEqWorker</strong></a><br /> | Compares a specified number of characters from the beginning of two localized strings.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-ischarspacea"><strong>IsCharSpace</strong></a><br /> | Determines whether a character represents a space.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-shloadindirectstring"><strong>SHLoadIndirectString</strong></a><br /> | Extracts a specified text resource when given that resource in the form of an indirect string (a string that begins with the '@' symbol).<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-shstrdupa"><strong>SHStrDup</strong></a><br /> | Makes a copy of a string in newly allocated memory.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcatw"><strong>StrCat</strong></a><br /> | Appends one string to another. <br /><blockquote>[!Note]<br />Do not use. See Remarks for alternative functions.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcatbuffa"><strong>StrCatBuff</strong></a><br /> | Copies and appends characters from one string to the end of another. <br /><blockquote>[!Note]<br />Do not use. See Remarks for alternative functions.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcatchainw"><strong>StrCatChainW</strong></a><br /> | Concatenates two Unicode strings. Used when repeated concatenations to the same buffer are required.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strchra"><strong>StrChr</strong></a><br /> | Searches a string for the first occurrence of a character that matches the specified character. The comparison is case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strchria"><strong>StrChrI</strong></a><br /> | Searches a string for the first occurrence of a character that matches the specified character. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strchrniw"><strong>StrChrNIW</strong></a><br /> | Searches a string for the first occurrence of a specified character. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strchrnw"><strong>StrChrNW</strong></a><br /> | Searches a string for the first occurrence of a specified character. The comparison is case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcmpw"><strong>StrCmp</strong></a><br /> | Compares two strings to determine if they are the same. The comparison is case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcmpca"><strong>StrCmpC</strong></a><br /> | Compares strings using C run-time (ASCII) collation rules. The comparison is case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcmpiw"><strong>StrCmpI</strong></a><br /> | Compares two strings to determine if they are the same. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcmpica"><strong>StrCmpIC</strong></a><br /> | Compares two strings using C run-time (ASCII) collation rules. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcmplogicalw"><strong>StrCmpLogicalW</strong></a><br /> | Compares two Unicode strings. Digits in the strings are considered as numerical content rather than text. This test is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcmpna"><strong>StrCmpN</strong></a><br /> | Compares a specified number of characters from the beginning of two strings to determine if they are the same. The comparison is case-sensitive. The <strong>StrNCmp</strong> macro differs from this function in name only.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcmpnca"><strong>StrCmpNC</strong></a><br /> | Compares a specified number of characters from the beginning of two strings using C run-time (ASCII) collation rules. The comparison is case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcmpnia"><strong>StrCmpNI</strong></a><br /> | Compares a specified number of characters from the beginning of two strings to determine if they are the same. The comparison is not case-sensitive. The <strong>StrNCmpI</strong> macro differs from this function in name only.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcmpnica"><strong>StrCmpNIC</strong></a><br /> | Compares a specified number of characters from the beginning of two strings using C run-time (ASCII) collation rules. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcpyw"><strong>StrCpy</strong></a><br /> | Copies one string to another. <br /><blockquote>[!Note]<br />Do not use. See Remarks for alternative functions.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcpynw"><strong>StrCpyN</strong></a><br /> | Copies a specified number of characters from the beginning of one string to another.<br /><blockquote>[!Note]<br />Do not use this function or the <strong>StrNCpy</strong> macro. See Remarks for alternative functions.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcspna"><strong>StrCSpn</strong></a><br /> | Searches a string for the first occurrence of any of a group of characters. The search method is case-sensitive, and the terminating <strong>NULL</strong> character is included within the search pattern match.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strcspnia"><strong>StrCSpnI</strong></a><br /> | Searches a string for the first occurrence of any of a group of characters. The search method is not case-sensitive, and the terminating <strong>NULL</strong> character is included within the search pattern match.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strdupa"><strong>StrDup</strong></a><br /> | Duplicates a string.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strformatbytesize64a"><strong>StrFormatByteSize64</strong></a><br /> | Converts a numeric value into a string that represents the number expressed as a size value in bytes, kilobytes, megabytes, or gigabytes, depending on the size.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strformatbytesizea"><strong>StrFormatByteSizeA</strong></a><br /> | Converts a numeric value into a string that represents the number expressed as a size value in bytes, kilobytes, megabytes, or gigabytes, depending on the size. Differs from <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strformatbytesizew"><strong>StrFormatByteSizeW</strong></a> in one parameter type.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strformatbytesizeex"><strong>StrFormatByteSizeEx</strong></a><br /> | Converts a numeric value into a string that represents the number in bytes, kilobytes, megabytes, or gigabytes, depending on the size. Extends <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strformatbytesizew"><strong>StrFormatByteSizeW</strong></a> by offering the option to round to the nearest displayed digit or to discard undisplayed digits.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strformatbytesizew"><strong>StrFormatByteSizeW</strong></a><br /> | Converts a numeric value into a string that represents the number expressed as a size value in bytes, kilobytes, megabytes, or gigabytes, depending on the size. Differs from <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strformatbytesizea"><strong>StrFormatByteSizeA</strong></a> in one parameter type.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strformatkbsizea"><strong>StrFormatKBSize</strong></a><br /> | Converts a numeric value into a string that represents the number expressed as a size value in kilobytes.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strfromtimeintervala"><strong>StrFromTimeInterval</strong></a><br /> | Converts a time interval, specified in milliseconds, to a string.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strisintlequala"><strong>StrIsIntlEqual</strong></a><br /> | Compares a specified number of characters from the beginning of two strings to determine if they are equal.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strncata"><strong>StrNCat</strong></a><br /> | Appends a specified number of characters from the beginning of one string to the end of another. <br /><blockquote>[!Note]<br />Do not use this function or the <strong>StrCatN</strong> macro. See Remarks for alternative functions.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strpbrka"><strong>StrPBrk</strong></a><br /> | Searches a string for the first occurrence of a character contained in a specified buffer. This search does not include the terminating null character.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strrchra"><strong>StrRChr</strong></a><br /> | Searches a string for the last occurrence of a specified character. The comparison is case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strrchria"><strong>StrRChrI</strong></a><br /> | Searches a string for the last occurrence of a specified character. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strrettobstr"><strong>StrRetToBSTR</strong></a><br /> | Accepts a <a href="/windows/desktop/api/Shtypes/ns-shtypes-strret"><strong>STRRET</strong></a> structure returned by <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof"><strong>IShellFolder::GetDisplayNameOf</strong></a> that contains or points to a string, and returns that string as a <a href="/previous-versions/windows/desktop/automat/bstr"><strong>BSTR</strong></a>.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strrettobufa"><strong>StrRetToBuf</strong></a><br /> | Converts an <a href="/windows/desktop/api/Shtypes/ns-shtypes-strret"><strong>STRRET</strong></a> structure returned by <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof"><strong>IShellFolder::GetDisplayNameOf</strong></a> to a string, and places the result in a buffer.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strrettostra"><strong>StrRetToStr</strong></a><br /> | Takes an <a href="/windows/desktop/api/Shtypes/ns-shtypes-strret"><strong>STRRET</strong></a> structure returned by <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof"><strong>IShellFolder::GetDisplayNameOf</strong></a> and returns a pointer to an allocated string containing the display name.<br /> | 
| <a href="strrettostrn.md"><strong>StrRetToStrN</strong></a><br /> | Takes an <a href="/windows/desktop/api/Shtypes/ns-shtypes-strret"><strong>STRRET</strong></a> structure returned by <a href="/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof"><strong>IShellFolder::GetDisplayNameOf</strong></a>, converts it to a string, and places the result in a buffer.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strrstria"><strong>StrRStrI</strong></a><br /> | Searches for the last occurrence of a specified substring within a string. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strspna"><strong>StrSpn</strong></a><br /> | Obtains the length of a substring within a string that consists entirely of characters contained in a specified buffer.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strstra"><strong>StrStr</strong></a><br /> | Finds the first occurrence of a substring within a string. The comparison is case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strstria"><strong>StrStrI</strong></a><br /> | Finds the first occurrence of a substring within a string. The comparison is not case-sensitive.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strtointa"><strong>StrToInt</strong></a><br /> | Converts a string that represents a decimal value to an integer. The <strong>StrToLong</strong> macro is identical to this function.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strtoint64exa"><strong>StrToInt64Ex</strong></a><br /> | Converts a string representing a decimal or hexadecimal value to a 64-bit integer.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strtointexa"><strong>StrToIntEx</strong></a><br /> | Converts a string representing a decimal or hexadecimal number to an integer.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-strtrima"><strong>StrTrim</strong></a><br /> | Removes specified leading and trailing characters from a string.<br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-wnsprintfa"><strong>wnsprintf</strong></a><br /> | Takes a variable-length argument list and returns the values of the arguments as a <a href="https://www.microsoft.com/download/details.aspx?id=55979"><strong>printf</strong></a>-style formatted string. <br /><blockquote>[!Note]<br />Do not use this function. See Remarks for alternative functions.</blockquote><br /> | 
| <a href="/windows/desktop/api/Shlwapi/nf-shlwapi-wvnsprintfa"><strong>wvnsprintf</strong></a><br /> | Takes a list of arguments and returns the values of the arguments as a <a href="https://www.microsoft.com/download/details.aspx?id=55979"><strong>printf</strong></a>-style formatted string. <br /><blockquote>[!Note]<br />Do not use this function. See Remarks for alternative functions.</blockquote><br /> | 




 

 

 
