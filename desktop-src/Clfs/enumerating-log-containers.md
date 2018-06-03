---
Description: This topic shows how to enumerate log containers.
ms.assetid: dc7e204c-201d-4a84-9a87-576c73627f67
title: Enumerating Log Containers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Log Containers

This topic shows how to enumerate log containers.

## Sample Code

The following example shows how to:

1.  Open a log
2.  Retrieve the log file information
3.  Initialize the context
4.  Scan log containers


```C++
// LogInfo.cpp : Defines the entry point for the console application.
//
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <wchar.h>
#include <iostream>
#include <iomanip>
#include <clfsw32.h>
#include <Clfsmgmtw32.h>

#pragma comment(lib, "Clfsw32.lib")

using std::wcout;
using std::cout;
using std::cerr;
using std::endl;
using std::hex;
using std::dec;
using std::setw;
using std::left;

const unsigned long MAX_SCAN_CONTAINERS = 1;

void usage(wchar_t cmd[])
{
   wcout << "Usage:  " << cmd << " <LogFileName>" << endl << endl
      << "  LogFileName:  The relative or absolute path to " << endl
      << "the physical log file" << endl
      << "      NOTE: do not add the .BLF extension" << endl;
   exit(-1);
}

void ErrorExit(const char* id)
{
   DWORD errNum = GetLastError();
   cerr << "Encountered unexpected error from " << id 
      << ": " << errNum << endl;
   exit (errNum);
}

std::wostream&amp;
operator << (std::wostream&amp; ostr, const GUID &amp;g)
{ 
   ostr << "["
        << hex << g.Data1 << "-" 
        << hex << g.Data2 << "-"
        << hex << g.Data3 << "-"
        << hex << (DWORD)g.Data4 << "]" << dec << endl;
   return ostr;
}

std::wostream&amp;
operator << (std::wostream&amp; ostr, const CLFS_LSN &amp;lsn)
{
   ostr << "["   
        << LsnContainer(&amp;lsn)         << ":"
        << LsnBlockOffset(&amp;lsn)       << ":"
        << LsnRecordSequence(&amp;lsn)    << "]";
   return ostr;
}

std::wostream&amp;
operator << (std::wostream&amp; ostr, const CLFS_INFORMATION &amp;logInfo)
{
   ostr << left << setw(35) << "Total Space Available: " 
        << logInfo.TotalAvailable << endl;
   ostr << left << setw(35) << "Current Available: " 
        << logInfo.CurrentAvailable << endl;
   ostr << left << setw(35) << "Total Reserved: " 
        << logInfo.TotalReservation << endl;
   ostr << left << setw(35) << "BLF filesize: " 
        << logInfo.BaseFileSize << endl;
   ostr << left << setw(35) << "Container Size: " 
        << logInfo.ContainerSize << endl;
   ostr << left << setw(35) << "Number of containers: " 
        << logInfo.TotalContainers << endl;

   // Specifies the number of containers not in active log.
   ostr << left << setw(35) << "Number of free containers: " 
        << logInfo.FreeContainers << endl;               

   ostr << left << setw(35) << "Number of managed clients: " 
        << logInfo.TotalClients << endl;

   ostr << left << setw(35) << "Log Attributes: ";
   if (logInfo.Attributes & FILE_ATTRIBUTE_ARCHIVE) 
      ostr << "Non-Ephemeral";
   else ostr << "Ephemeral";

   if (logInfo.Attributes & FILE_ATTRIBUTE_DEDICATED)
      ostr << "; Dedicated";
   else ostr << "; Multiplexed";

   if (logInfo.Attributes & FILE_ATTRIBUTE_READONLY)
      ostr << "; ReadOnly";
   else ostr << "; Modifiable";

   if (logInfo.Attributes & FILE_ATTRIBUTE_SYSTEM)
      ostr << "; System"; // Vista

   if (logInfo.Attributes & FILE_ATTRIBUTE_HIDDEN)
      ostr << "; Hidden"; // Vista
   ostr << endl;

   ostr << left << setw(35) << "Flush threshold: " 
        << logInfo.FlushThreshold << endl;
   ostr << left << setw(35) << "Sector size: " 
        << logInfo.SectorSize << endl;
   ostr << left << setw(35) << "Archive Tail LSN: " 
        << logInfo.MinArchiveTailLsn << endl;
   ostr << left << setw(35) << "Base LSN: " << logInfo.BaseLsn 
        << endl;
   ostr << left << setw(35) << "Last flushed LSN: " 
        << logInfo.LastFlushedLsn << endl;
   ostr << left << setw(35) << "Last LSN in Active Region: " 
        << logInfo.LastLsn << endl;
   ostr << left << setw(35) << "LSN of the latest restart record: " 
        << logInfo.RestartLsn << endl;
   ostr << left << setw(35) << "Log GUID: " << logInfo.Identity;
   return ostr;
}


std::wostream&amp;
operator << (std::wostream&amp; ostr, const FILETIME* fileTime)
{
   static const int DATE_BUFSIZE = 60;
   wchar_t buffer[60];

   FILETIME localTime;
   if (!FileTimeToLocalFileTime(fileTime, &amp;localTime))
      ErrorExit("FileTimeToLocalTime");

   SYSTEMTIME sysTime;
   if (!FileTimeToSystemTime(&amp;localTime, &amp;sysTime))
      ErrorExit("FileTimeToSystemTime");

   GetDateFormat(LOCALE_USER_DEFAULT, 
                 DATE_LONGDATE, 
                 &amp;sysTime, 
                 NULL, 
                 buffer, 
                 DATE_BUFSIZE);
   ostr << buffer;
   GetTimeFormat(LOCALE_USER_DEFAULT, 
                 LOCALE_NOUSEROVERRIDE, 
                 &amp;sysTime, 
                 NULL, 
                 buffer, 
                 DATE_BUFSIZE);
   ostr << " " << buffer;
   return ostr;
}

std::wostream&amp; 
operator << (std::wostream&amp; ostr, 
             const CLFS_CONTAINER_INFORMATION &amp;cInfo) 
{  
   // File Attributes
   ostr << setw(25) << "ContainerLogicalId: " 
        << cInfo.LogicalContainerId << endl;
   ostr << setw(25) << "ContainerPhyscialId: " 
        << cInfo.PhysicalContainerId << endl;
   ostr << setw(25) << "ContainerPath: " << cInfo.FileName << endl;
   ostr << setw(25) << "ContainerSize: " << cInfo.ContainerSize 
        << endl;

   ostr << setw(25) << "CreationTime: "   
        << (FILETIME*)&amp;cInfo.CreationTime << endl;  
   ostr << setw(25) << "LastAccessTime: " << 
        (FILETIME*)&amp;cInfo.LastAccessTime << endl;  
   ostr << setw(25) << "LastWriteTime: "  
        << (FILETIME*)&amp;cInfo.LastWriteTime << endl;  

   ostr << setw(25) << "State: ";
   switch (cInfo.State) 
   {
      case ClfsContainerInitializing:               ostr 
         << "Initializing"; break;
      case ClfsContainerInactive:                   ostr 
         << "Inactive"; break;
      case ClfsContainerActive:                     ostr 
         << "Active"; break;
      case ClfsContainerActivePendingDelete:        ostr 
         << "Active Pending Delete"; break;
      case ClfsContainerPendingArchive:             ostr 
         << "Pending Archive"; break;
      case ClfsContainerPendingArchiveAndDelete:    ostr 
         << "Pending Archive and Delete"; break;
      default:                                      ostr 
         << "Unknown"; break;
   }

   return ostr;
}

int wmain(int argc, wchar_t* argv[])
{
   // Check arguments
   if (argc != 2)
      usage(argv[0]);

   // Open log file
   std::wstring logFileName = L"LOG:";
   std::wstring inputName = argv[1];
   logFileName += inputName;
   HANDLE logHndl = CreateLogFile(logFileName.c_str(), 
                                  GENERIC_READ, FILE_SHARE_READ | 
                                  FILE_SHARE_WRITE |FILE_SHARE_DELETE,
                                  NULL, 
                                  OPEN_EXISTING, 
                                  0 );

   if (logHndl == INVALID_HANDLE_VALUE)
      ErrorExit("CreateLogFile");

   // Retrieve log info
   CLFS_INFORMATION logInfo;
   ULONG infoSize = sizeof(logInfo);

   if (!GetLogFileInformation(logHndl, &amp;logInfo, &amp;infoSize))
      ErrorExit("GetLogFileInformation");

   wcout << logInfo << endl;

   // Create the container list
   // Initialize the context structures
   CLFS_SCAN_CONTEXT ctx;
   if (!CreateLogContainerScanContext(logHndl, 
                                      0, 
                                      MAX_SCAN_CONTAINERS, 
                                      CLFS_SCAN_FORWARD, 
                                      &amp;ctx, 
                                      NULL))
      if (GetLastError() != ERROR_NO_MORE_ITEMS)
         ErrorExit("CreateLogContainerScanContext");

   // The first scan was made by create
   for (unsigned int i = 0; i < ctx.cContainersReturned; ++i)
      wcout << ctx.pinfoContainer[i] << endl << endl;

   // Continue to scan
   while (GetLastError() != ERROR_NO_MORE_ITEMS) 
   {
      if (!ScanLogContainers(&amp;ctx, CLFS_SCAN_FORWARD, NULL))
      {
         if (GetLastError() != ERROR_NO_MORE_ITEMS)
            ErrorExit("ScanLogContainers");
      }

      for (unsigned int i = 0; i < ctx.cContainersReturned; ++i)
         wcout << ctx.pinfoContainer[i] << endl << endl;
   }

   return 0;
}

```



 

 



