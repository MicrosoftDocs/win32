---
title: Setting and Retrieving Internet Options
description: This topic describes how to set and retrieve Internet options using the InternetSetOption and InternetQueryOption functions.
ms.assetid: b596a4a9-c34a-402a-af76-b930fe5f0901
keywords:
- Setting and Retrieving Internet Options
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting and Retrieving Internet Options

This topic describes how to set and retrieve Internet options using the [**InternetSetOption**](/windows/win32/Wininet/nf-wininet-internetsetoptiona?branch=master) and [**InternetQueryOption**](/windows/win32/Wininet/nf-wininet-internetqueryoptiona?branch=master) functions.

Internet options can be set on, or retrieved from, a specified [**HINTERNET**](appendix-a-hinternet-handles.md) handle or the current settings in Microsoft Internet Explorer.

-   [Implementation Steps](#implementation-steps)
    -   [Choosing Internet Options](#choosing-internet-options)
    -   [Choosing the HINTERNET Handle](#choosing-the-hinternet-handle)
    -   [Setting or Retrieving the Options](#setting-or-retrieving-the-options)
-   [Scope of HINTERNET Handle](#scope-of-hinternet-handle)
-   [Setting Individual Options](#setting-individual-options)
-   [Retrieving Individual Options](#retrieving-individual-options)
    -   [Complete Sample](#complete-sample)
-   [Setting Connection Options](#setting-connection-options)
-   [Retrieving Connection Options](#retrieving-connection-options)
-   [Related topics](#related-topics)

## Implementation Steps

To set or retrieve Internet options complete the following:

-   [Choosing Internet Options](#choosing-internet-options)
-   [Choosing the HINTERNET Handle](#choosing-the-hinternet-handle)
-   [Setting or Retrieving the Options](#setting-or-retrieving-the-options)

### Choosing Internet Options

Because there are so many Internet options, choosing the right options is important. Many Internet options affect the behavior of the WinINet functions and Internet Explorer:

For example, you can:

-   Handle basic server and proxy authentication by setting user names and passwords.
-   Set or retrieve the user agent string used by servers to identify the features of the client application or browser.
-   Retrieve the handle type of the specified [**HINTERNET**](appendix-a-hinternet-handles.md) handle.

For more information and a list of the Internet options, see [**Option Flags**](option-flags.md).

In Internet Explorer 5 and later, some options can be set or retrieved from a specific Internet connection using the [**INTERNET\_PER\_CONN\_OPTION\_LIST**](/windows/win32/Wininet/ns-wininet-internet_per_conn_option_lista?branch=master) and [**INTERNET\_PER\_CONN\_OPTION**](/windows/win32/Wininet/ns-wininet-internet_per_conn_optiona?branch=master) structures. For more information and a list of options that can be set or retrieved from a specific Internet connection, see the **dwOptions** member of the [**INTERNET\_PER\_CONN\_OPTION**](/windows/win32/Wininet/ns-wininet-internet_per_conn_optiona?branch=master) structure.

### Choosing the HINTERNET Handle

The [**HINTERNET**](appendix-a-hinternet-handles.md) handle used to set or retrieve Internet options determines the scope of the operation. All the handles created through this handle will inherit the options set on this handle.

For example, client applications that require a proxy with authentication, probably do not require setting the proxy user name and password every time the application attempts to access an Internet resource. If all requests on a given connection are handled by the same proxy, setting the proxy user name and password on a connection type [**HINTERNET**](appendix-a-hinternet-handles.md) handle, that is, a handle created by a call to [**InternetConnect**](/windows/win32/Wininet/nf-wininet-internetconnecta?branch=master), would allow any calls derived from this **HINTERNET** handle to use the same proxy user name and password. Setting the proxy user name and password every time an **HINTERNET** handle is created by [**HttpOpenRequest**](/windows/win32/Wininet/nf-wininet-httpopenrequesta?branch=master) would require extra and unnecessary overhead. Be aware that if the application uses a proxy that requires authentication, it should set the proxy credentials on every new connection.

### Setting or Retrieving the Options

When you have determined what Internet options and [**HINTERNET**](appendix-a-hinternet-handles.md) handle to use, retrieve those Internet options. To set or retrieve options, call either [**InternetQueryOption**](/windows/win32/Wininet/nf-wininet-internetqueryoptiona?branch=master) or [**InternetSetOption**](/windows/win32/Wininet/nf-wininet-internetsetoptiona?branch=master).

## Scope of HINTERNET Handle

The [**HINTERNET**](appendix-a-hinternet-handles.md) handle used to set or retrieve Internet options determines the actions for which the options are valid.

These handles have three levels:

-   The root [**HINTERNET**](appendix-a-hinternet-handles.md) handle (created by a call to [**InternetOpen**](/windows/win32/Wininet/nf-wininet-internetopena?branch=master)) would contain all the Internet options that affect this instance of WinINet.
-   [**HINTERNET**](appendix-a-hinternet-handles.md) handles that connect to a server (created by a call to [**InternetConnect**](/windows/win32/Wininet/nf-wininet-internetconnecta?branch=master))
-   [**HINTERNET**](appendix-a-hinternet-handles.md) handles associated with a resource or enumeration of resources on a particular server.

In addition to the various [**HINTERNET**](appendix-a-hinternet-handles.md) handles, an application can also use **NULL** to set or retrieve the default values of the Internet options used by Internet Explorer and the WinINet functions. Setting Internet options when using **NULL** as the handle changes the default values of the options, which are currently stored in the registry. Client applications should not use registry functions to change the default values of the Internet options, because the implementation of how the options are stored can be altered in the future.

The following table lists the type of [**HINTERNET**](appendix-a-hinternet-handles.md) handles and the scope of the Internet options associated with them.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Handle Type</th>
<th>Scope</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>NULL</strong></td>
<td>The default option settings for Internet Explorer.</td>
</tr>
<tr class="even">
<td>INTERNET_HANDLE_TYPE_CONNECT_FTP</td>
<td>The option settings for this connection to an FTP server. These options affect any operations initiated from this [<strong>HINTERNET</strong>](appendix-a-hinternet-handles.md) handle, such as file downloads.</td>
</tr>
<tr class="odd">
<td>INTERNET_HANDLE_TYPE_CONNECT_GOPHER</td>
<td>The option settings for this connection to a Gopher server. These options affect any operations initiated from this [<strong>HINTERNET</strong>](appendix-a-hinternet-handles.md) handle, such as file downloads.
<blockquote>
[!Note]<br />
Windows XP and Windows Server 2003 R2 and earlier only.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>INTERNET_HANDLE_TYPE_CONNECT_HTTP</td>
<td>The option settings for this connection to an HTTP server. These options affect any operations initiated from this [<strong>HINTERNET</strong>](appendix-a-hinternet-handles.md) handle, such as file downloads.</td>
</tr>
<tr class="odd">
<td>INTERNET_HANDLE_TYPE_FILE_REQUEST</td>
<td>The option settings associated with this file request.</td>
</tr>
<tr class="even">
<td>INTERNET_HANDLE_TYPE_FTP_FILE</td>
<td>The option settings associated with this FTP resource download.</td>
</tr>
<tr class="odd">
<td>INTERNET_HANDLE_TYPE_FTP_FILE_HTML</td>
<td>The option settings associated with this FTP resource download formatted in HTML.</td>
</tr>
<tr class="even">
<td>INTERNET_HANDLE_TYPE_FTP_FIND</td>
<td>The option settings associated with this search of files on an FTP server.</td>
</tr>
<tr class="odd">
<td>INTERNET_HANDLE_TYPE_FTP_FIND_HTML</td>
<td>The option settings associated with this search of files on an FTP server formatted in HTML.</td>
</tr>
<tr class="even">
<td>INTERNET_HANDLE_TYPE_GOPHER_FILE</td>
<td>The option settings associated with this Gopher resource download.
<blockquote>
[!Note]<br />
Windows XP and Windows Server 2003 R2 and earlier only.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>INTERNET_HANDLE_TYPE_GOPHER_FILE_HTML</td>
<td>The option settings associated with this Gopher resource download formatted in HTML.
<blockquote>
[!Note]<br />
Windows XP and Windows Server 2003 R2 and earlier only.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>INTERNET_HANDLE_TYPE_GOPHER_FIND</td>
<td>The option settings associated with this search of files on an Gopher server.
<blockquote>
[!Note]<br />
Windows XP and Windows Server 2003 R2 and earlier only.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>INTERNET_HANDLE_TYPE_GOPHER_FIND_HTML</td>
<td>The option settings associated with this search of files on an Gopher server formatted in HTML.
<blockquote>
[!Note]<br />
Windows XP and Windows Server 2003 R2 and earlier only.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>INTERNET_HANDLE_TYPE_HTTP_REQUEST</td>
<td>The option settings associated with this HTTP request.</td>
</tr>
<tr class="odd">
<td>INTERNET_HANDLE_TYPE_INTERNET</td>
<td>The option settings associated with this instance of the WinINet functions.</td>
</tr>
</tbody>
</table>



 

## Setting Individual Options

After determining the Internet options you want to set and the scope you want affected by these options, setting Internet options is not complicated. All you would need to do is call the [**InternetSetOption**](/windows/win32/Wininet/nf-wininet-internetsetoptiona?branch=master) function with desired [**HINTERNET**](appendix-a-hinternet-handles.md) handle, Internet option flag, and a buffer that contains the information you want set.

The following example shows how to set the proxy user name and password on a specified [**HINTERNET**](appendix-a-hinternet-handles.md) handle.


```C++
// strUsername is a string buffer of cchMax characters or less.
// It contains the proxy user name.
size_t cchMax = 80;
size_t cchUserLength, cchPasswordLength;
HRESULT hr = StringCchLength(strUsername, cchMax, &amp;cchUserLength);

if (SUCCEEDED(hr))
{
   // hOpen is the HINTERNET handle created by InternetConnect.
   InternetSetOption(hConnect, INTERNET_OPTION_PROXY_USERNAME,
      strUsername, DWORD(cchUserLength)+1);
}
else
{
   // Insert error handling code here.
}

// strPassword is the string buffer that contains the proxy password.
hr = StringCchLength(strPassword, cchMax, &amp;cchPasswordLength);

InternetSetOption(hOpen, INTERNET_OPTION_PROXY_PASSWORD,
    strPassword, DWORD(cchPasswordLength)+1);
```



## Retrieving Individual Options

Internet options can be retrieved using the [**InternetQueryOption**](/windows/win32/Wininet/nf-wininet-internetqueryoptiona?branch=master) function. To retrieve Internet options:

1.  Determine the buffer size necessary to retrieve the Internet option information.

    The buffer size can be determined by using **NULL** for the address of the buffer and passing it a buffer size of zero.

    ```C++
    DWORD dwSize;
    InternetQueryOption(NULL, INTERNET_OPTION_USER_AGENT, NULL, &amp;dwSize);
    ```

    

    The value returned by [**InternetQueryOption**](/windows/win32/Wininet/nf-wininet-internetqueryoptiona?branch=master) is the amount of memory required to retrieve the information, in bytes.

2.  Allocate a memory for the buffer.
    ```C++
    char *lpszData;
    lpszData = new char[dwSize];
    ```

    

3.  Retrieve the data.
    ```C++
    InternetQueryOption( NULL, 
                         INTERNET_OPTION_USER_AGENT,
                         lpszData, &amp;dwSize );
    ```

    

4.  Free the memory.
    ```C++
    delete [] lpszData;
    ```

    

### Complete Sample

The following is the complete sample used in the previous section. This sample shows how to retrieve the default user agent string.


```C++
// This call determines the required buffer size.
DWORD dwSize;
InternetQueryOption(NULL, INTERNET_OPTION_USER_AGENT, NULL, &amp;dwSize);

// Allocate the necessary memory.
char *lpszData;
lpszData = new char[dwSize];

// Call InternetQueryOption again with the provided buffer.
InternetQueryOption( NULL, 
                     INTERNET_OPTION_USER_AGENT,
                     lpszData, &amp;dwSize );

// Insert code here to use the user agent string data.

// Free the allocated memory.
delete [] lpszData;
```



## Setting Connection Options

In Internet Explorer 5 and later, Internet options can be set for on a specific connection. Previously, all connections shared the same Internet option settings. To set options for a particular connection:

1.  Create an [**INTERNET\_PER\_CONN\_OPTION\_LIST**](/windows/win32/Wininet/ns-wininet-internet_per_conn_option_lista?branch=master) structure.
2.  Allocate the memory for the individual Internet options that you want to set for the connection.
3.  Set the options in [**INTERNET\_PER\_CONN\_OPTION**](/windows/win32/Wininet/ns-wininet-internet_per_conn_optiona?branch=master) structures.
4.  Set the options using [**InternetSetOption**](/windows/win32/Wininet/nf-wininet-internetsetoptiona?branch=master).

The following code example shows how to set proxy data for a LAN connection.


```C++
BOOL SetConnectionOptions()
{
    INTERNET_PER_CONN_OPTION_LIST list;
    BOOL    bReturn;
    DWORD   dwBufSize = sizeof(list);

    // Fill the list structure.
    list.dwSize = sizeof(list);

    // NULL == LAN, otherwise connectoid name.
    list.pszConnection = NULL;

    // Set three options.
    list.dwOptionCount = 3;
    list.pOptions = new INTERNET_PER_CONN_OPTION[3];

    // Ensure that the memory was allocated.
    if(NULL == list.pOptions)
    {
        // Return FALSE if the memory wasn't allocated.
        return FALSE;
    }

    // Set flags.
    list.pOptions[0].dwOption = INTERNET_PER_CONN_FLAGS;
    list.pOptions[0].Value.dwValue = PROXY_TYPE_DIRECT |
        PROXY_TYPE_PROXY;

    // Set proxy name.
    list.pOptions[1].dwOption = INTERNET_PER_CONN_PROXY_SERVER;
    list.pOptions[1].Value.pszValue = TEXT("http://proxy:80");

    // Set proxy override.
    list.pOptions[2].dwOption = INTERNET_PER_CONN_PROXY_BYPASS;
    list.pOptions[2].Value.pszValue = TEXT("local");

    // Set the options on the connection.
    bReturn = InternetSetOption(NULL,
        INTERNET_OPTION_PER_CONNECTION_OPTION, &amp;list, dwBufSize);

    // Free the allocated memory.
    delete [] list.pOptions;

    return bReturn;
}
```



## Retrieving Connection Options

In Internet Explorer 5 and later, Internet options can be retrieved from a specific connection. To retrieve options from a particular connection:

1.  Create a [**INTERNET\_PER\_CONN\_OPTION\_LIST**](/windows/win32/Wininet/ns-wininet-internet_per_conn_option_lista?branch=master) structure.
2.  Allocate the memory for the individual Internet options to retrieve from the connection.
3.  Specify the options using [**INTERNET\_PER\_CONN\_OPTION**](/windows/win32/Wininet/ns-wininet-internet_per_conn_optiona?branch=master) structures.
4.  Retrieve the options using [**InternetQueryOption**](/windows/win32/Wininet/nf-wininet-internetqueryoptiona?branch=master).
5.  Utilize the option data.
6.  Free the memory, allocated to hold the option data, using the [**GlobalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366579) function.

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](https://msdn.microsoft.com/library/windows/desktop/aa384273).

 

## Related topics

<dl> <dt>

[Handling Authentication](handling-authentication.md)
</dt> <dt>

[HINTERNET Handles](appendix-a-hinternet-handles.md)
</dt> </dl>

 

 





