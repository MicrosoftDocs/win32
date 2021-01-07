---
description: 'Every process has an environment block that contains a set of environment variables and their values. There are two types of environment variables: user environment variables (set for each user) and system environment variables (set for everyone).'
ms.assetid: '6732b12f-ced1-4769-b947-79da8fd2237a'
title: Environment Variables
ms.topic: article
ms.date: 05/31/2018
---

# Environment Variables

Every process has an environment block that contains a set of environment variables and their values. There are two types of environment variables: user environment variables (set for each user) and system environment variables (set for everyone).

By default, a child process inherits the environment variables of its parent process. Programs started by the command processor inherit the command processor's environment variables. To specify a different environment for a child process, create a new environment block and pass a pointer to it as a parameter to the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function.

The command processor provides the **set** command to display its environment block or to create new environment variables. You can also view or modify the environment variables by selecting **System** from the **Control Panel**, selecting **Advanced system settings**, and clicking **Environment Variables**.

Each environment block contains the environment variables in the following format:<dl> *Var1*=*Value1*\\0  
*Var2*=*Value2*\\0  
*Var3*=*Value3*\\0  
...  
*VarN*=*ValueN*\\0\\0  
</dl>

The name of an environment variable cannot include an equal sign (=).

The [**GetEnvironmentStrings**](/windows/win32/api/processenv/nf-processenv-getenvironmentstrings) function returns a pointer to the environment block of the calling process. This should be treated as a read-only block; do not modify it directly. Instead, use the [**SetEnvironmentVariable**](/windows/desktop/api/WinBase/nf-winbase-setenvironmentvariable) function to change an environment variable. When you are finished with the environment block obtained from **GetEnvironmentStrings**, call the [**FreeEnvironmentStrings**](/windows/win32/api/processenv/nf-processenv-freeenvironmentstringsa) function to free the block.

Calling [**SetEnvironmentVariable**](/windows/desktop/api/WinBase/nf-winbase-setenvironmentvariable) has no effect on the system environment variables. To programmatically add or modify system environment variables, add them to the **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Environment** registry key, then broadcast a [**WM\_SETTINGCHANGE**](/windows/desktop/winmsg/wm-settingchange) message with *lParam* set to the string "Environment". This allows applications, such as the shell, to pick up your updates.

The maximum size of a user-defined environment variable is 32,767 characters. There is no technical limitation on the size of the environment block. However, there are practical limits depending on the mechanism used to access the block. For example, a batch file cannot set a variable that is longer than the maximum command line length.

**Windows Server 2003 and Windows XP:** The maximum size of the environment block for the process is 32,767 characters. Starting with Windows Vista and Windows Server 2008, there is no technical limitation on the size of the environment block.

The [**GetEnvironmentVariable**](/windows/desktop/api/WinBase/nf-winbase-getenvironmentvariable) function determines whether a specified variable is defined in the environment of the calling process, and, if so, what its value is.

To retrieve a copy of the environment block for a given user, use the [**CreateEnvironmentBlock**](/windows/win32/api/userenv/nf-userenv-createenvironmentblock) function.

To expand environment-variable strings, use the [**ExpandEnvironmentStrings**](/windows/desktop/api/processenv/nf-processenv-expandenvironmentstringsa) function.

## Related topics

<dl> <dt>

[Changing Environment Variables](changing-environment-variables.md)
</dt> <dt>

[User Environment Variables](../shell/user-environment-variables.md)
</dt> </dl>

 

 
