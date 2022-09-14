---
description: C++ example shows how to display all paths for each volume and device. For each volume in the system, the example locates the volume, obtains the device name, obtains all paths for that volume, and displays the paths.
ms.assetid: a9ee8cc8-fa62-4fc9-aa69-35ee98afe417
title: Displaying Volume Paths
ms.topic: article
ms.date: 05/31/2018
---

# Displaying Volume Paths

The following C++ example shows how to display all paths for each volume and device. For each volume in the system, the example locates the volume, obtains the device name, obtains all paths for that volume, and displays the paths.


```C++
#include <windows.h>
#include <stdio.h>

void DisplayVolumePaths(
        __in PWCHAR VolumeName
        )
{
    DWORD  CharCount = MAX_PATH + 1;
    PWCHAR Names     = NULL;
    PWCHAR NameIdx   = NULL;
    BOOL   Success   = FALSE;

    for (;;) 
    {
        //
        //  Allocate a buffer to hold the paths.
        Names = (PWCHAR) new BYTE [CharCount * sizeof(WCHAR)];

        if ( !Names ) 
        {
            //
            //  If memory can't be allocated, return.
            return;
        }

        //
        //  Obtain all of the paths
        //  for this volume.
        Success = GetVolumePathNamesForVolumeNameW(
            VolumeName, Names, CharCount, &CharCount
            );

        if ( Success ) 
        {
            break;
        }

        if ( GetLastError() != ERROR_MORE_DATA ) 
        {
            break;
        }

        //
        //  Try again with the
        //  new suggested size.
        delete [] Names;
        Names = NULL;
    }

    if ( Success )
    {
        //
        //  Display the various paths.
        for ( NameIdx = Names; 
              NameIdx[0] != L'\0'; 
              NameIdx += wcslen(NameIdx) + 1 ) 
        {
            wprintf(L"  %s", NameIdx);
        }
        wprintf(L"\n");
    }

    if ( Names != NULL ) 
    {
        delete [] Names;
        Names = NULL;
    }

    return;
}

void __cdecl wmain(void)
{
    DWORD  CharCount            = 0;
    WCHAR  DeviceName[MAX_PATH] = L"";
    DWORD  Error                = ERROR_SUCCESS;
    HANDLE FindHandle           = INVALID_HANDLE_VALUE;
    BOOL   Found                = FALSE;
    size_t Index                = 0;
    BOOL   Success              = FALSE;
    WCHAR  VolumeName[MAX_PATH] = L"";

    //
    //  Enumerate all volumes in the system.
    FindHandle = FindFirstVolumeW(VolumeName, ARRAYSIZE(VolumeName));

    if (FindHandle == INVALID_HANDLE_VALUE)
    {
        Error = GetLastError();
        wprintf(L"FindFirstVolumeW failed with error code %d\n", Error);
        return;
    }

    for (;;)
    {
        //
        //  Skip the \\?\ prefix and remove the trailing backslash.
        Index = wcslen(VolumeName) - 1;

        if (VolumeName[0]     != L'\\' ||
            VolumeName[1]     != L'\\' ||
            VolumeName[2]     != L'?'  ||
            VolumeName[3]     != L'\\' ||
            VolumeName[Index] != L'\\') 
        {
            Error = ERROR_BAD_PATHNAME;
            wprintf(L"FindFirstVolumeW/FindNextVolumeW returned a bad path: %s\n", VolumeName);
            break;
        }

        //
        //  QueryDosDeviceW does not allow a trailing backslash,
        //  so temporarily remove it.
        VolumeName[Index] = L'\0';

        CharCount = QueryDosDeviceW(&VolumeName[4], DeviceName, ARRAYSIZE(DeviceName)); 

        VolumeName[Index] = L'\\';

        if ( CharCount == 0 ) 
        {
            Error = GetLastError();
            wprintf(L"QueryDosDeviceW failed with error code %d\n", Error);
            break;
        }

        wprintf(L"\nFound a device:\n %s", DeviceName);
        wprintf(L"\nVolume name: %s", VolumeName);
        wprintf(L"\nPaths:");
        DisplayVolumePaths(VolumeName);

        //
        //  Move on to the next volume.
        Success = FindNextVolumeW(FindHandle, VolumeName, ARRAYSIZE(VolumeName));

        if ( !Success ) 
        {
            Error = GetLastError();

            if (Error != ERROR_NO_MORE_FILES) 
            {
                wprintf(L"FindNextVolumeW failed with error code %d\n", Error);
                break;
            }

            //
            //  Finished iterating
            //  through all the volumes.
            Error = ERROR_SUCCESS;
            break;
        }
    }

    FindVolumeClose(FindHandle);
    FindHandle = INVALID_HANDLE_VALUE;

    return;
}
```



The following is example output from running the application. For each volume, the output includes a volume device path, a volume GUID path, and a drive letter.

``` syntax
Found a device:
 \Device\HarddiskVolume2
Volume name: \\?\Volume{4c1b02c1-d990-11dc-99ae-806e6f6e6963}\
Paths:  C:\

Found a device:
 \Device\CdRom0
Volume name: \\?\Volume{4c1b02c4-d990-11dc-99ae-806e6f6e6963}\
Paths:  D:\
```

## Related topics

<dl> <dt>

[**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew)
</dt> <dt>

[**FindNextVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findnextvolumew)
</dt> <dt>

[**FindVolumeClose**](/windows/desktop/api/FileAPI/nf-fileapi-findvolumeclose)
</dt> <dt>

[**GetVolumePathNamesForVolumeName**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumepathnamesforvolumenamew)
</dt> <dt>

[**QueryDosDevice**](/windows/desktop/api/FileAPI/nf-fileapi-querydosdevicew)
</dt> </dl>

 

 



