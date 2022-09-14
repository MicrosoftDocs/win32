---
title: MIDL Compiler Options
description: MIDL Compiler Options
ms.assetid: a78505cf-cda6-4b41-abd1-2609aec4dcb3
ms.topic: article
ms.date: 05/31/2018
---

# MIDL Compiler Options

You can use the following command-line options to override some of the default behavior of the MIDL compiler and to choose optimizations appropriate for your application. For a complete listing of MIDL command-line options, see the [MIDL Command-Line Reference](/windows/desktop/Midl/midl-command-line-reference).



| Command line switch                                       | Description                                                                                                                                                                                                                                      |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**/acf**](/windows/desktop/Midl/-acf)<br/>                          | Use to supply an explicit ACF filename. This switch also enables the use of different interface names in the IDL and ACF files.<br/>                                                                                                       |
| [**/dlldata**](/windows/desktop/Midl/-dlldata)<br/>                  | Specifies a filename for the generated DLL data file for a proxy DLL. The default filename is Dlldata.c.<br/>                                                                                                                              |
| [**/env**](/windows/desktop/Midl/-env)<br/>                          | Directs MIDL to generate stubs or a type library for a target environment.<br/>                                                                                                                                                            |
| [**/header**](/windows/desktop/Midl/-header), [**/h**](/windows/desktop/Midl/-h)<br/> | Specifies the name of the interface header file. The default name is that of the IDL file with an .h extension.<br/>                                                                                                                       |
| [**/iid**](/windows/desktop/Midl/-iid)<br/>                          | Specifies an interface identifier filename that overrides the default interface identifier filename for a COM interface.<br/>                                                                                                              |
| [**/lcid**](/windows/desktop/Midl/-lcid)<br/>                        | Provides full DBCS support so that you can use international characters in your input files, filenames, and directory paths.<br/>                                                                                                          |
| [**/no\_format\_opt**](/windows/desktop/Midl/-no-format-opt)<br/>    | By default, to reduce code size, MIDL eliminates duplicate descriptors. This switch turns off this optimizing behavior.<br/>                                                                                                               |
| [**/Oi**](/windows/desktop/Midl/-oi), **/Oic**, **/Oif**<br/>        | Directs MIDL to use a fully interpreted marshaling method. The /Oic and /Oicf switches provide additional performance enhancements.<br/>                                                                                                   |
| [**/out**](/windows/desktop/Midl/-out)<br/>                          | Specifies the directory to which the MIDL compiler writes output files. The output directory can be specified with a drive letter, an absolute pathname, or both. The default is that MIDL writes the files to the current directory.<br/> |
| [**/proxy**](/windows/desktop/Midl/-proxy)<br/>                      | Specifies the name of the interface proxy file for a COM interface. The default name is that of the IDL file plus "\_p.c".<br/>                                                                                                            |
| [**/tlb**](/windows/desktop/Midl/-tlb)<br/>                          | Specifies the name of the type library file. The default name is that of the IDL file, with a .tlb extension.<br/>                                                                                                                         |



 

## Related topics

<dl> <dt>

[MIDL Compilation](midl-compilation.md)
</dt> </dl>

 

