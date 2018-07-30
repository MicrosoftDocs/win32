---
title: Windows Data Types
description: The data types supported by Windows are used to define function return values, function and message parameters, and structure members.
ms.assetid: 4553cafc-450e-4493-a4d4-cb6e2f274d46
keywords:
- data types
- data types,Windows
- Windows API
- Windows API,data types
- APIENTRY
- ATOM
- BOOL
- BOOLEAN
- BYTE
- CALLBACK
- CCHAR
- CHAR
- COLORREF
- CONST
- DWORD
- DWORDLONG
- DWORD_PTR
- DWORD32
- DWORD64
- FLOAT
- HACCEL
- HALF_PTR
- HANDLE
- HBITMAP
- HBRUSH
- HCOLORSPACE
- HCONV
- HCONVLIST
- HCURSOR
- HDC
- HDDEDATA
- HDESK
- HDROP
- HDWP
- HENHMETAFILE
- HFILE
- HFONT
- HGDIOBJ
- HGLOBAL
- HHOOK
- HICON
- HINSTANCE
- HKEY
- HKL
- HLOCAL
- HMENU
- HMETAFILE
- HMODULE
- HMONITOR
- HPALETTE
- HPEN
- HRESULT
- HRGN
- HRSRC
- HSZ
- HWINSTA
- HWND
- INT
- INT_PTR
- INT8
- INT16
- INT32
- INT64
- LANGID
- LCID
- LCTYPE
- LGRPID
- LONG
- LONGLONG
- LONG_PTR
- LONG32
- LONG64
- LPARAM
- LPBOOL
- LPBYTE
- LPCOLORREF
- LPCSTR
- LPCTSTR
- LPCVOID
- LPCWSTR
- LPDWORD
- LPHANDLE
- LPINT
- LPLONG
- LPSTR
- LPTSTR
- LPVOID
- LPWORD
- LPWSTR
- LRESULT
- PBOOL
- PBOOLEAN
- PBYTE
- PCHAR
- PCSTR
- PCTSTR
- PCWSTR
- PDWORD
- PDWORDLONG
- PDWORD_PTR
- PDWORD32
- PDWORD64
- PFLOAT
- PHALF_PTR
- PHANDLE
- PHKEY
- PINT
- PINT_PTR
- PINT8
- PINT16
- PINT32
- PINT64
- PLCID
- PLONG
- PLONGLONG
- PLONG_PTR
- PLONG32
- PLONG64
- POINTER_32
- POINTER_64
- POINTER_SIGNED
- POINTER_UNSIGNED
- PSHORT
- PSIZE_T
- PSSIZE_T
- PSTR
- PTBYTE
- PTCHAR
- PTSTR
- PUCHAR
- PUHALF_PTR
- PUINT
- PUINT_PTR
- PUINT8
- PUINT16
- PUINT32
- PUINT64
- PULONG
- PULONGLONG
- PULONG_PTR
- PULONG32
- PULONG64
- PUSHORT
- PVOID
- PWCHAR
- PWORD
- PWSTR
- QWORD
- SC_HANDLE
- SC_LOCK
- SERVICE_STATUS_HANDLE
- SHORT
- SIZE_T
- SSIZE_T
- TBYTE
- TCHAR
- UCHAR
- UHALF_PTR
- UINT
- UINT_PTR
- UINT8
- UINT16
- UINT32
- UINT64
- ULONG
- ULONGLONG
- ULONG_PTR
- ULONG32
- ULONG64
- UNICODE_STRING
- USHORT
- USN
- VOID
- WCHAR
- WINAPI
- WORD
- WPARAM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Data Types

The data types supported by Windows are used to define function return values, function and message parameters, and structure members. They define the size and meaning of these elements. For more information about the underlying C/C++ data types, see [Data Type Ranges](Http://go.microsoft.com/fwlink/p/?linkid=83930).

The following table contains the following types: character, integer, Boolean, pointer, and handle. The character, integer, and Boolean types are common to most C compilers. Most of the pointer-type names begin with a prefix of P or LP. Handles refer to a resource that has been loaded into memory.

For more information about handling 64-bit integers, see [Large Integers](large-integers.md).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Data type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="APIENTRY"></span><span id="apientry"></span><strong>APIENTRY</strong></td>
<td>The calling convention for system functions.<br/> This type is declared in WinDef.h as follows:<br/> <code>#define APIENTRY WINAPI</code><br/></td>
</tr>
<tr class="even">
<td><span id="ATOM"></span><span id="atom"></span><strong>ATOM</strong></td>
<td>An atom. For more information, see [About Atom Tables](https://msdn.microsoft.com/library/windows/desktop/ms649053).<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef WORD ATOM;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="BOOL"></span><span id="bool"></span><strong>BOOL</strong></td>
<td>A Boolean variable (should be <strong>TRUE</strong> or <strong>FALSE</strong>).<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef int BOOL;</code><br/></td>
</tr>
<tr class="even">
<td><span id="BOOLEAN"></span><span id="boolean"></span><strong>BOOLEAN</strong></td>
<td>A Boolean variable (should be <strong>TRUE</strong> or <strong>FALSE</strong>).<br/> This type is declared in WinNT.h as follows:<br/> <code>typedef BYTE BOOLEAN;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="BYTE"></span><span id="byte"></span><strong>BYTE</strong></td>
<td>A byte (8 bits).<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef unsigned char BYTE;</code><br/></td>
</tr>
<tr class="even">
<td><span id="CALLBACK"></span><span id="callback"></span><strong>CALLBACK</strong></td>
<td>The calling convention for callback functions.<br/> This type is declared in WinDef.h as follows:<br/> <code>#define CALLBACK __stdcall</code><br/> <strong>CALLBACK</strong>, <strong>WINAPI</strong>, and <strong>APIENTRY</strong> are all used to define functions with the __stdcall calling convention. Most functions in the Windows API are declared using <strong>WINAPI</strong>. You may wish to use <strong>CALLBACK</strong> for the callback functions that you implement to help identify the function as a callback function.<br/></td>
</tr>
<tr class="odd">
<td><span id="CCHAR"></span><span id="cchar"></span><strong>CCHAR</strong></td>
<td>An 8-bit Windows (ANSI) character.<br/> This type is declared in WinNT.h as follows:<br/> <code>typedef char CCHAR;</code><br/></td>
</tr>
<tr class="even">
<td><span id="CHAR"></span><span id="char"></span><strong>CHAR</strong></td>
<td>An 8-bit Windows (ANSI) character. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).<br/> This type is declared in WinNT.h as follows:<br/> <code>typedef char CHAR;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="COLORREF"></span><span id="colorref"></span><strong>COLORREF</strong></td>
<td>The red, green, blue (RGB) color value (32 bits). See [<strong>COLORREF</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183449) for information on this type.<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef DWORD COLORREF;</code><br/></td>
</tr>
<tr class="even">
<td><span id="CONST"></span><span id="const"></span><strong>CONST</strong></td>
<td>A variable whose value is to remain constant during execution. <br/> This type is declared in WinDef.h as follows:<br/> <code>#define CONST const</code><br/></td>
</tr>
<tr class="odd">
<td><span id="DWORD"></span><span id="dword"></span><strong>DWORD</strong></td>
<td>A 32-bit unsigned integer. The range is 0 through 4294967295 decimal.<br/> This type is declared in IntSafe.h as follows:<br/> <code>typedef unsigned long DWORD;</code><br/></td>
</tr>
<tr class="even">
<td><span id="DWORDLONG"></span><span id="dwordlong"></span><strong>DWORDLONG</strong></td>
<td>A 64-bit unsigned integer. The range is 0 through 18446744073709551615 decimal.<br/> This type is declared in IntSafe.h as follows:<br/> <code>typedef unsigned __int64 DWORDLONG;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="DWORD_PTR"></span><span id="dword_ptr"></span><strong>DWORD_PTR</strong></td>
<td>An unsigned long type for pointer precision. Use when casting a pointer to a long type to perform pointer arithmetic. (Also commonly used for general 32-bit parameters that have been extended to 64 bits in 64-bit Windows.)<br/> This type is declared in BaseTsd.h as follows:<br/> <code>typedef ULONG_PTR DWORD_PTR;</code><br/></td>
</tr>
<tr class="even">
<td><span id="DWORD32"></span><span id="dword32"></span><strong>DWORD32</strong></td>
<td>A 32-bit unsigned integer.<br/> This type is declared in BaseTsd.h as follows:<br/> <code>typedef unsigned int DWORD32;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="DWORD64"></span><span id="dword64"></span><strong>DWORD64</strong></td>
<td>A 64-bit unsigned integer.<br/> This type is declared in BaseTsd.h as follows:<br/> <code>typedef unsigned __int64 DWORD64;</code><br/></td>
</tr>
<tr class="even">
<td><span id="FLOAT"></span><span id="float"></span><strong>FLOAT</strong></td>
<td>A floating-point variable.<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef float FLOAT;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="HACCEL"></span><span id="haccel"></span><strong>HACCEL</strong></td>
<td>A handle to an [accelerator table](https://msdn.microsoft.com/library/ms645526(v=VS.85).aspx).<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef HANDLE HACCEL;</code><br/></td>
</tr>
<tr class="even">
<td><span id="HALF_PTR"></span><span id="half_ptr"></span><strong>HALF_PTR</strong></td>
<td>Half the size of a pointer. Use within a structure that contains a pointer and two small fields.<br/> This type is declared in BaseTsd.h as follows:<br/> <span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef _WIN64
 typedef int HALF_PTR;
#else
 typedef short HALF_PTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="odd">
<td><span id="HANDLE"></span><span id="handle"></span><strong>HANDLE</strong></td>
<td><p>A handle to an object.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef PVOID HANDLE;</code></p></td>
</tr>
<tr class="even">
<td><span id="HBITMAP"></span><span id="hbitmap"></span><strong>HBITMAP</strong></td>
<td><p>A handle to a [bitmap](https://msdn.microsoft.com/library/windows/desktop/dd183377).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HBITMAP;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HBRUSH"></span><span id="hbrush"></span><strong>HBRUSH</strong></td>
<td><p>A handle to a [brush](https://msdn.microsoft.com/library/windows/desktop/dd183394).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HBRUSH;</code></p></td>
</tr>
<tr class="even">
<td><span id="HCOLORSPACE"></span><span id="hcolorspace"></span><strong>HCOLORSPACE</strong></td>
<td><p>A handle to a [color space](https://msdn.microsoft.com/en-us/library/Dd316799(v=VS.85).aspx).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HCOLORSPACE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HCONV"></span><span id="hconv"></span><strong>HCONV</strong></td>
<td><p>A handle to a dynamic data exchange (DDE) conversation.</p>
<p>This type is declared in Ddeml.h as follows:</p>
<p><code>typedef HANDLE HCONV;</code></p></td>
</tr>
<tr class="even">
<td><span id="HCONVLIST"></span><span id="hconvlist"></span><strong>HCONVLIST</strong></td>
<td><p>A handle to a DDE conversation list.</p>
<p>This type is declared in Ddeml.h as follows:</p>
<p><code>typedef HANDLE HCONVLIST;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HCURSOR"></span><span id="hcursor"></span><strong>HCURSOR</strong></td>
<td><p>A handle to a [cursor](https://msdn.microsoft.com/library/ms646970(v=VS.85).aspx).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HICON HCURSOR;</code></p></td>
</tr>
<tr class="even">
<td><span id="HDC"></span><span id="hdc"></span><strong>HDC</strong></td>
<td><p>A handle to a [device context](https://msdn.microsoft.com/library/windows/desktop/dd183560) (DC).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HDC;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HDDEDATA"></span><span id="hddedata"></span><strong>HDDEDATA</strong></td>
<td><p>A handle to DDE data.</p>
<p>This type is declared in Ddeml.h as follows:</p>
<p><code>typedef HANDLE HDDEDATA;</code></p></td>
</tr>
<tr class="even">
<td><span id="HDESK"></span><span id="hdesk"></span><strong>HDESK</strong></td>
<td><p>A handle to a [desktop](https://msdn.microsoft.com/library/windows/desktop/ms682573).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HDESK;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HDROP"></span><span id="hdrop"></span><strong>HDROP</strong></td>
<td><p>A handle to an internal drop structure.</p>
<p>This type is declared in ShellApi.h as follows:</p>
<p><code>typedef HANDLE HDROP;</code></p></td>
</tr>
<tr class="even">
<td><span id="HDWP"></span><span id="hdwp"></span><strong>HDWP</strong></td>
<td><p>A handle to a deferred window position structure.</p>
<p>This type is declared in WinUser.h as follows:</p>
<p><code>typedef HANDLE HDWP;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HENHMETAFILE"></span><span id="henhmetafile"></span><strong>HENHMETAFILE</strong></td>
<td><p>A handle to an [enhanced metafile](https://msdn.microsoft.com/library/windows/desktop/dd145051).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HENHMETAFILE;</code></p></td>
</tr>
<tr class="even">
<td><span id="HFILE"></span><span id="hfile"></span><strong>HFILE</strong></td>
<td><p>A handle to a file opened by [<strong>OpenFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa365430), not [<strong>CreateFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363858).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef int HFILE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HFONT"></span><span id="hfont"></span><strong>HFONT</strong></td>
<td><p>A handle to a [font](https://msdn.microsoft.com/library/windows/desktop/dd162470).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HFONT;</code></p></td>
</tr>
<tr class="even">
<td><span id="HGDIOBJ"></span><span id="hgdiobj"></span><strong>HGDIOBJ</strong></td>
<td><p>A handle to a GDI object.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HGDIOBJ;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HGLOBAL"></span><span id="hglobal"></span><strong>HGLOBAL</strong></td>
<td><p>A handle to a global memory block.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HGLOBAL;</code></p></td>
</tr>
<tr class="even">
<td><span id="HHOOK"></span><span id="hhook"></span><strong>HHOOK</strong></td>
<td><p>A handle to a [hook](https://msdn.microsoft.com/library/ms632589(v=VS.85).aspx).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HHOOK;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HICON"></span><span id="hicon"></span><strong>HICON</strong></td>
<td><p>A handle to an [icon](https://msdn.microsoft.com/library/ms646973(v=VS.85).aspx).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HICON;</code></p></td>
</tr>
<tr class="even">
<td><span id="HINSTANCE"></span><span id="hinstance"></span><strong>HINSTANCE</strong></td>
<td><p>A handle to an instance. This is the base address of the module in memory.</p>
<p><strong>HMODULE</strong> and <strong>HINSTANCE</strong> are the same today, but represented different things in 16-bit Windows.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HINSTANCE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HKEY"></span><span id="hkey"></span><strong>HKEY</strong></td>
<td><p>A handle to a registry key.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HKEY;</code></p></td>
</tr>
<tr class="even">
<td><span id="HKL"></span><span id="hkl"></span><strong>HKL</strong></td>
<td><p>An input locale identifier.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HKL;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HLOCAL"></span><span id="hlocal"></span><strong>HLOCAL</strong></td>
<td><p>A handle to a local memory block.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HLOCAL;</code></p></td>
</tr>
<tr class="even">
<td><span id="HMENU"></span><span id="hmenu"></span><strong>HMENU</strong></td>
<td><p>A handle to a [menu](https://msdn.microsoft.com/library/ms646977(v=VS.85).aspx).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HMENU;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HMETAFILE"></span><span id="hmetafile"></span><strong>HMETAFILE</strong></td>
<td><p>A handle to a [metafile](https://msdn.microsoft.com/library/windows/desktop/dd145051).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HMETAFILE;</code></p></td>
</tr>
<tr class="even">
<td><span id="HMODULE"></span><span id="hmodule"></span><strong>HMODULE</strong></td>
<td><p>A handle to a module. The is the base address of the module in memory.</p>
<p><strong>HMODULE</strong> and <strong>HINSTANCE</strong> are the same in current versions of Windows, but represented different things in 16-bit Windows.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HINSTANCE HMODULE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HMONITOR"></span><span id="hmonitor"></span><strong>HMONITOR</strong></td>
<td><p>A handle to a display monitor.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>if(WINVER &gt;= 0x0500) typedef HANDLE HMONITOR;</code></p></td>
</tr>
<tr class="even">
<td><span id="HPALETTE"></span><span id="hpalette"></span><strong>HPALETTE</strong></td>
<td><p>A handle to a palette.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HPALETTE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HPEN"></span><span id="hpen"></span><strong>HPEN</strong></td>
<td><p>A handle to a [pen](https://msdn.microsoft.com/library/windows/desktop/dd162786).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HPEN;</code></p></td>
</tr>
<tr class="even">
<td><span id="HRESULT"></span><span id="hresult"></span><strong>HRESULT</strong></td>
<td><p>The return codes used by COM interfaces. For more information, see [Structure of the COM Error Codes](https://msdn.microsoft.com/en-us/library/ms690088(v=VS.85).aspx). To test an <strong>HRESULT</strong> value, use the [<strong>FAILED</strong>](https://msdn.microsoft.com/en-us/library/ms693474(v=VS.85).aspx) and [<strong>SUCCEEDED</strong>](https://msdn.microsoft.com/en-us/library/ms687197(v=VS.85).aspx) macros.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef LONG HRESULT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HRGN"></span><span id="hrgn"></span><strong>HRGN</strong></td>
<td><p>A handle to a [region](https://msdn.microsoft.com/library/windows/desktop/dd162913).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HRGN;</code></p></td>
</tr>
<tr class="even">
<td><span id="HRSRC"></span><span id="hrsrc"></span><strong>HRSRC</strong></td>
<td><p>A handle to a resource.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HRSRC;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HSZ"></span><span id="hsz"></span><strong>HSZ</strong></td>
<td><p>A handle to a DDE string.</p>
<p>This type is declared in Ddeml.h as follows:</p>
<p><code>typedef HANDLE HSZ;</code></p></td>
</tr>
<tr class="even">
<td><span id="HWINSTA"></span><span id="hwinsta"></span><strong>HWINSTA</strong></td>
<td><p>A handle to a [window station](https://msdn.microsoft.com/library/windows/desktop/ms687096).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE WINSTA;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HWND"></span><span id="hwnd"></span><strong>HWND</strong></td>
<td><p>A handle to a [window](https://msdn.microsoft.com/library/ms632595(v=VS.85).aspx).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HWND;</code></p></td>
</tr>
<tr class="even">
<td><span id="INT"></span><span id="int"></span><strong>INT</strong></td>
<td><p>A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef int INT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="INT_PTR"></span><span id="int_ptr"></span><strong>INT_PTR</strong></td>
<td><p>A signed integer type for pointer precision. Use when casting a pointer to an integer to perform pointer arithmetic.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#if defined(_WIN64) 
 typedef __int64 INT_PTR; 
#else 
 typedef int INT_PTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><span id="INT8"></span><span id="int8"></span><strong>INT8</strong></td>
<td><p>An 8-bit signed integer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed char INT8;</code></p></td>
</tr>
<tr class="odd">
<td><span id="INT16"></span><span id="int16"></span><strong>INT16</strong></td>
<td><p>A 16-bit signed integer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed short INT16;</code></p></td>
</tr>
<tr class="even">
<td><span id="INT32"></span><span id="int32"></span><strong>INT32</strong></td>
<td><p>A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed int INT32;</code></p></td>
</tr>
<tr class="odd">
<td><span id="INT64"></span><span id="int64"></span><strong>INT64</strong></td>
<td><p>A 64-bit signed integer. The range is  9223372036854775808 through 9223372036854775807 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed __int64 INT64;</code></p></td>
</tr>
<tr class="even">
<td><span id="LANGID"></span><span id="langid"></span><strong>LANGID</strong></td>
<td><p>A language identifier. For more information, see [Language Identifiers](https://msdn.microsoft.com/library/windows/desktop/dd318691).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef WORD LANGID;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LCID"></span><span id="lcid"></span><strong>LCID</strong></td>
<td><p>A locale identifier. For more information, see [Locale Identifiers](https://msdn.microsoft.com/library/windows/desktop/dd373763).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef DWORD LCID;</code></p></td>
</tr>
<tr class="even">
<td><span id="LCTYPE"></span><span id="lctype"></span><strong>LCTYPE</strong></td>
<td><p>A locale information type. For a list, see [Locale Information Constants](https://msdn.microsoft.com/library/windows/desktop/dd464799).</p>
<p>This type is declared in WinNls.h as follows:</p>
<p><code>typedef DWORD LCTYPE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LGRPID"></span><span id="lgrpid"></span><strong>LGRPID</strong></td>
<td><p>A language group identifier. For a list, see [<strong>EnumLanguageGroupLocales</strong>](https://msdn.microsoft.com/library/windows/desktop/dd317819).</p>
<p>This type is declared in WinNls.h as follows:</p>
<p><code>typedef DWORD LGRPID;</code></p></td>
</tr>
<tr class="even">
<td><span id="LONG"></span><span id="long"></span><strong>LONG</strong></td>
<td><p>A 32-bit signed integer. The range is  2147483648 through 2147483647 decimal.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef long LONG;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LONGLONG"></span><span id="longlong"></span><strong>LONGLONG</strong></td>
<td><p>A 64-bit signed integer. The range is  9223372036854775808 through 9223372036854775807 decimal.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#if !defined(_M_IX86)
 typedef __int64 LONGLONG; 
#else
 typedef double LONGLONG;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><span id="LONG_PTR"></span><span id="long_ptr"></span><strong>LONG_PTR</strong></td>
<td><p>A signed long type for pointer precision. Use when casting a pointer to a long to perform pointer arithmetic.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#if defined(_WIN64)
 typedef __int64 LONG_PTR; 
#else
 typedef long LONG_PTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="LONG32"></span><span id="long32"></span><strong>LONG32</strong></td>
<td><p>A 32-bit signed integer. The range is  2147483648 through 2147483647 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed int LONG32;</code></p></td>
</tr>
<tr class="even">
<td><span id="LONG64"></span><span id="long64"></span><strong>LONG64</strong></td>
<td><p>A 64-bit signed integer. The range is  9223372036854775808 through 9223372036854775807 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef __int64 LONG64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPARAM"></span><span id="lparam"></span><strong>LPARAM</strong></td>
<td><p>A message parameter.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef LONG_PTR LPARAM;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPBOOL"></span><span id="lpbool"></span><strong>LPBOOL</strong></td>
<td><p>A pointer to a [<strong>BOOL</strong>](#bool).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef BOOL far *LPBOOL;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPBYTE"></span><span id="lpbyte"></span><strong>LPBYTE</strong></td>
<td><p>A pointer to a [<strong>BYTE</strong>](#byte).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef BYTE far *LPBYTE;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPCOLORREF"></span><span id="lpcolorref"></span><strong>LPCOLORREF</strong></td>
<td><p>A pointer to a [<strong>COLORREF</strong>](https://msdn.microsoft.com/library/windows/desktop/dd183449) value.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef DWORD *LPCOLORREF;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPCSTR"></span><span id="lpcstr"></span><strong>LPCSTR</strong></td>
<td><p>A pointer to a constant null-terminated string of 8-bit Windows (ANSI) characters. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef __nullterminated CONST CHAR *LPCSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPCTSTR"></span><span id="lpctstr"></span><strong>LPCTSTR</strong></td>
<td><p>An [<strong>LPCWSTR</strong>](#lpcwstr) if <strong>UNICODE</strong> is defined, an [<strong>LPCSTR</strong>](#lpcstr) otherwise. For more information, see [Windows Data Types for Strings](https://msdn.microsoft.com/library/windows/desktop/dd374131).</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef UNICODE
 typedef LPCWSTR LPCTSTR; 
#else
 typedef LPCSTR LPCTSTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="LPCVOID"></span><span id="lpcvoid"></span><strong>LPCVOID</strong></td>
<td><p>A pointer to a constant of any type.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef CONST void *LPCVOID;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPCWSTR"></span><span id="lpcwstr"></span><strong>LPCWSTR</strong></td>
<td><p>A pointer to a constant null-terminated string of 16-bit Unicode characters. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CONST WCHAR *LPCWSTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPDWORD"></span><span id="lpdword"></span><strong>LPDWORD</strong></td>
<td><p>A pointer to a [<strong>DWORD</strong>](#dword).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef DWORD *LPDWORD;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPHANDLE"></span><span id="lphandle"></span><strong>LPHANDLE</strong></td>
<td><p>A pointer to a [<strong>HANDLE</strong>](#handle).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE *LPHANDLE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPINT"></span><span id="lpint"></span><strong>LPINT</strong></td>
<td><p>A pointer to an [<strong>INT</strong>](#int).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef int *LPINT;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPLONG"></span><span id="lplong"></span><strong>LPLONG</strong></td>
<td><p>A pointer to a [<strong>LONG</strong>](#long).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef long *LPLONG;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPSTR"></span><span id="lpstr"></span><strong>LPSTR</strong></td>
<td><p>A pointer to a null-terminated string of 8-bit Windows (ANSI) characters. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CHAR *LPSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPTSTR"></span><span id="lptstr"></span><strong>LPTSTR</strong></td>
<td><p>An [<strong>LPWSTR</strong>](#lpwstr) if <strong>UNICODE</strong> is defined, an [<strong>LPSTR</strong>](#lpstr) otherwise. For more information, see [Windows Data Types for Strings](https://msdn.microsoft.com/library/windows/desktop/dd374131).</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef UNICODE
 typedef LPWSTR LPTSTR;
#else
 typedef LPSTR LPTSTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="LPVOID"></span><span id="lpvoid"></span><strong>LPVOID</strong></td>
<td><p>A pointer to any type.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef void *LPVOID;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPWORD"></span><span id="lpword"></span><strong>LPWORD</strong></td>
<td><p>A pointer to a [<strong>WORD</strong>](#word).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef WORD *LPWORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPWSTR"></span><span id="lpwstr"></span><strong>LPWSTR</strong></td>
<td><p>A pointer to a null-terminated string of 16-bit Unicode characters. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef WCHAR *LPWSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="LRESULT"></span><span id="lresult"></span><strong>LRESULT</strong></td>
<td><p>Signed result of message processing.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef LONG_PTR LRESULT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PBOOL"></span><span id="pbool"></span><strong>PBOOL</strong></td>
<td><p>A pointer to a [<strong>BOOL</strong>](#bool).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef BOOL *PBOOL;</code></p></td>
</tr>
<tr class="even">
<td><span id="PBOOLEAN"></span><span id="pboolean"></span><strong>PBOOLEAN</strong></td>
<td><p>A pointer to a [<strong>BOOLEAN</strong>](#boolean).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef BOOLEAN *PBOOLEAN;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PBYTE"></span><span id="pbyte"></span><strong>PBYTE</strong></td>
<td><p>A pointer to a [<strong>BYTE</strong>](#byte).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef BYTE *PBYTE;</code></p></td>
</tr>
<tr class="even">
<td><span id="PCHAR"></span><span id="pchar"></span><strong>PCHAR</strong></td>
<td><p>A pointer to a [<strong>CHAR</strong>](#char).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CHAR *PCHAR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PCSTR"></span><span id="pcstr"></span><strong>PCSTR</strong></td>
<td><p>A pointer to a constant null-terminated string of 8-bit Windows (ANSI) characters. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CONST CHAR *PCSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="PCTSTR"></span><span id="pctstr"></span><strong>PCTSTR</strong></td>
<td><p>A [<strong>PCWSTR</strong>](#pcwstr) if <strong>UNICODE</strong> is defined, a [<strong>PCSTR</strong>](#pcstr) otherwise. For more information, see [Windows Data Types for Strings](https://msdn.microsoft.com/library/windows/desktop/dd374131).</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef UNICODE
 typedef LPCWSTR PCTSTR;
#else
 typedef LPCSTR PCTSTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="PCWSTR"></span><span id="pcwstr"></span><strong>PCWSTR</strong></td>
<td><p>A pointer to a constant null-terminated string of 16-bit Unicode characters. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CONST WCHAR *PCWSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="PDWORD"></span><span id="pdword"></span><strong>PDWORD</strong></td>
<td><p>A pointer to a [<strong>DWORD</strong>](#dword).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef DWORD *PDWORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PDWORDLONG"></span><span id="pdwordlong"></span><strong>PDWORDLONG</strong></td>
<td><p>A pointer to a [<strong>DWORDLONG</strong>](#dwordlong).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef DWORDLONG *PDWORDLONG;</code></p></td>
</tr>
<tr class="even">
<td><span id="PDWORD_PTR"></span><span id="pdword_ptr"></span><strong>PDWORD_PTR</strong></td>
<td><p>A pointer to a [<strong>DWORD_PTR</strong>](#dword-ptr).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef DWORD_PTR *PDWORD_PTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PDWORD32"></span><span id="pdword32"></span><strong>PDWORD32</strong></td>
<td><p>A pointer to a [<strong>DWORD32</strong>](#dword32).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef DWORD32 *PDWORD32;</code></p></td>
</tr>
<tr class="even">
<td><span id="PDWORD64"></span><span id="pdword64"></span><strong>PDWORD64</strong></td>
<td><p>A pointer to a [<strong>DWORD64</strong>](#dword64).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef DWORD64 *PDWORD64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PFLOAT"></span><span id="pfloat"></span><strong>PFLOAT</strong></td>
<td><p>A pointer to a [<strong>FLOAT</strong>](#float).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef FLOAT *PFLOAT;</code></p></td>
</tr>
<tr class="even">
<td><span id="PHALF_PTR"></span><span id="phalf_ptr"></span><strong>PHALF_PTR</strong></td>
<td><p>A pointer to a [<strong>HALF_PTR</strong>](#half-ptr).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef _WIN64
 typedef HALF_PTR *PHALF_PTR;
#else
 typedef HALF_PTR *PHALF_PTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="PHANDLE"></span><span id="phandle"></span><strong>PHANDLE</strong></td>
<td><p>A pointer to a [<strong>HANDLE</strong>](#handle).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef HANDLE *PHANDLE;</code></p></td>
</tr>
<tr class="even">
<td><span id="PHKEY"></span><span id="phkey"></span><strong>PHKEY</strong></td>
<td><p>A pointer to an [<strong>HKEY</strong>](#hkey).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HKEY *PHKEY;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PINT"></span><span id="pint"></span><strong>PINT</strong></td>
<td><p>A pointer to an [<strong>INT</strong>](#int).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef int *PINT;</code></p></td>
</tr>
<tr class="even">
<td><span id="PINT_PTR"></span><span id="pint_ptr"></span><strong>PINT_PTR</strong></td>
<td><p>A pointer to an [<strong>INT_PTR</strong>](#int-ptr).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT_PTR *PINT_PTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PINT8"></span><span id="pint8"></span><strong>PINT8</strong></td>
<td><p>A pointer to an [<strong>INT8</strong>](#int8).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT8 *PINT8;</code></p></td>
</tr>
<tr class="even">
<td><span id="PINT16"></span><span id="pint16"></span><strong>PINT16</strong></td>
<td><p>A pointer to an [<strong>INT16</strong>](#int16).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT16 *PINT16;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PINT32"></span><span id="pint32"></span><strong>PINT32</strong></td>
<td><p>A pointer to an [<strong>INT32</strong>](#int32).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT32 *PINT32;</code></p></td>
</tr>
<tr class="even">
<td><span id="PINT64"></span><span id="pint64"></span><strong>PINT64</strong></td>
<td><p>A pointer to an [<strong>INT64</strong>](#int64).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT64 *PINT64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PLCID"></span><span id="plcid"></span><strong>PLCID</strong></td>
<td><p>A pointer to an [<strong>LCID</strong>](#lcid).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef PDWORD PLCID;</code></p></td>
</tr>
<tr class="even">
<td><span id="PLONG"></span><span id="plong"></span><strong>PLONG</strong></td>
<td><p>A pointer to a [<strong>LONG</strong>](#long).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef LONG *PLONG;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PLONGLONG"></span><span id="plonglong"></span><strong>PLONGLONG</strong></td>
<td><p>A pointer to a [<strong>LONGLONG</strong>](#longlong).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef LONGLONG *PLONGLONG;</code></p></td>
</tr>
<tr class="even">
<td><span id="PLONG_PTR"></span><span id="plong_ptr"></span><strong>PLONG_PTR</strong></td>
<td><p>A pointer to a [<strong>LONG_PTR</strong>](#long-ptr).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef LONG_PTR *PLONG_PTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PLONG32"></span><span id="plong32"></span><strong>PLONG32</strong></td>
<td><p>A pointer to a [<strong>LONG32</strong>](#long32).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef LONG32 *PLONG32;</code></p></td>
</tr>
<tr class="even">
<td><span id="PLONG64"></span><span id="plong64"></span><strong>PLONG64</strong></td>
<td><p>A pointer to a [<strong>LONG64</strong>](#long64).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef LONG64 *PLONG64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="POINTER_32"></span><span id="pointer_32"></span><strong>POINTER_32</strong></td>
<td><p>A 32-bit pointer. On a 32-bit system, this is a native pointer. On a 64-bit system, this is a truncated 64-bit pointer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#if defined(_WIN64)
#define POINTER_32 __ptr32
#else
#define POINTER_32
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><span id="POINTER_64"></span><span id="pointer_64"></span><strong>POINTER_64</strong></td>
<td><p>A 64-bit pointer. On a 64-bit system, this is a native pointer. On a 32-bit system, this is a sign-extended 32-bit pointer.</p>
<p>Note that it is not safe to assume the state of the high pointer bit.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#if (_MSC_VER &gt;= 1300)
#define POINTER_64 __ptr64
#else
#define POINTER_64
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="POINTER_SIGNED"></span><span id="pointer_signed"></span><strong>POINTER_SIGNED</strong></td>
<td><p>A signed pointer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>#define POINTER_SIGNED __sptr</code></p></td>
</tr>
<tr class="even">
<td><span id="POINTER_UNSIGNED"></span><span id="pointer_unsigned"></span><strong>POINTER_UNSIGNED</strong></td>
<td><p>An unsigned pointer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>#define POINTER_UNSIGNED __uptr</code></p></td>
</tr>
<tr class="odd">
<td><span id="PSHORT"></span><span id="pshort"></span><strong>PSHORT</strong></td>
<td><p>A pointer to a [<strong>SHORT</strong>](#short).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef SHORT *PSHORT;</code></p></td>
</tr>
<tr class="even">
<td><span id="PSIZE_T"></span><span id="psize_t"></span><strong>PSIZE_T</strong></td>
<td><p>A pointer to a [<strong>SIZE_T</strong>](#size-t).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef SIZE_T *PSIZE_T;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PSSIZE_T"></span><span id="pssize_t"></span><strong>PSSIZE_T</strong></td>
<td><p>A pointer to a [<strong>SSIZE_T</strong>](#ssize-t).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef SSIZE_T *PSSIZE_T;</code></p></td>
</tr>
<tr class="even">
<td><span id="PSTR"></span><span id="pstr"></span><strong>PSTR</strong></td>
<td><p>A pointer to a null-terminated string of 8-bit Windows (ANSI) characters. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CHAR *PSTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PTBYTE"></span><span id="ptbyte"></span><strong>PTBYTE</strong></td>
<td><p>A pointer to a [<strong>TBYTE</strong>](#tbyte).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef TBYTE *PTBYTE;</code></p></td>
</tr>
<tr class="even">
<td><span id="PTCHAR"></span><span id="ptchar"></span><strong>PTCHAR</strong></td>
<td><p>A pointer to a [<strong>TCHAR</strong>](#tchar).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef TCHAR *PTCHAR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PTSTR"></span><span id="ptstr"></span><strong>PTSTR</strong></td>
<td><p>A [<strong>PWSTR</strong>](#pwstr) if <strong>UNICODE</strong> is defined, a [<strong>PSTR</strong>](#pstr) otherwise. For more information, see [Windows Data Types for Strings](https://msdn.microsoft.com/library/windows/desktop/dd374131).</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef UNICODE
 typedef LPWSTR PTSTR;
#else typedef LPSTR PTSTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><span id="PUCHAR"></span><span id="puchar"></span><strong>PUCHAR</strong></td>
<td><p>A pointer to a [<strong>UCHAR</strong>](#uchar).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef UCHAR *PUCHAR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUHALF_PTR"></span><span id="puhalf_ptr"></span><strong>PUHALF_PTR</strong></td>
<td><p>A pointer to a [<strong>UHALF_PTR</strong>](#uhalf-ptr).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef _WIN64
 typedef UHALF_PTR *PUHALF_PTR;
#else
 typedef UHALF_PTR *PUHALF_PTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><span id="PUINT"></span><span id="puint"></span><strong>PUINT</strong></td>
<td><p>A pointer to a [<strong>UINT</strong>](#uint).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef UINT *PUINT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUINT_PTR"></span><span id="puint_ptr"></span><strong>PUINT_PTR</strong></td>
<td><p>A pointer to a [<strong>UINT_PTR</strong>](#uint-ptr).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT_PTR *PUINT_PTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="PUINT8"></span><span id="puint8"></span><strong>PUINT8</strong></td>
<td><p>A pointer to a [<strong>UINT8</strong>](#uint8).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT8 *PUINT8;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUINT16"></span><span id="puint16"></span><strong>PUINT16</strong></td>
<td><p>A pointer to a [<strong>UINT16</strong>](#uint16).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT16 *PUINT16;</code></p></td>
</tr>
<tr class="even">
<td><span id="PUINT32"></span><span id="puint32"></span><strong>PUINT32</strong></td>
<td><p>A pointer to a [<strong>UINT32</strong>](#uint32).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT32 *PUINT32;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUINT64"></span><span id="puint64"></span><strong>PUINT64</strong></td>
<td><p>A pointer to a [<strong>UINT64</strong>](#uint64).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT64 *PUINT64;</code></p></td>
</tr>
<tr class="even">
<td><span id="PULONG"></span><span id="pulong"></span><strong>PULONG</strong></td>
<td><p>A pointer to a [<strong>ULONG</strong>](#ulong).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef ULONG *PULONG;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PULONGLONG"></span><span id="pulonglong"></span><strong>PULONGLONG</strong></td>
<td><p>A pointer to a [<strong>ULONGLONG</strong>](#ulonglong).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef ULONGLONG *PULONGLONG;</code></p></td>
</tr>
<tr class="even">
<td><span id="PULONG_PTR"></span><span id="pulong_ptr"></span><strong>PULONG_PTR</strong></td>
<td><p>A pointer to a [<strong>ULONG_PTR</strong>](#ulong-ptr).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef ULONG_PTR *PULONG_PTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PULONG32"></span><span id="pulong32"></span><strong>PULONG32</strong></td>
<td><p>A pointer to a [<strong>ULONG32</strong>](#ulong32).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef ULONG32 *PULONG32;</code></p></td>
</tr>
<tr class="even">
<td><span id="PULONG64"></span><span id="pulong64"></span><strong>PULONG64</strong></td>
<td><p>A pointer to a [<strong>ULONG64</strong>](#ulong64).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef ULONG64 *PULONG64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUSHORT"></span><span id="pushort"></span><strong>PUSHORT</strong></td>
<td><p>A pointer to a [<strong>USHORT</strong>](#ushort).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef USHORT *PUSHORT;</code></p></td>
</tr>
<tr class="even">
<td><span id="PVOID"></span><span id="pvoid"></span><strong>PVOID</strong></td>
<td><p>A pointer to any type.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef void *PVOID;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PWCHAR"></span><span id="pwchar"></span><strong>PWCHAR</strong></td>
<td><p>A pointer to a [<strong>WCHAR</strong>](#wchar).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef WCHAR *PWCHAR;</code></p></td>
</tr>
<tr class="even">
<td><span id="PWORD"></span><span id="pword"></span><strong>PWORD</strong></td>
<td><p>A pointer to a [<strong>WORD</strong>](#word).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef WORD *PWORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PWSTR"></span><span id="pwstr"></span><strong>PWSTR</strong></td>
<td><p>A pointer to a null-terminated string of 16-bit Unicode characters. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef WCHAR *PWSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="QWORD"></span><span id="qword"></span><strong>QWORD</strong></td>
<td><p>A 64-bit unsigned integer.</p>
<p>This type is declared as follows:</p>
<p><code>typedef unsigned __int64 QWORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="SC_HANDLE"></span><span id="sc_handle"></span><strong>SC_HANDLE</strong></td>
<td><p>A handle to a service control manager database. For more information, see [SCM Handles](https://msdn.microsoft.com/library/windows/desktop/ms685104).</p>
<p>This type is declared in WinSvc.h as follows:</p>
<p><code>typedef HANDLE SC_HANDLE;</code></p></td>
</tr>
<tr class="even">
<td><span id="SC_LOCK"></span><span id="sc_lock"></span><strong>SC_LOCK</strong></td>
<td><p>A lock to a service control manager database. For more information, see [SCM Handles](https://msdn.microsoft.com/library/windows/desktop/ms685104).</p>
<p>This type is declared in WinSvc.h as follows:</p>
<p><code>typedef LPVOID SC_LOCK;</code></p></td>
</tr>
<tr class="odd">
<td><span id="SERVICE_STATUS_HANDLE"></span><span id="service_status_handle"></span><strong>SERVICE_STATUS_HANDLE</strong></td>
<td><p>A handle to a service status value. For more information, see [SCM Handles](https://msdn.microsoft.com/library/windows/desktop/ms685104).</p>
<p>This type is declared in WinSvc.h as follows:</p>
<p><code>typedef HANDLE SERVICE_STATUS_HANDLE;</code></p></td>
</tr>
<tr class="even">
<td><span id="SHORT"></span><span id="short"></span><strong>SHORT</strong></td>
<td><p>A 16-bit integer. The range is  32768 through 32767 decimal.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef short SHORT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="SIZE_T"></span><span id="size_t"></span><strong>SIZE_T</strong></td>
<td><p>The maximum number of bytes to which a pointer can point. Use for a count that must span the full range of a pointer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef ULONG_PTR SIZE_T;</code></p></td>
</tr>
<tr class="even">
<td><span id="SSIZE_T"></span><span id="ssize_t"></span><strong>SSIZE_T</strong></td>
<td><p>A signed version of [<strong>SIZE_T</strong>](#size-t).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef LONG_PTR SSIZE_T;</code></p></td>
</tr>
<tr class="odd">
<td><span id="TBYTE"></span><span id="tbyte"></span><strong>TBYTE</strong></td>
<td><p>A [<strong>WCHAR</strong>](#wchar) if <strong>UNICODE</strong> is defined, a [<strong>CHAR</strong>](#char) otherwise.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef UNICODE
 typedef WCHAR TBYTE;
#else
 typedef unsigned char TBYTE;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><span id="TCHAR"></span><span id="tchar"></span><strong>TCHAR</strong></td>
<td><p>A [<strong>WCHAR</strong>](#wchar) if <strong>UNICODE</strong> is defined, a [<strong>CHAR</strong>](#char) otherwise.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef UNICODE
 typedef WCHAR TCHAR;
#else
 typedef char TCHAR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="UCHAR"></span><span id="uchar"></span><strong>UCHAR</strong></td>
<td><p>An unsigned [<strong>CHAR</strong>](#char).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned char UCHAR;</code></p></td>
</tr>
<tr class="even">
<td><span id="UHALF_PTR"></span><span id="uhalf_ptr"></span><strong>UHALF_PTR</strong></td>
<td><p>An unsigned [<strong>HALF_PTR</strong>](#half-ptr). Use within a structure that contains a pointer and two small fields.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#ifdef _WIN64
 typedef unsigned int UHALF_PTR;
#else
 typedef unsigned short UHALF_PTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="UINT"></span><span id="uint"></span><strong>UINT</strong></td>
<td><p>An unsigned [<strong>INT</strong>](#int). The range is 0 through 4294967295 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned int UINT;</code></p></td>
</tr>
<tr class="even">
<td><span id="UINT_PTR"></span><span id="uint_ptr"></span><strong>UINT_PTR</strong></td>
<td><p>An unsigned [<strong>INT_PTR</strong>](#int-ptr).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#if defined(_WIN64)
 typedef unsigned __int64 UINT_PTR;
#else
 typedef unsigned int UINT_PTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="UINT8"></span><span id="uint8"></span><strong>UINT8</strong></td>
<td><p>An unsigned [<strong>INT8</strong>](#int8).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned  char UINT8;</code></p></td>
</tr>
<tr class="even">
<td><span id="UINT16"></span><span id="uint16"></span><strong>UINT16</strong></td>
<td><p>An unsigned [<strong>INT16</strong>](#int16).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned  short UINT16;</code></p></td>
</tr>
<tr class="odd">
<td><span id="UINT32"></span><span id="uint32"></span><strong>UINT32</strong></td>
<td><p>An unsigned [<strong>INT32</strong>](#int32). The range is 0 through 4294967295 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned int UINT32;</code></p></td>
</tr>
<tr class="even">
<td><span id="UINT64"></span><span id="uint64"></span><strong>UINT64</strong></td>
<td><p>An unsigned [<strong>INT64</strong>](#int64). The range is 0 through 18446744073709551615 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef usigned __int 64 UINT64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="ULONG"></span><span id="ulong"></span><strong>ULONG</strong></td>
<td><p>An unsigned [<strong>LONG</strong>](#long). The range is 0 through 4294967295 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned long ULONG;</code></p></td>
</tr>
<tr class="even">
<td><span id="ULONGLONG"></span><span id="ulonglong"></span><strong>ULONGLONG</strong></td>
<td><p>A 64-bit unsigned integer. The range is 0 through 18446744073709551615 decimal.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#if !defined(_M_IX86)
 typedef unsigned __int64 ULONGLONG;
#else
 typedef double ULONGLONG;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="ULONG_PTR"></span><span id="ulong_ptr"></span><strong>ULONG_PTR</strong></td>
<td><p>An unsigned [<strong>LONG_PTR</strong>](#long-ptr).</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#if defined(_WIN64)
 typedef unsigned __int64 ULONG_PTR;
#else
 typedef unsigned long ULONG_PTR;
#endif</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><span id="ULONG32"></span><span id="ulong32"></span><strong>ULONG32</strong></td>
<td><p>An unsigned [<strong>LONG32</strong>](#long32). The range is 0 through 4294967295 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned int ULONG32;</code></p></td>
</tr>
<tr class="odd">
<td><span id="ULONG64"></span><span id="ulong64"></span><strong>ULONG64</strong></td>
<td><p>An unsigned [<strong>LONG64</strong>](#long64). The range is 0 through 18446744073709551615 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned __int64 ULONG64;</code></p></td>
</tr>
<tr class="even">
<td><span id="UNICODE_STRING"></span><span id="unicode_string"></span><strong>UNICODE_STRING</strong></td>
<td><p>A Unicode string.</p>
<p>This type is declared in Winternl.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _UNICODE_STRING {
  USHORT  Length;
  USHORT  MaximumLength;
  PWSTR  Buffer;
} UNICODE_STRING;
typedef UNICODE_STRING *PUNICODE_STRING;
typedef const UNICODE_STRING *PCUNICODE_STRING;</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><span id="USHORT"></span><span id="ushort"></span><strong>USHORT</strong></td>
<td><p>An unsigned [<strong>SHORT</strong>](#short). The range is 0 through 65535 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned short USHORT;</code></p></td>
</tr>
<tr class="even">
<td><span id="USN"></span><span id="usn"></span><strong>USN</strong></td>
<td><p>An update sequence number (USN).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef LONGLONG USN;</code></p></td>
</tr>
<tr class="odd">
<td><span id="VOID"></span><span id="void"></span><strong>VOID</strong></td>
<td><p>Any type.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>#define VOID void</code></p></td>
</tr>
<tr class="even">
<td><span id="WCHAR"></span><span id="wchar"></span><strong>WCHAR</strong></td>
<td><p>A 16-bit Unicode character. For more information, see [Character Sets Used By Fonts](https://msdn.microsoft.com/library/windows/desktop/dd183415).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef wchar_t WCHAR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="WINAPI"></span><span id="winapi"></span><strong>WINAPI</strong></td>
<td><p>The calling convention for system functions.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>#define WINAPI __stdcall</code></p>
<p><strong>CALLBACK</strong>, <strong>WINAPI</strong>, and <strong>APIENTRY</strong> are all used to define functions with the __stdcall calling convention. Most functions in the Windows API are declared using <strong>WINAPI</strong>. You may wish to use <strong>CALLBACK</strong> for the callback functions that you implement to help identify the function as a callback function.</p></td>
</tr>
<tr class="even">
<td><span id="WORD"></span><span id="word"></span><strong>WORD</strong></td>
<td><p>A 16-bit unsigned integer. The range is 0 through 65535 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned short WORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="WPARAM"></span><span id="wparam"></span><strong>WPARAM</strong></td>
<td><p>A message parameter.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef UINT_PTR WPARAM;</code></p></td>
</tr>
</tbody>
</table>



## Requirements



|                                     |                                                                                                                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                |
| Header<br/>                   | <dl> <dt>BaseTsd.h; </dt> <dt>WinDef.h; </dt> <dt>WinNT.h</dt> </dl> |



 

 





