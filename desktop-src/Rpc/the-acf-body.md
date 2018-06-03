---
title: The ACF Body
description: The ACF body contains configuration attributes that apply to types and functions defined in the interface body of the IDL file.
ms.assetid: 7d6344d3-1117-40b9-be95-a400b81339d7
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The ACF Body

The ACF body contains configuration attributes that apply to types and functions defined in the interface body of the IDL file. The body of the ACF can be empty or it can contain ACF [**include**](https://msdn.microsoft.com/library/windows/desktop/aa367052), [**typedef**](https://msdn.microsoft.com/library/windows/desktop/aa367287), function, and parameter attributes. All of these items are optional. Attributes applied to individual types and functions in the ACF body override attributes in the ACF header.

The ACF specifies behavior on the local computer and does not affect the data transmitted over the network. It is used to specify details of a stub to be generated. In DCE-compatibility mode ([**/osf**](https://msdn.microsoft.com/library/windows/desktop/aa367357)), the ACF does not affect interaction between stubs, but between the stub and application code.

A parameter specified in the ACF must be one of the parameters specified in the IDL file. The order of specification of the parameter in the ACF is not significant because the matching is by name, not by position. The parameter list in the ACF can be empty, even when the parameter list in the corresponding IDL signature is not (but this is not recommended). Abstract declarators (unnamed parameters) in the IDL file cause the MIDL compiler to report errors while processing the ACF because the parameter is not found.

The ACF **include** directive specifies the header files to appear in the generated header as part of a standard C-preprocessor **\#include** statement. The ACF keyword **include** differs from an **\#include** directive. The ACF keyword **include** causes the line "**\#include** *filename*" to appear in the generated header file, while the C-language directive "**\#include** *filename*" causes the contents of that file to be placed in the ACF.

The ACF [**typedef**](https://msdn.microsoft.com/library/windows/desktop/aa367287) statement lets you apply ACF type attributes to types previously defined in the IDL file. The ACF **typedef** syntax differs from the C **typedef** syntax.

The ACF function attributes let you specify attributes that apply to the function as a whole. For more information, see **\[**[**code**](https://msdn.microsoft.com/library/windows/desktop/aa366752)**\]**, **\[**[**optimize**](https://msdn.microsoft.com/library/windows/desktop/aa367131)**\]**, and **\[**[**nocode**](https://msdn.microsoft.com/library/windows/desktop/aa367116)**\]**.

The ACF parameter attributes let you specify attributes that apply to individual parameters of the function. For more information, see **\[**[**byte\_count**](https://msdn.microsoft.com/library/windows/desktop/aa366744)**\]**.

## Related topics

<dl> <dt>

[**/app\_config**](https://msdn.microsoft.com/library/windows/desktop/aa367312)
</dt> <dt>

[**/osf**](https://msdn.microsoft.com/library/windows/desktop/aa367357)
</dt> <dt>

[**\[auto\_handle\]**](https://msdn.microsoft.com/library/windows/desktop/aa366736)
</dt> <dt>

[**\[code\]**](https://msdn.microsoft.com/library/windows/desktop/aa366752)
</dt> <dt>

[**\[explicit\_handle\]**](https://msdn.microsoft.com/library/windows/desktop/aa366825)
</dt> <dt>

[The Interface Definition Language (IDL) File](the-interface-definition-language-idl-file.md)
</dt> <dt>

[**\[implicit\_handle\]**](https://msdn.microsoft.com/library/windows/desktop/aa367046)
</dt> <dt>

[**include**](https://msdn.microsoft.com/library/windows/desktop/aa367052)
</dt> <dt>

[midl](https://msdn.microsoft.com/library/windows/desktop/aa367088)
</dt> <dt>

[**\[nocode\]**](https://msdn.microsoft.com/library/windows/desktop/aa367116)
</dt> <dt>

[**\[optimize\]**](https://msdn.microsoft.com/library/windows/desktop/aa367131)
</dt> <dt>

[**\[represent\_as\]**](https://msdn.microsoft.com/library/windows/desktop/aa367154)
</dt> <dt>

[**typedef**](https://msdn.microsoft.com/library/windows/desktop/aa367287)
</dt> </dl>

 

 




