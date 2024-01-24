---
title: IDN Support in WinINet
description: Starting in Windows Server 2008 and Windows Vista, the host portion of the Unicode URL is converted to the Internationalized Domain Name (IDN).
ms.assetid: 7c56908e-f6d0-48dc-9ac1-73f888fb7b6c
ms.topic: article
ms.date: 05/31/2018
---

# IDN Support in WinINet

Starting in Windows Server 2008 and Windows Vista, the host portion of the Unicode URL is converted to the Internationalized Domain Name (IDN). Separate portions of the Unicode URL encoding can also be modified by configurations set by the application. The ANSI versions of the WinINet API continue to send the URL over the wire as entered by the application, however the WinINet Unicode versions of the API now conform to the IDN standard (RFC3490) for URL encodings.

By default, when a URL is entered as a Unicode parameter, the host portion, for both proxy and direct connections, is converted to IDN format. The application has the option to disable IDN host formatting by setting the **INTERNET\_OPTION\_IDN** option. IDN host conversion can be enabled on only the direct or proxy connections by using the **INTERNET\_FLAG\_IDN\_DIRECT** or **INTERNET\_FLAG\_IDN\_PROXY** flags with **INTERNET\_OPTION\_IDN**.

The following code example shows how to disable IDN host conversion for both the proxy and direct connections.

``` syntax
DWORD IDN = 0; 
InternetSetOption( hRequest, 
                   INTERNET_OPTION_IDN,
                   &IDN, 
                   sizeof(DWORD) ); 
```

If IDN host formatting is disabled, the application has the option to specify the desired codepage using **INTERNET\_OPTION\_CODEPAGE**.

The following code example shows how to specify the Japanese code page.

``` syntax
DWORD CP_SHIFT_JIS = 932;  // ANSI/OEM  Japanese, Shift-JIS
InternetSetOption( hRequest, 
                   INTERNET_OPTION_CODEPAGE,
                   &CP_SHIFT_JIS, 
                   Sizeof(DWORD) ); 
```

The path portion of the URL is UTF8 encoded by default, and the remaining segments of the URL, the query or fragment, are converted to the default system code page (CP\_ACP).

The following example shows how to specify the Korean language code page for the path portion of the URL.

``` syntax
DWORD CP_KOREAN = 949;   // ANSI/OEM Korean 
InternetSetOption( hRequest, 
                   INTERNET_OPTION_CODEPAGE_PATH,
                   &CP_KOREAN, 
                   sizeof(DWORD) );
```

The following table defines the options that support IDN. For more information, see the [Option flags](option-flags.md) topic.



| Option                            | Description                                                                                                                                                                                                                     |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INTERNET\_OPTION\_CODEPAGE        | This option is set on the request, or connection handle, to specify a code page encoding scheme for the host portion of the URL. This option is ignored if IDN is enabled.                                                      |
| INTERNET\_OPTION\_CODEPAGE\_PATH  | This option is set on the request, or connection handle enables the specified encoding scheme for the path portion of the URL. By default, the path portion of the URL is UTF8 encoded.                                         |
| INTERNET\_OPTION\_CODEPAGE\_EXTRA | Setting this option on the request, or connection handle enables the specified encoding scheme for the extra portion of the URL. By default, the extra portion of the URL is encoded in the default system code page (CP\_ACP). |
| INTERNET\_OPTION\_IDN             | This option can be used on the request, or connection handle to enable or disable IDN host conversion. When IDN is disabled, WinINet uses the default system codepage to encode the host or authority portion of the URL.       |



 

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

 

 