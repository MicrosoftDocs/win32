---
Description: 
title: How to download and use the Microsoft Error Lookup Tool
ms.topic: article
ms.date: 10/29/2019
---

# How to download and use the Microsoft Error Lookup Tool

Microsoft Windows and other software components report status messages, including error-level information, in the form of hexadecimal values. These values often use DWORD (double word) format. The software uses this format to conserve energy and compute resources. One DWORD value often takes less space in memory than a string of Unicode text. However, this means that end-users and technicians have to convert those codes to human-readable text, so that you have a better idea of the event being reported in event logs, text logs, and other diagnostic sources.

There are several options available to decode Microsoft event message codes:

- Use your favorite search engine, search for the code, hope for the best
- Install the Debugging Tools for Windows, load a memory dump file, then run \!err \<code>
- Search the Microsoft Protocols site, which contains raw text of many of the error codes. For more information, see [[MS-ERREF]: Windows Error Codes](https://docs.microsoft.com/openspecs/windows_protocols/ms-erref/1bc92ddf-b79e-413c-bbaa-99a5281a6c90)
- Use the Microsoft Error Lookup Tool (download details below)

The Microsoft Error Lookup Tool quickly and easily converts DWORD status and other codes to the text of the message. This text is defined in various Microsoft source-code header files, such as Winerror.h, Setupapi.h, and so on.

> [!NOTE]
> This tool is digitally signed by Microsoft. The following is the SHA256 information on the file download:
> |Algorithm |Hash |
> | - | - |
> |SHA256 |88739EC82BA16A0B4A3C83C1DD2FCA6336AD8E2A1E5F1238C085B1E86AB8834A |

## Usage

1. Click the download link, to download Error Lookup Tool.
1. Copy the file "Err_6.4.5.exe" to any folder you like (as is, no installation or unpacking required)
   > [!NOTE]
   > - If you copy it to a folder already in your path, it will work from any command prompt.
   > - In work environments there may be restrictions as to what files can run and from where. You may first need to get permission and perhaps an exception to allow this tool, which is Microsoft digitally signed. Second, there may be restrictions as to what folder or folders you can run this tool from. You might for example be allowed to store this tool in your 'Documents' folder. Or, this tool could be available on a central file server, which may be the ideal scenario
1. Now open a command prompt (Cmd.exe), and if necessary, change drive and directory to the location of the Error Lookup Tool
1. Run the following command:
   ```cmd
   Err_6.4.5.exe <error code>
   ```

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

That's all there is. A simple utility to decode most Microsoft error codes. One thing to keep in mind that this is a "point-in-time" tool. That is, the ability of this tool to decode error messages is only as good as the input files used to compile this tool. As Windows and other technologies evolve, there are needs to define new event and error codes. This tool should have a long shelf-life, but eventually may not be able to resolve event and error codes. In that case either look for a newer version of this tool, or consult the Microsoft Protocols site, as in the URL listed above.

Download Location
https://download.microsoft.com/download/4/3/2/432140e8-fb6c-4145-8192-25242838c542/Err_6.4.5/Err_6.4.5.exe

