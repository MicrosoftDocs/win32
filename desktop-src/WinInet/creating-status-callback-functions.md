---
title: Creating Status Callback Functions
description: This tutorial describes how to create a status callback function used to monitor the status of an Internet request.
ms.assetid: 518d0800-5ea6-4327-8459-901e6d9a8a5a
ms.topic: article
ms.date: 05/31/2018
---

# Creating Status Callback Functions

This tutorial describes how to create a status callback function used to monitor the status of an Internet request.

Status callback functions receive status callbacks on any Internet requests that originated from any WinINet function that was passed a nonzero context value.


The following steps are necessary for creating a status callback function:

1.  [Define the context value.](#defining-the-context-value)
2.  [Create the status callback function.](#creating-status-callback-functions)

### Defining the Context Value

The context value can be any unsigned long integer value. Ideally, the context value should identify what request has just been completed and the location of any associated resources, if needed.

One of the most useful ways to use the context value is to pass the address of a structure and cast it to a **DWORD\_PTR**. The structure can be used to store information about the request, so that it is passed to the status callback function.

The following structure is an example of a possible context value. The members of the structure are chosen with the [**InternetOpenUrl**](/windows/desktop/api/Wininet/nf-wininet-internetopenurla) function in mind.


```C++
typedef struct{
    HWND       hWindow;      // Window handle
    int        nStatusList;  // List box control to hold callbacks
    HINTERNET  hResource;    // HINTERNET handle created by InternetOpenUrl
    char       szMemo[512];  // String to store status memo
} REQUEST_CONTEXT;
```



In this example, the status callback function would have access to the window handle, which would allow it to display a user interface. The [**HINTERNET**](appendix-a-hinternet-handles.md) handle created by [**InternetOpenUrl**](/windows/desktop/api/Wininet/nf-wininet-internetopenurla) could be passed to another function that can download the resource and an array of characters that can be used to pass information about the request.

The members of the structure can be changed to fit the needs of a particular application, so do not feel constrained by this example.

### Creating the Status Callback Function

The status callback function must follow the format of [*InternetStatusCallback*](/windows/desktop/api/Wininet/nc-wininet-internet_status_callback). To do this:

1.  Write a function declaration for your status callback function.

    The following example shows a sample declaration.

    ```C++
    void CALLBACK CallMaster( HINTERNET,
                              DWORD_PTR,
                              DWORD,
                              LPVOID,
                              DWORD );
    ```

    

2.  Determine what your status callback function will do. For applications that are making asynchronous calls, the status callback function must handle the INTERNET\_STATUS\_REQUEST\_COMPLETE value, which indicates an asynchronous request is complete. The status callback function can also be used to track the progress of an Internet request.

    In general, it works best to use a switch statement with *dwInternetStatus* as the switch value and the status values for the case statements. Depending on the types of functions your application is calling, you can ignore some of the status values. For a definition of the different status values, see the listing under the *dwInternetStatus* parameter of [*InternetStatusCallback*](/windows/desktop/api/Wininet/nc-wininet-internet_status_callback).

    The following switch statement is an example of how to handle status callbacks.

    ``` syntax
    switch (dwInternetStatus)
    {
        case INTERNET_STATUS_REQUEST_COMPLETE:
            // Add code
            break;
        default:
            // Add code
            break;
    }
    ```

3.  Create the code to handle the status values.

    The code to handle each of the status values depends heavily on your intended use of the status callback function. For applications that are just tracking the progress of a request, writing a string to a list box might be all you need. For asynchronous operations, the code must handle some of the data returned in the callback.

    The following status callback function uses a switch function to determine what the status value is and creates a string that includes the name of the status value and the previous function called, which is stored in the szMemo member of the REQUEST\_CONTEXT structure.

    ```C++
    void __stdcall CallMaster(
        HINTERNET hInternet,
        DWORD_PTR dwContext,
        DWORD dwInternetStatus,
        LPVOID lpvStatusInformation,
        DWORD dwStatusInformationLength
    )
    {
        UNREFERENCED_PARAMETER(hInternet);
        UNREFERENCED_PARAMETER(lpvStatusInformation);
        UNREFERENCED_PARAMETER(dwStatusInformationLength);

        REQUEST_CONTEXT *cpContext;
        cpContext = (REQUEST_CONTEXT*)dwContext;
        char szStatusText[80];

        switch (dwInternetStatus)
        {
            case INTERNET_STATUS_CLOSING_CONNECTION:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s CLOSING_CONNECTION",
                                  cpContext->szMemo);
                break;
            case INTERNET_STATUS_CONNECTED_TO_SERVER:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s CONNECTED_TO_SERVER",
                                  cpContext->szMemo );
                break;
            case INTERNET_STATUS_CONNECTING_TO_SERVER:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s CONNECTING_TO_SERVER",
                                  cpContext->szMemo );
                break;
            case INTERNET_STATUS_CONNECTION_CLOSED:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s CONNECTION_CLOSED",
                                  cpContext->szMemo );
                break;
            case INTERNET_STATUS_HANDLE_CLOSING:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s HANDLE_CLOSING",
                                  cpContext->szMemo );
                break;
            case INTERNET_STATUS_HANDLE_CREATED:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s HANDLE_CREATED",
                                  cpContext->szMemo);
                break;
            case INTERNET_STATUS_INTERMEDIATE_RESPONSE:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s INTERMEDIATE_RESPONSE",
                                  cpContext->szMemo );
                break;
            case INTERNET_STATUS_NAME_RESOLVED:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s NAME_RESOLVED",
                                  cpContext->szMemo);
                break;
            case INTERNET_STATUS_RECEIVING_RESPONSE:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s RECEIVING_RESPONSE",
                                  cpContext->szMemo);
                break;
            case INTERNET_STATUS_RESPONSE_RECEIVED:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s RESPONSE_RECEIVED",
                                  cpContext->szMemo);
                break;
            case INTERNET_STATUS_REDIRECT:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s REDIRECT",
                                  cpContext->szMemo );
                break;
            case INTERNET_STATUS_REQUEST_COMPLETE:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s REQUEST_COMPLETE",
                                  cpContext->szMemo);
                break;
            case INTERNET_STATUS_REQUEST_SENT:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s REQUEST_SENT",
                                  cpContext->szMemo);
                break;
            case INTERNET_STATUS_RESOLVING_NAME:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s RESOLVING_NAME",
                                  cpContext->szMemo );
                break;
            case INTERNET_STATUS_SENDING_REQUEST:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s SENDING_REQUEST",
                                  cpContext->szMemo );
                break;
            case INTERNET_STATUS_STATE_CHANGE:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s STATE_CHANGE",
                                  cpContext->szMemo );
                break;
            default:
                StringCchPrintfA( szStatusText,
                                  80,
                                  "%s Unknown Status %d Given",
                                  cpContext->szMemo,
                                  dwInternetStatus);
                break;
        }

        SendDlgItemMessage( cpContext->hWindow,
                          cpContext->nStatusList,
                          LB_ADDSTRING,
                          0, (LPARAM)szStatusText );

    }
    ```

    

4.  Use the [**InternetSetStatusCallback**](/windows/desktop/api/Wininet/nf-wininet-internetsetstatuscallback) function to set the status callback function on the [**HINTERNET**](appendix-a-hinternet-handles.md) handle for which you want to receive status callbacks.

    The following example demonstrates how to set a status callback function.

    ```C++
    HINTERNET hOpen;                       // Root HINTERNET handle
    INTERNET_STATUS_CALLBACK iscCallback;  // Holds the callback function

    // Create the root HINTERNET handle.
    hOpen = InternetOpen( TEXT("Test Application"),
                          INTERNET_OPEN_TYPE_PRECONFIG,
                          NULL, NULL, 0);

    // Set the status callback function.
    iscCallback = InternetSetStatusCallback( hOpen, (INTERNET_STATUS_CALLBACK)CallMaster );
    ```

    

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

## Related topics

<dl> <dt>

[Creating Status Callback Functions](creating-status-callback-functions.md)
</dt> <dt>

[**InternetSetStatusCallback**](/windows/desktop/api/Wininet/nf-wininet-internetsetstatuscallback)
</dt> <dt>

[*InternetStatusCallback*](/windows/desktop/api/Wininet/nc-wininet-internet_status_callback)
</dt> </dl>

 

 