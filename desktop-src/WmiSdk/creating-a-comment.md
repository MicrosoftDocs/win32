---
description: The Managed Object Format (MOF) compiler supports two styles of comment using two different styles of comment delimiters.
ms.assetid: 5ab71b45-7ed1-44c4-8710-6b833b0afb80
ms.tgt_platform: multiple
title: Creating a Comment
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating a Comment

The Managed Object Format (MOF) compiler supports two styles of comment using two different styles of comment delimiters.

The following table lists the delimiters that are used for comments and the effect that the delimiters have in the code.



| Delimiter   | Marks                                                                                         |
|-------------|-----------------------------------------------------------------------------------------------|
| //          | Start of a comment that terminates at the end of the line.                                    |
| /\* and \*/ | Beginning and end of a comment that may span multiple lines or only span a portion of a line. |



 

As in the C and C++ programming languages, you must use the // delimiter with single-line comments only, but use the /\* and \*/ delimiters with either single-line or multiple-line comments.

The following code example describes the two delimiter styles.

``` syntax
int32 MyProp = 2; // This is a comment until the line ends.
int32 /* This is a comment. */ MyProp = 2;
```

## Related topics

<dl> <dt>

[Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md)
</dt> </dl>

 

 



