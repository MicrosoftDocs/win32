---
title: HH\_GET\_LAST\_ERROR command
description: Returns information about the last error that occurred in the HTML Help ActiveX control (Hhctrl.ocx).
ms.assetid: 94EA23C7-86F7-420a-8FA0-4F683CD830FC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HH\_GET\_LAST\_ERROR command

Returns information about the last error that occurred in the HTML Help ActiveX control (Hhctrl.ocx).



| *pszFile*     | *dwData*                                                                     |
|---------------|------------------------------------------------------------------------------|
| Must be NULL. | A pointer to a [**HH\_LAST\_ERROR**](hh-last-error-structure.md) structure. |



 

## Example


```
USES_CONVERSIONS; // For Unicode to ANSI string conversion
HH_LAST_ERROR lasterror ;
HWND hwnd = HtmlHelp(
                     hOwner,
                     NULL,
                     HH_GET_LAST_ERROR,
                     reinterpret_cast<DWORD>(&amp;lasterror)) ;
// Make sure that HH_GET_LAST_ERROR succeeded.
if (hwnd != 0)
{
   // Only report an error if we found one:
   if (FAILED(lasterror.hr))
   {
      // Is there a text message to display...
      if (lasterror.description)
      {
         // Convert the String to ANSI
         TCHAR* pDesc = OLE2T(lasterror.description) ;
         ::SysFreeString(lasterror.description) ;
         // Display
         MessageBox(hOwner, pDesc,
                       "Help Error", MB_OK) ;
      }
   }
}
```



## Return Value

-   On failure, zero.
-   On success, non zero.

## Remarks

-   There is no user interface (UI) associated with this command. The caller is responsible for returning error codes and text to a UI, such as a message box or a text file, and/or responding to an error.
-   This command reports on a limited range of possible errors. If a call to HtmlHelp() returns NULL, **HH\_GET\_LAST\_ERROR** may not always report an error.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




