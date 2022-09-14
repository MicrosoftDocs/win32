---
description: All functions, prototypes, structures, and constants are defined in the Winwlx.h header file.
ms.assetid: 13b5bc92-583d-4031-94f9-f84dbfbf7ee7
title: Building and Testing a GINA DLL
ms.topic: article
ms.date: 05/31/2018
---

# Building and Testing a GINA DLL

All functions, prototypes, structures, and constants are defined in the Winwlx.h header file.

> [!Note]  
> GINA DLLs are ignored in Windows Vista.

 

To test a [*GINA*](/windows/desktop/SecGloss/g-gly) DLL, use the Winlogon.exe from a checked version of the operating system, which is available with the Microsoft Windows Driver Development Kit (DDK). The checked version of [*Winlogon*](/windows/desktop/SecGloss/w-gly) supports debugging GINAs as follows:

-   You can use the following syntax to create a section in Win.ini to specify Winlogon debugging options.

    ``` syntax
    [WinlogonDebug]
    LogFile=C:\Winlogon.log
    DebugFlags=Flag1 [, Flag2 ...]
    ```

    If specified, **LogFile** should contain the fully qualified name of the file that will be used to log debugging information. If the file does not exist, it will be created.

    The **DebugFlags** options specify which kinds of debugging information to write to the log file, or debugger. **DebugFlags** can contain one or more of the following flags.

    

    | Debugging flag | Description                                                                                                                                                                |
    |----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | CoolSwitch     | The CTRL+ALT+SHIFT+TAB key combination will cause a debug break in Winlogon.                                                                                               |
    | Error          | Print errors.                                                                                                                                                              |
    | Init           | Print initialization and progress messages.                                                                                                                                |
    | Notify         | Print notification package messages.                                                                                                                                       |
    | SAS            | Print information about [*secure attention sequence*](/windows/desktop/SecGloss/s-gly) (SAS) notifications. |
    | State          | Print messages when Winlogon changes state.                                                                                                                                |
    | Timeout        | Print messages when a time limit is set or a time limit is reached.                                                                                                        |
    | Trace          | Print verbose trace information.                                                                                                                                           |
    | Warn           | Print warnings.                                                                                                                                                            |

    

     

-   To start the checked version of Winlogon in a debugger, add the following entry to the registry:

    ```
    HKEY_LOCAL_MACHINE
       Software
          Microsoft
             Windows NT
                CurrentVersion
                   Image File Execution Options
                      winlogon.exe
                         Debugger = ntsd -d<dl>
    <dt>

                     Data type
</dt>
    <dd>                     REG_SZ</dd>
    </dl>
    ```

> [!NOTE]
> You must use the Windows symbolic debugger (NTSD) to debug Winlogon.

## Related topics

<dl> <dt>

[Loading and Running a GINA DLL](loading-and-running-a-gina-dll.md)
</dt> <dt>

[GINA Export Functions](authentication-functions.md)
</dt> <dt>

[GINA Structures](authentication-structures.md)
</dt> <dt>

[Terminal Services GINA Functions](terminal-services-gina-functions.md)
</dt> </dl>

 

 
