---
title: Automation Include File Requirements
description: Lists the files you and your customers need to run Automation applications.
ms.assetid: '1a6783ec-ef73-4973-bbc7-82dd25582c1f'
---

# Automation Include File Requirements

The file names followed by an asterisk (\*) are required by your application at run time.



| 32-bit file names                                                      | 16-bit file names                                                                      | Purpose                                                                                                                                                            |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None<br/>                                                        | Ole2.reg<br/>                                                                    | Registers OLE and Automation. OLE is a system component on 32-bit systems, therefore, no .reg file is required.<br/>                                         |
| None<br/>                                                        | Ole2nls.dll\*<br/> Ole2nls.lib<br/> Olenls.h<br/>                    | Provides functions for applications that support multiple national languages. On 32-bit systems, NLS features are provided by the Win32 NLS API.<br/>        |
| Oleprx32.dll<br/>                                                | Ole2prox.dll\*<br/>                                                              | Coordinates object access across processes.<br/>                                                                                                             |
| MkTypLib.exe<br/>                                                | MkTypLib.exe<br/>                                                                | Builds type libraries from interface descriptions.<br/>                                                                                                      |
| Oleaut32.dll\*<br/> Oleaut32.lib<br/> Oleauto.h<br/> | TypeLib.dll\*<br/> Dispatch.h<br/>                                         | Accesses type libraries.<br/>                                                                                                                                |
|                                                                        | Ole2disp.dll\*<br/> Ole2disp.lib<br/> Dispatch.h<br/>                | Provides functions for creating ActiveX objects and retrieving active objects at run time. Accesses ActiveX objects by invoking methods and properties.<br/> |
| Ole32.dll\*<br/> Ole32.lib<br/> Ole2.h<br/>          | Ole2.dll\*<br/> Ole2.lib<br/> Ole2.h<br/>                            | Provides OLE functions that can be used by OLE and ActiveX objects or containers.<br/>                                                                       |
|                                                                        | Compobj.dll\*<br/> Compobj.lib<br/> Ole2.h<br/> Compobj.h<br/> | Supports COM creation and access.<br/>                                                                                                                       |
|                                                                        | Storage.dll\*<br/> Storage.lib<br/> Ole2.h<br/> Storage.h<br/> | Supports access to subfiles, such as type libraries, within compound documents.<br/>                                                                         |



 

 

 





