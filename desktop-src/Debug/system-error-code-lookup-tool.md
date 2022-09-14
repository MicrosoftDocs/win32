---
description: Describes how to use the Microsoft Error Lookup Tool to find text explanations of hexadecimal error codes in Windows.
title: The Microsoft Error Lookup Tool
ms.topic: article
ms.date: 12/4/2019
---

# The Microsoft Error Lookup Tool

The Microsoft Error Lookup Tool displays the message text that is associated with a hexadecimal status code (or other code). This text is defined in various Microsoft source-code header files, such as Winerror.h, Setupapi.h, and so on.

The tool is digitally signed by Microsoft. The following is the SHA256 information for the file download:  

|Algorithm |Hash |
| --- | --- |
|SHA256 |88739EC82BA16A0B4A3C83C1DD2FCA6336AD8E2A1E5F1238C085B1E86AB8834A |

> [!NOTE]
> Business environments may restrict which files can run and from where. Before you download and run this tool, check the following details:
> - Do you have to have permission or a security exception in order to download or run the tool?
> - Can you store and run this tool on your computer (for example, in your Documents folder)? Or do you have to store and run the tool on a specialized computer, such as a central file server?

## Usage

1. Download the tool by selecting [this link](https://download.microsoft.com/download/4/3/2/432140e8-fb6c-4145-8192-25242838c542/Err_6.4.5/Err_6.4.5.exe).
1. If you didn't specify a location in step 1, go to your download folder, and copy or move the downloaded file (Err_6.4.5.exe) to folder in which you will store the tool. You do not have to expand or install the file.
   > [!NOTE]
   > If you copy or move the file to a folder that is listed in your operating system's **Path** environment variable, it will work at any command prompt.

1. Open a Command Prompt window. If necessary, change the directory to the location of the Error Lookup Tool.
1. Run the following command:
   ```cmd
   Err_6.4.5.exe <error code>
   ```
   > [!NOTE]  
   > In this command, \<*error code*> represents the hexadecimal code that you want to look up.

## Examples

```cmd
C:\Tools>Err_6.4.5.exe c000021a
# for hex 0xc000021a / decimal -1073741286
 STATUS_SYSTEM_PROCESS_TERMINATED                ntstatus.h​
# {Fatal System Error}​
# The %hs system process terminated unexpectedly with a​
# status of 0x%08x (0x%08x 0x%08x).​
# The system has been shut down.​
# as an HRESULT: Severity: FAILURE (1), FACILITY_NULL (0x0), Code 0x21a​
# for hex 0x21a / decimal 538​
 ERROR_ABIOS_ERROR                               winerror.h​
# An error occurred in the ABIOS subsystem.​
# 2 matches found for "c000021a"
```

```cmd
C:\Tools>Err_6.4.5.exe 7b
# for hex 0x7b / decimal 123
 INACCESSIBLE_BOOT_DEVICE                       bugcodes.h​
 NMERR_SECURITY_BREACH_CAPTURE_DELETED              netmon.h​
 ERROR_INVALID_NAME                       winerror.h​
# The filename, directory name, or volume label syntax is​
# incorrect.​
# as an HRESULT: Severity: SUCCESS (0), FACILITY_NULL (0x0), Code 0x7b​
# for hex 0x7b / decimal 123​
 ERROR_INVALID_NAME                       winerror.h​
# The filename, directory name, or volume label syntax is​
# incorrect.​
# 4 matches found for "7b"
```

## More information

Keep in mind that this is a "point-in-time" tool. The Microsoft Error Lookup Tool decodes most Microsoft error codes as of the date on which the tool was compiled. As new releases of Windows add new event and error codes, you may have to download a new version of the Error Lookup Tool. Check the Microsoft Download Center for a new version, or see [Error Codes](system-error-codes.md).
