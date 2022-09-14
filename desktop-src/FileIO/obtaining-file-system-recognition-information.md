---
description: File system recognition is the ability to recognize storage media that contain a valid file system/volume layout that has not been defined yet, but the media is able to identify itself through the presence of the recognition structure defined internally by Windows.
ms.assetid: 23ed6de0-25ff-4841-91f6-94b487dee613
title: Obtaining File System Recognition Information
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining File System Recognition Information

[File system recognition](file-system-recognition.md) is the ability to recognize storage media that contain a valid file system/volume layout that has not been defined yet, but the media is able to identify itself through the presence of the recognition structure defined internally by Windows.

Because no existing file system will recognize a new disk layout, the "RAW" file system will mount the volume and provide direct block level access. The "RAW" file system, incorporated in *NtosKrnl*, will have the ability to read the file system recognition structure and provide applications access to such structures through the file system control request [**FSCTL\_QUERY\_FILE\_SYSTEM\_RECOGNITION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_file_system_recognition), shown in the following example.


```C++
STDMETHODIMP CheckFileSystem(
    PCWSTR pcwszDrive
    ) 
{
    HRESULT hr = S_OK;
    HANDLE  hDisk = INVALID_HANDLE_VALUE;
    BOOL    fResult = FALSE;    
    ULONG   BytesReturned = 0;    
    FILE_SYSTEM_RECOGNITION_INFORMATION     FsRi = {0};
    
    //
    // Open the target, for example "\\.\C:"
    //
    wprintf( L"CreateFile on %s...", pcwszDrive );
    hDisk = CreateFile( pcwszDrive, 
                        FILE_READ_ATTRIBUTES|SYNCHRONIZE|FILE_TRAVERSE,                        
                        FILE_SHARE_READ|FILE_SHARE_WRITE,
                        NULL, OPEN_EXISTING, 0, NULL );    
    if( hDisk == INVALID_HANDLE_VALUE ) 
    {
        hr = HRESULT_FROM_WIN32( GetLastError() );
        wprintf( L"CreateFile failed on %s, GLE = 0x%x\n", pcwszDrive, GetLastError() );
        goto exit;
    }
    wprintf( L"succeeded.\n\n" );

    wprintf( L"\nPress Any Key to send down the FSCTL\n" );
    _getwch();

    //
    // Send down the FSCTL
    //
    wprintf( L"Calling DeviceIoControl( FSCTL_QUERY_FILE_SYSTEM_RECOGNITION ) " );
    
    fResult = DeviceIoControl( hDisk, 
                               FSCTL_QUERY_FILE_SYSTEM_RECOGNITION, 
                               NULL, 
                               0, 
                               &FsRi, 
                               sizeof(FsRi), 
                               &BytesReturned, 
                               NULL );
    if( !fResult ) 
    {
        hr = HRESULT_FROM_WIN32( GetLastError() );
        wprintf( L"failed GLE = 0x%x\n", GetLastError() );
        goto exit;
    }
    wprintf( L"succeeded.\n\n" );

    wprintf( L"FSCTL_QUERY_FILE_SYSTEM_RECOGNITION returned success.\n" );

    wprintf( L"FSCTL_QUERY_FILE_SYSTEM_RECOGNITION retrieved \"%S\".\n",
              FsRi.FileSystem );

exit:

    if( hDisk != INVALID_HANDLE_VALUE ) 
    {
        CloseHandle( hDisk );
        hDisk = INVALID_HANDLE_VALUE;
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[File System Recognition](file-system-recognition.md)
</dt> <dt>

[**FILE\_SYSTEM\_RECOGNITION\_STRUCTURE**](file-system-recognition-structure.md)
</dt> <dt>

[**FSCTL\_QUERY\_FILE\_SYSTEM\_RECOGNITION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_file_system_recognition)
</dt> </dl>

 

 
