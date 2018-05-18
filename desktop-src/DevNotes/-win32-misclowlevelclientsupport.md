---
Description: 'This topic contains information about low-level APIs that are used by the Windows client infrastructure.'
ms.assetid: '14a6e970-2032-420e-9930-a15909dbbb97'
title: 'Miscellaneous Low-Level Client Support'
---

# Miscellaneous Low-Level Client Support

This topic contains information about low-level APIs that are used by the Windows client infrastructure.

### Functions



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Contents</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>_lclose</strong>](-lclose.md)</td>
<td>The _lclose function closes the specified file so that it is no longer available for reading or writing. This function is provided for compatibility with 16-bit versions of Windows. Win32-based applications should use the CloseHandle function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>_lopen</strong>](-lopen.md)</td>
<td>The _lopen function opens an existing file and sets the file pointer to the beginning of the file. This function is provided for compatibility with 16-bit versions of Windows. Win32-based applications should use the CreateFile function. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>_lread</strong>](-lread.md)</td>
<td>The _lread function reads data from the specified file. This function is provided for compatibility with 16-bit versions of Windows. Win32-based applications should use the ReadFile function. <br/></td>
</tr>
<tr class="even">
<td>[<strong>AreDvdCodecsEnabled</strong>](aredvdcodecsenabled.md)</td>
<td>Returns a value indicating whether DVD codecs are enabled on the current device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DisableProcessWindowsGhosting</strong>](disableprocesswindowsghosting.md)</td>
<td>Disables the window ghosting feature for the calling GUI process. Window ghosting is a Windows Manager feature that lets the user minimize, move, or close the main window of an application that is not responding.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetMediaComponentPackageInfo</strong>](getmediacomponentpackageinfo.md)</td>
<td>Returns a list of properties for all media codecs installed on the system that meet the specified requirements.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetMediaExtensionCommunicationFactory</strong>](getmediaextensioncommunicationfactory.md)</td>
<td>Creates a communication factory for registering a media extension.<br/></td>
</tr>
<tr class="even">
<td>[<strong>InstantiateComponentFromPackage</strong>](instantiatecomponentfrompackage.md)</td>
<td>Creates an instance of a class in an application package. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IsMediaBehaviorEnabled</strong>](ismediabehaviorenabled.md)</td>
<td>Gets a value indicating whether the media behavior associated with the specified GUID is enabled.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NtClose</strong>](ntclose.md)</td>
<td>Deprecated. This function is used to close the specified handle. [<strong>NtClose</strong>](ntclose.md) is superseded by [CloseHandle](http://msdn.microsoft.com/en-us/library/ms724211(VS.85).aspx).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NtDeviceIoControlFile</strong>](ntdeviceiocontrolfile.md)</td>
<td>Deprecated. Builds descriptors for the supplied buffer(s) and passes the untyped data to the device driver associated with the file handle. [<strong>NtDeviceIoControlFile</strong>](ntdeviceiocontrolfile.md) is superseded by [DeviceIoControl](http://msdn.microsoft.com/en-us/library/aa363216(VS.85).aspx).<br/></td>
</tr>
<tr class="even">
<td>[<strong>NtWaitForSingleObject</strong>](ntwaitforsingleobject.md)</td>
<td>Deprecated. Waits until the specified object attains a state of <code>signaled</code>. [<strong>NtWaitForSingleObject</strong>](ntwaitforsingleobject.md) is superseded by [WaitForSingleObject](http://msdn.microsoft.com/en-us/library/ms687032.aspx).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RtlAnsiStringToUnicodeString</strong>](rtlansistringtounicodestring.md)</td>
<td>Converts the specified ANSI source string into a Unicode string. <br/></td>
</tr>
<tr class="even">
<td>[<strong>RtlCharToInteger</strong>](rtlchartointeger.md)</td>
<td>Converts a character string to an integer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RtlFormatCurrentUserKeyPath</strong>](winprog.rtlformatcurrentuserkeypath)</td>
<td>Initializes the supplied buffer with a string representation of the SID for the current user. <br/></td>
</tr>
<tr class="even">
<td>[<strong>RtlFreeAnsiString</strong>](rtlfreeansistring.md)</td>
<td>Frees the string buffer allocated by [<strong>RtlUnicodeStringToAnsiString</strong>](rtlunicodestringtoansistring.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RtlFreeOemString</strong>](rtlfreeoemstring.md)</td>
<td>Frees the string buffer allocated by [<strong>RtlUnicodeStringToOemString</strong>](rtlunicodestringtooemstring.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>RtlFreeUnicodeString</strong>](rtlfreeunicodestring.md)</td>
<td>Frees the string buffer allocated by [<strong>RtlAnsiStringToUnicodeString</strong>](rtlansistringtounicodestring.md) or by [RtlUpcaseUnicodeString](http://msdn.microsoft.com/en-us/library/ms803011.aspx).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RtlInitString</strong>](rtlinitstring.md)</td>
<td>Initializes a counted string. <br/></td>
</tr>
<tr class="even">
<td>[<strong>RtlInitUnicodeString</strong>](rtlinitunicodestring.md)</td>
<td>Initializes a counted Unicode string. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>RtlUnicodeStringToAnsiString</strong>](rtlunicodestringtoansistring.md)</td>
<td>Converts the specified Unicode source string into an ANSI string. <br/></td>
</tr>
<tr class="even">
<td>[<strong>RtlUnicodeStringToOemString</strong>](rtlunicodestringtooemstring.md)</td>
<td>This functions converts the specified Unicode source string into an OEM string. The translation is done with respect to the OEM code page (OCP). <br/></td>
</tr>
<tr class="odd">
<td>[<strong>RtlUnicodeToMultiByteSize</strong>](rtlunicodetomultibytesize.md)</td>
<td>Determines how many bytes are needed to represent a Unicode string as an ANSI string.<br/></td>
</tr>
<tr class="even">
<td>[<strong>RtlUnicodeToUTF8N</strong>](rtlunicodetoutf8n.md)</td>
<td>The [<strong>RtlUnicodeToUTF8N</strong>](rtlunicodetoutf8n.md) function translates the specified Unicode string into a new character string, using the 8-bit Unicode Transformation Format (UTF-8) code page.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RtlUTF8ToUnicodeN</strong>](rtlutf8tounicoden.md)</td>
<td>The [<strong>RtlUTF8ToUnicodeN</strong>](rtlutf8tounicoden.md) function translates the specified source string into a Unicode string, using the UTF-8 code page.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SendIMEMessageEx</strong>](-win32-sendimemessageex.md)</td>
<td>Specifies an action or processing for the Input Method Editor (IME) through a specified subfunction.
<blockquote>
[!Note]<br />
This function is obsolete and should not be used.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>WINNLSEnableIME</strong>](-win32-winnlsenableime.md)</td>
<td>Temporarily enables or disables an IME and, at the same time, turns on or off the display of all windows owned by the IME.
<blockquote>
[!Note]<br />
This function is obsolete and should not be used.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

### Structures



| Topic                                 | Contents                                                                                                                                                                                                                              |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMESTRUCT**](-win32-imestruct.md) | Used by [**SendIMEMessageEx**](-win32-sendimemessageex.md) to specify the subfunction to be executed in the IME message and its parameters. This structure is also used to receive return values from those subfunctions.<br/> |
| [**STRING**](-win32-string.md)       | This structure is used with the [**RtlUnicodeStringToOemString**](rtlunicodestringtooemstring.md) function. <br/>                                                                                                              |



 

### Compiler Routines



| Topic                                                             | Contents                                                                                                     |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**\_\_C\_specific\_handler Routine**](--c-specific-handler2.md) | [**\_\_C\_specific\_handler**](--c-specific-handler2.md) is a helper routine for the C compiler.<br/> |
| [\_alldiv Routine](-win32-alldiv.md)                             | [\_alldiv Routine](-win32-alldiv.md) is a helper routine for the C compiler.<br/>                     |
| [\_chkstk Routine](-win32-chkstk.md)                             | [\_chkstk Routine](-win32-chkstk.md) is a helper routine for the C compiler.<br/>                     |



 

 

 




