---
description: The following example uses the GetComputerName, GetUserName, GetSystemDirectory, GetWindowsDirectory, and ExpandEnvironmentStrings functions to get information that describes the system configuration.
ms.assetid: 965bd14b-be93-4084-bce8-642f5704cef1
title: Getting System Information
ms.topic: article
ms.date: 05/31/2018
---

# Getting System Information

The following example uses the [**GetComputerName**](/windows/desktop/api/Winbase/nf-winbase-getcomputernamea), [**GetUserName**](/windows/desktop/api/Winbase/nf-winbase-getusernamea), [**GetSystemDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya), [**GetWindowsDirectory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya), and [**ExpandEnvironmentStrings**](/windows/win32/api/processenv/nf-processenv-expandenvironmentstringsa) functions to get information that describes the system configuration.


```C++
#include <windows.h>
#include <tchar.h>
#include <stdio.h>

TCHAR* envVarStrings[] =
{
  TEXT("OS         = %OS%"),
  TEXT("PATH       = %PATH%"),
  TEXT("HOMEPATH   = %HOMEPATH%"),
  TEXT("TEMP       = %TEMP%")
};
#define  ENV_VAR_STRING_COUNT  (sizeof(envVarStrings)/sizeof(TCHAR*))
#define INFO_BUFFER_SIZE 32767
void printError( TCHAR* msg );

void main( )
{
  DWORD i;
  TCHAR  infoBuf[INFO_BUFFER_SIZE];
  DWORD  bufCharCount = INFO_BUFFER_SIZE;
 
  // Get and display the name of the computer. 
  bufCharCount = INFO_BUFFER_SIZE;
  if( !GetComputerName( infoBuf, &bufCharCount ) )
    printError( TEXT("GetComputerName") ); 
  _tprintf( TEXT("\nComputer name:      %s"), infoBuf ); 
 
  // Get and display the user name. 
  bufCharCount = INFO_BUFFER_SIZE;
  if( !GetUserName( infoBuf, &bufCharCount ) )
    printError( TEXT("GetUserName") ); 
  _tprintf( TEXT("\nUser name:          %s"), infoBuf ); 
 
  // Get and display the system directory. 
  if( !GetSystemDirectory( infoBuf, INFO_BUFFER_SIZE ) )
    printError( TEXT("GetSystemDirectory") ); 
  _tprintf( TEXT("\nSystem Directory:   %s"), infoBuf ); 
 
  // Get and display the Windows directory. 
  if( !GetWindowsDirectory( infoBuf, INFO_BUFFER_SIZE ) )
    printError( TEXT("GetWindowsDirectory") ); 
  _tprintf( TEXT("\nWindows Directory:  %s"), infoBuf ); 
 
  // Expand and display a few environment variables. 
  _tprintf( TEXT("\n\nSmall selection of Environment Variables:") ); 
  for( i = 0; i < ENV_VAR_STRING_COUNT; ++i )
  {
    bufCharCount = ExpandEnvironmentStrings(envVarStrings[i], infoBuf,
        INFO_BUFFER_SIZE ); 
    if( bufCharCount > INFO_BUFFER_SIZE )
      _tprintf( TEXT("\n\t(Buffer too small to expand: \"%s\")"), 
              envVarStrings[i] );
    else if( !bufCharCount )
      printError( TEXT("ExpandEnvironmentStrings") );
    else
      _tprintf( TEXT("\n   %s"), infoBuf );
  }
  _tprintf( TEXT("\n\n"));
}

void printError( TCHAR* msg )
{
  DWORD eNum;
  TCHAR sysMsg[256];
  TCHAR* p;

  eNum = GetLastError( );
  FormatMessage( FORMAT_MESSAGE_FROM_SYSTEM | 
         FORMAT_MESSAGE_IGNORE_INSERTS,
         NULL, eNum,
         MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
         sysMsg, 256, NULL );

  // Trim the end of the line and terminate it with a null
  p = sysMsg;
  while( ( *p > 31 ) || ( *p == 9 ) )
    ++p;
  do { *p-- = 0; } while( ( p >= sysMsg ) &&
                          ( ( *p == '.' ) || ( *p < 33 ) ) );

  // Display the message
  _tprintf( TEXT("\n\t%s failed with error %d (%s)"), msg, eNum, sysMsg );
}
```



 

 
