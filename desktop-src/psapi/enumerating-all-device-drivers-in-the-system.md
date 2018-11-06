---
title: Enumerating All Device Drivers in the System
description: The following sample code uses the EnumDeviceDrivers function to enumerate the current device drivers in the system.
ms.assetid: 047d8541-e17e-4738-8453-674db69365df
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating All Device Drivers in the System

The following sample code uses the [**EnumDeviceDrivers**](/windows/desktop/api/Psapi/nf-psapi-enumdevicedrivers) function to enumerate the current device drivers in the system. It passes the load addresses retrieved from this function call to the [**GetDeviceDriverBaseName**](/windows/desktop/api/Psapi/nf-psapi-getdevicedriverbasenamea) function to retrieve a name that can be displayed.


```C++
#include <windows.h>
#include <psapi.h>
#include <tchar.h>
#include <stdio.h>

// To ensure correct resolution of symbols, add Psapi.lib to TARGETLIBS
// and compile with -DPSAPI_VERSION=1

#define ARRAY_SIZE 1024

int main( void )
{
   LPVOID drivers[ARRAY_SIZE];
   DWORD cbNeeded;
   int cDrivers, i;

   if( EnumDeviceDrivers(drivers, sizeof(drivers), &cbNeeded) && cbNeeded < sizeof(drivers))
   { 
      TCHAR szDriver[ARRAY_SIZE];

      cDrivers = cbNeeded / sizeof(drivers[0]);

      _tprintf(TEXT("There are %d drivers:\n"), cDrivers);      
      for (i=0; i < cDrivers; i++ )
      {
         if(GetDeviceDriverBaseName(drivers[i], szDriver, sizeof(szDriver) /              sizeof(szDriver[0])))
         {
            _tprintf(TEXT("%d: %s\n"), i+1, szDriver);
         }
      }
   }
   else 
   {
        _tprintf(TEXT("EnumDeviceDrivers failed; array size needed is %d\n"),             cbNeeded / sizeof(LPVOID));
        return 1;
   }

return 0;
}
```



 

 




