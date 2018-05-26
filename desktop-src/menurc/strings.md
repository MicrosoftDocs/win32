---
title: Strings
description: This section discusses the string functions.
ms.assetid: f1799fbf-4619-4b19-998e-b1d2f4c19a35
keywords:
- resources,strings
- strings
- string functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<td>[<strong>CharLower</strong>](/windows/win32/Winuser/nf-winuser-charlowera?branch=master)</td>
<td>Converts a character string or a single character to lowercase. If the operand is a character string, the function converts the characters in place. <br/></td>
</tr>
<tr class="even">
<td>[<strong>CharLowerBuff</strong>](/windows/win32/Winuser/nf-winuser-charlowerbuffa?branch=master)</td>
<td>Converts uppercase characters in a buffer to lowercase characters. The function converts the characters in place. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharNext</strong>](/windows/win32/Winuser/nf-winuser-charnexta?branch=master)</td>
<td>Retrieves a pointer to the next character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CharNextExA</strong>](/windows/win32/Winuser/nf-winuser-charnextexa?branch=master)</td>
<td>Retrieves the pointer to the next character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharPrev</strong>](/windows/win32/Winuser/nf-winuser-charpreva?branch=master)</td>
<td>Retrieves a pointer to the preceding character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CharPrevExA</strong>](/windows/win32/Winuser/nf-winuser-charprevexa?branch=master)</td>
<td>Retrieves the pointer to the preceding character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharToOem</strong>](/windows/win32/Winuser/nf-winuser-chartooema?branch=master)</td>
<td>Translates a string into the OEM-defined character set.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CharToOemBuff</strong>](/windows/win32/Winuser/nf-winuser-chartooembuffa?branch=master)</td>
<td>Translates a specified number of characters in a string into the OEM-defined character set.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharUpper</strong>](/windows/win32/Winuser/nf-winuser-charuppera?branch=master)</td>
<td>Converts a character string or a single character to uppercase. If the operand is a character string, the function converts the characters in place. <br/></td>
</tr>
<tr class="even">
<td>[<strong>CharUpperBuff</strong>](/windows/win32/Winuser/nf-winuser-charupperbuffa?branch=master)</td>
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
<td>[<strong>IsCharAlpha</strong>](/windows/win32/Winuser/nf-winuser-ischaralphaa?branch=master)</td>
<td>Determines whether a character is an alphabetical character. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IsCharAlphaNumeric</strong>](/windows/win32/Winuser/nf-winuser-ischaralphanumerica?branch=master)</td>
<td>Determines whether a character is either an alphabetical or a numeric character. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsCharLower</strong>](/windows/win32/Winuser/nf-winuser-ischarlowera?branch=master)</td>
<td>Determines whether a character is lowercase. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IsCharUpper</strong>](/windows/win32/Winuser/nf-winuser-ischaruppera?branch=master)</td>
<td>Determines whether a character is uppercase. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>LoadString</strong>](/windows/win32/Winuser/nf-winuser-loadstringa?branch=master)</td>
<td>Loads a string resource from the executable file associated with a specified module, copies the string into a buffer, and appends a terminating NULL character.<br/></td>
</tr>
<tr class="even">
<td>[<strong>lstrcat</strong>](/windows/win32/Winbase/nf-winbase-lstrcata?branch=master)</td>
<td>Appends one string to another.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>lstrcmp</strong>](/windows/win32/Winbase/nf-winbase-lstrcmpa?branch=master)</td>
<td>Compares two character strings. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>lstrcmpi</strong>](/windows/win32/Winbase/nf-winbase-lstrcmpia?branch=master)</td>
<td>Compares two character strings. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>lstrcpy</strong>](/windows/win32/Winbase/nf-winbase-lstrcpya?branch=master)</td>
<td>Copies a string to a buffer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>lstrcpyn</strong>](/windows/win32/Winbase/nf-winbase-lstrcpyna?branch=master)</td>
<td>Copies a specified number of characters from a source string into a buffer. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>lstrlen</strong>](/windows/win32/Winbase/nf-winbase-lstrlena?branch=master)</td>
<td>Determines the length of the specified string (not including the terminating null character).<br/></td>
</tr>
<tr class="even">
<td>[<strong>OemToChar</strong>](/windows/win32/Winuser/nf-winuser-oemtochara?branch=master)</td>
<td>Translates a string from the OEM-defined character set into either an ANSI or a wide-character string.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OemToCharBuff</strong>](/windows/win32/Winuser/nf-winuser-oemtocharbuffa?branch=master)</td>
<td>Translates a specified number of characters in a string from the OEM-defined character set into either an ANSI or a wide-character string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>wsprintf</strong>](/windows/win32/Winuser/nf-winuser-wsprintfa?branch=master)</td>
<td>Writes formatted data to the specified buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>wvsprintf</strong>](/windows/win32/Winuser/nf-winuser-wvsprintfa?branch=master)</td>
<td>Writes formatted data to the specified buffer using a pointer to a list of arguments.<br/></td>
</tr>
</tbody>
</table>



 

### Strsafe Functions



| Name                                             | Description                                                                                      |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**StringCbCat**](/windows/win32/Strsafe/nf-strsafe-stringcbcata?branch=master)               | Concatenates one string to another string.<br/>                                            |
| [**StringCbCatEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcatexa?branch=master)           | Concatenates one string to another string.<br/>                                            |
| [**StringCbCatN**](/windows/win32/Strsafe/nf-strsafe-stringcbcatna?branch=master)             | Concatenates the specified number of bytes from one string to another string.<br/>         |
| [**StringCbCatNEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcatnexa?branch=master)         | Concatenates the specified number of bytes from one string to another string.<br/>         |
| [**StringCbCopy**](/windows/win32/Strsafe/nf-strsafe-stringcbcopya?branch=master)             | Copies one string to another.<br/>                                                         |
| [**StringCbCopyEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcopyexa?branch=master)         | Copies one string to another.<br/>                                                         |
| [**StringCbCopyN**](/windows/win32/Strsafe/nf-strsafe-stringcbcopyna?branch=master)           | Copies the specified number of bytes from one string to another.<br/>                      |
| [**StringCbCopyNEx**](/windows/win32/Strsafe/nf-strsafe-stringcbcopynexa?branch=master)       | Copies the specified number of bytes from one string to another.<br/>                      |
| [**StringCbGets**](/windows/win32/Strsafe/nf-strsafe-stringcbgetsa?branch=master)             | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCbGetsEx**](/windows/win32/Strsafe/nf-strsafe-stringcbgetsexa?branch=master)         | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCbLength**](/windows/win32/Strsafe/nf-strsafe-stringcblengtha?branch=master)         | Determines whether a string exceeds the specified length, in bytes.<br/>                   |
| [**StringCbPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcbprintfa?branch=master)         | Writes formatted data to the specified string.<br/>                                        |
| [**StringCbPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcbprintfexa?branch=master)     | Writes formatted data to the specified string.<br/>                                        |
| [**StringCbVPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcbvprintfa?branch=master)       | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |
| [**StringCbVPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcbvprintfexa?branch=master)   | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |
| [**StringCchCat**](/windows/win32/Strsafe/nf-strsafe-stringcchcata?branch=master)             | Concatenates one string to another string.<br/>                                            |
| [**StringCchCatEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcatexa?branch=master)         | Concatenates one string to another string.<br/>                                            |
| [**StringCchCatN**](/windows/win32/Strsafe/nf-strsafe-stringcchcatna?branch=master)           | Concatenates the specified number of characters from one string to another string.<br/>    |
| [**StringCchCatNEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcatnexa?branch=master)       | Concatenates the specified number of characters from one string to another string.<br/>    |
| [**StringCchCopy**](/windows/win32/Strsafe/nf-strsafe-stringcchcopya?branch=master)           | Copies one string to another.<br/>                                                         |
| [**StringCchCopyEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcopyexa?branch=master)       | Copies one string to another.<br/>                                                         |
| [**StringCchCopyN**](/windows/win32/Strsafe/nf-strsafe-stringcchcopyna?branch=master)         | Copies the specified number of characters from one string to another.<br/>                 |
| [**StringCchCopyNEx**](/windows/win32/Strsafe/nf-strsafe-stringcchcopynexa?branch=master)     | Copies the specified number of characters from one string to another.<br/>                 |
| [**StringCchGets**](/windows/win32/Strsafe/nf-strsafe-stringcchgetsa?branch=master)           | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCchGetsEx**](/windows/win32/Strsafe/nf-strsafe-stringcchgetsexa?branch=master)       | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCchLength**](/windows/win32/Strsafe/nf-strsafe-stringcchlengtha?branch=master)       | Determines whether a string exceeds the specified length, in characters.<br/>              |
| [**StringCchPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcchprintfa?branch=master)       | Writes formatted data to the specified string.<br/>                                        |
| [**StringCchPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcchprintfexa?branch=master)   | Writes formatted data to the specified string.<br/>                                        |
| [**StringCchVPrintf**](/windows/win32/Strsafe/nf-strsafe-stringcchvprintfa?branch=master)     | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |
| [**StringCchVPrintfEx**](/windows/win32/Strsafe/nf-strsafe-stringcchvprintfexa?branch=master) | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |



 

 

 





