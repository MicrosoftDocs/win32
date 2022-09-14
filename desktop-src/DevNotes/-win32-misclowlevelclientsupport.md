---
description: This topic contains information about low-level APIs that are used by the Windows client infrastructure.
ms.assetid: 14a6e970-2032-420e-9930-a15909dbbb97
title: Miscellaneous Low-Level Client Support
ms.topic: article
ms.date: 05/31/2018
---

# Miscellaneous Low-Level Client Support

This topic contains information about low-level APIs that are used by the Windows client infrastructure.

### Functions




| Topic | Contents | 
|-------|----------|
| <a href="/windows/desktop/api/winbase/nf-winbase-_lclose"><strong>_lclose</strong></a> | The _lclose function closes the specified file so that it is no longer available for reading or writing. This function is provided for compatibility with 16-bit versions of Windows. Win32-based applications should use the CloseHandle function.<br /> | 
| <a href="/windows/desktop/api/winbase/nf-winbase-_lopen"><strong>_lopen</strong></a> | The _lopen function opens an existing file and sets the file pointer to the beginning of the file. This function is provided for compatibility with 16-bit versions of Windows. Win32-based applications should use the CreateFile function. <br /> | 
| <a href="/windows/desktop/api/winbase/nf-winbase-_lread"><strong>_lread</strong></a> | The _lread function reads data from the specified file. This function is provided for compatibility with 16-bit versions of Windows. Win32-based applications should use the ReadFile function. <br /> | 
| <a href="/windows/desktop/api/comppkgsup/nf-comppkgsup-aredvdcodecsenabled"><strong>AreDvdCodecsEnabled</strong></a> | Returns a value indicating whether DVD codecs are enabled on the current device.<br /> | 
| <a href="/windows/desktop/api/Winuser/nf-winuser-disableprocesswindowsghosting"><strong>DisableProcessWindowsGhosting</strong></a> | Disables the window ghosting feature for the calling GUI process. Window ghosting is a Windows Manager feature that lets the user minimize, move, or close the main window of an application that is not responding.<br /> | 
| <a href="/windows/desktop/api/comppkgsup/nf-comppkgsup-getmediacomponentpackageinfo"><strong>GetMediaComponentPackageInfo</strong></a> | Returns a list of properties for all media codecs installed on the system that meet the specified requirements.<br /> | 
| <a href="/windows/desktop/api/comppkgsup/nf-comppkgsup-getmediaextensioncommunicationfactory"><strong>GetMediaExtensionCommunicationFactory</strong></a> | Creates a communication factory for registering a media extension.<br /> | 
| <a href="/windows/desktop/api/comppkgsup/nf-comppkgsup-instantiatecomponentfrompackage"><strong>InstantiateComponentFromPackage</strong></a> | Creates an instance of a class in an application package. <br /> | 
| <a href="/windows/desktop/api/comppkgsup/nf-comppkgsup-ismediabehaviorenabled"><strong>IsMediaBehaviorEnabled</strong></a> | Gets a value indicating whether the media behavior associated with the specified GUID is enabled.<br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-ntclose"><strong>NtClose</strong></a> | Deprecated. This function is used to close the specified handle. <a href="/windows/desktop/api/Winternl/nf-winternl-ntclose"><strong>NtClose</strong></a> is superseded by <a href="/windows/desktop/api/handleapi/nf-handleapi-closehandle">CloseHandle</a>.<br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-ntdeviceiocontrolfile"><strong>NtDeviceIoControlFile</strong></a> | Deprecated. Builds descriptors for the supplied buffer(s) and passes the untyped data to the device driver associated with the file handle. <a href="/windows/desktop/api/Winternl/nf-winternl-ntdeviceiocontrolfile"><strong>NtDeviceIoControlFile</strong></a> is superseded by <a href="/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol">DeviceIoControl</a>.<br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-ntwaitforsingleobject"><strong>NtWaitForSingleObject</strong></a> | Deprecated. Waits until the specified object attains a state of <code>signaled</code>. <a href="/windows/desktop/api/Winternl/nf-winternl-ntwaitforsingleobject"><strong>NtWaitForSingleObject</strong></a> is superseded by <a href="/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobject">WaitForSingleObject</a>.<br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlansistringtounicodestring"><strong>RtlAnsiStringToUnicodeString</strong></a> | Converts the specified ANSI source string into a Unicode string. <br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlchartointeger"><strong>RtlCharToInteger</strong></a> | Converts a character string to an integer.<br /> | 
| <a href="/previous-versions//ff899322(v=vs.85)"><strong>RtlFormatCurrentUserKeyPath</strong></a> | Initializes the supplied buffer with a string representation of the SID for the current user. <br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlfreeansistring"><strong>RtlFreeAnsiString</strong></a> | Frees the string buffer allocated by <a href="/windows/desktop/api/Winternl/nf-winternl-rtlunicodestringtoansistring"><strong>RtlUnicodeStringToAnsiString</strong></a>.<br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlfreeoemstring"><strong>RtlFreeOemString</strong></a> | Frees the string buffer allocated by <a href="/windows/desktop/api/Winternl/nf-winternl-rtlunicodestringtooemstring"><strong>RtlUnicodeStringToOemString</strong></a>.<br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlfreeunicodestring"><strong>RtlFreeUnicodeString</strong></a> | Frees the string buffer allocated by <a href="/windows/desktop/api/Winternl/nf-winternl-rtlansistringtounicodestring"><strong>RtlAnsiStringToUnicodeString</strong></a> or by <a href="https://msdn.microsoft.com/library/ms803011.aspx">RtlUpcaseUnicodeString</a>.<br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlinitstring"><strong>RtlInitString</strong></a> | Initializes a counted string. <br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlinitunicodestring"><strong>RtlInitUnicodeString</strong></a> | Initializes a counted Unicode string. <br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlunicodestringtoansistring"><strong>RtlUnicodeStringToAnsiString</strong></a> | Converts the specified Unicode source string into an ANSI string. <br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlunicodestringtooemstring"><strong>RtlUnicodeStringToOemString</strong></a> | This functions converts the specified Unicode source string into an OEM string. The translation is done with respect to the OEM code page (OCP). <br /> | 
| <a href="/windows/desktop/api/Winternl/nf-winternl-rtlunicodetomultibytesize"><strong>RtlUnicodeToMultiByteSize</strong></a> | Determines how many bytes are needed to represent a Unicode string as an ANSI string.<br /> | 
| <a href="/windows/desktop/devnotes/rtlunicodetoutf8n"><strong>RtlUnicodeToUTF8N</strong></a> | The <a href="/windows/desktop/devnotes/rtlunicodetoutf8n"><strong>RtlUnicodeToUTF8N</strong></a> function translates the specified Unicode string into a new character string, using the 8-bit Unicode Transformation Format (UTF-8) code page.<br /> | 
| <a href="/windows/desktop/devnotes/rtlutf8tounicoden"><strong>RtlUTF8ToUnicodeN</strong></a> | The <a href="/windows/desktop/devnotes/rtlutf8tounicoden"><strong>RtlUTF8ToUnicodeN</strong></a> function translates the specified source string into a Unicode string, using the UTF-8 code page.<br /> | 
| <a href="/windows/desktop/api/Ime/nf-ime-sendimemessageexa"><strong>SendIMEMessageEx</strong></a> | Specifies an action or processing for the Input Method Editor (IME) through a specified subfunction.<blockquote>[!Note]<br />This function is obsolete and should not be used.</blockquote><br /><br /> | 
| <a href="/windows/desktop/api/Winnls32/nf-winnls32-winnlsenableime"><strong>WINNLSEnableIME</strong></a> | Temporarily enables or disables an IME and, at the same time, turns on or off the display of all windows owned by the IME.<blockquote>[!Note]<br />This function is obsolete and should not be used.</blockquote><br /><br /> | 




 

### Structures



| Topic                                 | Contents                                                                                                                                                                                                                              |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMESTRUCT**](/windows/win32/api/ime/ns-ime-imestruct) | Used by [**SendIMEMessageEx**](/windows/desktop/api/Ime/nf-ime-sendimemessageexa) to specify the subfunction to be executed in the IME message and its parameters. This structure is also used to receive return values from those subfunctions.<br/> |
| [**STRING**](/windows/desktop/api/Winternl/ns-winternl-string)       | This structure is used with the [**RtlUnicodeStringToOemString**](/windows/desktop/api/Winternl/nf-winternl-rtlunicodestringtooemstring) function. <br/>                                                                                                              |



 

### Compiler Routines



| Topic                                                             | Contents                                                                                                     |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**\_\_C\_specific\_handler Routine**](--c-specific-handler2.md) | [**\_\_C\_specific\_handler**](--c-specific-handler2.md) is a helper routine for the C compiler.<br/> |
| [\_alldiv Routine](-win32-alldiv.md)                             | [\_alldiv Routine](-win32-alldiv.md) is a helper routine for the C compiler.<br/>                     |
| [\_allmul](-win32-allmul.md) | Multiplies two **LONGLONG** or **ULONGLONG**. |
| [\_aulldiv](-win32-aulldiv.md) | Divides two **ULONGLONG** integers. |
| [\_chkstk Routine](-win32-chkstk.md)                             | [\_chkstk Routine](-win32-chkstk.md) is a helper routine for the C compiler.<br/>                     |
