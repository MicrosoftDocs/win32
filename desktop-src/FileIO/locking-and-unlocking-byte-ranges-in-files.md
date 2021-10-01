---
description: Example code that shows byte range locking and unlocking by using the LockFileEx and UnlockFileEx functions.
ms.assetid: 9d54fe11-b1ad-4723-a42a-00bc6dc64072
title: Locking and Unlocking Byte Ranges in Files
ms.topic: article
ms.date: 05/31/2018
---

# Locking and Unlocking Byte Ranges in Files

Although the system allows more than one application to open a file and write to it, applications must not write over each other's work. An application can prevent this problem by temporarily locking a byte range in a file.

The [**LockFile**](/windows/desktop/api/FileAPI/nf-fileapi-lockfile) and [**LockFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-lockfileex) functions lock a specified range of bytes in a file. The range may extend beyond the current end of the file. Locking part of a file gives the threads of the locking processes exclusive access to the specified byte range by using the specified file handle. Attempts to access a byte range that is locked by another process always fail. If the locking process attempts to access a locked byte range through a second file handle, the attempt fails.

> [!Note]  
> Byte range locks are ignored when using memory mapped files.

 

The [**LockFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-lockfileex) function allows an application to specify one of two types of locks. An *exclusive lock* denies all other processes both read and write access to the specified byte range of a file. A *shared lock* denies all processes write access to the specified byte range of a file, including the process that first locks the byte range. This can be used to create a read-only byte range in a file.

An application unlocks the byte range by using the [**UnlockFile**](/windows/desktop/api/FileAPI/nf-fileapi-unlockfile) or [**UnlockFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-unlockfileex) function and should unlock all locked areas before closing a file.

For an example of using [**LockFile**](/windows/desktop/api/FileAPI/nf-fileapi-lockfile), see [Appending One File to Another File](appending-one-file-to-another-file.md).

The following examples show how to use [**LockFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-lockfileex). The first example is a simple demonstration to create a file, write some data to it, and then lock a section in the middle.

**Note**  This example does not change the data after the file is locked.


```C++
// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
// PARTICULAR PURPOSE.
//
// Copyright (C) Microsoft. All rights reserved

#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

#define NUMWRITES 10
#define TESTSTRLEN 11

const char TestData[NUMWRITES][TESTSTRLEN] = 
{ 
    "TestData0\n",
    "TestData1\n",
    "TestData2\n",
    "TestData3\n",
    "TestData4\n",
    "TestData5\n",
    "TestData6\n",
    "TestData7\n",
    "TestData8\n",
    "TestData9\n"
};

int main(int argc, char *argv[])
{
    BOOL fSuccess = FALSE;

    // Create the file, open for both read and write.
    HANDLE hFile = CreateFile(TEXT("datafile.txt"),
                       GENERIC_READ | GENERIC_WRITE,
                       0,          // open with exclusive access
                       NULL,       // no security attributes
                       CREATE_NEW, // creating a new temp file
                       0,          // not overlapped index/O
                       NULL);
    
    if (hFile == INVALID_HANDLE_VALUE) 
    {
        // Handle the error.
        printf("CreateFile failed (%d)\n", GetLastError());
        return (1);
    }

    // Write some data to the file.
    DWORD dwNumBytesWritten = 0;

    for (int i=0; i<NUMWRITES; i++)
    {
        fSuccess = WriteFile(hFile,
                             TestData[i],
                             TESTSTRLEN,
                             &dwNumBytesWritten,
                             NULL);  // sync operation.
        if (!fSuccess) 
        {
           // Handle the error.
           printf("WriteFile failed (%d)\n", GetLastError());
           return (2);
        }
    } 

    FlushFileBuffers(hFile);

    // Lock the 4th write-section.  
    // First, set up the Overlapped structure with the file offset 
    // required by LockFileEx, three lines in to the file.
    OVERLAPPED sOverlapped;
    sOverlapped.Offset = TESTSTRLEN * 3;
    sOverlapped.OffsetHigh = 0;

    // Actually lock the file.  Specify exclusive access, and fail 
    // immediately if the lock cannot be obtained.
    fSuccess = LockFileEx(hFile,         // exclusive access, 
                          LOCKFILE_EXCLUSIVE_LOCK | 
                          LOCKFILE_FAIL_IMMEDIATELY,
                          0,             // reserved, must be zero
                          TESTSTRLEN,    // number of bytes to lock
                          0,
                          &sOverlapped); // contains the file offset
    if (!fSuccess) 
    {
       // Handle the error.
       printf ("LockFileEx failed (%d)\n", GetLastError());
       return (3);
    }
    else printf("LockFileEx succeeded\n");

    /////////////////////////////////////////////////////////////////
    // Add code that does something interesting to locked section,  /
    // which should be line 4                                       /
    /////////////////////////////////////////////////////////////////

    // Unlock the file.
    fSuccess = UnlockFileEx(hFile, 
                            0,             // reserved, must be zero
                            TESTSTRLEN,    // num. of bytes to unlock
                            0,
                            &sOverlapped); // contains the file offset
    if (!fSuccess) 
    {
       // Handle the error.
       printf ("UnlockFileEx failed (%d)\n", GetLastError());
       return (4);
    }
    else printf("UnlockFileEx succeeded\n");

    // Clean up handles, memory, and the created file.
    fSuccess = CloseHandle(hFile);
    if (!fSuccess) 
    {
       // Handle the error.
       printf ("CloseHandle failed (%d)\n", GetLastError());
       return (5);
    }

    fSuccess = DeleteFile(TEXT("datafile.txt"));
    if (!fSuccess) 
    {
        // Handle the error.
       printf ("DeleteFile failed (%d)\n", GetLastError());
       return (6);
    }
    return (0);
}
```



The following example is an advanced demonstration of byte range locking, using multiple threads and a simple database performing random operations on a single data file. For more information, see the embedded code comments and the section following the sample code.


```C++
// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
// PARTICULAR PURPOSE.
//
// Copyright (C) Microsoft. All rights reserved

#define UNICODE
#define _CRT_RAND_S
#include <stdlib.h>
#include <windows.h>

#include <stdio.h>

#include <malloc.h>
#include <conio.h>
#include <process.h>
#include <winioctl.h>

#define RECORD_SIZE 0x300
#define NUM_RECORDS 0x1000
#define NUM_THREADS 8

#define NUM_FILEOPS 500

#define BITMAP_SIZE ((NUM_RECORDS) / 8)
#define DATA_SIZE   ((RECORD_SIZE) - sizeof(RECORD_HEADER))

#define MSG_PRINTF(S,...) wprintf(L"[THREAD_ID %d] " S, \
    GetCurrentThreadId(), \
    __VA_ARGS__)

#if defined BRLS_DEBUG

#define DBG_PRINTF(S,...) wprintf(L"[THREAD_ID %d] " S, \
    GetCurrentThreadId(), \
    __VA_ARGS__)

#else

#define DBG_PRINTF(...)
#define PrintBitmap(...)

#endif


#define MASTER_RECORD_TYPE_CODE 'rtsM'
#define DATA_RECORD_TYPE_CODE   'ataD'


//
//  Record type definitions.
//
typedef struct _RECORD_HEADER {
    ULONG TypeCode;     // Either MASTER_RECORD_TYPE_CODE or DATA_RECORD_TYPE_CODE.
    ULONG SeqNumber;    // Starts at 1 and is incremented every time contents are modified.
} RECORD_HEADER;

typedef struct _MASTER_RECORD {
    RECORD_HEADER Header;
    BYTE Bitmap[BITMAP_SIZE];  // A bitmap indicating which records are allocated.
} MASTER_RECORD;

typedef struct _DATA_RECORD {
    RECORD_HEADER Header;
    BYTE Data[DATA_SIZE];       // Record raw data.
} DATA_RECORD;


//
//  Types of I/O for IoRecord.
//
typedef enum {
    IoRead,
    IoWrite,
    IoLock,
    IoUnlock
} IO_TYPE;


//
//  Types of operations for OperateOnRecord.
//
typedef enum {
    CreateRecord = 0,
    DeleteRecord,
    ModifyRecord,
    MaxOprRecord
} OPERATION;


//
//  Parameter block for I/Os passed to IoRecord.
//
typedef struct _IO_PARAM {
    IO_TYPE Type;
    union _IO_PARAM_PARAMS {
        struct {
            PVOID Data;
            ULONG RecSize;
        } IoInfo;
        struct {
            BOOL Exclusive;
        } LockInfo ;
    } Params;
} IO_PARAM, *PIO_PARAM;

void ErrorExitThread()
//
//  This function is called immediately after an unrecoverable error is logged.
//
{
    MSG_PRINTF(L"An error has been logged, calling ExitThread.\n");
    ExitThread(1);
}

BOOL IoRecord(HANDLE hFile, ULONG RecNumber, PIO_PARAM pIoParam)
//
//  This function performs I/O (read, write, lock or unlock) in a record, according
//  to the parameters passed in the IO_PARAM block.
//
//  Arguments:
//      hFile       - Handle to the file containing the records.
//      RecNumber   - Number of the record to be operated on.
//      pIoParam    - Pointer to IO_PARAM structure.
//
//  Return value:
//      TRUE if the I/O succeeded, FALSE if not.
//
{
    OVERLAPPED Overlapped;
    BOOL Result;
    ULARGE_INTEGER RecOffset;
    DWORD NumBytes;

    //  Initialize Overlapped.
    SecureZeroMemory(&Overlapped, sizeof(OVERLAPPED));
    Overlapped.hEvent = CreateEvent(NULL,
        FALSE,
        FALSE,
        NULL);

    if (NULL == Overlapped.hEvent) 
    {
        MSG_PRINTF(L"CreateEvent for Overlapped.hEvent failed with error 0x%08x.\n", 
            GetLastError());
        ErrorExitThread();
    }

    //  Calculate record position.
    RecOffset.QuadPart = RecNumber * RECORD_SIZE;

    Overlapped.Offset     = RecOffset.LowPart;
    Overlapped.OffsetHigh = RecOffset.HighPart;

    //  Issue the operation.
    switch (pIoParam->Type) 
    {
    case IoLock:
        Result = LockFileEx(hFile,
            pIoParam->Params.LockInfo.Exclusive ? LOCKFILE_EXCLUSIVE_LOCK : 0,
            0,
            RECORD_SIZE,
            0,
            &Overlapped);
        break;
    case IoUnlock:
        Result = UnlockFileEx(hFile,
            0,
            RECORD_SIZE,
            0,
            &Overlapped);
        break;
    case IoRead:
        Result = ReadFile(hFile,
            pIoParam->Params.IoInfo.Data,
            pIoParam->Params.IoInfo.RecSize,
            NULL,
            &Overlapped);
        break;
    case IoWrite:
        Result = WriteFile(hFile,
            pIoParam->Params.IoInfo.Data,
            pIoParam->Params.IoInfo.RecSize,
            NULL,
            &Overlapped);
        break;
    default:
        Result = FALSE;
        break;
    }

    if (!Result) 
    {
        if (GetLastError() == ERROR_IO_PENDING) 
        {
            //  Wait until the operation finishes.
            if (GetOverlappedResult(hFile,
                &Overlapped,
                &NumBytes,
                TRUE) == FALSE) 
            {
                MSG_PRINTF(L"GetOverlappedResult for Overlapped.hEvent failed with error 0x%08x.\n", 
                    GetLastError());
                ErrorExitThread();
            }
            Result = TRUE;
        } else {
            MSG_PRINTF(L"IoRecord failed with error 0x%08x. Failure passed to caller.\n", 
                GetLastError());
        }
    }
    CloseHandle(Overlapped.hEvent);
    return Result;
}


//
//  The following functions are wrappers around IoRecord, they just set the correct
//  parameters in the IO_PARAM block to correspond to the requested operation and
//  pass that to IoRecord.
//
BOOL ReadRecord(HANDLE hFile, ULONG RecNumber, PVOID Record, ULONG RecSize)
{
    IO_PARAM IoParam;

    IoParam.Type                  = IoRead;
    IoParam.Params.IoInfo.Data    = Record;
    IoParam.Params.IoInfo.RecSize = RecSize;

    return IoRecord(hFile, RecNumber, &IoParam);
}


BOOL WriteRecord(HANDLE hFile, ULONG RecNumber, PVOID Record, ULONG RecSize)
{
    IO_PARAM IoParam;

    IoParam.Type                  = IoWrite;
    IoParam.Params.IoInfo.Data    = Record;
    IoParam.Params.IoInfo.RecSize = RecSize;

    return IoRecord(hFile, RecNumber, &IoParam);
}


BOOL LockRecord(HANDLE hFile, ULONG RecNumber, BOOL Exclusive)
{
    IO_PARAM IoParam;

    IoParam.Type                      = IoLock;
    IoParam.Params.LockInfo.Exclusive = Exclusive;

    return IoRecord(hFile, RecNumber, &IoParam);
}


BOOL UnlockRecord(HANDLE hFile, ULONG RecNumber)
{
    IO_PARAM IoParam;

    IoParam.Type = IoUnlock;

    return IoRecord(hFile, RecNumber, &IoParam);
}


ULONG ReserveFirstFreeRecord(BYTE* Bitmap)
//
//  This function iterates through the bitmap and reserves the first free record
//  it can find in the bitmap.
//
//  Arguments:
//      Bitmap  - Pointer to the bitmap.
//
//  Return value:
//      Either zero, if there are no free records, or the position of the record
//      that was just reserved.
//          
{
    int i;
    BYTE Bit = 1;

    for (i = 0; i < NUM_RECORDS; i++) 
    {
        if (Bitmap[i / 8] & Bit) 
        {
            Bit <<= 1;
            if (Bit == 0) { Bit = 1; }
        } else {
            Bitmap[i / 8] |= Bit;
            return i;
        }
    }

    return 0;
}


BOOL TestBit(BYTE* Bitmap, ULONG Bit)
//
//  This function tests if a given bit is set in the bitmap.
//
//  Arguments:
//      Bitmap  - Pointer to the bitmap.
//      Bit     - Position of the bit in the bitmap.
//
//  Return value:
//      TRUE if the bit is set, FALSE otherwise.
//
{
    ULONG Byte = Bit / 8;

    Bit = Bit % 8;

    return (BOOL)(Bitmap[Byte] & (1 << Bit));
}


void ClearBit(BYTE* Bitmap, ULONG Bit)
//
//  This function clears a given bit in the bitmap.
//
//  Arguments:
//      Bitmap  - Pointer to the bitmap.
//      Bit     - Position of the bit in the bitmap.
//
{
    ULONG Byte = Bit / 8;

    Bit = Bit % 8;

    Bitmap[Byte] &= ~(1 << Bit);
}


#ifdef BRLS_DEBUG
void PrintBitmap(BYTE* Bitmap)
//
//   This function prints the whole bitmap, for debugging purposes.
//
//   Arguments:
//      Bitmap  - Pointer to the bitmap.
//
{
    int i;

    for (i = 0; i < BITMAP_SIZE; i++) 
    {
        wprintf(L"%1x", Bitmap[i]);
    }

    wprintf(L"\n");
}
#endif


void InitRecord(RECORD_HEADER* Record, BOOL Master, ULONG SeqNumber)
//
//  This function initializes a in-memory record structure with the correct
//  type code and sequence number. In case of the Master Record, the bitmap
//  is initialized too.
//
//  Arguments:
//      Record      - Pointer to the record structure.
//      Master      - TRUE if this is a Master Record, FALSE otherwise.
//      SeqNumber   - Initial sequence number.
//
{
    ULONG RecSize   = Master ? sizeof(MASTER_RECORD)   : sizeof(DATA_RECORD);
    ULONG TypeCode  = Master ? MASTER_RECORD_TYPE_CODE : DATA_RECORD_TYPE_CODE;

    SecureZeroMemory(Record, RecSize);

    Record->TypeCode  = TypeCode;
    Record->SeqNumber = Master ? 0 : SeqNumber;

    if (Master) 
    {
        ((MASTER_RECORD*)Record)->Bitmap[0] = 1;
    }
}


DATA_RECORD* PrepareRecord(ULONG SeqNumber)
//
//  This function allocates a new in-memory record structure and initializes it
//  as a brand new data record.
//
//  Arguments:
//      SeqNumber   - Sequence number with which to initialize the record.
//
//  Return value:
//      Pointer to the record structure.
//
{
    DATA_RECORD* Record = NULL;

    Record = (DATA_RECORD*) malloc(sizeof(DATA_RECORD));

    if (Record == NULL) 
    {
        MSG_PRINTF(L"Critical error: malloc for CreateRecord failed.\n");
        ErrorExitThread();
    }

    InitRecord((RECORD_HEADER*)Record, FALSE, SeqNumber);

    return Record;
}


void WriteData(DATA_RECORD* Record)
//
//  This function fills a in-memory data record structure with random data.
//  Errors do not interrupt execution.
//
//  Arguments:
//      Record  - Pointer to the record structure.
//
{
    PUINT iData;
    int i;
    errno_t err;

    iData = (PUINT)Record->Data;

    for (i = 0; i < DATA_SIZE; i += sizeof(ULONG), iData++) 
    {
        err = rand_s(iData);
        if (err != 0) 
        {
            MSG_PRINTF(L"rand_s for WriteData failed with error 0x%08x, continuing execution.\n", 
                err);
        }
    }
}


BOOL OperateOnRecord(HANDLE hFile, PULONG RecNumber, OPERATION Operation)
//
//  This function executes a high-level operation in a record (create, modify or delete).
//
//  Arguments:
//      hFile       - Handle to the file containing the record to be operated on.
//      RecNumber   - Pointer to a ULONG that either will receive the number of the
//                    record created by this operation or just contains the number
//                    of the record that will be modified or deleted.
//      Operation   - Operation to be performed (CreateRecord, ModifyRecord or
//                    DeleteRecord).
//
//  Return value:
//      TRUE if the operation succeeded, FALSE otherwise.
//
{
    BOOL Result;
    BOOL Exists;
    BOOL ExclusiveLock;
    MASTER_RECORD MasterRecord;
    DATA_RECORD*  Record;

    //  Fail operations on Master Record.
    if ((Operation != CreateRecord) && (*RecNumber == 0)) 
    {
        MSG_PRINTF(L"Cannot operate on Master Record.\n");
        return FALSE;
    }

    //  Lock Master Record. If we're just modifying a record, we can get a
    //  shared lock.
    ExclusiveLock = (Operation != ModifyRecord);

    Result = LockRecord(hFile, 0, ExclusiveLock);
    if (!Result) 
    {
        MSG_PRINTF(L"LockRecord (MasterRecord) for OperateOnRecord failed with error 0x%08x.\n", 
            GetLastError());
        ErrorExitThread();
    }

    //  Read in Master Record.
    Result = ReadRecord(hFile, 0, (PVOID)&MasterRecord, sizeof(MASTER_RECORD));
    if (!Result) 
    {
        MSG_PRINTF(L"ReadRecord (MasterRecord) for OperateOnRecord failed with error 0x%08x.\n", 
            GetLastError());
        ErrorExitThread();
    }

    if (MasterRecord.Header.TypeCode != MASTER_RECORD_TYPE_CODE) 
    {
        MSG_PRINTF(L"Master Record corruption error: wrong typecode!\n");
        ErrorExitThread();
    }

    DBG_PRINTF(L"MasterRecord bitmap (before): ");
    PrintBitmap(MasterRecord.Bitmap);

    if (Operation != CreateRecord) 
    {
        //  Test the bit in the bitmap corresponding to this record.
        Exists = TestBit(MasterRecord.Bitmap, *RecNumber);

        //  Clear the bit if we are deleting the record.
        if ((Operation == DeleteRecord) && Exists) 
        {
            ClearBit(MasterRecord.Bitmap, *RecNumber);
        }

    } else {

        //  Reserve the first free record.
        *RecNumber = ReserveFirstFreeRecord(MasterRecord.Bitmap);

        if (*RecNumber != 0) 
        {
            Exists = TRUE;
        } else {
            Exists = FALSE;
            MSG_PRINTF(L"File is full!\n");
        }
    }

    DBG_PRINTF(L"MasterRecord bitmap (after): ");
    PrintBitmap(MasterRecord.Bitmap);

    if ((Operation != ModifyRecord) && Exists) 
    {
        //  Update the Master Record's sequence number.
        MasterRecord.Header.SeqNumber++;

        //  Write Master Record down.
        Result = WriteRecord(hFile, 0, (PVOID)&MasterRecord, sizeof(MASTER_RECORD));
        if (!Result) 
        {
            MSG_PRINTF(L"WriteRecord (MasterRecord) for CreateRecord failed with error 0x%08x.\n", 
                GetLastError());
            ErrorExitThread();
        }
    }

    //  Unlock Master Record.
    Result = UnlockRecord(hFile, 0);
    if (!Result) 
    {
        MSG_PRINTF(L"UnlockRecord (MasterRecord) for OperateOnRecord failed with error 0x%08x.\n", 
            GetLastError());
        ErrorExitThread();
    }

    if (!Exists) 
    {
        if (*RecNumber != 0) 
        {
            MSG_PRINTF(L"Record %d not present!\n", *RecNumber);
        }
        return FALSE;
    }

    //  For record deletion, processing is done and skip to write.
    //  Otherwise, there is more to do.
    if (Operation != DeleteRecord) 
    {
        //  Prepare a new record in memory.
        Record = PrepareRecord(1);

        //  Lock the record exclusively.
        Result = LockRecord(hFile, *RecNumber, TRUE);
        if (!Result) 
        {
            MSG_PRINTF(L"LockRecord for ModifyRecord failed with error 0x%08x.\n", 
                GetLastError());
            ErrorExitThread();
        }

        if (Operation == ModifyRecord) 
        {
            //  Read the record in from the file if we're modifying it.
            Result = ReadRecord(hFile, *RecNumber, Record, RECORD_SIZE);
            if (!Result) 
            {
                MSG_PRINTF(L"ReadRecord for ModifyRecord failed with error 0x%08x.\n", 
                    GetLastError());
                ErrorExitThread();
            }

            //  Update record sequence number.
            Record->Header.SeqNumber++;
        }

        //  Write to the in-memory record.
        WriteData(Record);

        //  Write the record to the file.
        Result = WriteRecord(hFile, *RecNumber, Record, RECORD_SIZE);
        if (!Result) 
        {
            MSG_PRINTF(L"WriteRecord for ModifyRecord failed with error 0x%08x.\n", 
                GetLastError());
            ErrorExitThread();
        }

        //  Unlock the record.
        Result = UnlockRecord(hFile, *RecNumber);
        if (!Result) 
        {
            MSG_PRINTF(L"UnlockRecord for ModifyRecord failed with error 0x%08x.\n", 
                GetLastError());
            ErrorExitThread();
        }

        //  Free the record structure.
        free(Record);
    }

    return TRUE;
}


ULONG RandomOption(ULONG NumOpts)
//
//  This function returns a random number between 0 and (NumOpts - 1).
//  It basically is a random option select.
//
//  Arguments:
//      NumOpts - Number of options to choose from.
//
//  Return value:
//      A random option (random ULONG x | 0 <= x < NumOpts).
//
{
    UINT Random;
    errno_t err;

    err = rand_s(&Random);
    if (err != 0) 
    {
        MSG_PRINTF(L"rand_s for RandomOption failed with error 0x%08x\n", 
            err);
    }

    return Random % NumOpts;
}


DWORD WINAPI WorkerThread(PVOID data)
//
//  This is the tight loop executed by each of the threads operating in the file.
//  Each thread has its own handle to the same file. After obtaining that handle,
//  they go into a tight loop in which a record number and a record operation are
//  chosen at random and that operation is then performed in that record.
//
//  Arguments:
//      Data    - PVOID to a string containing the file name (so it can be opened).
//
//  Return value:
//      It should not return.
//
{
    HANDLE hFile;
    LPCWSTR FileName = (LPCWSTR)data;
    ULONG RecNumber;
    OPERATION Operation;
    BOOL Result;

    UINT i;

    hFile = CreateFile(FileName,
        GENERIC_READ | GENERIC_WRITE,
        FILE_SHARE_READ | FILE_SHARE_WRITE,
        NULL,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL | FILE_FLAG_OVERLAPPED,
        NULL);

    if (hFile == INVALID_HANDLE_VALUE) 
    {
        MSG_PRINTF(L"CreateFile failed with error 0x%08x.\n", 
            GetLastError());
        ErrorExitThread();
    }

    //  Main loop for doing the random operations.
    for (i = 0; i < NUM_FILEOPS; i++) 
    {
        RecNumber = RandomOption(NUM_RECORDS);
        Operation = (OPERATION)RandomOption(MaxOprRecord);

        //  Output message as to what action is being attempted.
        switch (Operation) 
        {
        case CreateRecord:
            MSG_PRINTF(L"attempting record creation.\n");
            break;
        case ModifyRecord:
            MSG_PRINTF(L"attempting modification of record %d.\n", RecNumber);
            break;
        case DeleteRecord:
            MSG_PRINTF(L"attempting deletion of record %d.\n", RecNumber);
            break;
        }

        //  Perform the actual operation and handle the result, 
        //  then loop again until done.
        Result = OperateOnRecord(hFile, &RecNumber, Operation);

        if (Result) 
        {
            switch (Operation) 
            {
            case CreateRecord:
                MSG_PRINTF(L"created record %d.\n", RecNumber);
                break;

            case ModifyRecord:
                MSG_PRINTF(L"modified record %d.\n", RecNumber);
                break;

            case DeleteRecord:
                MSG_PRINTF(L"deleted record %d.\n", RecNumber);
                break;
            }
        }
    }

    CloseHandle(hFile);
    MSG_PRINTF(L"%d file operations complete. Exiting thread.\n", i);

    return 0;
}


BOOL InitNewFile(LPCWSTR FileName)
//
//  This function initializes a file with records. If the file already exists, it
//  just returns, assuming it has a valid Master Record on it. If it does not 
//  exist, a brand new file is created and initialized with a clean Master Record.
//
//  Arguments:
//      FileName    - Name of the file to be initialized.
//
//  Return value:
//      TRUE if the initialization succeeded, FALSE otherwise.
//      
{
    HANDLE hFile;
    MASTER_RECORD MasterRecord;
    DWORD BytesWritten;
    DWORD Result;

    //
    //  Create the file or open existing.
    //
    hFile = CreateFile(FileName,
        GENERIC_READ | GENERIC_WRITE,
        FILE_SHARE_READ | FILE_SHARE_WRITE,
        NULL,
        OPEN_ALWAYS,
        FILE_ATTRIBUTE_NORMAL,
        NULL);

    if (INVALID_HANDLE_VALUE == hFile) 
    {
        MSG_PRINTF(L"CreateFile failed with error 0x%08x.\n", 
            GetLastError());
        return FALSE;
    } 
    else if (ERROR_ALREADY_EXISTS == GetLastError()) 
    {
        //  This is ok, simply assume it's a valid file.
        //  Note that this does not actually test that the file
        //  is valid for this application. That error is caught later.
        CloseHandle(hFile);
        return TRUE;
    } //  The implied "else" is that the handle is a good one.


    InitRecord((RECORD_HEADER*)&MasterRecord, TRUE, 0);

    Result = WriteFile(hFile,
        &MasterRecord,
        sizeof(MASTER_RECORD),
        &BytesWritten,
        NULL);

    if (!Result) 
    {
        MSG_PRINTF(L"WriteFile failed with error 0x%08x.\n", 
            GetLastError());
    }

    CloseHandle(hFile);

    return Result;
}


int __cdecl wmain(int argc, LPCWSTR argv[])
//
//  Main function. Reads file name from command line argument, initializes the file
//  and starts the worker threads, waiting for them to return.
//
{
    HANDLE gThread[NUM_THREADS];

    DWORD IdThread;
    DWORD ResultCode;
    LPCWSTR FileName = NULL;

    if (argc != 2) {
        wprintf(L"Invalid number of arguments!\n");
        wprintf(L"Usage: %ws file_name\n", argv[0]);
        return -1;
    }

    FileName = argv[1];

    if (!InitNewFile(FileName))
    {
        wprintf(L"Unable to initialize the data file %ws.\n", FileName);
    }

    wprintf(L"Main thread creating %d worker threads for processing.\n", 
        NUM_THREADS);
    for (int i = 0; i < NUM_THREADS; i++) 
    {
        gThread[i] = CreateThread(NULL,
            0,
            (LPTHREAD_START_ROUTINE)WorkerThread,
            (PVOID)FileName,
            0,
            &IdThread);
    }

    wprintf(L"Main thread waiting for worker threads to exit...\n");

    ResultCode = WaitForMultipleObjects(
        NUM_THREADS,
        gThread,
        TRUE,
        INFINITE);

    wprintf(L"WaitForMultipleObjects returned 0x%08x, execution complete.\n",
        ResultCode);

    // Do some clean-up.
    for (int i = 0; i < NUM_THREADS; i++) 
    {
        CloseHandle(gThread[i]);
    }

    return 0;
}
```



This sample is a Windows console application that executes multiple concurrent accesses to a file, all coordinated by byte range locks using a simple database, composed of several records of a fixed size. Note that true concurrence depends on how many processor cores exist on the host system.

All records have the first two fields in common: a type code and a sequence number. The type code is one of two codes: The "Mstr" code refers to the **MASTER\_RECORD** type, and the "Data" code refers to a **DATA\_RECORD** type. There can be only one **MASTER\_RECORD** and zero or more **DATA\_RECORD**s. For this example, data contained in the data records is randomly generated. The second field, the sequence number, is incremented every time a record is modified.

When execution begins, if the data file does not already exist, it is created and initialized by the **InitNewFile** function. The **InitNewFile** function writes a record of type Master with an empty bitmap at the beginning. If the file already exists, it is opened; it is assumed to have a valid Master record at the beginning.

After the file is either successfully created or successfully opened, multiple worker threads are started, and all of them run a loop in which an operation and a record are chosen at random and then that operation is attempted on that record. Because these operations are random, not all of them succeed, but are not necessarily errors. Appropriate status information is logged to the console.

The possible operations are as follows: creation of a new record, modification of an existing record, or deletion of an existing record. The creation operation looks at the bitmap to find the first free record and allocates that record as the new record. The modification operation reads the bitmap to see whether that record actually exists and, if so, modifies that record. The deletion operation clears the bit in the bitmap corresponding to the record, freeing the space that record occupied for future allocation. Further, these operations are split in two parts: access to the MasterRecord, where the metadata is stored, and access to the data record itself.

Because they write data to the data records, the record creation and record modification operations are the only ones that require data record access. For that reason, the region covered by the record is locked exclusively prior to the operation being performed. The creation and deletion operations modify the bitmap, so they need to lock the Master record exclusively. However, record modification operations only need to read the bitmap, not write to it, in order to verify whether the file exists. For that operation, the Master record needs only a shared byte range lock.

Exclusive byte range locks prevent both read and write access from all other handles to the file, and that's the reason why they are used when writing to a record. On the other hand, a shared byte range lock prevents write access from all handles, including the handle owning the lock, but allows read access from all of them.

To demonstrate the use of byte range locks with the file, all I/O in this sample, other than new file initialization, is done via an asynchronous file handle. This can be seen in the **IoRecord** function in the **IoLock** and **IoUnlock** cases within the switch statement. The [**LockFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-lockfileex) and [**UnlockFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-unlockfileex) functions are used with the overlapped I/O model by passing an [**OVERLAPPED**](/windows/desktop/api/MinWinBase/ns-minwinbase-overlapped_entry) structure to them with the offset for the start of the locked range, and an event that will be signaled after the lock over that range is granted unless the function returns immediately.

After issuing the asynchronous I/O request, the next operation in the **IoRecord** function is to wait for the operation in-line. This is often a sub-optimal scenario when maximum performance is desired, and is used here for the sake of simplicity. In production applications, the use of [I/O completion ports](i-o-completion-ports.md) or similar mechanisms is preferred because it releases threads to do other processing while the I/O completes.

The sample ends after executing **NUM\_FILEOPS** random operations. Each thread will log its termination status as either an error condition or normal termination. Note that not all threads will end at the same time, depending on how many processor cores the host system has and the speed of the I/O subsystem.

 

 



