---
title: Detecting Whether a Remote Computer Supports WS-Management Protocol
description: You can use the Session.Identify or IWSManSession.Identify methods to determine if the remote computer has a service that supports the WS-Management protocol.
ms.assetid: 4d11ac02-fa8b-45d7-bceb-a18f561bc928
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Detecting Whether a Remote Computer Supports WS-Management Protocol

You can use the [**Session.Identify**](session-identify.md) or [**IWSManSession.Identify**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmansession-identify) methods to determine if the remote computer has a service that supports the WS-Management protocol.

If a WS-Management protocol service is configured on the remote computer and is listening for requests, the service can detect an Identify request by the following XML in the header.


```XML
xmlns:wsmid="https://schemas.dmtf.org/wbem/wsman/identity/1/wsmanidentity"
```



The WS-Management protocol service that receives the request returns the information, contained in the following list, in the body of the message:

-   The WS-Management protocol version. For example, "https://schemas.dmtf.org/wbem/wsman/1/wsman".
-   The product vendor, for example, "Microsoft Corporation".
-   The product version. If the request is sent with **WSManFlagUseNoAuthentication** in the *flags* parameter, then no product version information is returned. If the request is sent with either the default authentication in effect or with another authentication mode specified, then the product version information can be returned.

The request to detect whether the remote computer has a configured and listening WS-Management protocol service can be performed at the beginning of a script with other operations. This will verify that the target computer or computers can respond to further WS-Management protocol requests. The verification also can be done in a separate script.

**To detect a WS-Management protocol service**

1.  Create a [**WSMan**](wsman.md) object.

    ```VB
    Set objWsman = CreateObject("Wsman.Automation")
    ```

    

2.  Determine whether the request should be sent authenticated or unauthenticated and set the *flags* parameter accordingly in the call to [**WSMan.CreateSession**](wsman-createsession.md).

    ```VB
    set objSession = objWsman.CreateSession("Remote1", _
       objWsman.SessionFlagUseNoAuthentication)
    ```

    

3.  Call [**Session.Identify**](session-identify.md).

    ```VB
    objSession.Identify
    ```

    

## Examples

The following VBScript code example sends an unauthenticated Identify request to the remote computer named "Remote1" in the same domain.


```VB
set objWsman = CreateObject("Wsman.Automation")
set objSession = objWsman.CreateSession("Remote1", _
  objWsman.SessionFlagUseNoAuthentication)
WScript.Echo objSession.Identify
```



The following response shows the XML returned by the remote computer. The WS-Management protocol version ("https://schemas.dmtf.org/wbem/wsman/1/wsman.xsd") and the operating system vendor ("Microsoft Corporation") are specified in the returned XML. Because the message is sent unauthenticated, the product version is not returned by the Windows Remote Management service.


```XML
<wsmid:IdentifyResponse xmlns:wsmid=
    "https://schemas.dmtf.org/wbem/wsman/identity/1/wsmanidentity.xsd">
<wsmid:ProtocolVersion>https://schemas.dmtf.org/wbem/wsman/1/wsman.xsd
    </wsmid:ProtocolVersion>
<wsmid:ProductVendor>Microsoft Corporation</wsmid:ProductVendor>
<wsmid:ProductVersion>OS: 0.0.0 SP: 0.0 Stack:1.0</wsmid:ProductVersion>
</wsmid:IdentifyResponse>
```



The following VBScript code example sends an authenticated Identify request to the remote computer.


```VB
set ObjWSMan = CreateObject("Wsman.Automation")
set objSession = WSMan.CreateSession("Remote1", _
  objWSMan.SessionFlagUseKerberos)
WScript.Echo objSession.Identify
```



Because the request was sent with authentication, the version information is returned.


```XML
<wsmid:IdentifyResponse xmlns:wsmid=
    "https://schemas.dmtf.org/wbem/wsman/identity/1/wsmanidentity.xsd">
<wsmid:ProtocolVersion>https://schemas.dmtf.org/wbem/wsman/1/wsman.xsd
    </wsmid:ProtocolVersion>
<wsmid:ProductVendor>Microsoft Corporation</wsmid:ProductVendor>
<wsmid:ProductVersion>OS: 6.0.5384 SP: 0.0 Stack:1.0</wsmid:ProductVersion>
</wsmid:IdentifyResponse>
```



## Related topics

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Using Windows Remote Management](using-windows-remote-management.md)
</dt> <dt>

[Windows Remote Management Reference](windows-remote-management-reference.md)
</dt> </dl>

 

 




