---
title: DVC Server Module Example
description: C++ code sample that shows how to create the server-side dynamic virtual channel (DVC) module.
ms.assetid: 497d4ed3-8160-43d2-8f03-b2f2b7988dc3
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# DVC Server Module Example

The following C++ code sample provides an example of how to create the server-side dynamic virtual channel (DVC) module.


```C++
#include <windows.h>
#include <wtsapi32.h>
#include <pchannel.h>
#include <crtdbg.h>

#pragma comment(lib, "wtsapi32.lib")

#define _MAX_WAIT       60000
#define MAX_MSG_SIZE    0x20000
#define START_MSG_SIZE  4
#define STEP_MSG_SIZE   113

DWORD OpenDynamicChannel(LPCSTR szChannelName, HANDLE *phFile);
DWORD WINAPI WriteThread(PVOID param);
DWORD WINAPI ReadThread(PVOID param);

INT _cdecl wmain(INT argc, __in_ecount( argc ) WCHAR **argv)
{
    DWORD rc;
    HANDLE hFile;

    rc = OpenDynamicChannel ( "DVC_Sample", &hFile );
    if ( ERROR_SUCCESS != rc )
    {
        return 0;
    }

    DWORD dwThreadId;
    HANDLE hReadThread = CreateThread(
        NULL,
        0,
        ReadThread,
        hFile,
        0,
        &dwThreadId );

    HANDLE hWriteThread = CreateThread(
        NULL,
        0,
        WriteThread,
        hFile,
        0,
        &dwThreadId );

    HANDLE ah[] = {hReadThread, hWriteThread};
    WaitForMultipleObjects(2, ah, TRUE, INFINITE );

    CloseHandle( hReadThread );
    CloseHandle( hWriteThread );
    CloseHandle( hFile );

    return 1;
}

/*
*  Open a dynamic channel with the name given in szChannelName.
*  The output file handle can be used in ReadFile/WriteFile calls.
*/
DWORD OpenDynamicChannel(
    LPCSTR szChannelName, 
    HANDLE *phFile )
{
    HANDLE hWTSHandle = NULL;
    HANDLE hWTSFileHandle;
    PVOID vcFileHandlePtr = NULL;
    DWORD len;
    DWORD rc = ERROR_SUCCESS;

    hWTSHandle = WTSVirtualChannelOpenEx(
        WTS_CURRENT_SESSION,
        (LPSTR)szChannelName,
        WTS_CHANNEL_OPTION_DYNAMIC );
    if ( NULL == hWTSHandle )
    {
        rc = GetLastError();
        goto exitpt;
    }

    BOOL fSucc = WTSVirtualChannelQuery(
        hWTSHandle,
        WTSVirtualFileHandle,
        &vcFileHandlePtr,
        &len );
    if ( !fSucc )
    {
        rc = GetLastError();
        goto exitpt;
    }
    if ( len != sizeof( HANDLE ))
    {
        rc = ERROR_INVALID_PARAMETER;
        goto exitpt;
    }

    hWTSFileHandle = *(HANDLE *)vcFileHandlePtr;

    fSucc = DuplicateHandle(
        GetCurrentProcess(),
        hWTSFileHandle,
        GetCurrentProcess(),
        phFile,
        0,
        FALSE,
        DUPLICATE_SAME_ACCESS );
    if ( !fSucc )
    {
        rc = GetLastError();
        goto exitpt;
    }

    rc = ERROR_SUCCESS;

exitpt:
    if ( vcFileHandlePtr )
    {
        WTSFreeMemory( vcFileHandlePtr );
    }
    if ( hWTSHandle )
    {
        WTSVirtualChannelClose( hWTSHandle );
    }

    return rc;
}

/* 
*  Write a series of random messages into the dynamic virtual channel.
*/
DWORD WINAPI WriteThread(PVOID param)
{
    HANDLE  hFile;
    BYTE    WriteBuffer[MAX_MSG_SIZE];
    DWORD   dwWritten;
    BOOL    fSucc;
    BYTE    b = 0;
    HANDLE  hEvent;

    hFile = (HANDLE)param;

    hEvent = CreateEvent( NULL, FALSE, FALSE, NULL );

    for( ULONG msgSize = START_MSG_SIZE; 
        msgSize < MAX_MSG_SIZE; 
        msgSize += STEP_MSG_SIZE )
    {
        OVERLAPPED  Overlapped = {0};
        Overlapped.hEvent = hEvent;

        for( ULONG i = 0; i < msgSize; i++, b++ )
        {
            WriteBuffer[i] = b;
        }

        fSucc = WriteFile(
            hFile,
            WriteBuffer,
            msgSize,
            &dwWritten,
            &Overlapped );
        if ( !fSucc )
        {
            if ( GetLastError() == ERROR_IO_PENDING )
            {
                DWORD dw = WaitForSingleObject( Overlapped.hEvent, _MAX_WAIT );
                _ASSERT( WAIT_OBJECT_0 == dw );
                fSucc = GetOverlappedResult(
                    hFile,
                    &Overlapped,
                    &dwWritten,
                    FALSE );
            }
        }

        if ( !fSucc )
        {
            DWORD error = GetLastError();
            return error;
        }

        _ASSERT( dwWritten == msgSize );
    }

    return 0;
}

/* 
*  Read the data from the dynamic virtual channel reconstruct the original 
*  message and verify its content.
*/
DWORD WINAPI ReadThread(PVOID param)
{
    HANDLE hFile;
    BYTE ReadBuffer[CHANNEL_PDU_LENGTH];
    DWORD dwRead;
    BYTE b = 0;
    CHANNEL_PDU_HEADER *pHdr;
    BOOL fSucc;
    HANDLE hEvent;

    hFile = (HANDLE)param;
    pHdr = (CHANNEL_PDU_HEADER*)ReadBuffer;

    hEvent = CreateEvent( NULL, FALSE, FALSE, NULL );

    for( ULONG msgSize = START_MSG_SIZE; 
        msgSize < MAX_MSG_SIZE; 
        msgSize += STEP_MSG_SIZE )
    {
        OVERLAPPED  Overlapped = {0};
        DWORD TotalRead = 0;
        do {
            Overlapped.hEvent = hEvent;
            
            // Read the entire message.
            fSucc = ReadFile(
                hFile,
                ReadBuffer,
                sizeof( ReadBuffer ),
                &dwRead,
                &Overlapped );
            if ( !fSucc )
            {
                if ( GetLastError() == ERROR_IO_PENDING )
                {
                    DWORD dw = WaitForSingleObject( Overlapped.hEvent, INFINITE );
                    _ASSERT( WAIT_OBJECT_0 == dw );
                    fSucc = GetOverlappedResult(
                        hFile,
                        &Overlapped,
                        &dwRead,
                        FALSE );
                }
            }

            if ( !fSucc )
            {
                DWORD error = GetLastError();
                return error;
            }

            ULONG packetSize = dwRead - sizeof( *pHdr );
            TotalRead += packetSize;
            PBYTE pData = (PBYTE)( pHdr + 1 );
            for ( ULONG i = 0; i < packetSize; pData++, i++, b++ )
            {
                _ASSERT( *pData == b );
            }

            _ASSERT( msgSize == pHdr->length );

        } while( 0 == ( pHdr->flags & CHANNEL_FLAG_LAST ));

        _ASSERT( TotalRead == msgSize );
    }

    return 0;
}

```



 

 




