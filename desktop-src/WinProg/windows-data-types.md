---
title: Windows Data Types (BaseTsd.h)
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
ms.topic: reference
ms.date: 11/07/2024
---

# Windows Data Types

The data types supported by Windows are used to define function return values, function and message parameters, and structure members. They define the size and meaning of these elements. For more information about the underlying C/C++ data types, see [Data Type Ranges](/cpp/cpp/data-type-ranges).

The following table contains the following types: character, integer, Boolean, pointer, and handle. The character, integer, and Boolean types are common to most C compilers. Most of the pointer-type names begin with a prefix of P or LP. Handles refer to a resource that has been loaded into memory.

For more information about handling 64-bit integers, see [Large Integers](large-integers.md).



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Data type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="APIENTRY"></span><span id="apientry"></span><code>APIENTRY</code></td>
<td>The calling convention for system functions.<br/> This type is declared in WinDef.h as follows:<br/> <code>#define APIENTRY WINAPI</code><br/></td>
</tr>
<tr class="even">
<td><span id="ATOM"></span><span id="atom"></span><code>ATOM</code></td>
<td>An atom. For more information, see <a href="/windows/desktop/dataxchg/about-atom-tables">About Atom Tables</a>.<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef WORD ATOM;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="BOOL"></span><span id="bool"></span><code>BOOL</code></td>
<td>A Boolean variable (should be <strong>TRUE</strong> or <strong>FALSE</strong>).<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef int BOOL;</code><br/></td>
</tr>
<tr class="even">
<td><span id="BOOLEAN"></span><span id="boolean"></span><code>BOOLEAN</code></td>
<td>A Boolean variable (should be <strong>TRUE</strong> or <strong>FALSE</strong>).<br/> This type is declared in WinNT.h as follows:<br/> <code>typedef BYTE BOOLEAN;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="BYTE"></span><span id="byte"></span><code>BYTE</code></td>
<td>A byte (8 bits).<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef unsigned char BYTE;</code><br/></td>
</tr>
<tr class="even">
<td><span id="CALLBACK"></span><span id="callback"></span><code>CALLBACK</code></td>
<td>The calling convention for callback functions.<br/> This type is declared in WinDef.h as follows:<br/> <code>#define CALLBACK __stdcall</code><br/> <strong>CALLBACK</strong>, <strong>WINAPI</strong>, and <strong>APIENTRY</strong> are all used to define functions with the __stdcall calling convention. Most functions in the Windows API are declared using <strong>WINAPI</strong>. You may wish to use <strong>CALLBACK</strong> for the callback functions that you implement to help identify the function as a callback function.<br/></td>
</tr>
<tr class="odd">
<td><span id="CCHAR"></span><span id="cchar"></span><code>CCHAR</code></td>
<td>An 8-bit Windows (ANSI) character.<br/> This type is declared in WinNT.h as follows:<br/> <code>typedef char CCHAR;</code><br/></td>
</tr>
<tr class="even">
<td><span id="CHAR"></span><span id="char"></span><code>CHAR</code></td>
<td>An 8-bit Windows (ANSI) character. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.<br/> This type is declared in WinNT.h as follows:<br/> <code>typedef char CHAR;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="COLORREF"></span><span id="colorref"></span><code>COLORREF</code></td>
<td>The red, green, blue (RGB) color value (32 bits). See <a href="/windows/desktop/gdi/colorref"><strong>COLORREF</strong></a> for information on this type.<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef DWORD COLORREF;</code><br/></td>
</tr>
<tr class="even">
<td><span id="CONST"></span><span id="const"></span><code>CONST</code></td>
<td>A variable whose value is to remain constant during execution. <br/> This type is declared in WinDef.h as follows:<br/> <code>#define CONST const</code><br/></td>
</tr>
<tr class="odd">
<td><span id="DWORD"></span><span id="dword"></span><code>DWORD</code></td>
<td>A 32-bit unsigned integer. The range is 0 through 4294967295 decimal.<br/> This type is declared in IntSafe.h as follows:<br/> <code>typedef unsigned long DWORD;</code><br/></td>
</tr>
<tr class="even">
<td><span id="DWORDLONG"></span><span id="dwordlong"></span><code>DWORDLONG</code></td>
<td>A 64-bit unsigned integer. The range is 0 through 18446744073709551615 decimal.<br/> This type is declared in IntSafe.h as follows:<br/> <code>typedef unsigned __int64 DWORDLONG;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="DWORD_PTR"></span><span id="dword_ptr"></span><code>DWORD_PTR</code></td>
<td>An unsigned long type for pointer precision. Use when casting a pointer to a long type to perform pointer arithmetic. (Also commonly used for general 32-bit parameters that have been extended to 64 bits in 64-bit Windows.)<br/> This type is declared in BaseTsd.h as follows:<br/> <code>typedef ULONG_PTR DWORD_PTR;</code><br/></td>
</tr>
<tr class="even">
<td><span id="DWORD32"></span><span id="dword32"></span><code>DWORD32</code></td>
<td>A 32-bit unsigned integer.<br/> This type is declared in BaseTsd.h as follows:<br/> <code>typedef unsigned int DWORD32;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="DWORD64"></span><span id="dword64"></span><code>DWORD64</code></td>
<td>A 64-bit unsigned integer.<br/> This type is declared in BaseTsd.h as follows:<br/> <code>typedef unsigned __int64 DWORD64;</code><br/></td>
</tr>
<tr class="even">
<td><span id="FLOAT"></span><span id="float"></span><code>FLOAT</code></td>
<td>A floating-point variable.<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef float FLOAT;</code><br/></td>
</tr>
<tr class="odd">
<td><span id="HACCEL"></span><span id="haccel"></span><code>HACCEL</code></td>
<td>A handle to an <a href="/windows/desktop/menurc/keyboard-accelerators">accelerator table</a>.<br/> This type is declared in WinDef.h as follows:<br/> <code>typedef HANDLE HACCEL;</code><br/></td>
</tr>
<tr class="even">
<td><span id="HALF_PTR"></span><span id="half_ptr"></span><code>HALF_PTR</code></td>
<td>Half the size of a pointer. Use within a structure that contains a pointer and two small fields.<br/> This type is declared in BaseTsd.h as follows:<br/> <span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="HANDLE"></span><span id="handle"></span><code>HANDLE</code></td>
<td><p>A handle to an object.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef PVOID HANDLE;</code></p></td>
</tr>
<tr class="even">
<td><span id="HBITMAP"></span><span id="hbitmap"></span><code>HBITMAP</code></td>
<td><p>A handle to a <a href="/windows/desktop/gdi/bitmaps">bitmap</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HBITMAP;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HBRUSH"></span><span id="hbrush"></span><code>HBRUSH</code></td>
<td><p>A handle to a <a href="/windows/desktop/gdi/brushes">brush</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HBRUSH;</code></p></td>
</tr>
<tr class="even">
<td><span id="HCOLORSPACE"></span><span id="hcolorspace"></span><code>HCOLORSPACE</code></td>
<td><p>A handle to a <a href="/previous-versions//dd316799(v=vs.85)">color space</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HCOLORSPACE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HCONV"></span><span id="hconv"></span><code>HCONV</code></td>
<td><p>A handle to a dynamic data exchange (DDE) conversation.</p>
<p>This type is declared in Ddeml.h as follows:</p>
<p><code>typedef HANDLE HCONV;</code></p></td>
</tr>
<tr class="even">
<td><span id="HCONVLIST"></span><span id="hconvlist"></span><code>HCONVLIST</code></td>
<td><p>A handle to a DDE conversation list.</p>
<p>This type is declared in Ddeml.h as follows:</p>
<p><code>typedef HANDLE HCONVLIST;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HCURSOR"></span><span id="hcursor"></span><code>HCURSOR</code></td>
<td><p>A handle to a <a href="/windows/desktop/menurc/cursors">cursor</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HICON HCURSOR;</code></p></td>
</tr>
<tr class="even">
<td><span id="HDC"></span><span id="hdc"></span><code>HDC</code></td>
<td><p>A handle to a <a href="/windows/desktop/gdi/device-context-types">device context</a> (DC).</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HDC;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HDDEDATA"></span><span id="hddedata"></span><code>HDDEDATA</code></td>
<td><p>A handle to DDE data.</p>
<p>This type is declared in Ddeml.h as follows:</p>
<p><code>typedef HANDLE HDDEDATA;</code></p></td>
</tr>
<tr class="even">
<td><span id="HDESK"></span><span id="hdesk"></span><code>HDESK</code></td>
<td><p>A handle to a <a href="/windows/desktop/winstation/desktops">desktop</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HDESK;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HDROP"></span><span id="hdrop"></span><code>HDROP</code></td>
<td><p>A handle to an internal drop structure.</p>
<p>This type is declared in ShellApi.h as follows:</p>
<p><code>typedef HANDLE HDROP;</code></p></td>
</tr>
<tr class="even">
<td><span id="HDWP"></span><span id="hdwp"></span><code>HDWP</code></td>
<td><p>A handle to a deferred window position structure.</p>
<p>This type is declared in WinUser.h as follows:</p>
<p><code>typedef HANDLE HDWP;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HENHMETAFILE"></span><span id="henhmetafile"></span><code>HENHMETAFILE</code></td>
<td><p>A handle to an <a href="/windows/desktop/gdi/metafiles">enhanced metafile</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HENHMETAFILE;</code></p></td>
</tr>
<tr class="even">
<td><span id="HFILE"></span><span id="hfile"></span><code>HFILE</code></td>
<td><p>A handle to a file opened by <a href="/windows/desktop/api/winbase/nf-winbase-openfile"><strong>OpenFile</strong></a>, not <a href="/windows/desktop/api/fileapi/nf-fileapi-createfilea"><strong>CreateFile</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef int HFILE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HFONT"></span><span id="hfont"></span><code>HFONT</code></td>
<td><p>A handle to a <a href="/windows/desktop/gdi/about-fonts">font</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HFONT;</code></p></td>
</tr>
<tr class="even">
<td><span id="HGDIOBJ"></span><span id="hgdiobj"></span><code>HGDIOBJ</code></td>
<td><p>A handle to a GDI object.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HGDIOBJ;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HGLOBAL"></span><span id="hglobal"></span><code>HGLOBAL</code></td>
<td><p>A handle to a global memory block.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HGLOBAL;</code></p></td>
</tr>
<tr class="even">
<td><span id="HHOOK"></span><span id="hhook"></span><code>HHOOK</code></td>
<td><p>A handle to a <a href="/windows/desktop/winmsg/hooks">hook</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HHOOK;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HICON"></span><span id="hicon"></span><code>HICON</code></td>
<td><p>A handle to an <a href="/windows/desktop/menurc/icons">icon</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HICON;</code></p></td>
</tr>
<tr class="even">
<td><span id="HINSTANCE"></span><span id="hinstance"></span><code>HINSTANCE</code></td>
<td><p>A handle to an instance. This is the base address of the module in memory.</p>
<p><strong>HMODULE</strong> and <strong>HINSTANCE</strong> are the same today, but represented different things in 16-bit Windows.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HINSTANCE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HKEY"></span><span id="hkey"></span><code>HKEY</code></td>
<td><p>A handle to a registry key.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HKEY;</code></p></td>
</tr>
<tr class="even">
<td><span id="HKL"></span><span id="hkl"></span><code>HKL</code></td>
<td><p>An input locale identifier.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HKL;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HLOCAL"></span><span id="hlocal"></span><code>HLOCAL</code></td>
<td><p>A handle to a local memory block.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HLOCAL;</code></p></td>
</tr>
<tr class="even">
<td><span id="HMENU"></span><span id="hmenu"></span><code>HMENU</code></td>
<td><p>A handle to a <a href="/windows/desktop/menurc/menus">menu</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HMENU;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HMETAFILE"></span><span id="hmetafile"></span><code>HMETAFILE</code></td>
<td><p>A handle to a <a href="/windows/desktop/gdi/metafiles">metafile</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HMETAFILE;</code></p></td>
</tr>
<tr class="even">
<td><span id="HMODULE"></span><span id="hmodule"></span><code>HMODULE</code></td>
<td><p>A handle to a module. This is the base address of the module in memory.</p>
<p><strong>HMODULE</strong> and <strong>HINSTANCE</strong> are the same in current versions of Windows, but represented different things in 16-bit Windows.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HINSTANCE HMODULE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HMONITOR"></span><span id="hmonitor"></span><code>HMONITOR</code></td>
<td><p>A handle to a display monitor.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>if(WINVER >= 0x0500) typedef HANDLE HMONITOR;</code></p></td>
</tr>
<tr class="even">
<td><span id="HPALETTE"></span><span id="hpalette"></span><code>HPALETTE</code></td>
<td><p>A handle to a palette.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HPALETTE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HPEN"></span><span id="hpen"></span><code>HPEN</code></td>
<td><p>A handle to a <a href="/windows/desktop/gdi/pens">pen</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HPEN;</code></p></td>
</tr>
<tr class="even">
<td><span id="HRESULT"></span><span id="hresult"></span><code>HRESULT</code></td>
<td><p>The return codes used by COM interfaces. For more information, see <a href="/windows/desktop/com/structure-of-com-error-codes">Structure of the COM Error Codes</a>. To test an <strong>HRESULT</strong> value, use the <a href="/windows/desktop/api/winerror/nf-winerror-failed"><strong>FAILED</strong></a> and <a href="/windows/desktop/api/winerror/nf-winerror-succeeded"><strong>SUCCEEDED</strong></a> macros.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef LONG HRESULT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HRGN"></span><span id="hrgn"></span><code>HRGN</code></td>
<td><p>A handle to a <a href="/windows/desktop/gdi/regions">region</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HRGN;</code></p></td>
</tr>
<tr class="even">
<td><span id="HRSRC"></span><span id="hrsrc"></span><code>HRSRC</code></td>
<td><p>A handle to a resource.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HRSRC;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HSZ"></span><span id="hsz"></span><code>HSZ</code></td>
<td><p>A handle to a DDE string.</p>
<p>This type is declared in Ddeml.h as follows:</p>
<p><code>typedef HANDLE HSZ;</code></p></td>
</tr>
<tr class="even">
<td><span id="HWINSTA"></span><span id="hwinsta"></span><code>HWINSTA</code></td>
<td><p>A handle to a <a href="/windows/desktop/winstation/window-stations">window station</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE WINSTA;</code></p></td>
</tr>
<tr class="odd">
<td><span id="HWND"></span><span id="hwnd"></span><code>HWND</code></td>
<td><p>A handle to a <a href="/windows/desktop/winmsg/windows">window</a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE HWND;</code></p></td>
</tr>
<tr class="even">
<td><span id="INT"></span><span id="int"></span><code>INT</code></td>
<td><p>A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef int INT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="INT_PTR"></span><span id="int_ptr"></span><code>INT_PTR</code></td>
<td><p>A signed integer type for pointer precision. Use when casting a pointer to an integer to perform pointer arithmetic.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="INT8"></span><span id="int8"></span><code>INT8</code></td>
<td><p>An 8-bit signed integer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed char INT8;</code></p></td>
</tr>
<tr class="odd">
<td><span id="INT16"></span><span id="int16"></span><code>INT16</code></td>
<td><p>A 16-bit signed integer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed short INT16;</code></p></td>
</tr>
<tr class="even">
<td><span id="INT32"></span><span id="int32"></span><code>INT32</code></td>
<td><p>A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed int INT32;</code></p></td>
</tr>
<tr class="odd">
<td><span id="INT64"></span><span id="int64"></span><code>INT64</code></td>
<td><p>A 64-bit signed integer. The range is -9223372036854775808 through 9223372036854775807 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed __int64 INT64;</code></p></td>
</tr>
<tr class="even">
<td><span id="LANGID"></span><span id="langid"></span><code>LANGID</code></td>
<td><p>A language identifier. For more information, see <a href="/windows/desktop/Intl/language-identifiers">Language Identifiers</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef WORD LANGID;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LCID"></span><span id="lcid"></span><code>LCID</code></td>
<td><p>A locale identifier. For more information, see <a href="/windows/desktop/Intl/locale-identifiers">Locale Identifiers</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef DWORD LCID;</code></p></td>
</tr>
<tr class="even">
<td><span id="LCTYPE"></span><span id="lctype"></span><code>LCTYPE</code></td>
<td><p>A locale information type. For a list, see <a href="/windows/desktop/Intl/locale-information-constants">Locale Information Constants</a>.</p>
<p>This type is declared in WinNls.h as follows:</p>
<p><code>typedef DWORD LCTYPE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LGRPID"></span><span id="lgrpid"></span><code>LGRPID</code></td>
<td><p>A language group identifier. For a list, see <a href="/windows/desktop/api/winnls/nf-winnls-enumlanguagegrouplocalesa"><strong>EnumLanguageGroupLocales</strong></a>.</p>
<p>This type is declared in WinNls.h as follows:</p>
<p><code>typedef DWORD LGRPID;</code></p></td>
</tr>
<tr class="even">
<td><span id="LONG"></span><span id="long"></span><code>LONG</code></td>
<td><p>A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef long LONG;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LONGLONG"></span><span id="longlong"></span><code>LONGLONG</code></td>
<td><p>A 64-bit signed integer. The range is -9223372036854775808 through 9223372036854775807 decimal.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="LONG_PTR"></span><span id="long_ptr"></span><code>LONG_PTR</code></td>
<td><p>A signed long type for pointer precision. Use when casting a pointer to a long to perform pointer arithmetic.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="LONG32"></span><span id="long32"></span><code>LONG32</code></td>
<td><p>A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef signed int LONG32;</code></p></td>
</tr>
<tr class="even">
<td><span id="LONG64"></span><span id="long64"></span><code>LONG64</code></td>
<td><p>A 64-bit signed integer. The range is -9223372036854775808 through 9223372036854775807 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef __int64 LONG64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPARAM"></span><span id="lparam"></span><code>LPARAM</code></td>
<td><p>A message parameter.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef LONG_PTR LPARAM;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPBOOL"></span><span id="lpbool"></span><code>LPBOOL</code></td>
<td><p>A pointer to a <a href="#bool"><strong>BOOL</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef BOOL far *LPBOOL;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPBYTE"></span><span id="lpbyte"></span><code>LPBYTE</code></td>
<td><p>A pointer to a <a href="#byte"><strong>BYTE</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef BYTE far *LPBYTE;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPCOLORREF"></span><span id="lpcolorref"></span><code>LPCOLORREF</code></td>
<td><p>A pointer to a <a href="/windows/desktop/gdi/colorref"><strong>COLORREF</strong></a> value.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef DWORD *LPCOLORREF;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPCSTR"></span><span id="lpcstr"></span><code>LPCSTR</code></td>
<td><p>A pointer to a constant null-terminated string of 8-bit Windows (ANSI) characters. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef __nullterminated CONST CHAR *LPCSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPCTSTR"></span><span id="lpctstr"></span><code>LPCTSTR</code></td>
<td><p>An <a href="#lpcwstr"><strong>LPCWSTR</strong></a> if <strong>UNICODE</strong> is defined, an <a href="#lpcstr"><strong>LPCSTR</strong></a> otherwise. For more information, see <a href="/windows/desktop/Intl/windows-data-types-for-strings">Windows Data Types for Strings</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="LPCVOID"></span><span id="lpcvoid"></span><code>LPCVOID</code></td>
<td><p>A pointer to a constant of any type.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef CONST void *LPCVOID;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPCWSTR"></span><span id="lpcwstr"></span><code>LPCWSTR</code></td>
<td><p>A pointer to a constant null-terminated string of 16-bit Unicode characters. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CONST WCHAR *LPCWSTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPDWORD"></span><span id="lpdword"></span><code>LPDWORD</code></td>
<td><p>A pointer to a <a href="#dword"><strong>DWORD</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef DWORD *LPDWORD;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPHANDLE"></span><span id="lphandle"></span><code>LPHANDLE</code></td>
<td><p>A pointer to a <a href="#handle"><strong>HANDLE</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HANDLE *LPHANDLE;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPINT"></span><span id="lpint"></span><code>LPINT</code></td>
<td><p>A pointer to an <a href="#int"><strong>INT</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef int *LPINT;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPLONG"></span><span id="lplong"></span><code>LPLONG</code></td>
<td><p>A pointer to a <a href="#long"><strong>LONG</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef long *LPLONG;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPSTR"></span><span id="lpstr"></span><code>LPSTR</code></td>
<td><p>A pointer to a null-terminated string of 8-bit Windows (ANSI) characters. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CHAR *LPSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPTSTR"></span><span id="lptstr"></span><code>LPTSTR</code></td>
<td><p>An <a href="#lpwstr"><strong>LPWSTR</strong></a> if <strong>UNICODE</strong> is defined, an <a href="#lpstr"><strong>LPSTR</strong></a> otherwise. For more information, see <a href="/windows/desktop/Intl/windows-data-types-for-strings">Windows Data Types for Strings</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="LPVOID"></span><span id="lpvoid"></span><code>LPVOID</code></td>
<td><p>A pointer to any type.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef void *LPVOID;</code></p></td>
</tr>
<tr class="even">
<td><span id="LPWORD"></span><span id="lpword"></span><code>LPWORD</code></td>
<td><p>A pointer to a <a href="#word"><strong>WORD</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef WORD *LPWORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="LPWSTR"></span><span id="lpwstr"></span><code>LPWSTR</code></td>
<td><p>A pointer to a null-terminated string of 16-bit Unicode characters. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef WCHAR *LPWSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="LRESULT"></span><span id="lresult"></span><code>LRESULT</code></td>
<td><p>Signed result of message processing.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef LONG_PTR LRESULT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PBOOL"></span><span id="pbool"></span><code>PBOOL</code></td>
<td><p>A pointer to a <a href="#bool"><strong>BOOL</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef BOOL *PBOOL;</code></p></td>
</tr>
<tr class="even">
<td><span id="PBOOLEAN"></span><span id="pboolean"></span><code>PBOOLEAN</code></td>
<td><p>A pointer to a <a href="#boolean"><strong>BOOLEAN</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef BOOLEAN *PBOOLEAN;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PBYTE"></span><span id="pbyte"></span><code>PBYTE</code></td>
<td><p>A pointer to a <a href="#byte"><strong>BYTE</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef BYTE *PBYTE;</code></p></td>
</tr>
<tr class="even">
<td><span id="PCHAR"></span><span id="pchar"></span><code>PCHAR</code></td>
<td><p>A pointer to a <a href="#char"><strong>CHAR</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CHAR *PCHAR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PCSTR"></span><span id="pcstr"></span><code>PCSTR</code></td>
<td><p>A pointer to a constant null-terminated string of 8-bit Windows (ANSI) characters. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CONST CHAR *PCSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="PCTSTR"></span><span id="pctstr"></span><code>PCTSTR</code></td>
<td><p>A <a href="#pcwstr"><strong>PCWSTR</strong></a> if <strong>UNICODE</strong> is defined, a <a href="#pcstr"><strong>PCSTR</strong></a> otherwise. For more information, see <a href="/windows/desktop/Intl/windows-data-types-for-strings">Windows Data Types for Strings</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="PCWSTR"></span><span id="pcwstr"></span><code>PCWSTR</code></td>
<td><p>A pointer to a constant null-terminated string of 16-bit Unicode characters. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CONST WCHAR *PCWSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="PDWORD"></span><span id="pdword"></span><code>PDWORD</code></td>
<td><p>A pointer to a <a href="#dword"><strong>DWORD</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef DWORD *PDWORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PDWORDLONG"></span><span id="pdwordlong"></span><code>PDWORDLONG</code></td>
<td><p>A pointer to a <a href="#dwordlong"><strong>DWORDLONG</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef DWORDLONG *PDWORDLONG;</code></p></td>
</tr>
<tr class="even">
<td><span id="PDWORD_PTR"></span><span id="pdword_ptr"></span><code>PDWORD_PTR</code></td>
<td><p>A pointer to a <a href="#dword_ptr"><strong>DWORD_PTR</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef DWORD_PTR *PDWORD_PTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PDWORD32"></span><span id="pdword32"></span><code>PDWORD32</code></td>
<td><p>A pointer to a <a href="#dword32"><strong>DWORD32</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef DWORD32 *PDWORD32;</code></p></td>
</tr>
<tr class="even">
<td><span id="PDWORD64"></span><span id="pdword64"></span><code>PDWORD64</code></td>
<td><p>A pointer to a <a href="#dword64"><strong>DWORD64</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef DWORD64 *PDWORD64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PFLOAT"></span><span id="pfloat"></span><code>PFLOAT</code></td>
<td><p>A pointer to a <a href="#float"><strong>FLOAT</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef FLOAT *PFLOAT;</code></p></td>
</tr>
<tr class="even">
<td><span id="PHALF_PTR"></span><span id="phalf_ptr"></span><code>PHALF_PTR</code></td>
<td><p>A pointer to a <a href="#half_ptr"><strong>HALF_PTR</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="PHANDLE"></span><span id="phandle"></span><code>PHANDLE</code></td>
<td><p>A pointer to a <a href="#handle"><strong>HANDLE</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef HANDLE *PHANDLE;</code></p></td>
</tr>
<tr class="even">
<td><span id="PHKEY"></span><span id="phkey"></span><code>PHKEY</code></td>
<td><p>A pointer to an <a href="#hkey"><strong>HKEY</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef HKEY *PHKEY;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PINT"></span><span id="pint"></span><code>PINT</code></td>
<td><p>A pointer to an <a href="#int"><strong>INT</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef int *PINT;</code></p></td>
</tr>
<tr class="even">
<td><span id="PINT_PTR"></span><span id="pint_ptr"></span><code>PINT_PTR</code></td>
<td><p>A pointer to an <a href="#int_ptr"><strong>INT_PTR</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT_PTR *PINT_PTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PINT8"></span><span id="pint8"></span><code>PINT8</code></td>
<td><p>A pointer to an <a href="#int8"><strong>INT8</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT8 *PINT8;</code></p></td>
</tr>
<tr class="even">
<td><span id="PINT16"></span><span id="pint16"></span><code>PINT16</code></td>
<td><p>A pointer to an <a href="#int16"><strong>INT16</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT16 *PINT16;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PINT32"></span><span id="pint32"></span><code>PINT32</code></td>
<td><p>A pointer to an <a href="#int32"><strong>INT32</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT32 *PINT32;</code></p></td>
</tr>
<tr class="even">
<td><span id="PINT64"></span><span id="pint64"></span><code>PINT64</code></td>
<td><p>A pointer to an <a href="#int64"><strong>INT64</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef INT64 *PINT64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PLCID"></span><span id="plcid"></span><code>PLCID</code></td>
<td><p>A pointer to an <a href="#lcid"><strong>LCID</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef PDWORD PLCID;</code></p></td>
</tr>
<tr class="even">
<td><span id="PLONG"></span><span id="plong"></span><code>PLONG</code></td>
<td><p>A pointer to a <a href="#long"><strong>LONG</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef LONG *PLONG;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PLONGLONG"></span><span id="plonglong"></span><code>PLONGLONG</code></td>
<td><p>A pointer to a <a href="#longlong"><strong>LONGLONG</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef LONGLONG *PLONGLONG;</code></p></td>
</tr>
<tr class="even">
<td><span id="PLONG_PTR"></span><span id="plong_ptr"></span><code>PLONG_PTR</code></td>
<td><p>A pointer to a <a href="#long_ptr"><strong>LONG_PTR</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef LONG_PTR *PLONG_PTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PLONG32"></span><span id="plong32"></span><code>PLONG32</code></td>
<td><p>A pointer to a <a href="#long32"><strong>LONG32</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef LONG32 *PLONG32;</code></p></td>
</tr>
<tr class="even">
<td><span id="PLONG64"></span><span id="plong64"></span><code>PLONG64</code></td>
<td><p>A pointer to a <a href="#long64"><strong>LONG64</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef LONG64 *PLONG64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="POINTER_32"></span><span id="pointer_32"></span><code>POINTER_32</code></td>
<td><p>A 32-bit pointer. On a 32-bit system, this is a native pointer. On a 64-bit system, this is a truncated 64-bit pointer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="POINTER_64"></span><span id="pointer_64"></span><code>POINTER_64</code></td>
<td><p>A 64-bit pointer. On a 64-bit system, this is a native pointer. On a 32-bit system, this is a sign-extended 32-bit pointer.</p>
<p>Note that it is not safe to assume the state of the high pointer bit.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#if (_MSC_VER >= 1300)
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
<td><span id="POINTER_SIGNED"></span><span id="pointer_signed"></span><code>POINTER_SIGNED</code></td>
<td><p>A signed pointer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>#define POINTER_SIGNED __sptr</code></p></td>
</tr>
<tr class="even">
<td><span id="POINTER_UNSIGNED"></span><span id="pointer_unsigned"></span><code>POINTER_UNSIGNED</code></td>
<td><p>An unsigned pointer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>#define POINTER_UNSIGNED __uptr</code></p></td>
</tr>
<tr class="odd">
<td><span id="PSHORT"></span><span id="pshort"></span><code>PSHORT</code></td>
<td><p>A pointer to a <a href="#short"><strong>SHORT</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef SHORT *PSHORT;</code></p></td>
</tr>
<tr class="even">
<td><span id="PSIZE_T"></span><span id="psize_t"></span><code>PSIZE_T</code></td>
<td><p>A pointer to a <a href="#size_t"><strong>SIZE_T</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef SIZE_T *PSIZE_T;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PSSIZE_T"></span><span id="pssize_t"></span><code>PSSIZE_T</code></td>
<td><p>A pointer to a <a href="#ssize_t"><strong>SSIZE_T</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef SSIZE_T *PSSIZE_T;</code></p></td>
</tr>
<tr class="even">
<td><span id="PSTR"></span><span id="pstr"></span><code>PSTR</code></td>
<td><p>A pointer to a null-terminated string of 8-bit Windows (ANSI) characters. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef CHAR *PSTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PTBYTE"></span><span id="ptbyte"></span><code>PTBYTE</code></td>
<td><p>A pointer to a <a href="#tbyte"><strong>TBYTE</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef TBYTE *PTBYTE;</code></p></td>
</tr>
<tr class="even">
<td><span id="PTCHAR"></span><span id="ptchar"></span><code>PTCHAR</code></td>
<td><p>A pointer to a <a href="#tchar"><strong>TCHAR</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef TCHAR *PTCHAR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PTSTR"></span><span id="ptstr"></span><code>PTSTR</code></td>
<td><p>A <a href="#pwstr"><strong>PWSTR</strong></a> if <strong>UNICODE</strong> is defined, a <a href="#pstr"><strong>PSTR</strong></a> otherwise. For more information, see <a href="/windows/desktop/Intl/windows-data-types-for-strings">Windows Data Types for Strings</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="PUCHAR"></span><span id="puchar"></span><code>PUCHAR</code></td>
<td><p>A pointer to a <a href="#uchar"><strong>UCHAR</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef UCHAR *PUCHAR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUHALF_PTR"></span><span id="puhalf_ptr"></span><code>PUHALF_PTR</code></td>
<td><p>A pointer to a <a href="#uhalf_ptr"><strong>UHALF_PTR</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="PUINT"></span><span id="puint"></span><code>PUINT</code></td>
<td><p>A pointer to a <a href="#uint"><strong>UINT</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef UINT *PUINT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUINT_PTR"></span><span id="puint_ptr"></span><code>PUINT_PTR</code></td>
<td><p>A pointer to a <a href="#uint_ptr"><strong>UINT_PTR</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT_PTR *PUINT_PTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="PUINT8"></span><span id="puint8"></span><code>PUINT8</code></td>
<td><p>A pointer to a <a href="#uint8"><strong>UINT8</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT8 *PUINT8;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUINT16"></span><span id="puint16"></span><code>PUINT16</code></td>
<td><p>A pointer to a <a href="#uint16"><strong>UINT16</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT16 *PUINT16;</code></p></td>
</tr>
<tr class="even">
<td><span id="PUINT32"></span><span id="puint32"></span><code>PUINT32</code></td>
<td><p>A pointer to a <a href="#uint32"><strong>UINT32</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT32 *PUINT32;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUINT64"></span><span id="puint64"></span><code>PUINT64</code></td>
<td><p>A pointer to a <a href="#uint64"><strong>UINT64</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef UINT64 *PUINT64;</code></p></td>
</tr>
<tr class="even">
<td><span id="PULONG"></span><span id="pulong"></span><code>PULONG</code></td>
<td><p>A pointer to a <a href="#ulong"><strong>ULONG</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef ULONG *PULONG;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PULONGLONG"></span><span id="pulonglong"></span><code>PULONGLONG</code></td>
<td><p>A pointer to a <a href="#ulonglong"><strong>ULONGLONG</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef ULONGLONG *PULONGLONG;</code></p></td>
</tr>
<tr class="even">
<td><span id="PULONG_PTR"></span><span id="pulong_ptr"></span><code>PULONG_PTR</code></td>
<td><p>A pointer to a <a href="#ulong_ptr"><strong>ULONG_PTR</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef ULONG_PTR *PULONG_PTR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PULONG32"></span><span id="pulong32"></span><code>PULONG32</code></td>
<td><p>A pointer to a <a href="#ulong32"><strong>ULONG32</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef ULONG32 *PULONG32;</code></p></td>
</tr>
<tr class="even">
<td><span id="PULONG64"></span><span id="pulong64"></span><code>PULONG64</code></td>
<td><p>A pointer to a <a href="#ulong64"><strong>ULONG64</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef ULONG64 *PULONG64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PUSHORT"></span><span id="pushort"></span><code>PUSHORT</code></td>
<td><p>A pointer to a <a href="#ushort"><strong>USHORT</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef USHORT *PUSHORT;</code></p></td>
</tr>
<tr class="even">
<td><span id="PVOID"></span><span id="pvoid"></span><code>PVOID</code></td>
<td><p>A pointer to any type.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef void *PVOID;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PWCHAR"></span><span id="pwchar"></span><code>PWCHAR</code></td>
<td><p>A pointer to a <a href="#wchar"><strong>WCHAR</strong></a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef WCHAR *PWCHAR;</code></p></td>
</tr>
<tr class="even">
<td><span id="PWORD"></span><span id="pword"></span><code>PWORD</code></td>
<td><p>A pointer to a <a href="#word"><strong>WORD</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef WORD *PWORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="PWSTR"></span><span id="pwstr"></span><code>PWSTR</code></td>
<td><p>A pointer to a null-terminated string of 16-bit Unicode characters. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef WCHAR *PWSTR;</code></p></td>
</tr>
<tr class="even">
<td><span id="QWORD"></span><span id="qword"></span><code>QWORD</code></td>
<td><p>A 64-bit unsigned integer.</p>
<p>This type is declared as follows:</p>
<p><code>typedef unsigned __int64 QWORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="SC_HANDLE"></span><span id="sc_handle"></span><code>SC_HANDLE</code></td>
<td><p>A handle to a service control manager database. For more information, see <a href="/windows/desktop/Services/scm-handles">SCM Handles</a>.</p>
<p>This type is declared in WinSvc.h as follows:</p>
<p><code>typedef HANDLE SC_HANDLE;</code></p></td>
</tr>
<tr class="even">
<td><span id="SC_LOCK"></span><span id="sc_lock"></span><code>SC_LOCK</code></td>
<td><p>A lock to a service control manager database. For more information, see <a href="/windows/desktop/Services/scm-handles">SCM Handles</a>.</p>
<p>This type is declared in WinSvc.h as follows:</p>
<p><code>typedef LPVOID SC_LOCK;</code></p></td>
</tr>
<tr class="odd">
<td><span id="SERVICE_STATUS_HANDLE"></span><span id="service_status_handle"></span><code>SERVICE_STATUS_HANDLE</code></td>
<td><p>A handle to a service status value. For more information, see <a href="/windows/desktop/Services/scm-handles">SCM Handles</a>.</p>
<p>This type is declared in WinSvc.h as follows:</p>
<p><code>typedef HANDLE SERVICE_STATUS_HANDLE;</code></p></td>
</tr>
<tr class="even">
<td><span id="SHORT"></span><span id="short"></span><code>SHORT</code></td>
<td><p>A 16-bit integer. The range is -32768 through 32767 decimal.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef short SHORT;</code></p></td>
</tr>
<tr class="odd">
<td><span id="SIZE_T"></span><span id="size_t"></span><code>SIZE_T</code></td>
<td><p>The maximum number of bytes to which a pointer can point. Use for a count that must span the full range of a pointer.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef ULONG_PTR SIZE_T;</code></p></td>
</tr>
<tr class="even">
<td><span id="SSIZE_T"></span><span id="ssize_t"></span><code>SSIZE_T</code></td>
<td><p>A signed version of <a href="#size_t"><strong>SIZE_T</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef LONG_PTR SSIZE_T;</code></p></td>
</tr>
<tr class="odd">
<td><span id="TBYTE"></span><span id="tbyte"></span><code>TBYTE</code></td>
<td><p>A <a href="#wchar"><strong>WCHAR</strong></a> if <strong>UNICODE</strong> is defined, a <a href="#char"><strong>CHAR</strong></a> otherwise.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="TCHAR"></span><span id="tchar"></span><code>TCHAR</code></td>
<td><p>A <a href="#wchar"><strong>WCHAR</strong></a> if <strong>UNICODE</strong> is defined, a <a href="#char"><strong>CHAR</strong></a> otherwise.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="UCHAR"></span><span id="uchar"></span><code>UCHAR</code></td>
<td><p>An unsigned <a href="#char"><strong>CHAR</strong></a>.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned char UCHAR;</code></p></td>
</tr>
<tr class="even">
<td><span id="UHALF_PTR"></span><span id="uhalf_ptr"></span><code>UHALF_PTR</code></td>
<td><p>An unsigned <a href="#half_ptr"><strong>HALF_PTR</strong></a>. Use within a structure that contains a pointer and two small fields.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="UINT"></span><span id="uint"></span><code>UINT</code></td>
<td><p>An unsigned <a href="#int"><strong>INT</strong></a>. The range is 0 through 4294967295 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned int UINT;</code></p></td>
</tr>
<tr class="even">
<td><span id="UINT_PTR"></span><span id="uint_ptr"></span><code>UINT_PTR</code></td>
<td><p>An unsigned <a href="#int_ptr"><strong>INT_PTR</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="UINT8"></span><span id="uint8"></span><code>UINT8</code></td>
<td><p>An unsigned <a href="#int8"><strong>INT8</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned  char UINT8;</code></p></td>
</tr>
<tr class="even">
<td><span id="UINT16"></span><span id="uint16"></span><code>UINT16</code></td>
<td><p>An unsigned <a href="#int16"><strong>INT16</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned  short UINT16;</code></p></td>
</tr>
<tr class="odd">
<td><span id="UINT32"></span><span id="uint32"></span><code>UINT32</code></td>
<td><p>An unsigned <a href="#int32"><strong>INT32</strong></a>. The range is 0 through 4294967295 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned int UINT32;</code></p></td>
</tr>
<tr class="even">
<td><span id="UINT64"></span><span id="uint64"></span><code>UINT64</code></td>
<td><p>An unsigned <a href="#int64"><strong>INT64</strong></a>. The range is 0 through 18446744073709551615 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned __int64 UINT64;</code></p></td>
</tr>
<tr class="odd">
<td><span id="ULONG"></span><span id="ulong"></span><code>ULONG</code></td>
<td><p>An unsigned <a href="#long"><strong>LONG</strong></a>. The range is 0 through 4294967295 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned long ULONG;</code></p></td>
</tr>
<tr class="even">
<td><span id="ULONGLONG"></span><span id="ulonglong"></span><code>ULONGLONG</code></td>
<td><p>A 64-bit unsigned integer. The range is 0 through 18446744073709551615 decimal.</p>
<p>This type is declared in WinNT.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="ULONG_PTR"></span><span id="ulong_ptr"></span><code>ULONG_PTR</code></td>
<td><p>An unsigned <a href="#long_ptr"><strong>LONG_PTR</strong></a>.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="ULONG32"></span><span id="ulong32"></span><code>ULONG32</code></td>
<td><p>An unsigned <a href="#long32"><strong>LONG32</strong></a>. The range is 0 through 4294967295 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned int ULONG32;</code></p></td>
</tr>
<tr class="odd">
<td><span id="ULONG64"></span><span id="ulong64"></span><code>ULONG64</code></td>
<td><p>An unsigned <a href="#long64"><strong>LONG64</strong></a>. The range is 0 through 18446744073709551615 decimal.</p>
<p>This type is declared in BaseTsd.h as follows:</p>
<p><code>typedef unsigned __int64 ULONG64;</code></p></td>
</tr>
<tr class="even">
<td><span id="UNICODE_STRING"></span><span id="unicode_string"></span><code>UNICODE_STRING</code></td>
<td><p>A Unicode string.</p>
<p>This type is declared in Winternl.h as follows:</p>
<div class="code">
<span data-codelanguage="ManagedCPlusPlus"></span>
<table>
<colgroup>
<col  />
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
<td><span id="USHORT"></span><span id="ushort"></span><code>USHORT</code></td>
<td><p>An unsigned <a href="#short"><strong>SHORT</strong></a>. The range is 0 through 65535 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned short USHORT;</code></p></td>
</tr>
<tr class="even">
<td><span id="USN"></span><span id="usn"></span><code>USN</code></td>
<td><p>An update sequence number (USN).</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef LONGLONG USN;</code></p></td>
</tr>
<tr class="odd">
<td><span id="VOID"></span><span id="void"></span><code>VOID</code></td>
<td><p>Any type.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>#define VOID void</code></p></td>
</tr>
<tr class="even">
<td><span id="WCHAR"></span><span id="wchar"></span><code>WCHAR</code></td>
<td><p>A 16-bit Unicode character. For more information, see <a href="/windows/desktop/gdi/character-sets-used-by-fonts">Character Sets Used By Fonts</a>.</p>
<p>This type is declared in WinNT.h as follows:</p>
<p><code>typedef wchar_t WCHAR;</code></p></td>
</tr>
<tr class="odd">
<td><span id="WINAPI"></span><span id="winapi"></span><code>WINAPI</code></td>
<td><p>The calling convention for system functions.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>#define WINAPI __stdcall</code></p>
<p><strong>CALLBACK</strong>, <strong>WINAPI</strong>, and <strong>APIENTRY</strong> are all used to define functions with the __stdcall calling convention. Most functions in the Windows API are declared using <strong>WINAPI</strong>. You may wish to use <strong>CALLBACK</strong> for the callback functions that you implement to help identify the function as a callback function.</p></td>
</tr>
<tr class="even">
<td><span id="WORD"></span><span id="word"></span><code>WORD</code></td>
<td><p>A 16-bit unsigned integer. The range is 0 through 65535 decimal.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef unsigned short WORD;</code></p></td>
</tr>
<tr class="odd">
<td><span id="WPARAM"></span><span id="wparam"></span><code>WPARAM</code></td>
<td><p>A message parameter.</p>
<p>This type is declared in WinDef.h as follows:</p>
<p><code>typedef UINT_PTR WPARAM;</code></p></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                |
| Header<br/>                   | <dl> <dt>BaseTsd.h; </dt> <dt>WinDef.h; </dt> <dt>WinNT.h</dt> </dl> |
