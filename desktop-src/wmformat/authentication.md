---
title: Authentication (Windows Media Format 11 SDK)
description: Authentication
ms.assetid: 9c181615-e864-4588-846f-d04d73824f5f
keywords:
- Windows Media Format SDK,authentication
- Windows Media Format SDK,network authentication
- Advanced Systems Format (ASF),authentication
- ASF (Advanced Systems Format),authentication
- Advanced Systems Format (ASF),network authentication
- ASF (Advanced Systems Format),network authentication
- authentication
- network authentication,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Authentication (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The reader object can handle network authentication challenges, including digest authentication and NTLM authentication. In some cases the application must provide the user's credentials through a callback interface:

-   Digest authentication: The application must implement the **IWMCredentialCallback** interface, as described later in this topic.
-   NTLM authentication: The reader automatically responds with the user's logon credentials. If the current user is authorized to log on to the server, the application does not have to do anything. If the user does not have authorization, the application must implement the **IWMCredentialCallback** interface.

    > [!Note]  
    > Windows Media Services version 4.1 does not support NTLM authentication through a proxy server. NTLM authentication requires several client-server exchanges on the same connection, and version 4.1 does not keep a persistent connection with the proxy. Windows Media Services 9 Series in Microsoft Windows Server 2003 supports NTLM authentication through a proxy server, as long as the proxy supports keep-alive connections.

     

As noted, in some cases the application must provide the user's credentials. This occurs through the **IWMCredentialCallback** interface, which has a single method, **AcquireCredentials**. To support authentication, implement this interface in your application. The reader object queries for this interface by calling **QueryInterface** on the [**IWMReaderCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadercallback) pointer that it received from the application in the [**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open) method. If the reader object needs to get the user's credentials, it calls the application's **AcquireCredentials** method.

If the credentials will be sent over the network without encryption, the reader sets the WMT\_CREDENTIAL\_CLEAR\_TEXT flag in the *pdwFlags* parameter. This gives the application an opportunity to warn the user that his or her credentials will be sent in plain text.

Otherwise, the reader object automatically encrypts the credentials before sending them over the network. The application can return them to the reader object in plain text. In addition, if the reader object sets the WMT\_CREDENTIAL\_ENCRYPT flag, it means the reader supports getting encrypted credentials from the application. In that case, the application can either return the credentials in plain text, or else encrypt them itself using the **CryptProtectData** function, which is described in the Platform SDK documentation. If the application encrypts the credentials, it must set the WMT\_CREDENTIAL\_ENCRYPT flag in the *pdwFlags* parameter before the method returns.

Generally, it is not necessary to encrypt the data, because the reader object encrypts the data if necessary. However, encryption might be useful if the application keeps the user name and password in memory, because it prevents an attacker from inspecting a memory dump of the process.

## Related topics

<dl> <dt>

[**IWMCredentialCallback Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcredentialcallback)
</dt> <dt>

[**IWMReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader)
</dt> </dl>

 

 




