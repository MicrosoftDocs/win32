---
Description: The following functions are used with error handling.
ms.assetid: ae8ad3a2-1f1a-46d6-adaa-74c50c07dcc5
title: Error Handling Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Error Handling Functions

The following functions are used with error handling.



| Function                                                 | Description                                                                                                                   |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**Beep**](/windows/win32/WinBase/?branch=master)                                     | Generates simple tones on the speaker.                                                                                        |
| [**CaptureStackbackTrace**](capturestackbacktrace.md)   | Captures a stack back trace by walking up the stack and recording the information for each frame.                             |
| [**FatalAppExit**](/windows/win32/WinBase/?branch=master)                     | Displays a message box and terminates the application when the message box is closed.                                         |
| [**FlashWindow**](/windows/win32/Winuser/nf-winuser-flashwindow?branch=master)                       | Flashes the specified window one time.                                                                                        |
| [**FlashWindowEx**](/windows/win32/Winuser/nf-winuser-flashwindowex?branch=master)                   | Flashes the specified window.                                                                                                 |
| [**FormatMessage**](/windows/win32/WinBase/nf-winbase-formatmessage?branch=master)                   | Formats a message string.                                                                                                     |
| [**GetErrorMode**](/windows/win32/WinBase/?branch=master)                     | Retrieves the error mode for the current process.                                                                             |
| [**GetLastError**](/windows/win32/WinBase/?branch=master)                     | Retrieves the calling thread's last-error code value.                                                                         |
| [**GetThreadErrorMode**](/windows/win32/WinBase/?branch=master)         | Retrieves the error mode for the calling thread.                                                                              |
| [**MessageBeep**](/windows/win32/WinUser/nf-winuser-messagebeep?branch=master)                       | Plays a waveform sound.                                                                                                       |
| [**RtlLookupFunctionEntry**](/windows/win32/WinNT/nf-winnt-rtllookupfunctionentry?branch=master) | Searches the active function tables for an entry that corresponds to the specified PC value.                                  |
| [**RtlNtStatusToDosError**](/windows/win32/Winternl/nf-winternl-rtlntstatustodoserror?branch=master)   | Retrieves the system error code that corresponds to the specified NT error code.                                              |
| [**RtlPcToFileHeader**](/windows/win32/WinNT/nf-winnt-rtlpctofileheader?branch=master)           | Retrieves the base address of the image that contains the specified PC value.                                                 |
| [**RtlUnwind**](/windows/win32/WinNT/nf-winnt-rtlunwind?branch=master)                           | Initiates an unwind of procedure call frames.                                                                                 |
| [**RtlUnwind2**](/windows/win32/WinNT/nf-winnt-rtlunwind2?branch=master)                         | Initiates an unwind of procedure call frames.                                                                                 |
| [**RtlUnwindEx**](/windows/win32/WinNT/nf-winnt-rtlunwindex?branch=master)                       | Initiates an unwind of procedure call frames.                                                                                 |
| [**RtlVirtualUnwind**](/windows/win32/WinNT/nf-winnt-rtlvirtualunwind?branch=master)             | Retrieves the invocation context of the function that precedes the specified function context.                                |
| [**SetErrorMode**](/windows/win32/WinBase/?branch=master)                     | Controls whether the system will handle the specified types of serious errors, or whether the process will handle them.       |
| [**SetLastError**](/windows/win32/WinBase/?branch=master)                     | Sets the last-error code for the calling thread.                                                                              |
| [**SetLastErrorEx**](/windows/win32/Winuser/nf-winuser-setlasterrorex?branch=master)                 | Sets the last-error code for the calling thread.                                                                              |
| [**SetThreadErrorMode**](/windows/win32/WinBase/?branch=master)         | Controls whether the system will handle the specified types of serious errors or whether the calling thread will handle them. |



 

 

 



