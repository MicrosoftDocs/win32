---
Description: Where necessary, the DbgHelp library has been widened to support both 32- and 64-bit Windows.
ms.assetid: 34ec8cd3-3260-441d-b55f-4ea21c736eb1
title: Updated Platform Support
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Updated Platform Support

Where necessary, the DbgHelp library has been widened to support both 32- and 64-bit Windows. The original function and structure definitions are still in DbgHelp.h, but there are also updated versions of these definitions that are compatible with 64-bit Windows. If you use the updated functions in your code, it can be compiled for both 32- and 64-bit Windows. Your code will also be more efficient, since the original functions simply call the updated functions to perform the work.

For example, DbgHelp.h contains definitions for **SymUnloadModule** (original function) and **SymUnloadModule64** (updated function). These definitions are nearly identical, but use different types for the *BaseOfDll* parameter. (**SymUnloadModule** uses the **DWORD** type, while **SymUnloadModule64** uses the **DWORD64** type.) If you write your code to use **SymUnloadModule64**, it can be compiled for both 32- and 64-bit Windows. The code is also more efficient than if it were to call **SymUnloadModule**.

The following is a list of the updated functions:

<dl>

[**EnumerateLoadedModules64**](/windows/win32/Dbghelp/nf-dbghelp-enumerateloadedmodules?branch=master)  
[**StackWalk64**](/windows/win32/DbgHelp/nf-dbghelp-stackwalk?branch=master)  
[**SymEnumerateModules64**](/windows/win32/Dbghelp/nf-dbghelp-symenumeratemodules?branch=master)  
[**SymEnumerateSymbols64**](/windows/win32/Dbghelp/nf-dbghelp-symenumeratesymbols?branch=master)  
[**SymFunctionTableAccess64**](/windows/win32/Dbghelp/nf-dbghelp-symfunctiontableaccess?branch=master)  
[**SymGetLineFromAddr64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlinefromaddr?branch=master)  
[**SymGetLineFromName64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlinefromname?branch=master)  
[**SymGetLineNext64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlinenext?branch=master)  
[**SymGetLinePrev64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlineprev?branch=master)  
[**SymGetModuleBase64**](/windows/win32/Dbghelp/nf-dbghelp-symgetmodulebase?branch=master)  
[**SymGetModuleInfo64**](/windows/win32/Dbghelp/nf-dbghelp-symgetmoduleinfo?branch=master)  
[**SymGetSymFromAddr64**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymfromaddr?branch=master)  
[**SymGetSymFromName64**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymfromname?branch=master)  
[**SymGetSymNext64**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymnext?branch=master)  
[**SymGetSymPrev64**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymprev?branch=master)  
[**SymLoadModule64**](/windows/win32/Dbghelp/nf-dbghelp-symloadmodule?branch=master)  
[**SymRegisterCallback64**](/windows/win32/Dbghelp/nf-dbghelp-symregistercallback?branch=master)  
[**SymRegisterFunctionEntryCallback64**](/windows/win32/Dbghelp/nf-dbghelp-symregisterfunctionentrycallback?branch=master)  
[**SymUnDName64**](/windows/win32/Dbghelp/nf-dbghelp-symundname?branch=master)  
[**SymUnloadModule64**](/windows/win32/Dbghelp/nf-dbghelp-symunloadmodule?branch=master)  
</dl>

The following is a list of the updated structures:

<dl>

[**ADDRESS64**](/windows/win32/DbgHelp/ns-dbghelp-_tagaddress?branch=master)  
[**IMAGEHLP\_DEFERRED\_SYMBOL\_LOAD64**](/windows/win32/DbgHelp/ns-dbghelp-_imagehlp_deferred_symbol_load?branch=master)  
[**IMAGEHLP\_DUPLICATE\_SYMBOL64**](/windows/win32/DbgHelp/ns-dbghelp-_imagehlp_duplicate_symbol?branch=master)  
[**IMAGEHLP\_LINE64**](/windows/win32/DbgHelp/ns-dbghelp-_imagehlp_line?branch=master)  
[**IMAGEHLP\_MODULE64**](/windows/win32/DbgHelp/ns-dbghelp-_imagehlp_module?branch=master)  
[**IMAGEHLP\_SYMBOL64**](/windows/win32/DbgHelp/ns-dbghelp-_imagehlp_symbol?branch=master)  
[**KDHELP64**](/windows/win32/DbgHelp/ns-dbghelp-_kdhelp?branch=master)  
[**STACKFRAME64**](/windows/win32/DbgHelp/ns-dbghelp-_tagstackframe?branch=master)  
</dl>

 

 



