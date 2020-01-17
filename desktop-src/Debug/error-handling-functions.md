---
Description: The following functions are used with error handling.
ms.assetid: ae8ad3a2-1f1a-46d6-adaa-74c50c07dcc5
title: Error Handling Functions
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling Functions

The following functions are used with error handling.



| Function                                                 | Description                                                                                                                   |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**Beep**](https://msdn.microsoft.com/library/ms679277(v=VS.85).aspx)                                     | Generates simple tones on the speaker.                                                                                        |
| [**CaptureStackbackTrace**](https://msdn.microsoft.com/library/Bb204633(v=VS.85).aspx)   | Captures a stack back trace by walking up the stack and recording the information for each frame.                             |
| [**FatalAppExit**](https://msdn.microsoft.com/library/ms679336(v=VS.85).aspx)                     | Displays a message box and terminates the application when the message box is closed.                                         |
| [**FlashWindow**](/windows/desktop/api/Winuser/nf-winuser-flashwindow)                       | Flashes the specified window one time.                                                                                        |
| [**FlashWindowEx**](/windows/desktop/api/Winuser/nf-winuser-flashwindowex)                   | Flashes the specified window.                                                                                                 |
| [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage)                   | Formats a message string.                                                                                                     |
| [**GetErrorMode**](https://msdn.microsoft.com/library/ms679355(v=VS.85).aspx)                     | Retrieves the error mode for the current process.                                                                             |
| [**GetLastError**](https://msdn.microsoft.com/library/ms679360(v=VS.85).aspx)                     | Retrieves the calling thread's last-error code value.                                                                         |
| [**GetThreadErrorMode**](https://msdn.microsoft.com/library/Dd553629(v=VS.85).aspx)         | Retrieves the error mode for the calling thread.                                                                              |
| [**MessageBeep**](/windows/desktop/api/WinUser/nf-winuser-messagebeep)                       | Plays a waveform sound.                                                                                                       |
| [**RtlLookupFunctionEntry**](/windows/desktop/api/WinNT/nf-winnt-rtllookupfunctionentry) | Searches the active function tables for an entry that corresponds to the specified PC value.                                  |
| [**RtlNtStatusToDosError**](/windows/desktop/api/Winternl/nf-winternl-rtlntstatustodoserror)   | Retrieves the system error code that corresponds to the specified NT error code.                                              |
| [**RtlPcToFileHeader**](/windows/desktop/api/WinNT/nf-winnt-rtlpctofileheader)           | Retrieves the base address of the image that contains the specified PC value.                                                 |
| [**RtlUnwind**](/windows/desktop/api/WinNT/nf-winnt-rtlunwind)                           | Initiates an unwind of procedure call frames.                                                                                 |
| [**RtlUnwind2**](/windows/desktop/api/WinNT/nf-winnt-rtlunwind2)                         | Initiates an unwind of procedure call frames.                                                                                 |
| [**RtlUnwindEx**](/windows/desktop/api/WinNT/nf-winnt-rtlunwindex)                       | Initiates an unwind of procedure call frames.                                                                                 |
| [**RtlVirtualUnwind**](/windows/desktop/api/WinNT/nf-winnt-rtlvirtualunwind)             | Retrieves the invocation context of the function that precedes the specified function context.                                |
| [**SetErrorMode**](https://msdn.microsoft.com/library/ms680621(v=VS.85).aspx)                     | Controls whether the system will handle the specified types of serious errors, or whether the process will handle them.       |
| [**SetLastError**](https://msdn.microsoft.com/library/ms680627(v=VS.85).aspx)                     | Sets the last-error code for the calling thread.                                                                              |
| [**SetLastErrorEx**](/windows/desktop/api/Winuser/nf-winuser-setlasterrorex)                 | Sets the last-error code for the calling thread.                                                                              |
| [**SetThreadErrorMode**](https://msdn.microsoft.com/library/Dd553630(v=VS.85).aspx)         | Controls whether the system will handle the specified types of serious errors or whether the calling thread will handle them. |



 

 

 



