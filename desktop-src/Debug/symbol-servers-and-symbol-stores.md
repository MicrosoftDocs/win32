---
description: Setting up symbols correctly for debugging can be a challenging task, particularly for kernel debugging.
ms.assetid: 96b2c9db-58fb-4c28-b17c-3b1cc06ed96b
title: Symbol Server and Symbol Stores
ms.topic: article
ms.date: 05/31/2018
---

# Symbol Server and Symbol Stores

Setting up symbols correctly for debugging can be a challenging task, particularly for kernel debugging. It often requires that you know the names and releases of all products on your computer. The debugger must be able to locate the symbol files that correspond to each product release and service pack. This can result in an extremely long symbol path consisting of a long list of directories.

To simplify these difficulties in coordinating symbol files, use the *symbol server*. The symbol server enables the debuggers to automatically retrieve the correct symbol files without product names, releases, or build numbers. Debugging Tools for Windows contains the SymSrv symbol server.

The symbol server is activated by including a certain text string in the symbol path. Each time the debugger needs to load symbols for a newly loaded module, it calls the symbol server to locate the appropriate symbol files. The symbol server locates the files in a *symbol store*. This is a collection of symbol files, an index, and a tool that can be used by an administrator to add and delete files. The files are indexed according to unique parameters such as the time stamp and image size. Debugging Tools for Windows contains a symbol store tool called SymStore.

For more information, see:

-   [Using SymSrv](using-symsrv.md)
-   [Using SymStore](using-symstore.md)
-   [Using Other Symbol Stores](using-other-symbol-stores.md)
-   [SymStore Command-Line Options](symstore-command-line-options.md)
-   [Symbol Server and Internet Firewalls](symbol-servers-and-internet-firewalls.md)

## Related topics

<dl> <dt>

[Symbol Files](symbol-files.md)
</dt> </dl>

 

 



