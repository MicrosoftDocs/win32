---
title: Constants
description: A constant can be either numeric or a string, depending on the attribute.
ms.assetid: '115ee0aa-19c4-4d00-a36d-16eaff3afa4c'
---

# Constants

A constant can be either numeric or a string, depending on the attribute.

## Numeric

Numeric input is usually an integer (in either decimal or in hexadecimal, using the standard 0x format), but can also be a single character constant (for example, \\0).

## String

A string is delimited by double quotation marks (") and cannot span multiple lines. The backslash character (\) acts as an escape character. The backslash character followed by any character (even another backslash) prevents the second character from being interpreted with any special meaning. The backslash is not included in the text.

For example, to include a double quotation mark (") in the text without causing it to be interpreted as the closing delimiter, it should be preceded with a backslash (\\"). Similarly, a double backslash (\\\) should be used to put a backslash into the text. Some examples of valid strings are:


```C++
"commandName"
"This string contains a \"quote\"."
"Here's a pathname: c:\\bin\\binp"
```



A string can be up to 255 characters long.

 

 




