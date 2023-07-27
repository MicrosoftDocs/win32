---
description: Adding Region-Change Support to an Application
ms.assetid: 4a5c049d-b59f-4130-9252-bc28662a7931
title: Adding Region-Change Support to an Application
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Adding Region-Change Support to an Application

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following functions are provided for developers who wish to integrate region-change support into their decoders or DVD applications.


```C++
// Forward declares, constants, typedefs.
const short MAX_DRIVE_NAME = 4;
struct DriveName
{
    TCHAR name[MAX_DRIVE_NAME];
};
BOOL DoesFileExist(LPTSTR pszFile);
BOOL GetDriveLetter(IDvdInfo2 *pDvd, DriveName& szDrive);

#define ARRAY_SIZE(x) (sizeof(x)/sizeof(x[0]))

/////////////////////////////////////////////////////////////////////
// ChangeDVDRegion :  Function to change the DVD drive region.
// Parameters:
//     hWnd - Handle to the application window.
// Returns TRUE if the change is successful, or FALSE otherwise.
// (Failure usually means there was no drive with a valid DVD-V disc.)
/////////////////////////////////////////////////////////////////////
BOOL ChangeDVDRegion(HWND hWnd, IDvdInfo2 *pDvd)
{
    typedef BOOL (APIENTRY *DVDPPLAUNCHER) (HWND hWnd, CHAR DriveLetter);
    
    // First find out which drive is a DVD drive with a valid DVD-V disc.
    DriveName  szDVDDrive;

    if (! GetDriveLetter(pDvd, szDVDDrive) )
    {
        MessageBox(hWnd, TEXT("No DVD drive was found with DVD-V disc."),
            TEXT("Error"), MB_OK | MB_ICONERROR) ;
        return FALSE;
    }

    // Detect the version. 
    
    OSVERSIONINFO   ver;
    ver.dwOSVersionInfoSize = sizeof(OSVERSIONINFO);
    GetVersionEx(&ver);

    if (VER_PLATFORM_WIN32_NT  == ver.dwPlatformId)
    {
        HINSTANCE      hInstDLL;
        DVDPPLAUNCHER  dvdPPLauncher;
        CHAR           szDVDDriveA[MAX_DRIVE_NAME];

        const TCHAR szDllName[] =  TEXT("\\storprop.dll");
        
        // Allocate a large enough string to hold the path + the name.
        TCHAR szCmdLine[MAX_PATH + (sizeof(szDllName)/sizeof(TCHAR)) + 1];

#ifdef UNICODE
        WideCharToMultiByte(CP_ACP, 0, szDVDDrive.name, -1,
            szDVDDriveA, sizeof(szDVDDriveA), NULL, NULL );
#else
        StringCchCopy(szDVDDriveA, MAX_DRIVE_NAME, szDVDDrive.name);
#endif  
        

        UINT cb = GetSystemDirectory(szCmdLine, MAX_PATH + 1);
        if (cb == 0 || cb > MAX_PATH + 1)
        {
            return FALSE;
        }

        StringCchCat(szCmdLine, ARRAY_SIZE(szCmdLine), szDllName);
        
        hInstDLL = LoadLibrary (szCmdLine);
        if (hInstDLL)
        {
            BOOL bResult = FALSE;

            dvdPPLauncher = (DVDPPLAUNCHER) GetProcAddress(hInstDLL,
                "DvdLauncher");
            if (dvdPPLauncher)
            {
                 bResult = dvdPPLauncher(hWnd, szDVDDriveA[0]);
            }
            FreeLibrary(hInstDLL);
            return bResult;
        }
    }  
    else  
    {
        return FALSE;
    }  

    return FALSE;
} 


/////////////////////////////////////////////////////////////////////
// GetDriveLetter: Returns the drive letter of the active DVD drive.
// Parameters:
//     pDvdC - IDvdControl2 interface of the DVD Navigator filter.
//     pszDrive - Receives the first DVD drive with a valid DVD-V disc.
// Returns TRUE if there is a DVD drive with a valid disc.
/////////////////////////////////////////////////////////////////////
BOOL GetDriveLetter(IDvdInfo2 *pDvd, DriveName& pszDrive) 
{
    WCHAR  szPathW[MAX_PATH];
    TCHAR  szPath[MAX_PATH];
    ULONG  ulActualSize = 0;

    pszDrive.name[0] = pszDrive.name[MAX_DRIVE_NAME - 1] = 0;
    
    // Get the current root directory
    HRESULT hr = pDvd->GetDVDDirectory(szPathW, MAX_PATH, &ulActualSize);

    if (SUCCEEDED(hr))
    {

#ifdef UNICODE
        StringCchCopy(pszDrive.name, MAX_DRIVE_NAME, szPathW);
#else
        WideCharToMultiByte(CP_ACP, 0, szPathW, ulActualSize, szPath, MAX_PATH, 0, 0);
        StringCchCopy(pszDrive.name, MAX_DRIVE_NAME, szPath);
#endif  
        
        if (DRIVE_CDROM == GetDriveType(pszDrive.name)) // could be a DVD drive
            return TRUE;
    }

  // Now loop through all the valid drives to detect which one
  // is a DVD drive with a valid DVD-V disc in it.

  // Get all valid drives
  DWORD dwLen = GetLogicalDriveStrings(MAX_PATH, szPath);

  if (dwLen > MAX_PATH)
  {
      // The function returns a larger value if the buffer is too small.
      return FALSE;
  }

  // Try all drives one by one
  for (size_t dw = 0; dw < dwLen; ) 
  {
      
      TCHAR *szTmp = szPath + dw;
      
      // Look only for CD-ROM drives that has a disc with required (.ifo) files
      if (DRIVE_CDROM  == GetDriveType(szTmp)) 
      {
          TCHAR   szDVDPath1[MAX_PATH + 1];
          TCHAR   szDVDPath2[MAX_PATH + 1];
          
          StringCchCopy(szDVDPath1, MAX_DRIVE_NAME, szTmp);
          StringCchCopy(szDVDPath2, MAX_DRIVE_NAME, szTmp);
          StringCchCat(szDVDPath1, ARRAY_SIZE(szDVDPath1), TEXT("Video_ts\\Video_ts.ifo"));
          StringCchCat(szDVDPath2, ARRAY_SIZE(szDVDPath2), TEXT("Video_ts\\Vts_01_0.ifo"));
          
          // If the .ifo files exist on this drive then it has a valid DVD-V disc
          if (DoesFileExist(szDVDPath1) && DoesFileExist(szDVDPath2))    
          {
              StringCchCopy(pszDrive.name, MAX_DRIVE_NAME, szTmp);
              return TRUE;   // return the first drive that has a valid DVD-V disc
          }
      }

      size_t len = 0;
      StringCchLength(szTmp, STRSAFE_MAX_CCH, &len);
      dw += len + 1;
  }

  return FALSE ;   // didn't find any DVD drive with DVD-V content
} 

/////////////////////////////////////////////////////////////////////
// DoesFileExist : Determines whether a specified file exists
// Parameters:
//     pszFile - File name to check.
// Returns TRUE if the specified file is found, or FALSE otherwise.
/////////////////////////////////////////////////////////////////////
BOOL DoesFileExist(LPTSTR pszFile)
{
    if (pszFile == NULL)
    {
        return FALSE;
    }

    size_t len = 0;

    if (FAILED(StringCchLength(pszFile, STRSAFE_MAX_CCH, &len)))
    {
        return FALSE;
    }

    if (len > MAX_PATH)
    {
        return FALSE;
    }


    // We don't want any error message box to pop up when we try to test
    // if the required file is available to open for read --apcb.
    
    UINT uErrorMode = SetErrorMode(SEM_FAILCRITICALERRORS | SEM_NOOPENFILEERRORBOX);
    
    HANDLE hFile = CreateFile(pszFile, GENERIC_READ, FILE_SHARE_READ, NULL, 
        OPEN_EXISTING, FILE_FLAG_SEQUENTIAL_SCAN, NULL);

    SetErrorMode(uErrorMode);  // restore error mode
    
    if (INVALID_HANDLE_VALUE  == hFile) 
    {
        return FALSE;    
    }
    
    CloseHandle(hFile);
    return TRUE;
} 
```



## Related topics

<dl> <dt>

[DVD Region Change Support in Windows](dvd-region-change-support-in-windows.md)
</dt> </dl>

 

 



