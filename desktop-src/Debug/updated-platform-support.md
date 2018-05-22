---
Description: 'Where necessary, the DbgHelp library has been widened to support both 32- and 64-bit Windows.'
ms.assetid: '34ec8cd3-3260-441d-b55f-4ea21c736eb1'
title: Updated Platform Support
---

# Updated Platform Support

Where necessary, the DbgHelp library has been widened to support both 32- and 64-bit Windows. The original function and structure definitions are still in DbgHelp.h, but there are also updated versions of these definitions that are compatible with 64-bit Windows. If you use the updated functions in your code, it can be compiled for both 32- and 64-bit Windows. Your code will also be more efficient, since the original functions simply call the updated functions to perform the work.

For example, DbgHelp.h contains definitions for **SymUnloadModule** (original function) and **SymUnloadModule64** (updated function). These definitions are nearly identical, but use different types for the *BaseOfDll* parameter. (**SymUnloadModule** uses the **DWORD** type, while **SymUnloadModule64** uses the **DWORD64** type.) If you write your code to use **SymUnloadModule64**, it can be compiled for both 32- and 64-bit Windows. The code is also more efficient than if it were to call **SymUnloadModule**.

The following is a list of the updated functions:

<dl>

[**EnumerateLoadedModules64**](enumerateloadedmodules64.md)  
[**StackWalk64**](stackwalk64.md)  
[**SymEnumerateModules64**](symenumeratemodules64.md)  
[**SymEnumerateSymbols64**](symenumeratesymbols64.md)  
[**SymFunctionTableAccess64**](symfunctiontableaccess64.md)  
[**SymGetLineFromAddr64**](symgetlinefromaddr64.md)  
[**SymGetLineFromName64**](symgetlinefromname64.md)  
[**SymGetLineNext64**](symgetlinenext64.md)  
[**SymGetLinePrev64**](symgetlineprev64.md)  
[**SymGetModuleBase64**](symgetmodulebase64.md)  
[**SymGetModuleInfo64**](symgetmoduleinfo64.md)  
[**SymGetSymFromAddr64**](symgetsymfromaddr64.md)  
[**SymGetSymFromName64**](symgetsymfromname64.md)  
[**SymGetSymNext64**](symgetsymnext64.md)  
[**SymGetSymPrev64**](symgetsymprev64.md)  
[**SymLoadModule64**](symloadmodule64.md)  
[**SymRegisterCallback64**](symregistercallback64.md)  
[**SymRegisterFunctionEntryCallback64**](symregisterfunctionentrycallback64.md)  
[**SymUnDName64**](symundname64.md)  
[**SymUnloadModule64**](symunloadmodule64.md)  
</dl>

The following is a list of the updated structures:

<dl>

[**ADDRESS64**](address64-str.md)  
[**IMAGEHLP\_DEFERRED\_SYMBOL\_LOAD64**](imagehlp-deferred-symbol-load64-str.md)  
[**IMAGEHLP\_DUPLICATE\_SYMBOL64**](imagehlp-duplicate-symbol64-str.md)  
[**IMAGEHLP\_LINE64**](imagehlp-line64-str.md)  
[**IMAGEHLP\_MODULE64**](imagehlp-module64-str.md)  
[**IMAGEHLP\_SYMBOL64**](imagehlp-symbol64-str.md)  
[**KDHELP64**](kdhelp64-str.md)  
[**STACKFRAME64**](stackframe64-str.md)  
</dl>

 

 



