---
title: Searching for Files
description: By default, RC searches for header files and resource files (such as icon and cursor files) first in the current directory and then in the directories specified by the INCLUDE environment variable.
ms.assetid: 6c8c905d-b0f6-4665-9a93-62617ff30137
ms.topic: article
ms.date: 05/31/2018
---

# Searching for Files

By default, RC searches for header files and resource files (such as icon and cursor files) first in the current directory and then in the directories specified by the INCLUDE environment variable. (The PATH environment variable has no effect on which directories RC searches.)

## Adding a Directory to Search

You can use the **/i** option to add a directory to the list of directories RC searches. The compiler then searches the directories in the following order:

1.  The current directory
2.  The directory or directories you specify by using the **/i** option, in the order in which they appear on the RC command line
3.  The list of directories specified by the INCLUDE environment variable, in the order in which the variable lists them, unless you specify the **/x** option

The following example compiles the resource-definition file MyApp.rc:

**rc /i c:\\source\\stuff /i d:\\resources myapp.rc**

When compiling the script MyApp.rc, RC searches for header files and resource files first in the current directory, then in C:\\Source\\Stuff and D:\\Resources, and then in the directories specified by the INCLUDE environment variable.

## Ignoring the INCLUDE Environment Variable

You can prevent RC from using the INCLUDE environment variable when determining the directories to search. To do so, use the **/x** option. The compiler then searches for files only in the current directory and in any directories you specify by using the **/i** option.

The following command compiles the script file MyApp.rc:

**rc /x /i c:\\source\\stuff myapp.rc**

When compiling the script MyApp.rc, RC searches for header files and resource files first in the current directory and then in C:\\Source\\Stuff. It does not search the directories specified by the INCLUDE environment variable.

 

 




