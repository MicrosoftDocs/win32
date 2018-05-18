---
Description: 'Before you can use CLFS, you must create a log file using the CreateLogFile function.'
ms.assetid: '70d1f73b-bb39-46f8-a2fa-e68693a56082'
title: Creating a Log File
---

# Creating a Log File

Before you can use CLFS, you must create a log file using the [**CreateLogFile**](createlogfile.md) function. A log file is made up of a base log file that contains metadata, and a number of containers that hold the actual data. On any local file system, containers can be in one or more separate files; on NTFS, containers can be in one or more streams within a file.

You can create containers using the [**AddLogContainer**](addlogcontainer.md) and [**AddLogContainerSet**](addlogcontainerset.md) functions. You can also use the [CLFS Management API](common-log-file-system-management-api.md) to have CLFS create containers for you.

When you create containers, they are created using the same security attributes as the .blf file, and are created within the context of the user calling the [**AddLogContainer**](addlogcontainer.md) function, not the context of the owner of the .blf file. For more information about .blf files, see [Log Types](log-types.md).

## Log File Names

Log file names consist of the log name and an optional log stream name, depending on whether the log is dedicated or multiplexed. The following table enumerates the different ways you can specify a log file name.



| Log file name                                                               | Description                                                                                    |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| *Log***:***&lt;LogName&gt;***\[::***&lt;LogStreamName&gt;***\]**<br/> | The basic format of a log file name, including both required and optional elements.<br/> |
| *&lt;LogName&gt;*<br/>                                                | Corresponds to a valid file path on the underlying file system.<br/>                     |
| *&lt;LogStreamName&gt;*<br/>                                          | The unique name of a log stream in the log.<br/>                                         |



 

Reading the first "::" from left to right delimits the end of the log name and the start of the log stream name. For example, you can create a dedicated or multiplexed log if you specify the log names in the table above when calling the [**CreateLogFile**](createlogfile.md) function.

Dedicated logs are created by clients that specify only a log name in the *pszLogFileName* parameter of the [**CreateLogFile**](createlogfile.md) function. This function creates a base log file (.blf) on the path that is specified by the log name. The path can be either absolute or relative. For example, if you specify "log" as the value of *pszLogFileName*, the file name on the computer is "log.blf", but the name of the log for the application is "log".

When a log is created, CLFS determines whether the log is dedicated or multiplexed depending on whether a dedicated log path or a multiplexed log path is specified by the *pszLogFileName* parameter.

## Multiplex Log Design Considerations

Logs can either be dedicated or multiplexed. Dedicated logs contain one stream, and can never contain more streams. Multiplexed logs have one or more streams. You can create more streams for a multiplexed log in the future.

"Pinning a log tail" means that one log stream does not move its tail, so that all other streams within the log operate normally, write records, and move their respective tails. Eventually, because containers cannot be recycled, the log fills up and no more records can be written. Your application must ensure that when it shares a log that it only does so to users, clients, and processes that are trusted. The ACL for the log file should only include those trusted entities. For example, only allow *CompanyXAdmin* accounts to have write permissions to the log. By registering as a managed client, an application is entered into an implied contract between all consumers of a log that each consumer is a well-behaved application, and will move their respective log tails when requested to do so.

## Sample Code

The following example shows how to:

1.  Create a log file
2.  Create the initial containers
3.  Set the policy for container size
4.  Create containers according to the policy
5.  Set the policy for maximum container size


```C++
// CreateLog.cpp : Defines the entry point for the console 
// application.
//
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <wchar.h>
#include <iostream>
#include <clfsw32.h>
#include <Clfsmgmtw32.h>

#pragma comment(lib, "Clfsw32.lib")

using std::cout;
using std::wcout;
using std::cerr;
using std::endl;

const ULONG SECTOR_SIZE = 512;

void usage(wchar_t* imageName)
{

   wcout << "USAGE: " << imageName << 
      " logFileName [numContainers containerSize]" << endl;
   cout << "Create a new CLFS logfile and optionally add new " << endl
      << "containers using log policy" << endl 
      << "If the logfile already exists, you can use this " << endl
      << "utility to add containers" << endl;
   cout << "   logFileName\t:\ta relative or fully qualified" << endl 
      << " path " << endl
      << "\t\t\t\tto create the BLF file " << endl
      << "\t\t\t\t(Do not add .BLF extension)" << endl;
   cout << "   numContainers   :   Number of containers " << endl
      << "to create" << endl;
   cout << "   containerSize   :   Size of containers (in " << endl
      << "multiples of 512)" << endl 
      << "\t\t\t\tNote: ContainerSize policy ONLY works on Vista";
   exit(-1);
}

void ErrorExit(const char* id)
{
   DWORD errNum = GetLastError();
   cerr << "Encountered unexpected error from " << id << ": " << endl
      << errNum << endl;
   exit (errNum);
}


int wmain(int argc, wchar_t* argv[])
{

   if (argc < 2 || argc > 4)
      usage(argv[0]);

   // Create log file
   std::wstring logFileName = L"LOG:";
   std::wstring inputName = argv[1];
   logFileName += inputName;
   HANDLE logHndl = CreateLogFile(logFileName.c_str(), 
                                  GENERIC_WRITE | GENERIC_READ, 
                                  0, 
                                  NULL, 
                                  OPEN_ALWAYS, 
                                  0);

   if (logHndl == INVALID_HANDLE_VALUE)
      ErrorExit("CreateLogFile");
   else wcout << "Created Log " << argv[1] << ".blf" << endl; 

   if (!RegisterManageableLogClient(logHndl,0))
      ErrorExit("RegisterManageableLogClient");

   if (argc > 2) // Create containers
   {
      CLFS_MGMT_POLICY logPolicy;
      CLFS_INFORMATION logInfo;
      ULONG infoSize = sizeof(logInfo);
   
      if (!GetLogFileInformation(logHndl, &amp;logInfo, &amp;infoSize))
         ErrorExit("GetLogFileInformation");
      
      // Set new container policy size
      if (argc > 3 &amp;&amp; logInfo.TotalContainers == 0)
      {
         ULONG logContainerSize = _wtol(argv[3]);
         logPolicy.Version = CLFS_MGMT_POLICY_VERSION;
         logPolicy.LengthInBytes = sizeof(logPolicy);
         logPolicy.PolicyType = ClfsMgmtPolicyNewContainerSize;
         logPolicy.PolicyParameters.NewContainerSize.SizeInBytes = logContainerSize;
         
         if (!InstallLogPolicy(logHndl, &amp;logPolicy))
            ErrorExit("InstallLogPolicy for Container Length");
      } else if (argc > 3)
         cerr << "Log has containers; Container size is " << endl
            << "ignored" << endl;

      // Create log containers through policy
      ULONGLONG desiredSize = logInfo.TotalContainers + _wtol(argv[2]);
      ULONGLONG resultingSize = 0;
      if (!SetLogFileSizeWithPolicy(logHndl, 
                                    &amp;desiredSize, 
                                    &amp;resultingSize))
         ErrorExit("SetLogFileSizeWithPolicy");
      // Policy probably does not allow it
      else if (desiredSize != resultingSize) 
      {
         // Check the policy before setting it
         // Set new max policy
         logPolicy.PolicyType = ClfsMgmtPolicyMaximumSize;
         logPolicy.PolicyParameters.MaximumSize.Containers = 
            (ULONG)desiredSize;
         logPolicy.LengthInBytes = sizeof(logPolicy);
         if (!InstallLogPolicy(logHndl, &amp;logPolicy))
            ErrorExit("InstallLogPolicy for MaxSize");

         // Try setting container size
         if (!SetLogFileSizeWithPolicy(logHndl, 
                                       &amp;desiredSize, 
                                       &amp;resultingSize))
            ErrorExit("SetLogFileSizeWithPolicy after Setting Policy");
         }

         cout << "Requested: " << _wtol(argv[2]) << endl
            << " more containers to be added to the log" << endl;
         cout << "Initial num.: " << logInfo.TotalContainers << endl;
         cout << "Resulting num.: " << resultingSize << endl;

   } // If argc > 2
   return 0;
}

```



 

 




