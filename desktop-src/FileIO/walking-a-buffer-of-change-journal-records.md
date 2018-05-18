---
Description: 'How to return change journal records that meet specified criteria.'
ms.assetid: '8946adb5-da47-4711-8800-86f323081c4c'
title: Walking a Buffer of Change Journal Records
---

# Walking a Buffer of Change Journal Records

The control codes that return update sequence number (USN) change journal records, [**FSCTL\_READ\_USN\_JOURNAL**](fsctl-read-usn-journal.md) and [**FSCTL\_ENUM\_USN\_DATA**](fsctl-enum-usn-data.md), return similar data in the output buffer. Both return a USN followed by zero or more change journal records, each in a [**USN\_RECORD\_V2**](usn-record-str.md) or [**USN\_RECORD\_V3**](usn-record-v3.md) structure.

The target volume for USN operations must be ReFS or NTFS 3.0 or later. To obtain the NTFS version of a volume, open a command prompt with Administrator access rights and execute the following command:

**FSUtil.exe FSInfo NTFSInfo** *X***:**

where *X* is the drive letter of the volume.

The following list identifies ways to get change journal records:

-   Use [**FSCTL\_ENUM\_USN\_DATA**](fsctl-enum-usn-data.md) to get a listing (enumeration) of all change journal records between two USNs.
-   Use [**FSCTL\_READ\_USN\_JOURNAL**](fsctl-read-usn-journal.md) to be more selective, such as selecting specific reasons for changes or returning when a file is closed.

> [!Note]  
> Both of these operations return only the subset of change journal records that meet the specified criteria.

 

The USN returned as the first item in the output buffer is the USN of the next record number to be retrieved. Use this value to continue reading records from the end boundary forward.

The **FileName** member of [**USN\_RECORD\_V2**](usn-record-str.md) or [**USN\_RECORD\_V3**](usn-record-v3.md) contains the name of the file to which the record in question applies. The file name varies in length, so **USN\_RECORD\_V2** and **USN\_RECORD\_V3** are variable length structures. Their first member, **RecordLength**, is the length of the structure (including the file name), in bytes.

When you work with the **FileName** member of [**USN\_RECORD\_V2**](usn-record-str.md) and [**USN\_RECORD\_V3**](usn-record-v3.md) structures, do not assume that the file name contains a trailing '\\0' delimiter. To determine the length of the file name, use the **FileNameLength** member.

The following example calls [**FSCTL\_READ\_USN\_JOURNAL**](fsctl-read-usn-journal.md) and walks the buffer of change journal records that the operation returns.


```C++
#include <Windows.h>
#include <WinIoCtl.h>
#include <stdio.h>

#define BUF_LEN 4096

void main()
{
   HANDLE hVol;
   CHAR Buffer[BUF_LEN];

   USN_JOURNAL_DATA JournalData;
   READ_USN_JOURNAL_DATA ReadData = {0, 0xFFFFFFFF, FALSE, 0, 0};
   PUSN_RECORD UsnRecord;  

   DWORD dwBytes;
   DWORD dwRetBytes;
   int I;

   hVol = CreateFile( TEXT("\\\\.\\c:"), 
               GENERIC_READ | GENERIC_WRITE, 
               FILE_SHARE_READ | FILE_SHARE_WRITE,
               NULL,
               OPEN_EXISTING,
               0,
               NULL);

   if( hVol == INVALID_HANDLE_VALUE )
   {
      printf("CreateFile failed (%d)\n", GetLastError());
      return;
   }

   if( !DeviceIoControl( hVol, 
          FSCTL_QUERY_USN_JOURNAL, 
          NULL,
          0,
          &amp;JournalData,
          sizeof(JournalData),
          &amp;dwBytes,
          NULL) )
   {
      printf( "Query journal failed (%d)\n", GetLastError());
      return;
   }

   ReadData.UsnJournalID = JournalData.UsnJournalID;

   printf( "Journal ID: %I64x\n", JournalData.UsnJournalID );
   printf( "FirstUsn: %I64x\n\n", JournalData.FirstUsn );

   for(I=0; I<=10; I++)
   {
      memset( Buffer, 0, BUF_LEN );

      if( !DeviceIoControl( hVol, 
            FSCTL_READ_USN_JOURNAL, 
            &amp;ReadData,
            sizeof(ReadData),
            &amp;Buffer,
            BUF_LEN,
            &amp;dwBytes,
            NULL) )
      {
         printf( "Read journal failed (%d)\n", GetLastError());
         return;
      }

      dwRetBytes = dwBytes - sizeof(USN);

      // Find the first record
      UsnRecord = (PUSN_RECORD)(((PUCHAR)Buffer) + sizeof(USN));  

      printf( "****************************************\n");

      // This loop could go on for a long time, given the current buffer size.
      while( dwRetBytes > 0 )
      {
         printf( "USN: %I64x\n", UsnRecord->Usn );
         printf("File name: %.*S\n", 
                  UsnRecord->FileNameLength/2, 
                  UsnRecord->FileName );
         printf( "Reason: %x\n", UsnRecord->Reason );
         printf( "\n" );

         dwRetBytes -= UsnRecord->RecordLength;

         // Find the next record
         UsnRecord = (PUSN_RECORD)(((PCHAR)UsnRecord) + 
                  UsnRecord->RecordLength); 
      }
      // Update starting USN for next call
      ReadData.StartUsn = *(USN *)&amp;Buffer; 
   }

   CloseHandle(hVol);

}
```



The size in bytes of any record specified by a [**USN\_RECORD\_V2**](usn-record-str.md) or [**USN\_RECORD\_V3**](usn-record-v3.md) structure is at most `((MaxComponentLength - 1) * Width) + Size` where *MaxComponentLength* is the maximum length in characters of the record file name. The width is the size of a wide character, and the *Size* is the size of the structure.

To obtain the maximum length, call the [**GetVolumeInformation**](getvolumeinformation.md) function and examine the value pointed to by the *lpMaximumComponentLength* parameter. Subtract one from *MaxComponentLength* to account for the fact that the definition of [**USN\_RECORD**](usn-record-str.md) and [**USN\_RECORD\_V3**](usn-record-v3.md) includes one character of the file name.

In the C programming language, the largest possible record size is the following:

`(MaxComponentLength - 1) * sizeof(WCHAR) + sizeof(USN_RECORD)`

 

 



