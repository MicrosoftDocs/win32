---
description: The following functions are used with error handling.
ms.assetid: ae8ad3a2-1f1a-46d6-adaa-74c50c07dcc5
title: Error Handling Functions
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling Functions

The following functions are used with error handling.



| Function                                                 | Description                                                                                                                   |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**Beep**](/windows/win32/api/utilapiset/nf-utilapiset-beep)                                     | Generates simple tones on the speaker.                                                                                        |
| [**CaptureStackbackTrace**](/previous-versions/windows/desktop/legacy/bb204633(v=vs.85))   | Captures a stack back trace by walking up the stack and recording the information for each frame.                             |
| [**FatalAppExit**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-fatalappexita)                     | Displays a message box and terminates the application when the message box is closed.                                         |
| [**FlashWindow**](/windows/desktop/api/Winuser/nf-winuser-flashwindow)                       | Flashes the specified window one time.                                                                                        |
| [**FlashWindowEx**](/windows/desktop/api/Winuser/nf-winuser-flashwindowex)                   | Flashes the specified window.                                                                                                 |
| [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage)                   | Formats a message string.                                                                                                     |
| [**GetErrorMode**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-geterrormode)                     | Retrieves the error mode for the current process.                                                                             |
| [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror)                     | Retrieves the calling thread's last-error code value.                                                                         |
| [**GetThreadErrorMode**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getthreaderrormode)         | Retrieves the error mode for the calling thread.                                                                              |
| [**MessageBeep**](/windows/desktop/api/WinUser/nf-winuser-messagebeep)                       | Plays a waveform sound.                                                                                                       |
| [**RtlLookupFunctionEntry**](/windows/desktop/api/WinNT/nf-winnt-rtllookupfunctionentry) | Searches the active function tables for an entry that corresponds to the specified PC value.                                  |
| [**RtlNtStatusToDosError**](/windows/desktop/api/Winternl/nf-winternl-rtlntstatustodoserror)   | Retrieves the system error code that corresponds to the specified NT error code.                                              |
| [**RtlPcToFileHeader**](/windows/desktop/api/WinNT/nf-winnt-rtlpctofileheader)           | Retrieves the base address of the image that contains the specified PC value.                                                 |
| [**RtlUnwind**](/windows/desktop/api/WinNT/nf-winnt-rtlunwind)                           | Initiates an unwind of procedure call frames.                                                                                 |
| [**RtlUnwind2**](/windows/desktop/api/WinNT/nf-winnt-rtlunwind2)                         | Initiates an unwind of procedure call frames.                                                                                 |
| [**RtlUnwindEx**](/windows/desktop/api/WinNT/nf-winnt-rtlunwindex)                       | Initiates an unwind of procedure call frames.                                                                                 |
| [**RtlVirtualUnwind**](/windows/desktop/api/WinNT/nf-winnt-rtlvirtualunwind)             | Retrieves the invocation context of the function that precedes the specified function context.                                |
| [**SetErrorMode**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-seterrormode)                     | Controls whether the system will handle the specified types of serious errors, or whether the process will handle them.       |
| [**SetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-setlasterror)                     | Sets the last-error code for the calling thread.                                                                              |
| [**SetLastErrorEx**](/windows/desktop/api/Winuser/nf-winuser-setlasterrorex)                 | Sets the last-error code for the calling thread.                                                                              |
| [**SetThreadErrorMode**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-setthreaderrormode)         | Controls whether the system will handle the specified types of serious errors or whether the calling thread will handle them. |



 

 

 
