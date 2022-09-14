---
title: /cpp_cmd switch
description: The /cpp\_cmd switch specifies the preprocessor that the MIDL compiler uses to preprocess input files.
ms.assetid: d6261fdd-155d-4327-b254-d0267f0dec69
keywords:
- /cpp_cmd switch MIDL
topic_type:
- apiref
api_name:
- /cpp_cmd
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /cpp\_cmd switch

The **/cpp\_cmd** switch specifies the preprocessor that the MIDL compiler uses to preprocess input files.

``` syntax
midl /cpp_cmd "C_preprocessor_binary"
```

## Switch Options

<dl> <dt>

*C\_preprocessor\_binary* 
</dt> <dd>

Specifies the command that invokes the preprocessor. This command allows developers to override the default preprocessor. By default, MIDL invokes the Microsoft C/C++ compiler from the build machine's build environment.

</dd> </dl>

## Remarks

The *C\_preprocessor\_binary* argument to the switch may specify the full path; the exe suffix and quotes are optional. Typically, developers use the switch to choose a particular version of the Microsoft C/C++ preprocessor or equivalent in the build environment. In this case, it is not necessary to use the [**/cpp\_opt**](-cpp-opt.md) switch with **/cpp\_cmd**.

When using a non-Microsoft preprocessor, especially when the specified preprocessor does not direct its output to stdout, the C compiler switch that redirects output to stdout as part of the MIDL compiler [**/cpp\_opt**](-cpp-opt.md) switch must be specified. See [C-Preprocessor Requirements for MIDL](c-preprocessor-requirements-for-midl.md) for details

The preprocessor is invoked by a command string that is formed from the information provided to the MIDL compiler by **/cpp\_cmd**, [**/cpp\_opt**](-cpp-opt.md), [**/D**](-d.md), [**/I**](-i.md), and [**/U**](-u.md) switches. The following table summarizes how the command string is constructed for each combination of **/cpp\_cmd** and **/cpp\_opt** switches.

When the **/cpp\_cmd** switch is not specified, the MIDL compiler invokes the Microsoft C/C++ compiler. MIDL uses a Cl.exe binary found in the build environment.

When the [**/cpp\_opt**](-cpp-opt.md) switch is not present, the MIDL compiler concatenates the string specified by the **/cpp\_cmd** switch with the information specified by the MIDL [**/I**](-i.md), [**/D**](-d.md) and [**/U**](-u.md) options. The string /E is also concatenated to the C-compiler invocation string to indicate that the C/C++ compiler should perform preprocessing only. The [**/nologo**](-nologo.md) switch is added to suppress the C/C++ compiler banner. The MIDL compiler uses the concatenated string to invoke the C preprocessor for top-level IDL as well as imported IDL files, and also for any present, corresponding ACF files.

When the [**/cpp\_opt**](-cpp-opt.md) switch is present, which should be a rare case for the current 32-bit and 64-bit platforms, the MIDL compiler concatenates the string specified by the **/cpp\_cmd** switch with the string specified by the **/cpp\_opt** switch. The MIDL compiler uses the concatenated string to invoke the indicated preprocessor binary in place of the default preprocessor. When the **/cpp\_opt** switch is present, neither the MIDL compiler options specified by the [**/I**](-i.md), [**/D**](-d.md), and [**/U**](-u.md) switches nor the C compiler switch /E is concatenated with the string. You must supply the /E option, or equivalent, as part of the string.



| /cpp\_cmd present? | /cpp\_opt present? | Description                                                                                                                                                                                                       |
|--------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No (default)       | No (default)       | Invokes the default Microsoft C/C++ compiler with settings obtained from MIDL [**/I**](-i.md), [**/D**](-d.md) and [**/U**](-u.md) switches. Adds the preprocessor switches /E and [**/nologo**](-nologo.md). |
| Yes                | No                 | Invokes the indicated preprocessor binary with the same switches as above.                                                                                                                                        |
| No                 | Yes                | Invokes the Microsoft C compiler with specified options. Does not use MIDL [**/I**](-i.md), [**/D**](-d.md), [**/U**](-u.md) options. You must supply /E as part of [**/cpp\_opt**](-cpp-opt.md).             |
| Yes                | Yes                | Invokes the specified preprocessor binary with specified options only. You must use quotes.                                                                                                                       |



 

## Examples

**midl /cpp\_cmd d:\\nt\\tools\\ia64\\cl.exe /DFLAG=TRUE /Ic:\\inc filename.idl**

**midl /cpp\_cmd "mycpp" /DFLAG=TRUE /Ic:\\inc filename.idl**

**midl /cpp\_opt "/E /DFLAG=TRUE /Ic:\\inc" filename.idl**

**midl /cpp\_cmd "cl" /cpp\_opt "/E /DFLAG=TRUE /Ic:\\inc" filename.idl**

## See also

<dl> <dt>

[**/savePP**](-savepp.md)
</dt> <dt>

[**/cpp\_opt**](-cpp-opt.md)
</dt> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/no\_cpp**](-no-cpp-nocpp.md)
</dt> <dt>

[C-Preprocessor Requirements for MIDL](c-preprocessor-requirements-for-midl.md)
</dt> </dl>

 

 




