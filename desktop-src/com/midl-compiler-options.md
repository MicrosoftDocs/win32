---
title: MIDL Compiler Options
description: MIDL Compiler Options
ms.assetid: a78505cf-cda6-4b41-abd1-2609aec4dcb3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MIDL Compiler Options

You can use the following command-line options to override some of the default behavior of the MIDL compiler and to choose optimizations appropriate for your application. For a complete listing of MIDL command-line options, see the [MIDL Command-Line Reference](https://msdn.microsoft.com/library/windows/desktop/aa367084).



| Command line switch                                       | Description                                                                                                                                                                                                                                      |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**/acf**](https://msdn.microsoft.com/library/windows/desktop/aa367310)<br/>                          | Use to supply an explicit ACF filename. This switch also enables the use of different interface names in the IDL and ACF files.<br/>                                                                                                       |
| [**/dlldata**](https://msdn.microsoft.com/library/windows/desktop/aa367322)<br/>                  | Specifies a filename for the generated DLL data file for a proxy DLL. The default filename is Dlldata.c.<br/>                                                                                                                              |
| [**/env**](https://msdn.microsoft.com/library/windows/desktop/aa367323)<br/>                          | Directs MIDL to generate stubs or a type library for a target environment.<br/>                                                                                                                                                            |
| [**/header**](https://msdn.microsoft.com/library/windows/desktop/aa367326), [**/h**](https://msdn.microsoft.com/library/windows/desktop/aa367325)<br/> | Specifies the name of the interface header file. The default name is that of the IDL file with an .h extension.<br/>                                                                                                                       |
| [**/iid**](https://msdn.microsoft.com/library/windows/desktop/aa367329)<br/>                          | Specifies an interface identifier filename that overrides the default interface identifier filename for a COM interface.<br/>                                                                                                              |
| [**/lcid**](https://msdn.microsoft.com/library/windows/desktop/aa367331)<br/>                        | Provides full DBCS support so that you can use international characters in your input files, filenames, and directory paths.<br/>                                                                                                          |
| [**/no\_format\_opt**](https://msdn.microsoft.com/library/windows/desktop/aa367348)<br/>    | By default, to reduce code size, MIDL eliminates duplicate descriptors. This switch turns off this optimizing behavior.<br/>                                                                                                               |
| [**/Oi**](https://msdn.microsoft.com/library/windows/desktop/aa367352), **/Oic**, **/Oif**<br/>        | Directs MIDL to use a fully interpreted marshaling method. The /Oic and /Oicf switches provide additional performance enhancements.<br/>                                                                                                   |
| [**/out**](https://msdn.microsoft.com/library/windows/desktop/aa367358)<br/>                          | Specifies the directory to which the MIDL compiler writes output files. The output directory can be specified with a drive letter, an absolute pathname, or both. The default is that MIDL writes the files to the current directory.<br/> |
| [**/proxy**](https://msdn.microsoft.com/library/windows/desktop/aa367362)<br/>                      | Specifies the name of the interface proxy file for a COM interface. The default name is that of the IDL file plus "\_p.c".<br/>                                                                                                            |
| [**/tlb**](https://msdn.microsoft.com/library/windows/desktop/aa367372)<br/>                          | Specifies the name of the type library file. The default name is that of the IDL file, with a .tlb extension.<br/>                                                                                                                         |



 

## Related topics

<dl> <dt>

[MIDL Compilation](midl-compilation.md)
</dt> </dl>

 

 





