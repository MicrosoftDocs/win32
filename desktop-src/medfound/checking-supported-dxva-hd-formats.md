---
Description: '.'
ms.assetid: '43ae9f70-34a1-48ca-be61-e974e2daebd7'
title: 'Checking Supported DXVA-HD Formats'
---

# Checking Supported DXVA-HD Formats

## Checking Supported Input Formats

To get a list of the input formats that the Microsoft DirectX Video Acceleration High Definition (DXVA-HD) device supports, do the following:

1.  Call [**IDXVAHD\_Device::GetVideoProcessorDeviceCaps**](idxvahd-device-getvideoprocessordevicecaps.md) to get the device capabilities.
2.  Check the **InputFormatCount** member of the [**DXVAHD\_VPDEVCAPS**](dxvahd-vpdevcaps.md) structure. This member gives the number of supported input formats.
3.  Allocate an array of **D3DFORMAT** values, of size **InputFormatCount**.
4.  Pass this array to the [**IDXVAHD\_Device::GetVideoProcessorInputFormats**](idxvahd-device-getvideoprocessorinputformats.md) method. The methods fills the array with a list of input formats.

The following code shows these steps:


```C++
// Checks whether a DXVA-HD device supports a specified input format.

HRESULT CheckInputFormatSupport(
    IDXVAHD_Device          *pDXVAHD,
    const DXVAHD_VPDEVCAPS&amp; caps,
    D3DFORMAT               d3dformat
    )
{
    D3DFORMAT *pFormats = new (std::nothrow) D3DFORMAT[ caps.InputFormatCount ];
    if (pFormats == NULL)
    {
        return E_OUTOFMEMORY;
    }

    HRESULT hr = pDXVAHD->GetVideoProcessorInputFormats(
        caps.InputFormatCount, 
        pFormats
        );

    if (FAILED(hr)) 
    { 
        goto done; 
    }

    UINT index;
    for (index = 0; index < caps.InputFormatCount; index++)
    {
        if (pFormats[index] == d3dformat)
        {
            break;
        }
    }
    if (index == caps.InputFormatCount)
    {
        hr = E_FAIL;
    }

done:
    delete [] pFormats;
    return hr;
}
```



## Checking Supported Output Formats

To get a list of the output formats that the DXVA-HD device supports, do the following:

1.  Call [**IDXVAHD\_Device::GetVideoProcessorDeviceCaps**](idxvahd-device-getvideoprocessordevicecaps.md) to get the device capabilities.
2.  Check the **OutputFormatCount** member of the [**DXVAHD\_VPDEVCAPS**](dxvahd-vpdevcaps.md) structure. This member gives the number of supported input formats.
3.  Allocate an array of **D3DFORMAT** values, of size **OutputFormatCount**.
4.  Pass this array to the [**IDXVAHD\_Device::GetVideoProcessorOutputFormats**](idxvahd-device-getvideoprocessoroutputformats.md) method. The methods fills the array with a list of output formats.

The following code shows these steps:


```C++
// Checks whether a DXVA-HD device supports a specified output format.

HRESULT CheckOutputFormatSupport(
    IDXVAHD_Device          *pDXVAHD,
    const DXVAHD_VPDEVCAPS&amp; caps,
    D3DFORMAT               d3dformat
    )
{
    D3DFORMAT *pFormats = new (std::nothrow) D3DFORMAT[caps.OutputFormatCount];
    if (pFormats == NULL)
    {
        return E_OUTOFMEMORY;
    }

    HRESULT hr = pDXVAHD->GetVideoProcessorOutputFormats(
        caps.OutputFormatCount, 
        pFormats
        );

    if (FAILED(hr)) 
    { 
        goto done; 
    }

    UINT index;
    for (index = 0; index < caps.OutputFormatCount; index++)
    {
        if (pFormats[index] == d3dformat)
        {
            break;
        }
    }
    if (index == caps.OutputFormatCount)
    {
        hr = E_FAIL;
    }

done:
    delete [] pFormats;
    return hr;
}
```



## Related topics

<dl> <dt>

[DXVA-HD](dxva-hd.md)
</dt> </dl>

 

 



