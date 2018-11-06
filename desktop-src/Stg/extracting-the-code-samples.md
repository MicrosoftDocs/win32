---
title: Extracting the Code Samples
description: Though the code samples are divided into a series of tutorial lessons, the appropriate sample groupings can easily be extracted from the collection.
ms.assetid: f8e20e40-cfef-4844-8b28-5a11fdcd691a
ms.topic: article
ms.date: 05/31/2018
---

# Extracting the Code Samples

Though the code samples are divided into a series of tutorial lessons, the appropriate sample groupings can easily be extracted from the collection. Most of the individual sample directories are meant to work in conjunction with at least one other sample directory. The component-related samples consist of a client and server pair, with the server requiring the use of the REGISTER sample utility. Here is a summary of the sample groupings and how to extract each group as a buildable unit. For each sample grouping, copy the content of the directories shown. The parent \[destination\] directory shown requires no content from the samples branch. However, the help menus in the running samples do assume that the appropriate tutorial .HTM help files are located in this parent \[destination\] directory.

For the Win32 READTUT application:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    READTUT
```

For the Win32 EXE skeleton application:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    EXESKEL
```

For the Win32 DLL skeleton:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    DLLSKEL
    DLLUSER
```

For the basic COM object samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    COMOBJ
    COMUSER
```

For the basic in-process DLL component client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    DLLSERVE
    DLLCLIEN
```

For the licensed component client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    LICSERVE
    LICCLIEN
```

For the standard marshaling samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    MARSHAL
    MARSHAL2
```

For the out-of-process local client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    MARSHAL
    LOCSERVE
    LOCCLIEN
```

For the apartment model client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    MARSHAL
    APTSERVE
    APTCLIEN
```

For the DCOM (Distributed COM) client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    MARSHAL
    APTSERVE
    REMCLIEN
```

For the free threading client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    FRESERVE
    FRECLIEN
```

For the connectable COM object client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    CONSERVE
    CONCLIEN
```

For the structured storage client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    STOSERVE
    STOCLIEN
```

For the persistent object client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    PERSERVE
    PERTEXT
    PERDRAW
    PERCLIEN
```

For the DCOM security client/server samples:

``` syntax
[destination]
    APPUTIL
    INC
    LIB
    REGISTER
    DCDMARSH
    DCDSERVE
    DCOMDRAW
```

 

 




