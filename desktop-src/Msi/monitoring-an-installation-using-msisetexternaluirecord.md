---
description: Package authors can monitor internal Windows Installer messages through the creation of an executable application that contains both a record-based callback handler to receive the messages and functionality to initiate an installation.
ms.assetid: 5d9e51dd-7918-491f-aea9-01a6e0317c57
title: Monitoring an Installation Using MsiSetExternalUIRecord
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring an Installation Using MsiSetExternalUIRecord

Package authors can monitor internal Windows Installer messages through the creation of an executable application that contains both a record-based callback handler to receive the messages and functionality to initiate an installation.

The record-based handler in the following example conforms to the [**INSTALLUI\_HANDLER\_RECORD**](/windows/win32/api/msi/nc-msi-installui_handler_record) prototype, and a pointer to this callback handler is passed to [**MsiSetExternalUIRecord**](/windows/desktop/api/Msi/nf-msi-msisetexternaluirecord) function.


```C++
//
// ExternalUIRecord.cpp : Defines the entry point for the console application.
//
#include <tchar.h>
#include <windows.h>
#include <stdio.h>
#include <msi.h>
#include <msiquery.h>
#pragma comment(lib, "msi.lib")
#pragma comment(lib, "user32.lib")
#ifndef _WIN32_MSI
#define _WIN32_MSI    310
#endif 

void Usage(LPCTSTR szProgram)
{
_tprintf(TEXT("Usage: %s <path to .MSI package>\n"), szProgram);
return;
}

// In the following snippet, the hRecord parameter is used only
// to format the displayed message. However, because hRecord is 
// a handle to a MSI record, the MSI API could be called to
// obtain information. The external UI handler should not close
// hRecord because the handle belongs to the Windows Installer.

INT CALLBACK UIHandler(LPVOID pvContext, UINT uiMessageType, MSIHANDLE hRecord)
{
INSTALLMESSAGE iMessage = (INSTALLMESSAGE)(0xFF000000 & uiMessageType);
BOOL bMessage = (INSTALLMESSAGE_ERROR == iMessage);
BOOL bFatalExit = (INSTALLMESSAGE_FATALEXIT == iMessage);
BOOL bWarning = (INSTALLMESSAGE_WARNING == iMessage);

if ((bMessage || bFatalExit || bWarning) && hRecord && pvContext)
{
TCHAR rgchMessage[1024];
DWORD dwMessage = sizeof(rgchMessage)/sizeof(TCHAR);
LPTSTR pszMessage = rgchMessage;

UINT uiRet = MsiFormatRecord(*(MSIHANDLE*)pvContext, 
                                 hRecord, pszMessage, &dwMessage);
if (ERROR_MORE_DATA == uiRet)
{
// Allocate a buffer to hold the string and terminating null.
pszMessage = new TCHAR[++dwMessage];
if (!pszMessage)
{
// no memory, return an error
return -1;
}
uiRet = MsiFormatRecord(*(MSIHANDLE*)pvContext, 
                                 hRecord, pszMessage, &dwMessage);
if (ERROR_SUCCESS != uiRet)
{
// Return an error if an unexpected error occurs.
if (rgchMessage != pszMessage)
    delete [] pszMessage;
return -1;
}
}
TCHAR rgchFatalError[] = TEXT("Fatal Error");
TCHAR rgchError[] = TEXT("Error");
TCHAR rgchWarning[] = TEXT("Warning");
TCHAR* pszCaption = NULL;

if (INSTALLMESSAGE_ERROR == iMessage)
    pszCaption = rgchError;
else if (INSTALLMESSAGE_FATALEXIT == iMessage)
    pszCaption = rgchFatalError;
else if (INSTALLMESSAGE_WARNING == iMessage)
    pszCaption = rgchWarning;

int iResponse = MessageBox(NULL, pszMessage, 
                         pszCaption, uiMessageType & 0x00FFFFFF);

if (rgchMessage != pszMessage)
    delete [] pszMessage;
return iResponse;
}

// Signal that the handler handled this message.
return IDOK;
}

// A console application that takes the path to a package,
// installs the package silently, and uses a record based 
// external UI handler to display any error.

int _tmain(int argc, _TCHAR* argv[])
{
UINT uiRet = ERROR_SUCCESS;
MSIHANDLE hProduct = NULL;

if (2 != argc)
{
    // Incorrect command line used.
    Usage(argv[0]);
    uiRet = 1;
    goto End;
}

// Because thid example won't restore the UI level,
// ignore return value.
MsiSetInternalUI(INSTALLUILEVEL_NONE, /* pWnd */ NULL);

uiRet = MsiOpenPackage(argv[1], &hProduct);
if (ERROR_SUCCESS != uiRet)
{
    _tprintf(TEXT("ERROR: Failed to open %s database.\n"), argv[1]);
    uiRet = 1;
    goto End;
}

// set the external UI handler
DWORD dwMessageFilter = INSTALLLOGMODE_FATALEXIT
       | INSTALLLOGMODE_ERROR | INSTALLLOGMODE_WARNING;

//Pass the pointer to hProduct as the pvContext argument, 
// so that the record based external UI handler
// can use it to format the records we send to it.

uiRet = MsiSetExternalUIRecord(UIHandler, 
              dwMessageFilter, (LPVOID)&hProduct, /* ppuiPrevHandle */ NULL);

if (ERROR_SUCCESS != uiRet)
{
    _tprintf(TEXT("ERROR: Failed to set the external UI handler.\n"));
    uiRet = 1;
    goto End;
}

// Do the default action and install the product.
uiRet = MsiDoAction(hProduct, TEXT(""));

End:
// Close opened resources.
if (hProduct)
    MsiCloseHandle(hProduct);

return ERROR_SUCCESS == uiRet ? 0 : 1;
}
//
```



 

 
