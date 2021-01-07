---
description: How to add or remove persistent drive letter assignments. These drive letter assignments persist through system shutdown.
ms.assetid: 17a6df9d-07df-42f7-89c9-72a1d02141f6
title: Editing Drive Letter Assignments
ms.topic: article
ms.date: 05/31/2018
---

# Editing Drive Letter Assignments

The code example in this topic shows you how to add or remove persistent drive letter assignments. These drive letter assignments persist through system shutdown. For more information, see [Assigning a Drive Letter to a Volume](assigning-a-drive-letter-to-a-volume.md).

The code example uses the following functions: [**DefineDosDevice**](/windows/desktop/api/FileAPI/nf-fileapi-definedosdevicew), [**DeleteVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-deletevolumemountpointw), [**GetVolumeNameForVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw), and [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa).


```C++
/*
DLEDIT  -- Drive Letter Assignment Editor

Command-line syntax:
   DLEDIT <drive letter> <device name>      -- Adds a drive letter
   DLEDIT -r <drive letter>                 -- Removes a drive letter

Command-line examples:

   If E: refers to the CD-ROM drive, use the following commands to 
   make F: point to the CD-ROM drive instead. 

   DLEDIT -r E:\
   DLEDIT F:\ \Device\CdRom0

*****************************************************************
WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING  

   This program will change drive letter assignments, and the    
   changes persist through reboots. Do not remove drive letters  
   of your hard disks if you do not have this program on floppy  
   disk or you might not be able to access your hard disks again!
*****************************************************************
*/
#ifdef _WIN32_WINNT
#undef _WIN32_WINNT
#define _WIN32_WINNT 0x0500
#endif

#ifdef NTDDI_VERSION
#undef NTDDI_VERSION
#define NTDDI_VERSION 0x05000000
#endif

#include <Windows.h>
#include <stdio.h>
#include <tchar.h>

#if defined (DEBUG)
   static void DebugPrint (LPCTSTR pszMsg, DWORD dwErr);
   #define DEBUG_PRINT(pszMsg, dwErr) DebugPrint(pszMsg, dwErr)
#else
   #define DEBUG_PRINT(pszMsg, dwErr) NULL
#endif

#pragma warning (disable : 4800)

void PrintHelp (LPCTSTR pszAppName);

/*--------------------------------------------------------------------
The main function is the main routine. It parses the command-line 
arguments and either removes or adds a drive letter.

Parameters
   argc
      Count of the command-line arguments
   argv
      Array of pointers to the individual command-line arguments

--------------------------------------------------------------------*/
void _tmain (int argc, TCHAR *argv[])
{
   TCHAR * pszDriveLetter,
        * pszNTDevice,
        * pszOptions;

   TCHAR szUniqueVolumeName[MAX_PATH];
   TCHAR szDriveLetterAndSlash[4];
   TCHAR szDriveLetter[3];

   BOOL  fRemoveDriveLetter;
   BOOL  fResult;

   if (argc != 3)
   {
      PrintHelp(argv[0]);
      return;
   }

   // Use the command line to see if user wants to add or remove the 
   // drive letter. Do this by looking for the -r option.

   fRemoveDriveLetter = !lstrcmpi (argv[1], TEXT("-r"));

   if (fRemoveDriveLetter)
   {
      // User wants to remove the drive letter. Command line should 
      // be: dl -r <drive letter>

      pszOptions       = argv[1];
      pszDriveLetter   = argv[2];
      pszNTDevice      = NULL;
   }
   else
   {
      // User wants to add a drive letter. Command line should be:
      // dl <drive letter> <NT device name>

      pszOptions       = NULL;
      pszDriveLetter   = argv[1];
      pszNTDevice      = argv[2];
   }

   // GetVolumeNameForVolumeMountPoint, SetVolumeMountPoint, and
   // DeleteVolumeMountPoint require drive letters to have a trailing 
   // backslash. However, DefineDosDevice requires that the trailing 
   // backslash be absent. So, use:
   // 
   //    szDriveLetterAndSlash     for the mounted folder functions
   //    szDriveLetter             for DefineDosDevice
   // 
   // This way, command lines that use a: or a:\ 
   // for drive letters can be accepted without writing back to the original command-
   // line argument.

   szDriveLetter[0] = pszDriveLetter[0];
   szDriveLetter[1] = TEXT(':');
   szDriveLetter[2] = TEXT('\0');

   szDriveLetterAndSlash[0] = pszDriveLetter[0];
   szDriveLetterAndSlash[1] = TEXT(':');
   szDriveLetterAndSlash[2] = TEXT('\\');
   szDriveLetterAndSlash[3] = TEXT('\0');

   // Now add or remove the drive letter.

   if (fRemoveDriveLetter)
   {
      fResult = DeleteVolumeMountPoint (szDriveLetterAndSlash);

      if (!fResult)
         _tprintf(TEXT("error %lu: couldn't remove %s\n"),
                GetLastError(), szDriveLetterAndSlash);
   }
   else
   {
      // To add a drive letter that persists through reboots, use
      // SetVolumeMountPoint. This requires the volume GUID path 
      // of the device to which the new drive letter will refer. 
      // To get the volume GUID path, use 
      // GetVolumeNameForVolumeMountPoint; it requires the drive 
      // letter to already exist. So, first define the drive 
      // letter as a symbolic link to the device name. After  
      // you have the volume GUID path the new drive letter will 
      // point to, you must delete the symbolic link because the 
      // mount manager allows only one reference to a device at a 
      // time (the new one to be added).

      fResult = DefineDosDevice (DDD_RAW_TARGET_PATH, szDriveLetter,
                                 pszNTDevice);

      if (fResult)
      {
          // If GetVolumeNameForVolumeMountPoint fails, then 
          // SetVolumeMountPoint will also fail. However, 
          // DefineDosDevice must be called to remove the temporary symbolic link. 
          // Therefore, set szUniqueVolume to a known empty string.

         if (!GetVolumeNameForVolumeMountPoint (szDriveLetterAndSlash,
                  szUniqueVolumeName,
                  MAX_PATH))
         {
            DEBUG_PRINT(TEXT("GetVolumeNameForVolumeMountPoint failed"),
                        GetLastError());
            szUniqueVolumeName[0] = '\0';
         }

         fResult = DefineDosDevice ( 
                      DDD_RAW_TARGET_PATH|DDD_REMOVE_DEFINITION|
                      DDD_EXACT_MATCH_ON_REMOVE, szDriveLetter,
                      pszNTDevice);

         if (!fResult)
            DEBUG_PRINT(TEXT("DefineDosDevice failed"), 
                        GetLastError());

         fResult = SetVolumeMountPoint (szDriveLetterAndSlash, 
                        szUniqueVolumeName);

         if (!fResult)
            _tprintf (TEXT("error %lu: could not add %s\n"), 
                      GetLastError(), 
                    szDriveLetterAndSlash);
      }
   }
}

/*-------------------------------------------------------------------
The PrintHelp function prints the command-line usage help.

Parameters
   pszAppName
      The name of the executable. Used in displaying the help.

-------------------------------------------------------------------*/
void PrintHelp (LPCTSTR pszAppName)
{
   _tprintf(
       TEXT("Adds/removes a drive letter assignment for a device.\n\n"));
   _tprintf(
       TEXT("Usage: %s <Drive> <Device name> add a drive letter\n"), pszAppName);
   _tprintf(
       TEXT("       %s -r <Drive>            remove a drive letter\n\n"), pszAppName);
   _tprintf(
       TEXT("Example: %s e:\\ \\Device\\CdRom0\n"), pszAppName);
   _tprintf(
       TEXT("         %s -r e:\\\n"), pszAppName);
}

#if defined (DEBUG)
/*--------------------------------------------------------------------
The DebugPrint function prints a string to STDOUT.

Parameters
   pszMsg
      The string to be printed to STDOUT.
   dwErr
      The error code; usually obtained from GetLastError. If dwErr is 
      zero, no error code is added to the error string. If dwErr is 
      nonzero, the error code will be printed in the error string.
--------------------------------------------------------------------*/
void DebugPrint (LPCTSTR pszMsg, DWORD dwErr)
{
   if (dwErr)
      _tprintf(TEXT("%s: %lu\n"), pszMsg, dwErr);
   else
      _tprintf(TEXT("%s\n"), pszMsg);
}
#endif
```



 

 



