---
title: Data Management
description: This topic discusses how memory objects pass data from one application to another.
ms.assetid: 32919f27-4699-4831-8837-c5160b1daf4e
keywords:
- Windows User Interface,Dynamic Data Exchange (DDE)
- Dynamic Data Exchange (DDE),data management
- DDE (Dynamic Data Exchange),data management
- data exchange,Dynamic Data Exchange (DDE)
- Windows User Interface,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange Management Library (DDEML),data management
- DDEML (Dynamic Data Exchange Management Library),data management
- data exchange,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange (DDE),objects
- DDE (Dynamic Data Exchange),objects
- Dynamic Data Exchange Management Library (DDEML),objects
- DDEML (Dynamic Data Exchange Management Library),objects
ms.topic: article
ms.date: 05/31/2018
---

# Data Management

Because Dynamic Data Exchange (DDE) uses memory objects to pass data from one application to another, the Dynamic Data Exchange Management Library (DDEML) provides a set of functions that DDE applications can use to create and manage DDE objects.

All transactions that involve the exchange of data require the application supplying the data to create a local buffer containing the data and then to call the [**DdeCreateDataHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatedatahandle) function. This function allocates a DDE object, copies the data from the buffer to the object, and returns a data handle. A data handle is a **DWORD** value that the DDEML uses to provide access to data in the DDE object. To share the data in a DDE object, an application passes the data handle to the DDEML, and the DDEML passes the handle to the DDE callback function of the application that is receiving the data transaction.

The following example shows how to create a DDE object and obtain a handle to the object. During the [**XTYP\_ADVREQ**](xtyp-advreq.md) transaction, the callback function converts the current time to an ASCII string, copies the string to a local buffer, and then creates a DDE object that contains the string. The callback function returns the handle to the DDE object (HDDEDATA) to the DDEML, which passes the handle to the client application.


```
typedef struct tagTIME 
{ 
    INT     hour;   // 0 - 11 hours for analog clock 
    INT     hour12; // 12-hour format 
    INT     hour24; // 24-hour format 
    INT     minute; 
    INT     second; 
    INT     ampm;   // 0 - AM , 1 - PM 
} TIME; 
 
HDDEDATA EXPENTRY DdeCallback(uType, uFmt, hconv, hsz1, hsz2, 
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
 
    CHAR szBuf[32];
    HRESULT hResult;
    size_t * pcch;
    HRESULT hResult; 
 
    switch (uType) 
    { 
    case XTYP_ADVREQ: 
        if ((hsz1 == hszTime && hsz2 == hszNow) && 
                (uFmt == CF_TEXT)) 
        { 
            // Copy the formatted string to a buffer. 
 
            itoa(tmTime.hour, szBuf, 10);
            hResult = StringCchCat(szBuf, 32/sizeof(TCHAR), ":"); 
            if (FAILED(hResult))
            {
            // TO DO: Write error handler.
                return;
            }
            if (tmTime.minute < 10)
                hResult = StringCchCat(szBuf, 32/sizeof(TCHAR), "0"); 
                if (FAILED(hResult)
            {
            // TO DO: Write error handler.
                return;
            } 
            hResult = StringCchLength(szBuf, 32/sizeof(TCHAR), pcch);
            if (FAILED(hResult))
            {
            // TO DO: Write error handler.
                return;
            }
            itoa(tmTime.minute, &szBuf[*pcch], 10);
            hResult = StringCchCat(szBuf, 32/sizeof(TCHAR), ":"); 
            if (FAILED(hResult)
            {
            // TO DO: Write error handler.
                return;
            }
            if (tmTime.second < 10) 
                hResult = StringCchCat(szBuf, 32/sizeof(TCHAR), "0"); 
            if (FAILED(hResult)
            {
            // TO DO: Write error handler.
                return;
            }
            hResult = StringCchLength(szBuf, 32/sizeof(TCHAR), pcch);
            if (FAILED(hResult))
            {
            // TO DO: Write error handler.
                return;
            }
            itoa(tmTime.second, &szBuf[*pcch], 10);
            hResult = StringCchLength(szBuf, 32/sizeof(TCHAR), pcch);
            if (FAILED(hResult))
            {
            // TO DO: Write error handler.
                return;
            } 
            szBuf[*pcch] = '\0'; 
 
            // Create a global object and return its data handle. 
            hResult = StringCchLength(szBuf, 32/sizeof(TCHAR), pcch);
            if (FAILED(hResult))
            {
            // TO DO: Write error handler.
                return;
            }
            return (DdeCreateDataHandle( 
                idInst, 
                (LPBYTE) szBuf,     // instance identifier 
                *pcch + 1,          // source buffer length 
                0,                  // offset from beginning 
                hszNow,             // item name string 
                CF_TEXT,            // clipboard format 
                0));                // no creation flags 
        } else return (HDDEDATA) NULL; 
 
    // Process other transactions. 
    } 
} 
```



The receiving application obtains a pointer to the DDE object by passing the data handle to the [**DdeAccessData**](/windows/desktop/api/Ddeml/nf-ddeml-ddeaccessdata) function. The pointer returned by **DdeAccessData** provides read-only access. The application should use the pointer to review the data and then call the [**DdeUnaccessData**](/windows/desktop/api/Ddeml/nf-ddeml-ddeunaccessdata) function to invalidate the pointer. The application can copy the data to a local buffer by using the [**DdeGetData**](/windows/desktop/api/Ddeml/nf-ddeml-ddegetdata) function.

The following example obtains a pointer to the DDE object identified by the *hData* parameter, copies the contents to a local buffer, and then invalidates the pointer.


```
HDDEDATA hdata; 
LPBYTE lpszAdviseData; 
DWORD cbDataLen; 
DWORD i; 
char szData[32]; 
 
// 
case XTYP_ADVDATA: 
    lpszAdviseData = DdeAccessData(hdata, &cbDataLen); 
    for (i = 0; i < cbDataLen; i++) 
        szData[i] = *lpszAdviseData++; 
    DdeUnaccessData(hdata); 
    return (HDDEDATA) TRUE; 
//
```



Usually, when an application that created a data handle passes that handle to the DDEML, the handle becomes invalid in the creating application. This situation is not a problem if the application must share data with only a single application. If an application must share the same data with multiple applications, however, the creating application should specify the HDATA\_APPOWNED flag in [**DdeCreateDataHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatedatahandle). Doing so gives ownership of the DDE object to the creating application and prevents the DDEML from invalidating the data handle. The application can then pass the data handle any number of times after calling **DdeCreateDataHandle** only once.

If an application specifies the HDATA\_APPOWNED flag in the *afCmd* parameter of [**DdeCreateDataHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatedatahandle), it must call the [**DdeFreeDataHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddefreedatahandle) function to free the memory handle, regardless of whether it passed the handle to the DDEML. Before it terminates, an application must call **DdeFreeDataHandle** to free any data handle that it created but did not pass to the DDEML.

An application that has not yet passed the handle to a DDE object to the DDEML can add data to the object or overwrite data in the object by using the [**DdeAddData**](/windows/desktop/api/Ddeml/nf-ddeml-ddeadddata) function. Typically, an application uses **DdeAddData** to fill an uninitialized DDE object. After an application passes a data handle to the DDEML, the DDE object identified by the handle cannot be changed; it can only be freed.

 

 




