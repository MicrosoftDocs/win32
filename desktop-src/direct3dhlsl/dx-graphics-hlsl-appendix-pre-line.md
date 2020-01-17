---
title: ' line Directive'
description: Preprocessor directive that sets the compiler's internally-stored line number and filename to the specified values.
ms.assetid: 307410af-bd78-4b3d-b515-adf58298f35f
keywords:
- line Directive HLSL
topic_type:
- apiref
api_name:
- line Directive
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# \#line Directive

Preprocessor directive that sets the compiler's internally-stored line number and filename to the specified values.



| \#line *lineNumber* "*filename*" |
|----------------------------------|



 

## Parameters



| Item                                                                                                                              | Description                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="lineNumber"></span><span id="linenumber"></span><span id="LINENUMBER"></span>*lineNumber*<br/>                    | Line number to set. This can be any integer constant. Macro replacement can be performed on the preprocessing tokens, as long as the result evaluates to the correct syntax. <br/>                     |
| <span id="filename__optional__________"></span><span id="FILENAME__OPTIONAL__________"></span>*filename* \[optional\] <br/> | Filename to set. The filename can be any combination of characters, and must be enclosed in double quotation marks (" "). If this parameter is omitted, the previous filename remains unchanged. <br/> |



 

## Remarks

The compiler uses the line number and filename to refer to errors that it finds during compilation. The line number usually refers to the current input line, and the filename refers to the current input file. The line number is incremented after each line is processed. If you change the line number and filename, the compiler ignores the previous values and continues processing with the new values. The \#line directive is typically used by program generators to cause error messages to refer to the original source file instead of to the generated program.

The translator uses the line number and filename to determine the values of the predefined macros \_\_FILE\_\_ and \_\_LINE\_\_. You can use these macros to insert self-descriptive error messages into the program text. The \_\_FILE\_\_ macro expands to a string whose contents are the filename, surrounded by double quotation marks (" ").

## Examples

The following example sets the line number to 151 and the filename to "copy.c".


```
#line 151 "copy.c"
```



In the following example, the macro ASSERT uses the predefined macros \_\_LINE\_\_ and \_\_FILE\_\_ to print an error message about the source file if the specified assertion is not true.


```
#define ASSERT(cond)

if( !(cond) )\
{printf( "assertion error line %d, file(%s)\n", \
__LINE__, __FILE__ );}
```



## See also

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> </dl>

 

 





