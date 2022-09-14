---
description: Synchronized Accessible Media Interchange (SAMI) is a format for adding captions to digital media.
ms.assetid: 007c8181-089e-4e56-a31d-9d1942f90b07
title: SAMI Media Source
ms.topic: article
ms.date: 05/31/2018
---

# SAMI Media Source

Synchronized Accessible Media Interchange (SAMI) is a format for adding captions to digital media. The captions are stored in a separate text file with the file name extension .smi or .sami.

In Media Foundation, SAMI caption files are supported through the SAMI media source. Use the [Source Resolver](source-resolver.md) to create an instance of the SAMI media source from a URL or byte stream. Media Foundation does not provide a component that displays SAMI captions. The application must interpret the caption data that it receives from the SAMI media source.

The following shows an example SAMI file.

``` syntax
<SAMI>
<HEAD>
    <STYLE TYPE="text/css">
    <!--
    P {
        font-family: Arial;
        background: #000000;
        text-align: center;
        }

#standard {Name: Standard; color: #FFFFFF; font-size: 14pt; } 
#hilite {Name: Youth; color: greenyellow; font-size: 18pt;}

    .ENUSCC { Name: English; lang: EN-US-CC; }
    .FRFRCC { Name: French; lang: fr-FR; } 

    -->
    </STYLE>
</HEAD>
<BODY>
    <SYNC Start="0">
        <P Class="ENUSCC">The <I>first</I> caption.</P>
        <P Class="FRFRCC">Un</P>
    </SYNC>
    <SYNC Start="3000">
        <P Class="ENUSCC">The <I>second</I> caption.</P>
        <P Class="FRFRCC">Deux</P>
    </SYNC>
    <SYNC Start="5000">
        <P Class="ENUSCC">The <I>third</I> caption.</P>
        <P Class="FRFRCC">Trois</P>
    </SYNC>
</BODY>
</SAMI>
```

The `<STYLE>` element contains style information. This example contains a base style for `<P>` elements, along with two named styles, "standard" and "hilite". The named styles are used to modify the base style. Captions are placed within `<SYNC>` elements. The start attribute gives the presentation time in milliseconds for that caption. The captions in this example are given in two languages, specified by their RFC-1766 language tags, "en-US" and "fr -FR". Within the captions, languages are identified by their class names; in this case, "ENUSCC" and "FRFRCC".

The SAMI media source creates one media stream for each language. By default, the first stream is selected and the remaining streams are deselected. The application can change the stream selection by calling [**IMFPresentationDescriptor::SelectStream**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-selectstream) and [**IMFPresentationDescriptor::DeselectStream**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-deselectstream). Each stream descriptor contains the following attributes.



| Attribute                                                       | Description                                      |
|-----------------------------------------------------------------|--------------------------------------------------|
| [**MF\_SD\_LANGUAGE**](mf-sd-language-attribute.md)            | Language tag, as given by the `lang` attribute.  |
| [**MF\_SD\_SAMI\_LANGUAGE**](mf-sd-sami-language-attribute.md) | Language name, as given by the `Name` attribute. |



 

Each stream has the following media type:



| Attribute                                                                            | Value                 |
|--------------------------------------------------------------------------------------|-----------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md)                            | **MFMediaType\_SAMI** |
| [**MF\_MT\_ALL\_SAMPLES\_INDEPENDENT**](mf-mt-all-samples-independent-attribute.md) | **TRUE**              |



 

The SAMI source delivers each caption in a separate media sample. The sample time stamp and duration are derived from the `<SYNC>` element. The media buffer contained in the sample holds the caption as ASCII text. The caption style is embedded in the caption as an inline `STYLE` attribute. For example, given the previous SAMI file, and using the English-language stream with the default styles, the first media buffer would contain the following data. (The line breaks might differ from what is shown here.)

``` syntax
<P STYLE="
    font-family: Arial;
    background: #000000;
    text-align: center;
    Name: English; lang: EN-US-CC;  
    Name: Standard; color: #FFFFFF; 
    font-size: 14pt; ">The<I>first</I> caption.
```

## SAMI Styles

To change the current style, use the [**IMFSAMIStyle**](/windows/desktop/api/mfidl/nn-mfidl-imfsamistyle) interface. This interface is obtained by calling [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) on the SAMI media source. (If you are using the SAMI media source with the Media Session, call **GetService** on the Media Session.) The service identifier is **MF\_SAMI\_SERVICE**.

The following example sets the current SAMI style, specified by index.


```C++
HRESULT SetSAMIStyleByIndex(IMFMediaSource *pSource, DWORD index)
{
    IMFSAMIStyle *pSami = NULL;

    DWORD cStyles;
    PROPVARIANT varStyles;

    HRESULT hr = MFGetService(pSource, MF_SAMI_SERVICE, IID_PPV_ARGS(&pSami));
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pSami->GetStyleCount(&cStyles);
    if (FAILED(hr))
    {
        goto done;
    }

    if (index >= cStyles)
    {
        hr = E_INVALIDARG;
        goto done;
    }

    hr = pSami->GetStyles(&varStyles);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pSami->SetSelectedStyle(varStyles.calpwstr.pElems[index]);

done:
    PropVariantClear(&varStyles);
    SafeRelease(&pSami);
    return hr;
}
```



This example calls the following methods on the SAMI media source:

-   [**IMFSAMIStyle::GetStyleCount**](/windows/desktop/api/mfidl/nf-mfidl-imfsamistyle-getstylecount) gets the number of styles.
-   [**IMFSAMIStyle::GetStyles**](/windows/desktop/api/mfidl/nf-mfidl-imfsamistyle-getstyles) gets a list of the style names, stored in a **PROPVARIANT**.
-   [**IMFSAMIStyle::SetSelectedStyle**](/windows/desktop/api/mfidl/nf-mfidl-imfsamistyle-setselectedstyle) sets a style by name.

The list of style names is also stored on the presentation descriptor, in the [**MF\_PD\_SAMI\_STYLELIST**](mf-pd-sami-stylelist-attribute.md) attribute.

## Related topics

<dl> <dt>

[Media Sources and Sinks](media-sources-and-sinks.md)
</dt> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> </dl>

 

 



