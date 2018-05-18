---
title: Strings
description: This section discusses the string functions.
ms.assetid: 'f1799fbf-4619-4b19-998e-b1d2f4c19a35'
keywords: ["resources,strings", "strings", "string functions"]
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
<td>[<strong>CharLower</strong>](charlower.md)</td>
<td>Converts a character string or a single character to lowercase. If the operand is a character string, the function converts the characters in place. <br/></td>
</tr>
<tr class="even">
<td>[<strong>CharLowerBuff</strong>](charlowerbuff.md)</td>
<td>Converts uppercase characters in a buffer to lowercase characters. The function converts the characters in place. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharNext</strong>](charnext.md)</td>
<td>Retrieves a pointer to the next character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CharNextExA</strong>](charnextexa.md)</td>
<td>Retrieves the pointer to the next character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharPrev</strong>](charprev.md)</td>
<td>Retrieves a pointer to the preceding character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CharPrevExA</strong>](charprevexa.md)</td>
<td>Retrieves the pointer to the preceding character in a string. This function can handle strings consisting of either single- or multi-byte characters.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharToOem</strong>](chartooem.md)</td>
<td>Translates a string into the OEM-defined character set.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CharToOemBuff</strong>](chartooembuff.md)</td>
<td>Translates a specified number of characters in a string into the OEM-defined character set.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CharUpper</strong>](charupper.md)</td>
<td>Converts a character string or a single character to uppercase. If the operand is a character string, the function converts the characters in place. <br/></td>
</tr>
<tr class="even">
<td>[<strong>CharUpperBuff</strong>](charupperbuff.md)</td>
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
<td>[<strong>IsCharAlpha</strong>](ischaralpha.md)</td>
<td>Determines whether a character is an alphabetical character. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IsCharAlphaNumeric</strong>](ischaralphanumeric.md)</td>
<td>Determines whether a character is either an alphabetical or a numeric character. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsCharLower</strong>](ischarlower.md)</td>
<td>Determines whether a character is lowercase. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IsCharUpper</strong>](ischarupper.md)</td>
<td>Determines whether a character is uppercase. This determination is based on the semantics of the language selected by the user during setup or through Control Panel. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>LoadString</strong>](loadstring.md)</td>
<td>Loads a string resource from the executable file associated with a specified module, copies the string into a buffer, and appends a terminating NULL character.<br/></td>
</tr>
<tr class="even">
<td>[<strong>lstrcat</strong>](lstrcat.md)</td>
<td>Appends one string to another.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>lstrcmp</strong>](lstrcmp.md)</td>
<td>Compares two character strings. The comparison is case-sensitive.<br/></td>
</tr>
<tr class="even">
<td>[<strong>lstrcmpi</strong>](lstrcmpi.md)</td>
<td>Compares two character strings. The comparison is not case-sensitive.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>lstrcpy</strong>](lstrcpy.md)</td>
<td>Copies a string to a buffer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>lstrcpyn</strong>](lstrcpyn.md)</td>
<td>Copies a specified number of characters from a source string into a buffer. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>lstrlen</strong>](lstrlen.md)</td>
<td>Determines the length of the specified string (not including the terminating null character).<br/></td>
</tr>
<tr class="even">
<td>[<strong>OemToChar</strong>](oemtochar.md)</td>
<td>Translates a string from the OEM-defined character set into either an ANSI or a wide-character string.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OemToCharBuff</strong>](oemtocharbuff.md)</td>
<td>Translates a specified number of characters in a string from the OEM-defined character set into either an ANSI or a wide-character string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>wsprintf</strong>](wsprintf.md)</td>
<td>Writes formatted data to the specified buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>wvsprintf</strong>](wvsprintf.md)</td>
<td>Writes formatted data to the specified buffer using a pointer to a list of arguments.<br/></td>
</tr>
</tbody>
</table>



 

### Strsafe Functions



| Name                                             | Description                                                                                      |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**StringCbCat**](stringcbcat.md)               | Concatenates one string to another string.<br/>                                            |
| [**StringCbCatEx**](stringcbcatex.md)           | Concatenates one string to another string.<br/>                                            |
| [**StringCbCatN**](stringcbcatn.md)             | Concatenates the specified number of bytes from one string to another string.<br/>         |
| [**StringCbCatNEx**](stringcbcatnex.md)         | Concatenates the specified number of bytes from one string to another string.<br/>         |
| [**StringCbCopy**](stringcbcopy.md)             | Copies one string to another.<br/>                                                         |
| [**StringCbCopyEx**](stringcbcopyex.md)         | Copies one string to another.<br/>                                                         |
| [**StringCbCopyN**](stringcbcopyn.md)           | Copies the specified number of bytes from one string to another.<br/>                      |
| [**StringCbCopyNEx**](stringcbcopynex.md)       | Copies the specified number of bytes from one string to another.<br/>                      |
| [**StringCbGets**](stringcbgets.md)             | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCbGetsEx**](stringcbgetsex.md)         | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCbLength**](stringcblength.md)         | Determines whether a string exceeds the specified length, in bytes.<br/>                   |
| [**StringCbPrintf**](stringcbprintf.md)         | Writes formatted data to the specified string.<br/>                                        |
| [**StringCbPrintfEx**](stringcbprintfex.md)     | Writes formatted data to the specified string.<br/>                                        |
| [**StringCbVPrintf**](stringcbvprintf.md)       | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |
| [**StringCbVPrintfEx**](stringcbvprintfex.md)   | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |
| [**StringCchCat**](stringcchcat.md)             | Concatenates one string to another string.<br/>                                            |
| [**StringCchCatEx**](stringcchcatex.md)         | Concatenates one string to another string.<br/>                                            |
| [**StringCchCatN**](stringcchcatn.md)           | Concatenates the specified number of characters from one string to another string.<br/>    |
| [**StringCchCatNEx**](stringcchcatnex.md)       | Concatenates the specified number of characters from one string to another string.<br/>    |
| [**StringCchCopy**](stringcchcopy.md)           | Copies one string to another.<br/>                                                         |
| [**StringCchCopyEx**](stringcchcopyex.md)       | Copies one string to another.<br/>                                                         |
| [**StringCchCopyN**](stringcchcopyn.md)         | Copies the specified number of characters from one string to another.<br/>                 |
| [**StringCchCopyNEx**](stringcchcopynex.md)     | Copies the specified number of characters from one string to another.<br/>                 |
| [**StringCchGets**](stringcchgets.md)           | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCchGetsEx**](stringcchgetsex.md)       | Gets one line of text from stdin, up to and including the newline character ('\\n').<br/>  |
| [**StringCchLength**](stringcchlength.md)       | Determines whether a string exceeds the specified length, in characters.<br/>              |
| [**StringCchPrintf**](stringcchprintf.md)       | Writes formatted data to the specified string.<br/>                                        |
| [**StringCchPrintfEx**](stringcchprintfex.md)   | Writes formatted data to the specified string.<br/>                                        |
| [**StringCchVPrintf**](stringcchvprintf.md)     | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |
| [**StringCchVPrintfEx**](stringcchvprintfex.md) | Writes formatted data to the specified string using a pointer to a list of arguments.<br/> |



 

 

 





