---
title: Modifying the Scale Property
description: Modifying the Scale Property
ms.assetid: 32ebaa54-ed13-4b10-8876-bf8e188d7317
keywords:
- Windows Media Player plug-ins,Echo sample properties
- plug-ins,Echo sample properties
- digital signal processing plug-ins,Echo sample properties
- DSP plug-ins,Echo sample properties
- Echo DSP plug-in sample,scale property
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Modifying the Scale Property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The default wizard implementation exposes the scale property. You can change the existing implementation to expose the delay time property instead.

First, use the following example to change the function prototypes for get\_scale and put\_scale in Echo.h. Change the name of the methods and the data types for the parameters:


```C++
// IEcho methods
STDMETHOD(get_delay)(DWORD *pVal);
STDMETHOD(put_delay)(DWORD newVal);

```



Next, change the implementations of the get\_scale and put\_scale methods in Echo.cpp. Make the code match the following examples:


```C++
// Formerly get_scale
STDMETHODIMP CEcho::get_delay(DWORD *pVal)
{
    if ( NULL == pVal )
    {
        return E_POINTER;
    }

    *pVal = m_dwDelayTime;

    return S_OK;
}

// Formerly put_scale
STDMETHODIMP CEcho::put_delay(DWORD newVal)
{
    m_dwDelayTime = newVal;

    return S_OK;
}

```



The preceding example code changes the method names and the parameter data types. The member variable name should have been changed previously. Remember to change the comments that introduce each method as well.

Now, change the interface definition. The following code replaces the code in the IEcho interface declaration in Echo.idl:


```C++
HRESULT get_delay([out] DWORD *pVal);
HRESULT put_delay([in] DWORD newVal);

```



## Related topics

<dl> <dt>

[**Echo Sample Properties**](echo-sample-properties.md)
</dt> </dl>

 

 




