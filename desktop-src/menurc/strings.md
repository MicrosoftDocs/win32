---
title: Strings
description: This section discusses the string functions.
ms.assetid: f1799fbf-4619-4b19-998e-b1d2f4c19a35
keywords:
- resources,strings
- strings
- string functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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
<td>[<strong>CharLower</strong>](/windows/desktop/api/Winuser/nf-winuser-charlowera)</td>
<td>Converts a character string or a single character to lowercase. If the operand is a character string, the function converts the characters in place. <br/></td>
</tr>
<tr class="even">
<td>[<strong>CharLowerBuff</strong>](/windows/desktop/api/Winuser/nf-winuser-charlowerbuffa)</td>
<td>Converts uppercase characters in a buffer to lowercase characters. The function converts the characters in place. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharNext</strong>](/windows/desktop/api/Winuser/nf-winuser-charnexta)</td>
<td>Retrieves a pointer to the next character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CharNextExA</strong>](/windows/desktop/api/Winuser/nf-winuser-charnextexa)</td>
<td>Retrieves the pointer to the next character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharPrev</strong>](/windows/desktop/api/Winuser/nf-winuser-charpreva)</td>
<td>Retrieves a pointer to the preceding character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CharPrevExA</strong>](/windows/desktop/api/Winuser/nf-winuser-charprevexa)</td>
<td>Retrieves the pointer to the preceding character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharToOem</strong>](/windows/desktop/api/Winuser/nf-winuser-chartooema)</td>
<td>Translates a string into the OEM-defined character set.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CharToOemBuff</strong>](/windows/desktop/api/Winuser/nf-winuser-chartooembuffa)</td>
<td>Translates a specified number of characters in a string into the OEM-defined character set.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharUpper</strong>](/windows/desktop/api/Winuser/nf-winuser-charuppera)</td>
<td>Converts a character string or a single character to uppercase. If the operand is a character string, the function converts the characters in place. <br/></td>
</tr>
<tr class="even">
<td>[<strong>CharUpperBuff</strong>](/windows/desktop/api/Winuser/nf-winuser-charupperbuffa)</td>
<td>Converts lowercase characters in a buffer to uppercase characters. The function converts the characters in place. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>CompareString</strong>](https://msdn.microsoft.com/library/windows/desktop/dd317759)</td>
<td>Compares two character strings, using the specified locale.
<blockquote>
[!Note]<br />
For compatibility with Unicode, use [<strong>CompareStringEx</strong>](https://msdn.microsoft.com/library/windows/desktop/dd317761) or the Unicode version of [<strong>CompareString</strong>](https://msdn.microsoft.com/library/windows/desktop/dd317759).
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>CompareStringEx</strong>](https://msdn.microsoft.com/library/windows/desktop/dd317761)</td>
<td>Compares two Unicode (wide character) strings, using the specified locale.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FoldString</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318063)</td>
<td>Maps one string to another, performing a specified transformation option. <br/></td>
</tr>
<tr class="even">
<td>[<strong>GetStringTypeA</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318117)</td>
<td>Retrieves character-type information for the characters in the specified source string. For each character in the string, the function sets one or more bits in the corresponding 16-bit element of the output array. Each bit identifies a given character type, such as whether the character is a letter, a digit, or neither.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetStringTypeEx</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318118)</td>
<td>Retrieves character-type information for the characters in the specified source string. For each character in the string, the function sets one or more bits in the corresponding 16-bit element of the output array. Each bit identifies a given character type, such as whether the character is a letter, a digit, or neither. <br/> Unlike its close relatives [<strong>GetStringTypeA</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318117) and [<strong>GetStringTypeW</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318119), [<strong>GetStringTypeEx</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318118) exhibits standard behavior through the use of the <strong>#define UNICODE</strong> switch. It is the recommended function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetStringTypeW</strong>](https://msdn.microsoft.com/library/windows/desktop/dd318119)</td>
<td>Retrieves character-type information for the characters in the specified source string. For each character in the string, the function sets one or more bits in the corresponding 16-bit element of the output array. Each bit identifies a given character type, such as whether the character is a letter, a digit, or neither.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsCharAlpha</strong>](/windows/desktop/api/Winuser/nf-winuser-ischaralphaa)</td>
<td>Determines whether a character is an alphabetical character. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IsCharAlphaNumeric</strong>](/windows/desktop/api/Winuser/nf-winuser-ischaralphanumerica)</td>
<td>Determines whether a character is either an alphabetical or a numeric character. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsCharLower</strong>](/windows/desktop/api/Winuser/nf-winuser-ischarlowera)</td>
<td>Determines whether a character is lowercase. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IsCharUpper</strong>](/windows/desktop/api/Winuser/nf-winuser-ischaruppera)</td>
<td>Determines whether a character is uppercase. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>LoadString</strong>](/windows/desktop/api/Winuser/nf-winuser-loadstringa)</td>
<td>Loads a string resource from the executable file associated with a specified module, copies the string into a buffer, and appends a terminating NULL character.<br/></td>
</tr>
<tr class="even">
<td>[<strong>lstrcat</strong>](/windows/desktop/api/Winbase/nf-winbase-lstrcata)</td>
<td>Appends one string to another.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>lstrcmp</strong>](/windows/desktop/api/Winbase/nf-winbase-lstrcmpa)</td>
<td>Compares two character strings. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>lstrcmpi</strong>](/windows/desktop/api/Winbase/nf-winbase-lstrcmpia)</td>
<td>Compares two character strings. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>lstrcpy</strong>](/windows/desktop/api/Winbase/nf-winbase-lstrcpya)</td>
<td>Copies a string to a buffer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>lstrcpyn</strong>](/windows/desktop/api/Winbase/nf-winbase-lstrcpyna)</td>
<td>Copies a specified number of characters from a source string into a buffer. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>lstrlen</strong>](/windows/desktop/api/Winbase/nf-winbase-lstrlena)</td>
<td>Determines the length of the specified string (not including the terminating null character).<br/></td>
</tr>
<tr class="even">
<td>[<strong>OemToChar</strong>](/windows/desktop/api/Winuser/nf-winuser-oemtochara)</td>
<td>Translates a string from the OEM-defined character set into either an ANSI or a wide-character string.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OemToCharBuff</strong>](/windows/desktop/api/Winuser/nf-winuser-oemtocharbuffa)</td>
<td>Translates a specified number of characters in a string from the OEM-defined character set into either an ANSI or a wide-character string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>wsprintf</strong>](/windows/desktop/api/Winuser/nf-winuser-wsprintfa)</td>
<td>Writes formatted data to the specified buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>wvsprintf</strong>](/windows/desktop/api/Winuser/nf-winuser-wvsprintfa)</td>
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



 

 

 





