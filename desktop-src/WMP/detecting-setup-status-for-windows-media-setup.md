---
title: Detecting Setup Status for Windows Media Setup
description: Detecting Setup Status for Windows Media Setup
ms.assetid: c3acc268-934b-4a10-aab5-4b1764cb4c87
keywords:
- Windows Media Player,detecting setup status
- Windows Media Player,setup status
- Windows Media Player,redistributing software
- Windows Media Player,software redistribution
- detecting setup status
- setup status
- redistributing software
- software redistribution
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Detecting Setup Status for Windows Media Setup

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following code can be used with the Windows Media Player redistribution packages. The installation status is stored in the **InstallResult** registry entry under the following subkey:

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\MediaPlayer\\Setup**

The **InstallResult**registry entry has the following form.



| Name              | Type           | Value                                                                                                                   |
|-------------------|----------------|-------------------------------------------------------------------------------------------------------------------------|
| **InstallResult** | **REG\_DWORD** | An **HRESULT** that indicates whether Windows Media Player installation was successful and whether a restart is needed. |



 

Here is example C++ code that could be incorporated into a calling setup application. This code will set the `fSuccess` and `fRebootNeeded` variables to **true** or **false**, as appropriate, based on the **HRESULT** value written by Windows Media Player Setup in the component redistribution package.


```C++
#include <windows.h>
#include <stdio.h>
 
// If NS_S_REBOOT_REQUIRED is undefined, use 0xD2AF9.
#ifndef NS_S_REBOOT_REQUIRED
#define NS_S_REBOOT_REQUIRED       0xd2af9
#endif
 
int main( void )
{
    HKEY hKey = NULL;
    BOOL fSuccess = FALSE;
    BOOL fRebootNeeded = FALSE;
 
if( ERROR_SUCCESS == RegOpenKeyExA( 
                         HKEY_CURRENT_USER, 
                         "Software\\Microsoft\\MediaPlayer\\Setup", 
                         0, KEY_QUERY_VALUE, &hKey ))
    {
        char szResult[64];
        DWORD dwResult = sizeof( szResult );
 
if( ERROR_SUCCESS == RegQueryValueExA( 
                         hKey, "InstallResult", NULL, NULL, 
                         (LPBYTE)szResult, &dwResult ) )
        {
            sscanf_s( szResult, "%x", &dwResult );
            fSuccess = SUCCEEDED( dwResult );
            fRebootNeeded = ( NS_S_REBOOT_REQUIRED == dwResult );
        }
 
        RegCloseKey( hKey );
    }
 
    if( fSuccess )
    {
        printf( "Setup Succeeded..." );
        if( fRebootNeeded )
            printf( "A restart IS required...\n" );
        else
            printf( "A restart IS NOT required...\n" );
    }
    else
    {
        printf( "Setup Failed..." );
        if( fRebootNeeded )
            printf( "A restart IS required...\n" );
        else
            printf( "A restart IS NOT required...\n" );
    }
 
    return 0;
}
```



## Related topics

<dl> <dt>

[**Redistributing Windows Media Player Software**](redistributing-windows-media-player-software.md)
</dt> </dl>

 

 




