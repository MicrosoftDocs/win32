---
title: Client Logging (Windows Media Format 11 SDK)
description: Learn about client logging for Windows Media Format 11 SDK. Logging provides a way for the media server to track the activity of the clients that connect to it.
ms.assetid: 3e0d0fea-4370-41f8-b461-73a37de8d8bc
keywords:
- Windows Media Format SDK,client logging
- Windows Media Format SDK,logging
- Advanced Systems Format (ASF),client logging
- ASF (Advanced Systems Format),client logging
- Advanced Systems Format (ASF),logging
- ASF (Advanced Systems Format),logging
- client logging
- logging clients
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Client Logging (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When the reader object reads data from a server, it sends logging information to the server. Content providers typically use this information to measure quality of service, generate billing information, or track advertising. The logging information contains no personal data.

The application can specify some of the information that is logged, by calling the [**IWMReaderAdvanced::SetClientInfo**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-setclientinfo) method on the reader object. For example, you can specify the user-agent string, the name of the player application, or the Web page that hosts the player.

The logging information includes a GUID that identifies the session. By default, the reader generates an anonymous session ID. Optionally, the reader can instead send an ID that uniquely identifies the current user. To enable this feature, call the [**IWMReaderAdvanced2::SetLogClientID**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setlogclientid) method with the value **TRUE**.

You can configure the reader object to send the logging information to another server, in addition to the originating server. To do so, call the [**IWMReaderNetworkConfig::AddLoggingUrl**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadernetworkconfig-addloggingurl) method with the URL of the server. This URL should point to a script or executable that can handle HTTP GET and POST requests. You can use the Multicast and Logging Advertisement Agent (wmsiislog.dll), or you can write a custom ASP or CGI script to receive the log data.

> [!Note]  
> You can get the same functionality by creating a server-side playlist with a **logURL** attribute.

 

When the reader object sends the log, it does the following:

1.  Sends an empty GET request to the server.
2.  Parses the server response for one of the following strings:
    -   `<body><h1>NetShow ISAPI Log Dll</h1>`
    -   `<body><h1>WMS ISAPI Log Dll/0.0.0.0</h1>` where "0.0.0.0" is any valid version number.
3.  Sends a POST request with the log information.

The following code shows an example ASP script that receives the logging information and writes it to a file:


```
<html>
<body>
<h1>WMS ISAPI Log Dll/9.00.00.00.00</h1>
<%@ Language=VBScript %>
<%
  Dim temp, i, post, file, fso

  ' Convert the binary data to a string.
  For i = 1 To Request.TotalBytes
    temp = Request.BinaryRead(1)
    pose = pose & Chr(AscB(temp))
  Next

  Set fso = createobject("Scripting.FileSystemObject")
  Set file = fso.OpenTextFile("C:\log.txt", 8, TRUE)

  file.writeline Now
  file.writeline post
  file.writeBlankLines 2 
%>
</body>
</html>
```



You can specify multiple servers to receive logging information; just call **AddLoggingUrl** once with each URL. To clear the list of servers that receive logs, call the [**IWMReaderNetworkConfig::ResetLoggingUrlList**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreadernetworkconfig-resetloggingurllist) method.

## Related topics

<dl> <dt>

[**Implementing Network Functionality**](implementing-network-functionality.md)
</dt> <dt>

[**IWMReaderAdvanced Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced)
</dt> <dt>

[**IWMReaderAdvanced2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2)
</dt> </dl>

 

 




