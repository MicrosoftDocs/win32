---
description: Encoder API
ms.assetid: 3d19152f-17a3-4576-a2a2-5b827d9ca8d1
title: Encoder API
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Encoder API

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Encoder API provides a uniform interface for configuring software and hardware encoders. Applications can use the Encoder API to configure an encoder and to store the configuration settings. Encoder vendors can use the Encoder API to expose the capabilities of an encoder. Although the Encoder API is designed primarily for encoders, it is general enough that decoders can support it as well.

The Encoder API is exposed to applications through the [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi) interface, which is exposed by the encoder filter. The encoder filter may be a native DirectShow filter, a hardware encoder, or a DirectX Media Object (DMO).

-   Software filters: An encoder that is implemented as a native DirectShow filter should expose the [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi) directly.
-   Hardware encoders: The encoding device is exposed through one or more AVStream minidrivers, which are represented in user mode by KSProxy. KSProxy translates [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi) method calls into KS property sets. For more information, see the DDK documentation.
-   DMOs: The DMO should expose the [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi) interface. DirectShow applications can query the DMO Wrapper filter, which exposes the interface by aggregating the DMO. Applications not based on DirectShow can query the DMO directly.

### Encoder Capabilties

An encoder can register a list of high-level capabilities by storing them in the system registry. Each capability is identified by a GUID. To enumerate the capabilities of a particular encoder, do the following:

1.  Create the moniker that represents the encoder filter. (See [Using the System Device Enumerator](using-the-system-device-enumerator.md).)
2.  Query the filter moniker for the [**IGetCapabilitiesKey**](/windows/desktop/api/Strmif/nn-strmif-igetcapabilitieskey) interface.
3.  Call [**IGetCapabilitiesKey::GetCapabilitiesKey**](/windows/desktop/api/Strmif/nf-strmif-igetcapabilitieskey-getcapabilitieskey). The method returns a handle to the registry key that contains the filter's capabilities list.
4.  Call the **RegEnumValue** function to enumerate the values for the returned key.

If you are devloping an encoder, create the registry entries for the capabilities when the filter is registered. For software filters, create a key named **Capabilities** that is adjacent to the **FilterData** and **FriendlyName** keys. Typically, you would add this information after calling [**AMovieDllRegisterServer2**](amoviedllregisterserver2.md) to register the standard filter data. For more information, see [How to Register DirectShow Filters](how-to-register-directshow-filters.md). Alternatively, you can create a **CapabilitiesLocation** key that contains a string giving the location of the **Capabilities** key in the registry. The string should start with "HKLM\\", "HKCR\\", or "HKCU\\" to indicate the registry subtree. For Plug and Play devices, the driver's setup files should create a **Capabilities** key adjacent to the filter's **FriendlyName** key, or it can use a **CapabilitiesLocation** key as described for software filters.

Once you have created the **Capabilities** key, create a value for each capability GUID. The name of the value should be the string form of the GUID, in the form `{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}`. Each value type should be one of the following:

-   Single numerical value. Use a **DWORD** value.
-   GUID. Use the string form of the GUID.
-   Numeric pairs. Use a string with the form "a,b" to represent pairs of values, such as width and height, or numerator and denominator for fractions.
-   Arrays of values. Use multi-strings (**REG\_SZ\_MULTI**) to represent more than one value.

The following example shows the registry layout for a software filter:


```C++
\HKCR\CLSID\Filter Category\Instance\Filter CLSID\Capabilities\
    
Values: 
    
    guid1: 1234 (REG_DWORD)   
    
    guid2: "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}" (REG_SZ)
    
    guid3: "2","4","6" (REG_SZ_MULTI)
    
    guid4: "720,480" (REG_SZ) 
```



### Encoder Profiles

An *encoder profile* is a fixed list of configuration settings that can be applied to an encoder at run time. Profiles are independent of the encoder; an application can select an encoder, then select a profile and apply the profile settings to the encoder. Profiles are identified by GUID and should be stored in the following location in the registry:


```C++
\HKLM\Software\Microsoft\EncoderProfiles\Profile GUID\
```



where *Profile GUID*

is the string form of the GUID that identifies the profile. Create values for each setting. Also create a string value named "FriendlyName" whose data identifies the profile (such as "LowBandwidthVideo").

## Related topics

<dl> <dt>

[Encoder and Decoder Development](encoder-and-decoder-development.md)
</dt> </dl>

 

 



