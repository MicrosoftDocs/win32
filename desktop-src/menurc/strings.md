---
title: Strings
description: This section discusses the string functions.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\resources\strings.htm'
keywords:
- resources,strings
- strings
- string functions
ms.topic: article
ms.date: 05/31/2018
---

# Strings

This section describes the string functions and explains how to use them in your applications.

### In This Section



| Name                                     | Description                                             |
|------------------------------------------|---------------------------------------------------------|
| [About Strings](about-strings.md)       | Discusses the string functions.<br/>              |
| [About Strsafe.h](strsafe-ovw.md)       | Discusses the string functions in Strsafe.h.<br/> |
| [String Reference](string-reference.md) | Contains the API reference.<br/>                  |



 

### String Functions



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-charlowera"><strong>CharLower</strong></a></td>
<td>Converts a character string or a single character to lowercase. If the operand is a character string, the function converts the characters in place. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-charlowerbuffa"><strong>CharLowerBuff</strong></a></td>
<td>Converts uppercase characters in a buffer to lowercase characters. The function converts the characters in place. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-charnexta"><strong>CharNext</strong></a></td>
<td>Retrieves a pointer to the next character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-charnextexa"><strong>CharNextExA</strong></a></td>
<td>Retrieves the pointer to the next character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-charpreva"><strong>CharPrev</strong></a></td>
<td>Retrieves a pointer to the preceding character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-charprevexa"><strong>CharPrevExA</strong></a></td>
<td>Retrieves the pointer to the preceding character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-chartooema"><strong>CharToOem</strong></a></td>
<td>Translates a string into the OEM-defined character set.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-chartooembuffa"><strong>CharToOemBuff</strong></a></td>
<td>Translates a specified number of characters in a string into the OEM-defined character set.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-charuppera"><strong>CharUpper</strong></a></td>
<td>Converts a character string or a single character to uppercase. If the operand is a character string, the function converts the characters in place. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-charupperbuffa"><strong>CharUpperBuff</strong></a></td>
<td>Converts lowercase characters in a buffer to uppercase characters. The function converts the characters in place. <br/></td>
</tr>
<tr class="odd">
<td><a href="https://docs.microsoft.com/windows/desktop/api/stringapiset/nf-stringapiset-comparestringw"><strong>CompareString</strong></a></td>
<td>Compares two character strings, using the specified locale.
<blockquote>
[!Note]<br />
For compatibility with Unicode, use <a href="https://docs.microsoft.com/windows/desktop/api/stringapiset/nf-stringapiset-comparestringex"><strong>CompareStringEx</strong></a> or the Unicode version of <a href="https://docs.microsoft.com/windows/desktop/api/stringapiset/nf-stringapiset-comparestringw"><strong>CompareString</strong></a>.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td><a href="https://docs.microsoft.com/windows/desktop/api/stringapiset/nf-stringapiset-comparestringex"><strong>CompareStringEx</strong></a></td>
<td>Compares two Unicode (wide character) strings, using the specified locale.<br/></td>
</tr>
<tr class="odd">
<td><a href="https://docs.microsoft.com/windows/desktop/api/stringapiset/nf-stringapiset-foldstringw"><strong>FoldString</strong></a></td>
<td>Maps one string to another, performing a specified transformation option. <br/></td>
</tr>
<tr class="even">
<td><a href="https://docs.microsoft.com/windows/desktop/api/winnls/nf-winnls-getstringtypea"><strong>GetStringTypeA</strong></a></td>
<td>Retrieves character-type information for the characters in the specified source string. For each character in the string, the function sets one or more bits in the corresponding 16-bit element of the output array. Each bit identifies a given character type, such as whether the character is a letter, a digit, or neither.<br/></td>
</tr>
<tr class="odd">
<td><a href="https://docs.microsoft.com/windows/desktop/api/winnls/nf-winnls-getstringtypeexa"><strong>GetStringTypeEx</strong></a></td>
<td>Retrieves character-type information for the characters in the specified source string. For each character in the string, the function sets one or more bits in the corresponding 16-bit element of the output array. Each bit identifies a given character type, such as whether the character is a letter, a digit, or neither. <br/> Unlike its close relatives <a href="https://docs.microsoft.com/windows/desktop/api/winnls/nf-winnls-getstringtypea"><strong>GetStringTypeA</strong></a> and <a href="https://docs.microsoft.com/windows/desktop/api/stringapiset/nf-stringapiset-getstringtypew"><strong>GetStringTypeW</strong></a>, <a href="https://docs.microsoft.com/windows/desktop/api/winnls/nf-winnls-getstringtypeexa"><strong>GetStringTypeEx</strong></a> exhibits standard behavior through the use of the <strong>#define UNICODE</strong> switch. It is the recommended function.<br/></td>
</tr>
<tr class="even">
<td><a href="https://docs.microsoft.com/windows/desktop/api/stringapiset/nf-stringapiset-getstringtypew"><strong>GetStringTypeW</strong></a></td>
<td>Retrieves character-type information for the characters in the specified source string. For each character in the string, the function sets one or more bits in the corresponding 16-bit element of the output array. Each bit identifies a given character type, such as whether the character is a letter, a digit, or neither.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-ischaralphaa"><strong>IsCharAlpha</strong></a></td>
<td>Determines whether a character is an alphabetical character. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-ischaralphanumerica"><strong>IsCharAlphaNumeric</strong></a></td>
<td>Determines whether a character is either an alphabetical or a numeric character. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-ischarlowera"><strong>IsCharLower</strong></a></td>
<td>Determines whether a character is lowercase. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-ischaruppera"><strong>IsCharUpper</strong></a></td>
<td>Determines whether a character is uppercase. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-loadstringa"><strong>LoadString</strong></a></td>
<td>Loads a string resource from the executable file associated with a specified module, copies the string into a buffer, and appends a terminating NULL character.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winbase/nf-winbase-lstrcata"><strong>lstrcat</strong></a></td>
<td>Appends one string to another.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winbase/nf-winbase-lstrcmpa"><strong>lstrcmp</strong></a></td>
<td>Compares two character strings. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winbase/nf-winbase-lstrcmpia"><strong>lstrcmpi</strong></a></td>
<td>Compares two character strings. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winbase/nf-winbase-lstrcpya"><strong>lstrcpy</strong></a></td>
<td>Copies a string to a buffer.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winbase/nf-winbase-lstrcpyna"><strong>lstrcpyn</strong></a></td>
<td>Copies a specified number of characters from a source string into a buffer. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winbase/nf-winbase-lstrlena"><strong>lstrlen</strong></a></td>
<td>Determines the length of the specified string (not including the terminating null character).<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-oemtochara"><strong>OemToChar</strong></a></td>
<td>Translates a string from the OEM-defined character set into either an ANSI or a wide-character string.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-oemtocharbuffa"><strong>OemToCharBuff</strong></a></td>
<td>Translates a specified number of characters in a string from the OEM-defined character set into either an ANSI or a wide-character string.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-wsprintfa"><strong>wsprintf</strong></a></td>
<td>Writes formatted data to the specified buffer.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Winuser/nf-winuser-wvsprintfa"><strong>wvsprintf</strong></a></td>
<td>Writes formatted data to the specified buffer using a pointer to a list of arguments.<br/></td>
</tr>
</tbody>
</table>



 

### Strsafe Functions



| Name                                             | Description                                                                                      |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**StringCbCat**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcata)               | Concatenates one string to another string.<br/>                                            |
| [**StringCbCatEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcatexa)           | Concatenates one string to another string.<br/>                                            |
| [**StringCbCatN**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcatna)             | Concatenates the specified number of bytes from one string to another string.<br/>         |
| [**StringCbCatNEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcatnexa)         | Concatenates the specified number of bytes from one string to another string.<br/>         |
| [**StringCbCopy**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopya)             | Copies one string to another.<br/>                                                         |
| [**StringCbCopyEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopyexa)         | Copies one string to another.<br/>                                                         |
| [**StringCbCopyN**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopyna)           | Copies the specified number of bytes from one string to another.<br/>                      |
| [**StringCbCopyNEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbcopynexa)       | Copies the specified number of bytes from one string to another.<br/>                      |
| [**StringCbGets**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbgetsa)             | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCbGetsEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbgetsexa)         | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCbLength**](/windows/desktop/api/Strsafe/nf-strsafe-stringcblengtha)         | Determines whether a string exceeds the specified length, in bytes.<br/>                   |
| [**StringCbPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbprintfa)         | Writes formatted data to the specified string.<br/>                                        |
| [**StringCbPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbprintfexa)     | Writes formatted data to the specified string.<br/>                                        |
| [**StringCbVPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbvprintfa)       | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |
| [**StringCbVPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcbvprintfexa)   | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |
| [**StringCchCat**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcata)             | Concatenates one string to another string.<br/>                                            |
| [**StringCchCatEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcatexa)         | Concatenates one string to another string.<br/>                                            |
| [**StringCchCatN**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcatna)           | Concatenates the specified number of characters from one string to another string.<br/>    |
| [**StringCchCatNEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcatnexa)       | Concatenates the specified number of characters from one string to another string.<br/>    |
| [**StringCchCopy**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopya)           | Copies one string to another.<br/>                                                         |
| [**StringCchCopyEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopyexa)       | Copies one string to another.<br/>                                                         |
| [**StringCchCopyN**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopyna)         | Copies the specified number of characters from one string to another.<br/>                 |
| [**StringCchCopyNEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchcopynexa)     | Copies the specified number of characters from one string to another.<br/>                 |
| [**StringCchGets**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchgetsa)           | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCchGetsEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchgetsexa)       | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCchLength**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchlengtha)       | Determines whether a string exceeds the specified length, in characters.<br/>              |
| [**StringCchPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchprintfa)       | Writes formatted data to the specified string.<br/>                                        |
| [**StringCchPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchprintfexa)   | Writes formatted data to the specified string.<br/>                                        |
| [**StringCchVPrintf**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchvprintfa)     | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |
| [**StringCchVPrintfEx**](/windows/desktop/api/Strsafe/nf-strsafe-stringcchvprintfexa) | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |



 

 

 





