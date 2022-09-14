---
description: ICE65 checks that the Environment table does not have invalid prefix or append values.
ms.assetid: 95d4e618-9a19-40db-910a-daab105559ae
title: ICE65
ms.topic: article
ms.date: 05/31/2018
---

# ICE65

ICE65 checks that the [Environment table](environment-table.md) does not have invalid prefix or append values.

Failure to fix a warning or error reported by ICE65 generally leads to problems in install, uninstall, or repair of the environment variable. For example, only some values of a particular variable may be removed if one or more of the values for that variable have a trailing separator.

## Result

ICE65 posts a warning or an error if the environment table has invalid prefix or append values.

## Example

ICE65 reports the following error and warning for the example shown.

``` syntax
The environment variable 'Var3' has a separator beginning or ending its value.
```

The trailing null at the end of the value (\[~\]) marks this value to be prepended to any existing value. The character immediately before the null (a semicolon) becomes the separator for this value. This value has a semicolon at the beginning of the string as well.

To fix this error, simply delete the leading semicolon.

``` syntax
WARNING: The environment variable 'Var2' has an alphanumeric separator
```

The leading null in the value (\[~\]) marks this value to be appended to any existing value. The character immediately after the null becomes the separator for this value. In this case, that character is the letter "e", which also occurs in the middle of the string to be appended. This condition (having a separator that is the same as a character within the string to be appended) can cause unpredictable results.

The letter "e", being a common letter, is likely to be found in the value. A better choice would be ";" or some other non-alphanumeric character. (However, if the value is a path, then ":" and "\\" and "." are risky choices.)

To fix this warning, use a different separator character.

[Environment Table](environment-table.md)



| Component | Directory | Attributes         | KeyPath       |
|-----------|-----------|--------------------|---------------|
| Var1      | TestVar   | \[~\];AppendThis   | TestComponent |
| Var2      | TestVar   | \[~\]eAppendThis   | TestComponent |
| Var3      | TestVar   | ;PrependThis;\[~\] | TestComponent |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



