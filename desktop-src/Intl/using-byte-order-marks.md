---
description: Always prefix a Unicode plain text file with a byte order mark, which informs an application receiving the file that the file is byte-ordered.
ms.assetid: d9f1ef5c-6367-4183-9c07-01c73cb4debc
title: Using Byte Order Marks
ms.topic: article
ms.date: 05/31/2018
---

# Using Byte Order Marks

Always prefix a Unicode plain text file with a byte order mark, which informs an application receiving the file that the file is byte-ordered. Available byte order marks are listed in the following table. Because Unicode plain text is a sequence of 16-bit code values, it is sensitive to the byte ordering used when the text is written.

> [!Note]  
> A byte order mark is not a control character that selects the byte order of the text.

 



| Byte order mark | Description           |
|-----------------|-----------------------|
| EF BB BF        | UTF-8                 |
| FF FE           | UTF-16, little endian |
| FE FF           | UTF-16, big endian    |
| FF FE 00 00     | UTF-32, little endian |
| 00 00 FE FF     | UTF-32, big-endian    |



 

> [!Note]  
> Microsoft uses UTF-16, little endian byte order.

 

Ideally, all Unicode text follows only one set of byte ordering rules. This is not possible, however, because microprocessors differ in the placement of the least significant byte. Intel and MIPS processors position the least significant byte first, whereas Motorola processors (and all byte-reversed Unicode files) position it last. With only a single set of byte ordering rules, users of one type of microprocessor are forced to swap the byte order every time a plain text file is read from or written to, even if the file is never transferred to another operating system based on a different microprocessor.

The preferred place to specify byte order is in a file header, but text files do not have headers. Therefore, Unicode has defined a character (U+FEFF) and a noncharacter (U+FFFE) as byte order marks. They are mirror byte images of each other.

Since the sequence U+FEFF is exceedingly rare at the beginning of a regular non-Unicode text file, it can serve as an implicit marker or signature to identify the file as a Unicode file. Applications that read both Unicode and non-Unicode text files should use the presence of this sequence as an indicator that the file is most likely a Unicode file. Compare this technique to using the MS-DOS EOF marker to terminate text files.

When an application finds U+FEFF at the beginning of a text file, it typically processes the file as a Unicode file, although it can perform further heuristic checks for verification. Such a check can be as simple as testing to find out if the variation in the low-order bytes is much higher than the variation in the high-order bytes. For example, if ASCII text is converted to Unicode text, every second byte is 0. Also, checking both for the linefeed and carriage return characters (U+000A and U+000D) and for even or odd file size can provide a strong indicator of the nature of the file.

When an application finds U+FFFE at the beginning of a text file, it interprets it to mean that the file is a byte-reversed Unicode file. The application can either swap the order of the bytes or alert the user that an error has occurred.

Since the Unicode byte order mark character is not found in any code page, it disappears if data is converted to ANSI. Unlike other Unicode characters, it is not replaced by a default character when it is converted. If a byte order mark is found in the middle of a file, it is not interpreted as a Unicode character and has no effect on text output.

> [!Note]  
> The Unicode value U+FFFF is illegal in plain text files and cannot be passed between applications. It is reserved for the private use of an application.

 

## Related topics

<dl> <dt>

[Using Special Characters in Unicode](using-special-characters-in-unicode.md)
</dt> </dl>

 

 



