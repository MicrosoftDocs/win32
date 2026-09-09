---
title: Resource Types (Winuser.h)
description: The following are the predefined resource types.
ms.assetid: 8d27f79a-8165-4565-a975-f25b2344efdc
topic_type:
- apiref
api_name:
- RT_ACCELERATOR
- RT_ANICURSOR
- RT_ANIICON
- RT_BITMAP
- RT_CURSOR
- RT_DIALOG
- RT_DLGINCLUDE
- RT_FONT
- RT_FONTDIR
- RT_GROUP_CURSOR
- RT_GROUP_ICON
- RT_HTML
- RT_ICON
- RT_MANIFEST
- RT_MENU
- RT_MESSAGETABLE
- RT_PLUGPLAY
- RT_RCDATA
- RT_STRING
- RT_VERSION
- RT_VXD
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Resource Types

The following are the predefined resource types.



| Constant/value                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                      |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RT_ACCELERATOR"></span><span id="rt_accelerator"></span><dl> <dt>**RT\_ACCELERATOR**</dt> <dt>MAKEINTRESOURCE(9)</dt> </dl>                                 | Accelerator table.<br/>                                                                                                                                                                                                                                                                    |
| <span id="RT_ANICURSOR"></span><span id="rt_anicursor"></span><dl> <dt>**RT\_ANICURSOR**</dt> <dt>MAKEINTRESOURCE(21)</dt> </dl>                                      | Animated cursor.<br/>                                                                                                                                                                                                                                                                      |
| <span id="RT_ANIICON"></span><span id="rt_aniicon"></span><dl> <dt>**RT\_ANIICON**</dt> <dt>MAKEINTRESOURCE(22)</dt> </dl>                                            | Animated icon.<br/>                                                                                                                                                                                                                                                                        |
| <span id="RT_BITMAP"></span><span id="rt_bitmap"></span><dl> <dt>**RT\_BITMAP**</dt> <dt>MAKEINTRESOURCE(2)</dt> </dl>                                                | Bitmap resource.<br/>                                                                                                                                                                                                                                                                      |
| <span id="RT_CURSOR"></span><span id="rt_cursor"></span><dl> <dt>**RT\_CURSOR**</dt> <dt>MAKEINTRESOURCE(1)</dt> </dl>                                                | Hardware-dependent cursor resource.<br/>                                                                                                                                                                                                                                                   |
| <span id="RT_DIALOG"></span><span id="rt_dialog"></span><dl> <dt>**RT\_DIALOG**</dt> <dt>MAKEINTRESOURCE(5)</dt> </dl>                                                | Dialog box.<br/>                                                                                                                                                                                                                                                                           |
| <span id="RT_DLGINCLUDE"></span><span id="rt_dlginclude"></span><dl> <dt>**RT\_DLGINCLUDE**</dt> <dt>MAKEINTRESOURCE(17)</dt> </dl>                                   | Allows a resource editing tool to associate a string with an .rc file. Typically, the string is the name of the header file that provides symbolic names. The resource compiler parses the string but otherwise ignores the value. For example, <br/> `1 DLGINCLUDE "MyFile.h"`<br/> |
| <span id="RT_FONT"></span><span id="rt_font"></span><dl> <dt>**RT\_FONT**</dt> <dt>MAKEINTRESOURCE(8)</dt> </dl>                                                      | Font resource.<br/>                                                                                                                                                                                                                                                                        |
| <span id="RT_FONTDIR"></span><span id="rt_fontdir"></span><dl> <dt>**RT\_FONTDIR**</dt> <dt>MAKEINTRESOURCE(7)</dt> </dl>                                             | Font directory resource.<br/>                                                                                                                                                                                                                                                              |
| <span id="RT_GROUP_CURSOR"></span><span id="rt_group_cursor"></span><dl> <dt>**RT\_GROUP\_CURSOR**</dt> <dt>MAKEINTRESOURCE((ULONG\_PTR)(RT\_CURSOR) + 11)</dt> </dl> | Hardware-independent cursor resource.<br/>                                                                                                                                                                                                                                                 |
| <span id="RT_GROUP_ICON"></span><span id="rt_group_icon"></span><dl> <dt>**RT\_GROUP\_ICON**</dt> <dt>MAKEINTRESOURCE((ULONG\_PTR)(RT\_ICON) + 11)</dt> </dl>         | Hardware-independent icon resource.<br/>                                                                                                                                                                                                                                                   |
| <span id="RT_HTML"></span><span id="rt_html"></span><dl> <dt>**RT\_HTML**</dt> <dt>MAKEINTRESOURCE(23)</dt> </dl>                                                     | HTML resource.<br/>                                                                                                                                                                                                                                                                        |
| <span id="RT_ICON"></span><span id="rt_icon"></span><dl> <dt>**RT\_ICON**</dt> <dt>MAKEINTRESOURCE(3)</dt> </dl>                                                      | Hardware-dependent icon resource.<br/>                                                                                                                                                                                                                                                     |
| <span id="RT_MANIFEST"></span><span id="rt_manifest"></span><dl> <dt>**RT\_MANIFEST**</dt> <dt>MAKEINTRESOURCE(24)</dt> </dl>                                         | Side-by-Side Assembly Manifest.<br/>                                                                                                                                                                                                                                                       |
| <span id="RT_MENU"></span><span id="rt_menu"></span><dl> <dt>**RT\_MENU**</dt> <dt>MAKEINTRESOURCE(4)</dt> </dl>                                                      | Menu resource.<br/>                                                                                                                                                                                                                                                                        |
| <span id="RT_MESSAGETABLE"></span><span id="rt_messagetable"></span><dl> <dt>**RT\_MESSAGETABLE**</dt> <dt>MAKEINTRESOURCE(11)</dt> </dl>                             | Message-table entry.<br/>                                                                                                                                                                                                                                                                  |
| <span id="RT_PLUGPLAY"></span><span id="rt_plugplay"></span><dl> <dt>**RT\_PLUGPLAY**</dt> <dt>MAKEINTRESOURCE(19)</dt> </dl>                                         | Plug and Play resource.<br/>                                                                                                                                                                                                                                                               |
| <span id="RT_RCDATA"></span><span id="rt_rcdata"></span><dl> <dt>**RT\_RCDATA**</dt> <dt>MAKEINTRESOURCE(10)</dt> </dl>                                               | Application-defined resource (raw data).<br/>                                                                                                                                                                                                                                              |
| <span id="RT_STRING"></span><span id="rt_string"></span><dl> <dt>**RT\_STRING**</dt> <dt>MAKEINTRESOURCE(6)</dt> </dl>                                                | String-table entry. See **Remarks** below for more info.<br/>                                                                                                                                                                                                                                                                   |
| <span id="RT_VERSION"></span><span id="rt_version"></span><dl> <dt>**RT\_VERSION**</dt> <dt>MAKEINTRESOURCE(16)</dt> </dl>                                            | Version resource.<br/>                                                                                                                                                                                                                                                                     |
| <span id="RT_VXD"></span><span id="rt_vxd"></span><dl> <dt>**RT\_VXD**</dt> <dt>MAKEINTRESOURCE(20)</dt> </dl>                                                        | VXD.<br/>                                                                                                                                                                                                                                                                                  |



## Remarks

### String Table Resources

When enumerating String Table resources (type **RT_STRING**) with functions such as **EnumResourceNamesW**, the system doesn't
enumerate each individual string resource ID; instead it enumerates blocks of resources. You must inpsect these blocks to 
determine which string resource ID(s) they actually contain.

String resources are packaged into blocks, each of which contains 16 length-prefixed strings representing 16 consecutive
IDs (some of which may not be used; see below). Given a string resource ID `X`, it will placed in the resource block number 
`(X \ 16) + 1` (where `\` denotes integer division). Within that block, the resource can be found as the `N`th entry, 
where `N = X % 16`. 

The following table shows some example string resource IDs and the block number (and offset) of where they will be
located:

| Resource ID | Block # | Offset |
|-|-|-|
| 1 | `(1 \ 16) + 1` = 1 | `1 % 16` = 1 |
| 2 | `(2 \ 16) + 1` = 1 | `2 % 16` = 2 |
| 5 | `(3 \ 16) + 1` =  1 | `5 % 16` = 5 |
| 15 | `(15 \ 16) + 1` = 1 | `15 % 16` = 15 |
| 20 | `(20 \ 16) + 1` = 2 | `20 % 16` = 4 |
| 32 | `(32 \ 16) + 1` = 3 | `32 % 16` = 0 |
| 50 | `(50 \ 16) + 1` = 4 | `50 % 16` = 2 |
| 100 | `(100 \ 16) + 1` = 7 | `100 % 16` = 4 |

Any unused (missing) resource IDs are denoted by zero-length strings. So in the example above, block #1 will have zero-length strings
representing IDs 0, 3, 4, and 6 - 14. None of the strings in the block have terminating **NULL** characters, since it is permitted 
for string resources to contain embedded **NULLs**. Thus, the memory layout of block #1 looks like this, assuming each string's value 
is "Hello world" (11 characters long) and where the numbers in angle brackets represent integers (not literal characters):

```
<0><11>Hello world<11>Hello world<0><0>
<11>Hello world<0><0><0><0><0><0><0><0>
<0><11>Hello world
```

The following code snippet shows an enumeration callback function that will enumerate individual **RT_STRING** resources
just like other types (like **RT_ICON**) than the blocks:

```C++
// Number of entries in the string table.
constexpr UINT STRING_TABLE_SIZE{ 16 };

// Returns the original resource ID from a given block / offset.
inline UINT GetStringResourceIdFromStringTable(LPCWSTR lpName, const unsigned int index)
{
    _ASSERT(index < STRING_TABLE_SIZE);
    return ((reinterpret_cast<UINT>(lpName) - 1) * STRING_TABLE_SIZE) + index;
}

// Helper function that will enumerate string table blocks, looking for resources.
BOOL EnumerateResourceNamesWrapperForStrings(HMODULE hModule, LPWSTR lpName, LONG_PTR lParam, ENUMRESNAMEPROCW lpEnumFunc)
{
    // No need to free or unlock resources in Win32, so OK to throw away intermediates
    auto ptr = (wchar_t*)LockResource(LoadResource(hModule, FindResource(hModule, lpName, RT_STRING)));
    if (ptr)
    {
        for (unsigned int i = 0; i < STRING_TABLE_SIZE; ++i)
        {
            wchar_t size = *ptr;
            if (size > 0)
            {
                auto id = GetStringResourceIdFromStringTable(lpName, i);

                // Invoke the callback for this string resource ID.
                auto callbackResult = lpEnumFunc(hModule, RT_STRING, MAKEINTRESOURCE(id), lParam);
                if (!callbackResult)
                {
                    return callbackResult;
                }
            }
            // Skip to next potential string in the block
            ptr += size + 1;
        }
        return TRUE;
    }

    // Couldn't load the string table entry; something is wrong.
    return FALSE;
}

// Wrapper function for EnumResourceNamesW that will enumerate individual string resources.
BOOL EnumResourceNamesIncludingStringsW(HMODULE hModule, LPCWSTR lpType, ENUMRESNAMEPROCW lpEnumFunc, LONG_PTR lParam)
{
    struct param_wrapper { ENUMRESNAMEPROCW lpEnumFunc; LONG_PTR lParam; } params{ lpEnumFunc, lParam };

    // Use a simple lambda to either call our String helper, or directly call the user's callback
    return EnumResourceNamesW(hModule, lpType, [](auto hModule, auto lpType, auto lpName, auto lParam)
        {
            auto params = reinterpret_cast<param_wrapper*>(lParam);
            if (lpType == RT_STRING)
            {
                return EnumerateResourceNamesWrapperForStrings(hModule, lpName, params->lParam, params->lpEnumFunc);
            }

            return params->lpEnumFunc(hModule, lpType, lpName, params->lParam);
        }, reinterpret_cast<LONG_PTR>(&params));
};

//////////

// Sample callback that just increments a counter.
BOOL CountResources(HMODULE, LPCWSTR, LPWSTR, LONG_PTR lParam)
{
    // Add one to the count...
    (*(reinterpret_cast<UINT*>(lParam)))++;
    return TRUE;
}

// Sample usage:
void CountStringsInExplorer()
{
    auto lib = LoadLibraryExW(LR"(c:\windows\explorer.exe)", nullptr, LOAD_LIBRARY_AS_DATAFILE);
    if (!lib)
    {
        return;
    }

    UINT nStringBlocks{ 0 };
    UINT nStrings{ 0 };

    // Count the number of string blocks using raw Win32 API.
    EnumResourceNamesW(lib, RT_STRING, CountResources, (LONG_PTR)&nStringBlocks);

    // Count the number of actual strings, using the wrapper.
    EnumResourceNamesIncludingStringsW(lib, RT_STRING, CountResources, (LONG_PTR)&nStrings);

    // Outputs something like:
    //
    // Explorer.exe contains 44 strings (in 17 blocks).
    //

    std::wcout << L"Explorer.exe contains " << nStrings << L" strings (in " << nStringBlocks
        << L" blocks)." << std::endl;
}
```

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winuser.h</dt> </dl> |



 

 





