---
Description: Describes how to use the Microsoft Error Lookup Tool to find text explanations of hexadecimal error codes in Windows.
title: How to download and use the Microsoft Error Lookup Tool
ms.topic: article
ms.date: 11/01/2019
---

# How to download and use the Microsoft Error Lookup Tool

Microsoft Windows and other software components report status information, including error-level information, in the form of hexadecimal values. These values often use DWORD (double word) format. The software uses this format to conserve energy and compute resources. One DWORD value often takes less space in memory than a string of Unicode text. However, this means that the stored value, by itself, may not have meaning for end users and technicians. They have to convert those codes to human-readable text to understand the event as reported by event logs, text logs, and other diagnostic sources.

There are several options available to decode Microsoft event message codes:

- Use your favorite search engine, search for the code, and hope for the best.
- Install the Debugging Tools for Windows, load a memory dump file, then run **\!err \<code>**.
- Search the Microsoft Protocols site, which contains raw text of many of the error codes. For more information, see [[MS-ERREF]: Windows Error Codes](https://docs.microsoft.com/openspecs/windows_protocols/ms-erref/1bc92ddf-b79e-413c-bbaa-99a5281a6c90).
- Use the Microsoft Error Lookup Tool (described in this article).

The Microsoft Error Lookup Tool quickly and easily produces the message text that is associated with a DWORD hexadecimal status code or other code. This text is defined in various Microsoft source-code header files, such as Winerror.h, Setupapi.h, and so on.

> [!NOTE]
> This tool is digitally signed by Microsoft. The following is the SHA256 information for the file download:
> |Algorithm |Hash |
> | - | - |
> |SHA256 |88739EC82BA16A0B4A3C83C1DD2FCA6336AD8E2A1E5F1238C085B1E86AB8834A |
> Business environments may restrict what files can run and from where.
> - Before you can download and run this tool, you may need to get permission and perhaps a security exception.
> - You may be allowed to store this tool in your 'Documents' folder. Or, this tool could be available on a central file server, which may be the ideal scenario.

## Usage

1. Download the tool by selecting [this link](https://download.microsoft.com/download/4/3/2/432140e8-fb6c-4145-8192-25242838c542/Err_6.4.5/Err_6.4.5.exe).
1. Go to your download folder, and copy or move the downloaded file (Err_6.4.5.exe) to folder in which you will store the tool. You do not have to unzip or install the file.
   > [!NOTE]
   > If you copy or move the file to a folder that is listed in your operating system's PATH statement, it will work from any command prompt.

1. Open a Command Prompt window, and if necessary, change directory to the location of the Error Lookup Tool.
1. Run the following command:
   ```cmd
   Err_6.4.5.exe <error code>
   ```
   In this command, \<*error code*> represents the hexadecimal code that you want to look up.

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

## More Information

This simple utility decodes most Microsoft error codes (as of the date that the tool was compiled). Keep in mind that this is a "point-in-time" tool. Over time, as new releases of Windows add new event and error codes, you may need to download a new version of the tool. You can check the Microsoft Download Center for a new version, or consult the [Microsoft Protocols](https://docs.microsoft.com/openspecs/windows_protocols/ms-erref/1bc92ddf-b79e-413c-bbaa-99a5281a6c90) site.
