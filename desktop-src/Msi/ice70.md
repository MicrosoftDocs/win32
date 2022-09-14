---
description: ICE70 verifies that integer values for registry entries are specified correctly.
ms.assetid: f8493622-867b-42e1-9fda-a7c3229bbb4e
title: ICE70
ms.topic: article
ms.date: 05/31/2018
---

# ICE70

ICE70 verifies that integer values for registry entries are specified correctly. Values of the form \#\#str, \#%unexpanded str are not validated. Values of the form \#xhex, \#Xhex, \#integer, and \#\[property\] are validated. The following table provides a brief overview.



| Value                 | Validation                                                                    |
|-----------------------|-------------------------------------------------------------------------------|
| \#\#str               | valid                                                                         |
| \#%unexpanded str     | valid                                                                         |
| \#xHex,\#XHex         | Validate for valid hex characters (0-9,a-f,A-F). Properties are allowed here. |
| \#+int, \#-int, \#int | Validate for valid numeric characters (0-9). Properties are allowed here.     |



 

The syntax for an integer value to be entered into the registry is \#integer where integer is numerical.

## Result

ICE70 reports an error if integer values for registry entries are not specified correctly.

## Example

ICE70 reports the following errors for the given example.

``` syntax
The value #12xz34 is an invalid numeric value for registry entry Reg1. If you meant to use a string, then the string value entry must be preceded by ## not #.
```

To fix this error: If you want the value to be numeric, change the value to use all numeric characters. If you want the value to be a string, it must be preceded by two '\#' (\#\#) instead of just one.

``` syntax
The value #xz34 is an invalid hexadecimal value for registry entry Reg2.
```

To fix this error: Valid hexadecimal characters are 0-9, A-F, and a-f. Only these characters can follow the \#x (or \#X).

[Registry table](registry-table.md) (partial)



| Registry | Value    |
|----------|----------|
| Reg1     | \#12xz34 |
| Reg2     | \#xz34   |



 

## Remarks

-   \#\[myproperty\] is valid.
-   \#\[myproperty is not valid (missing ending bracket).
-   \#\[myprop1\] \[myprop2 is valid. (Even though the last one is missing the ending bracket, myprop1 could evaluate to \#str so you would have \#\#str \[myprop2, which is valid
-   \#\]myproperty\[ is not valid
-   Any embedded property in a value string cannot be in \[$compkey\], \[\#filekey\], or \[!filekey\] form because these are not numeric. However, there is one exception, \#\[myproperty\] \[$compkey\] (or \[\#filekey\] or \[!filekey\]) is valid because, as with the preceding, \[myproperty\] can evaluate to \#str.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



