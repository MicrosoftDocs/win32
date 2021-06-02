---
description: Supported Protocols
ms.assetid: 3c026426-c2b7-4909-9524-9cc0bd45347e
title: Supported Protocols
ms.topic: article
ms.date: 05/31/2018
---

# Supported Protocols

Media Foundation supports the following protocols:

-   Real Time Streaming Protocol (RTSP)

    RTSP is mainly used for streaming media content. It can use UDP or TCP as transport protocols. UDP is the most efficient for content delivery because the bandwidth overhead is less than with TCP-based protocols. Even though the TCP protocol ensures reliable packet delivery, TCP is not well suited for digital media streams, where efficient use of bandwidth is more important than occasional lost packets.

-   Hypertext Transfer Protocol (HTTP)

    HTTP uses TCP and is used by web servers. The "httpd://" scheme indicates that the source is downloadable from a web server. HTTP is also used in case of firewalls, which are usually configured to accept HTTP requests and typically reject other streaming protocols.

The application can get the protocols supported by Media Foundation by using the [**IMFNetSchemeHandlerConfig**](/windows/desktop/api/mfidl/nn-mfidl-imfnetschemehandlerconfig) interface. To do this, the application must first retrieve the number of protocols, by calling [**IMFNetSchemeHandlerConfig::GetNumberOfSupportedProtocols**](/windows/desktop/api/mfidl/nf-mfidl-imfnetschemehandlerconfig-getnumberofsupportedprotocols) and then get the protocol type based on the index by calling [**IMFNetSchemeHandlerConfig::GetSupportedProtocolType**](/windows/desktop/api/mfidl/nf-mfidl-imfnetschemehandlerconfig-getsupportedprotocoltype). This method returns one of the values defined in the [**MFNETSOURCE\_PROTOCOL\_TYPE**](/windows/desktop/api/mfidl/ne-mfidl-mfnetsource_protocol_type) enumeration.

The application can also get the schemes supported by the source resolver by calling the [**MFGetSupportedSchemes**](/windows/desktop/api/mfidl/nf-mfidl-mfgetsupportedschemes) function.

## Protocol Rollover

When an application specifies "mms://" as the URL scheme, the source resolver performs a *protocol rollover* operation. In this process, the source resolver determines the best protocol for the network source to use for getting the content. Typically, for media steaming, RTSP with UDP (RTSPU) is more efficient than HTTP. However, if the content is hosted on a web server, HTTP is a better choice.

Protocol rollover can also occur when an attempt to use the protocol specified in the URL scheme fails. For example, a protocol can fail when a firewall blocks UDP packets. In this case, the source resolver switches to HTTP.

Protocol rollover does not apply if the URL scheme contains a specific protocol, such as "rtspu://". Also, rollover is not performed if authentication fails or the server has reached a limit of client connections. It is recommended that applications specify the "mms://" scheme and allow the source resolver to select the best protocol for the scenario.

The following table lists the rollover order.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Schemes allowed</th>
<th>Protocol rollover order</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>mms:// or rtsp://</td>
<td>Fast Cache enabled:<br/>
<ol>
<li>RTSP with TCP (RTSPT)<br/></li>
<li>RTSP with UDP (RTSPU)<br/></li>
<li>HTTP Streaming<br/></li>
<li>HTTP download (HTTPD)<br/></li>
</ol>
Fast Cache disabled:<br/>
<ol>
<li>RTSPU<br/></li>
<li>RTSPT<br/></li>
<li>HTTP Streaming<br/></li>
<li>HTTP Download<br/></li>
</ol></td>
</tr>
<tr class="even">
<td>rtspu://</td>
<td>RTSPU</td>
</tr>
<tr class="odd">
<td>rtspt://</td>
<td>RTSPT</td>
</tr>
<tr class="even">
<td>https://</td>
<td><ol>
<li>HTTP<br/></li>
<li>HTTPD<br/></li>
</ol></td>
</tr>
<tr class="odd">
<td>httpd://</td>
<td>HTTPD</td>
</tr>
</tbody>
</table>



 

## Retrieving the Current Protocol

After a protocol rollover operation, the network source might use a protocol other than the one specified by the application in the URL scheme. The protocol rollover result is available to the application after the network source establishes the connection with the media server.

To get the protocol and transport that are used for getting the content, the application can retrieve the property values for the [MFNETSOURCE\_PROTOCOL](mfnetsource-protocol-property.md) property and the [MFNETSOURCE\_TRANSPORT](mfnetsource-transport-property.md) property of an **IPropertyStore** object from the network source.

The following code shows how to get these values.


```C++
// Create an IPropertyStore object.
    IPropertyStore *pProp = NULL;
    hr = CreatePropertyStore(&pProp);

    PROPVARIANT var;
    PropVariantInit(&var);

// Get the property store from the network source.
// The network source is created by the source resolver. Not shown.
    if (SUCCEEDED(hr))
    {
        hr = pNetworkSource->QueryInterface 
                (__uuidof(IPropertyStore), 
                (void**)&pProp);
    }
    if (SUCCEEDED(hr))
    {
        // Create a property key.
        PROPERTYKEY key;
        // Get the MFNETSOURCE_PROTOCOL property value.
        key.fmtid = MFNETSOURCE_PROTOCOL;
        hr = pProp->GetValue (key, &var);

        // Get the MFNETSOURCE_TRANSPORT property value.
        key.fmtid = MFNETSOURCE_TRANSPORT;
        key.pid = 0;
        hr = pProp->GetValue (key, &var);

    }
```



In the preceding example code, **IPropertyStore::GetValue** retrieves the MFNETSOURCE\_PROTOCOL value, which is a member of the [**MFNETSOURCE\_PROTOCOL\_TYPE**](/windows/desktop/api/mfidl/ne-mfidl-mfnetsource_protocol_type) enumeration. For MFNETSOURCE\_TRANSPORT, the value is a member of the [**MFNETSOURCE\_TRANSPORT\_TYPE**](/windows/desktop/api/mfidl/ne-mfidl-mfnetsource_transport_type) enumeration.

Alternately, the application can get the same values by using the MFNETSOURCE\_STATISTICS\_SERVICE service. To use this service, the application can call the [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) function to get the property store from the network source. This property store contains network statistics in the [MFNETSOURCE\_STATISTICS](mfnetsource-statistics-property.md) property. Protocol and transport values can be retrieved by specifying MFNETSOURCE\_PROTOCOL\_ID and MFNETSOURCE\_TRANSPORT\_ID—defined in the [**MFNETSOURCE\_STATISTICS\_IDS**](/windows/desktop/api/mfidl/ne-mfidl-mfnetsource_statistics_ids) enumeration. The following code shows how to get the protocol and transport values by using the MFNETSOURCE\_STATISTICS\_SERVICE service.


```C++
// Create an IPropertyStore object.
    IPropertyStore *pProp = NULL;
    hr = CreatePropertyStore(&pProp);

    HRESULT hr = S_OK;

    hr = MFGetService(
        pMediaSource, 
        MFNETSOURCE_STATISTICS_SERVICE, 
        IID_IPropertyStore, 
        (void**) & pProp); 

    if (SUCCEEDED(hr))
    {
        // Create a property key.
        PROPERTYKEY key;
        // Get the property value.
        key.fmtid = MFNETSOURCE_STATISTICS;
        key.pid = MFNETSOURCE_PROTOCOL_ID;
        hr = pProp->GetValue (key, &var);

        // Get the transport value.
        key.fmtid = MFNETSOURCE_STATISTICS;
        key.pid = MFNETSOURCE_TRANSPORT_ID;
        hr = pProp->GetValue (key, &var);

    }
```



## Enabling and Disabling Protocols

The application can configure the network source so that certain protocols are skipped during the rollover process. To do this, network source properties are used to disable specific protocols. The following table shows the properties and the protocols they control.



| Property                                                                    | Description                                 |
|-----------------------------------------------------------------------------|---------------------------------------------|
| [MFNETSOURCE\_ENABLE\_HTTP](mfnetsource-enable-http-property.md)           | Enables or disables HTTP and HTTPD.         |
| [MFNETSOURCE\_ENABLE\_RTSP](mfnetsource-enable-rtsp-property.md)           | Enables or disables RTSPU and RTSPT.        |
| [MFNETSOURCE\_ENABLE\_TCP](mfnetsource-enable-tcp-property.md)             | Enables or disables RTSPT.                  |
| [MFNETSOURCE\_ENABLE\_UDP](mfnetsource-enable-udp-property.md)             | Enables or disables RTSPU.                  |
| [MFNETSOURCE\_ENABLE\_DOWNLOAD](mfnetsource-enable-download-property.md)   | Enables or disables HTTPD.                  |
| [MFNETSOURCE\_ENABLE\_STREAMING](mfnetsource-enable-streaming-property.md) | Enables or disables RTSPU, RTSPT, and HTTP. |



 

## Related topics

<dl> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 




