---
description: The symbol handler will load symbols when you call the SymInitialize function with the fInvadeProcess parameter set to TRUE or when you call the SymLoadModuleEx function to specify a module.
ms.assetid: 'fae1895e-9fed-45e3-8ecf-4c6cc67a6094'
title: Symbol Loading
ms.topic: article
ms.date: 05/31/2018
---

# Symbol Loading

The symbol handler will load symbols when you call the [**SymInitialize**](/windows/desktop/api/Dbghelp/nf-dbghelp-syminitialize) function with the *fInvadeProcess* parameter set to **TRUE** or when you call the [**SymLoadModuleEx**](/windows/desktop/api/Dbghelp/nf-dbghelp-symloadmoduleex) function to specify a module. In either case, the symbol handler either loads the symbols or defers symbol loading until symbols are requested, depending on the options set by the [**SymSetOptions**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetoptions) function.

The symbol handler can be used to retrieve symbolic information for any module; it does not need to be associated with a process specified in the [**SymInitialize**](/windows/desktop/api/Dbghelp/nf-dbghelp-syminitialize) call. To use an arbitrary module, specify the full path to the module image in the *ImageName* parameter. You can use a path to any executable module that has debugging information (.exe, .dll, .drv, .sys, .scr, .cpl, or .com). Use the *BaseOfDll* parameter to specify any load address, then symbol addresses will be based from that address.

It may not be necessary to keep a symbol module loaded through the duration of an application. To release the symbol module from the symbol handler's list of modules, use the [**SymUnloadModule64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symunloadmodule) function. This function releases the memory allocated for the symbol module. To use symbols for that module again, you must call the [**SymLoadModuleEx**](/windows/desktop/api/Dbghelp/nf-dbghelp-symloadmoduleex) function even if the symbol deferred load option is set.

## Diagnosing Symbol Load Problems

To view all attempts to load symbols, call [**SymSetOptions**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetoptions) with SYMOPT\_DEBUG. This causes DbgHelp to call the [**OutputDebugString**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa) function with detailed information on symbol searches, such as the directories it is searching and and error messages. If your code uses [**SymRegisterCallback64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symregistercallback), DbgHelp will call your callback function instead of calling **OutputDebugString**. The *ActionCode* parameter is set to CBA\_DEBUG\_INFO and the *CallbackData* parameter is a string that can be displayed.

To enable this debug output to be displayed to the console without changing your source code, set the DBGHELP\_DBGOUT environment variable to a non-**NULL** value before calling the [**SymInitialize**](/windows/desktop/api/Dbghelp/nf-dbghelp-syminitialize) function. To log the information to a file, set the DBGHELP\_LOG environment variable to the name of the log file to be used.

Note that these features should be used only when needed. They may slow down symbol loading of modules that contain many symbols.

 

 
