---
title: Implementing a Custom Audio Endpoint Enumerator
description: Beginning with Windows Server 2008 R2, you can implement a custom remote audio endpoint enumerator as part of a Remote Desktop protocol provider.
ms.assetid: 684bd62e-1e28-4330-a3c5-6bce684d652d
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Custom Audio Endpoint Enumerator

Beginning with Windows Server 2008 R2, you can implement a custom remote audio endpoint enumerator as part of a Remote Desktop protocol provider. A Remote Desktop protocol provider can use a custom audio endpoint enumerator to retrieve a collection of audio endpoints that have a specific set of capabilities.

**To implement a custom remote audio endpoint enumerator**

1.  Your custom endpoint enumerator solution should implement four main types of objects: device enumerator objects, device collection objects, device objects, and property store objects.

    

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Object type</th>
    <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td>Device enumerator object<br/></td>
    <td>A device enumerator object provides the endpoint enumerator functionality. It exposes methods that return a default endpoint and specified collections of endpoints. For example, depending on the criteria specified, the enumerator can return communication endpoints, playback endpoints, or capture endpoints. The device enumerator object must implement the <a href="https://msdn.microsoft.com/library/windows/desktop/dd371399"><strong>IMMDeviceEnumerator</strong></a> interface.<br/></td>
    </tr>
    <tr class="even">
    <td>Device collection object<br/></td>
    <td>A device collection object represents a collection of audio devices. It must implement the <a href="https://msdn.microsoft.com/library/windows/desktop/dd371396"><strong>IMMDeviceCollection</strong></a> interface.<br/></td>
    </tr>
    <tr class="odd">
    <td>Device object<br/></td>
    <td>A device object represents a particular audio device. It provides access to the audio device's property store and exposes the audio playback and capture interfaces available on the device. The device object must implement the <a href="https://msdn.microsoft.com/library/windows/desktop/dd371395"><strong>IMMDevice</strong></a> and <a href="https://msdn.microsoft.com/library/windows/desktop/dd371414"><strong>IMMEndpoint</strong></a> interfaces.<br/></td>
    </tr>
    <tr class="even">
    <td>Property store object<br/></td>
    <td>A property store object exposes the properties associated with an audio device. Some of these properties are used by the system, but applications can store arbitrary properties with the audio endpoint as well.<br/> All audio devices have the following three properties:<br/>
    <ul>
    <li><a href="https://msdn.microsoft.com/library/windows/desktop/dd316587"><strong>PKEY_DeviceInterface_FriendlyName</strong></a></li>
    <li><a href="https://msdn.microsoft.com/library/windows/desktop/dd316591"><strong>PKEY_Device_DeviceDesc</strong></a></li>
    <li><a href="https://msdn.microsoft.com/library/windows/desktop/dd316594"><strong>PKEY_Device_FriendlyName</strong></a></li>
    </ul>
    The property store object must implement the <a href="https://go.microsoft.com/fwlink/p/?linkid=177452">IPropertyStore</a> interface.<br/></td>
    </tr>
    </tbody>
    </table>

    

     

2.  The custom endpoint enumerator must be implemented in a DLL that can be loaded into the audio system and other applications. The DLL must be signed so that secure processes can load it. The DLL must implement and export the [**GetTSAudioEndpointEnumeratorForSession**](gettsaudioendpointenumeratorforsession.md) function, which acts as an entry point to the custom endpoint enumerator.

The Remote Desktop Services service calls the [**QueryProperty**](/windows/desktop/api/Wtsprotocol/nf-wtsprotocol-iwtsprotocolconnection-queryproperty) method and sets the *QueryType* parameter to **WTS\_QUERY\_AUDIOENUM\_DLL** to retrieve the name of the enumerator object.

Custom enumerator objects use COM-like interfaces and a COM-like reference counting mechanism, but they are not true COM objects. The custom endpoint enumerator must have the ability to work with legacy audio interfaces used by applications that do not support COM. For this reason, the custom endpoint enumerator must not rely on COM's life cycle management mechanism. Consumers of your audio endpoint enumerator, such as MMDevAPI.dll, load the custom endpoint enumerator DLL when required by user applications, and they will not unload the enumerator while the enumerator holds a reference to a device enumerator object, device collection object, device object, or property store object. It is not possible, however, for these consumers to track references to other types of objects owned by the custom endpoint enumerator. Accordingly, we recommend that your custom endpoint enumerator not create any objects that could outlive these four types of objects.

## To implement a custom audio endpoint

To implement a custom audio device enumerator, you must implement a custom audio endpoint. The way that your custom audio devices are linked is by using the following two statements:

-   `IMMDevice::Activate(IAudioOutputEndpointRT)`
-   `IMMDevice::Activate(IAudioInputEndpointRT)`

We do not expect you to implement the full list of [**IMMDevice::Activate**](https://msdn.microsoft.com/library/windows/desktop/dd371405) interfaces in your custom audio device enumerator. Instead, you should implement [**IAudioOutputEndpointRT**](/windows/desktop/api/Audioengineendpoint/nn-audioengineendpoint-iaudiooutputendpointrt) and [**IAudioInputEndpointRT**](/windows/desktop/api/Audioengineendpoint/nn-audioengineendpoint-iaudioinputendpointrt). You can optionally implement a few more, such as [**IAudioEndpointVolume**](https://msdn.microsoft.com/library/windows/desktop/dd370892). For any interface you do not implement, you should return **E\_NOINTERFACE** (you must use this specific failure code). Windows will then fall back to a stock implementation of the interface (for example, [**IAudioClient2**](https://msdn.microsoft.com/library/windows/desktop/hh404179)).

For additional reference documentation about how to implement and register audio endpoints, see [**IAudioInputEndpointRT**](/windows/desktop/api/Audioengineendpoint/nn-audioengineendpoint-iaudioinputendpointrt). For a diagram that shows how WASAPI works, see [User-Mode Audio Components](https://msdn.microsoft.com/library/windows/desktop/dd316780). Note that all of user-mode audio is new beginning with Windows Server 2008.

## Related topics

<dl> <dt>

[Creating a Remote Desktop Protocol Provider](creating-a-custom-remote-protocol.md)
</dt> <dt>

[**GetTSAudioEndpointEnumeratorForSession**](gettsaudioendpointenumeratorforsession.md)
</dt> <dt>

[**IMMDevice**](https://msdn.microsoft.com/library/windows/desktop/dd371395)
</dt> <dt>

[**IMMDeviceCollection**](https://msdn.microsoft.com/library/windows/desktop/dd371396)
</dt> <dt>

[**IMMDeviceEnumerator**](https://msdn.microsoft.com/library/windows/desktop/dd371399)
</dt> <dt>

[**IMMEndpoint**](https://msdn.microsoft.com/library/windows/desktop/dd371414)
</dt> <dt>

[IPropertyStore](https://go.microsoft.com/fwlink/p/?linkid=177452)
</dt> </dl>

 

 





