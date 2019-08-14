---
title: Monitoring Applications
description: This topic discusses how elements of the Dynamic Data Exchange Management Library can be used to create an application that monitors dynamic data exchange activity in the system.
ms.assetid: 6705dc8e-d1e9-4057-9fa2-42cd5cf818af
keywords:
- Windows User Interface,Dynamic Data Exchange (DDE)
- Dynamic Data Exchange (DDE),monitoring applications
- DDE (Dynamic Data Exchange),monitoring applications
- data exchange,Dynamic Data Exchange (DDE)
- Windows User Interface,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange Management Library (DDEML),monitoring applications
- DDEML (Dynamic Data Exchange Management Library),monitoring applications
- data exchange,Dynamic Data Exchange Management Library (DDEML)
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring Applications

The API elements of the Dynamic Data Exchange Management Library (DDEML) can be used to create an application that monitors Dynamic Data Exchange (DDE) activity in the system. Like any DDEML application, a DDE monitoring application contains a DDE callback function. The DDEML notifies a monitoring application's DDE callback function whenever a DDE event occurs, passing information about the event to the callback function. The application typically displays the information in a window or writes it to a file.

To receive notifications from the DDEML, an application must have registered as a DDE monitor by specifying the APPCLASS\_MONITOR flag in a call to the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function. In this same call, the application can specify one or more monitor flags to indicate the types of events for which the DDEML is to notify the application's callback function. The following monitor flags can be specified by an application:



| Flag          | Description                                                                                                                                                                                                                                         |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MF\_CALLBACKS | Notifies the callback function whenever a transaction is sent to any DDE callback function in the system.                                                                                                                                           |
| MF\_CONV      | Notifies the callback function whenever a conversation is established or terminated.                                                                                                                                                                |
| MF\_ERRORS    | Notifies the callback function whenever a DDEML error occurs.                                                                                                                                                                                       |
| MF\_HSZ\_INFO | Notifies the callback function whenever a DDEML application creates, frees, or increments the usage count of a string handle or whenever a string handle is freed as a result of a call to the [**DdeUninitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeuninitialize) function. |
| MF\_LINKS     | Notifies the callback function whenever an advise loop is started or ended.                                                                                                                                                                         |
| MF\_POSTMSGS  | Notifies the callback function whenever the system or an application posts a DDE message.                                                                                                                                                           |
| MF\_SENDMSGS  | Notifies the callback function whenever the system or an application sends a DDE message.                                                                                                                                                           |



 

The following example shows how to register a DDE monitoring application so that its DDE callback function receives notifications of all DDE events.


```
DWORD idInst; 
PFNCALLBACK lpDdeProc; 
hInst = hInstance; 
 
if (DdeInitialize( 
        (LPDWORD) &idInst,  // instance identifier 
        DDECallback,        // pointer to callback function 
        APPCLASS_MONITOR |  // this is a monitoring application 
        MF_CALLBACKS     |  // monitor callback functions 
        MF_CONV          |  // monitor conversation data 
        MF_ERRORS        |  // monitor DDEML errors 
        MF_HSZ_INFO      |  // monitor data handle activity 
        MF_LINKS         |  // monitor advise loops 
        MF_POSTMSGS      |  // monitor posted DDE messages 
        MF_SENDMSGS,        // monitor sent DDE messages 
        0))                 // reserved 
{
    return FALSE; 
}
```



The DDEML informs a monitoring application of a DDE event by sending an [**XTYP\_MONITOR**](xtyp-monitor.md) transaction to the application's DDE callback function. During this transaction, the DDEML passes a monitor flag that specifies the type of DDE event that has occurred and a handle to a DDE object that contains detailed information about the event. The DDEML provides a set of structures that the application can use to extract the information from the DDE object. There is a corresponding structure for each type of DDE event.



| Structure                                  | Description                                                       |
|--------------------------------------------|-------------------------------------------------------------------|
| [**MONCBSTRUCT**](/windows/win32/api/ddeml/ns-ddeml-moncbstruct)     | Contains information about a transaction.                         |
| [**MONCONVSTRUCT**](/windows/win32/api/ddeml/ns-ddeml-monconvstruct) | Contains information about a conversation.                        |
| [**MONERRSTRUCT**](/windows/win32/api/ddeml/ns-ddeml-monerrstruct)   | Contains information about the latest DDE error.                  |
| [**MONLINKSTRUCT**](/windows/win32/api/ddeml/ns-ddeml-monlinkstruct) | Contains information about an advise loop.                        |
| [**MONHSZSTRUCT**](/windows/win32/api/ddeml/ns-ddeml-monhszstructa)   | Contains information about a string handle.                       |
| [**MONMSGSTRUCT**](/windows/win32/api/ddeml/ns-ddeml-monmsgstruct)   | Contains information about a DDE message that was sent or posted. |



 

The following example shows the DDE callback function of a DDE monitoring application that formats information about each string handle event and then displays the information in a window. The function uses the [**MONHSZSTRUCT**](/windows/win32/api/ddeml/ns-ddeml-monhszstructa) structure to extract the information from the DDE object.


```
HDDEDATA CALLBACK DDECallback(uType, uFmt, hconv, hsz1, hsz2, 
    hdata, dwData1, dwData2) 
UINT uType; 
UINT uFmt; 
HCONV hconv; 
HSZ hsz1; 
HSZ hsz2; 
HDDEDATA hdata; 
DWORD dwData1; 
DWORD dwData2; 
{ 
    LPVOID lpData; 
    CHAR *szAction; 
    CHAR szBuf[256]; 
    DWORD cb;
    HRESULT hResult; 
 
    switch (uType) 
    { 
        case XTYP_MONITOR: 
            // Obtain a pointer to the global memory object. 
 
            if (lpData = DdeAccessData(hdata, &cb)) 
            { 
                // Examine the monitor flag. 
 
                switch (dwData2) 
                { 
                    case MF_HSZ_INFO: 
 
#define PHSZS ((MONHSZSTRUCT *)lpData) 
 
                        // The global memory object contains 
                        // string handle data. Use the MONHSZSTRUCT 
                        // structure to access the data. 
 
                        switch (PHSZS->fsAction) 
                        { 
                            // Examine the action flags to determine
                            // the action performed on the handle.
 
                            case MH_CREATE: 
                                szAction = "Created"; 
                                break; 
 
                            case MH_KEEP: 
                                szAction = "Incremented"; 
                                break; 
 
                            case MH_DELETE: 
                                szAction = "Deleted"; 
                                break; 
 
                            case MH_CLEANUP: 
                                szAction = "Cleaned up"; 
                                break; 
 
                            default: 
                                DdeUnaccessData(hdata); 
                                return (HDDEDATA) 0; 
                        } 
 
                        // Write formatted output to a buffer. 
                        hResult = StringCchPrintf(szBuf, 256/sizeof(TCHAR),
                            "Handle %s, Task: %x, Hsz: %lx(%s)", 
                            (LPSTR) szAction, PHSZS->hTask, 
                            PHSZS->hsz, (LPSTR) PHSZS->str);
                        if (FAILED(hResult))
                        {
                        // TO DO: Write error handler.
                            return;
                        } 
                        // Display text or write to a file. 
 
                        break; 
 
#undef PHSZS 
 
                    // Process other MF_* flags. 
 
                    default: 
                        break; 
                } 
            } 
 
            // Free the global memory object. 
 
            DdeUnaccessData(hdata); 
            break; 
 
        default: 
            break; 
    } 
    return (HDDEDATA) 0; 
} 
```



 

 




