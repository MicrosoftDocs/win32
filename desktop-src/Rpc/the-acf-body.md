---
title: The ACF Body
description: The ACF body contains configuration attributes that apply to types and functions defined in the interface body of the IDL file.
ms.assetid: 7d6344d3-1117-40b9-be95-a400b81339d7
ms.topic: article
ms.date: 05/31/2018
---

# The ACF Body

The ACF body contains configuration attributes that apply to types and functions defined in the interface body of the IDL file. The body of the ACF can be empty or it can contain ACF [**include**](/windows/desktop/Midl/include), [**typedef**](/windows/desktop/Midl/typedef), function, and parameter attributes. All of these items are optional. Attributes applied to individual types and functions in the ACF body override attributes in the ACF header.

The ACF specifies behavior on the local computer and does not affect the data transmitted over the network. It is used to specify details of a stub to be generated. In DCE-compatibility mode ([**/osf**](/windows/desktop/Midl/-osf)), the ACF does not affect interaction between stubs, but between the stub and application code.

A parameter specified in the ACF must be one of the parameters specified in the IDL file. The order of specification of the parameter in the ACF is not significant because the matching is by name, not by position. The parameter list in the ACF can be empty, even when the parameter list in the corresponding IDL signature is not (but this is not recommended). Abstract declarators (unnamed parameters) in the IDL file cause the MIDL compiler to report errors while processing the ACF because the parameter is not found.

The ACF **include** directive specifies the header files to appear in the generated header as part of a standard C-preprocessor **\#include** statement. The ACF keyword **include** differs from an **\#include** directive. The ACF keyword **include** causes the line "**\#include** *filename*" to appear in the generated header file, while the C-language directive "**\#include** *filename*" causes the contents of that file to be placed in the ACF.

The ACF [**typedef**](/windows/desktop/Midl/typedef) statement lets you apply ACF type attributes to types previously defined in the IDL file. The ACF **typedef** syntax differs from the C **typedef** syntax.

The ACF function attributes let you specify attributes that apply to the function as a whole. For more information, see **\[**[**code**](/windows/desktop/Midl/code)**\]**, **\[**[**optimize**](/windows/desktop/Midl/optimize)**\]**, and **\[**[**nocode**](/windows/desktop/Midl/nocode)**\]**.

The ACF parameter attributes let you specify attributes that apply to individual parameters of the function. For more information, see **\[**[**byte\_count**](/windows/desktop/Midl/byte-count)**\]**.

## Related topics

<dl> <dt>

[**/app\_config**](/windows/desktop/Midl/-app-config)
</dt> <dt>

[**/osf**](/windows/desktop/Midl/-osf)
</dt> <dt>

[**\[auto\_handle\]**](../midl/auto-handle.md)
</dt> <dt>

[**\[code\]**](../midl/code.md)
</dt> <dt>

[**\[explicit\_handle\]**](../midl/explicit-handle.md)
</dt> <dt>

[The Interface Definition Language (IDL) File](the-interface-definition-language-idl-file.md)
</dt> <dt>

[**\[implicit\_handle\]**](../midl/implicit-handle.md)
</dt> <dt>

[**include**](/windows/desktop/Midl/include)
</dt> <dt>

[midl](/windows/desktop/Midl/midl-language-reference)
</dt> <dt>

[**\[nocode\]**](../midl/nocode.md)
</dt> <dt>

[**\[optimize\]**](../midl/optimize.md)
</dt> <dt>

[**\[represent\_as\]**](../midl/represent-as.md)
</dt> <dt>

[**typedef**](/windows/desktop/Midl/typedef)
</dt> </dl>

 

 