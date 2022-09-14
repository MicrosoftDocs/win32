---
title: Compiling and Linking
description: The following makefile shows the dependencies among the files needed to compile the client and server applications and link them to the RPC run-time library and the standard C run-time library.
ms.assetid: 9182baea-7307-4db0-8d66-7fba14227ac9
keywords:
- Remote Procedure Call RPC , tasks, compiling and linking
ms.topic: article
ms.date: 05/31/2018
---

# Compiling and Linking

The following makefile shows the dependencies among the files needed to compile the client and server applications and link them to the RPC run-time library and the standard C run-time library.

This makefile can be used to build client and server applications from the source code in this tutorial. The stubs and headers shown here were generated with MIDL version 2.0. The compiler and linker commands and arguments may be different for your computer configuration. See your compiler documentation for more information.

``` syntax
#makefile for helloc.exe and hellos.exe
#link refers to the linker
#conflags refers to flags for console applications
#conlibs refers to libraries for console applications
 
!include <ntwin32.mak>
 
all : helloc hellos
 
# Make the client side application helloc
helloc : helloc.exe
helloc.exe : helloc.obj hello_c.obj
    $(link) $(linkdebug) $(conflags) -out:helloc.exe \
        helloc.obj hello_c.obj \
        rpcrt4.lib $(conlibs)
 
# helloc main program
helloc.obj : helloc.c hello.h
    $(cc) $(cdebug) $(cflags) $(cvars) $*.c
 
# helloc stub
hello_c.obj : hello_c.c hello.h
    $(cc) $(cdebug) $(cflags) $(cvars) $*.c
 
# Make the server side application
hellos : hellos.exe
hellos.exe : hellos.obj hellop.obj hello_s.obj
    $(link) $(linkdebug) $(conflags) -out:hellos.exe \
        hellos.obj hello_s.obj hellop.obj \
        rpcrt4.lib $(conlibsmt)
 
# hello server main program
hellos.obj : hellos.c hello.h
    $(cc) $(cdebug) $(cflags) $(cvarsmt) $*.c
 
# remote procedures
hellop.obj : hellop.c hello.h
    $(cc) $(cdebug) $(cflags) $(cvarsmt) $*.c
 
# hellos stub file
hello_s.obj : hello_s.c hello.h
    $(cc) $(cdebug) $(cflags) $(cvarsmt) $*.c
 
# Stubs and header file from the IDL file
hello.h hello_c.c hello_s.c : hello.idl hello.acf
    midl hello.idl
```

 

 




